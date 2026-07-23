# Saída — protótipo matricial de K_partial Q51

Classificação: fixture matemático, não previsão.

Base: $e_0$ modo nu $4N$, $e_1$ modo do núcleo filho, $e_2$ modo coletivo residual.

Autovetor alfa realizado:

$$
v_\alpha=\sqrt p\,e_0+\sqrt{1-p}\,e_1.
$$

Então:

$$
\|P_\alpha e_0\|^2=p.
$$

| Núcleo | p_req | p_model | autovalores K | autovetor alfa |
| --- | ---: | ---: | --- | ---: |
| U-238 | 0.000000 | 0.000000 | `0.000, 1.000, 3.000` | `0.000, 1.000, 0.000` |
| U-234 | 0.938269 | 0.938269 | `-0.000, 1.000, 3.000` | `-0.969, -0.248, -0.000` |
| U-232 | 0.630933 | 0.630933 | `0.000, 1.000, 3.000` | `-0.794, -0.608, -0.000` |
| Th-232 | 0.000000 | 0.000000 | `0.000, 1.000, 3.000` | `0.000, 1.000, 0.000` |
| Ra-226 | 0.812735 | 0.812735 | `0.000, 1.000, 3.000` | `-0.902, -0.433, -0.000` |
| Po-212 | 0.507847 | 0.507847 | `-0.000, 1.000, 3.000` | `-0.713, -0.702, -0.000` |

## Veredito

O protótipo mostra que pesos nulos, quase unitários e intermediários são exatamente normas quadráticas de projetores espectrais. Isso valida o mecanismo matemático, mas a matriz acima é construída a partir dos pesos requeridos; portanto é fixture, não previsão.

O próximo passo físico é substituir essa matriz por blocos calculados da Hessiana de superfície do background nuclear.
