---
title: "Kinetic normalization of the Hopf mode"
---

# Kinetic normalization of the Hopf mode

This note records the internal normalization of the electroweak mode. It separates what is a closed internal integral from what depends on global dimensional conversion.

## 1. Charged torsional fluctuation

On the link $S^3$, take a harmonic $\ell=1$:

$$
-\Delta_{S^3}Y=\lambda_1Y,
\qquad
\lambda_1=\frac3{R^2}.
$$

The normalization used is:

$$
\langle Y^2\rangle=\frac14.
$$

The electroweak torsional fluctuation is:

$$
\delta B_{\rm EW}
=
\beta(x)Y\,{\rm vol}_{S^3}.
$$

Since $Y$ has zero mean, the 3-form is exact in the sector orthogonal to the homogeneous flux. A 2-form potential is:

$$
\mathcal A_{\rm EW}
=
-\frac1{\lambda_1}*_{3}dY.
$$

Then:

$$
d\mathcal A_{\rm EW}
=
Y\,{\rm vol}_{S^3}
$$

in the adopted sign convention.

## 2. Internal norm

By the spectral identity:

$$
\langle|dY|^2\rangle
=
\lambda_1\langle Y^2\rangle.
$$

Thus:

$$
\left\langle
|\mathcal A_{\rm EW}|^2
\right\rangle
=
\frac{\langle Y^2\rangle}{\lambda_1}
=
\frac{R^2}{12}.
$$

For:

$$
R=1{,}998411184770,
$$

we obtain:

$$
\left\langle
|\mathcal A_{\rm EW}|^2
\right\rangle
=
0{,}332804.
$$

## 3. Effective kinetic term

When $\beta$ varies in physical space-time:

$$
B
=
d[\beta(x)\mathcal A_{\rm EW}]
=
d_4\beta\wedge\mathcal A_{\rm EW}
+\beta Y\,{\rm vol}_{S^3}.
$$

Integrating the internal space with the normalized official measure:

$$
Z_\beta
=
C_{\rm GDQ}\tau\frac{R^2}{12},
$$

where:

$$
C_{\rm GDQ}
=
\frac{\hbar}{\Lambda_C^2}\mathfrak C_\gamma.
$$

The reduced canonical field is:

$$
\Phi_c=\sqrt{Z_\beta}\,\beta.
$$

Therefore:

$$
v=\sqrt{Z_\beta}\,\beta_\ast.
$$

## 4. Limitation of the result

The internal integral is closed:

$$
\frac{Z_\beta}{C_{\rm GDQ}}
=
\tau\frac{R^2}{12}.
$$

But the conversion to GeV requires the global dimensional and causal normalization. The chapter uses the already recorded reduced scale:

$$
v
=
m_p\frac{6\pi^5}{7}
=
246{,}111195996\,{\rm GeV}.
$$

This separation avoids using $G_F$ or $m_W$ as input to define $v$.

## 5. Computational verification

The script:

$$
{\tt scripts/hopf\_kinetic\_normalization.py}
$$

calculates $\lambda_1$, $\langle|\mathcal A_{\rm EW}|^2\rangle$, and $Z_\beta/C_{\rm GDQ}$.
