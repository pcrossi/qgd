---
title: "GDQ construction of the physical Hilbert and quantization"
---

# GDQ construction of the physical Hilbert and quantization

## 1. Statement

The Hilbert space is not a primary axiom of GDQ. It is reconstructed as the operational layer of a regular geometric sector.

The construction is:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast
\to
K_{\rm GDQ}
\to
P_{\rm phys}
\to
K_{\rm phys}
\to
\mathcal H_{\rm phys}
\to
\text{self-adjoint operators}.
$$

## 2. Admissible Background

We choose a stationary background:

$$
\Phi_\ast=(g_\ast,J_\ast,H_\ast,f_\ast).
$$

It satisfies the first variation of the official action in the domain considered:

$$
\left.
\frac{\delta\mathcal S_{\rm GDQ}}{\delta\Phi}
\right|_{\Phi_\ast}
=
0.
$$

This step is conditional on the sector: without an admissible background, there is no operational reconstruction of that sector.

## 3. Hessian and Physical Sector

The second variation defines:

$$
K_{\rm GDQ}
=
\left.
\frac{\delta^2\mathcal S_{\rm GDQ}}
{\delta\Phi\,\delta\Phi}
\right|_{\Phi_\ast}.
$$

The raw Hessian contains constraints, zero modes, and gauge directions. The physical sector is obtained by projection:

$$
K_{\rm phys}
=
P_{\rm phys}^{\dagger}
K_{\rm GDQ}
P_{\rm phys}.
$$

The projector preserves variations compatible with charge, flux, normalization, and boundary conditions.

## 4. Inner Product

In the reflected Euclidean sector, reflection positivity yields:

$$
\langle [F],[G]\rangle_{\mathcal H}
=
\langle \Theta F\,G\rangle_E.
$$

Null states and gauge modes are quotiented:

$$
\mathcal H_{\rm phys}
=
\overline{
\mathcal D_+/
(\mathcal N+\mathcal G)
}.
$$

In the local regular sector, the reduced representation is:

$$
\mathcal H_{\rm phys}
\simeq
L^2(N,E,d\Sigma_h).
$$

## 5. Operators and Quantization

Physical operators are closed forms of the Hessian or generators of symmetries in the projected sector. Self-adjointness is not assumed by notation; it requires:

1. dense domain;
2. boundary conditions;
3. removal of zero modes;
4. positivity of the physical inner product.

Thus:

$$
\text{physical operator}
=
\text{generator/quadratic form in }
\mathcal H_{\rm phys}.
$$

## 6. Wallstrom and Circulation

The phase is circular:

$$
e^{iS_R/\hbar}\in U(1).
$$

Therefore, in a closed loop:

$$
\oint dS_R
=
2\pi\hbar k,
\qquad
k\in\mathbb Z.
$$

This quantization is not added to hydrodynamics. It comes from the topology of the phase bundle.

## 7. Uncertainty

In the regular sector, Cauchy--Schwarz in the physical inner product yields:

$$
\Delta A\,\Delta B
\ge
\frac12
\left|
\langle [A,B]\rangle
\right|.
$$

Thus uncertainty is a consequence of Hermitian positivity and operator domains, not an isolated axiom.

## 8. Limitation

This construction closes the regular operational sector. The universal reconstruction of all backgrounds remains conditioned on the existence, positivity, and domain of each sector.
