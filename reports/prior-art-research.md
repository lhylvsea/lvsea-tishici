# Prior-Art Research

## Research date and scope

- Date: 2026-08-23
- Queries: `prompt engineering prompt generator`; `AI prompt optimizer skill`; `agent skill prompt generation`
- Catalog result: 68 normalized candidate families; skills.sh and SkillsMP returned successfully for all three queries.
- Metric boundary: installs, repository stars, recency and human quality are separate signals; no combined score was calculated.

## Reviewed sources

### 1. Prompt Master

- Source: https://github.com/nidhinjs/prompt-master
- Reviewed revision: `d15eabbe5d2122eedc060bae8a771381e9873d1b` (`docs: update MiniMax routing to M3 as default`)
- License: MIT; copyright notice retained in this package.
- `keep`: target-tool routing, 9 intent dimensions, tool-specific templates, credit-killing pattern diagnosis, memory block, credential safety and agentic stop conditions.
- `adapt`: English Claude-first natural activation becomes explicit Chinese `/lvsea-tishici` and `$lvsea-tishici`; visible strategy/token notes become a prompt-only output lock; generic tasks default to a platform-neutral model to honor the user's one-pass workflow.
- `reject`: forced visible framework names, token estimates, unbounded prompt length and chain-of-thought instructions for reasoning-native models.
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
