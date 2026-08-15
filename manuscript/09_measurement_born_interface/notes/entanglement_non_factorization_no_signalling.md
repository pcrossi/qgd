---
title: "Entanglement, non-factorization and no-signalling"
---

# Entanglement, non-factorization and no-signalling

## 1. Statement

In the multiparticle sector, the conceptual error to avoid is to imagine two point particles exchanging signals in the reconstructed physical space. In GDQ, the joint state is a geometric section in the configuration space:

$$
Q_{AB}
=
M_A\times M_B.
$$

A separable configuration requires simultaneously:

$$
\rho_{AB}(x_A,x_B)
=
\rho_A(x_A)\rho_B(x_B),
$$

and:

$$
S_{AB}(x_A,x_B)
=
S_A(x_A)+S_B(x_B).
$$

Entanglement means the failure of at least one of these factorizations:

$$
\rho_{AB}\ne\rho_A\rho_B
\quad
\text{or}
\quad
S_{AB}\ne S_A+S_B.
$$

This failure is geometric: it belongs to the global section in $Q_{AB}$, not to a signal propagating from $A$ to $B$.

## 2. Gluing by Mayer--Vietoris

Consider a cover:

$$
Q_{AB}=U_A\cup U_B.
$$

The local phases are 1-forms:

$$
\theta_A=dS_A,
\qquad
\theta_B=dS_B.
$$

On the intersection:

$$
\theta_A|_{U_A\cap U_B}
-
\theta_B|_{U_A\cap U_B}
=
d\chi.
$$

The Mayer--Vietoris sequence organizes the global obstruction:

$$
\cdots
to
H^1(Q_{AB})
to
H^1(U_A)\oplus H^1(U_B)
to
H^1(U_A\cap U_B)
\xrightarrow{\delta}
H^2(Q_{AB})
to
\cdots .
$$

Wait, let's fix the arrow notation in line 76-85:
`\to` was translated by the subagent but some might have been left as `to`?
In the target block:
```latex
\cdots
\to
H^1(Q_{AB})
\to
H^1(U_A)\oplus H^1(U_B)
\to
H^1(U_A\cap U_B)
\xrightarrow{\delta}
H^2(Q_{AB})
\to
\cdots .
```
Yes, let's use `\to` instead of `to`.

When the gluing class is non-trivial, the global section cannot be written as the product of two independent sections. This is the topological content of the correlation.

## 3. Operational causality condition

The global correlation is only physically admissible if it does not allow operational signalling. For apparatus choices $x$ and $y$, and records $a$ and $b$, we require:

$$
P(a|x,y)
=
\sum_b P(a,b|x,y)
=
P(a|x),
$$

and:

$$
P(b|x,y)
=
\sum_a P(a,b|x,y)
=
P(b|y).
$$

Therefore:

$$
\text{global correlation}
\ne
\text{communication channel}.
$$

## 4. Reduced operational target

In the reconstructed projective sector, the ideal target of two spinorial channels is the singlet. For unit axes $\boldsymbol a$ and $\boldsymbol b$:

$$
E(\boldsymbol a,\boldsymbol b)
=
-
\boldsymbol a\cdot\boldsymbol b.
$$

The joint probabilities can be written as:

$$
P(s,t|\boldsymbol a,\boldsymbol b)
=
\frac14
\left(
1
-
st\,\boldsymbol a\cdot\boldsymbol b
\right),
\qquad
s,t\in\{-1,+1\}.
$$

The marginals are:

$$
P(s|\boldsymbol a,\boldsymbol b)
=
\sum_t
P(s,t|\boldsymbol a,\boldsymbol b)
=
\frac12,
$$

and:

$$
P(t|\boldsymbol a,\boldsymbol b)
=
\sum_s
P(s,t|\boldsymbol a,\boldsymbol b)
=
\frac12.
$$

Thus, the correlation depends on both axes, but each local marginal does not depend on the distant choice.

## 5. How this enters GDQ

The structural chain is:

$$
\mathcal S_{\rm GDQ}
\to
(\rho,S_R)_{AB}
\to
\text{R}_A(\boldsymbol a)
\oplus
\text{R}_B(\boldsymbol b)
\to
P(s,t|\boldsymbol a,\boldsymbol b)
\to
E(\boldsymbol a,\boldsymbol b).
$$

The chapter demonstrates the geometric form and operational compatibility in the reduced sector. The strong metrological closure still requires calculating, for real apparatuses:

$$
K_{AB}^{\rm phys},
\qquad
\text{R}_A(\boldsymbol a),
\qquad
\text{R}_B(\boldsymbol b),
\qquad
\Delta_{\rm gap}.
$$

## 6. Noise protection criterion

Robustness is not absolute immunity. The correct statement is spectral:

$$
\Delta_{\rm gap}
=
\lambda_1(K_{AB}^{\rm phys})
-
\lambda_0(K_{AB}^{\rm phys})
>
0.
$$

Local environmental perturbations are small if:

$$
\|\delta K_{\rm env}\|
\ll
\Delta_{\rm gap}.
$$

Without this calculation, the formulation remains structural and conditional at the metrological level.
