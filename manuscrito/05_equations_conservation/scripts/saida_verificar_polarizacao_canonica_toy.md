# Saída — polarização canônica toy

## Classificação

Ilustração de Routh/Cauchy--Schwarz. Não é previsão física.

## Desigualdade

$$
H[\Pi,\rho]=\int\frac{\Pi^2}{2A\rho}\,d\Sigma
\geq
\frac{Q^2}{2AN_\rho}.
$$

A igualdade ocorre para:

$$
\Pi=\frac{Q}{N_\rho}\rho.
$$

## Parâmetros toy

- $A=2.0$.
- $Q=1.0$.
- $N_\rho=1$.
- Limite inferior: `2.500000000000e-01`.

## Perturbações de carga zero em torno do minimizador

| amplitude | carga | $H$ | excesso $H-H_{min}$ |
|---:|---:|---:|---:|
| 0 | 1.000000000000e+00 | 2.500000000000e-01 | 0.000000000000e+00 |
| 0.1 | 1.000000000000e+00 | 2.513082384843e-01 | 1.308238484342e-03 |
| 0.5 | 1.000000000000e+00 | 2.827059621086e-01 | 3.270596210856e-02 |
| 1 | 1.000000000000e+00 | 3.808238484342e-01 | 1.308238484342e-01 |

## Veredito

A checagem passou.

Esta saída ilustra o minimizador condicionado. Ela não prova que a dinâmica GDQ seleciona esse setor sem a ponte global--local/medida.
