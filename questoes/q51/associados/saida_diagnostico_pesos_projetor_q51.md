# Saída — pesos requeridos do projetor Q51

Classificação: diagnóstico inverso, não previsão.

Define:

$$
p_{\rm req}=E_{\partial}^{\rm req}/E_{\partial}^{\rm spec}.
$$

| Núcleo | E_req | E_spec | p_req | sqrt(p_req) | Status |
| --- | ---: | ---: | ---: | ---: | --- |
| U-238 | 0.000000 | 0.329982 | 0.000000 | 0.000000 | compatível com projetor |
| U-234 | 0.425065 | 0.453031 | 0.938269 | 0.968643 | compatível com projetor |
| U-232 | 0.373825 | 0.592495 | 0.630933 | 0.794313 | compatível com projetor |
| Th-232 | 0.000000 | 0.318344 | 0.000000 | 0.000000 | compatível com projetor |
| Ra-226 | 0.422411 | 0.519740 | 0.812735 | 0.901518 | compatível com projetor |
| Po-212 | 1.557848 | 3.067555 | 0.507847 | 0.712634 | compatível com projetor |

Verificação global:

$$
0\le p_{\rm req}\le1\quad\text{para todos} = true.
$$

Interpretação: a impedância média pode ser mantida; o que falta é o projetor espectral de canal que preserva apenas a componente alfa admissível.
