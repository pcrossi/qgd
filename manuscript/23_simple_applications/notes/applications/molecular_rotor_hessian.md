---
title: "Molecular rotor and collective Hessian"
---

# Molecular rotor and collective Hessian

Status: conditional effective reduction.

## Collective Coordinates

For a diatomic molecule:

$$
R(t)\in\mathbb R_+,
\qquad
\Omega(t)\in S^2.
$$

After physical projection:

$$
L_{\rm eff}
=
\frac{\mu}{2}\dot R^2
+
\frac{\mu R^2}{2}|\dot\Omega|^2
-
V(R).
$$

## Angular Sector

At the equilibrium $R_0$:

$$
I_0=\mu R_0^2.
$$

The angular operator is:

$$
K_{\rm ang}
=
-
\frac{\hbar^2}{2I_0}\Delta_{S^2}.
$$

Since:

$$
-\Delta_{S^2}Y_{Jm}=J(J+1)Y_{Jm},
$$

we have:

$$
E_J=BJ(J+1),
\qquad
B=\frac{\hbar^2}{2I_0}.
$$

## Centrifugal Distortion

With:

$$
V(R)=V_0+\frac12\mu\omega_e^2(R-R_0)^2+\cdots,
$$

minimizing:

$$
E(R;J)
=
\frac{\hbar^2J(J+1)}{2\mu R^2}
+
\frac12\mu\omega_e^2(R-R_0)^2
$$

is the step where centrifugal distortion appears. Define:

$$
L^2=\hbar^2J(J+1),
\qquad
R=R_0+x.
$$

For low rotation, $|x|\ll R_0$, so:

$$
\frac{1}{(R_0+x)^2}
=
\frac{1}{R_0^2}
\left(
1-\frac{2x}{R_0}
+
\frac{3x^2}{R_0^2}
-\cdots
\right).
$$

Substituting:

$$
E(x;J)
=
\frac{L^2}{2\mu R_0^2}
-
\frac{L^2}{\mu R_0^3}x
+
\frac{3L^2}{2\mu R_0^4}x^2
+
\frac{1}{2}\mu\omega_e^2x^2
+\cdots .
$$

To the order required to obtain the $L^4$ term, the minimum satisfies:

$$
\mu\omega_e^2x
-
\frac{L^2}{\mu R_0^3}
=
0.
$$

Therefore:

$$
x_\ast(J)
=
\frac{L^2}{\mu^2\omega_e^2R_0^3}
=
\frac{\hbar^2J(J+1)}
{\mu^2\omega_e^2R_0^3}.
$$

Substituting $x_\ast$ back into the energy gives:

$$
E_J
=
BJ(J+1)
-
D[J(J+1)]^2+\cdots,
$$

where:

$$
D
=
\frac{\hbar^4}{2\mu^3\omega_e^2R_0^6}.
$$

The negative sign has physical meaning: upon rotating, the molecule slightly stretches the bridge, increases the effective moment of inertia, and reduces the rotational energy compared to a perfectly rigid rotor.

In wave number:

$$
D\simeq\frac{4B^3}{\omega_e^2}.
$$

## Legacy Elastic Parameter

If the legacy text wrote:

$$
D
=
\gamma_{\rm elastic}
\frac{\hbar^4}{4I_0^3\omega_e^2},
$$

with $I_0=\mu R_0^2$, the harmonic derivation above implies:

$$
D
=
\frac{\hbar^4}{2I_0^3\omega_e^2}.
$$

Therefore, under this normalization:

$$
\gamma_{\rm elastic}^{\rm red}=2.
$$

This number is not a new fundamental constant. It is merely the translation of the minimal radial harmonic model to the old notation. In a real molecule, the full Hessian may add anisotropy, torsion, anharmonicity, and boundary response; these effects must be calculated, not absorbed into a universal parameter.

## Scope

If $B$ and $\omega_e$ are experimental inputs, the calculation is a phenomenological comparison. For absolute prediction, GDQ must calculate $\mu$, $R_0$, and $\omega_e$ from the Hessian of the molecular bridge.
