#!/usr/bin/env python3
"""Extract repeated keywords and lightweight risk signals from a job description."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


STOPWORDS = {
    "and", "or", "the", "with", "for", "to", "of", "in", "a", "an", "is", "are",
    "you", "we", "our", "your", "will", "be", "as", "on", "by", "from",
    "岗位", "职责", "要求", "具备", "熟悉", "相关", "优先", "能够", "以及", "进行", "负责",
}

RISK_RULES = [
    ("possible_ai_washing", [r"AI Agent", r"智能体", r"大模型", r"AIGC"], [r"API", r"RAG", r"评估", r"workflow", r"工具", r"模型", r"工程"]),
    ("possible_sales_disguised", [r"转化", r"客户", r"线索", r"销售", r"业绩", r"成交"], [r"产品需求", r"原型", r"PRD", r"用户研究"]),
    ("inflated_junior_role", [r"应届", r"实习", r"初级"], [r"独立负责", r"全生命周期", r"架构", r"带领团队", r"从0到1"]),
    ("vague_role", [r"完成领导", r"其他工作", r"快速成长", r"抗压", r"有激情"], [r"具体", r"交付", r"指标"]),
]


def extract(text: str, limit: int = 40) -> list[tuple[str, int]]:
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9+#.\-]{1,}|[\u4e00-\u9fff]{2,}", text)
    normalized = [token.lower() for token in tokens if token.lower() not in STOPWORDS]
    counts = Counter(normalized)
    return counts.most_common(limit)


def risk_signals(text: str) -> list[str]:
    findings: list[str] = []
    for name, positive_patterns, balancing_patterns in RISK_RULES:
        positive = any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in positive_patterns)
        balancing = any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in balancing_patterns)
        if positive and not balancing:
            findings.append(name)
    return findings


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract high-frequency JD keywords and simple risk signals.")
    parser.add_argument("file", help="JD text file")
    parser.add_argument("--limit", type=int, default=40)
    parser.add_argument("--risks", action="store_true", help="Also print lightweight JD reality-check risk signals")
    args = parser.parse_args()

    text = Path(args.file).read_text(encoding="utf-8")
    print("# keywords")
    for keyword, count in extract(text, args.limit):
        print(f"{keyword}\t{count}")
    if args.risks:
        print("\n# risk_signals")
        risks = risk_signals(text)
        if risks:
            for risk in risks:
                print(f"- {risk}")
        else:
            print("- none")


if __name__ == "__main__":
    main()