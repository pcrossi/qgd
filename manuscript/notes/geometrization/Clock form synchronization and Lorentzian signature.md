---
title: "Clock form, synchronization and Lorentzian signature"
---

# Clock form, synchronization and Lorentzian signature

This note records the construction used in Chapter 2 to pass from the positive Riemannian bulk to the effective physical space-time. The construction does not change the official action and does not alter the signature of the bulk. It defines a projected physical metric after a clock-direction has been selected.

## 1. The Riemannian pullback remains positive

If $X:N^4\to M^8$ is an immersion and $g$ is positive in the bulk, then

$$
q=X^*g
$$

is positive on $N$. For every non-zero vector $v\in T_pN$,

$$
q(v,v)=g(dXv,dXv)>0.
$$

Therefore, the Lorentzian signature cannot arise solely by restricting $g$ to a submanifold. An additional datum is required: a clock 1-form.

## 2. Reflection by a clock-form

Let $u$ be a non-zero 1-form on $N$ and define

$$
s=q^{-1}(u,u)>0.
$$

The effective physical metric is

$$
h=q-2\frac{u\otimes u}{s}.
$$

Choose a $q$-orthonormal frame in which

$$
u=\sqrt{s}\,e^0.
$$

Then

$$
q=(e^0)^2+(e^1)^2+(e^2)^2+(e^3)^2
$$

and

$$
2\frac{u\otimes u}{s}=2(e^0)^2.
$$

Therefore

$$
h=-(e^0)^2+(e^1)^2+(e^2)^2+(e^3)^2.
$$

Thus,

$$
\operatorname{sign}(h)=(-,+,+,+).
$$

This is an algebraic result. It proves the signature once the clock-form is given, but it does not yet select which clock-form is physical.

## 3. Selection by cosmological simultaneity

In the Einstein cosmological space used as an auxiliary global domain,

$$
M_{\rm cos}=T^5\times S^3,
$$

separate the distinguished cosmological cycle:

$$
T^5=T^4\times S_E^1.
$$

If $\Theta_E$ parametrizes $S_E^1$ and $R_E$ is its radius, the length 1-form of this cycle is

$$
\omega_E=R_Ed\Theta_E.
$$

The hypersurfaces

$$
\Theta_E=\text{constant}
$$

define comoving simultaneity. In the pointed local limit, we introduce

$$
x^0=R_E\Theta_E.
$$

Therefore,

$$
dx^0=R_Ed\Theta_E=\omega_E.
$$

The local tangent limit transports the cosmological form to

$$
\omega_0=dx^0.
$$

In the local physical frame,

$$
u=X^*\omega_0.
$$

The synchronization at the common event requires

$$
\iota^*\omega_E=u,
$$

where $\iota$ identifies the cosmological sheet with the local tangent frame at the base-point. This condition fixes the direction and the unit of the clock. After normalization,

$$
q^{-1}(u,u)=1.
$$

The causal boundary $\gamma$ fixes the orientation between $u$ and $-u$.

## 4. Logical status

The result is a conditional theorem:

- given the Einstein cosmological background;
- given its comoving foliation;
- given the pointed local tangent limit;
- given the synchronization at the common event;
- given the causal orientation;

then the physical clock-form is selected and the projected metric has a Lorentzian signature.

No second Lorentzian bulk was postulated. Nor was the official action altered. The construction only explains how a physical observer reads an effective metric with signature $(-,+,+,+)$ from a positive Riemannian bulk when the clock-direction is selected by the global-local bridge.
