# AI Employee Blueprint — 规范蓝图（Canonical Schema）

这是本作品集中每个案例的唯一事实来源。一份“Case File”是由符合本 schema 的 Blueprint 生成出来的仓库（或文档）。生成器 `generate_casefile.py` 读取 Blueprint JSON 并渲染出标准的 Case File markdown。

> 协议说明：本 schema 即下游构建/部署步骤（local OaaS、digital-colleague-deployer）所消费的“AI Employee Blueprint 统一协议”。保持稳定，用 `schema_version` 做版本管理。

## `schema_version` · 模式版本

`string` — 例如 `"1.0"`。发生破坏性变更时递增。

## `meta` · 元信息

| 字段 Field | 类型 Type | 必填 Required | 说明 Notes |
|---|---|---|---|
| `name` | string | 是 | 案例/仓库标题 |
| `tagline` | string | 否 | 一句话描述 |
| `domain` | string | 否 | 行业/职能 |
| `status` | string | 否 | 例如“公开参考案例” |

## `business_problem` · 业务问题

| 字段 Field | 类型 Type | 必填 Required | 说明 Notes |
|---|---|---|---|
| `description` | string | 是 | 用业务语言描述的真实痛点 |
| `why_existing_fails` | string | 否 | 现有人工/工具流程为何失效 |

## `reframing` · 重构

| 字段 Field | 类型 Type | 必填 Required | 说明 Notes |
|---|---|---|---|
| `how` | string | 是 | 如何把工作重构为 AI 员工的工作 |
| `ai_employee.role` | string | 是 | AI 员工扮演的角色 |
| `ai_employee.responsibilities` | string[] | 否 | 它负责什么 |
| `ai_employee.tasks` | string[] | 否 | 它执行的具体任务 |

## `business_semantics` · 业务语义

| 字段 Field | 类型 Type | 必填 Required | 说明 Notes |
|---|---|---|---|
| `overview` | string | 否 | 语义为何重要 |
| `layers` | object[] | 否 | 每项：`name`, `captures` |

## `agent_architecture` · Agent 架构

| 字段 Field | 类型 Type | 必填 Required | 说明 Notes |
|---|---|---|---|
| `overview` | string | 否 | 各 Agent 如何协同 |
| `agents` | object[] | 否 | 每项：`name`, `role`, `inputs`, `outputs` |
| `workflow` | string[] | 否 | 有序的阶段名称 |

## `harness` · 约束框架

| 字段 Field | 类型 Type | 必填 Required | 说明 Notes |
|---|---|---|---|
| `overview` | string | 否 | 为何需要 Harness |
| `context` | string | 否 | Agent 能看到什么 |
| `tools` | string | 否 | 它能调用什么 |
| `rules` | string | 否 | 硬性约束 |
| `guardrails` | string | 否 | 安全边界 |
| `human_in_the_loop` | string | 否 | 人工必须在何处审批 |

## `evaluation` · 评估

| 字段 Field | 类型 Type | 必填 Required | 说明 Notes |
|---|---|---|---|
| `method` | string | 否 | 如何衡量质量 |
| `metrics` | object[] | 否 | 每项：`name`, `target` |
| `human_review` | string | 否 | 签字/复核流程 |

## `demo` · 演示

| 字段 Field | 类型 Type | 必填 Required | 说明 Notes |
|---|---|---|---|
| `what` | string | 否 | 演示展示什么 |
| `how_to_run` | string | 否 | 运行命令 |

## `implementation` · 实现

| 字段 Field | 类型 Type | 必填 Required | 说明 Notes |
|---|---|---|---|
| `tech_stack` | string[] | 否 | 刻意排在**最后** |
| `notes` | string | 否 | 注意事项，例如“未使用客户数据” |

---

### 设计准则

技术栈是每个 Case File 的*最后*一节，而非开头。叙述顺序始终为：

**业务问题 → 为何失败 → 重构 → 语义 → 架构 → 约束框架 → 评估 → 演示 → 实现**
