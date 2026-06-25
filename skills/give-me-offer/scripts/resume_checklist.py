#!/usr/bin/env python3
"""Lightweight text checklist for resume drafts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


RISKY_PATTERNS = [
    r"\bsignificantly\b",
    r"\bexcellent\b",
    r"\bexpert\b",
    r"\bmaster(?:ed)?\b",
    r"显著",
    r"精通",
    r"大幅",
    r"丰富经验",
]

AI_STYLE_PATTERNS = [
    r"赋能",
    r"闭环",
    r"抓手",
    r"底层逻辑",
    r"显著提升",
    r"strong ability",
    r"excellent communication",
]

DECORATION_PATTERNS = [
    r"技能条",
    r"进度条",
    r"雷达图",
    r"自我评价",
    r"兴趣爱好",
    r"\|\s*\|\s*\|",
]


def analyze(text: str, target: str = "general") -> list[str]:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    findings: list[str] = []
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    bullets = [line for line in lines if line.startswith(("-", "*", "•"))]
    headings = [line for line in lines if line.startswith("#")]

    one_page_targets = {"china", "campus", "early", "switch", "general"}
    if target in one_page_targets and len(text) > 5200:
        findings.append("Likely one-page overflow for early-career/China-facing resume; cut weak content before shrinking font.")
    elif len(text) > 7000:
        findings.append("Resume may be too long; verify whether a two-page resume is justified.")

    if len(bullets) < 4:
        findings.append("Add more concrete bullets with actions, tools, and evidence.")
    if len(headings) > 9:
        findings.append("Too many sections may fragment the one-page story; merge weak sections.")
    if target in {"china", "campus", "early", "switch"} and len(text) > 4200 and not re.search(r"求职方向|目标岗位|Target", text, flags=re.IGNORECASE):
        findings.append("3-second scan risk: target role is not obvious near the top.")

    for pattern in RISKY_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            findings.append(f"Check unsupported strong wording: {pattern}")
    for pattern in DECORATION_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            findings.append(f"Check whether this layout/content hurts recruiter scanning or ATS parsing: {pattern}")
    for pattern in AI_STYLE_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            findings.append(f"Possible AI/template tone; make it more concrete and interview-defensible: {pattern}")

    if re.search(r"AI Agent|RAG|fine[- ]?tuning|大模型|智能体|检索增强", text, flags=re.IGNORECASE) and not re.search(r"prototype|demo|原型|限制|evaluation|评估", text, flags=re.IGNORECASE):
        findings.append("AI-related claim found; classify AI skill level and add proof/limitations if needed.")
    if re.search(r"\d+%|\d+\s*(users|用户|人|万|k|K)", text) and "[confirm]" not in text:
        findings.append("Numeric claims found; verify they are confirmed and defensible.")
    if not re.search(r"GitHub|github|作品集|portfolio|项目", text, flags=re.IGNORECASE):
        findings.append("Consider adding project/portfolio evidence if relevant.")
    if target in {"china", "campus"} and not re.search(r"求职方向|目标岗位|Target", text, flags=re.IGNORECASE):
        findings.append("China-facing early-career resumes should show a clear target role near the header.")

    return findings or ["No obvious checklist issues found. Still review evidence, layout, and JD fit manually."]


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a simple resume-risk and layout checklist.")
    parser.add_argument("file", help="Resume text/Markdown file")
    parser.add_argument("--target", default="general", choices=["general", "china", "campus", "early", "switch", "senior"])
    args = parser.parse_args()

    text = Path(args.file).read_text(encoding="utf-8")
    for item in analyze(text, args.target):
        print(f"- {item}")


if __name__ == "__main__":
    main()