---
title: "Saída — hierarquia 8D por Schur"
---

# Saída — hierarquia 8D por Schur

## Valores reduzidos

- $R_\mu^{(0)} = 206.768593470628673$
- $R_\tau^{(0)} = 3477.446405098381092$
- $Q(R_\mu^{(0)},R_\tau^{(0)}) = 0.666666666666667$

## Resposta linear da saturação

- $\partial Q/\partial R_\mu = -4.426729664581531e-04$
- $\partial Q/\partial R_\tau = 2.884779013665275e-05$
- $(dR_\tau/dR_\mu)_Q = 15.345125722323942$

## Cotas de Schur

| cenário | $j_{\rm mix}$ | $m_\perp^2$ | $\Delta_{\rm Schur}$ | $|\delta R_\mu|_{\max}$ | $|\delta R_\tau|_{\max}$ direto |
|---|---:|---:|---:|---:|---:|
| produto | 0 | 1 | 0 | 0 | 0 |
| subcritico_fraco | 0.1 | 0.99 | 0.010101010101 | 0.010101010101 | 0.010101010101 |
| subcritico_4canais | 0.4 | 0.96 | 0.166666666667 | 0.166666666667 | 0.166666666667 |

## Fórmula 8D

$$
R_\mu^{(8)}
=
R_\mu^{(0)}-\sigma_\mu.
$$

$$
|\sigma_\ell|\le\Delta_{\rm Schur}.
$$

Mantendo a saturação $Q=2/3$:

$$
dR_\tau
=
-\frac{\partial_\mu Q}{\partial_\tau Q}dR_\mu.
$$
