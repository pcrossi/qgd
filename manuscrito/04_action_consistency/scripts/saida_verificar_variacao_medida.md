# Saída — variação da medida constitutiva

## Classificação

Teste simbólico de identidade constitutiva. Não é previsão física.

## Identidade linearizada

Para métrica fixa e $z_\tau$ fixo:

$$
\frac{\delta\mathcal U}{\mathcal U}
=-\frac12\delta(f+\bar f).
$$

## Teste por diferenças finitas

| $\epsilon$ | variação relativa exata | predição linear | erro |
|---:|---:|---:|---:|
| 1e-02 | -4.9875208073175640e-03 | -5.0000000000000001e-03 | 1.248e-05 |
| 1e-04 | -4.9998750020897234e-05 | -5.0000000000000002e-05 | 1.250e-09 |
| 1e-06 | -4.9999987497300998e-07 | -4.9999999999999998e-07 | 1.250e-13 |
| 1e-08 | -4.9999999858525233e-09 | -5.0000000000000001e-09 | 1.415e-17 |

## Veredito

A checagem passou no limite linear.

Esta saída verifica apenas a variação constitutiva da medida, não as equações de movimento.
