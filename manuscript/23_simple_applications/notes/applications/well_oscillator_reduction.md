---
title: "Well and oscillator as reduction"
---

# Well and oscillator as reduction

Status: self-contained effective reduction.

## Statement

In the flat, stationary, and one-dimensional sector, the GDQ density equation reduces to known spectral problems.

The conceptual point is important: the infinite well and the harmonic oscillator do not validate GDQ by themselves. They verify that the reduction chain from the official action to the physical Madelung sector does not destroy the elementary limits that any acceptable theory must recover.

We start from the constitutive variables:

$$
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f),
\qquad
R=\sqrt\rho.
$$

In the local, flat sector stabilized by the physical clock, the reduced action takes the form:

$$
I_{\rm red}
=
\int dt\int_\Sigma
\left[
\rho\partial_tS_R
+
\rho\frac{|\nabla S_R|^2}{2m}
+
\rho V
+
\frac{\hbar^2}{8m}\frac{|\nabla\rho|^2}{\rho}
\right]d\Sigma.
$$

Variation with respect to $S_R$ gives:

$$
\partial_t\rho
+
\nabla\cdot\left(\rho\frac{\nabla S_R}{m}\right)
=0.
$$

Variation with respect to $\rho$ gives:

$$
\partial_tS_R
+
\frac{|\nabla S_R|^2}{2m}
+
V
-
\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=0.
$$

For real stationary states,

$$
S_R=-Et,
\qquad
\nabla S_R=0,
$$

and the reduced equation becomes:

$$
E
=
V
-
\frac{\hbar^2}{2m}
\frac{\Delta R}{R}.
$$

## Well

With $S_R=-Et$ and $V=0$:

$$
E
=
-
\frac{\hbar^2}{2m}
\frac{R''}{R}.
$$

Therefore:

$$
-R''
=
k^2R,
\qquad
k^2=\frac{2mE}{\hbar^2}.
$$

With $R(0)=R(L)=0$:

$$
R_n=A\sin\left(\frac{n\pi x}{L}\right),
\qquad
E_n=\frac{\hbar^2\pi^2n^2}{2mL^2}.
$$

The same quantization can be written as the closed circulation of the phase:

$$
\oint p\,dx=nh.
$$

In the well, a closed orbit hits both walls and returns to the initial point, therefore:

$$
2pL=nh,
\qquad
p=\frac{nh}{2L}.
$$

Therefore:

$$
E_n=\frac{p^2}{2m}
=
\frac{n^2h^2}{8mL^2}
=
\frac{\hbar^2\pi^2n^2}{2mL^2}.
$$

In the GDQ reading, this route makes explicit that the spectral condition is a closure condition of holonomy/circulation of the $S_R$ sector against the boundary.

## Oscillator

With $V=m\omega^2x^2/2$:

$$
E
=
\frac12m\omega^2x^2
-
\frac{\hbar^2}{2m}
\frac{R''}{R}.
$$

For $R=Ae^{-\alpha x^2/2}$:

$$
\frac{R''}{R}
=
\alpha^2x^2-\alpha.
$$

The term proportional to $x^2$ vanishes if:

$$
\alpha=\frac{m\omega}{\hbar}.
$$

Then:

$$
E_0=\frac12\hbar\omega.
$$

To show that the Gaussian is not just a guess, it can also be obtained variationally. The stationary functional is:

$$
\mathcal E[R]
=
\int_{\mathbb R}
\left[
\frac{\hbar^2}{2m}|R'|^2
+
\frac12m\omega^2x^2R^2
\right]dx,
\qquad
\int_{\mathbb R}R^2dx=1.
$$

With multiplier $E$:

$$
\delta
\left(
\mathcal E[R]
-
E\int_{\mathbb R}R^2dx
\right)=0
$$

generates:

$$
-
\frac{\hbar^2}{2m}R''
+
\frac12m\omega^2x^2R
=
ER.
$$

The ground state is the positive minimizer of this elliptic problem. The spectral dominance of the normalized gradient flow also selects this state: if

$$
R(\tau,x)=\sum_{n\ge0}c_n(\tau)R_n(x),
$$

then, after subtracting the ground state energy,

$$
c_n(\tau)=c_n(0)e^{-(E_n-E_0)\tau},
\qquad
n>0.
$$

Since $E_n-E_0>0$, the excited components decay and only $R_0$ remains.

For the full ladder, the circulation rule with two turning points gives:

$$
\oint p\,dx
=
h\left(n+\frac12\right).
$$

Since:

$$
\oint p\,dx=\frac{2\pi E}{\omega},
$$

it follows that:

$$
E_n=\hbar\omega\left(n+\frac12\right).
$$

The term $1/2$ is the Maslov index of the two turning points. In GDQ terminology, it is the boundary/caustic phase required to close the circulation of the phase channel.

## Hessian and Index

In the ideal well:

$$
\mathcal J_n
=
-
\frac{\hbar^2}{2m}\frac{d^2}{dx^2}
-E_n.
$$

In the oscillator:

$$
\mathcal J_n
=
-
\frac{\hbar^2}{2m}\frac{d^2}{dx^2}
+\frac12m\omega^2x^2
-E_n.
$$

The relative eigenvalues are $E_k-E_n$. This identifies the stability of the ground state and the Morse index of the excited states.

For the well, with $n=1,2,\ldots$, the state $R_n$ has $n-1$ negative directions in the Hessian restricted to the normalization. For the oscillator, with $n=0,1,\ldots$, the state $R_n$ has $n$ negative directions. Thus:

$$
\operatorname{ind}_{\rm Morse}^{\rm well}(R_n)=n-1,
\qquad
\operatorname{ind}_{\rm Morse}^{\rm osc}(R_n)=n.
$$

This separates a physical minimum from an excited critical point. GDQ recovers this structure as the reduced Hessian of the flat sector, rather than as a postulated fundamental operator.

## Permissible Geometric Perturbations

If the reduced background is not exactly flat, we write in one dimension:

$$
ds^2=a^2(x)dx^2,
\qquad
d\mu_g=a(x)dx.
$$

The Laplace--Beltrami operator is:

$$
\Delta_gR
=
\frac1a\partial_x
\left(
\frac1a\partial_xR
\right).
$$

For:

$$
a(x)=1+\varepsilon h(x),
\qquad
V_{\rm tor}(x)=\varepsilon W_T(x),
\qquad
|\varepsilon|\ll1,
$$

the geodesic coordinate $dy=a(x)dx$ implies:

$$
x(y)=y-\varepsilon H(y)+O(\varepsilon^2),
\qquad
H'(y)=h(y).
$$

In the oscillator:

$$
\frac12m\omega^2x^2
=
\frac12m\omega^2y^2
-
\varepsilon m\omega^2yH(y)
+
O(\varepsilon^2).
$$

The first geometric correction is:

$$
\Delta E_n^{\rm geom}
=
-
\varepsilon m\omega^2
\langle n|yH(y)|n\rangle
+
\varepsilon\langle n|W_T(y)|n\rangle.
$$

This expression is only predictive when $h$ and $W_T$ are calculated from the GDQ metric/torsional equation. If they are chosen freely, it is merely a phenomenological parameterization.

## Scope

This note does not demonstrate the existence of physical walls or external potentials. It merely shows that, given a reduced domain and boundary, GDQ recovers the expected operators.

Strong material closure requires calculating the wall, the effective potential, or the torsional perturbation via the physical Hessian of the official action. The correspondence closure, however, is complete: in the flat, stationary limit with an ideal boundary, known spectra are recovered without introducing any new action.
