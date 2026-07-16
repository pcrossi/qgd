---
title: Official action dimensional consistency
status: active
concepts:
  - official action
  - Lambda_C
  - dimensional analysis
---

# Official action dimensional consistency

## Statement

The official GDQ action is dimensionally consistent when `Lambda_C` is read as
a dimensionless cutoff number in coordinates normalized by the Cartan length.

## Derivation

Use

$$
z^a=\ell_C\widehat z^a,
\qquad
\tau=\ell_C^2\widehat\tau,
\qquad
z_\tau=\ell_C^2\widehat z_\tau.
$$

Then

$$
\mathcal R=\ell_C^{-2}\widehat{\mathcal R},
\qquad
\mathcal U=\ell_C^{-2n}\widehat{\mathcal U},
\qquad
dV_g=\ell_C^{2n}dV_{\widehat g},
$$

and `d tau/tau` is dimensionless. Therefore the full integral multiplying the
prefactor is a pure number.

The action has dimension of action because

$$
\Lambda_C=\ell_Ck_C=1,
\qquad
\left[\frac{\hbar}{\Lambda_C^2}\right]=[\hbar].
$$

## Consequence

Do not use `Lambda_C` as a dimensional length, momentum or energy in the
official action. Use:

- `ell_C` for length;
- `k_C=ell_C^{-1}` for inverse length;
- `E_C=hbar c k_C` for energy.

## Sources

- `manuscrito/04_action_consistency/04.2 - A ação oficial da GDQ.md`
- `manuscrito/04_action_consistency/04.4 - Como ler cada termo da ação.md`
- `manuscrito/notes/action/Dimensão e normalização da ação oficial.md`
