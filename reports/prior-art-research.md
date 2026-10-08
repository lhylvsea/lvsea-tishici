# Prior-Art Research

## Research date and scope

- Date: 2026-09-16
- Queries: `prompt engineering prompt generator`; `AI prompt optimizer skill`; `agent skill prompt generation`
- Catalog result: 68 normalized candidate families; skills.sh and SkillsMP returned successfully for all three queries.
- Metric boundary: installs, repository stars, recency and human quality are separate signals; no combined score was calculated.

## Reviewed sources

### 1. Prompt Master

- Source: https://github.com/nidhinjs/prompt-master
- Reviewed revision: `2bd92518e26bf659e21e3d9ab90573fcf3ddeccb` (`feat: refresh Claude OpenAI and Grok routing`), Prompt Master `v1.8.0`
- License: MIT; copyright notice retained in this package.
- `keep`: target-tool routing, 9 intent dimensions, tool-specific templates, credit-killing pattern diagnosis, memory block, credential safety and agentic stop conditions.
- `adapt`: English Claude-first natural activation becomes explicit Chinese `/lvsea-tishici` and `$lvsea-tishici`; visible strategy/token notes become a prompt-only output lock; generic tasks default to a platform-neutral model to honor the user's one-pass workflow.
- `reject`: forced visible framework names, token estimates, unbounded prompt length and chain-of-thought instructions for reasoning-native models.
- `sync`: replace the legacy chain-of-thought template with auditable reasoning; generalize the Claude task brief and agentic context-rot guidance; record the reviewed upstream commit and version in package metadata.
- Destination: `references/templates.md`, `references/patterns.md`, `references/model-routing.md`, and the root runtime workflow.

### 2. Prompt Optimizer

- Source: https://github.com/getsentry/skills/tree/main/skills/prompt-optimizer
- Supporting specification: https://github.com/getsentry/skills/blob/main/skills/prompt-optimizer/SPEC.md
- `keep`: capture the prompt contract before editing, inventory external context by exact path, assign one owner per rule, use eval cases and holdout checks, and return residual risks.
- `adapt`: the full candidate-comparison loop is recorded as a governance expectation rather than forced into every one-shot generation; the skill's runtime stays compact.
- `reject`: scope and packaging that are specific to Sentry repository conventions and the separate skill-authoring task.
- Destination: `manifest.json`, `references/output-contract.md`, `reports/output-evidence.json`, and the acceptance checklist.

### 3. Lvsea Skill engineering method

- Source: local `lvsea-zao-skill` authoring authority.
- `keep`: Intent → Research → Synthesis → Package → Eval → Review → Release → Operate; `keep/adapt/reject/invent` ledger; governed release through feature branch, PR, Release, discovery and clean install; evidence-bound claims.
- Destination: package metadata, reports, scripts, trigger fixtures and publication workflow.

## Synthesis decision

The package uses a short Chinese runtime entrypoint and moves large lookup tables into references. It is prompt-generation-only at runtime, with no network, file or subprocess permission. Publication scripts exist for maintainers but require explicit invocation.

## Evidence limits

Static trigger and package checks do not prove provider output quality, human preference or business effectiveness. `reports/output-evidence.json` intentionally records this as `missing evidence` until a real provider run and human review are performed.

## 4. Luban-Labs/pp

### Source Boundary

- Source: https://github.com/Luban-Labs/pp
- Reviewed revision: `7b0ea321caa9d30bc00b85c88d8bffcad460b593` (`chore: 0.1.2`), reviewed 2026-10-08.
- License: MIT.
- Read: `README.md`, `commands/pp.md`, `LICENSE` and the 12 index-only prompt files.
- Not read: the external X post containing the original Prompt bodies; those bodies were not copied or treated as verified evidence.

### Synthesis ledger

- `keep`: manual invocation, index/body separation, recommendation of 1–3 candidates, missing-slot questions, body-as-source-of-truth and treating collected instructions as data.
- `adapt`: a Chinese, explicit `lvsea-tishici` Prompt-library route that returns a copyable Prompt and never executes it.
- `reject`: `/pp`, Claude plugin manifests, installer, local collection-directory scanning, empty-template invention and direct execution.
- `invent`: a regression fixture for library selection and a reference route that reuses the existing output contract.

