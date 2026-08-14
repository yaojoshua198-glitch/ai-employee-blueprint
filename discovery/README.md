# Discovery

FDE thinking, made runnable. · FDE 思维，做成可运行的。

`discover.py` takes a business process and a pain point and returns a
**Discovery canvas** plus an **AI employee candidate** skeleton. It is the
"AI Scenario Discovery" step from the portfolio plan — folded into this
repository as a phase, not shipped as a separate repo.
`discover.py` 接收一个业务过程与一个痛点，返回一份 **Discovery 画布** 加一个 **AI 员工候选** 骨架。它就是作品集规划里的"AI 场景发现"步骤——折进本仓库作为一个阶段，而非独立仓库发布。

```bash
python discover.py --process "采购工程师核查 BOM" --pain "耗时且容易不一致"
```

Output · 输出:

```
# Discovery Canvas · 发现画布

**Business process · 业务过程:** 采购工程师核查 BOM
**Pain point · 痛点:** 耗时且容易不一致

## Tasks (decompose the work) · 任务（拆解工作）
1. ...
...

## AI Opportunity (what AI can take on) · AI 机会（AI 可承担的部分）
- [ ] Retrieval · 检索
- [ ] Comparison · 比对
- [ ] Rule-based validation · 基于规则的校验
- [ ] Report generation · 报告生成

## AI Employee Candidate · AI 员工候选
**Role · 角色:** ...
**Skills · 技能:** ...
```

The blank lines are the point: discovery is a *conversation starter*, not a
finished design. Fill it in with the business, then promote the result into a
Blueprint JSON and run `generate_casefile.py`.
那些留白正是重点：发现是一个*对话起点*，而非完成的设计。和业务方一起填好它，再把结果提升为一份 Blueprint JSON，然后运行 `generate_casefile.py`。
