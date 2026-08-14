# ai-employee-blueprint

**把真实业务工作转化为 AI 员工的方法论。**

这是我作品集的母体仓库。它持有 canonical schema（规范蓝图），BOM 校验、绩效评价、虚拟电厂等每个案例都由它生成——因此这些案例是*同一方法的不同实例*，而非五个互不相关的 Demo。

```
业务现场 Field
   ↓  数据探照 + 对话（先业务，后数据）
语义 Semantic
   ↓  本体（领域/项目）+ 红线规则
Agent
   ↓  角色 / 技能 / 工作流
约束框架 Harness
   ↓  上下文 / 工具 / 规则 / 人在环
验证 Validation
   ↓  真实任务 + 人工复核 + KPI
```

## 这里有什么

| 路径 | 是什么 |
|---|---|
| `blueprint.schema.md` | 规范蓝图（唯一事实来源） |
| `generate_casefile.py` | 把 Blueprint JSON 渲染成 Case File（仅用标准库） |
| `templates/` | 示例 Blueprint + 生成的 Case File |
| `essays/` | 我对 AI 员工、语义、Harness、FDE 的思考 |
| `discovery/` | 从业务描述到 AI 员工候选 |

## 核心思想

大多数企业 AI 失败，不是因为模型弱，而是因为业务的*含义*从未被显式表达——什么是"合格的 BOM"，什么是"好的绩效"。本仓库把**业务语义**作为一等层（区分领域本体与项目本体、把红线规则写成硬约束），并把**Agent 质量视为 Harness 问题**而非模型问题：一个 AI 员工能不能上岗，看的是"企业敢不敢把一个岗位交给它"，而不是"它回答对不对"。

## 我是怎么做的

从现场到上岗，是一条有次序的链：

1. **场景发现**：先用*数据探照*把业务闭环扫一遍，标出"数据在哪"（系统自动 / 文档 / 只在人脑 / 根本没有）；再用*对话*拆岗位——先聊业务动作，最后才聊数据，避免做成 chatbot。
2. **语义化**：识别本体（领域词典 + 项目账本）与红线规则，把"含义"变成机器可读、可审计的资产。
3. **定义 Agent**：角色、技能、多 Agent 工作流。
4. **设计 Harness**：上下文、工具、硬规则、人在环审批——质量是被设计出来的，不是评出来的。
5. **验证**：真实任务 + 人工复核 + 每日 KPI（准确 / 业务影响 / 安全 / 效率）。

这套方法已在供应链风险、汽修回访等真实项目里跑通（含公开数据集与合成数据实测），不是纸面框架。

## 案例如何生成

1. 编写一份符合 `blueprint.schema.md` 的 Blueprint JSON。
2. 运行生成器：
   ```bash
   python generate_casefile.py templates/bom-blueprint.json -o templates/bom-casefile.md
   ```
3. 输出是一份 Case File，遵循固定的叙述顺序：
   **业务问题 → 为何失败 → 重构 → 语义 → 架构 → 约束框架 → 评估 → 演示 → 实现**
   技术栈永远排在*最后*。

## 发现阶段（不是独立仓库）

"AI 场景发现"这一步是本方法内部的一个阶段，而非第五个仓库。见 `discovery/discover.py`：输入一个业务过程与痛点，得到一份 Discovery 画布与 AI 员工候选骨架。

## 由本 schema 生成的案例

- [`bom-ai-employee`](https://github.com/yaojoshua198-glitch/ai-employee-blueprint/blob/main/templates/bom-casefile.md) — 多 Agent 的 BOM 校验
- [`performance-evaluation-agent`](https://github.com/yaojoshua198-glitch/ai-employee-blueprint/blob/main/templates/performance-eval-casefile.md) — 基于证据的绩效评价
- [`virtual-power-plant-ai-employees`](https://github.com/yaojoshua198-glitch/ai-employee-blueprint/blob/main/templates/virtual-power-plant-casefile.md) — 把传统系统重构为 AI 员工

每个案例仓库的 README 都会回链到这里，作为它的方法来源。

## 读读这些思考

建议从 [`essays/01-why-ai-employees-differ-from-assistants.md`](essays/01-why-ai-employees-differ-from-assistants.md) 开始。其中几篇融入了真实项目的经验：
- `02` 业务语义缺失层（领域/项目本体、红线规则）
- `03` Agent 质量是 Harness 问题（95 分框架、岗位工作循环、证据图）
- `04` 从业务流程到 AI 员工（数据探照 + 对话拆岗）
- `06` 从工作坊到前线部署（现场纪律）

---

<sub>已发布。本仓库是下游构建/部署工具所引用的"AI Employee Blueprint 统一协议"的落点。
另见我的 GitHub 主页：[yaojoshua198-glitch](https://github.com/yaojoshua198-glitch)</sub>
