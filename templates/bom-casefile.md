# BOM AI Employee
> A multi-agent AI employee for BOM validation and engineering review. · 用于 BOM 校验与工程审查的多 Agent AI 员工。

**Domain · 领域:** Manufacturing engineering · 制造工程  ·  **Status · 状态:** Public reference case · 公开参考案例

## Business Problem · 业务问题

Engineers manually validate bills of materials (BOM) against material standards, parameter limits, and design rules. A single BOM can contain thousands of line items, each needing a check against the right standard and the right parameter window.

工程师手工对照材料标准、参数限值与设计规则来校验物料清单（BOM）。一张 BOM 可能包含上千个行项目，每一项都需要对照正确的标准与正确的参数窗口进行检查。

### Why It Fails · 为什么现有流程会失败

The work is repetitive retrieval and comparison at scale. Humans get fatigued, coverage is inconsistent across engineers, and feedback to design is slow because review happens late in the cycle.

这是大规模下的重复性检索与比对工作。人会疲劳，不同工程师的覆盖度不一致，而且因为审查发生在周期后段，给设计的反馈很慢。

## How I Reframed the Work · 我如何重构这项工作

Instead of one engineer doing search-compare-report end to end, reframe the work as a coordinated set of agents: a planner breaks the BOM into checkable units, retrievers pull the governing standards and material data, an executor runs the comparisons, and a reviewer gates the output before a human signs off.

不再让一名工程师端到端地做“检索—比对—报告”，而是把工作重构为一组协同的 Agent：规划器把 BOM 拆成可检查单元，检索器拉取适用的标准与材料数据，执行器跑比对，审查器在人工签字前对输出把关。

### AI Employee Definition · AI 员工定义

- **Role · 角色:** BOM Validation Engineer · BOM 校验工程师
- **Responsibilities · 职责:**
  - Detect BOM anomalies before they reach production · 在问题流入生产前发现 BOM 异常
  - Cite the standard clause that governs each finding · 为每条发现引用其适用的标准条款
  - Produce a review-ready report a human can trust · 产出人工可信、可直接审查的报告
- **Tasks · 任务:**
  - Parse the BOM into checkable items · 把 BOM 解析为可检查项
  - Retrieve applicable standards and material specs · 检索适用的标准与材料规格
  - Compare parameters against limits and rules · 对照限值与规则比对参数
  - Detect risks and inconsistencies · 发现风险与不一致
  - Draft a structured review report · 起草结构化的审查报告

## Business Semantics · 业务语义

The semantic layer is what makes a finding auditable. Without it, the agent can say 'parameter out of range' but cannot prove which rule was violated. Semantics turns a guess into an evidence-linked claim.

语义层让一条发现可被审计。没有它，Agent 只能说“参数超范围”，却无法证明违反了哪条规则。语义把一个猜测变成一条带证据的断言。

| Layer · 层 | What it captures · 捕获什么 |
|---|---|
| Ontology · 本体 | BOM entities, material classes, standard references and how they relate · BOM 实体、材料类别、标准引用及其关系 |
| Rules · 规则 | Parameter limits, compatibility constraints, design intent · 参数限值、兼容性约束、设计意图 |
| Evidence mapping · 证据映射 | Each finding linked to the exact standard clause that proves it · 每条发现都链到证明其成立的精确标准条款 |

## Agent Architecture · Agent 架构

A planner coordinates three knowledge sources and an executor, then a reviewer gates the output. The human approves the final report.

一个规划器协调三个知识源与一个执行器，再由审查器对输出把关。最终报告由人工批准。

| Agent | Role · 角色 | Inputs · 输入 | Outputs · 输出 |
|---|---|---|---|
| Planner · 规划器 | Decompose BOM review into subtasks · 把 BOM 审查拆成子任务 | BOM | Task plan · 任务计划 |
| Standards Retriever · 标准检索器 | Find governing standards · 查找适用的标准 | Part specification · 零件规格 | Standard clauses · 标准条款 |
| Materials Retriever · 材料检索器 | Fetch material specs · 获取材料规格 | Material id · 材料编号 | Material data · 材料数据 |
| Rules Engine · 规则引擎 | Apply validation rules · 应用校验规则 | Specs + rules · 规格 + 规则 | Pass / fail per item · 逐项通过/失败 |
| Executor · 执行器 | Run comparisons · 执行比对 | Plan + retrieved data · 计划 + 检索数据 | Findings · 发现 |
| Reviewer · 审查器 | Check findings quality · 检查发现质量 | Findings · 发现 | Reviewed findings · 已审查发现 |

**Workflow · 工作流:** Planner · 规划器 → Standards + Materials Retrievers · 标准+材料检索器 → Executor · 执行器 → Reviewer · 审查器 → Human Approval · 人工批准 → Final Report · 最终报告

## Harness · 约束框架

The harness constrains what the agent may do and forces evidence before any claim.

约束框架限定 Agent 能做什么，并强制在任何断言之前先有证据。

- **Context · 上下文:** BOM + standards library + material database · BOM + 标准库 + 材料数据库
- **Tools · 工具:** Standards search, material lookup, rule evaluator · 标准检索、材料查询、规则求值
- **Rules · 规则:** Every finding must cite a standard clause; no claim without evidence · 每条发现必须引用标准条款；无证据不得断言
- **Guardrails · 护栏:** Read-only on source systems; never auto-edit the BOM · 对源系统只读；绝不自动修改 BOM
- **Human-in-the-loop · 人在环:** A senior engineer approves the report before it reaches design · 高级工程师在报告到达设计之前批准

## Evaluation · 评估

Sample BOMs reviewed by both a human engineer and the AI employee; compare finding coverage and false positives.

由人工工程师与 AI 员工分别审查抽样 BOM，比较发现的覆盖率与误报率。

| Metric · 指标 | Target · 目标 |
|---|---|
| Finding recall · 发现召回率 | >= 90% vs human · 对比人工 ≥ 90% |
| False positive rate · 误报率 | < 5% |

**Human review · 人工复核:** Senior engineer signs off each report · 高级工程师对每份报告签字确认

## Demo · 演示

A public reference run on a synthetic BOM, showing findings with cited standard clauses.

在合成 BOM 上的公开参考运行，展示带标准条款引用的发现。

```
python generate_casefile.py templates/bom-blueprint.json
```

## Implementation · 实现

**Tech stack · 技术栈:** Python, LangGraph (optional), RAG over standards, JSON rules, Streamlit (demo)

Public reference architecture. No client data is used; all inputs are synthetic. · 公开参考架构。未使用任何客户数据，所有输入均为合成数据。

---

_Generated from ai-employee-blueprint schema · 由 ai-employee-blueprint schema 生成 · 2026-08-14_
