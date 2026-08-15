#!/usr/bin/env python3
"""Simple GDQ numerical result classifier.

Classification:
    documentary tool / rule example.

The goal is to make it explicit when a calculation should be called a direct
evaluation, consistency test, phenomenological comparison, or blind prediction.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent / "output_classify_result.md"


@dataclass(frozen=True)
class Scenario:
    name: str
    formula_derived: bool
    target_used_before: bool
    has_convergence: bool
    has_analytic_limit: bool
    apparatus_independent: bool


SCENARIOS = [
    Scenario("formula already derived, no target data", True, False, False, True, True),
    Scenario("mesh refined against analytical limit", True, False, True, True, True),
    Scenario("parameter inferred from target", False, True, False, False, False),
    Scenario("formula frozen and subsequent comparison", True, False, True, False, True),
    Scenario("no target, multiple observables, measured apparatus", True, False, True, True, True),
]


def classify(s: Scenario) -> str:
    if s.target_used_before:
        return "reverse engineering or fit"
    if s.formula_derived and s.has_convergence and s.has_analytic_limit and s.apparatus_independent:
        return "strong prediction or strong metrological test"
    if s.formula_derived and s.has_convergence:
        return "controlled phenomenological comparison"
    if s.formula_derived and s.has_analytic_limit:
        return "consistency test"
    if s.formula_derived:
        return "direct evaluation"
    return "exploratory"


def main() -> None:
    lines = ["# Output — result classifier\n\n"]
    lines.append("Classification: documentary tool / rule example.\n\n")
    lines.append("| scenario | classification |\n")
    lines.append("|---|---|\n")
    for scenario in SCENARIOS:
        lines.append(f"| {scenario.name} | {classify(scenario)} |\n")
    lines.append("\n## Rule\n\n")
    lines.append("If the experimental target entered before the formula, do not call it a prediction.\n")
    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
