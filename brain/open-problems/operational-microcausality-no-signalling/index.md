---
title: Operational microcausality and no-signalling
status: open
concepts:
  - microcausality
  - no-signalling
  - measurement
  - future data
  - retarded response
---

# Operational microcausality and no-signalling

## Problem

Chapter 3 separates global two-boundary dependence from operational signalling.
It does not prove the full measurement-level no-signalling theorem.

There is operational signalling to the past only if a future apparatus choice
`a` changes an earlier observable distribution:

$$
P(x\mid a)\neq P(x).
$$

No-signalling requires:

$$
\boxed{
P(x\mid a)=P(x).
}
$$

If `y` denotes future results not accessible at the earlier event, one must
prove that marginalization removes the dependence:

$$
P(x\mid a)=\sum_yP(x,y\mid a)
$$

or:

$$
P(x\mid a)=\int P(x,y\mid a)\,dy.
$$

## Required later work

For an apparatus, one must construct:

- admissible global background;
- physical Hessian and domain;
- reconstructed Lorentzian operator;
- retarded Green function;
- conditioned normalized measure;
- marginalization proof;
- stability of the two-boundary problem.

## Status

Open as an operational theorem for measurement. It does not reopen the
definition of the causal contour `gamma`.

## Source

`manuscrito/03_complex_causality/03.7 - Microcausalidade e dados futuros.md`

