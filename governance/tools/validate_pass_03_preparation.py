#!/usr/bin/env python3
"""Validate the bounded, unexecuted GOV-AUD-001 PASS-03 preparation package."""
from __future__ import annotations
import hashlib
from pathlib import Path
import sys
import subprocess
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib.strict_yaml import load

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'governance/audits/GOV-AUD-001-gov7-enablement/passes/PASS-03'
REQUIRED = {'contract.yaml','preparation-input-manifest.yaml','output-artifact-specification.yaml','validation-plan.yaml','adversarial-review-plan.yaml','custody-and-publication-requirements.md'}
OUTPUTS = {'observable-event-requirements','evidence-and-authority-model','learning-lifecycle-and-state-machine','candidate-routing-and-promotion-model','selective-retrieval-requirements','effectiveness-and-burden-metrics','privacy-retention-and-rollback-requirements','tooling-neutral-capability-model','risks-open-questions-and-pass-04-handoff'}
def main():
    errors=[]
    if {p.name for p in BASE.iterdir() if p.is_file()} & REQUIRED != REQUIRED: errors.append('required PASS-03 preparation artifacts missing')
    contract=load(BASE/'contract.yaml')['pass']
    if contract.get('status') != 'PREPARED_VALIDATED_PENDING_PROJECT_OWNER_EXECUTION_AUTHORIZATION': errors.append('preparation status mismatch')
    if contract.get('contract_identity',{}).get('contract_id') != 'GOV-AUD-001-PASS-03-CONTRACT': errors.append('contract identity mismatch')
    if set(contract.get('required_outputs',[])) != OUTPUTS: errors.append('required output set mismatch')
    if contract.get('verification_states') != ['HYPOTHESIS_PENDING_VERIFICATION','CONFIRMED','REFUTED','PARTIALLY_CONFIRMED','UNRESOLVED']: errors.append('verification state mismatch')
    forbidden=' '.join(contract.get('exclusions',[])).lower()
    if 'hidden chain-of-thought' not in forbidden or 'tool' not in forbidden: errors.append('required prohibitions missing')
    manifest=load(BASE/'preparation-input-manifest.yaml')['manifest']
    for item in manifest.get('inputs',[]):
        p=ROOT / item['path']
        result=subprocess.run(['git','-C',str(ROOT),'show','HEAD:'+item['path']], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False)
        actual=hashlib.sha256(result.stdout).hexdigest() if result.returncode == 0 else (hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None)
        if actual != item.get('sha256'): errors.append('input hash mismatch: '+item['path'])
    spec=load(BASE/'output-artifact-specification.yaml')['output_specification']
    if {x.get('name') for x in spec.get('artifacts',[])} != OUTPUTS: errors.append('output specification mismatch')
    attacks=load(BASE/'adversarial-review-plan.yaml')['adversarial_review_plan'].get('attacks',[])
    if len(attacks) != 13: errors.append('adversarial attack coverage mismatch')
    print('VALID' if not errors else 'INVALID: '+ '; '.join(errors))
    return 0 if not errors else 1
if __name__ == '__main__': raise SystemExit(main())
