# ZG Skills

> 面向创业者、一人公司和内容创作者的中文 AI Skills。把真实处境、业务材料和当前卡点交给 Agent，获得清晰判断、可直接使用的交付物，以及一个能立刻开始的下一步。

[![Skills](https://img.shields.io/badge/Skills-14-111111.svg)](#skill-全目录)
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

你不需要先学会每个 Skill 背后的全部方法。只要把眼前发生的事、手里已有的材料和你真正想解决的问题说清楚，对应 Skill 会帮你选择当前最值得处理的一个点。

| 真实处境 | 你会得到 |
| --- | --- |
| 不知道朋友圈该发什么，或者写出来总像在硬卖 | 适合当前材料的主术式和一条可直接发布的中文文案 |
| 手里有产品、案例或人设素材，却不知道朋友圈九宫格该选哪一格 | 一个核心种草目标、事实边界检查和 200 字内可发布成稿 |
| 有用户反馈、真实案例或一个反常识观点，却不知道怎么讲清楚 | 单一内容目标、证据链检查和结构化成稿 |
| 已经写好一条内容，但担心夸大、空泛、压迫感强 | 当前术式判断、最影响效果的 1–3 个问题和局部修改方向 |
| 客户在私聊里说“太贵”“考虑一下”或“怕没效果”，不知道怎么继续 | 基于产品与客户知识的疑虑诊断、应对原理和可直接发送的话术 |
| 想做低价课、体验营或诊断产品，却分不清课程内容和客户结果 | 一个可验收的主结果、标准化交付闭环、后端承接和付费验证计划 |
| 遇到结果异常，却只能归因为“我水平不行”或“内容不好” | 基于关键证据淘汰错误解释，定位真正值得解决的问题 |
| 老板同时面对多个产品、方向或同行动作，不知道资源该押在哪里 | 真正决策问题、最强正反证据、当前倾向、信心等级和改判条件 |

## 快速开始

安装完成后，直接在 Agent 中说出问题。支持显式 Skill 调用的 Agent，可以这样开始：

```text
$zg-seed-content-8-methods
我做创业者私域咨询，想发一条朋友圈：很多人不是没有流量，而是没有持续经营已有用户。
我没有可公开的案例和数据，不要帮我编，也不要写得太营销。
```

```text
$zg-ai-nine-grid-moments
根据下面的客户案例写一条 200 字以内的朋友圈。请自行选择九宫格里最合适的一格，只讲透一个点，不要编造数据。
```

```text
$zg-socratic-problem-locator
我最近连续发布 20 条短视频，播放量都没有超过 1 万。
先别急着给方案，请根据已有数据帮我定位真正的问题。
```

```text
$zg-ai-strategy-expert
结合我的业务，帮我判断未来 6 个月的增长应该押在哪条主线上。
先给工作性判断，一次只问一个真正影响结论的问题。
```

```text
$zg-private-chat-sales-assistant
请先读取我的产品资料和目标客户画像，再分析下面这段客户疑虑。
输出应对方法、背后原理和一版可以直接发送的微信话术。
```

```text
$zg-lead-product-designer
我的后端产品是一门 3980 元线下课，想做一个 99 元三天体验课。
请帮我把课程主题收敛成一个客户看得见、能验收、可以规模交付的结果。
```

不知道选哪个 Skill 时，先判断你要处理的是“战略取舍”“问题尚未定位”，还是“内容的生成与表达”。

## 能力一览

| 工作目标 | 主要入口 | 常见产出 |
| --- | --- | --- |
| 从零生成朋友圈、私域或个人品牌内容 | `$zg-seed-content-8-methods` | 术式选择、可发布成稿、待核实项 |
| 改写或诊断已有文案 | `$zg-seed-content-8-methods` | 单一目标、问题优先级、局部修改示例 |
| 设计一组连续内容 | `$zg-seed-content-8-methods` | 内容布局、术式交替和 7 条最小排期 |
| 用九宫格把素材写成朋友圈 | `$zg-ai-nine-grid-moments` | 主格选择、事实核验、200 字内可发布成稿 |
| 诊断客户私聊疑虑并生成下一条回复 | `$zg-private-chat-sales-assistant` | 疑虑判断、应对方法、原理和可发送话术 |
| 设计或诊断低价课、体验营、诊断服务等引流品 | `$zg-lead-product-designer` | 主结果、验收标准、交付闭环、后端承接与验证计划 |
| 一句话生成公众号文章并保存到草稿箱 | `$zg-wewrite` | 选题、框架、正文、SEO、配图、排版与草稿箱 |
| 写反常识公众号长文 | `$zg-counterintuitive-wechat-article` | 标题、现象、观点、方法和金句收尾 |
| 判断目标、产品、方向、合作或同行证据 | `$zg-ai-strategy-expert` | 真正决策、正反论证、倾向、信心和改判条件 |
| 梳理个人定位与长期内容框架 | `$zg-daofa-content-framework` | 核心服务问题与道法术器二级内容框架 |
| 把真实素材翻译成可生产的短视频选题 | `$zg-xuan-ti-fan-yi-qi` | 受众、场景、矛盾、证据、判断与商业去向 |
| 从模糊困惑、异常结果或草率归因中定位真问题 | `$zg-socratic-problem-locator` | 当前断点、被推翻解释、关键未知和最小验证动作 |

## 安装

### 一键安装全部 Skills

在终端执行：

```bash
npx -y skills add zenggeai/zgskill -g --all
```

这会把仓库内的全部 Skills 全局安装到已检测的 AI Agent。安装完成后，刷新或重启对应 Agent 即可使用。

### 只安装一个 Skill

```bash
npx -y skills add zenggeai/zgskill -g --skill zg-seed-content-8-methods
npx -y skills add zenggeai/zgskill -g --skill zg-wewrite
npx -y skills add zenggeai/zgskill -g --skill zg-counterintuitive-wechat-article
npx -y skills add zenggeai/zgskill -g --skill zg-socratic-problem-locator
npx -y skills add zenggeai/zgskill -g --skill zg-customer-case-collector
npx -y skills add zenggeai/zgskill -g --skill zg-persona-story-collector
npx -y skills add zenggeai/zgskill -g --skill zg-product-info-collector
npx -y skills add zenggeai/zgskill -g --skill zg-daofa-content-framework
npx -y skills add zenggeai/zgskill -g --skill zg-xuan-ti-fan-yi-qi
npx -y skills add zenggeai/zgskill -g --skill zg-hotspot-theory
npx -y skills add zenggeai/zgskill -g --skill zg-ai-nine-grid-moments
npx -y skills add zenggeai/zgskill -g --skill zg-ai-strategy-expert
npx -y skills add zenggeai/zgskill -g --skill zg-private-chat-sales-assistant
npx -y skills add zenggeai/zgskill -g --skill zg-lead-product-designer
```

### 先查看可安装的 Skills

```bash
npx -y skills add zenggeai/zgskill --list
```

### 更新

已经安装 ZG Skills 时，可执行：

```bash
npx -y skills update zg-seed-content-8-methods -g
npx -y skills update zg-wewrite -g
npx -y skills update zg-counterintuitive-wechat-article -g
npx -y skills update zg-socratic-problem-locator -g
npx -y skills update zg-customer-case-collector -g
npx -y skills update zg-persona-story-collector -g
npx -y skills update zg-product-info-collector -g
npx -y skills update zg-daofa-content-framework -g
npx -y skills update zg-xuan-ti-fan-yi-qi -g
npx -y skills update zg-hotspot-theory -g
npx -y skills update zg-ai-nine-grid-moments -g
npx -y skills update zg-ai-strategy-expert -g
npx -y skills update zg-private-chat-sales-assistant -g
npx -y skills update zg-lead-product-designer -g
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

### ZG · 客户案例采集

`$zg-customer-case-collector`

通过访谈式对话帮助学员批量整理客户成功案例。安装后不需要记住复杂提示词，直接说“帮我整理一个客户案例”即可。它按“谁—痛—解—果—证”逐步采访，不让用户填写复杂表格；完成后生成匿名化《客户成功案例卡》，并按行业、客户类型、问题类型、解决方案、结果类型和内容用途建立标签。它不会编造数据、证言或结果，缺少材料时会明确标记“证据待补充”。

适合这样问：

- “采访我，把过去服务过的客户整理成案例卡。”
- “下一个客户。”
- “汇总我的客户案例库，并列出待补证据。”

常见产出：自然对话 → 单个客户成功案例卡 → 批量案例标签索引与待补清单。

### ZG · 产品信息采集

`$zg-product-info-collector`

把知识库中的产品资料和用户口述整理成一个统一产品知识库中的产品卡。首次一次性采集 7 个核心字段：产品是什么、适合谁、解决什么场景下的什么问题、带来什么结果、交付权益、跟别人有什么不一样、价格。用户漏填时只集中补问一次，仍未回答的字段标记为“待补充”，不编造信息。

适合这样问：

- “帮我整理一个产品。”
- “我有五个产品，帮我建立统一产品库。”
- “汇总产品信息，并列出哪些字段还没补齐。”

常见产出：产品资料提炼 → 单个产品卡 → 统一产品索引与待补清单。

### ZG · 人设故事采集

`$zg-persona-story-collector`

用户只需说“帮我整理我的人设故事”，就可以自由倾倒从小到大的多段经历。Skill 会全部保留原始素材，自动切分并轻量整理，再推荐适合深挖的故事；选中后按背景、冲突、应对、过程、结果、影响完成采访，生成可用于个人品牌、内容创作、课程介绍和自我定位的人设故事卡。

常见产出：故事素材池 → 故事索引 → 重点故事深挖 → 人设故事卡 → 人设主题与内容用途汇总。

## 方法库与参考资料

仓库中每个 Skill 都将核心工作流程放在 `SKILL.md` 中，将只在特定场景才需要的详细方法放在 `references/` 中。Agent 会在需要时按需读取，避免每次调用都加载全部内容。

- 想了解种草力 8 术的选择条件、结构模板和诊断要点，阅读 [`methods.md`](skills/zg-seed-content-8-methods/references/methods.md)。
- 想设计连续朋友圈的内容结构与最小排期，阅读 [`content-layout.md`](skills/zg-seed-content-8-methods/references/content-layout.md)。
- 想了解朋友圈九宫格的九个主格与组合边界，阅读 [`nine-grid-marketing.md`](skills/zg-ai-nine-grid-moments/references/nine-grid-marketing.md)。
- 想了解案例、数字、来源优先级和自然表达规则，阅读 [`writing-and-evidence.md`](skills/zg-ai-nine-grid-moments/references/writing-and-evidence.md)。
- 想把“苏格拉底问题定位”方法复制给其他 AI，阅读 [`standalone-prompt.md`](skills/zg-socratic-problem-locator/references/standalone-prompt.md)。
- 想了解战略问题的共同判断骨架，阅读 [`strategy-core.md`](skills/zg-ai-strategy-expert/references/strategy-core.md)。
- 想了解目标增长、战略诊断、机会判断、同行研究和复盘的模式，阅读 [`modes.md`](skills/zg-ai-strategy-expert/references/modes.md)。
- 想了解战略研究的证据等级、联网条件和同行分类，阅读 [`evidence-and-research.md`](skills/zg-ai-strategy-expert/references/evidence-and-research.md)。
- 想完成私聊助手的首次知识接入，阅读 [`knowledge-intake.md`](skills/zg-private-chat-sales-assistant/references/knowledge-intake.md)。
- 想判断成交阶段、疑虑类别和应对方法，阅读 [`method-library.md`](skills/zg-private-chat-sales-assistant/references/method-library.md)。
- 想把课程主题、渠道和工具收敛成可验收结果，阅读 [`result-design.md`](skills/zg-lead-product-designer/references/result-design.md)。
- 想比较多个引流品候选并设计小样本测试，阅读 [`scoring-and-validation.md`](skills/zg-lead-product-designer/references/scoring-and-validation.md)。

### ZG · 选题翻译器

`$zg-xuan-ti-fan-yi-qi`

把经历、业务现场、客户案例、观点、文章、录音摘要或日常观察，翻译成有明确受众问题、核心判断、事实证据和商业去向的短视频选题。它区分事实、推断与待补证据，不把工具、生活流水账或耸动标题误当成成熟选题，也不把完整脚本写作冒充成选题开发。

适合这样问：

- “把这段业务现场翻译成精准获客选题。”
- “从我的日常观察里找 3 个能生产的选题，别编数据。”
- “这个选题够不够成立？帮我检查证据和商业去向。”

常见产出：素材判断 → 受众与矛盾 → 核心判断 → 证据缺口 → 推荐选题 → 生产状态。

## Skill 全目录

### AI 战略专家 SKILL

`$zg-ai-strategy-expert`

作为老板的长期 AI 战略合伙人，处理目标与增长、现有战略诊断、产品或方向判断、方案比较、同行研究和历史决策复盘。它不会一上来输出冗长计划，而是先识别真正需要决定的问题，呈现最强支持面和反对面，再给出当前倾向、信心等级和什么证据会让它改判；最终决定权始终留给用户。

适合这样问：

- “结合我的业务，未来 6 个月增长应该押在哪条主线上？”
- “这个产品要不要做？先帮我找出真正的战略取舍。”
- “看看这些同行，哪些是商业对标，哪些只能借鉴一个机制？”

常见产出：真正决策问题 → 已确认事实与关键未知 → 最强正反论证 → 当前倾向与信心 → 改判条件。纯排班、周任务、材料写作和详细项目管理会被明确路由到其他能力。

### AI私聊成交专家

`$zg-private-chat-sales-assistant`

先读取产品知识库、目标客户画像、真实案例与服务边界，再诊断客户私聊中的表层说法和真实顾虑。它会判断对话处于关系、需求、产品还是决策阶段，从价值、信任、效果、适配、风险、价格、时间和决策权等类型中选择一个主方法，生成自然、可信、可直接发送的下一条回复。

适合这样问：

- “客户说有点贵，我应该怎么回？这是前后五轮聊天。”
- “先读取我的产品卡和客户画像，再分析这段私聊卡在哪里。”
- “客户说要和合伙人商量，给我应对方法、原理和可直接发送的话术。”

常见产出：成交阶段与疑虑假设 → 应对方法 → 背后原理 → 可发送话术 → 下一步分支。知识不足时会先补产品和客户信息，不编造案例、效果、稀缺性或承诺，也不会用羞辱、恐吓和虚假紧迫感逼单。

### ZG · 引流品设计师

`$zg-lead-product-designer`

为免费、低价或体验型入口产品寻找一个客户看得懂、能完成、可验收且可以规模交付的小结果。它会先识别后端产品和购买前问题，再区分课程主题、传播渠道、工具手段与客户结果；通过一票否决和八项评分收敛一个主方案，用统一成品倒推交付，并设计自然承接与真实付费验证。

适合这样问：

- “我想做一个 99 元三天体验课，应该让客户完成什么结果？”
- “这个引流品看起来很丰富，为什么客户还是不想买？”
- “我有三个前端产品想法，帮我淘汰不适合规模交付的方案。”

常见产出：产品角色 → 目标客户与触发场景 → 一句话结果承诺 → 最终成品与验收 → 标准化交付 → 后端承接 → 小样本验证计划。它不会把资料数量、低价或课程目录当成价值，也不会承诺保证赚钱、涨粉或成交。

### ZG · 苏格拉底问题定位

`$zg-socratic-problem-locator`

把 Agent 的专业判断与苏格拉底式检验结合起来：先使用已有上下文和材料形成少量候选解释，再用一个最有区分度的问题寻找关键证据、推翻错误解释，最后定位成可验证的问题。它不会机械追问，也不会把“水平不行”“内容不好”当成原因。

适合这样问：

- “我做了很多内容但一直没结果，先别给方案，帮我定位真正的问题。”
- “我觉得可能是我能力不行，你帮我检查这个判断是否成立。”
- “这是平台数据截图，请结合决定性证据重新判断问题在哪里。”

常见产出：自然短对话 → 候选解释更新 → 决定性证据 → 真问题 → 一个最小验证动作。

### ZG · 种草力 8 术 Lite

`$zg-seed-content-8-methods`

用问题、结果、氛围、身份、反常识、体系、卡点、损失八种术式，生成、改写或诊断朋友圈、私域和个人品牌内容。它强调一条内容只打透一个点，用真实价值帮助合适的用户看见改变的可能，而不是靠夸大、恐吓或虚假稀缺推动成交。

适合这样问：

- “帮我把这段介绍改成不硬卖的朋友圈。”
- “我有用户反馈，怎么写成真实、有说服力的案例内容？”
- “这条朋友圈为什么显得很营销？帮我诊断，不要直接重写。”

常见产出：术式选择理由 → 可发布成稿或诊断建议 → 待核实的事实项。

### AI九宫格朋友圈助手

`$zg-ai-nine-grid-moments`

根据经历、观点、产品资料、客户案例或人设故事，从“种草自己、种草需求、种草产品”三大方向的九个主格中，只选择最适合当前素材的一格，写成真实、自然、有温度的朋友圈。默认不超过 200 字，不展示策略分析，不编造案例、数字、证言、稀缺性或收益承诺。

适合这样问：

- “根据这段经历写一条朋友圈，帮我自动选择最合适的九宫格策略。”
- “根据这份客户案例写 5 条朋友圈，每条使用不同的核心判断。”
- “这条朋友圈为什么像广告？先诊断，不要直接重写。”

常见产出：目标读者与第一目标 → 九宫格主格 → 事实边界检查 → 200 字内可发布成稿。

### WeWrite · 公众号文章全流程

`$zg-wewrite`

从一句公众号写作需求出发，自动完成热点抓取、选题、框架、素材、正文、SEO、视觉提示、微信排版，并在公众号配置完整时保存到微信公众号草稿箱。它保留降级方案：缺少发布配置时生成本地预览，缺少图片配置时输出图片提示词。

适合这样问：

- “帮我写一篇公众号文章，主题是中小企业怎么用 AI 做获客。”
- “用交互模式，先给我 10 个公众号选题。”
- “把这篇 Markdown 排版成微信公众号格式并保存草稿箱。”

常见产出：公众号正文 → SEO 标题/摘要/标签 → 封面和内文配图 → 微信排版 → 草稿箱 `media_id`。

### ZG · 反常识公众号文章

`$zg-counterintuitive-wechat-article`

用“关于 XX，你知道的都是错的”这类强冲突标题，为 0 基础读者生成反常识公众号文章。默认按现象、观点、方法组织：现象部分用对话体和心理学解释打开问题，观点部分给出反常识判断，方法部分最多给 3 个可执行动作，结尾用一句有情绪冲击力的金句收束。

适合这样问：

- “用反常识结构写一篇关于 AI 获客的公众号文章。”
- “关于私域运营，你知道的都是错的，帮我写 2500 字。”
- “把这个选题改成现象、观点、方法的反常识公众号文章。”

常见产出：反常识标题 → 现象小标题 → 观点小标题 → 方法小标题 → 金句结尾。

### 热点加专业skill

`$zg-hotspot-theory`

把当天八卦、社会或商业热点，用传播学、心理学或经济学经典理论拆解，生成 60–75 秒、手机竖屏、单人口播可直接念的短视频文案。它要求区分已知事实与待核实信息，并用一个理论完成专业收口。

适合这样问：

- “把这个热点写成热点加专业短视频口播。”
- “用注意力经济拆解这个新闻，控制在 65 秒。”
- “帮我把这条八卦改成有专业观点、但不造谣的口播稿。”

常见产出：钩子标题 → 热点切片 → 理论解释 → 核心观点 → 金句结尾 → 互动钩子。

## 使用原则与边界

- 先给真实处境、真实材料和真实目标；信息不足时，Skill 会保留事实空位，而不是自行补齐。
- `zg-seed-content-8-methods` 不捏造案例、数据、证言、稀缺性或身份背书，不依靠羞辱、恐吓和不切实际的收益承诺促成交。
- `zg-ai-nine-grid-moments` 默认一条只选一个九宫格主格；用户未明确要求产品种草时，不出现产品名称、价格、虚假限时或强成交口号。
- 医疗、法律、投资等高风险问题需要专业人士和当地规则的进一步核验。
- `zg-socratic-problem-locator` 不把尚未被反驳的解释当成真相；用户要求停止或换题时会立即结束当前问题链。
- `zg-ai-strategy-expert` 给出倾向但不替用户决定；动态经营数据和市场事实需要当次核验，未经确认不会写入长期决策记录。
- `zg-private-chat-sales-assistant` 必须先获得产品与目标客户信息；客户明确拒绝或要求停止联系时，会停止推进并尊重边界。
- `zg-lead-product-designer` 不把课程目录、工具功能或低价本身当成客户结果；不设计故意残缺的升单诱饵，也不把收入、成交和涨粉写成无条件保证。

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
│   ├── zg-ai-nine-grid-moments/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   ├── references/
│   │   └── scripts/
│   ├── zg-ai-strategy-expert/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── references/
│   ├── zg-counterintuitive-wechat-article/
│   ├── zg-customer-case-collector/
│   ├── zg-daofa-content-framework/
│   ├── zg-hotspot-theory/
│   ├── zg-lead-product-designer/
│   ├── zg-persona-story-collector/
│   ├── zg-private-chat-sales-assistant/
│   ├── zg-product-info-collector/
│   ├── zg-seed-content-8-methods/
│   ├── zg-socratic-problem-locator/
│   ├── zg-wewrite/
│   └── zg-xuan-ti-fan-yi-qi/
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
