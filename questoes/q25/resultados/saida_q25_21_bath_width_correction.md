# Q25.21 — Correção da largura térmica residual

Classificação: derivação reduzida e comparação.

A largura Schur anterior foi:

$$
\Theta_A^{\rm Schur}\simeq0.616921719.
$$

O ajuste efetivo pedia:

$$
\Theta_A^{\rm fit}\simeq0.721527850.
$$

Logo o resíduo alvo era:

$$
\Delta\Theta_A\simeq 1.046061310000e-01.
$$

Testei correções espectrais do banho usando os autovalores de `K_A` e os acoplamentos `J_k` do modo medido aos modos do aparelho:

| candidato | DeltaTheta | Theta total | erro vs fit |
|---|---:|---:|---:|
| `sum_J2_over_lam_plus_Ks_sq` | 3.123562407989e-02 | 6.481573430799e-01 | -7.337050692011e-02 |
| `sum_J2_over_lam_lam_plus_Ks` | 6.907130480224e-02 | 6.859930238022e-01 | -3.553482619776e-02 |
| `sqrt_gap_times_delta1` | 7.498274691141e-02 | 6.919044659114e-01 | -2.962338408859e-02 |
| `delta1_over_sqrt_KH` | 2.248389419717e-02 | 6.394056131972e-01 | -8.212223680283e-02 |

Veredito: o banho espectral discreto gera uma correção positiva da largura térmica, com ordem de grandeza correta mas ainda abaixo do resíduo necessário. Portanto a direção está correta, porém o modelo reduzido ainda omite canais dissipativos/causais ou pesos térmicos de aparelho que amplifiquem `DeltaTheta_A`.
