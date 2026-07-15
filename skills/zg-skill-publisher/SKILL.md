---
name: zg-skill-publisher
description: 将用户给出的文档、文件夹或已有能力整理成 ZG Skills 仓库里的标准 Skill，并发布到 GitHub。适用于“帮我把这个文档变成 skill”“整理成标准 skill 格式”“命名要用 zg 统一”“更新 README 并发布到 GitHub”“检查不要上传配置/输出稿/敏感文件”等任务。默认目标仓库是 zenggeai/zgskill，所有对外 Skill 名必须使用 `zg-` 前缀。
---

# 曾哥skill发布

把用户给出的材料整理成可发布的 ZG Skill。目标不是单纯搬文件，而是产出一个可被 Agent 正确发现、安装、调用，并且不会误传隐私或运行数据的标准 Skill。

## 核心原则

- 对外 Skill ID 一律使用 `zg-` 前缀，文件夹名和 `SKILL.md` 的 `name` 必须完全一致。
- 保留能力本身的品牌名或产品名，例如标题可以叫 WeWrite，但 Skill ID 必须类似 `zg-wewrite`。
- 只把可复用能力发布到 GitHub，不上传用户的真实配置、密钥、运行历史、生成稿或本地缓存。
- 修改仓库时只提交本次任务相关文件，保留用户已有的未跟踪或无关改动。
- 发布到 GitHub 前必须做本地校验；发布后必须确认远端分支指向新提交。

## 工作流程

### 1. 明确输入和目标

先判断用户给的是哪类材料：

- 单个文档：提炼成 `SKILL.md`，必要时拆出 `references/`。
- 已有文件夹：整理为标准 Skill 目录，保留脚本、资源、参考资料。
- 已发布但命名不一致的 Skill：重命名目录、`SKILL.md` 的 `name`、README 调用方式。
- 多个文件混杂的工作目录：区分可发布资源和本地运行数据。

如果目标仓库未说明，默认使用当前工作区的 ZG Skills 仓库。不要把无关文件纳入本次发布。

### 2. 规范命名

生成或修正 Skill ID：

1. 转为小写短横线格式。
2. 缺少 `zg-` 前缀时补上。
3. 文件夹名、`SKILL.md` frontmatter `name`、README 安装命令保持一致。
4. 避免使用空格、下划线、大写字母或中文作为 Skill ID。

示例：

| 原始名称 | 标准 Skill ID |
| --- | --- |
| We Write | `zg-wewrite` |
| 公众号排版助手 | `zg-wechat-formatting` |
| skill publisher | `zg-skill-publisher` |

### 3. 整理标准目录

每个 Skill 至少包含：

```text
skills/<zg-skill-name>/
├── SKILL.md
└── agents/openai.yaml
```

按需保留：

- `references/`：长说明、框架、模板、规则、判断标准。
- `scripts/`：可重复执行的工具脚本。
- `assets/`：图片、模板、字体等输出资源。
- `toolkit/`：运行时工具代码，只有原能力确实依赖时才保留。

不要额外创建 README、安装指南、变更日志等非必要文档，除非用户明确要求。

### 4. 写好 SKILL.md

`SKILL.md` frontmatter 只放 `name` 和 `description`。

`description` 必须写清：

- 这个 Skill 做什么。
- 用户说哪些话时应该触发。
- 它处理哪些文件、目录或发布任务。
- 关键约束，例如 ZG 命名、GitHub 发布、敏感文件排除。

正文写工作流程，不写空泛介绍。优先包含：

- 输入判断。
- 文件整理规则。
- 命名和 README 同步规则。
- 发布前安全检查。
- 提交和推送协议。
- 完成后如何向用户汇报。

### 5. 补 agents/openai.yaml

至少包含：

```yaml
interface:
  display_name: "曾哥skill发布"
  short_description: "整理并发布 ZG Skills 到 GitHub"
  default_prompt: "Use $zg-skill-publisher to turn a document into a standardized ZG Skill and publish it to GitHub."
```

`default_prompt` 必须显式包含 `$zg-skill-publisher`。

### 6. 更新仓库 README

新增或改名 Skill 后，同步更新根 README：

- 顶部 Skills 数量徽章。
- 能力一览表。
- 单独安装命令。
- 更新命令。
- Skill 全目录中的介绍、调用名和常见产出。
- 项目结构树。

如果只是修正命名，确保 README 中不再残留旧调用名、旧目录名或旧安装命令。

### 7. 发布前安全检查

提交前必须检查：

```bash
find skills/<zg-skill-name> -maxdepth 3 -type f \( -name 'config.yaml' -o -name 'style.yaml' -o -name 'history.yaml' -o -path '*/output/*' \) -print
rg -n "appid|secret|api_key|sk-|token|password|access_key" skills/<zg-skill-name>
```

允许示例文件中出现占位符，例如 `config.example.yaml` 里的 `your_api_key`。发现真实凭证、运行历史或生成稿时，不要提交，先移除或加入 `.gitignore`。

同时检查工作区：

```bash
git status --short
git diff --cached --name-status
```

只暂存本次相关文件。不要提交用户无关的未跟踪文件。

### 8. 校验 Skill

运行标准校验：

```bash
python3 <skill-creator>/scripts/quick_validate.py skills/<zg-skill-name>
```

如果本机缺少依赖导致校验脚本不能运行，用 Ruby 或系统 YAML 做等价检查，至少确认：

- `SKILL.md` 存在。
- frontmatter 是合法 YAML。
- `name` 存在且等于目录名。
- `description` 存在且非空。
- `name` 只包含小写字母、数字和短横线。

### 9. 提交并发布到 GitHub

只有在用户明确要求发布时才推送。发布前如果需要联网或真实 GitHub 操作，遵守当前环境的联网工具与审批要求。

推荐提交信息：

- 新增 Skill：`Add <zg-skill-name> skill`
- 重命名 Skill：`Rename <old-name> skill to <zg-skill-name>`
- 修正格式：`Standardize <zg-skill-name> skill`

推送后确认：

```bash
git status --short --branch
git log -1 --oneline
git ls-remote origin refs/heads/main
```

远端提交号必须和本地最新提交一致。

## 完成汇报

最终回复用户时说明：

- 新 Skill 名和目录。
- 是否已推送到 GitHub。
- 最新提交号。
- 安装或调用命令。
- 哪些文件被刻意排除，例如真实配置、历史记录、输出稿。
- 仍留在本地但未处理的无关文件。
