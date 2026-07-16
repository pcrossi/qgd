---
title: Physical Hessian and GDQ loops
status: active
concepts:
  - Hessian
  - loops
  - perturbation
  - P_phys
---

# Physical Hessian and GDQ loops

## Definition

Given an admissible on-shell background

$$
\Phi_*=(g_*,f_*,\bar f_*),
$$

the raw Hessian is

$$
\mathbb H_*
=\operatorname{Hess}\operatorname{Re}\mathcal S_{\rm GDQ}\big|_{\Phi_*}.
$$

The physical Hessian is

$$
\mathbb H_*^{\rm phys}
=P_{\rm phys}\mathbb H_*P_{\rm phys},
$$

with domain fixed by regularity, constraints, quotient conditions and
boundary/interface data.

## Loop meaning

The fundamental one-loop GDQ object is

$$
\Gamma_{\rm GDQ}^{(1)}
=\frac12\operatorname{Tr}_{\rm phys}
\ln\operatorname{Hess}\mathcal S_{\rm GDQ}.
$$

External propagators such as Dirac, Yang-Mills or Lichnerowicz operators can
appear only as reductions or audits after this Hessian has been constructed.

## Consequence

No background is perturbatively valid until:

1. it is on shell;
2. the normalization and boundary constraints are imposed;
3. gauge/redundant directions are quotiented;
4. the physical Hessian is stable or its instabilities are classified.

## Sources

- `manuscrito/04_action_consistency/04.7 - O que significa consistência em loops.md`
