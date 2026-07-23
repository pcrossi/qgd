# Verificação do gap eletromagnético no colar cilíndrico

## Classificação

**Avaliação direta e teste de convergência** do operador radial de
Neumann derivado em questoes/q35/associados/operador_em_cilindrico_no_go.md.

| $L$ | modo zero | $\lambda_1^{\rm num}$ | $\pi^2/L^2$ | erro relativo |
|---:|---:|---:|---:|---:|
| 1.0 | -1.421e-10 | 9.8695917174e+00 | 9.8696044011e+00 | 1.285e-06 |
| 2.0 | -3.553e-11 | 2.4673979294e+00 | 2.4674011003e+00 | 1.285e-06 |
| 4.0 | -8.882e-12 | 6.1684948234e-01 | 6.1685027507e-01 | 1.285e-06 |
| 8.0 | -2.220e-12 | 1.5421237058e-01 | 1.5421256877e-01 | 1.285e-06 |
| 16.0 | -5.551e-13 | 3.8553092646e-02 | 3.8553142192e-02 | 1.285e-06 |

## Refinamento para $L=1$

| pontos | $\lambda_1^{\rm num}$ | erro relativo |
|---:|---:|---:|
| 50 | 9.8663578586e+00 | 3.289e-04 |
| 100 | 9.8687926854e+00 | 8.224e-05 |
| 200 | 9.8694014672e+00 | 2.056e-05 |
| 400 | 9.8695536673e+00 | 5.140e-06 |
| 800 | 9.8695917174e+00 | 1.285e-06 |

A combinação $L^2\lambda_1$ converge para $\pi^2$. Assim,

$$
\lambda_1^+=\frac{\pi^2}{L^2}\longrightarrow0
\quad\text{quando}\quad L\longrightarrow\infty.
$$

O cálculo confirma que o colar local infinito não fornece uma escala
eletromagnética positiva; no colar compacto ela depende do comprimento
global $L$.
