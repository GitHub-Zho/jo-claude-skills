#!/usr/bin/env python3
"""Validate the paper-reasoning-deep-dive package beyond basic YAML checks."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/design-rationale.md",
    "references/evidence-audit.md",
    "references/mechanism-and-math.md",
    "references/lineage-and-future.md",
    "references/output-template.md",
)

REQUIRED_TRIGGERS = (
    "read paper",
    "精读论文",
    "explain why each design decision",
)


def fail(messages: list[str]) -> int:
    for message in messages:
        print(f"ERROR: {message}")
    return 1


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    errors: list[str] = []

    for relative_path in REQUIRED_FILES:
        if not (root / relative_path).is_file():
            errors.append(f"missing required file: {relative_path}")

    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return fail(errors)

    text = skill_path.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not frontmatter:
        errors.append("SKILL.md has no valid YAML frontmatter block")
    else:
        metadata = frontmatter.group(1)
        if "name: paper-reasoning-deep-dive" not in metadata:
            errors.append("frontmatter name does not match the folder name")
        lowered = metadata.lower()
        for trigger in REQUIRED_TRIGGERS:
            if trigger.lower() not in lowered:
                errors.append(f"description is missing trigger phrase: {trigger}")

    linked_references = set(
        re.findall(r"\]\((references/[^)]+\.md)\)", text)
    )
    expected_references = {
        item for item in REQUIRED_FILES if item.startswith("references/")
    }
    missing_links = expected_references - linked_references
    for reference in sorted(missing_links):
        errors.append(f"SKILL.md does not link to {reference}")

    openai_yaml = root / "agents/openai.yaml"
    if openai_yaml.is_file():
        yaml_text = openai_yaml.read_text(encoding="utf-8")
        if "allow_implicit_invocation: true" not in yaml_text:
            errors.append("implicit invocation is not explicitly enabled")
        if "$paper-reasoning-deep-dive" not in yaml_text:
            errors.append("default_prompt does not mention the skill explicitly")

    if errors:
        return fail(errors)

    print(f"VALID: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
