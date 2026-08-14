# 03 — Why Agent Quality Is a Harness Problem
# 03 — 为什么 Agent 质量是一个 Harness 问题

**Thesis:** A weak model in a strong harness beats a strong model in a weak
harness. Quality comes from the *system around* the model, not the model alone.
**论点：** 强 Harness 里的弱模型，胜过弱 Harness 里的强模型。质量来自模型*周围的系统*，而非模型本身。

---

There is a tempting arms race in agent building: chase the biggest model,
expect quality to follow. It rarely does, because an agent's output is decided
less by its model than by everything *around* it.
Agent 构建里有一场诱人的军备竞赛：追逐最大的模型，指望质量随之而来。这很少发生，因为一个 Agent 的输出，与其说由它的模型决定，不如说由它*周围的一切*决定。

The **harness** is that everything:
**Harness** 就是那一切：

- **Context** — what the agent is allowed to see. Give it the wrong window and
  even a frontier model will hallucinate from absence.
  **上下文**——Agent 被允许看到什么。给它错误的窗口，即便前沿模型也会因"信息缺失"而幻觉。
- **Tools** — what it can call. A model that can't look up the standard can
  only invent one.
  **工具**——它能调用什么。一个查不到标准的模型，只能发明一个。
- **Rules** — hard constraints it must obey ("every finding cites a clause").
  **规则**——它必须遵守的硬性约束（"每条发现都引用条款"）。
- **Guardrails** — boundaries it cannot cross (read-only on source systems).
  **护栏**——它不能越过的边界（对源系统只读）。
- **Human-in-the-loop** — the gate where a person approves before anything
  ships.
  **人在环**——任何东西交付前由人批准的关卡。

Each of these is a lever you control *without* changing the model. And they
compound: good context reduces hallucination, rules turn output into claims,
guardrails keep it safe, and the human gate catches what slips through.
这些每一个都是你*无需更换模型*就能控制的杠杆。而且它们会复利：好的上下文减少幻觉，规则把输出变成断言，护栏保证安全，人工关卡兜住漏网之鱼。

This reframes the build order. You do not start with "which model." You start
with "what should this employee be allowed to see, do, and prove — and where
does a human check it?" The model is a component you can swap; the harness is
the product.
这重构了构建顺序。你不是从"用哪个模型"开始，而是从"这名员工该被允许看什么、做什么、证明什么——以及人在哪里检查它？"开始。模型是可替换的部件；Harness 才是产品。

In practice this is why the cases here always show the harness as its own
section, placed *before* evaluation. If the harness is right, evaluation is
mostly about tuning. If the harness is wrong, no model upgrade saves you.
也正因如此，这里的案例总把 Harness 作为独立一节，放在评估*之前*。Harness 对了，评估基本只是调参；Harness 错了，换多强的模型都救不回来。
