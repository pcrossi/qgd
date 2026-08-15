---
title: "Variational torsional profile of the neutron"
---

# Variational torsional profile of the neutron

## 1. Objective

The neutron has zero total charge:

$$
G_E^n(0)=0.
$$

But this does not imply a zero internal electrical density. In GDQ, the neutron is a baryonic configuration with an inverted stoma and antiparallel torsional shear. The low-energy electrical profile must therefore be obtained as a surface response.

## 2. Local Surface Coordinate

The coordinate normal to the stoma is used:

$$
\xi=r-r_p.
$$

The physical distance is the surface projection:

$$
r=r_p+\xi.
$$

## 3. Stationary Torsional Source

The leading torsional separation is:

$$
\xi_+
=
-\frac12r_p\alpha_{\rm tor}^{(2)},
\qquad
\xi_-
=
\frac12r_p\alpha_{\rm tor}^{(2)},
$$

with:

$$
\alpha_{\rm tor}^{(2)}
=
2\alpha\ln(2\pi^2).
$$

The amplitude is fixed by the neutron magnetic moment:

$$
A_n=|\mu_n|.
$$

## 4. Variational Problem

The smooth profile is the solution of the Perelman heat flow in the surface layer:

$$
\left(
\partial_t-\partial_\xi^2
\right)
H_n(\xi,\tau)
=
0.
$$

With a dipolar initial condition:

$$
H_n(\xi,0)
=
|\mu_n|
\left[
\delta(\xi-\xi_+)
-
\delta(\xi-\xi_-)
\right].
$$

Thus:

$$
H_n(\xi,\tau_n)
=
|\mu_n|
\left[
K_{\tau_n}(\xi,\xi_+)
-
K_{\tau_n}(\xi,\xi_-)
\right],
$$

where:

$$
K_\tau(\xi,\xi_0)
=
\frac1{\sqrt{4\pi\tau}}
\exp
\left[
-\frac{(\xi-\xi_0)^2}{4\tau}
\right].
$$

The natural width chosen by the torsional separation is:

$$
\sigma_r
=
\sqrt{2\tau_n}
=
\frac12r_p\alpha_{\rm tor}^{(2)}.
$$

## 5. Form Factor

The neutron electrical factor at the leading level is:

$$
G_E^n(q^2)
=
\int
H_n(\xi,\tau_n)
j_0(q(r_p+\xi))
d\xi.
$$

Since both cores have the same total mass and opposite signs:

$$
\int H_n d\xi=0,
$$

then:

$$
G_E^n(0)=0.
$$

The quadratic radius follows from the expansion of $j_0$:

$$
j_0(qr)
=
1-\frac{q^2r^2}{6}+O(q^4).
$$

Thus:

$$
-6
\left.
\frac{dG_E^n}{dq^2}
\right|_0
=
\int H_n(\xi,\tau_n)(r_p+\xi)^2d\xi.
$$

In the leading limit:

$$
\langle r_n^2\rangle
=
-2|\mu_n|\alpha_{\rm tor}^{(2)}r_p^2.
$$

## 6. Physical Meaning

The $H_n$ profile closes the zero charge and the low-energy slope. It should not be confused with the complete form factor measured by scattering: the electromagnetic probe also possesses a surface impedance.

Script:

[[../../scripts/neutron_torsional_profile|neutron_torsional_profile.py]]

Output:

[[../../scripts/output_neutron_torsional_profile|Output — neutron torsional profile]].
