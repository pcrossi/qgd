---
title: "Casimir as a boundary Hessian"
---

# Casimir as a boundary Hessian

Status: effective reduction with ideal boundary.

## Effective Hessian

In the flat limit:

$$
K_{\rm EM}^{\rm eff}
\sim
-\partial_t^2+c^2(-\Delta_\parallel-\partial_z^2).
$$

With ideal plates:

$$
k_z=\frac{n\pi}{a}.
$$

The frequencies are:

$$
\omega_{n,\mathbf k}
=
c\sqrt{k^2+\left(\frac{n\pi}{a}\right)^2}.
$$

## Determinant

The formal energy is:

$$
\frac{E}{A}
=
\frac{\hbar}{2}
\sum_n
\int\frac{d^2k}{(2\pi)^2}
\omega_{n,\mathbf k}.
$$

The observable is the $a$-dependent difference after subtracting the reference without plates and the local surface terms. The universal part is:

$$
\frac{\Delta E}{A}
=
-
\frac{\pi^2\hbar c}{720a^3}.
$$

## Derivation of the universal coefficient

For the ideal electromagnetic field, there are two transverse polarizations. Thus:

$$
\frac{E}{A}
=
\frac{\hbar c}{2}
\cdot 2
\sum_{n=1}^{\infty}
\int
\frac{d^2k}{(2\pi)^2}
\sqrt{
k^2+
\left(\frac{n\pi}{a}\right)^2
}.
$$

By dimensional continuation:

$$
\int
\frac{d^2k}{(2\pi)^2}
\sqrt{k^2+m^2}
=
-
\frac{m^3}{6\pi}
$$

as the regularized finite part. Therefore:

$$
\frac{\Delta E}{A}
=
-
\frac{\hbar c}{6\pi}
\left(
\frac{\pi}{a}
\right)^3
\sum_{n=1}^{\infty}n^3.
$$

The spectral continuation gives:

$$
\sum_{n=1}^{\infty}n^3
\to
\zeta(-3)
=
\frac{1}{120}.
$$

Therefore:

$$
\frac{\Delta E}{A}
=
-
\frac{\pi^2\hbar c}{720a^3}.
$$

This step is a technique for extracting the universal part of the determinant. In GDQ, it does not alter the official action nor does it transform the zeta function into physical ontology. The regulator separates the universal $a$-dependent energy from the local surface terms.

Therefore:

$$
P
=
-
\frac{\pi^2\hbar c}{240a^4}.
$$

## Real plates

For real plates:

$$
\mathsf R_{\rm plate}
=
K_{YY}-K_{YI}K_{II}^{-1}K_{IY}.
$$

The actual material force depends on $\mathsf R_{\rm plate}$, not just the ideal universal coefficient.
