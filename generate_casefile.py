#!/usr/bin/env python3
"""把一份符合 blueprint.schema.md 的 Blueprint 渲染为**中文** Case File。

本脚本证明这套方法是可以运行的，而不只是被描述出来：作品集里每个案例
都是由一份 Blueprint 经本生成器产出的。

用法 Usage:
    python generate_casefile.py templates/bom-blueprint.json
    python generate_casefile.py templates/bom-blueprint.json -o templates/bom-casefile.md

依赖: 仅用 Python 3 标准库。
"""

import json
import sys
import argparse
import datetime


def _bullet_block(items, indent=0):
    pad = "  " * indent
    out = []
    for it in items:
        out.append(f"{pad}- {it}")
    return "\n".join(out)


def render(bp: dict) -> str:
    L = []
    meta = bp.get("meta", {})
    name = meta.get("name", "未命名案例")
    L.append(f"# {name}")
    tagline = meta.get("tagline")
    if tagline:
        L.append(f"> {tagline}\n")
    domain = meta.get("domain", "")
    status = meta.get("status", "")
    if domain or status:
        L.append(f"**领域:** {domain}  ·  **状态:** {status}\n")

    # --- 业务问题（刻意放在最前）---
    bsec = bp.get("business_problem", {})
    L.append("## 业务问题\n")
    L.append(bsec.get("description", "") + "\n")
    why = bsec.get("why_existing_fails")
    if why:
        L.append("### 为什么现有流程会失败\n")
        L.append(why + "\n")

    # --- 重构 ---
    ref = bp.get("reframing", {})
    L.append("## 我如何重构这项工作\n")
    L.append(ref.get("how", "") + "\n")
    emp = ref.get("ai_employee", {})
    L.append("### AI 员工定义\n")
    if emp.get("role"):
        L.append(f"- **角色:** {emp['role']}")
    if emp.get("responsibilities"):
        L.append("- **职责:**")
        L.append(_bullet_block(emp["responsibilities"], 1))
    if emp.get("tasks"):
        L.append("- **任务:**")
        L.append(_bullet_block(emp["tasks"], 1))
    L.append("")

    # --- 业务语义 ---
    sem = bp.get("business_semantics", {})
    L.append("## 业务语义\n")
    L.append(sem.get("overview", "") + "\n")
    if sem.get("layers"):
        L.append("| 层 | 捕获什么 |")
        L.append("|---|---|")
        for l in sem["layers"]:
            L.append(f"| {l.get('name', '')} | {l.get('captures', '')} |")
        L.append("")

    # --- Agent 架构 ---
    arch = bp.get("agent_architecture", {})
    L.append("## Agent 架构\n")
    L.append(arch.get("overview", "") + "\n")
    if arch.get("agents"):
        L.append("| Agent | 角色 | 输入 | 输出 |")
        L.append("|---|---|---|---|")
        for a in arch["agents"]:
            L.append(
                f"| {a.get('name', '')} | {a.get('role', '')} | "
                f"{a.get('inputs', '')} | {a.get('outputs', '')} |"
            )
        L.append("")
    wf = arch.get("workflow")
    if wf:
        L.append("**工作流:** " + " → ".join(wf) + "\n")

    # --- 约束框架（Harness）---
    h = bp.get("harness", {})
    L.append("## 约束框架\n")
    L.append(h.get("overview", "") + "\n")
    for key, label in [
        ("context", "上下文"),
        ("tools", "工具"),
        ("rules", "规则"),
        ("guardrails", "护栏"),
        ("human_in_the_loop", "人在环"),
    ]:
        if h.get(key):
            L.append(f"- **{label}:** {h[key]}")
    L.append("")

    # --- 评估 ---
    ev = bp.get("evaluation", {})
    L.append("## 评估\n")
    L.append(ev.get("method", "") + "\n")
    if ev.get("metrics"):
        L.append("| 指标 | 目标 |")
        L.append("|---|---|")
        for m in ev["metrics"]:
            L.append(f"| {m.get('name', '')} | {m.get('target', '')} |")
        L.append("")
    if ev.get("human_review"):
        L.append(f"**人工复核:** {ev['human_review']}\n")

    # --- 演示 ---
    d = bp.get("demo", {})
    if d:
        L.append("## 演示\n")
        if d.get("what"):
            L.append(d["what"] + "\n")
        if d.get("how_to_run"):
            L.append("```\n" + d["how_to_run"] + "\n```\n")

    # --- 实现（刻意放在最后）---
    impl = bp.get("implementation", {})
    L.append("## 实现\n")
    if impl.get("tech_stack"):
        L.append("**技术栈:** " + ", ".join(impl["tech_stack"]) + "\n")
    if impl.get("notes"):
        L.append(impl["notes"] + "\n")

    L.append("---\n")
    L.append(
        f"_由 ai-employee-blueprint schema 生成 "
        f"· {datetime.date.today().isoformat()}_\n"
    )
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(
        description="把 Blueprint 渲染为中文 Case File。"
    )
    ap.add_argument("blueprint", help="Blueprint JSON 文件路径")
    ap.add_argument("-o", "--output", help="写入文件而非标准输出")
    args = ap.parse_args()

    try:
        with open(args.blueprint, encoding="utf-8") as f:
            bp = json.load(f)
    except FileNotFoundError:
        sys.exit(f"error: 找不到 blueprint: {args.blueprint}")
    except json.JSONDecodeError as e:
        sys.exit(f"error: {args.blueprint} 不是合法 JSON: {e}")

    out = render(bp)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(out)
        print(f"wrote {args.output}")
    else:
        print(out)


if __name__ == "__main__":
    main()
