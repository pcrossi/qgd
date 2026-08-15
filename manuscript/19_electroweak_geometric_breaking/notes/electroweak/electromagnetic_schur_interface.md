---
title: "Electromagnetic Schur interface"
---

# Electromagnetic Schur interface

The electromagnetic external data $A$ and the internal trace $x$ of the interface can be written by the quadratic energy:

$$
S_{\rm col}^{(2)}
=
\frac12K_0x^2
+
\frac12K_\partial(A-x)^2.
$$

In the basis $(x,A)$:

$$
\mathbb H_{\rm EM}
=
\begin{pmatrix}
K_0+K_\partial & -K_\partial\\
-K_\partial & K_\partial
\end{pmatrix}.
$$

Eliminating $x$ by Schur complement:

$$
K_{\rm EM}^{\rm eff}
=
K_\partial
-
K_\partial(K_0+K_\partial)^{-1}K_\partial.
$$

Thus:

$$
\boxed{
K_{\rm EM}^{\rm eff}
=
\frac{K_0K_\partial}{K_0+K_\partial}.
}
$$

Defining the surface admittance:

$$
\mathcal S_\partial
=
\frac{K_0}{K_\partial},
$$

we have:

$$
K_{\rm EM}^{\rm eff}
=
\frac{K_0}{1+\mathcal S_\partial}.
$$

With:

$$
\mathcal S_\partial
=
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right),
$$

we obtain:

$$
\frac{K_{\rm EM}^{\rm eff}}{K_0}
=
0{,}966590303209.
$$

This block is a conditional theorem: the Schur algebra is closed; the complete constitutive identification of $\mathcal S_\partial$ with the direct second variation of the official action remains a metrological refinement.
