# Saída — teste de proxy de camada Q51

Classificação: teste diagnóstico, não previsão.

Distância a números mágicos do núcleo filho:

$$
D_{\rm shell}=d_Z^2+d_N^2.
$$

| Núcleo | A_f | Z_f | N_f | dZ | dN | D_shell | p_req |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| U-238 | 234 | 90 | 144 | 8 | 18 | 388 | 0.000000 |
| U-234 | 230 | 90 | 140 | 8 | 14 | 260 | 0.938269 |
| U-232 | 228 | 90 | 138 | 8 | 12 | 208 | 0.630933 |
| Th-232 | 228 | 88 | 140 | 6 | 14 | 232 | 0.000000 |
| Ra-226 | 222 | 86 | 136 | 4 | 10 | 116 | 0.812735 |
| Po-212 | 208 | 82 | 126 | 0 | 0 | 0 | 0.507847 |

| Proxy ajustado | RMS em p_req | c ótimo |
| --- | ---: | ---: |
| D/(D+c) | 0.469018 | 257.562230 |
| c/(D+c) | 0.382452 | 206.187747 |
| lorentz_open | 0.367070 | 217.804884 |
| lorentz_closed | 0.516223 | 260.905537 |

## Veredito

A distância a números mágicos do núcleo filho não explica sozinha o peso de projeção. Em particular, U-238 e Th-232 têm distâncias de camada grandes mas p_req próximo de zero, enquanto Po-212 tem filha duplamente mágica e p_req intermediário.

Conclusão: o projetor não pode ser reduzido a uma função escalar de números mágicos. É necessário o espectro real de K_partial^phys e o overlap com o subespaço do filho.