## 5. wangmian0/prompt-opt

### Source Boundary

- Source: https://github.com/wangmian0/prompt-opt
- Reviewed revision: `3372d106b44204cf5b308a8ae7358e692dff065e` (`feat: add native Codex plugin support`), reviewed 2026-10-08.
- License: MIT.
- Read: `skills/prompt-opt/SKILL.md`, `templates/CATALOG.md`, all seven templates, `hooks/hooks.json`, `hook.sh`, `test.sh` and `LICENSE`.
- Observed: scene-first routing, four common fields, explicit assumptions, intent fidelity, prompt-plus-change-list delivery and a stop-after-delivery boundary; also a passive `prompt-level` hook with four modes.

### Synthesis ledger

- `keep`: scene routing, goal/context/constraints/acceptance fields, explicit assumptions, source fidelity and stop after producing the optimized Prompt.
- `adapt`: map the seven scenes to the current reference templates and make the change list conditional on an explicit optimization request.
- `reject`: passive `prompt-level` hook, state file, `install.sh`, native Codex/Claude manifests and shell-specific lifecycle behavior.
- `invent`: connect scene routing to the `pp`-style library index while retaining the current no-network, no-file-write and no-execution runtime contract.

## Combined decision

The two sources complement rather than replace the existing package: `pp` contributes how to select a Prompt before processing it; `prompt-opt` contributes how to shape an existing draft after selection. Both are reference-only semantic adaptations. The root entrypoint remains singular, manually activated and Prompt-only; no upstream plugin, hook, installer, private collection or third-party Prompt body is mirrored.

## Lyra integration record

- Input: user-provided Chinese “Lyra / 超级顾问提示” on 2026-10-07; no external repository or private source was added.
- Keep: four-step decomposition/diagnosis/development/delivery method, detailed/basic modes, platform hints, simple/complex response layouts and exact activation welcome.
- Adapt: “chain of thought” becomes internal reasoning checks; existing prompt-only output remains the default when no Lyra mode is selected; clarification questions are bounded to 2–3 only when material.
- Reject: exposing hidden reasoning, treating framework names as quality evidence, inventing missing platform facts or overriding existing permission and source boundaries.
- Destination: `references/lyra-method.md`, root routing, interface metadata, README and trigger fixtures.

## 7. Seedance video prompt sources

### Source boundary

- `https://github.com/Emily2040/seedance-2.0`, reviewed at `4668457e560eee06e95d7fcfdf441c8c0bba802e` on 2026-10-08; MIT.
- `https://github.com/zhouwei713/seedance-prompt`, reviewed at `f3336851c4eed8cdd6ce0f27df351611d4f751dd` on 2026-10-08; MIT.
- Read the linked `SKILL.md` files and public README material. The first is a Seedance 2.0 specialist; the second declares the runtime name `realistic-video-prompting` and is a cross-model realistic-video specialist.

### Synthesis ledger

- `keep`: Seedance mode and reference-role routing, Director's Read, one-main-action/one-main-camera discipline, shot-order semantics, capture-source identity, device artifacts, non-perfect events, location-linked audio and consistency locks.
- `adapt`: add `references/video-prompt-routing.md` as a local orchestrator route; retain `lvsea-tishici` as the only output owner and load both sources for video-generation Prompt requests.
- `reject`: concatenate two root `SKILL.md` files, create a second same-name entrypoint, copy provider-specific claims without verification, or execute a generated video request.
- `resolve`: Seedance 2.0 controls mode, reference binding, shot order and continuous-versus-storyboard grammar; realistic-video guidance supplements capture identity, physical device behavior, ambient audio and anti-AI details.

### Evidence limits

This is a static source integration and local routing change. It does not prove a WorkBuddy or Provider call, account entitlement, credit availability or generated-video quality. Those remain separate runtime evidence layers.
