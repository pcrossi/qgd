---
title: "Lean Formalization of the Gravitational and Cosmological Layer"
---

# Lean Formalization of the Gravitational and Cosmological Layer

This note separates what has been certified as an exact mathematical identity from what continues to depend on the cosmological solution of the official action.

The canonical module is [GravityCosmology.lean](../../../../formal/GDQ/GravityCosmology.lean).

## 1. Dimensionless Group and Horizon Response

We define:

$$
\Pi_G
=
\frac{GM^2}{\hbar c},
$$

and:

$$
G_{\rm rec}
=
\frac{\hbar c}{M^2}\Pi_G.
$$

Under $M\neq0$, $\hbar\neq0$, and $c\neq0$, direct substitution yields:

$$
G_{\rm rec}=G.
$$

This result certifies the dimensional reconstruction. It does not calculate $\Pi_G$.

Similarly, if the global boundary satisfies:

$$
R_H
=
\frac{2GE_H}{c^4},
$$

then, for $c\neq0$ and $E_H\neq0$:

$$
\frac{c^4R_H}{2E_H}
=
G.
$$

The theorem reconstructs the response after $R_H$ and $E_H$ are given by the cosmological problem. It does not transform them into universal numbers without a boundary.

## 2. Thermal Saddle and Axial Gluing

The Euclidean period:

$$
\beta_E=2\pi R_H
$$

exactly produces:

$$
\tau_\ast
=
\frac{\beta_E^2}{16}
=
\frac{\pi^2R_H^2}{4}.
$$

With:

$$
\lambda_{\rm ax}
=
\frac{2}{R^2},
$$

the relative cost is:

$$
\Delta u_v
=
\tau_\ast\pi^2\lambda_{\rm ax}
=
\frac{\pi^4}{2}\frac{R_H^2}{R^2}.
$$

The module then proves the conditional theorem:

$$
R
=
\pi^2\sqrt{\alpha}\,R_H
\quad\Longrightarrow\quad
\Delta u_v
=
\frac{1}{2\alpha},
$$

for $\alpha>0$ and $R_H\neq0$.

This formulation is deliberate. The exponent algebra is closed, but the gluing condition remains a geometric datum to be obtained from the full cosmological background.

## 3. Dilution and Antisymmetric Channels

The count:

$$
\dim\Lambda^2(\mathbb R^8)
=
\binom{8}{2}
=
28
$$

is certified directly.

For the weight $e^{-f}=r_p/r$, the exact radial ratio is:

$$
\frac{
\frac{r_p}{2}(R_H^2-r_p^2)
}{
\frac13R_H^3
}
=
\frac{3}{2}\frac{r_p}{R_H}
\left(
1-\frac{r_p^2}{R_H^2}
\right).
$$

Therefore, in the limit $R_H\gg r_p$, the dominant dependence is linear in $r_p/R_H$. The factor $3/2$ does not vanish by algebra: its absorption belongs to the normalization of the cosmological projector adopted in the reduced model.

## 4. Cosmological Density and Equations of State

Starting from:

$$
\rho_{\rm UV}^{p}
=
\frac{M_pc^2}{V_p},
\qquad
V_p
=
\frac{4\pi}{3}r_p^3,
$$

the module proves, for $c\neq0$:

$$
\alpha^2N
\rho_{\rm UV}^{p}
\frac{r_p}{R_H}
\frac{1}{c^2}
=
\alpha^2N
\frac{M_p}{V_p}
\frac{r_p}{R_H}.
$$

Thus, the cancellation of $c^2$ and the final dimension of mass density are exact. The choice of $N=28$, the global profile, and the $\alpha^2$ normalization remains identified in the body of the chapter.

Also certified:

$$
p_\Lambda=-\rho_\Lambda c^2
\quad\Longrightarrow\quad
w=-1,
$$

and, separately, that a free homogeneous 3-form with $\dot\rho=-6H\rho$ and perfect fluid continuity satisfies:

$$
p=\rho,
\qquad
w=1,
$$

when $H\neq0$. This prevents confusing free homogeneous torsion with dark energy.

## 5. Critical Acceleration

Under:

$$
R_H=\frac{c}{H_0},
$$

the module proves:

$$
\frac{c^2}{2\pi R_H}
=
\frac{cH_0}{2\pi},
$$

for $c\neq0$ and $H_0\neq0$.

This identity certifies the transition between Hubble radius and acceleration scale. Comparison with the galactic phenomenological scale remains an external evaluation, registered in the scripts of the chapter.

## 6. Logical Scope

The Lean module does not state:

1. having resolved the background $\Phi_\ast^{\rm cos}$;
2. having diagonalized $K_{\rm cos}^{\rm phys}$;
3. having spectrally derived the reduced prefactor of $G$;
4. having calculated CMB, BAO, supernovae, or structure growth;
5. that the numerical agreement replaces the missing variational chain.

It certifies the algebraic layer that will be used when these cosmological data are constructed.
