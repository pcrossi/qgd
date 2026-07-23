# Q53 — Execução reduzida do plano de massas neutras

## Classificação

Avaliação direta de uma cadeia GDQ reduzida/candidata. Não é ainda a Hessiana neutra 8D completa.

## Entradas GDQ congeladas antes da comparação

- `alpha = 7.297352564331424e-03`
- `Q_beta = 7.823335593100e+05 eV`
- `S_nu = alpha^7 Q_beta^2 = 6.744367477916e-04 eV^2`
- `chi_nu = 0.48 exp(-alpha/4) = 4.791251159771e-01`
- espectro reduzido candidato:

$$
\lambda = \left(0,\frac{\chi_\nu^2}{2},\frac{6\pi}{5}\right).
$$

O fator $6\pi/5$ é o ponto ainda condicional: precisa ser derivado da Hessiana/colagem neutra para virar previsão forte.

## Autovalores geométricos

| i | lambda_i |
|---:|---:|
| 1 | 0.000000000000e+00 |
| 2 | 1.147804383800e-01 |
| 3 | 3.769911184308e+00 |

## Escalas inerciais neutras resultantes

| modo | massa reduzida GDQ (eV) |
|---:|---:|
| 1 | 0.000000000000e+00 |
| 2 | 8.798417219655e-03 |
| 3 | 5.042386973059e-02 |
| soma | 5.922228695025e-02 |

## Diferenças quadradas

| quantidade | GDQ reduzido | NuFIT 6.0 NO | erro relativo |
|---|---:|---:|---:|
| dm21 | 7.741214557111e-05 | 7.490000000000e-05 | +3.353999e-02 |
| dm31 | 2.542566638608e-03 | 2.534000000000e-03 | +3.380678e-03 |

## Matriz folha--modo usada

| parâmetro | valor |
|---|---:|
| theta12 | 35.264389683 deg |
| theta23 | 45.000000000 deg |
| theta13 | 8.772427998 deg |
| delta_CP legado | 220.015793330 deg |
| erro unitariedade | 2.390e-16 |

## Bloco K^nu reduzido reconstruído

- erro hermiticidade: `1.388e-17`

Parte real:

- 1.250560347231e-01  -2.667862369375e-01  -3.424113861808e-01
- -2.667862369375e-01  1.886137751741e+00  1.803297501729e+00
- -3.424113861808e-01  1.803297501729e+00  1.873497836223e+00

Parte imaginária:

- 6.938893903907e-18  2.557318610447e-01  2.557318610447e-01
- -2.557318610447e-01  0.000000000000e+00  -5.306043550174e-03
- -2.557318610447e-01  5.306043550174e-03  0.000000000000e+00

## Veredito da execução

A cadeia reduzida produz a ordem correta e excelente acordo em `dm31`; `dm21` fica a poucos por cento.
A pendência física é derivar diretamente o autovalor superior `6*pi/5` e a primeira quebra `chi_nu^2/2` da Hessiana neutra oficial.
Até essa derivação, o resultado é candidato GDQ reduzido, não fechamento metrológico final.
