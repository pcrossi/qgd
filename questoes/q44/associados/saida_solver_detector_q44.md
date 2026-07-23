# Q44 — saída do solver reduzido com detector DtN
## Classificação
Avaliação direta de um detector reduzido derivado por DtN/Schur no setor Madelung em fundo fixo. Não é evolução da métrica completa.
## Parâmetros fixos do detector reduzido
- `lambda_det = 1.1`
- `L = 1`
- `R_det = lambda*coth(lambda*L) = 1.37414284103`
- `C_path = 1` marcador primitivo normalizado
## Resultados principais em N=8000
| zeta_det | Gamma_det | Contraste de franja `exp(-Gamma)` | Visibilidade bruta central | Norma trapezoidal |
|---:|---:|---:|---:|---:|
| 0 | 0.000000000 | 1.000000000 | 0.987400675 | 1.670914351 |
| 0.5 | 0.171767855 | 0.842174657 | 0.893408543 | 1.685773505 |
| 1.25 | 1.073549095 | 0.341793305 | 0.547559863 | 1.732884088 |
| 2.5 | 4.294196378 | 0.013647535 | 0.270891364 | 1.763778801 |

## Convergência de malha
| zeta_det | N | Gamma_det | Contraste de franja | Visibilidade bruta central |
|---:|---:|---:|---:|
| 0 | 1000 | 0.000000000 | 1.000000000 | 0.987399527 |
| 0 | 2000 | 0.000000000 | 1.000000000 | 0.987400345 |
| 0 | 4000 | 0.000000000 | 1.000000000 | 0.987400592 |
| 0 | 8000 | 0.000000000 | 1.000000000 | 0.987400675 |
| 0.5 | 1000 | 0.171767855 | 0.842174657 | 0.893187848 |
| 0.5 | 2000 | 0.171767855 | 0.842174657 | 0.893357065 |
| 0.5 | 4000 | 0.171767855 | 0.842174657 | 0.893368952 |
| 0.5 | 8000 | 0.171767855 | 0.842174657 | 0.893408543 |
| 1.25 | 1000 | 1.073549095 | 0.341793305 | 0.546696636 |
| 1.25 | 2000 | 1.073549095 | 0.341793305 | 0.547349962 |
| 1.25 | 4000 | 1.073549095 | 0.341793305 | 0.547397763 |
| 1.25 | 8000 | 1.073549095 | 0.341793305 | 0.547559863 |
| 2.5 | 1000 | 4.294196378 | 0.013647535 | 0.269735362 |
| 2.5 | 2000 | 4.294196378 | 0.013647535 | 0.270609027 |
| 2.5 | 4000 | 4.294196378 | 0.013647535 | 0.270673076 |
| 2.5 | 8000 | 4.294196378 | 0.013647535 | 0.270891364 |

## Validação de limites
- `zeta_det = 0`: `Gamma_det = 0`, logo o padrão coerente é recuperado.
- `zeta_det` crescente: o termo cruzado é multiplicado por `exp(-Gamma_det)` e a visibilidade cai monotonamente.
- `Gamma_det >> 1`: o contraste de franja `exp(-Gamma_det)` tende a zero e a densidade tende a `I1 + I2`, isto é, mistura sem interferência.
- A visibilidade bruta central não precisa tender exatamente a zero porque ainda inclui variação do envelope incoerente; o observável de coerência é o coeficiente do termo cruzado.

## Fórmula avaliada
$$
\rho_{\rm det}=I_1+I_2+2e^{-\Gamma_{\rm det}}\sqrt{I_1I_2}\cos\Delta\phi.
$$
com
$$
\Gamma_{\rm det}=\frac12\zeta_{\rm det}^2\lambda_{\rm det}\coth(\lambda_{\rm det}L).
$$
