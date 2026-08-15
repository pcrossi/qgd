---
title: "Torsional equilibrium proton–neutron"
---

# Torsional equilibrium proton–neutron

In the proton:

$$
(\mathcal T_1,\mathcal T_2,\mathcal T_3)
=
(\tau,\tau,\tau).
$$

In the neutron:

$$
(\mathcal T_1,\mathcal T_2,\mathcal T_3)
=
(\tau,\tau,-2\tau).
$$

This second configuration satisfies:

$$
\sum_a\mathcal T_a=0.
$$

The condition comes from phase/torsion variation:

$$
\delta_\vartheta\mathcal S_{\rm GDQ}=0
\quad\Longrightarrow\quad
dJ_{\rm tor}=0.
$$

The neutron mass excess is:

$$
\delta_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
$$

It represents antiparallel torsional shear, not a fixed antineutrino energy.

## 1. Where the $\ln(2\pi^2)$ factor comes from

The baryonic stoma has a topological boundary homeomorphic to $S^3$. In the reduced normalization used in this chapter, the surface entropic contribution is the logarithm of the unit volume of this boundary:

$$
\operatorname{Vol}(S^3)
=
2\pi^2.
$$

Thus, the dimensionless surface scale is:

$$
E_{\partial}^{(0)}
=
\ln\operatorname{Vol}(S^3)
=
\ln(2\pi^2).
$$

This term is not an absolute mass. It is a reduced surface energy measured in the electronic scale used by the ratios $M_B/M_e$.

## 2. Where the $3\sqrt2/5$ factor comes from

The proton has three aligned tensions:

$$
\mathbf t_p
=
(1,1,1).
$$

The stationary neutron has an inverted stoma with twice the opposite torsion:

$$
\mathbf t_n
=
(1,1,-2).
$$

The local equilibrium condition of torsional current is:

$$
\sum_{a=1}^{3}(\mathbf t_n)_a
=
1+1-2
=
0.
$$

Since the common orientation does not measure relative shear, the physical surface invariant must depend on the pairwise differences:

$$
I_{\rm sh}^2(\mathbf t)
=
\sum_{a<b}(t_a-t_b)^2.
$$

For the proton:

$$
I_{\rm sh}^2(\mathbf t_p)
=
0.
$$

For the neutron:

$$
I_{\rm sh}^2(\mathbf t_n)
=
(1-1)^2+(1+2)^2+(1+2)^2
=
18.
$$

Thus:

$$
I_{\rm sh}(\mathbf t_n)
=
3\sqrt2.
$$

This factor still needs to be projected onto the coupling between the three-dimensional sector of the stoma and the four-dimensional local continuum. The reduced projection is expressed by the $3$-$4$-$5$ Pythagorean triangle.

If $n=3$ is the number of torsional channels of the stoma and $D=4$ is the real dimension of the local continuum receiving the physical projection, then the phase deflection angle $\theta_c$ satisfies:

$$
\tan\theta_c
=
\frac{D}{n}
=
\frac43.
$$

Thus, the transmitted component in the stoma sector is:

$$
\cos\theta_c
=
\frac{n}{\sqrt{n^2+D^2}}
=
\frac{3}{\sqrt{3^2+4^2}}
=
\frac35.
$$

Since the fundamental variable is complex, $f=u+iv$, the coherent real–imaginative superposition introduces the elementary norm:

$$
\|1+i\|
=
\sqrt2.
$$

Therefore, the reduced Fredholm–Fano admittance of the baryonic sector is:

$$
\chi_B
=
\sqrt2\cos\theta_c
=
\frac{3\sqrt2}{5}.
$$

The $3$-$4$-$5$ triangle is not separate numerology from the torsional constraint. It records the compatibility between three internal stoma channels and the physical four-dimensional projection of the laboratory. The hypotenuse $5$ appears as the Euclidean norm of the $3\oplus4$ composition.

## 3. Reduced Result

Multiplying the surface entropic scale by the reduced shear invariant:

$$
\delta_B
=
E_{\partial}^{(0)}\chi_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
$$

Numerically:

$$
\delta_B
\simeq
2.530825921868.
$$

Status: conditional reduced derivation. It depends on the validity of the Fredholm–Fano reduction that projects the three torsional channels of the stoma onto the local four-dimensional continuum. The corresponding numerical evaluation is in [[../../scripts/output_derive_baryon_deltas|Output — reduced derivation of delta_B]].
