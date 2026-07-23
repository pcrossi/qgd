# Saída — aproximação espectral de R_partial Q51

Classificação: teste de consistência, não previsão final.

Base herdada da Q40:

$$
\mathcal I_\Sigma(x)=
j_0^2\frac{x^2}{1+x}
+j_1^2\frac{x^2}{(1+x)^2}
+j_2^2\frac{x^3}{(1+x)^2}
$$

com:

$$
j_0=1.712091781054,\quad j_1=1.341454657186,\quad j_2=1.063840998206.
$$

Variável de canal alfa testada:

$$
\chi_{\rm curv}=\frac{\delta_{\rm touch}^2}{x_{\rm barrier}}.
$$

Escala geométrica testada:

$$
E_{\partial}^{\rm spec}=\frac{4}{\alpha}\mathcal I_\Sigma(\chi_{\rm curv}).
$$

O fator 4 representa os quatro nucleons do cluster alfa; 1/alpha representa a complacência eletrogeométrica global. Esta é uma hipótese reduzida de escala, não fechamento.

| Núcleo | E_req | chi_curv | E_spec | Diferença |
| --- | ---: | ---: | ---: | ---: |
| U-238 | 0.000000 | 0.011353 | 0.329982 | 0.329982 |
| U-234 | 0.425065 | 0.013318 | 0.453031 | 0.027966 |
| U-232 | 0.373825 | 0.015247 | 0.592495 | 0.218671 |
| Th-232 | 0.000000 | 0.011150 | 0.318344 | 0.318344 |
| Ra-226 | 0.422411 | 0.014272 | 0.519740 | 0.097329 |
| Po-212 | 1.557848 | 0.035076 | 3.067555 | 1.509707 |

- RMS total = `0.651603`
- RMS nos casos positivos = `0.764409`

## Veredito

A base espectral herdada da Q40 acerta a escala de alguns actinídeos, mas falha como previsão universal: gera energia positiva onde o diagnóstico pede quase zero e superestima Po-212.

Conclusão: é necessário o projetor físico de canal `P_perp` e o espectro real de camada/superfície. A impedância média não basta.
