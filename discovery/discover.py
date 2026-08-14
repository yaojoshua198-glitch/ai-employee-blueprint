#!/usr/bin/env python3
"""发现工具 —— 从业务描述到 AI 员工候选。

本工具是可运行的 FDE（前线部署工程）思维证明：你可以把一个模糊的业务痛点，
产出一份结构化的 Discovery 画布加一个 AI 员工候选骨架，而无需先写任何 AI 代码。

用法 Usage:
    python discover.py --process "采购工程师核查 BOM" --pain "耗时且容易不一致"
    python discover.py --process "..." --pain "..." --json

依赖: 仅用 Python 3 标准库。
"""
import argparse
import json
import datetime


def discover(process: str, pain: str) -> str:
    return f"""# 发现画布

**业务过程:** {process}
**痛点:** {pain}

## 任务（拆解工作）
1. ...
2. ...
3. ...

## AI 机会（AI 可承担的部分）
- [ ] 检索
- [ ] 比对
- [ ] 基于规则的校验
- [ ] 报告生成

## AI 员工候选
**角色:** ...
**职责:**
- ...
**技能:**
- ...

---
_由 ai-employee-blueprint/discovery 生成 · {datetime.date.today().isoformat()}_
"""


def main():
    ap = argparse.ArgumentParser(
        description="把业务描述转化为 AI 员工候选。"
    )
    ap.add_argument("--process", required=True, help="业务过程")
    ap.add_argument("--pain", required=True, help="痛点")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    args = ap.parse_args()

    canvas = discover(args.process, args.pain)
    if args.json:
        print(json.dumps(
            {"process": args.process, "pain": args.pain, "canvas": canvas},
            ensure_ascii=False, indent=2,
        ))
    else:
        print(canvas)


if __name__ == "__main__":
    main()
