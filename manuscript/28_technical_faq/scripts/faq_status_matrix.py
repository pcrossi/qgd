#!/usr/bin/env python3
"""
Generates a self-contained status matrix of the objections in Chapter 28.

The goal is not to calculate new physics. The script documents the conservative
classification used in the technical FAQ, so that the table can be regenerated
and audited without depending on historical files external to the manuscript.
"""

from pathlib import Path


ITEMS = [
    {
        "objection": "Does the action change to match numbers?",
        "answer": "No. Background, boundary, source, constraint, projector, and observable change.",
        "status": "methodological definition",
        "action": "preserve the official action and declare external data",
    },
    {
        "objection": "Is GDQ the Standard Model renamed?",
        "answer": "No. The Standard Model appears only as a sectorial operational reduction.",
        "status": "effective reduction",
        "action": "do not invert the deductive chain",
    },
    {
        "objection": "Was 3D Perelman applied in 8D?",
        "answer": "The application is sectorial by factorization; mixed backgrounds require a full Hessian.",
        "status": "conditional theorem",
        "action": "indicate product or mixed domain",
    },
    {
        "objection": "Was Born assumed?",
        "answer": "Born is operational in the physical Hilbert space; the individual event requires an apparatus.",
        "status": "structurally closed",
        "action": "separate probability from registration mechanism",
    },
    {
        "objection": "Is Bell/no-signalling proven?",
        "answer": "The geometry of entanglement is formulated; real apparatuses are an extension.",
        "status": "future operational program",
        "action": "calculate marginals with real impedances",
    },
    {
        "objection": "Are ghosts/BRST ontology?",
        "answer": "No. They are auxiliary quotient auditing language, when used.",
        "status": "ontological classification",
        "action": "use Tr_phys log K_phys as the intrinsic object",
    },
    {
        "objection": "Do good numbers prove everything?",
        "answer": "No. They reinforce derived chains, but do not replace derivation.",
        "status": "numerical criterion",
        "action": "classify comparison and freeze parameters",
    },
    {
        "objection": "Are absolute masses predicted from nothing?",
        "answer": "No. Units require calibration; the theory targets dimensionless ratios.",
        "status": "metrology",
        "action": "separate dimensional ruler from geometric ratio",
    },
]


def render_table() -> str:
    lines = [
        "---",
        'title: "Output — FAQ status matrix"',
        "---",
        "",
        "# Output — FAQ status matrix",
        "",
        "| Objection | Short answer | Status | Recommended action |",
        "|---|---|---|---|",
    ]
    for item in ITEMS:
        lines.append(
            f"| {item['objection']} | {item['answer']} | {item['status']} | {item['action']} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    out = Path(__file__).with_name("output_faq_status_matrix.md")
    out.write_text(render_table(), encoding="utf-8")
    print(f"File generated: {out.name}")


if __name__ == "__main__":
    main()
