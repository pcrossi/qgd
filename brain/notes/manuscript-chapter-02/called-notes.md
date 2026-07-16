---
title: Manuscript chapter 02 called notes
status: active
concepts:
  - chapter 02 notes
  - geometrization notes
  - axiom audit
  - preservation map
---

# Manuscript chapter 02 called notes

This file records the notes and audits explicitly called by Chapter 2.

## 1. Bulk local R4xT4 and complex dimension four

Source:

`manuscrito/notes/geometrization/Bulk local R4xT4 e dimensão complexa quatro.md`

Role:

Verifies the consequences of the structural choice:

$$
M=\mathbb R^4\times T^4.
$$

Main results:

$$
\dim_{\mathbb R}M=8,
\qquad
\dim_{\mathbb C}M=4.
$$

Since both factors are parallelizable:

$$
TM\cong M\times\mathbb R^8,
\qquad
w_2(TM)=0.
$$

Status:

Definition verified. It does not dynamically select the bulk.

## 2. Hermitian, Kähler, and Bismut connection

Source:

`manuscrito/notes/geometrization/Estrutura Hermitiana, Kähler e conexão de Bismut.md`

Role:

Fixes the geometric distinction:

$$
J^2=-I,
\qquad
g(JX,JY)=g(X,Y),
\qquad
\omega_H(X,Y)=g(JX,Y).
$$

Kähler strict means:

$$
d\omega_H=0.
$$

Bismut torsion is:

$$
H=d_J^c\omega_H.
$$

Status:

Geometric definition. `H` is not an independent official action variable.

## 3. Decomposition of `f`

Source:

`manuscrito/notes/geometrization/Decomposição do campo f em densidade e fase.md`

Role:

Stores the exact algebra behind:

$$
f=-\frac{S_I}{\hbar}+i\frac{S_R}{\hbar},
$$

and:

$$
\rho=e^{-(f+\bar f)/2}=e^{S_I/\hbar}.
$$

The real Hermitian part of the gradient term is:

$$
\operatorname{Re}\left(
g^{\mu\bar\nu}
\partial_\mu f
\partial_{\bar\nu}\bar f
\right)
=
\frac1{\hbar^2}g^{\mu\bar\nu}
\left(
\partial_\mu S_I\partial_{\bar\nu}S_I
+\partial_\mu S_R\partial_{\bar\nu}S_R
\right).
$$

Status:

Exact identity.

## 4. GDQ measure, kernel dimension, and variation

Source:

`manuscrito/notes/geometrization/Medida GDQ, dimensão do kernel e variação.md`

Role:

Records the heat-kernel origin of the power:

$$
(4\pi\tau)^{-d/2}.
$$

For `d=2n=8`, this gives `(4 pi tau)^-4`.

The GDQ measure is:

$$
\mathcal U
=(4\pi z_\tau)^{-n}e^{-(f+\bar f)/2}.
$$

For fixed `z_tau`:

$$
\delta\mathcal U
=-\frac12\mathcal U(\delta f+\delta\bar f).
$$

Status:

Exact identity.

## 5. Official GDQ action term by term

Source:

`manuscrito/notes/geometrization/Ação oficial da GDQ termo a termo.md`

Role:

Records the scalar integrand:

$$
\mathcal L_0
=
\tau\left(
\mathcal R
+g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}
-n.
$$

`L_0` is dimensionless. The physical stationarity is applied to:

$$
S_{\rm phys}=\operatorname{Re}\mathcal S_{\rm GDQ}.
$$

Status:

Fundamental definition.

## 6. Geometric soliton versus material soliton

Source:

`manuscrito/notes/geometrization/Sóliton geométrico versus sóliton material.md`

Role:

Prevents identifying a Ricci soliton directly with matter.

Ricci gradient soliton:

$$
\operatorname{Ric}+\nabla^2f=\lambda g.
$$

Material background must satisfy:

$$
\delta\operatorname{Re}\mathcal S_{\rm GDQ}=0
$$

under declared domain and constraints, and its projected physical Hessian must
be nonnegative after removing gauge and collective modes.

Status:

Conditional criterion.

## 7. Axiom-to-theorem audit

Source:

`manuscrito/02_geometrization/axiom_to_theorem_audit.md`

Role:

Classifies which Chapter 2 elements remain axioms and which were promoted.

Promoted or derived:

- `n=4` from chosen bulk;
- spin existence from parallelizability;
- `16` spin structures on `T^4`;
- Bismut connection by uniqueness theorem;
- heat-kernel exponent four by dimension;
- dimension of `tau`;
- decomposition of `f`;
- variation of `U`;
- Lorentzian metric from a clock form;
- clock-form selection in the adopted cosmological background;
- spin antiperiodicity conditional on holonomy `-1`;
- transport global-local under pointed-family, localization, and gap
  hypotheses.

Still structural inputs:

- official action;
- local geometric class;
- causal contour class;
- physical global and boundary conditions;
- physical scales not yet derived.

Status:

Audit. It is authoritative for Chapter 2 classification.

## 8. Preservation map

Source:

`manuscrito/02_geometrization/preservation_map.md`

Role:

Records what was preserved from the historical chapter and what was corrected.

Important preserved ideas:

- dynamic geometry matters;
- Hamilton-Perelman flow architecture;
- density-phase mapping through `f`;
- weighted measure;
- Bohm term as density derivative structure;
- possible future dimension selection by index or anomaly;
- Lagrangian leaf as possible projection model;
- torsion as carrier of internal circulation.

Important corrections:

- Perelman `W` is auxiliary, not the official action;
- `f=-S/hbar` is wrong as a full mapping;
- Bohm term is not universally repulsive;
- Ricci soliton is not automatically a material particle;
- UV regularity is not automatic;
- phase is not automatically torsion.

Status:

Editorial audit, not independent physical source.

