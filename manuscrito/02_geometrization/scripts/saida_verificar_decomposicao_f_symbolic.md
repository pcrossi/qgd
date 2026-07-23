# Saída — verificação da decomposição de $f$

## Classificação

Teste simbólico de identidade constitutiva. Não é previsão física.

## Identidades verificadas

$$
f=-\frac{S_I}{\hbar}+i\frac{S_R}{\hbar},
\qquad
\bar f=-\frac{S_I}{\hbar}-i\frac{S_R}{\hbar}.
$$

Daí:

$$
\rho=e^{-(f+\bar f)/2}=e^{S_I/\hbar}
$$

e

$$
S_R=\frac{\hbar}{2i}(f-\bar f).
$$

## Casos numéricos arbitrários

| $\hbar$ | $S_I$ | $S_R$ | $\rho(f)$ | $e^{S_I/\hbar}$ | erro $\rho$ | erro $S_R$ |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | -0.3 | 0.7 | 0.740818220682 | 0.740818220682 | 0.000e+00 | 0.000e+00 |
| 2 | 1.1 | -0.4 | 1.73325301787 | 1.73325301787 | 0.000e+00 | 0.000e+00 |
| 0.5 | 0.2 | 1.3 | 1.49182469764 | 1.49182469764 | 0.000e+00 | 0.000e+00 |

## Veredito

A checagem passou.

Esta saída verifica apenas a identidade constitutiva. Ela não deriva a ação oficial nem a dinâmica de $f$.
