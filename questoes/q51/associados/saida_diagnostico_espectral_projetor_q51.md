# Saída — diagnóstico espectral do projetor Q51

Classificação: diagnóstico matemático, não previsão.

Partimos de:

$$
p_{\rm req}=E_{\partial}^{\rm req}/E_{\partial}^{\rm spec}.
$$

Se $p_{\rm req}$ é norma quadrática de projeção, então:

$$
\sqrt{p_{\rm req}}=\cos\theta_\alpha.
$$

Num modelo de janela espectral Lorentziana:

$$
p_{\rm req}=\frac{1}{1+(\Delta/\Gamma)^2}.
$$

| Núcleo | p_req | theta_alpha (graus) | Delta/Gamma |
| --- | ---: | ---: | ---: |
| U-238 | 0.000000 | 90.000000 | inf |
| U-234 | 0.938269 | 14.386179 | 0.256499 |
| U-232 | 0.630933 | 37.409591 | 0.764823 |
| Th-232 | 0.000000 | 90.000000 | inf |
| Ra-226 | 0.812735 | 25.641668 | 0.480014 |
| Po-212 | 0.507847 | 44.550389 | 0.984428 |

## Interpretação

Casos com $p\simeq0$ exigem que o modo $4N$ esteja quase ortogonal à janela alfa selecionada. Casos com $p\simeq1$ exigem alinhamento quase completo. Valores intermediários correspondem a mistura espectral parcial.

Isso define o que o operador $K_\partial^{\rm phys}$ precisa produzir: separações espectrais distintas por núcleo, não uma constante universal.
