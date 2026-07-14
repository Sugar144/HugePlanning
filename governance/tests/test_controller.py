#!/usr/bin/env python3
"""Offline deterministic tests for Phase 2 Controller foundations."""

from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import zipfile

import yaml
from jsonschema import Draft202012Validator

REPO = Path(__file__).resolve().parents[2]
GOV = REPO / "governance"
TOOLS = GOV / "tools"
sys.path.insert(0, str(TOOLS))

from _lib.atomic import write_new
from _lib.canonical import sha256_bytes
from _lib.safe_zip import ZipLimits, inspect
from _lib.strict_yaml import StrictYAMLError, load, load_bytes
from apply_loop_transition import blocking_signature, calculate
from validate_closure_loop import validate_loop
from validate_run_package import validate_package

GEN_SPEC = importlib.util.spec_from_file_location("package_cases", GOV / "tests/fixtures/packages/generate_cases.py")
GEN = importlib.util.module_from_spec(GEN_SPEC); GEN_SPEC.loader.exec_module(GEN)
LOOP = GOV / "methodology/loops/kernel-design-closure/kernel-design-closure-loop-v0.1.0.yaml"
LOOP_SCHEMA = GOV / "schemas/kernel-design-closure-loop.schema.json"
ENVELOPE = GOV / "runs/KGR-005-kernel-adversary-targeted-closure/input-envelope.yaml"
PROMPT = GOV / "runs/KGR-005-kernel-adversary-targeted-closure/prompt/05-kernel-adversary-targeted-closure-prompt-sol-high-v0.1.0.md"
LOOP_SNAPSHOT = GOV / "runs/KGR-005-kernel-adversary-targeted-closure/control/kernel-design-closure-loop-v0.1.0.yaml"
ZIP = Path("/home/sugar/Downloads/KGR-005-formal-input-package.zip")


class SchemaAndLoopTests(unittest.TestCase):
    def test_all_schemas_are_draft_2020_12_valid(self):
        for path in sorted((GOV / "schemas").rglob("*.schema.json")):
            schema = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
            Draft202012Validator.check_schema(schema)

    def test_canonical_loop_and_bound_protocols(self):
        adversary = (GOV / "methodology/roles/kernel-adversary/protocols/targeted-closure/05-kernel-adversary-targeted-closure-prompt-sol-high-v0.1.0.md").read_text()
        designer = (GOV / "methodology/roles/kernel-designer/protocols/closure-remediation/06-kernel-designer-closure-remediation-prompt-sol-high-v0.1.0.md").read_text()
        self.assertEqual(validate_loop(load(LOOP), LOOP_SCHEMA, adversary, designer), [])

    def test_static_mutation_matrix(self):
        base = load(LOOP); matrix = load(GOV / "tests/fixtures/loop-mutations/invariants.yaml")
        self.assertGreaterEqual(len(matrix["mutations"]), 27)
        for fixture in matrix["mutations"]:
            data = deepcopy(base); path = fixture["path"].split("."); parent = data
            for part in path[:-1]: parent = parent[int(part)] if isinstance(parent, list) else parent[part]
            key = int(path[-1]) if isinstance(parent, list) else path[-1]
            operation = fixture.get("operation")
            if operation == "remove_last": parent[key].pop()
            elif operation == "remove_targeted_sources": parent[key] = [x for x in parent[key] if x["from"] != "TARGETED_CLOSURE_IN_PROGRESS"]
            elif operation == "remove_package_conflict": parent[key].remove("BLOCKED_BY_PACKAGE_CONFLICT")
            elif operation == "remove_invalid_output": parent[key].remove("INVALID_OUTPUT_PACKAGE")
            elif operation == "remove_invalid_import": parent[key].remove("INVALID_IMPORT")
            else: parent[key] = fixture["value"]
            codes = {d.code for d in validate_loop(data, LOOP_SCHEMA, None, None)}
            self.assertIn(fixture["expected_diagnostic"], codes, fixture["id"])

    def test_duplicate_yaml_key_and_unknown_version(self):
        with self.assertRaises(StrictYAMLError): load_bytes(b"a: 1\na: 2\n")
        data = load(LOOP); data["loop"]["version"] = "9.9.9"
        self.assertIn("UNSUPPORTED_LOOP_VERSION", {d.code for d in validate_loop(data, LOOP_SCHEMA, None, None)})


class PackageSecurityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.root = Path(self.temp.name); self.cases = GEN.generate(self.root)
    def tearDown(self): self.temp.cleanup()

    def test_zip_security_cases(self):
        expected = {"duplicate_normalized":"ZIP_UNSAFE_PATH","traversal":"ZIP_UNSAFE_PATH","absolute":"ZIP_UNSAFE_PATH","backslash":"ZIP_UNSAFE_PATH","symlink":"ZIP_UNSAFE_FILE_TYPE","device":"ZIP_UNSAFE_FILE_TYPE","encrypted":"ZIP_ENCRYPTED"}
        for name, code in expected.items(): self.assertIn(code, {d.code for d in inspect(self.cases[name])[1]}, name)
        self.assertIn("ZIP_MEMBER_LIMIT", {d.code for d in inspect(self.cases["excessive_members"], ZipLimits(max_members=2))[1]})
        self.assertIn("ZIP_MEMBER_SIZE_LIMIT", {d.code for d in inspect(self.cases["excessive_size"], ZipLimits(max_member_bytes=10))[1]})
        self.assertIn("ZIP_TOTAL_SIZE_LIMIT", {d.code for d in inspect(self.cases["extra_member"], ZipLimits(max_total_bytes=1))[1]})
        self.assertIn("ZIP_COMPRESSION_RATIO_LIMIT", {d.code for d in inspect(self.cases["excessive_ratio"], ZipLimits(max_compression_ratio=2))[1]})

    @unittest.skipUnless(ZIP.is_file(), "external KGR-005 package unavailable")
    def test_real_kgr_005_isolated_and_preparation(self):
        facts, diags = validate_package("isolated-input","adversary",ZIP,ENVELOPE,PROMPT,LOOP_SNAPSHOT)
        self.assertEqual(diags, []); self.assertEqual(facts["member_count"],19); self.assertEqual(facts["package_sha256"],"26291b32594f2b73e12107bec9572b528e4ec3e32e4ca08f9746c5aba1adf9cf")
        _, diags = validate_package("preparation","adversary",ZIP,ENVELOPE,PROMPT,LOOP_SNAPSHOT)
        self.assertEqual(diags, [])

    @unittest.skipUnless(ZIP.is_file(), "external KGR-005 package unavailable")
    def test_member_integrity_mutations(self):
        with zipfile.ZipFile(ZIP) as source: original = [(x.filename, source.read(x)) for x in source.infolist()]
        for name, entries, code in [
            ("missing", original[:-1], "PACKAGE_MEMBER_MISSING"),
            ("extra", original + [("extra.txt",b"x")], "PACKAGE_MEMBER_EXTRA"),
            ("wrong", [(n,(b"wrong" if i==1 else d)) for i,(n,d) in enumerate(original)], "PACKAGE_MEMBER_HASH_MISMATCH")]:
            path = GEN.write_zip(self.root/f"{name}.zip", entries)
            _, diags=validate_package("isolated-input","adversary",path,ENVELOPE,PROMPT,LOOP_SNAPSHOT)
            self.assertIn(code,{d.code for d in diags})

    def test_invalid_utf8_duplicate_yaml_and_identity_mismatch(self):
        for case in ("invalid_utf8","duplicate_yaml_key"):
            _, diags=inspect(self.cases[case]); self.assertEqual(diags,[])
            members,_=inspect(self.cases[case])
            with self.assertRaises(StrictYAMLError): load_bytes(members["data.yaml"])
        bad = self.root / "prompt.md"; bad.write_text("wrong",encoding="utf-8")
        if ZIP.is_file():
            _, diags=validate_package("isolated-input","adversary",ZIP,ENVELOPE,bad,LOOP_SNAPSHOT)
            self.assertIn("PROMPT_ENVELOPE_IDENTITY_MISMATCH",{d.code for d in diags})

    @unittest.skipUnless(ZIP.is_file(), "external KGR-005 package unavailable")
    def test_stage_path_responsibilities_and_loop_mismatch(self):
        envelope_data=load(ENVELOPE)
        for entry in [x for section in ("current_proposal","original_review","predecessor_kernel") for x in envelope_data["input_envelope"][section]["artifacts"]]:
            entry.pop("path"); entry.pop("source_path")
        envelope_data["input_envelope"]["loop_control"].pop("path"); envelope_data["input_envelope"]["loop_control"].pop("source_path")
        isolated_envelope=self.root/"isolated-envelope.yaml"
        isolated_envelope.write_text(yaml.safe_dump(envelope_data,sort_keys=False),encoding="utf-8")
        with zipfile.ZipFile(ZIP) as source:
            entries=[(x.filename,(isolated_envelope.read_bytes() if x.filename=="input-envelope.yaml" else source.read(x))) for x in source.infolist()]
        package=GEN.write_zip(self.root/"isolated.zip",entries)
        _,diags=validate_package("isolated-input","adversary",package,isolated_envelope,PROMPT,LOOP_SNAPSHOT)
        self.assertEqual(diags,[])
        _,diags=validate_package("preparation","adversary",package,isolated_envelope,PROMPT,LOOP_SNAPSHOT)
        self.assertIn("PREPARATION_PATH_MISSING",{d.code for d in diags})
        wrong_loop=self.root/"loop.yaml"; wrong_loop.write_text("loop: {id: GOV-LOOP-001, version: 0.1.0}\n",encoding="utf-8")
        _,diags=validate_package("isolated-input","adversary",ZIP,ENVELOPE,PROMPT,wrong_loop)
        self.assertIn("LOOP_SNAPSHOT_MISMATCH",{d.code for d in diags})

    def test_output_schema_failure_and_import_custody_mismatch(self):
        output = self.root/"output.zip"
        entries=[(name,b"x") for name in ["00-targeted-closure-basis.md","02-targeted-adversarial-scenarios.md","03-regression-and-new-findings.md","04-markdown-yaml-parity-review.md","05-residual-risk-and-routing.md","07-targeted-closure-summary-and-handoff.md"]]
        entries += [("01-finding-closure-verdicts.yaml",b"finding_closure_verdicts: {}\n"),("06-closure-result.yaml",b"closure_result: {}\n")]
        GEN.write_zip(output,entries)
        _,diags=validate_package("output","adversary",output,ENVELOPE,None,None)
        self.assertIn("SCHEMA_VALIDATION_FAILED",{d.code for d in diags})
        custody=self.root/"custody.txt"; custody.write_bytes(b"different")
        env=self.root/"designer-envelope.yaml"
        env.write_text(f"execution_contract:\n  role: Kernel Designer\n  mode: CLOSURE_REMEDIATION\n  protocol_id: GOV-PROTOCOL-003\n  protocol_version: 0.1.0\n  target_run: KGR-006\nexpected_output_members: [result.yaml]\nformal_inputs:\n  artifacts:\n    - package_member: result.yaml\n      sha256: {sha256_bytes(b'package')}\n      import_path: {custody}\n",encoding="utf-8")
        package=GEN.write_zip(self.root/"import.zip",[("result.yaml",b"package")])
        _,diags=validate_package("import","designer",package,env,None,None)
        self.assertIn("IMPORT_CUSTODY_MISMATCH",{d.code for d in diags})


