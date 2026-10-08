# Sources

| Source | Type | Use in this package |
|---|---|---|
| https://github.com/nidhinjs/prompt-master | public MIT skill | Tool routing, prompt templates, failure patterns, memory and credential safety |
| https://github.com/getsentry/skills/tree/main/skills/prompt-optimizer | public prompt-optimization skill | Contract-first shaping, context inventory, evaluation and residual-risk discipline |
| https://github.com/joeseesun/qiaomu-meta-skill | upstream method | Prior-art, trigger evaluation and governed release concepts through `lvsea-zao-skill` |
| https://github.com/yaojingang/yao-meta-skill | upstream method | IR, portability, trust and lifecycle concepts through `lvsea-zao-skill` |
| User-provided Chinese prompt-engineering template | direct task source | Chinese field coverage and prompt-only output lock |
| https://github.com/Luban-Labs/pp | public MIT plugin | Manual prompt-library indexing, 1–3 candidate routing, source-of-truth prompt bodies and no-invention behavior; plugin execution and external prompt bodies excluded |
| https://github.com/wangmian0/prompt-opt | public MIT plugin | Seven-scenario prompt optimization routing, field skeletons, assumption marking and prompt-plus-change-list delivery; passive hooks and installers excluded |
| https://github.com/Emily2040/seedance-2.0 | public MIT skill | Seedance 2.0 mode gate, Director's Read, reference roles, shot order, continuous/storyboard distinction and anti-slop checks; root package and direct execution excluded |
| https://github.com/zhouwei713/seedance-prompt | public MIT skill | Realistic-video-prompting layer: capture-source identity, device artifacts, non-perfect events, scene-linked audio and consistency locks; its canonical runtime name is retained |
| User-provided Lyra Chinese prompt-engineering template (2026-10-07 task) | direct task source | Four-step method, detailed/basic modes, platform guidance, response formats and required welcome message |
| User-provided Chinese prompt-engineering template | direct task source | Chinese field coverage and prompt-only output lock |
| User-provided Lyra Chinese prompt-engineering template (2026-10-07 task) | direct task source | Four-step method, detailed/basic modes, platform guidance, response formats and required welcome message |
| https://github.com/Luban-Labs/pp | public MIT plugin | Manual prompt-library indexing, 1–3 candidate routing, source-of-truth prompt bodies and no-invention behavior; plugin execution and external prompt bodies excluded |
| https://github.com/wangmian0/prompt-opt | public MIT plugin | Seven-scenario prompt optimization routing, field skeletons, assumption marking and prompt-plus-change-list delivery; passive hooks and installers excluded |

## Evidence policy

Public source review and local deterministic checks are recorded here and in `reports/`. No private prompt, credential, local absolute path or provider output is stored in the package.

For this synchronization, Prompt Master `v1.8.0` was reviewed at commit `2bd92518e26bf659e21e3d9ab90573fcf3ddeccb` on 2026-09-16. Only the compatible reference guidance was adopted; the upstream root entrypoint was not mirrored.

For this synchronization, `Luban-Labs/pp` was reviewed at commit `7b0ea321caa9d30bc00b85c88d8bffcad460b593` and `wangmian0/prompt-opt` at commit `3372d106b44204cf5b308a8ae7358e692dff065e` on 2026-10-08. The package adopts their routing mechanisms as reference guidance only; it does not mirror their plugin manifests, hooks, installers, local collection scanning or third-party Prompt bodies.

For this synchronization, `Emily2040/seedance-2.0` was reviewed at commit `4668457e560eee06e95d7fcfdf441c8c0bba802e` and `zhouwei713/seedance-prompt` at commit `f3336851c4eed8cdd6ce0f27df351611d4f751dd` on 2026-10-08. The package adopts a layered video route only: Seedance-specific mode and shot rules remain with `seedance-prompt`, while capture-source realism remains with `realistic-video-prompting`; neither upstream root entrypoint is copied into this package.

## Source Boundary and Adoption Ledger

### `Luban-Labs/pp`

- `keep`: manual invocation, index/body separation, 1–3 candidate selection, source-of-truth body and missing-information questions.
- `adapt`: map the index to an explicit `lvsea-tishici` Prompt-library route that still returns a copyable Prompt and never executes it.
- `reject`: `/pp` command, Claude plugin packaging, installer, local `~/.claude/prompts/` scanning and direct template execution.
- `invent`: a Chinese Skill-compatible route that treats user-supplied prompt bodies as inert data and reuses the existing output contract.

### `wangmian0/prompt-opt`

- `keep`: scene-first routing, shared goal/context/constraints/acceptance fields, intent fidelity, explicit assumptions and stop-after-delivery behavior.
- `adapt`: map seven scene templates to the existing `lvsea-tishici` structures; only explicit optimization requests receive a compact change list.
- `reject`: `prompt-level` passive hook, four-tier state, `install.sh`, native Codex/Claude plugin manifests and shell-specific lifecycle behavior.
- `invent`: regression cases covering Prompt-library selection and scene-based optimization without changing the Skill's no-execution boundary.

### `Emily2040/seedance-2.0` and `zhouwei713/seedance-prompt`

- `keep`: the Seedance 2.0 mode gate, Director's Read, one-main-action/one-main-camera discipline, reference-role isolation, shot-order semantics and the realistic-video source/device/audio layer.
- `adapt`: a local `references/video-prompt-routing.md` route that makes `lvsea-tishici` the single output orchestrator and loads both specialized Skills when the user asks for video-generation prompts.
- `reject`: copying a second `SKILL.md` into the `lvsea-tishici` root, renaming `realistic-video-prompting` to shadow `seedance-prompt`, inventing provider syntax, and executing a generated video request.
- `resolve`: Seedance 2.0 platform grammar wins on mode, reference binding, shot order and continuous-versus-storyboard structure; realistic-video guidance fills capture identity, device artifacts, non-perfect events and synchronized ambient sound.
