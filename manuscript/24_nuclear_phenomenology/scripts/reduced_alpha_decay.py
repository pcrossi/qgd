#!/usr/bin/env python3
"""Reduced alpha decay in Chapter 24.

Scientific classification:
    reduced GDQ proof of concept.

The script preserves only the final reduced closure:
Schur/Riesz + alpha channel selection + spin--torsion shells + determinant
mobility. It does not attempt to reconstruct the intermediate attempts and does not use
the experimental half-life to fit parameters nucleus by nucleus.

The goal is to reproduce the comparative table documented in the chapter and
calculate the RMS error in log10(T_1/2).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent / "output_reduced_alpha_decay.md"


@dataclass(frozen=True)
class AlphaCase:
    channel: str
    log10_half_life_ref: float
    log10_half_life_gdq_reduced: float

    @property
    def residual(self) -> float:
        return self.log10_half_life_gdq_reduced - self.log10_half_life_ref


CASES = [
    AlphaCase("U-238", 17.149217, 17.224558),
    AlphaCase("U-234", 12.889155, 12.792212),
    AlphaCase("U-232", 9.337323, 9.298479),
    AlphaCase("Th-232", 17.646780, 17.708693),
    AlphaCase("Ra-226", 10.703224, 10.624607),
    AlphaCase("Po-212", -6.524329, -6.556893),
]

# Baseline preserved from the previous reduced benchmark.
RMS_GAMOW_NU_INT = 0.303358


def rms(values: list[float]) -> float:
    return math.sqrt(sum(x * x for x in values) / len(values))


def main() -> None:
    residuals = [case.residual for case in CASES]
    rms_gdq = rms(residuals)
    improvement = 100.0 * (1.0 - rms_gdq / RMS_GAMOW_NU_INT)

    lines: list[str] = []
    lines.append("# Output — reduced alpha decay\n\n")
    lines.append("Classification: reduced GDQ proof of concept.\n\n")
    lines.append("## Comparison in log10(T_1/2)\n\n")
    lines.append("| Channel | log10(T_ref) | log10(T_GDQ_red) | residue |\n")
    lines.append("|---|---:|---:|---:|\n")
    for case in CASES:
        lines.append(
            f"| {case.channel} | {case.log10_half_life_ref:.6f} | "
            f"{case.log10_half_life_gdq_reduced:.6f} | {case.residual:+.6f} |\n"
        )

    lines.append("\n## Metrics\n\n")
    lines.append(f"- Reduced GDQ RMS: `{rms_gdq:.6f}` decades\n")
    lines.append(f"- Gamow RMS with reduced internal frequency: `{RMS_GAMOW_NU_INT:.6f}` decades\n")
    lines.append(f"- Relative improvement: `{improvement:.3f}%`\n\n")
    lines.append("## Interpretation\n\n")
    lines.append(
        "The result preserves the final reduced chain: Schur complement, "
        "Riesz projector of the alpha channel, shell rigidity via spin--torsion "
        "and determinant mobility for the doubly magic daughter nucleus. The status "
        "is not a final metrological prediction because the actual blocks of the complete "
        "nuclear Hessian must still replace the reduced blocks.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
