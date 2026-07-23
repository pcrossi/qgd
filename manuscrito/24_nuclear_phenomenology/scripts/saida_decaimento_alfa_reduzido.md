# Saída — decaimento alfa reduzido

Classificação: prova de conceito GDQ reduzida.

## Comparação em log10(T_1/2)

| Canal | log10(T_ref) | log10(T_GDQ_red) | resíduo |
|---|---:|---:|---:|
| U-238 | 17.149217 | 17.224558 | +0.075341 |
| U-234 | 12.889155 | 12.792212 | -0.096943 |
| U-232 | 9.337323 | 9.298479 | -0.038844 |
| Th-232 | 17.646780 | 17.708693 | +0.061913 |
| Ra-226 | 10.703224 | 10.624607 | -0.078617 |
| Po-212 | -6.524329 | -6.556893 | -0.032564 |

## Métricas

- RMS GDQ reduzido: `0.067894` décadas
- RMS Gamow com frequência interna reduzida: `0.303358` décadas
- Melhoria relativa: `77.619%`

## Interpretação

O resultado preserva a cadeia reduzida final: complemento de Schur, projetor de Riesz do canal alfa, rigidez de camada por spin--torção e mobilidade de determinante para filho duplamente fechado. O status não é previsão metrológica final porque os blocos reais da Hessiana nuclear completa ainda devem substituir os blocos reduzidos.
