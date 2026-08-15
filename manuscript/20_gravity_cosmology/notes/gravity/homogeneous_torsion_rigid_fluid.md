---
title: "Homogeneous torsion as a rigid fluid"
---

# Homogeneous torsion as a rigid fluid

This note preserves a simple cosmological reduction. It does not define GDQ dark energy and does not replace the official action. Its purpose is to show what a homogeneous spatial 3-form would produce, in the effective cosmological limit, if treated as a free torsional sector on an FLRW metric.

Consider

$$
ds^2=-dt^2+a(t)^2\gamma_{ij}dx^idx^j,
$$

and a purely spatial homogeneous 3-form

$$
B_{ijk}=b_0\varepsilon_{ijk},
$$

where $\varepsilon_{ijk}$ is the reference spatial volume and $b_0$ is constant in the homogeneous sector. When raising indices with the spatial metric $a(t)^2\gamma_{ij}$, each spatial index contributes a factor of $a^{-2}$. Therefore,

$$
B_{\mu\nu\lambda}B^{\mu\nu\lambda}
=
B_{ijk}B^{ijk}
=
\frac{6b_0^2}{a^6}.
$$

In the effective reduction with a quadratic 3-form Lagrangian,

$$
\mathcal L_B
=
-\frac{1}{12}B_{\mu\nu\lambda}B^{\mu\nu\lambda},
$$

the homogeneous energy density scales as

$$
\rho_B
=
\frac{b_0^2}{2a^6}.
$$

The conservation of a perfect fluid in FLRW is

$$
\dot\rho+3H(\rho+P)=0.
$$

Since $\rho_B\propto a^{-6}$,

$$
\dot\rho_B=-6H\rho_B.
$$

Substituting into the conservation equation:

$$
-6H\rho_B+3H(\rho_B+P_B)=0.
$$

For $H\neq0$, it follows

$$
P_B=\rho_B.
$$

Therefore

$$
\boxed{
w_B=\frac{P_B}{\rho_B}=1.
}
$$

This is a rigid fluid, or stiff fluid. It dilutes as $a^{-6}$ and does not have the homogeneous signature of dark energy, which would require

$$
w=-1.
$$

In GDQ, the dark energy density discussed in the body of the chapter comes from the global boundary problem, the materialized UV tension, and the cosmological projection. The above reduction is useful to prevent the improper identification of free homogeneous torsion with a cosmological constant.
