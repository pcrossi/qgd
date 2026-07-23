# Saída — Q55 virial da sela radial e lambda_T

Classificação: teste de consistência / diagnóstico variacional.

## Identidade testada


$$
2K+3U_T+W=0
$$

com:

$$
K=\frac12\int |\nabla u|^2dV,
\quad
U_T=\frac{\lambda_T}{2}\int u^4dV,
\quad
W=\frac12\int \phi u^2dV.
$$

## Varredura


| lambda_T | success | mu | K | U_T | W | virial relativo | M power |
|---:|:---:|---:|---:|---:|---:|---:|---:|
| 0 | True | -3.840920e-02 | 3.856912e-01 | 0.000000e+00 | -4.341777e-01 | 2.797079e-01 | 3.00005593 |
| 0.5 | True | -3.784198e-02 | 3.853978e-01 | 3.399752e-03 | -4.338668e-01 | 2.857346e-01 | 3.00005847 |
| 1 | False | 1.741534e-01 | 2.846037e+02 | 4.377606e+01 | -9.460335e+01 | 7.620457e-01 | 26.14589536 |
| 3 | True | -1.067957e-01 | 3.167552e-01 | 9.808337e-02 | -9.274782e-01 | 1.522043e-04 | 3.00007134 |
| 8 | True | -7.962732e-02 | 1.860019e-01 | 1.131944e-01 | -7.065085e-01 | 3.581146e-03 | 3.00008994 |
| 21 | True | -5.607343e-02 | 1.126610e-01 | 1.189944e-01 | -5.276446e-01 | 4.924595e-02 | 3.00010046 |

## Leitura


A identidade de virial audita a estacionariedade sob reescala de massa preservada. Como o domínio é truncado por `u(R)=0`, o resíduo inclui termos de bordo finitos.

O teste mostra que `lambda_T` parametriza uma família de selas reduzidas. Portanto, a virial não determina sozinha o valor universal de `lambda_T`; ela fornece a equação de balanço que o valor derivado da Hessiana oficial deve satisfazer.

## Status


$$
\boxed{
\text{lambda_T ainda depende da projeção torsional da Hessiana oficial.}
}
$$