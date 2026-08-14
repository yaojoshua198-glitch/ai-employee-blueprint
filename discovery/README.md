# Discovery · 发现阶段

这是 `ai-employee-blueprint` 方法内部的“AI 场景发现”阶段，不是一个独立仓库。它把 FDE（前线部署工程）思维变成可运行的工具：输入一个业务过程与痛点，输出一份 Discovery 画布与 AI 员工候选骨架——**在写任何 AI 代码之前**就能看清机会。

## 运行

```bash
python discover.py --process "采购工程师核查 BOM" --pain "耗时且容易不一致"
```

加 `--json` 可输出 JSON，方便接入下游。

## 它产出什么

- **业务过程 / 痛点**：你输入的原话。
- **任务拆解**：把这项工作拆成可执行的步骤。
- **AI 机会**：哪些步骤适合由检索、比对、规则校验、报告生成来承担。
- **AI 员工候选**：角色、职责、技能的骨架。

## 设计意图

发现阶段的价值在于**先结构化问题，再谈技术**。它对应旗舰方法“业务 → 语义 → Agent”链条里的 Discovery 环节，也是 Portfolio 主线“From Business Work to AI Employees”的可运行证明。
