---
title: GDQ variational data
status: active
concepts:
  - variation
  - fields
  - measure
  - boundary
---

# GDQ variational data

## Definition

For the chapter 4 variational problem, the central fields are

$$
\Phi=(g,f,\bar f).
$$

The field `f` may be rewritten as

$$
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f).
$$

The measure is constitutive:

$$
\mathcal U=\frac{\rho}{(4\pi z_\tau)^n}.
$$

## Fixed structural data

Within one variational problem, the following are fixed unless explicitly
changed as a different sector:

- topology of `M`;
- causal contour `gamma`;
- complex dimension `n`;
- dimensionless cutoff convention `Lambda_C`;
- regularity class;
- admissible Hermitian/KT class;
- declared initial and boundary data.

## Normalization constraint

The measure satisfies

$$
\int_M\mathcal U\,dV_g=1.
$$

This can be handled by restricting variations or by using a multiplier
`lambda(tau)`. The multiplier is not a new interaction.

## Sources

- `manuscrito/04_action_consistency/04.3 - Campos, medida e dados estruturais.md`
- `manuscrito/04_action_consistency/04.5 - O princípio variacional e suas equações.md`
