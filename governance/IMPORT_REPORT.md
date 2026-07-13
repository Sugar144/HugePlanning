# GOV-0 Import Report

Import date: 2026-07-13
Bootstrap base commit: `3246b6849d370c8098ce53caa28fa6dd3c34846d`
Branch: `governance/bootstrap-v0.1`
Discovered inbox files: 32
Imported inbox files: 32
Archive-only members additionally extracted: 2
Raw checksum entries: 34

## Environment and limitations

This bootstrap was executed by a Codex workspace agent in a GPT-5-family environment. The exact model identifier, reasoning-mode setting, token usage, and interaction accounting are not exposed to this repository task and are therefore not recorded as facts. Network access was not required. Prior chat transcripts and Basic Memory were intentionally not inspected.

The initial Git checks established remote `https://github.com/Sugar144/HugePlanning.git`, branch `governance/bootstrap-v0.1`, HEAD/base `3246b6849d370c8098ce53caa28fa6dd3c34846d`, upstream `origin/main`, a clean tracked tree, and a separate S1 worktree on `feat/s1-discovery-interviewer`.

## Per-input inventory

All hashes below were calculated before import. Post-import equality is covered by `SOURCE_CHECKSUMS.sha256` and validation. “ZIP duplicate” means byte identity with the named archive member, not merely a similar filename.

