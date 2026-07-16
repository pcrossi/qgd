---
title: Manuscript chapter 03 called notes
status: active
concepts:
  - chapter 03 notes
  - causality notes
  - preservation map
---

# Manuscript chapter 03 called notes

This file records the notes and audits explicitly called by Chapter 3.

## 1. Exact derivatives, endpoint states, and causal continuation

Source:

`manuscrito/notes/causality/Derivadas exatas, estados de extremidade e continuação causal.md`

If:

$$
L'=L+\frac{dF(q,t)}{dt},
$$

then:

$$
S'[q]=S[q]+F(q_1,t_1)-F(q_0,t_0).
$$

The Lorentzian kernel transforms as:

$$
K'(q_1,t_1;q_0,t_0)
=e^{iF(q_1,t_1)/\hbar}
K(q_1,t_1;q_0,t_0)
e^{-iF(q_0,t_0)/\hbar}.
$$

Equivalently:

$$
U'(t_1,t_0)
=V(t_1)U(t_1,t_0)V(t_0)^{-1},
\qquad
V(t)=e^{iF(t)/\hbar}.
$$

Status:

Endpoint states must transform with the action. Euclidean continuation can
make the factors nonunitary, so domain, states, and reflection condition must
be transported too.

## 2. Causal complex variable

Source:

`manuscrito/notes/causality/Variável causal complexa - dimensão, simetrias e unicidade condicional.md`

In the minimal affine class:

$$
z=a\tau+ibt.
$$

Homogeneity requires:

$$
[b]=L^2T^{-1}.
$$

After real rescaling:

$$
z_\tau=\tau+i\nu_0t.
$$

Time reversal gives:

$$
t\mapsto -t
\quad\Longrightarrow\quad
z_\tau\mapsto\bar z_\tau.
$$

Status:

Conditional uniqueness in the minimal affine class.

## 3. Exact forms, periods, and residues

Source:

`manuscrito/notes/causality/Formas exatas, períodos e resíduos no contorno causal.md`

If `F` is globally defined near `gamma`:

$$
\oint_\gamma dF=0.
$$

If `omega` is closed but cohomologically nontrivial, its period may be
nonzero. If it is meromorphic:

$$
\oint_\gamma\omega
=2\pi i\sum_p\operatorname{Res}_p\omega.
$$

Status:

Separates cancellation, periods, and residues. Quantization still needs
integral classes and physical normalization.

## 4. Reality of action on a complex contour

Source:

`manuscrito/notes/causality/Realidade de uma ação integrada em contorno complexo.md`

For:

$$
I_+=\int_{\gamma_+}\omega(z),
$$

choose the conjugate branch `gamma_-` so that:

$$
\int_{\gamma_-}\omega(z)=\overline{I_+}.
$$

Then:

$$
I=I_++\overline{I_+}
=2\operatorname{Re}I_+
\in\mathbb R.
$$

Status:

Reality follows from reflection of the one-form plus compatible orientation,
not from contour shape alone.

## 5. Quantization by monodromy and integral class

Source:

`manuscrito/notes/causality/Quantização por monodromia e classe integral.md`

Local sections:

$$
\Psi_i=\sqrt\rho\,e^{iS_i/\hbar}.
$$

On overlaps:

$$
\Psi_i=e^{i\chi_{ij}}\Psi_j,
$$

so:

$$
S_i-S_j=\hbar\chi_{ij}
\quad\text{modulo }2\pi\hbar.
$$

Prequantization condition:

$$
\left[\frac{F_A}{2\pi}\right]
\in H^2(M,\mathbb Z).
$$

Holonomy:

$$
\operatorname{Hol}_\gamma(A)
=\exp\left(i\oint_\gamma A\right).
$$

Status:

Integer or half-integer periods follow from holonomy and integral-class
conditions after normalization. Residue calculus alone is insufficient.

## 6. Preservation map

Source:

`manuscrito/03_complex_causality/preservation_map.md`

Preserved:

- Wick is useful but requires domain, singularities, and boundary control;
- exact derivatives become endpoint data;
- `z_tau=tau+i nu_0 t` replaces invalid `tau+i t`;
- retarded and advanced sectors may appear in global prescriptions;
- closed contours cancel exact regular terms but preserve periods, cuts, and
  residues;
- circulation and monodromy can quantize sectors.

Corrections:

- Wick does not generally violate gauge;
- advanced sectors do not imply operational retrocausality;
- closed `gamma` does not prove unitarity;
- residue calculus does not fix physical charge units;
- monotonicity in `tau` is not physical time arrow by itself.

Status:

Editorial audit. It preserves historical content while preventing overclaims.

