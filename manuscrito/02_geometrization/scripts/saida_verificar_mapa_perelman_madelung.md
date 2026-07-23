# Saída — mapa Perelman--Madelung local

## Classificação

Teste simbólico/numérico de identidade constitutiva e não linearidade de Madelung. Não é previsão física.

## 1. Mapa direto e inverso no domínio $\rho>0$

| $\rho$ | $S_R$ | $\rho$ reconstruída | $S_R$ reconstruído | erro $\rho$ | erro $S_R$ | erro $f$ |
|---:|---:|---:|---:|---:|---:|---:|
| 0.2 | 0.7 | 0.2 | 0.7 | 0.000e+00 | 0.000e+00 | 0.000e+00 |
| 1.5 | -1.2 | 1.5 | -1.2 | 0.000e+00 | 0.000e+00 | 0.000e+00 |
| 3 | 2.4 | 3 | 2.4 | 4.441e-16 | 0.000e+00 | 0.000e+00 |

## 2. Nó $\rho=0$

No mapa inverso, $f=-\ln\rho+iS_R/\hbar$. Para $\rho=0$, $\ln\rho$ diverge. Portanto o nó não pertence ao domínio regular.

## 3. Superposição

A verificação usa:

$$
\rho_{12}=|\Psi_1+\Psi_2|^2=\rho_1+\rho_2+2\sqrt{\rho_1\rho_2}\cos((S_1-S_2)/\hbar).
$$

| $\rho_1$ | $\rho_2$ | $\Delta S/\hbar$ | $|\Psi_1+\Psi_2|^2$ | $\rho_1+\rho_2$ | interferência | erro identidade |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | -3.14159265359 | 1.49975978266e-32 | 2 | -2 | 1.500e-32 |
| 1 | 1 | -1.57079632679 | 2 | 2 | 1.22464679915e-16 | 4.441e-16 |
| 0.7 | 0.2 | 1.1 | 1.23944025567 | 0.9 | 0.339440255669 | 0.000e+00 |

## Veredito

As checagens passaram: o mapa é localmente invertível em $\rho>0$ e a superposição é não linear em $(\rho,S_R)$.

Nenhum alvo experimental foi usado.
