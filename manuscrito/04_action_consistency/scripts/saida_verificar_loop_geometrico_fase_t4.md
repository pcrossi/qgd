---
title: "Saída — loop geométrico da fase toroidal"
---

# Saída — loop geométrico da fase toroidal

Parâmetros geométricos sem ajuste:

- modo toroidal `n=1`
- `kappa=1.0`
- `R=1.0`
- `lambda_perp=0.0`
- `q_n=n*kappa=1.0`
- `m_n=sqrt(n^2/R^2+lambda_perp)=1.0`
- `s0=0.2`
- `eta=s0*m_n^2=0.2`

## Polarização e Ward

| $Q$ | $Q^2$ | $\Pi_{n,s_0}(Q^2)$ | $\|Q^\mu\Pi_{\mu\nu}\|$ |
|---:|---:|---:|---:|
| `0.000000` | `0.000000` | `0.000000000000e+00` | `0.000000000000e+00` |
| `0.250000` | `0.062500` | `1.074394263932e-05` | `0.000000000000e+00` |
| `0.500000` | `0.250000` | `4.230506124982e-05` | `0.000000000000e+00` |
| `1.000000` | `1.000000` | `1.594841707528e-04` | `0.000000000000e+00` |
| `2.000000` | `4.000000` | `5.247031413505e-04` | `0.000000000000e+00` |
| `5.000000` | `25.000000` | `1.566659054231e-03` | `0.000000000000e+00` |
| `10.000000` | `100.000000` | `2.241750121166e-03` | `0.000000000000e+00` |

## Saturação ultravioleta

- $\Pi(0)$ numérico: `0.000000000000e+00`.
- limite saturado $q_n^2 E_1(\eta)/(48\pi^2)$: `2.580841673285e-03`.
- maior resíduo de Ward na tabela: `0.000000000000e+00`.

## Classificação

Teste de consistência do loop geométrico derivado da Hessiana da fase; não é previsão metrológica.
