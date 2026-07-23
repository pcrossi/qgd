# Saída — integral de forma exata e período

## Classificação

Ilustração de contorno. Não é previsão física.

## Construção

Para $F(\theta)=\cos\theta$:

$$
\oint_{S^1}dF=F(2\pi)-F(0)=0.
$$

Para a coordenada angular multivalorada:

$$
\int_0^{2\pi}d\theta=2\pi.
$$

## Resultados numéricos

| N | $\oint d(\cos\theta)$ | $\int d\theta$ | erro período |
|---:|---:|---:|---:|
| 200 | 0.0000000000000000e+00 | 6.2831853071795862e+00 | 0.000e+00 |
| 1000 | 2.2204460492503131e-16 | 6.2831853071795862e+00 | 0.000e+00 |
| 5000 | 0.0000000000000000e+00 | 6.2831853071795862e+00 | 0.000e+00 |
| 20000 | -2.2204460492503131e-16 | 6.2831853071795862e+00 | 0.000e+00 |

## Veredito

A checagem passou: forma exata regular cancela; período angular sobrevive.

Esta saída ilustra a diferença entre exatidão global e período topológico. Ela não fixa unidade de carga nem normalização física.
