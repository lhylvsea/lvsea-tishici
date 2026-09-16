# Sources

| Source | Type | Use in this package |
|---|---|---|
| https://github.com/nidhinjs/prompt-master | public MIT skill | Tool routing, prompt templates, failure patterns, memory and credential safety |
| https://github.com/getsentry/skills/tree/main/skills/prompt-optimizer | public prompt-optimization skill | Contract-first shaping, context inventory, evaluation and residual-risk discipline |
| https://github.com/joeseesun/qiaomu-meta-skill | upstream method | Prior-art, trigger evaluation and governed release concepts through `lvsea-zao-skill` |
| https://github.com/yaojingang/yao-meta-skill | upstream method | IR, portability, trust and lifecycle concepts through `lvsea-zao-skill` |
| User-provided Chinese prompt-engineering template | direct task source | Chinese field coverage and prompt-only output lock |

## Evidence policy

Public source review and local deterministic checks are recorded here and in `reports/`. No private prompt, credential, local absolute path or provider output is stored in the package.

For this synchronization, Prompt Master `v1.8.0` was reviewed at commit `2bd92518e26bf659e21e3d9ab90573fcf3ddeccb` on 2026-09-16. Only the compatible reference guidance was adopted; the upstream root entrypoint was not mirrored.
