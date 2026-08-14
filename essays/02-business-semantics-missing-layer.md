# 02 — Business Semantics Are the Missing Layer in Enterprise AI
# 02 — 业务语义是企业 AI 缺失的那一层

**Thesis:** Most enterprise AI fails not because the model is weak, but because
the business's *meaning* was never encoded. RAG retrieves text; semantics
encodes judgment.
**论点：** 大多数企业 AI 失败，不是因为模型弱，而是因为业务的*含义*从未被编码。RAG 检索文本；语义编码判断。

---

Ask a manufacturing company what a "valid BOM" is, and you get a shrug followed
by a five-page tribal document. Ask an HR team what "good performance" means,
and you get three managers with three answers. This is the real bottleneck —
not token cost, not model size.
问一家制造企业"合格的 BOM 是什么"，你会先看到耸肩，接着是一份五页的"部落知识"文档。问 HR 团队"好的绩效"意味着什么，你会得到三位经理三种答案。这才是真正的瓶颈——不是 token 成本，也不是模型规模。

LLMs are brilliant at *language* and terrible at *meaning* they were never
given. RAG helps: it retrieves the five-page document. But retrieval is not
understanding. The model can quote the standard and still misapply it, because
nobody told it *which clause governs which situation*.
大模型擅长*语言*，却不擅长它从未被赋予的*含义*。RAG 有帮助：它能检索那五页文档。但检索不等于理解。模型可以引用标准，却仍然误用，因为没人告诉它*哪条条款适用于哪种情形*。

**Business semantics** is the layer that makes meaning explicit and machine-
usable:
**业务语义**是让含义显式化、可被机器使用的那一层：

- **Ontology** — what the entities are (BOM line, material class, standard)
  and how they relate.
  **本体**——实体是什么（BOM 行、材料类别、标准）以及它们如何关联。
- **Rules** — the limits and constraints a human applies without thinking.
  **规则**——人类不假思索就应用的限值与约束。
- **Evidence mapping** — the link between a claim ("parameter X out of range")
  and the exact source that proves it.
  **证据映射**——一条断言（"参数 X 超范围"）与证明其成立的精确来源之间的链接。

Once this layer exists, the AI stops guessing and starts *citing*. A finding
becomes auditable. A wrong answer becomes debuggable, because you can see which
rule fired.
一旦这一层存在，AI 就停止猜测、开始*引用*。一条发现变得可审计。一个错误答案变得可调试，因为你能看到是哪条规则被触发。

This is why the BOM and performance-evaluation cases in this portfolio lead
with semantics, not with the agent diagram. The agent is the easy part. The
semantic layer is the moat — and it is also the part enterprises consistently
skip, which is exactly why their AI pilots don't survive contact with reality.
正因如此，本作品集里的 BOM 与绩效评价案例都从语义起手，而非从 Agent 图起手。Agent 是容易的部分。语义层才是护城河——也是企业一贯跳过、因而它们的 AI 试点一碰现实就垮掉的部分。
