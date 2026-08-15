---
title: "Stationary 8D background of the hierarchy"
---

# Stationary 8D background of the hierarchy

The leptonic background used in the 8D lifting of Chapter 15 is the stationary product background:

$$
g_8=g_B\oplus g_K,
\qquad
K_5=T^5.
$$

The physical hypotheses are:

$$
\text{Re}(f)=\text{constant},
\qquad
\nabla_K f=0,
\qquad
H_{BK}=0,
\qquad
\mathcal C_{BK}=0.
$$

Here $\mathcal C_{BK}$ denotes the mixed block of the connection/metric that would measure the failure of the product. Therefore:

$$
a_W=\|\nabla_KA\|_\infty=0,
$$

$$
a_f=\|\nabla_Kf_K\|_\infty=0,
$$

$$
a_H=\|H_{BK}\|_\infty=0,
$$

$$
\varepsilon=\|\mathcal C_{BK}\|=0.
$$

The physical transverse gap is taken as the smallest conservative gap available in the reduced sector:

$$
\lambda_B^{\rm gap}=\frac12.
$$

With these values:

$$
m_\perp^2
=
C_\gamma\tau R_{\max}^{-2}
-
\left(c_Wa_W^2+c_fa_f^2+c_Ha_H^2+c_C\varepsilon^2\right)
>
0,
$$

and:

$$
j_{\rm mix}=b_Wa_W+b_fa_f+b_Ha_H+b_C\varepsilon=0.
$$

Thus:

$$
\Delta_{\rm Schur}
=
\frac{j_{\rm mix}^2}{m_\perp^2}
=
0.
$$

This proves that, on the stationary product background, the 8D lifting does not shift the leptonic ratios:

$$
R_\ell^{(8)}=R_\ell^{(0)}.
$$

The corresponding script is:

[[../scripts/stationary_8d_background|stationary_8d_background.py]]

and its output is:

[[../scripts/output_stationary_8d_background|Output — stationary 8D leptonic background]].
