# Saída — corrente de fase em 1D

## Classificação

Ilustração de conservação de corrente. Não é previsão física.

## Identidade verificada

Em um intervalo:

$$
\int_0^1\partial_xJ\,dx=J(1)-J(0).
$$

Logo:

$$
\frac{dQ}{dt}=-J(1)+J(0).
$$

## Resultados

| caso | $\int\partial_xJdx$ | $J(1)-J(0)$ | $dQ/dt$ |
|---|---:|---:|---:|
| constante | -1.136868377216e-16 | 0.000000000000e+00 | -0.000000000000e+00 |
| linear | 3.000000000000e-01 | 3.000000000000e-01 | -3.000000000000e-01 |
| sem_fluxo_liquido | -1.942890293094e-16 | 0.000000000000e+00 | -0.000000000000e+00 |

## Veredito

A checagem passou.

Esta saída ilustra conservação integrada; a corrente GDQ real depende de $\mathcal U$, $g$ e $S_R$.
