---
title: "GDQ criterion for a material soliton"
---

# GDQ criterion for a material soliton

This note establishes what it means to call a configuration a "particle" in GDQ. It prevents an externally chosen profile from being promoted to a physical solution without going through the variational problem.

## 1. Definition

A GDQ soliton is a configuration

$$
\mathfrak S=(g,H,f,\bar f)
$$

in a fixed sector of topology, gauge, and boundary, such that:

1. it satisfies the stationary equations of the official action or the associated geometric flow;
2. it has a normalizable density;
3. it has a finite geometric energy;
4. it has a controlled asymptotic behavior;
5. it has readable topological invariants such as charge and spin when the sector is charged/spinorial;
6. it has a stable physical Hessian after removing gauge and admissible zero modes;
7. it has an interaction response defined by boundaries, DtN/Schur, or interface couplings.

In the torsional sector compatible with the Bismut connection, the schematic stationary equation is

$$
R_{ij}
-\frac14H_{ik\ell}H_j{}^{k\ell}
+\nabla_i\nabla_j\phi
=
\lambda g_{ij},
$$

with

$$
dH=0,
\qquad
d_\phi^\dagger H=0,
$$

where

$$
f=\phi+i\chi,
\qquad
\rho=e^{-\phi}=e^{-(f+\bar f)/2}.
$$

The phase $\chi=S_R/\hbar$ carries circulation and holonomy.

## 2. Finite energy

A sufficient condition for finite energy is

$$
\int_M\rho\,dV_g=1,
$$

and

$$
\int_M
\left(
|R|
+|\nabla f|^2
+|H|^2
\right)
\rho\,dV_g
<\infty.
$$

The effective rest energy of a material sector is the excess relative to the vacuum of the same problem:

$$
m[\mathfrak S]c^2
=
E[\mathfrak S]-E[\mathfrak S_{\rm vac}].
$$

Therefore, mass is not a primitive parameter inserted afterwards. It is an energetic reading of the stationary geometry.

## 3. Charge

Charge must come from circulation, residue, or holonomy, not from an external label. For an admissible cycle $C$,

$$
N_C
=
\frac1{2\pi}\oint_Cd\chi
\in\mathbb Z.
$$

An effective charge appears after projection onto the internal sector:

$$
Q
=
e\sum_aq_aN_a.
$$

The weights $q_a$ belong to the effective internal bundle and to the global quotients of the sector. They are not mass.

## 4. Spin

Spin is read by spinorial holonomy and torsional circulation. In the reduced sector,

$$
\mathbf J
=
\int_\Sigma
\rho\,\mathbf x\times\nabla S_R\,d\mu_h
+\mathbf J_{\rm torsion}.
$$

For fermionic sectors, the minimum spinorial condition is

$$
\Psi\mapsto-\Psi
\quad
\text{under a }2\pi\text{ rotation,}
$$

and

$$
\Psi\mapsto\Psi
\quad
\text{under a }4\pi\text{ rotation.}
$$

Thus, a scalar circulation can help visualize spin, but the physical proof of spin $1/2$ uses spinorial structure, holonomy, and torsion.

## 5. Minimal explicit solution

In the neutral sector, without torsion, the Gaussian soliton exists:

$$
M=\mathbb R^d,
\qquad
g_{ij}=\delta_{ij},
\qquad
H=0,
$$

with

$$
\phi(x)=\frac{|x|^2}{4\sigma},
\qquad
\sigma>0.
$$

Then

$$
R_{ij}=0,
\qquad
\nabla_i\nabla_j\phi
=
\frac1{2\sigma}\delta_{ij}.
$$

Hence

$$
R_{ij}+\nabla_i\nabla_j\phi
=
\frac1{2\sigma}g_{ij}.
$$

The normalized density is

$$
\rho_N(x)
=
\frac{1}{(4\pi\sigma)^{d/2}}
\exp\left(-\frac{|x|^2}{4\sigma}\right).
$$

It is normalizable and has all polynomial moments finite.

For the reduced Perelman functional,

$$
\mathcal W_{\rm gauss}
=
\int_M
\left[
\sigma|\nabla\phi|^2+\phi-d
\right]
\rho_N\,dV.
$$

Since

$$
|\nabla\phi|^2=\frac{|x|^2}{4\sigma^2},
$$

we have

$$
\sigma|\nabla\phi|^2
=
\frac{|x|^2}{4\sigma}.
$$

In the Gaussian above, each coordinate has variance $2\sigma$, therefore

$$
\left\langle |x|^2\right\rangle=2d\sigma.
$$

Thus,

$$
\left\langle
\frac{|x|^2}{4\sigma}
\right\rangle
=
\frac d2,
\qquad
\langle\phi\rangle=\frac d2.
$$

Hence

$$
\mathcal W_{\rm gauss}
=
\frac d2+\frac d2-d
=
0.
$$

This result proves the explicit existence of a neutral normalizable solution. It does not prove, by itself, electron, proton, or neutron.

## 6. Linear stability of the Gaussian reference

In the reduced scalar sector, the weighted Hessian is modeled by the Ornstein--Uhlenbeck operator

$$
\mathcal L_{\rm OU}
=
-\Delta
+\frac{x}{2\sigma}\cdot\nabla.
$$

In $L^2(\rho_NdV)$, its spectrum is discrete:

$$
\lambda_k=\frac{k}{2\sigma},
\qquad
k=0,1,2,\ldots
$$

The mode $k=0$ is a normalization/symmetry zero mode. Translation, scale, and diffeomorphism modes must be classified and removed or treated as moduli. After projecting these modes, stability requires a positive gap in the physical sector.

## 7. Mandatory record for a physical particle

To declare a particle, the manuscript must provide a record:

| Item | Requirement |
|---|---|
| Background | Stationary $\mathfrak S_P=(g_P,H_P,f_P,\bar f_P)$. |
| Residue | $\mathcal E_g=\mathcal E_H=\mathcal E_f=0$ in the declared domain. |
| Energy | Finite weighted integral. |
| Mass | Energy excess against the vacuum of the same sector. |
| Charge | Circulation/residue/holonomy integral. |
| Spin | Spinorial holonomy and/or torsional integral. |
| Hessian | $K_{\rm phys}=P_{\rm phys}^\dagger K P_{\rm phys}$. |
| Zero modes | Identified gauge, translation, rotation, scale, or physical moduli. |
| Asymptotics | Decay or boundary matching. |
| Interaction | Response by source, boundary, DtN/Schur, or scattering. |

This checklist is the operational criterion of GDQ to distinguish a material solution from a phenomenological profile.
