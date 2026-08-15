---
title: "No-go of local product and Berger collar"
---

# No-go of local product and Berger collar

This note records negative results that must not be lost. They prevent repeating ansätze that have already been excluded.

## 1. Local product does not transport $3/8$

Consider:

1. junction $C_3$ with conserved primitive flux class;
2. product background $T^5\times S^3$;
3. constant profiles on the torus;
4. radial interface $r=R(1+\varepsilon Y)$ with $Y=x_4$;
5. normalized generators of $SU(2)_L$ and $U(1)_Y$.

At the junction:

$$
J_{\theta r}=0.
$$

Then:

$$
H_{\rm eff}
=
H_{\rm rel}
-
J_{\theta r}K_r^{-1}J_{\theta r}^{\dagger}
=
H_{\rm rel}.
$$

On the interface $\ell=1$, the weight depends only on $x_4$. By residual isotropy:

$$
I_{W_1}=I_{W_2}=I_{W_3}=I_Y.
$$

On the torus with constant profiles, the normalized measure provides a common factor. Thus:

$$
Z_W=Z_Y.
$$

Therefore:

$$
\sin^2\theta_W=\frac38.
$$

The product/local ansatz does not generate transport up to $2/9$.

## 2. Homogeneous Berger is unstable

In the Berger metric:

$$
ds^2=R^2(\sigma_1^2+\sigma_2^2+q^2\sigma_3^2),
$$

the homogeneous extremum is at:

$$
q=1.
$$

But the reduced Hessian of the squashing mode has:

$$
H_q^{\rm eff}
=
-2{,}67090856<0.
$$

Therefore, the homogeneous Berger mode is a real instability. The positive quartic of the electroweak mode $\ell=1$ stabilizes $\beta$, but does not automatically stabilize the common metric squashing $q$.

## 3. Dynamic collar with available interface

In the cohomogeneity one reduction:

$$
ds^2
=
N(r)^2dr^2
+a(r)^2(\sigma_1^2+\sigma_2^2)
+c(r)^2\sigma_3^2,
\qquad
q(r)=\frac{c(r)}{a(r)}.
$$

With closed torsion:

$$
B=h(r)\sigma_1\wedge\sigma_2\wedge\sigma_3,
\qquad
dB=0,
$$

we have:

$$
h'(r)=0.
$$

The currently derived natural boundary conditions are:

$$
\Pi_a=\Pi_c=\Pi_f=0.
$$

They imply:

$$
a'=c'=f'=0.
$$

Thus, without an additional metric-dilatonic interface pullback, the collar selects the homogeneous cylinder. In this cylinder:

$$
H_q^{\rm total}=-2{,}67090856<0.
$$

Furthermore, the radial photonic mode is constant. In an infinite collar:

$$
\|\Psi_\gamma\|^2=\infty,
$$

and the mode does not become localized.

## 4. Missing element

The missing mathematical object is:

$$
I_{\rm int}^{(a,c,f)}.
$$

That is, the metric-dilatonic pullback of the global gluing of the stoma. It must provide Robin conditions for $(a,c,f)$ derived from the official action and the global boundary. Choosing its coefficients numerically would be a new constitutive hypothesis.

## 5. Status

This no-go does not reopen the electroweak breaking. It delimits the fine metrology: to predict $\alpha_{\rm EW}$, photonic localization, and transport $2/9$ in a strong sense, a non-product global background with a derived boundary Hessian is required.

## 6. Computational verification

The script:

$$
{\tt scripts/no_go_berger_collar.py}
$$

reproduces the diagnostic values: $Z_W/Z_Y=1$, $\sin^2\theta_W=3/8$ in the local product, $H_q^{\rm eff}<0$, and the linear divergence of the photonic norm in the infinite collar.
