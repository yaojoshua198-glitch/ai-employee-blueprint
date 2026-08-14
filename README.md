# ai-employee-blueprint

**The method for turning real business work into AI employees. · 把真实业务工作转化为 AI 员工的方法论。**

This is the mother repository of my portfolio. It holds the canonical schema
that every case (BOM validation, performance evaluation, virtual power plant)
is generated from — so the cases are *instances of one method*, not five
unrelated demos.
这是我作品集的母体仓库。它持有 canonical schema（规范蓝图），BOM 校验、绩效评价、虚拟电厂等每个案例都由它生成——因此这些案例是*同一方法的不同实例*，而非五个互不相关的 Demo。

```
Business       业务
   ↓
Workflow       作业流
   ↓
Semantic       语义
   ↓
Agent          Agent
   ↓
Harness        约束框架
   ↓
Validation     验证
```

## What lives here · 这里有什么

| Path | What it is · 是什么 |
|---|---|
| `blueprint.schema.md` | The canonical schema (source of truth) · 规范蓝图（唯一事实来源） |
| `generate_casefile.py` | Renders a Blueprint JSON into a Case File (stdlib only) · 把 Blueprint JSON 渲染成 Case File（仅用标准库） |
| `templates/` | Sample Blueprint(s) + generated Case File(s) · 示例 Blueprint + 生成的 Case File |
| `essays/` | My thinking on AI employees, semantics, harness, FDE · 我对 AI 员工、语义、Harness、FDE 的思考 |
| `discovery/` | From a business description to an AI employee candidate · 从业务描述到 AI 员工候选 |

## The core idea · 核心思想

Most enterprise AI fails not because models are weak, but because the
business's *meaning* was never made explicit — what a "valid BOM" means, what
"good performance" means. This repo treats **business semantics** as a first-class
layer, and treats **agent quality as a harness problem**, not a model problem.
大多数企业 AI 失败，不是因为模型弱，而是因为业务的*含义*从未被显式表达——什么是"合格的 BOM"，什么是"好的绩效"。本仓库把**业务语义**作为一等层，并把**Agent 质量视为 Harness 问题**而非模型问题。

## How a case is produced · 案例如何生成

1. Write a Blueprint JSON that conforms to `blueprint.schema.md`.
   编写一份符合 `blueprint.schema.md` 的 Blueprint JSON。
2. Run the generator · 运行生成器：
   ```bash
   python generate_casefile.py templates/bom-blueprint.json -o templates/bom-casefile.md
   ```
3. The output is a Case File with the fixed narrative order · 输出是一份 Case File，遵循固定的叙述顺序：
   **Business Problem → Why It Fails → Reframing → Semantics →
   Architecture → Harness → Evaluation → Demo → Implementation**
   **业务问题 → 为何失败 → 重构 → 语义 → 架构 → 约束框架 → 评估 → 演示 → 实现**
   Tech stack is always *last* · 技术栈永远排在*最后*。

## Discovery (not a separate repo) · 发现阶段（不是独立仓库）

The "AI Scenario Discovery" step is a phase inside this method, not a fifth
repository. See `discovery/discover.py`: feed it a business process and a pain
point, get back a Discovery canvas and an AI employee candidate skeleton.
"AI 场景发现"这一步是本方法内部的一个阶段，而非第五个仓库。见 `discovery/discover.py`：输入一个业务过程与痛点，得到一份 Discovery 画布与 AI 员工候选骨架。

## Cases generated from this schema · 由本 schema 生成的案例

- `bom-ai-employee` — multi-agent BOM validation · 多 Agent 的 BOM 校验
- `performance-evaluation-agent` — evidence-based performance evaluation · 基于证据的绩效评价
- `virtual-power-plant-ai-employees` — reframing a traditional system as AI employees · 把传统系统重构为 AI 员工

Each case repository's README links back here as its source of method.
每个案例仓库的 README 都会回链到这里，作为它的方法来源。

## Read the thinking · 读读这些思考

Start with [`essays/01-why-ai-employees-differ-from-assistants.md`](essays/01-why-ai-employees-differ-from-assistants.md).
建议从 [`essays/01-why-ai-employees-differ-from-assistants.md`](essays/01-why-ai-employees-differ-from-assistants.md) 开始。

---

<sub>Draft — not yet published. This repository is the planned home of the
"AI Employee Blueprint 统一协议" referenced by downstream build / deploy tooling.
· 草稿——尚未发布。本仓库是下游构建/部署工具所引用的"AI Employee Blueprint 统一协议"的计划落点。</sub>
