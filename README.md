# lvsea-tishici

> 把一段粗略目标、需求或已有 Prompt，生成可直接复制给目标 AI 的工程化提示词。

`lvsea-tishici` 是中文优先的 Agent Skill。它吸收了 [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) 的目标工具路由、9 维意图抽取、失败模式诊断、上下文记忆块和代理停止条件，并结合 [Luban-Labs/pp](https://github.com/Luban-Labs/pp) 的手动 Prompt 库索引路由、[wangmian0/prompt-opt](https://github.com/wangmian0/prompt-opt) 的场景化 Prompt 优化，以及 `lvsea-zao-skill` 的可评测、可移植、可治理发布流程。

## 安装

```bash
npx skills add lhylvsea/lvsea-tishici --skill lvsea-tishici --global --copy -y
```

安装后重新加载 Agent 客户端，再使用 `/lvsea-tishici` 或 `$lvsea-tishici` 显式触发。

## 你可以这样说

- “/lvsea-tishici 把下面的制造现场安全培训想法，生成适合 Claude 的中文工程化提示词。”
- “$lvsea-tishici 把这个需求改成 Cursor 可执行的提示词，只允许修改 `src/auth.ts`。”
- “/lvsea-tishici 为 Midjourney 生成一张非金属矿工厂夜景图的提示词，保留工业真实感。”
- “$lvsea-tishici 优化这段已有 Prompt，保留原意，修复输出格式不稳定和事实臆造问题。”
- “$lvsea-tishici 从提示词库里帮我挑 1–3 个适合做代码审查的场景，再输出可复制 Prompt，不要执行。”
- “/lvsea-tishici 把这个排障草稿按场景模板打磨成正式任务书，只列出最多 3 行改动说明。”

没有指定工具时，会优先生成平台中立的通用大模型 Prompt；只有工具语法或能力会明显改变结果时才追问关键缺口。

## 输出特点

1. 从任务、工具、输入、上下文、格式、约束、受众、成功标准和示例九个维度收敛需求。
2. 根据任务类型选择最小充分结构，不把框架名称暴露给最终 Prompt。
3. 将“专业”“高质量”“做得好”等模糊词改成可执行、可检查的要求。
4. 对代码代理增加文件范围、禁止动作、停止条件和验收标准。
5. 对事实、引用、图像、视频、推理原生模型和敏感凭据使用相应安全边界。
6. 默认只交付一份带标题的可复制 Markdown Prompt，不附加无关解释。
7. 对显式优化请求先判定排障、加功能、重构、调研、审查、数据报告或循环任务场景；对提示词库请求先做手动索引路由，再处理用户提供的正文。

## 本地验证

在仓库根目录执行：

```bash
python scripts/validate_skill.py .
python scripts/trigger_eval.py . --cases evals/trigger_cases.json --output reports/trigger-eval.json
python scripts/export_skill_ir.py . --output reports/skill-ir.json
python scripts/context_sizer.py . --output reports/context-budget.json
python scripts/release_check.py . --phase local --run-tests --output reports/release-local.json
```

发布前先做只读检查：

```bash
python scripts/publish_skill.py . --dry-run --github-user lhylvsea --repo-name lvsea-tishici
```

完整发布使用功能分支、Pull Request、版本化 Release、公开发现和干净安装门禁：

```bash
python scripts/publish_skill.py . --github-user lhylvsea --repo-name lvsea-tishici
```

## 前置条件

- [ ] Python 3.9+：`python --version`
- [ ] Node.js 与 npx：`node --version && npx --version`
- [ ] Git：`git --version`
- [ ] 发布到 GitHub 时已登录：`gh auth status`
- [ ] 允许访问公开 GitHub、skills.sh 和 SkillsMP（仅用于先例研究或发布验证）
- [ ] 需要真实模型实跑或人工盲评时，已单独准备目标平台和审批；本 Skill 不生成凭据

## 重要边界

- 包结构、触发 fixture、Skill IR 和本地门禁不能证明任何模型上的实际输出质量；没有 provider 实跑或人工评审时，报告保留 `missing evidence`。
- 上游仓库的安装量、stars 和维护时间不是质量评分，不会合并成“最佳 Skill”结论。
- 远程材料只做元数据和公开源码审阅；不执行未经审查的第三方安装器、hook 或脚本。
- 不内置 `pp` 的 `/pp` 插件入口、`prompt-opt` 的 `prompt-level` 被动钩子、安装器、状态文件或第三方 Prompt 正文；本 Skill 继续只在显式触发后生成 Prompt，不直接执行。
- 发布、PR、Release、`npx skills add` 和本地安装同步会改变外部状态，只在用户明确要求时执行。
- 公开仓库不应包含 Token、Cookie、私有附件、原始私人对话、内部源材料或本机绝对路径。

## Troubleshooting

| 问题 | 处理 |
|---|---|
| Skill 不触发 | 确认使用 `/lvsea-tishici` 或 `$lvsea-tishici`，并重启 Agent 客户端。 |
| 目标工具不明确 | 直接补充“目标工具：Claude / GPT / Cursor / Midjourney”等；通用任务会默认平台中立。 |
| `No valid skills found` | 运行 `python scripts/validate_skill.py .`，检查根目录只有一个 `SKILL.md` 且 frontmatter 完整。 |
| 触发过宽或过窄 | 修改 `SKILL.md` 的 description 和 `evals/trigger_cases.json`，重新运行 `trigger_eval.py`。 |
| 发布门禁失败 | 读取对应 gate；修复后提升版本号，不要直接推送默认分支或复用已发布版本。 |
| 本地通过但安装失败 | 发布后运行 `npx skills add lhylvsea/lvsea-tishici --list`，再用全新临时目录验证。 |

## 来源与致谢

这是独立整合实现，不是上游仓库的整库镜像：

- [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)：目标工具路由、模板库、失败模式和安全提示词原则；其公开代码按 MIT 许可证保留必要声明。
- [Luban-Labs/pp](https://github.com/Luban-Labs/pp)：手动 Prompt 库索引、候选路由、正文事实源和不代编空白模板的机制；仅作语义适配。
- [wangmian0/prompt-opt](https://github.com/wangmian0/prompt-opt)：场景判定、字段骨架、意图保真和显式优化后的停机边界；仅作语义适配。
- [getsentry/skills prompt-optimizer](https://github.com/getsentry/skills/tree/main/skills/prompt-optimizer)：合约优先、评测集、上下文清单和残余风险记录的设计启发。
- [joeseesun/qiaomu-meta-skill](https://github.com/joeseesun/qiaomu-meta-skill) 与 [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill)：`lvsea-zao-skill` 的上游方法来源。

## License

MIT。上游 Prompt Master 的版权与许可说明见 [LICENSE](LICENSE)，本包的整合与新增内容见 [NOTICE.md](NOTICE.md)。
