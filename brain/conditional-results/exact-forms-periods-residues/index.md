---
title: Exact forms, periods, and residues
status: conditionally_demonstrated
concepts:
  - exact forms
  - periods
  - residues
  - contour
  - monodromy
---

# Exact forms, periods, and residues

## Statement

For a regular single-valued function `F` in a neighborhood of a closed contour:

$$
\oint_\gamma dF=0.
$$

This cancellation does not erase periods, monodromy, cuts, or residues.

## Cases

Exact regular form:

$$
\omega=dF
\quad\Longrightarrow\quad
\oint_\gamma\omega=0.
$$

Closed but not exact:

$$
d\omega=0,
\qquad
[\omega]\neq0
\quad\Longrightarrow\quad
\oint_\gamma\omega
\text{ may be nonzero}.
$$

Meromorphic form:

$$
\oint_\gamma\omega
=2\pi i
\sum_p\operatorname{Res}_p\omega.
$$

## Status

Demonstrated under stated analytic hypotheses. Quantization needs additional
integrality and normalization data.

## Source

`manuscrito/03_complex_causality/03.3 - O contorno causal e as formas exatas.md`

