#!/usr/bin/env python3
"""Verifica fatores de grupo do coeficiente não abeliano líder da Q34."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Matter:
    multiplicity: float
    index: float


def b0(
    c_adjoint: float,
    dirac: list[Matter] | None = None,
    weyl: list[Matter] | None = None,
    real_scalars: list[Matter] | None = None,
    complex_scalars: list[Matter] | None = None,
) -> float:
    value = 11.0 * c_adjoint / 3.0
    value -= 4.0 / 3.0 * sum(x.multiplicity * x.index for x in dirac or [])
    value -= 2.0 / 3.0 * sum(x.multiplicity * x.index for x in weyl or [])
    value -= 1.0 / 6.0 * sum(x.multiplicity * x.index for x in real_scalars or [])
    value -= 1.0 / 3.0 * sum(x.multiplicity * x.index for x in complex_scalars or [])
    return value


def main() -> int:
    su3 = b0(3.0, dirac=[Matter(6, 0.5)])
    su2_without_order = b0(2.0, weyl=[Matter(12, 0.5)])
    su2_with_order = b0(
        2.0,
        weyl=[Matter(12, 0.5)],
        complex_scalars=[Matter(1, 0.5)],
    )

    assert abs(su3 - 7.0) < 1e-14
    assert abs(su2_without_order - 10.0 / 3.0) < 1e-14
    assert abs(su2_with_order - 19.0 / 6.0) < 1e-14

    print(f"b0 SU(3), seis sabores Dirac: {su3:.12f}")
    print(f"b0 SU(2), doze doublets Weyl: {su2_without_order:.12f}")
    print(f"b0 SU(2), incluindo modo escalar complexo: {su2_with_order:.12f}")
    print("Todos os testes algébricos passaram.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
