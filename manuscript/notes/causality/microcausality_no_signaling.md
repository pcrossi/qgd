---
title: "Microcausality and operational no-signaling"
---

# Microcausality and operational no-signaling

This note records the secure closure of operational causality. GDQ does not use the advanced branch as a message channel to the past. The controllable response of classical apparatuses is retarded, while advanced sectors can appear as global boundary conditions.

## 1. Causal cone

On the reconstructed physical sheet, causality is defined by the Lorentzian metric $h$:

$$
\mathcal C_h(p)
=
\{v\in T_pN:h_p(v,v)\le0\}.
$$

In the flat sector,

$$
h=-dt^2+d\mathbf x^2.
$$

Therefore,

$$
h(v,v)\le0
\quad
\Longleftrightarrow
\quad
|\mathbf v|\le |v^0|.
$$

## 2. Propagators

If $P_h$ is the effective hyperbolic operator of the sector, with principal symbol $h^{\mu\nu}k_\mu k_\nu$, the fundamental propagators satisfy

$$
P_hG_{\rm ret}(x,y)=\delta_h(x,y),
\qquad
\operatorname{supp}G_{\rm ret}(\cdot,y)\subset J_h^+(y),
$$

and

$$
P_hG_{\rm adv}(x,y)=\delta_h(x,y),
\qquad
\operatorname{supp}G_{\rm adv}(\cdot,y)\subset J_h^-(y).
$$

The Feynman propagator organizes time-ordered amplitudes:

$$
G_F(x,y)
=
\langle\Omega|
T\{\Phi(x)\Phi(y)\}
|\Omega\rangle.
$$

In the flat sector,

$$
G_F(k)
=
\frac{i}{k_h^2-m^2+i0},
\qquad
k_h^2=h^{\mu\nu}k_\mu k_\nu.
$$

## 3. Commutator and causal support

The Pauli--Jordan function is defined as:

$$
\Delta(x,y)
=
G_{\rm ret}(x,y)-G_{\rm adv}(x,y).
$$

For a reconstructed scalar field,

$$
[\Phi(x),\Phi(y)]
=
i\hbar\,\Delta(x,y).
$$

Since the support of $\Delta$ is contained within the causal cone,

$$
x\perp_h y
\quad
\Longrightarrow
\quad
\Delta(x,y)=0.
$$

Therefore,

$$
x\perp_h y
\quad
\Longrightarrow
\quad
[\Phi(x),\Phi(y)]=0.
$$

For local observables, the operational statement is:

$$
O_A\perp_h O_B
\quad
\Longrightarrow
\quad
[\mathcal A(O_A),\mathcal A(O_B)]=0.
$$

## 4. Why Sudarshan does not signal to the past

The symmetric combination

$$
G_{\rm sym}
=
\frac12
\left(
G_{\rm ret}+G_{\rm adv}
\right)
$$

is a global boundary solution. It can encode phase, closure, normalization, poles, and boundary constraints.

The controllable physical response to a local classical source $J_{\rm app}$ is retarded:

$$
\delta\Phi(x)
=
\int_N
G_{\rm ret}(x,y)
J_{\rm app}(y)
dV_h(y).
$$

Thus,

$$
x\notin J_h^+(\operatorname{supp}J_{\rm app})
\quad
\Longrightarrow
\quad
\delta\Phi(x)=0.
$$

The advanced branch is part of the conditioned solution, not a degree of freedom that an agent can modulate to transmit bits to the past.

## 5. No-signaling in separate algebras

In the reconstructed operational layer, consider two spatially separated regions $O_A$ and $O_B$. If

$$
[\mathcal A(O_A),\mathcal A(O_B)]=0,
$$

a non-selective local operation in $O_B$, described by operators $M_\alpha\in\mathcal A(O_B)$ with

$$
\sum_\alpha M_\alpha^\dagger M_\alpha=1,
$$

does not alter the statistics of an observable $A\in\mathcal A(O_A)$:

$$
\langle A\rangle'
=
\sum_\alpha
\operatorname{Tr}
\left(
M_\alpha\rho M_\alpha^\dagger A
\right).
$$

Using spatial commutation,

$$
\langle A\rangle'
=
\sum_\alpha
\operatorname{Tr}
\left(
\rho A M_\alpha^\dagger M_\alpha
\right)
=
\operatorname{Tr}(\rho A)
=
\langle A\rangle.
$$

Therefore, local operations in $O_B$ do not change local marginals in $O_A$.

## 6. Delayed choice

In the delayed choice experiment, the apparatus alters the boundary value problem at a late stage. This can change final correlations:

$$
P(a,b|x,y).
$$

But it cannot change the prior local marginal if the choice $y$ lies outside the causal past of the record $a$:

$$
P(a|x,y)=P(a|x,y').
$$

Therefore, the correct reading is:

$$
\boxed{
\text{global boundary change}
+
\text{local no-signaling},
\text{ not operational retrocausality.}
}
$$

## 7. Status

This closure depends on the operational reconstruction of the sector: local operators, domains, positive inner product, and physical algebra must be defined. When this layer exists, microcausality implies no-signaling.