class TransitionTests(unittest.TestCase):
    def test_all_twenty_fixtures(self):
        paths=sorted((GOV/"tests/fixtures/transitions").glob("*.yaml")); self.assertEqual(len(paths),20)
        with tempfile.TemporaryDirectory() as td:
            for path in paths:
                data=load(path); record,diags,_=calculate("import",LOOP,data["source_run"],data,Path(td)/"history",None,False)
                expected=data["expected_diagnostic"]
                if expected: self.assertIn(expected,{d.code for d in diags},path.name)
                else: self.assertEqual(diags,[],path.name)
                self.assertEqual(record["counters_after"],data["expected_counters_after"],path.name)
                self.assertEqual(record["resulting_state"],data["expected_transition"],path.name)
                self.assertEqual(record["next_role"],data["expected_next_role"],path.name)
                self.assertEqual(record["next_mode"],data["expected_next_mode"],path.name)

    def test_signature_order_determinism(self):
        a=[{"finding_id":"KA-F-020","severity":"HIGH","adversary_verdict":"REOPENED","failed_criteria":["b","a"],"relationships":[{"type":"REGRESSION_OF","finding_id":"KA-F-002"}]},{"finding_id":"KA-F-019","severity":"MEDIUM","adversary_verdict":"NEW"}]
        b=[deepcopy(a[1]),deepcopy(a[0])]; b[1]["failed_criteria"].reverse()
        self.assertEqual(blocking_signature(a),blocking_signature(b))

    def test_no_progress_guard_from_replayed_history(self):
        finding={"finding_id":"KA-F-003","adversary_verdict":"REOPENED","original_severity":"HIGH"}
        signature=blocking_signature([finding])[0]
        data=load(GOV/"tests/fixtures/transitions/17-no-progress-signature.yaml")
        data["history"]=[
            {"source_run":"KGR-005","source_role":"Kernel Adversary","previous_state":"READY_FOR_TARGETED_CLOSURE","counters_before":dict(completed_targeted_closure_runs=0,completed_designer_remediation_runs=0),"counters_after":dict(completed_targeted_closure_runs=1,completed_designer_remediation_runs=0),"resulting_state":"DESIGNER_REMEDIATION_REQUIRED","guards":{"blocking_finding_signature":signature,"blocking_finding_count":1}},
            {"source_run":"KGR-006","source_role":"Kernel Designer","previous_state":"DESIGNER_REMEDIATION_REQUIRED","counters_before":dict(completed_targeted_closure_runs=1,completed_designer_remediation_runs=0),"counters_after":dict(completed_targeted_closure_runs=1,completed_designer_remediation_runs=1),"resulting_state":"READY_FOR_TARGETED_CLOSURE"},
            {"source_run":"KGR-007","source_role":"Kernel Adversary","previous_state":"READY_FOR_TARGETED_CLOSURE","counters_before":dict(completed_targeted_closure_runs=1,completed_designer_remediation_runs=1),"counters_after":dict(completed_targeted_closure_runs=2,completed_designer_remediation_runs=1),"resulting_state":"DESIGNER_REMEDIATION_REQUIRED","guards":{"blocking_finding_signature":signature,"blocking_finding_count":1}},
            {"source_run":"KGR-008","source_role":"Kernel Designer","previous_state":"DESIGNER_REMEDIATION_REQUIRED","counters_before":dict(completed_targeted_closure_runs=2,completed_designer_remediation_runs=1),"counters_after":dict(completed_targeted_closure_runs=2,completed_designer_remediation_runs=2),"resulting_state":"READY_FOR_TARGETED_CLOSURE"},
        ]
        record,diags,_=calculate("import",LOOP,"KGR-009",data,Path("/nonexistent"),None,False)
        self.assertEqual(diags,[]); self.assertIn("NO_PROGRESS",record["guards"]["exhausted"])

    def test_missing_active_invalid_result_and_wrong_role(self):
        base=load(GOV/"tests/fixtures/transitions/01-valid-kgr-005-closure-confirmed.yaml")
        for mutate,code in [(lambda x:x.update(input_state="READY_FOR_TARGETED_CLOSURE"),"ACTIVE_STATE_EVIDENCE_MISSING"),(lambda x:x.update(input_result="UNKNOWN"),"RESULT_ENUM_INVALID"),(lambda x:x.update(source_role="designer"),"ROLE_MODE_MISMATCH")]:
            data=deepcopy(base); mutate(data); _,diags,_=calculate("import",LOOP,"KGR-005",data,Path("/nonexistent"),None,False); self.assertIn(code,{d.code for d in diags})
        wrapper={"controller_import":{"source_role":"adversary","source_mode":"TARGETED_CLOSURE","active_state_evidence":{"source_run":"KGR-005","state":"TARGETED_CLOSURE_IN_PROGRESS","execution_started":True,"evidence_ref":"synthetic-active-evidence"},"role_result":{"input_result":"CLOSURE_CONFIRMED"}}}
        record,diags,_=calculate("import",LOOP,"KGR-005",wrapper,Path("/nonexistent"),None,False)
        self.assertEqual(diags,[]); self.assertEqual(record["previous_state"],"TARGETED_CLOSURE_IN_PROGRESS")

    def test_history_fork_event_and_reentry_contracts(self):
        data=load(GOV/"tests/fixtures/transitions/01-valid-kgr-005-closure-confirmed.yaml")
        data["history"]=[{"source_run":"KGR-004","counters_before":{"completed_targeted_closure_runs":1,"completed_designer_remediation_runs":0}}]
        _,diags,_=calculate("import",LOOP,"KGR-005",data,Path("/nonexistent"),None,False)
        self.assertIn("HISTORY_FORK",{d.code for d in diags})
        duplicate=deepcopy(data); duplicate["history"]=[{"source_run":"KGR-005","previous_state":"READY_FOR_TARGETED_CLOSURE","counters_before":{"completed_targeted_closure_runs":0,"completed_designer_remediation_runs":0},"counters_after":{"completed_targeted_closure_runs":0,"completed_designer_remediation_runs":0},"resulting_state":"TARGETED_CLOSURE_IN_PROGRESS"}]
        _,diags,_=calculate("import",LOOP,"KGR-005",duplicate,Path("/nonexistent"),None,False)
        self.assertIn("DUPLICATE_SOURCE_RUN_TRANSITION",{d.code for d in diags})
        event={"typed_event":"TARGETED_CLOSURE_EXECUTION_BEGAN"}
        record,diags,_=calculate("event",LOOP,"KGR-005",event,Path("/nonexistent"),None,False)
        self.assertEqual(diags,[]); self.assertEqual(record["resulting_state"],"TARGETED_CLOSURE_IN_PROGRESS")
        history=self.root_history("OWNER_DECISION_REQUIRED")
        reentry={"resulting_state":"READY_FOR_TARGETED_CLOSURE","artifact":{"id":"OWNER-DECISION-TEST","applicable":True}}
        record,diags,_=calculate("reenter",LOOP,"KGR-006",reentry,history,None,False)
        self.assertEqual(diags,[]); self.assertEqual(record["resulting_state"],"READY_FOR_TARGETED_CLOSURE")
        reentry["artifact"]["applicable"]=False
        _,diags,_=calculate("reenter",LOOP,"KGR-006",reentry,history,None,False)
        self.assertIn("REENTRY_ARTIFACT_INVALID",{d.code for d in diags})

    def root_history(self, resulting_state):
        data={"history":[{"source_run":"KGR-005","previous_state":"READY_FOR_TARGETED_CLOSURE","counters_before":{"completed_targeted_closure_runs":0,"completed_designer_remediation_runs":0},"counters_after":{"completed_targeted_closure_runs":1,"completed_designer_remediation_runs":0},"resulting_state":resulting_state}]}
        td=tempfile.TemporaryDirectory(); self.addCleanup(td.cleanup)
        target=Path(td.name)/"KGR-005/controller"; target.mkdir(parents=True)
        (target/"controller-transition.json").write_text(json.dumps(data["history"][0]),encoding="utf-8")
        return Path(td.name)

    def test_missing_authorization_exit_3_apply_and_overwrite(self):
        fixture=GOV/"tests/fixtures/transitions/01-valid-kgr-005-closure-confirmed.yaml"
        with tempfile.TemporaryDirectory() as td:
            cmd=[sys.executable,str(TOOLS/"apply_loop_transition.py"),"import","--loop",str(LOOP),"--source-run","KGR-005","--input",str(fixture),"--history-root",td,"--apply","--json"]
            self.assertEqual(subprocess.run(cmd,capture_output=True).returncode,3)
            cmd += ["--authorization-ref","TEST-AUTH"]
            self.assertEqual(subprocess.run(cmd,capture_output=True).returncode,0)
            target=Path(td)/"KGR-005/controller/controller-transition.json"; self.assertTrue(target.is_file()); self.assertTrue(target.read_bytes().endswith(b"\n"))
            self.assertEqual(subprocess.run(cmd,capture_output=True).returncode,1)

    def test_atomic_failure_leaves_no_partial_target(self):
        with tempfile.TemporaryDirectory() as td:
            target=Path(td)/"record.json"
            with mock.patch("_lib.atomic.os.replace",side_effect=OSError("injected")):
                with self.assertRaises(OSError): write_new(target,b"{}\n")
            self.assertFalse(target.exists()); self.assertEqual(list(Path(td).iterdir()),[])


if __name__ == "__main__": unittest.main(verbosity=2)
