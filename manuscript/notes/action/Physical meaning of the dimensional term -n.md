---
title: "Physical meaning of the dimensional term -n"
---

# Physical meaning of the dimensional term $-n$

## What needs to be explained

In the official action appears

$$
\frac{f+\bar f}{2}-n
=
\operatorname{Re}f-n.
$$

This term is not a potential added to reproduce an observable. The number $n$ is already fixed by the complex dimension of the domain:

$$
\dim_{\mathbb R}M=2n.
$$

Its role can be determined by examining the reference diffusive state of the official measure.

## The normalized Gaussian

In the flat Euclidean section, take

$$
F_G
=
\operatorname{Re}f_G
=
\frac{|x|^2}{4\tau},
\qquad
\tau>0.
$$

The measure is

$$
d\mu_G
=
(4\pi\tau)^{-n}
\exp\left(-\frac{|x|^2}{4\tau}\right)d^{2n}x.
$$

It is normalized because each of the $2n$ Gaussian integrals yields $\sqrt{4\pi\tau}$:

$$
\int_{\mathbb R^{2n}}d\mu_G=1.
$$

Each real coordinate has variance $2\tau$. Therefore,

$$
\langle |x|^2\rangle_G
=
2n(2\tau)
=
4n\tau,
$$

and

$$
\boxed{
\langle F_G\rangle_G
=
\left\langle\frac{|x|^2}{4\tau}\right\rangle_G
=n.
}
$$

Thus, $-n$ is the unique dimensional constant that makes

$$
\langle F_G-n\rangle_G=0.
$$

## Physical meaning

The number $n$ represents the basal equipartition contribution of the $2n$ real directions: each quadratic direction contributes $1/2$. Subtracting $n$ removes this inevitable contribution of dimensionality and defines the normalized Gaussian as the zero of the entropic sector.

Thus, the action does not measure the simple fact that the density exists in $2n$ dimensions as a physical excitation. It preserves as non-trivial content:

- curvature;
- density and phase gradients;
- torsion contained in the Hermitian geometry;
- global and boundary conditions;
- departure from diffusive equilibrium.

Under a fixed second moment, this statement has an exact informational form. For

$$
u=(4\pi\tau)^{-n}e^{-F}
$$

and for the Gaussian $u_G$,

$$
D_{\rm KL}(u\|u_G)
=
\int u\ln\left(\frac{u}{u_G}\right)d^{2n}x
=
n-\langle F\rangle_u.
$$

Consequently,

$$
\boxed{
\langle F-n\rangle_u
=
-D_{\rm KL}(u\|u_G)
\le0.
}
$$

The term $F-n$ measures, in this sector, the entropic deficit in relation to the reference Gaussian.

## Why this is not the complete subtraction of Perelman

For the same Gaussian,

$$
\nabla F_G=\frac{x}{2\tau}
$$

and, in the usual real Riemannian norm,

$$
\left\langle\tau|\nabla F_G|^2\right\rangle_G=n.
$$

Perelman's real auxiliary functional uses the complete real dimension $d=2n$:

$$
\left\langle
\tau|\nabla F_G|^2+F_G-2n
\right\rangle_G
=
n+n-2n
=0.
$$

Therefore, the two choices answer different questions:

$$
-n
\quad\Longrightarrow\quad
\text{centering of the entropic sector},
$$

$$
-2n
\quad\Longrightarrow\quad
\text{vanishing of the complete real Perelman functional on the Gaussian}.
$$

The GDQ action preserves the first choice. It should not be silently identified with the auxiliary functional $\mathcal W$.

## Effect on variational equations

In the sector of fixed dimension and normalized measure,

$$
\int_M\mathcal U\,dV_g=1,
$$

an integrated dimensional constant only changes the reference value:

$$
\int_M C\mathcal U\,dV_g=C.
$$

For variations tangent to the normalization constraint,

$$
\delta\int_M C\mathcal U\,dV_g=0,
\qquad
\delta^2\int_M C\mathcal U\,dV_g=0.
$$

Thus, $-n$ does not alter the saddle or the physical Hessian in this sector. It defines the entropic zero. Outside the normalized constraint, however, the constant participates in the variation and cannot be removed as if it were a universal gauge.

## The cosmological space

The auxiliary cosmological space $T^5\times S^3$ has real dimension eight. To insert it into the complex writing of the action, it is necessary to specify an admissible Hermitian structure or a reduction map to the official bulk. When this compatibility yields complex dimension four,

$$
n=4
$$

remains the universal dimensional zero.

This does not force the cosmological background to have zero action. Its residual contribution is:

$$
\mathcal A_{\rm cos}
=
\left\langle
\tau\left(
\mathcal R_{\rm cos}
+
g^{\mu\bar\nu}
\partial_\mu f_{\rm cos}
\partial_{\bar\nu}\bar f_{\rm cos}
\right)
+
\operatorname{Re}f_{\rm cos}
-4
\right\rangle_{\rm cos}.
$$

The curvature of $S^3$, the torsion, the thermal profile, and the global conditions can make $\mathcal A_{\rm cos}$ different from zero. This residue is the physical content of the background, not a normalization error.

If it is convenient to measure excitations in relation to the stationary cosmological universe $\Phi_{\rm cos}$, we define the relative quantity:

$$
\mathcal S_{\rm rel}[\Phi]
=
\mathcal S_{\rm GDQ}[\Phi]
-
\mathcal S_{\rm GDQ}[\Phi_{\rm cos}].
$$

This subtraction does not modify the official action or its equations. It only chooses the cosmological background as the origin for the comparison of energies.

Therefore, there are two reference levels:

$$
\boxed{
-n
=
\text{universal dimensional zero},
}
$$

and

$$
\boxed{
\mathcal S_{\rm GDQ}[\Phi_{\rm cos}]
=
\text{optional physical zero of a specific cosmological background}.
}
$$

They must not be confused.
