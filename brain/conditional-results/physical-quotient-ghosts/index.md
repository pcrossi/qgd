---
title: Physical quotient and ghosts
status: active
concepts:
  - ghosts
  - physical quotient
  - gauge
  - Ward
  - Slavnov-Taylor
---

# Physical quotient and ghosts

## Statement

In GDQ, ghosts are not fundamental degrees of freedom. The intrinsic object is
the physical quotient of perturbations by redundant directions. Ghost fields
may be used as an auxiliary representation of the Jacobian of a chosen gauge
section.

## Mathematical object

The physical perturbation space is

$$
\mathcal V_{\rm phys}
=\ker C\cap\mathcal D_{\rm bordo}/\operatorname{Im}R.
$$

A gauge section `F[A]=0` introduces

$$
\Delta_{\rm FP}[A]
=\det\left(
\frac{\delta F[A^g]}{\delta g}
\right)_{g=1}.
$$

This is a coordinate Jacobian.

## Ward and Slavnov-Taylor

If the reduced operator is spectrally covariant,

$$
L_{A^g}=g^{-1}L_Ag,
$$

then trace cyclicity gives the Ward identity. In the abelian sector:

$$
q^\mu\Pi_{\mu\nu}(q)=0.
$$

The non-abelian analogue is the Slavnov-Taylor identity for the effective
functional of the quotient.

## Limits

This closes the ghost objection only in sectors where the operator,
constraints and domain are constructed. It does not replace the need to build
`P_phys` for each concrete background.

## Sources

- `manuscrito/04_action_consistency/04.7 - O que significa consistência em loops.md`
- `manuscrito/notes/action/Quociente físico, fantasmas e identidades de calibre.md`
