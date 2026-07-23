# Saída — teste de modelos escalares de superfície Q51

Classificação: engenharia inversa diagnóstica, não previsão.

Objetivo: verificar se a energia de superfície requerida poderia ser representada por poucos escalares geométricos simples. Se isso falhar ou depender de indicador de camada, o operador Schur/DtN completo é necessário.

| Núcleo | E_req | delta_touch | x_barrier | chi_curv=delta^2/x | Z^2/A | magic208 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| U-238 | 0.000000 | 0.250516 | 5.527682 | 0.011353 | 35.563025 | 0 |
| U-234 | 0.425065 | 0.251871 | 4.763516 | 0.013318 | 36.170940 | 0 |
| U-232 | 0.373825 | 0.252559 | 4.183590 | 0.015247 | 36.482759 | 0 |
| Th-232 | 0.000000 | 0.252559 | 5.720625 | 0.011150 | 34.913793 | 0 |
| Ra-226 | 0.422411 | 0.254671 | 4.544320 | 0.014272 | 34.265487 | 0 |
| Po-212 | 1.557848 | 0.259891 | 1.925627 | 0.035076 | 33.283019 | 1 |

| Modelo diagnóstico | RMS em E_req | Coeficientes |
| --- | ---: | --- |
| constante | 0.522569 | `0.463192` |
| curvatura | 0.111625 | `-0.562273, 61.2729` |
| curvatura+fissilidade | 0.109294 | `-1.61357, 63.9196, 0.0286787` |
| curvatura+magic | 0.083584 | `-1.20615, 110.989, -1.12906` |
| curvatura+fissilidade+magic | 0.082836 | `-0.677691, 113.233, -0.0157215, -1.21298` |

## Veredito

Modelos escalares globais são diagnósticos, não derivação. A presença do indicador `magic208` melhora a descrição apenas porque codifica informação estrutural de camada. Na GDQ essa informação não deve ser inserida como etiqueta; ela deve emergir do espectro de `R_partial^GDQ`.

Portanto, a rota correta permanece calcular o operador de superfície e seu projetor físico, não ajustar escalares.
