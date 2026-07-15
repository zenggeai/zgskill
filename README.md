# ZG Skills

> 面向创业者、一人公司和内容创作者的中文 AI Skills。把真实处境、业务材料和当前卡点交给 Agent，获得清晰判断、可直接使用的交付物，以及一个能立刻开始的下一步。

[![Skills](https://img.shields.io/badge/Skills-4-111111.svg)](#skill-全目录)
[![skills.sh](https://skills.sh/b/zenggeai/zgskill)](https://skills.sh/zenggeai/zgskill)
[![GitHub stars](https://img.shields.io/github/stars/zenggeai/zgskill?style=flat&color=111111)](https://github.com/zenggeai/zgskill/stargazers)

**支持：豆包、WorkBuddy、Claude Code、Codex，以及其他支持 Skills 的 Agent。**

ZG Skills 由 [曾哥](https://github.com/zenggeai) 创建。根据过往 16 年产业数字化和 AI 的落地经验，服务了 5000 +各行各业的AI 线下学员，帮助这些学员多变现 5000 万+，将验证过的方法论沉淀为可直接调用的 skill

它不是一组泛泛的提示词，而是把一人公司中反复出现的判断、表达和行动问题，逐步沉淀成可调用、可复用、有边界的 AI 员工能力。



[快速开始](#快速开始) · [安装](#安装) · [能力一览](#能力一览) · [Skill 全目录](#skill-全目录) · [反馈与共建](#反馈与共建)

```text
真实问题
   ↓
选择最贴近当前目标的 ZG Skill
   ↓
Agent 完成诊断、生成或改写
   ↓
带着真实结果继续补充，推进下一步
```

## ZG Skills 解决什么问题

你不需要先学会“打开度”或“种草力 8 术”的全部方法。只要把眼前发生的事、手里已有的材料和你真正想解决的问题说清楚，对应 Skill 会帮你选择当前最值得处理的一个点。

| 真实处境 | 你会得到 |
| --- | --- |
| 一听到反对意见就急着解释，事后才发现自己没有听进去 | 具体场景还原、主要卡点和一个低风险打开练习 |
| 想主动联系别人、表达需求或尝试新事物，却总是在行动前缩回去 | 对保护机制与现实代价的区分，以及可撤回的最小行动 |
| 不知道朋友圈该发什么，或者写出来总像在硬卖 | 适合当前材料的主术式和一条可直接发布的中文文案 |
| 有用户反馈、真实案例或一个反常识观点，却不知道怎么讲清楚 | 单一内容目标、证据链检查和结构化成稿 |
| 已经写好一条内容，但担心夸大、空泛、压迫感强 | 当前术式判断、最影响效果的 1–3 个问题和局部修改方向 |

## 快速开始

安装完成后，直接在 Agent 中说出问题。支持显式 Skill 调用的 Agent，可以这样开始：

```text
$zg-openness-degree
我每次开会被反对就急着证明自己，会后又觉得自己根本没听进去。
帮我判断卡在哪里，并给我一个今天就能做的练习。
```

```text
$zg-seed-content-8-methods
我做创业者私域咨询，想发一条朋友圈：很多人不是没有流量，而是没有持续经营已有用户。
我没有可公开的案例和数据，不要帮我编，也不要写得太营销。
```

不知道选哪个 Skill 时，只需先判断你要处理的是“人的打开与行动”，还是“内容的生成与表达”。

## 能力一览

| 工作目标 | 主要入口 | 常见产出 |
| --- | --- | --- |
| 判断学习、沟通、关系或管理中的封闭卡点 | `$zg-openness-degree` | 场景还原、主卡点、保护与代价 |
| 设计安全、具体、可复盘的打开练习 | `$zg-openness-degree` | 24 小时最小行动、停止条件、复盘问题 |
| 从零生成朋友圈、私域或个人品牌内容 | `$zg-seed-content-8-methods` | 术式选择、可发布成稿、待核实项 |
| 改写或诊断已有文案 | `$zg-seed-content-8-methods` | 单一目标、问题优先级、局部修改示例 |
| 设计一组连续内容 | `$zg-seed-content-8-methods` | 内容布局、术式交替和 7 条最小排期 |
| 一句话生成公众号文章并保存到草稿箱 | `$zg-wewrite` | 选题、框架、正文、SEO、配图、排版与草稿箱 |
| 把文档或文件夹整理成标准 Skill 并发布 | `$zg-skill-publisher` | zg 命名、标准目录、README 更新、GitHub 发布 |

## 安装

### 一键安装全部 Skills

在终端执行：

```bash
npx -y skills add zenggeai/zgskill -g --all
```

这会把仓库内的全部 Skills 全局安装到已检测的 AI Agent。安装完成后，刷新或重启对应 Agent 即可使用。

### 只安装一个 Skill

```bash
npx -y skills add zenggeai/zgskill -g --skill zg-openness-degree
npx -y skills add zenggeai/zgskill -g --skill zg-seed-content-8-methods
npx -y skills add zenggeai/zgskill -g --skill zg-wewrite
npx -y skills add zenggeai/zgskill -g --skill zg-skill-publisher
```

### 先查看可安装的 Skills

```bash
npx -y skills add zenggeai/zgskill --list
```

### 更新

已经安装 ZG Skills 时，可执行：

```bash
npx -y skills update zg-openness-degree zg-seed-content-8-methods -g
npx -y skills update zg-wewrite -g
npx -y skills update zg-skill-publisher -g
```

更新只会同步 Skill 文件。你在对话中提供的材料和 Agent 中的其他个人数据，不属于本仓库的更新范围。

## ZG Skills 怎样工作

```text
你提供真实处境、已有材料和当前目标
   ↓
Skill 先识别任务类型与信息缺口
   ↓
从框架中只选当前最有价值的一个主点
   ↓
输出诊断、成稿或最小行动
   ↓
你补充真实结果，Agent 再决定下一步
```

ZG Skills 的重点不是一次给出尽可能多的建议，而是处理此刻最值得推进的一个结点。它们会保留事实空位，不会为了让答案更完整而捏造案例、数据、证言或个人经历。

## 方法库与参考资料

仓库中每个 Skill 都将核心工作流程放在 `SKILL.md` 中，将只在特定场景才需要的详细方法放在 `references/` 中。Agent 会在需要时按需读取，避免每次调用都加载全部内容。

- 想了解打开度的五个通道、判断顺序和表达边界，阅读 [`framework.md`](skills/zg-openness-degree/references/framework.md)。
- 想按学习、沟通、管理、亲子或情绪场景选择练习，阅读 [`practice-library.md`](skills/zg-openness-degree/references/practice-library.md)。
- 想了解种草力 8 术的选择条件、结构模板和诊断要点，阅读 [`methods.md`](skills/zg-seed-content-8-methods/references/methods.md)。
- 想设计连续朋友圈的内容结构与最小排期，阅读 [`content-layout.md`](skills/zg-seed-content-8-methods/references/content-layout.md)。

## Skill 全目录

### ZG · 打开度

`$zg-openness-degree`

用“打开度”框架分析个人成长、学习、创造力、沟通、关系、管理、亲子与情绪中的封闭信号。它不会给人贴上“你就是封闭”的标签，而是帮你区分必要边界与惯性防御，找到一个低风险、可撤回、可复盘的打开动作。

适合这样问：

- “我总听不进不同意见，到底在防御什么？”
- “我知道该主动，但就是不敢联系别人，怎么办？”
- “孩子不愿意和我沟通，我可以先调整什么？”

常见产出：场景还原 → 主要卡点 → 保护与代价 → 最小行动 → 复盘问题。

### ZG · 种草力 8 术 Lite

`$zg-seed-content-8-methods`

用问题、结果、氛围、身份、反常识、体系、卡点、损失八种术式，生成、改写或诊断朋友圈、私域和个人品牌内容。它强调一条内容只打透一个点，用真实价值帮助合适的用户看见改变的可能，而不是靠夸大、恐吓或虚假稀缺推动成交。

适合这样问：

- “帮我把这段介绍改成不硬卖的朋友圈。”
- “我有用户反馈，怎么写成真实、有说服力的案例内容？”
- “这条朋友圈为什么显得很营销？帮我诊断，不要直接重写。”

常见产出：术式选择理由 → 可发布成稿或诊断建议 → 待核实的事实项。

### WeWrite · 公众号文章全流程

`$zg-wewrite`

从一句公众号写作需求出发，自动完成热点抓取、选题、框架、素材、正文、SEO、视觉提示、微信排版，并在公众号配置完整时保存到微信公众号草稿箱。它保留降级方案：缺少发布配置时生成本地预览，缺少图片配置时输出图片提示词。

适合这样问：

- “帮我写一篇公众号文章，主题是中小企业怎么用 AI 做获客。”
- “用交互模式，先给我 10 个公众号选题。”
- “把这篇 Markdown 排版成微信公众号格式并保存草稿箱。”

常见产出：公众号正文 → SEO 标题/摘要/标签 → 封面和内文配图 → 微信排版 → 草稿箱 `media_id`。

### 曾哥skill发布

`$zg-skill-publisher`

把用户给出的文档、文件夹或已有能力整理成标准 ZG Skill，并完成命名统一、目录规范、README 更新、安全检查、提交和 GitHub 发布。它强调所有对外 Skill ID 使用 `zg-` 前缀，并避免上传真实配置、密钥、运行历史或输出稿。

适合这样问：

- “帮我把这个文档整理成一个新的 skill，并发布到 GitHub。”
- “这个 skill 命名不统一，改成 zg 开头并同步 README。”
- “检查一下准备提交的 skill 目录，别把配置和输出稿传上去。”

常见产出：标准 Skill 目录 → README 更新 → 提交记录 → GitHub 发布确认。

## 使用原则与边界

- 先给真实处境、真实材料和真实目标；信息不足时，Skill 会保留事实空位，而不是自行补齐。
- `zg-openness-degree` 不提供医学或心理疾病诊断，也不把“打开”等同于无边界信任、过度暴露隐私或放弃判断。
- `zg-seed-content-8-methods` 不捏造案例、数据、证言、稀缺性或身份背书，不依靠羞辱、恐吓和不切实际的收益承诺促成交。
- 医疗、法律、投资等高风险问题需要专业人士和当地规则的进一步核验。

## 开源路线图：一人公司的 AI 员工

ZG Skills 将持续围绕一人公司的真实工作流开源。以下是当前方向，不代表已经发布，也不构成具体上线时间的承诺。

| 部门 | 计划沉淀的 AI 员工能力 |
| --- | --- |
| 获客与营销 | 短视频、公众号、朋友圈种草、一对一私聊 |
| 运营与管理 | 招聘、战略与赛道选择、产品打磨、交付 |
| 创始人能力 | 学习、沟通、关系、决策与行动卡点 |

每个方向都尽量沉淀为独立 Skill：有明确的适用场景、输入要求、工作流程、输出格式和使用边界。

## 项目结构

```text
zgskill/
├── skills/
│   ├── zg-openness-degree/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── references/
│   ├── zg-seed-content-8-methods/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── references/
│   ├── zg-wewrite/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   ├── references/
│   │   ├── scripts/
│   │   └── toolkit/
│   └── zg-skill-publisher/
│       ├── SKILL.md
│       └── agents/openai.yaml
└── README.md
```

每个 `skills/<skill-name>/` 都是一个可独立发现和安装的标准 Skill 目录。新增能力时，会继续使用同样的目录约定。

## 反馈与共建

如果你正在做一人公司，并希望优先开源某个岗位的 AI 员工能力，欢迎[提交 Issue](https://github.com/zenggeai/zgskill/issues)。

为了让问题更容易被处理，建议附上：

- 真实发生的业务或个人场景。
- 你现在怎么做，以及最卡的环节。
- 你希望 AI 最终交付什么。
- 若是现有 Skill 的问题，请附上脱敏后的输入与实际输出。

## 作者与支持

作者：[曾哥](https://github.com/zenggeai)（微信：zengge198406 ）

- 喜欢这个项目，可以给仓库一个 [Star](https://github.com/zenggeai/zgskill)。
- 发现问题或想提交需求，请前往 [GitHub Issues](https://github.com/zenggeai/zgskill/issues)。
- 想直接改进 Skill，欢迎提交 Pull Request。

## 许可证

本项目的开源许可证尚未正式发布。在 `LICENSE` 文件补充之前，请不要默认仓库内容已获得商业使用、修改或再分发授权。
