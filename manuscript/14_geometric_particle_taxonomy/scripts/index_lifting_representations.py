#!/usr/bin/env python3
"""
GDQ — Chapter 14 / Index lifting to representations

Objective:
    Verify the count of Weyl components of an effective generation and the
    additive lifting to three index units.

Classification:
    Discrete symbolic verification. No fitting, experimental data, or
    calibration.

Output:
    scripts/output_index_lifting_representations.md
"""

from pathlib import Path


MULTIPLETS = [
    ("Q", 3, 2, "1/6"),
    ("u^c", 3, 1, "-2/3"),
    ("d^c", 3, 1, "1/3"),
    ("L", 1, 2, "-1/2"),
    ("e^c", 1, 1, "1"),
]


def main() -> None:
    total_one = sum(color * weak for _, color, weak, _ in MULTIPLETS)
    total_three = 3 * total_one

    lines = [
        "# Output — index lifting to representations",
        "",
        "| Multiplet | color dim | weak dim | Y | Weyl components |",
        "|---|---:|---:|---:|---:|",
    ]

    for name, color, weak, hypercharge in MULTIPLETS:
        lines.append(
            f"| `{name}` | {color} | {weak} | {hypercharge} | {color * weak} |"
        )

    lines += [
        "",
        f"- Total per local index unit: `{total_one}` Weyl components.",
        f"- Total per three stomata: `{total_three}` Weyl components.",
        "",
        "Conclusion: the local APS unit counts generations; hypercharge is a separate line.",
    ]

    out = Path(__file__).with_name("output_index_lifting_representations.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
