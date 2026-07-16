# Comparação de kernels geométricos covariantes — Q34

## Classificação

**Teste de consistência e sensibilidade ao kernel.**

| kernel | $\Pi(0)$ | erro Ward | $\Pi(Q_*^2)$ | $\Pi(\infty)$ | monotônica | limitada |
|:---|---:|---:|---:|---:|:---:|:---:|
| canonico | 0.000e+00 | 1.917e-20 | 1.761341916722e-04 | 2.050140062891e-03 | True | True |
| mistura | 0.000e+00 | 1.016e-20 | 1.534833676711e-04 | 1.556555412333e-03 | True | True |
| inteiro_mais | 0.000e+00 | 2.794e-20 | 2.285301085616e-04 | 3.653648455168e-03 | True | True |

Variação do limite UV em relação ao kernel canônico:

- canonico: +0.000000%.
- mistura: -24.075655%.
- inteiro_mais: +78.214578%.

Ward, subtração e saturação são robustas. Os valores numéricos mudam,
logo kernels distintos representam resoluções físicas distintas.
