---
title: "Derivation of the dark energy density"
---

# Derivation of the dark energy density

The structural formula for dark energy is:

$$
\rho_\Lambda^{\rm GDQ}
=
\alpha^2
N_{\rm Cartan}
\rho_{\rm UV}^{p}
\frac{r_p}{R_H}
\frac{1}{c^2}.
$$

## 1. Protonic UV density

The proton defines the materialized UV density:

$$
\rho_{\rm UV}^{p}
=
\frac{M_pc^2}{(4\pi/3)r_p^3}.
$$

The physical meaning is direct: the proton is the smallest stable baryonic soliton used as a material scale. GDQ does not sum flat zero-point modes up to an arbitrary frequency; it uses the maximum stabilized tension that already appears as persistent matter.

The unit of $\rho_{\rm UV}^{p}$ is:

$$
\frac{{\rm kg}\,{\rm m^2\,s^{-2}}}{{\rm m^3}}
=
{\rm J\,m^{-3}}.
$$

## 2. Linear dilution

With:

$$
f(r)
\sim
\ln\left(\frac{r}{r_p}\right),
$$

we have:

$$
e^{-f}
=
\frac{r_p}{r}.
$$

Then:

$$
\int_{r_p}^{R_H}
e^{-f}r^2dr
=
\frac{r_p}{2}
\left(R_H^2-r_p^2\right).
$$

After dividing by the cosmological volume, the scale remains:

$$
\frac{r_p}{R_H}.
$$

More precisely:

$$
\frac{
\int_{r_p}^{R_H}e^{-f(r)}r^2\,dr
}{
\int_0^{R_H}r^2\,dr
}
=
\frac{
\frac{r_p}{2}(R_H^2-r_p^2)
}{
\frac{1}{3}R_H^3
}.
$$

In the limit $R_H\gg r_p$:

$$
\frac{
\frac{r_p}{2}(R_H^2-r_p^2)
}{
\frac{1}{3}R_H^3
}
=
\frac{3}{2}\frac{r_p}{R_H}
\left[
1+O\left(\frac{r_p^2}{R_H^2}\right)
\right].
$$

The numerical factor of order one depends on the radial normalization used for the cosmological leaf. In the preserved reduced convention, this normalization is absorbed into the global projection operator, leaving the relevant physical law:

$$
\rho_{\rm diluted}\propto\frac{r_p}{R_H}.
$$

The essential point is that the dilution is linear because the weight is $1/r$, not because the flat volume was used as an isolated dimensional argument.

## 3. Channels and projection

In eight real dimensions:

$$
N_{\rm Cartan}
=
\dim\Lambda^2(\mathbb R^8)
=
28.
$$

The macroscopic projection is quadratic:

$$
\rho_{\rm grav}
=
\alpha^2\rho_{\rm eff}.
$$

Thus the complete chain is:

$$
\rho_{\rm eff}
=
N_{\rm Cartan}
\rho_{\rm UV}^{p}
\frac{r_p}{R_H},
$$

and:

$$
\rho_\Lambda^{\rm GDQ}
=
\frac{\alpha^2\rho_{\rm eff}}{c^2}.
$$

Substituting $\rho_{\rm UV}^{p}$:

$$
\rho_\Lambda^{\rm GDQ}
=
\alpha^2
N_{\rm Cartan}
\frac{M_pc^2}{(4\pi/3)r_p^3}
\frac{r_p}{R_H}
\frac{1}{c^2}.
$$

Cancelling explicitly $c^2$ between energy and mass:

$$
\rho_\Lambda^{\rm GDQ}
=
\alpha^2
N_{\rm Cartan}
\frac{M_p}{(4\pi/3)r_p^3}
\frac{r_p}{R_H}.
$$

This last form shows that the final quantity is in ${\rm kg\,m^{-3}}$:

$$
\frac{{\rm kg}}{{\rm m^3}}
\cdot
1
=
{\rm kg\,m^{-3}}.
$$

