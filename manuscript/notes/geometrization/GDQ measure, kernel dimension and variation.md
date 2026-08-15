---
title: "GDQ measure, kernel dimension and variation"
type: derivation
status: exact-identity
---

# GDQ measure, kernel dimension and variation

In real dimension $d$, the flat heat kernel has the prefactor

$$
(4\pi\tau)^{-d/2}.
$$

Since $d=2n$, it becomes $(4\pi\tau)^{-n}$; with $n=4$, $(4\pi\tau)^{-4}$.

The complexified measure is

$$
\mathcal U
=(4\pi z_\tau)^{-n}e^{-(f+\bar f)/2}.
$$

Since the material density is defined by

$$
\rho=e^{-(f+\bar f)/2},
$$

the correct relation between the action measure and the density is

$$
\boxed{
\mathcal U
=\frac{\rho}{(4\pi z_\tau)^n}.
}
$$

Therefore, the short phrase "$\mathcal U=\rho$" is only correct if the kernel factor has been removed by definition. Defining

$$
\widetilde{\mathcal U}
:=(4\pi z_\tau)^n\mathcal U,
$$

we have

$$
\boxed{
\widetilde{\mathcal U}=\rho.
}
$$

This point is important because $\mathcal U$ and $\rho$ are not two independent fields that would need to be identified by a dynamic equation. Both come from the same text field $f$; $\mathcal U$ is the density $\rho$ accompanied by the geometric kernel weight.

With $z_\tau$ fixed,

$$
\delta\mathcal U
=-\frac12\mathcal U(\delta f+\delta\bar f).
$$

If the metric varies, the volume element contributes separately:

$$
\delta\sqrt{\det g}
=\frac12\sqrt{\det g}\,g^{AB}\delta g_{AB}
$$

in real coordinates, with the corresponding Hermitian form.

## Secondary path by uniqueness

Although GDQ does not need to prove $\widetilde{\mathcal U}=\rho$ by evolution, we can record the dynamic route to avoid logical ambiguity.

Suppose two functions $u_1$ and $u_2$ satisfy the same transport equation in the same domain:

$$
\partial_\tau u+\nabla_A(uv^A)=0,
$$

in

$$
M=\mathbb R^4\times T^4,
$$

with $v$ sufficiently regular, for example

$$
v\in L^1([0,T];W^{1,\infty}_{\rm loc}(M)),
$$

and

$$
u_1,u_2\in L^\infty([0,T];L^1(M)).
$$

Assume further periodicity in the $T^4$ sector, sufficient decay in the $\mathbb R^4$ sector, and no boundary flux unaccounted for by the causal boundary $\gamma$. If

$$
u_1(\tau_0,x)=u_2(\tau_0,x),
$$

then $w=u_1-u_2$ satisfies

$$
\partial_\tau w+\nabla_A(wv^A)=0,
\qquad
w(\tau_0,x)=0.
$$

By the uniqueness of the linear transport equation in this class,

$$
w(\tau,x)=0.
$$

Applying this to

$$
u_1=\widetilde{\mathcal U},
\qquad
u_2=\rho,
$$

we would obtain again

$$
\widetilde{\mathcal U}=\rho.
$$

But this proof is secondary: it requires the same initial and boundary conditions. The identity used in the official action is stronger, as it is constitutive.

## Relation with Born

In the projective Madelung sector, one writes

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
$$

Then

$$
|\Psi|^2=\rho.
$$

Therefore, the local probabilistic density of the effective layer is $\rho$, while $\mathcal U\,dV_g$ is the weighted measure of the action:

$$
\mathcal U\,dV_g
= \frac{\rho}{(4\pi z_\tau)^n}dV_g.
$$

The factor $(4\pi z_\tau)^{-n}$ belongs to the geometric kernel; it does not redefine the constitutive density $\rho$.
