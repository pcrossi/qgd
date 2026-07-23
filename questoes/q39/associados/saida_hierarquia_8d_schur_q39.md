# Q39 — saída da hierarquia 8D por Schur

## Valores reduzidos

- `R_mu_0 = 206.768593470628673`
- `R_tau_0 = 3477.446405098381092`
- `Q(R_mu_0,R_tau_0) = 0.666666666666667`

## Resposta linear da saturação

- `dQ/dR_mu = -4.426729664581531e-04`
- `dQ/dR_tau = 2.884779013665275e-05`
- `dR_tau/dR_mu | Q = 15.345125722323942`

## Cotas de Schur

| cenário | j_mix | m_perp^2 | Delta_Schur | |delta R_mu| max | |delta R_tau direto| max |
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
