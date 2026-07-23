# Saída — polarização heat-kernel toy

## Classificação

Ilustração heat-kernel. Não é previsão física.

## Integral toy

$$
I(\Lambda)=\int_0^\Lambda\frac{k}{k^2+m^2}e^{-\tau k^2}\,dk.
$$

A comparação sem regulador é:

$$
I_0(\Lambda)=\frac12\log\left(\frac{\Lambda^2+m^2}{m^2}\right).
$$

## Parâmetros

- $m=1$.
- $\tau=0.25$.

## Resultados

| $\Lambda$ | regulado | não regulado |
|---:|---:|---:|
| 1 | 3.110609607716e-01 | 3.465735902800e-01 |
| 2 | 5.764434765726e-01 | 8.047189562171e-01 |
| 4 | 6.686478778126e-01 | 1.416606672028e+00 |
| 8 | 6.704427190105e-01 | 2.087193634948e+00 |
| 16 | 6.704427218824e-01 | 2.774538042448e+00 |
| 32 | 6.704427202823e-01 | 3.466223945786e+00 |

## Veredito

A integral regulada satura numericamente no UV neste toy model.

Esta saída não prova finitude universal da GDQ. Ela apenas ilustra o efeito de um fator heat-kernel.