| Original relative path | Type / bytes | SHA-256 | Category / likely run | Relationship and confidence | Import action |
|---|---:|---|---|---|---|
| `_governance_inbox/hugeplanning-governance-bootstrap-codex-prompt-v0.2.md` | UTF-8 Markdown / 23685 | `643bceedc48422e9e9659731dba35720a0c903df962670f25dbbce2d73a7282b` | role prompt / GOV-0 | Exact member of Codex v0.2 ZIP; high | Moved byte-exact to `sources/raw/prompts/` |
| `_governance_inbox/hugeplanning-governance-bootstrap-prompt-pack-v0.1.zip` | ZIP / 39393 | `09233fdfab6907337a15d469a6eed6b4b5088a1d6c4f2c7ec3a3224691efab7b` | archive / governance role prompts | Original package; high | Moved byte-exact to `sources/raw/packages/`; safely tested |
| `_governance_inbox/hugeplanning-governance-bootstrap-prompt-pack-v0.1/00-worktree-setup-fish.md` | ASCII Markdown / 2255 | `f408a89130cd0558c7ec6291cd9a2080990f5d69912d722c76f296d6d4fc2d96` | process note / GOV-0 | ZIP duplicate; high | Moved byte-exact with extracted package |
| `_governance_inbox/hugeplanning-governance-bootstrap-prompt-pack-v0.1/01-kernel-intake-interviewer-prompt-canonical-v0.1.md` | UTF-8 Markdown / 31330 | `0500378df9b6986b0afae3e2679a99a8361aa105ee3aa79d13c227312f717195` | role prompt / KGR-001 | ZIP duplicate; explicitly reconstructed completion; high | Moved raw; exact run copy created |
| `_governance_inbox/hugeplanning-governance-bootstrap-prompt-pack-v0.1/02-kernel-designer-prompt-sol-high-v0.1.md` | UTF-8 Markdown / 20830 | `c82127c9bac88fe7fe1f20e0c672deddbc155684ce5314683d1047a086da0455` | role prompt / KGR-002 | ZIP duplicate; exact Designer prompt; high | Moved raw; exact run copy created |
| `_governance_inbox/hugeplanning-governance-bootstrap-prompt-pack-v0.1/03-kernel-adversary-prompt-sol-high-v0.1.md` | UTF-8 Markdown / 23193 | `ef3c6834f9c1bad35d3d25c198b063e4a97fd8a2da3926d9843cf1605a1a3e61` | role prompt / KGR-003 | ZIP duplicate; exact prompt, run not started; high | Moved raw; exact run copy created |
| `_governance_inbox/hugeplanning-governance-bootstrap-prompt-pack-v0.1/04-governance-role-prompts-index-v0.1.md` | UTF-8 Markdown / 2230 | `f7748b5a8f7967be3a48bf6d0d6d8ec73306a7c6889e31b54b48b8c408a7ff33` | process decision/index / all runs | ZIP duplicate; high | Moved byte-exact with extracted package |
| `_governance_inbox/hugeplanning-governance-bootstrap-prompt-pack-v0.1/05-governance-bootstrap-codex-prompt-v0.1.md` | UTF-8 Markdown / 20560 | `7dd969de5d655639498bef9f17f6baf24112aa2507152024b36cb2e0647a2505` | role prompt / GOV-0 | ZIP duplicate; predecessor of v0.2, not identical; high | Preserved byte-exact as prior version |
| `_governance_inbox/hugeplanning-governance-bootstrap-prompt-pack-v0.1/MANIFEST.md` | UTF-8 Markdown / 853 | `922a2fdab518283bfb73205c66b32cde1ab776795526ba445e95120fe892d02b` | package manifest / prompt pack | ZIP duplicate; high | Moved byte-exact with extracted package |
| `_governance_inbox/hugeplanning-governance-codex-bootstrap-v0.2.zip` | ZIP / 10834 | `499d6d6a8b44db4684c615c8eadaf67518056b52ec5765cf603edaa1fb8e6468` | archive / GOV-0 | Original package; high | Moved byte-exact; safely tested and fully extracted |
| `_governance_inbox/hugeplanning-governance-codex-bootstrap-v0.2/hugeplanning-governance-codex-setup-v0.2.md` | UTF-8 Markdown / 1896 | `809b33a303aa39a23e9067d6e873b139896c3e5cc86e000a997685d58531d82b` | process note / GOV-0 | ZIP duplicate; high | Moved byte-exact; retained in full extraction |
| `_governance_inbox/hugeplanning-kernel-designer-package-v0.1.zip` | ZIP / 41951 | `13affe3d2227f7a22eafa97e122a356b1185a0762ee293e3b0468c7717e0037c` | raw package / KGR-002 outputs | Original package; high | Moved byte-exact; safely tested |
| `_governance_inbox/hugeplanning-kernel-designer-package-v0.1/00-kernel-design-basis.md` | UTF-8 Markdown / 12209 | `25e24014e12cbb9799ba34cab45b6995a47e54f1dd5544551f5c3b3ae59beda6` | designer output / KGR-002 | ZIP duplicate; high | Moved raw; exact run/input copies created |
| `_governance_inbox/hugeplanning-kernel-designer-package-v0.1/01-kernel-admission-analysis.md` | UTF-8 Markdown / 14538 | `669d2012da1f0e7a8de221b02c0b0aabf7d48aba52840f263f8118aaf0aaa271` | designer output / KGR-002 | ZIP duplicate; high | Moved raw; exact run/input copies created |
| `_governance_inbox/hugeplanning-kernel-designer-package-v0.1/02-kernel-v0.1-draft.md` | UTF-8 Markdown / 28565 | `cbd1bce2edb9a369b9de3f6b2466709d9c00c2952c69030424cca3f73ecb463d` | designer output / KGR-002 | ZIP duplicate; proposed Kernel; high | Moved raw; byte-exact canonical candidate and run copies created |
| `_governance_inbox/hugeplanning-kernel-designer-package-v0.1/03-kernel-clauses.yaml` | YAML / 24048 | `bcf5816162396ff4a99d3a42d20c1705ec2c80fe2dcd55976c9c31e2acdd053a` | designer output / KGR-002 | ZIP duplicate; structured proposed Kernel; high | Moved raw; byte-exact canonical candidate and run copies created |
| `_governance_inbox/hugeplanning-kernel-designer-package-v0.1/04-designer-open-questions.md` | UTF-8 Markdown / 8093 | `668f91b8145b4a186d2844f922b79e7bea42efd1ea387240d6862693a626b414` | designer output / KGR-002 | ZIP duplicate; high | Moved raw; exact run/input copies created |
| `_governance_inbox/hugeplanning-kernel-designer-package-v0.1/05-lower-layer-routing.md` | UTF-8 Markdown / 12405 | `2278109a40f431b0883642aecd5b216072e03b6cd85d5f917a1b589ad243bd4d` | designer output / KGR-002 | ZIP duplicate; high | Moved raw; exact run/input copies created |
| `_governance_inbox/hugeplanning-kernel-designer-package-v0.1/06-kernel-adversary-handoff.md` | UTF-8 Markdown / 15514 | `046137abc39532d01063765b1e39e547054ebe750fd12f84e8226eb5c1bc8a13` | designer output/handoff / KGR-002 | ZIP duplicate; high | Moved raw; exact run/input copies created |
| `_governance_inbox/hugeplanning-kernel-intake-checkpoint-v0.1(22).md` | UTF-8 Markdown / 1321 | `1492d77faa9826c02eba76ec6544b863253efb02e2e33c45bfd806eb5640f444` | intake checkpoint / KGR-001 | Unique supplied checkpoint; high | Moved byte-exact to `sources/raw/checkpoints/` |
| `_governance_inbox/hugeplanning-kernel-intake-v0.1.zip` | ZIP / 33408 | `ab9762c3b1ae9b926fb2b8595e6b9b6778958f83ae79c3937bb837e57f7593db` | raw package / KGR-001 outputs | Original package; high | Moved byte-exact; safely tested |
| `_governance_inbox/hugeplanning-kernel-intake-v0.1/00-kernel-mandate.md` | UTF-8 Markdown / 8262 | `f09e9b16595ce3b90d654d3df662e92e0518c13a6db89fcc74b85e5238723a01` | intake output / KGR-001 | ZIP duplicate; high | Moved raw; exact run/input copies created |
| `_governance_inbox/hugeplanning-kernel-intake-v0.1/01-system-context.md` | UTF-8 Markdown / 9884 | `e0a87f291297b660e93d382bacf08ceb9fb78fd0362aebe27c6257b6b98fd12a` | intake output / KGR-001 | ZIP duplicate; high | Moved raw; exact run/input copies created |
| `_governance_inbox/hugeplanning-kernel-intake-v0.1/02-known-hazards.md` | UTF-8 Markdown / 14558 | `f3811f4897e705b2fcc7b16797981d4d3eea5b00fc81c8389db7a6a1bdd7bb11` | intake output / KGR-001 | ZIP duplicate; high | Moved raw; exact run/input copies created |
| `_governance_inbox/hugeplanning-kernel-intake-v0.1/03-authority-and-effects.yaml` | YAML / 11687 | `7579cae03fe70e6e8c897c4627c6d2e48118e65f6ef9314450384cecb769a2a8` | intake output / KGR-001 | ZIP duplicate; high | Moved raw; exact run/input copies created |
| `_governance_inbox/hugeplanning-kernel-intake-v0.1/04-criticality-model.md` | UTF-8 Markdown / 8403 | `aba8993106999b328e98e81657472850552611cc14442c024f06d18b483fa384` | intake output / KGR-001 | ZIP duplicate; high | Moved raw; exact run/input copies created |
| `_governance_inbox/hugeplanning-kernel-intake-v0.1/05-reference-scenarios.md` | UTF-8 Markdown / 9277 | `40ef0ff0cf0d214cbcc431955f9e9a342cbda8fa8bb6e11433e32cd926c38f56` | intake output / KGR-001 | ZIP duplicate; high | Moved raw; exact run/input copies created |
| `_governance_inbox/hugeplanning-kernel-intake-v0.1/06-open-questions.md` | UTF-8 Markdown / 10631 | `effe649fbbe8930434ad7163825ceb99b597474627b6d0e53b43599e2c98b92a` | intake output / KGR-001 | ZIP duplicate; high | Moved raw; exact run/input copies created |
| `_governance_inbox/hugeplanning-kernel-intake-v0.1/07-intake-summary.md` | UTF-8 Markdown / 9412 | `c5d473634bece727488bfe6318e6b2889440fbc9a918ee29ea434119a5f0a459` | intake output/handoff / KGR-001 | ZIP duplicate; historical `(1)` alias noted by Designer; high | Moved raw; exact run/input copies created |
| `_governance_inbox/metodologia_desarrollo_kernel_hugeplanning_con_ia.md` | UTF-8 Markdown / 33216 | `54f106f01ea143573648233f9ca89d7900a98c5bfe70b564528d93eccab82530` | research/process guide / linkage unknown | Unique source; supporting authority only; medium | Moved byte-exact to `sources/raw/research/` |
| `_governance_inbox/plan_maestro_metaingenieria_hugeplanning.md` | UTF-8 Markdown / 42725 | `821459e349d7b2bfa3f338dfcfba9509d4fb54adcb86607b8994f29d00238c98` | research/process guide / linkage unknown | Unique source; supporting authority only; medium | Moved byte-exact to `sources/raw/research/` |
| `_governance_inbox/principios_metaingenieria_ai_native_hugeplanning.md` | UTF-8 Markdown / 39491 | `89384b6d77870257244d2c6a513e9915f86a2f2c5081472e9361e72ed4a1b585` | research source / linkage unknown | Unique source; dated 2026-07-12; medium | Moved byte-exact to `sources/raw/research/` |

