"""Structural checks for the badge-graded Lab 02 prompt journal."""

from __future__ import annotations

import re
from pathlib import Path


JOURNAL = Path(__file__).parents[1] / "lab02_prompts.md"


def journal_text() -> str:
    assert JOURNAL.exists(), "Create week02/lab02_prompts.md from the template"
    text = JOURNAL.read_text(encoding="utf-8")
    forbidden = ("YOUR RESPONSE", "TODO", "[paste here]")
    assert not any(marker.lower() in text.lower() for marker in forbidden), (
        "Replace every template marker in lab02_prompts.md"
    )
    return text


def section(text: str, heading: str, next_heading_level: int = 2) -> str:
    pattern = rf"(?ms)^{re.escape(heading)}\s*$\n(.*?)(?=^{'#' * next_heading_level}\s|\Z)"
    match = re.search(pattern, text)
    assert match, f"Missing required section: {heading}"
    return match.group(1).strip()


def test_all_prompt_sections_and_blocks_exist():
    text = journal_text()
    headings = [
        "## Function 1: make_greeting",
        "### Initial prompt 1",
        "### Refined CPTF prompt 1",
        "## Function 2: is_even",
        "### Initial prompt 2",
        "### Refined CPTF prompt 2",
        "## Function 3: count_vowels",
        "### Initial prompt 3",
        "### Refined CPTF prompt 3",
        "## Test-guided revision",
        "## Explanation and reflection",
    ]
    for heading in headings:
        assert heading in text, f"Missing required heading: {heading}"

    prompt_blocks = re.findall(r"```text\s*\n(.+?)\n```", text, re.DOTALL)
    assert len(prompt_blocks) == 6, "Include six nonempty fenced text prompt blocks"
    assert all(block.strip() for block in prompt_blocks)


def test_test_guided_revision_has_required_length():
    text = journal_text()
    content = section(text, "## Test-guided revision")
    assert len(re.findall(r"\b[\w'-]+\b", content)) >= 75


def test_explanation_and_reflection_has_required_length():
    text = journal_text()
    content = section(text, "## Explanation and reflection")
    assert len(re.findall(r"\b[\w'-]+\b", content)) >= 100
