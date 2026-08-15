---
title: "CP relaxation proof by Lyapunov"
---

# CP relaxation proof by Lyapunov

Define:

$$
V(\theta)
=
\chi(1-\cos\theta),
\qquad
\chi>0.
$$

The reduced flow is:

$$
\dot\theta
=
-\kappa
\frac{dV}{d\theta},
\qquad
\kappa>0.
$$

Since:

$$
\frac{dV}{d\theta}
=
\chi\sin\theta,
$$

we have:

$$
\dot\theta
=
-\kappa\chi\sin\theta.
$$

Now:

$$
\frac{dV}{d\tau}
=
\frac{dV}{d\theta}
\dot\theta
=
-\kappa
\left(
\frac{dV}{d\theta}
\right)^2
\le0.
$$

Therefore $V$ is a Lyapunov function.

The critical points are:

$$
\sin\theta=0
\quad\Rightarrow\quad
\theta=n\pi.
$$

The second derivative is:

$$
\frac{d^2V}{d\theta^2}
=
\chi\cos\theta.
$$

Therefore:

$$
\theta=0\pmod{2\pi}
$$

is a stable minimum, and:

$$
\theta=\pi\pmod{2\pi}
$$

is an unstable maximum.

Thus, for any initial condition outside the unstable maximum:

$$
\theta(\tau)\to0\pmod{2\pi}.
$$

This proof uses only periodicity, positivity of $\chi$, and dissipative gradient flow of the torsional mode.