## Duplicate and variant disposition

- Exact ZIP/member duplicates: all 7 prompt-pack files, all 7 Designer files, all 8 Intake files, and the supplied Codex setup file. The standalone GOV-0 v0.2 prompt also matches the corresponding Codex ZIP member.
- The temporary root `AGENTS.override.md` matched the Codex ZIP member `HugePlanning-GOV0-AGENTS.override.md` byte-for-byte. The root copy was not imported separately because it was a temporary active instruction file that must not be committed; the archive member is preserved.
- `05-governance-bootstrap-codex-prompt-v0.1.md` and the v0.2 contract are differing versions, not duplicates. Both are preserved; v0.2 governs this run.
- No unresolved differing variants were found among Intake or Designer package members.
- The Designer's recorded `07-intake-summary(1).md` receipt name is treated as a filename alias/discrepancy, not a fabricated duplicate.

## ZIP inspection and extraction

All four ZIP archives passed `unzip -t`; their member names were inspected and contained no path traversal. Existing extracted Intake, Designer, and prompt-pack trees matched archive members byte-for-byte. The Codex v0.2 archive was fully extracted into its raw package directory, adding two archive-only visible members: the packaged override and v0.2 prompt. Original ZIPs were retained.

## Canonical candidates created

- Eight exact KGR-001 output copies and one explicitly reconstructed-source prompt copy.
- Eight exact KGR-002 input copies, seven exact outputs, and its exact prompt.
- Seven exact KGR-003 intended inputs and its exact prompt; no outputs were created.
- `kernel/proposed/0.1.0/02-kernel-v0.1-draft.md` and `03-kernel-clauses.yaml`, byte-exact with their Designer raw sources and still `PROPOSED_NOT_RATIFIED`.

No content normalization was performed.

## Files intentionally not imported

- Root `AGENTS.override.md`: temporary session instruction, exact bytes already preserved as a Codex ZIP member, and explicitly prohibited from commit.
- No inbox file was excluded.
- No conversation record was supplied.

## Unresolved classification questions

See `OPEN_IMPORT_QUESTIONS.md`: complete original Intake prompt recovery, missing historical execution metadata, the Intake-summary filename alias, and uncertain research-to-run linkage.

## Checksum verification

Pre-import hashes are recorded above. `SOURCE_CHECKSUMS.sha256` covers every raw file after import, including archive-only extracted members. Canonical Kernel and run copies are separately compared byte-for-byte during validation.
