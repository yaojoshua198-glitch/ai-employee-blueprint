# AI Employee Blueprint — Canonical Schema · 规范蓝图（Canonical Schema）

This is the single source of truth for every case in this portfolio.
A "Case File" is a repository (or document) generated from a Blueprint that
conforms to this schema. The generator `generate_casefile.py` consumes a
Blueprint JSON and renders the standard Case File markdown.
这是本作品集中每个案例的唯一事实来源。一份"Case File"是由符合本 schema 的 Blueprint 生成出来的仓库（或文档）。生成器 `generate_casefile.py` 读取 Blueprint JSON 并渲染出标准的 Case File markdown。

> Contract note · 协议说明：this schema is the "AI Employee Blueprint 统一协议" that
> downstream build / deploy steps (local OaaS, digital-colleague-deployer)
> are designed to consume. Keep it stable; version with `schema_version`.
> 本 schema 即下游构建/部署步骤（local OaaS、digital-colleague-deployer）所消费的"AI Employee Blueprint 统一协议"。保持稳定，用 `schema_version` 做版本管理。

## `schema_version` · 模式版本

`string` — e.g. `"1.0"`. Bump on breaking changes. · 例如 `"1.0"`。发生破坏性变更时递增。

## `meta` · 元信息

| Field | Type | Required | Notes · 说明 |
|---|---|---|---|
| `name` | string | yes | Case / repo title · 案例/仓库标题 |
| `tagline` | string | no | One-line description · 一句话描述 |
| `domain` | string | no | Industry / function · 行业/职能 |
| `status` | string | no | e.g. "Public reference case" · 例如"公开参考案例" |

## `business_problem` · 业务问题

| Field | Type | Required | Notes · 说明 |
|---|---|---|---|
| `description` | string | yes | The real business pain, in business language · 用业务语言描述的真实痛点 |
| `why_existing_fails` | string | no | Why the current human / tool workflow breaks · 现有人工/工具流程为何失效 |

## `reframing` · 重构

| Field | Type | Required | Notes · 说明 |
|---|---|---|---|
| `how` | string | yes | How the work is reframed as AI-employee work · 如何把工作重构为 AI 员工的工作 |
| `ai_employee.role` | string | yes | The role the AI employee plays · AI 员工扮演的角色 |
| `ai_employee.responsibilities` | string[] | no | What it is accountable for · 它负责什么 |
| `ai_employee.tasks` | string[] | no | Concrete tasks it performs · 它执行的具体任务 |

## `business_semantics` · 业务语义

| Field | Type | Required | Notes · 说明 |
|---|---|---|---|
| `overview` | string | no | Why semantics matter here · 语义为何重要 |
| `layers` | object[] | no | Each · 每项：`name`, `captures`（含义见下） |

## `agent_architecture` · Agent 架构

| Field | Type | Required | Notes · 说明 |
|---|---|---|---|
| `overview` | string | no | How agents coordinate · 各 Agent 如何协同 |
| `agents` | object[] | no | Each · 每项：`name`, `role`, `inputs`, `outputs` |
| `workflow` | string[] | no | Ordered stage names · 有序的阶段名称 |

## `harness` · 约束框架

| Field | Type | Required | Notes · 说明 |
|---|---|---|---|
| `overview` | string | no | Why the harness exists · 为何需要 Harness |
| `context` | string | no | What the agent can see · Agent 能看到什么 |
| `tools` | string | no | What it can call · 它能调用什么 |
| `rules` | string | no | Hard constraints · 硬性约束 |
| `guardrails` | string | no | Safety boundaries · 安全边界 |
| `human_in_the_loop` | string | no | Where a human must approve · 人工必须在何处审批 |

## `evaluation` · 评估

| Field | Type | Required | Notes · 说明 |
|---|---|---|---|
| `method` | string | no | How quality is measured · 如何衡量质量 |
| `metrics` | object[] | no | Each · 每项：`name`, `target`（指标名，目标） |
| `human_review` | string | no | Sign-off process · 签字/复核流程 |

## `demo` · 演示

| Field | Type | Required | Notes · 说明 |
|---|---|---|---|
| `what` | string | no | What the demo shows · 演示展示什么 |
| `how_to_run` | string | no | Command to run it · 运行命令 |

## `implementation` · 实现

| Field | Type | Required | Notes · 说明 |
|---|---|---|---|
| `tech_stack` | string[] | no | Listed **last** on purpose · 刻意排在**最后** |
| `notes` | string | no | Caveats, e.g. "no client data used" · 注意事项，例如"未使用客户数据" |

---

### Design rule · 设计准则

Tech stack is the *last* section of every Case File, not the first.
The narrative order is always · 技术栈是每个 Case File 的*最后*一节，而非开头。叙述顺序始终为：

**Business Problem → Why It Fails → Reframing → Semantics →
Architecture → Harness → Evaluation → Demo → Implementation**
**业务问题 → 为何失败 → 重构 → 语义 → 架构 → 约束框架 → 评估 → 演示 → 实现**
