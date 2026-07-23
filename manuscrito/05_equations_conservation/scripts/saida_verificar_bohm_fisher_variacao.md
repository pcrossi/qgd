# Saída — variação Fisher-Bohm

## Classificação

Teste numérico/simbólico de variação. Não é previsão física.

## Identidade verificada

$$
\frac{\delta}{\delta\rho}\int\frac{|\nabla\rho|^2}{\rho}\,dx
=-4\frac{\Delta\sqrt\rho}{\sqrt\rho}.
$$

## Resultados de malha periódica

| N | erro máximo | erro relativo |
|---:|---:|---:|
| 200 | 4.626814656239e-05 | 5.303095815359e-05 |
| 400 | 1.158038310345e-05 | 1.326992296575e-05 |
| 800 | 2.895440856521e-06 | 3.317479751867e-06 |
| 1600 | 7.239507249235e-07 | 8.294609553843e-07 |

## Veredito

A checagem passou no refinamento usado.

Esta saída verifica a identidade diferencial em 1D periódica; a forma GDQ geral usa $\Delta_g$ e domínio/contorno próprios.
