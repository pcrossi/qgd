---
title: Question 04
status: closed conditionally
source: questão_4.md
---

# Question 04

Question 04 asks whether the GDQ functional action is mathematically
consistent and whether it supports perturbative quantum loops.

## Canonical source

- `questão_4.md`

## Current answer

The official action is preserved:

$$
\mathcal S_{\rm GDQ}
=
\int_\gamma
\int_{\mathcal M_\mathbb C}
\frac{\hbar}{\Lambda_C^2}
\mathcal U
\mathcal L_0
\sqrt g\,d^{2n}z
\frac{d\tau}{\tau}.
$$

Question 04 is closed as variational consistency plus conditional
perturbative quantisation. It is not a nonperturbative all-background proof.

## Main points

- $n=4$ and $d=8$ follow from Q2/Q3.
- $z_\tau=\tau+i\nu_0t$ is the dimensionally correct causal variable.
- $\gamma$ is the structural Sudarshan causal prescription.
- $\mathcal U$ is constitutive, not an independent multiplier:

$$
\mathcal U
=\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}.
$$

- The effective Q2 action is a reduced/EFT check, not the official action.
- BRST/ghosts are auxiliary perturbative audit language, not GDQ ontology.

## Relation to the newer chapter-04 memory

The refined internal formulation of loops is through the physical Hessian:

$$
\Gamma_{\rm GDQ}^{(1)}
=\frac12\operatorname{Tr}_{\rm phys}
\ln\operatorname{Hess}\mathcal S_{\rm GDQ}.
$$

Thus Q4's BRST and form-factor language must be read as auxiliary sectoral
translation, not as replacement of the official Hessian formulation.

