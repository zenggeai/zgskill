# 道法术器内容框架教练｜使用说明

版本：0.1.0（试用初版）｜制作日期：2026-09-16

## 它只帮你完成什么

先搞清楚自己主要帮助谁、核心解决什么问题，再通过对话建立道、法、术、器四层的长期内容板块。
不要求你提前懂定位、价值观或底层原理。指导思想可选，想不出来不用填。
最终得到个人内容框架；同意保存后，可另外得到访谈进度，用于下一次继续。

## 给曾哥：这次提供了什么

这是实际的 Skill 源文件包，不是只有一份需求说明。已写入分步访谈、分类规则、回答不上来的分支、真实材料优先、本人确认、成果模板与进度保存规则。
原《选题.pdf》没有整份放入分发包；只整理了必要的个人框架作参考，避免将他人笔记、案例数据和私人记录一起分发。
这不是插件商店条目，没有发布到任何商店，也没有在学员设备上安装。先在本地 Codex 试用，验证后再决定是否另行打包成插件。

本包只有 Markdown 和 YAML 等说明文件，不包含安装脚本、账号密钥、服务器或自动上传功能。但运行时仍使用你所选 AI 产品：不是离线模型，提交的资料按所用平台规则处理。客户材料请脱敏。

## 先安装：本地 Codex 试用

按核对日期的 OpenAI 官方文档，本地个人 Skill 可放在 `$HOME/.agents/skills`。本次先采用这一简单路径；正式的跨团队／目录分发可再考虑插件。

将压缩包解压，得到名为 `daofa-content-framework` 的文件夹。把整个文件夹放到当前用户的 `.agents/skills` 目录；不要只复制 SKILL.md，也不要多套一层同名目录。

Mac／Linux 的示意路径：
```text
~/.agents/skills/daofa-content-framework/SKILL.md
```

Windows 原生环境的用户目录示意：
```text
%USERPROFILE%\.agents\skills\daofa-content-framework\SKILL.md
```

Windows 使用 WSL／远程环境时，放在 Codex 实际运行环境的 HOME 下，而不是不相关的宿主目录。
如果已有同名文件夹，先比较并备份旧版本，不直接覆盖。

也可以把解压后的文件夹提供给 Codex，让它根据真实路径安装；可复制下面这段说明：

```text
请把我提供的 daofa-content-framework 文件夹安装为当前用户的本地 Skill。
先确认源文件夹实际路径并检查 SKILL.md 的 name、description 和所有相对引用。
将整个文件夹复制到 Codex 当前运行环境 HOME 下的 .agents/skills/daofa-content-framework。
不要只复制 SKILL.md，不要额外套同名目录；如果源目录已经在目标位置，不要重复复制。
若存在旧版本，先说明差异并征求是否替换；若需要权限，正常请求权限，不绕过限制。
完成后检查目标文件及依赖是否齐全，告诉我实际安装路径。
不要声称仅检查文件就等于 Codex 已发现并成功运行了它；我会在界面确认并试用。
```

Codex 文档说明会自动检测本地 Skill 变化。未出现时，重启后再检查名称、目录层级及禁用配置。界面入口因宿主而异；Codex CLI／IDE 可用 `/skills` 查看，或输入 `$` 选择。

## 再启动：不是装完自动弹出问卷

新建或打开自己的内容工作区，启动一次对话。在 Codex 中显式调用：

```text
$daofa-content-framework
带我一步一步搭建我的道法术器内容框架。
```

从零也能开始，AI应该先问业务和客户，而不是一次让你填写完整问卷。
已有资料时，把文件或可读路径提供给 Codex，例如：

```text
$daofa-content-framework
这是我的业务介绍和过去写过的内容，请先读资料，只问还不清楚的部分，再带我建立框架。
```

这里的触发写法是 Codex 用法。其他宿主是否能安装文件夹、在哪里发现 Skill、用何种调用入口，要以其实际支持为准；不是把压缩包传到任何聊天软件就会自动安装。

## 学员实际会经历什么

确认核心问题 → 从经历中挖内容 → 共创道法术器板块 → 检查和本人确认。

每次只回答一个主要问题。不知道就直接说“不知道”，AI应该换成场景问题或给少量候选供你纠正。
有时AI会归纳：“这可能体现了某种原则。”它是候选解释，你可以否定；不需要为了配合AI而认同。

可以随时说：
```text
先给我看现在的框架草稿，不要继续追问。
这里不像我，把这项删掉。
今天先到这里，请把框架和进度保存到当前工作区。
读取我的访谈进度，继续上次的内容框架。
只改“术”，其他部分保留。
```

保存会先取得许可；默认建议工作区内的 `content-framework/本人/`，保存 `内容框架.md` 与 `访谈进度.md`。无法写文件时会提供可复制内容，不能假装保存成功。
每个学员使用自己的工作区，或在一个工作区内使用不同代号。不要把学员资料放进共享的 Skill 安装目录。

## 文件结构

```text
daofa-content-framework/
  SKILL.md                         核心规则与阶段流程
  agents/openai.yaml               显示名称与默认启动提示
  references/interview-guide.md    访谈问题与分支
  references/classification-rules.md  分类、依据与质量标准
  references/zengge-reference.md   曾哥的结构样本
  references/example-dialogue.md   明确标为假设的示范对话
  assets/framework-template.md     成品模板
  assets/progress-template.md      进度模板
  README.md                        本说明
  TESTING.md                       真实试用与回归检查清单
  VALIDATION.json                  包结构检查记录，不是实测报告
```

## 先试用，再分发

建议先找三位需求不同的学员实际试用，例如面向客户的律师、教育从业者、实体或专业服务老板。每个新开对话，不带入别人的资料。
重点检查：是否抓住核心问题；是否每轮少量提问；回答不上来能否继续；是不是生成本人板块而非套例子；是否允许无指导思想；能否从保存记录继续。
记录AI在哪一轮问偏、跳步、编造或强行分类；把这些失败写入TESTING.md，再修改相应规则。不要只检查最后那张表是否漂亮。

本次完成的是文件结构与静态规则检查；未在真实 Codex 会话或真实学员身上进行端到端测试。Skill 是模型可读取的工作流程，不是保证每次行为完全一致的硬编码程序。试用反馈用于继续改进。

## 技术依据与方法来源

方法来源：用户在本次对话明确的目标，以及《选题.pdf》第1页（四层定义）、第15—18页（定位与内容分层）、第20页（真实素材来源）。本包只复制必要结构，未核实或推广原稿的外部理论与对标数据。
访谈分支、阶段确认、进度记录和文件结构是本次实现设计。

技术文档核对日期：2026-09-16。以下是技术来源，不是每次访谈需要打开的材料：
```text
OpenAI Build skills
https://developers.openai.com/codex/build-skills
（访问时转向 OpenAI 的 learn.chatgpt.com 文档）

OpenAI Plugins — Build skills
https://developers.openai.com/plugins/build/skills

OpenAI — Testing Agent Skills Systematically with Evals
https://developers.openai.com/blog/eval-skills
```
