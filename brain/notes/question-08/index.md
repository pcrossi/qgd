---
title: Question 08 - Causality
status: closed_structurally
source: questoes/q08/questao_08.md
updated: 2026-07-16
---

# Question 08 - Causality

Q8 asks how causality is preserved in GDQ, including delayed choice and the
advanced-retarded Sudarshan prescription.

## Causal cone

Causality is defined on $(N,h)$:

$$
\mathcal C_h(p)
=
\{v\in T_pN:h_p(v,v)\le0\}.
$$

The principal symbol common to scalar, gauge, torsion, gravity-linearized and
spinorial effective equations is governed by

$$
h^{\mu\nu}k_\mu k_\nu.
$$

Thus all effective fields share the cone of $h$.

## Propagators and microcausality

For a hyperbolic effective operator $P_h$,

$$
P_hG_{\rm ret}=\delta_h,
\qquad
\operatorname{supp}G_{\rm ret}(\cdot,y)\subset J_h^+(y),
$$

and

$$
P_hG_{\rm adv}=\delta_h,
\qquad
\operatorname{supp}G_{\rm adv}(\cdot,y)\subset J_h^-(y).
$$

The Pauli--Jordan function is

$$
\Delta=G_{\rm ret}-G_{\rm adv}.
$$

For spacelike separation,

$$
x\perp_h y
\quad\Longrightarrow\quad
[\Phi(x),\Phi(y)]=0.
$$

## Sudarshan prescription

$$
G_{\rm sym}
=
\frac12(G_{\rm ret}+G_{\rm adv})
$$

is a global boundary/phase consistency object, not an operational signalling
propagator. Local controllable response to a source is retarded:

$$
\delta\Phi(x)
=
\int_NG_{\rm ret}(x,y)J(y)\,dV_h(y).
$$

## No-signalling

For spacelike separated regions $O_A\perp_h O_B$,

$$
[\mathcal A(O_A),\mathcal A(O_B)]=0.
$$

Therefore nonselective local operations in $O_B$ do not change local
statistics in $O_A$. Delayed-choice experiments are global boundary-condition
changes and changes of final correlations, not retrocausal changes in locally
accessible past marginals.

## Status

Q8 is structurally closed under the effective-sector assumptions: principal
cone $h$, microcausal local algebra and retarded operational response. It does
not by itself solve all later measurement, Bell or detector-dynamics problems.

