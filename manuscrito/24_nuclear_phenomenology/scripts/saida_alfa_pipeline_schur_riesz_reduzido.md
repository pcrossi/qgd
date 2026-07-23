# Saída — pipeline alfa Schur--Riesz reduzido

Classificação: prova de conceito GDQ reduzida / teste de consistência.

## Cadeia executada

`dados do canal -> K_II,K_Ib,K_bb -> Schur -> Riesz -> E_partial -> nu_GDQ -> T_1/2`.

## Tabela comparativa

| Canal | log10 T_ref | log10 T_GDQ_red | resíduo | chi_curv | shell | lambda_alpha | peso P_perp | E_partial | fechamentos filho |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| U-238 | 17.149217 | 17.224558 | +0.075341 | 0.011353 | 0.089145 | 0.329892 | 1.000000 | 0.329892 | 0 |
| U-234 | 12.889155 | 12.792212 | -0.096943 | 0.013318 | 0.126166 | 0.452902 | 1.000000 | 0.452902 | 0 |
| U-232 | 9.337323 | 9.298479 | -0.038844 | 0.015247 | 0.152132 | 0.592319 | 1.000000 | 0.592319 | 0 |
| Th-232 | 17.646780 | 17.708693 | +0.061913 | 0.011150 | 0.138575 | 0.318259 | 1.000000 | 0.318259 | 0 |
| Ra-226 | 10.703224 | 10.624607 | -0.078617 | 0.014272 | 0.240159 | 0.519591 | 1.000000 | 0.519591 | 0 |
| Po-212 | -6.524329 | -6.556893 | -0.032564 | 0.035076 | 1.000000 | 3.066214 | 0.999999 | 3.066212 | 2 |

## Métricas

- RMS GDQ reduzido: `0.067894` décadas
- RMS Gamow com frequência interna reduzida: `0.303358` décadas
- Melhoria relativa: `77.619%`

## Interpretação

A melhoria aparece quando o alfa é tratado como canal de contorno com impedância Schur--Riesz e quando o filho duplamente fechado recebe mobilidade de determinante. O cálculo permanece reduzido: a etapa metrológica final é substituir as matrizes acima pela Hessiana nuclear completa da ação oficial.