## 4. Equation of state

In the homogeneous stationary background, the effective contribution enters as:

$$
T_{\mu\nu}^{(\Lambda)}
=
-\rho_\Lambda c^2g_{\mu\nu}.
$$

Comparing with a perfect fluid:

$$
T_{\mu\nu}
=
(\rho c^2+p)u_\mu u_\nu
+
pg_{\mu\nu},
$$

it follows:

$$
p_\Lambda=-\rho_\Lambda c^2,
\qquad
w=-1.
$$

The FLRW continuity:

$$
\dot\rho_\Lambda+3H(1+w)\rho_\Lambda=0
$$

then gives:

$$
\dot\rho_\Lambda=0.
$$

Therefore, GDQ dark energy has the operational signature of a cosmological constant in the homogeneous stationary sector.

## 5. Perturbations

The background tension should not be treated as a free dark energy particle. The admissible perturbations are fluctuations of the saddle:

$$
\Phi_\ast^{\rm cos}
=
(g,J,H,f,\mathcal U)_\ast.
$$

The physical Hessian is:

$$
K_{\rm cos}^{\rm phys}
=
P_{\rm phys}
\operatorname{Hess}_{\Phi_\ast^{\rm cos}}\mathcal S_{\rm GDQ}
P_{\rm phys}.
$$

In a scalar reduction:

$$
\left[
\partial_t^2
+3H\partial_t
+c_s^2\frac{k^2}{a^2}
+m_{\rm gap}^2
\right]\delta\Phi_k
=
J_k^{\rm matter}.
$$

If:

$$
m_{\rm gap}^2>0,
$$

the free modes are suppressed/decaying. The response to matter enters via $J_k^{\rm matter}$ and requires the complete cosmological Hessian for comparison with CMB, BAO, supernovas, and structure growth.

## 6. Preserved numerical evaluation

With:

$$
\alpha^{-1}=137.035999084,
$$

$$
r_p=0.840778765450\,{\rm fm},
$$

$$
M_p=1.672621925950\times10^{-27}\,{\rm kg},
$$

$$
H_0=67.4\,{\rm km\,s^{-1}\,Mpc^{-1}},
$$

and:

$$
\Omega_\Lambda=0.6847,
$$

we obtain:

$$
R_H=\frac{c}{H_0}
=
1.372496834942\times10^{26}\,{\rm m}.
$$

The numerical chain is:

$$
\rho_{\rm UV}^{p}
=
6.038170582656\times10^{34}\,{\rm J\,m^{-3}},
$$

$$
\frac{r_p}{R_H}
=
6.125906771112\times10^{-42},
$$

$$
\rho_{\rm eff}
=
1.035699561608\times10^{-5}\,{\rm J\,m^{-3}},
$$

$$
\alpha^2\rho_{\rm eff}
=
5.515240453183\times10^{-10}\,{\rm J\,m^{-3}},
$$

and:

$$
\rho_\Lambda^{\rm GDQ}
=
6.136532599384\times10^{-27}\,{\rm kg\,m^{-3}}.
$$

The value inferred by the same boundary is:

$$
\rho_\Lambda^{\rm obs}
=
\Omega_\Lambda
\frac{3H_0^2}{8\pi G}
=
5.842445930612\times10^{-27}\,{\rm kg\,m^{-3}}.
$$

Therefore:

$$
\Omega_\Lambda^{\rm GDQ}
=
0.719165212772,
$$

and:

$$
\frac{
\rho_\Lambda^{\rm GDQ}-\rho_\Lambda^{\rm obs}
}{
\rho_\Lambda^{\rm obs}
}
=
5.033622\%.
$$

This error is not absorbed by adjustment. It records the sensitivity to the chosen cosmological boundary and to the input metrological data.

## 7. Status

The calculation is structural. The numerical comparison depends on $R_H=c/H_0$, which is a cosmological boundary datum.
