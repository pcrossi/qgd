# Saída — avaliação reduzida background/Hessiana Q51

Classificação: teste de consistência / avaliação reduzida.

Esta execução implementa os pontos 1 a 5 em versão reduzida GDQ. Não usa meia-vida experimental para construir os operadores. Ainda não é Hessiana completa da ação oficial.

Os fechamentos de camada usados por `closure` agora são gerados por `derivar_camadas_hessiana_reduzida_q51.py`, a partir do espectro angular reduzido com cisão spin--torção, e não por uma lista manual no script.

## Definições reduzidas usadas

Background de superfície:

$$
\Phi_N=(\sqrt{\chi_{curv}},\sqrt{s_{shell}},\sqrt{\delta_{touch}x_{barrier}})/\|\cdot\|.
$$

Hessiana de superfície:

$$
K_\partial^{phys}=K_{\partial\partial}-K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

Taxa:

$$
\Gamma_{GDQ}=\nu_{GDQ}\exp(-E_\partial^{GDQ})\exp(-W_{rad}^{GDQ}).
$$

## Comparação — variante `mismatch`

| Núcleo | log10 T_exp | log10 T_GDQ_red | resíduo | chi_curv | shell | lambda_alpha | peso P_perp | E_partial | nu_GDQ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| U-238 | 17.149217 | 17.224558 | 0.075341 | 0.011353 | 0.910855 | 0.329892 | 1.000000 | 0.329892 | 8.972890e+20 |
| U-234 | 12.889155 | 12.792212 | -0.096943 | 0.013318 | 0.873834 | 0.452902 | 1.000000 | 0.452902 | 1.005118e+21 |
| U-232 | 9.337323 | 9.298479 | -0.038844 | 0.015247 | 0.847868 | 0.592319 | 1.000000 | 0.592319 | 1.113476e+21 |
| Th-232 | 17.646780 | 17.708693 | 0.061913 | 0.011150 | 0.861425 | 0.318259 | 1.000000 | 0.318259 | 8.798254e+20 |
| Ra-226 | 10.703224 | 10.624607 | -0.078617 | 0.014272 | 0.759841 | 0.519591 | 1.000000 | 0.519591 | 1.039302e+21 |
| Po-212 | -6.524329 | -6.252298 | 0.272031 | 0.035076 | 0.000000 | 3.066213 | 1.000000 | 3.066213 | 2.346312e+21 |

- RMS contra experimento = `0.129485` décadas
- RMS de referência Gamow + nu_int = `0.303358` décadas
- melhoria relativa = `57.316%`

## Comparação — variante `closure`

| Núcleo | log10 T_exp | log10 T_GDQ_red | resíduo | chi_curv | shell | lambda_alpha | peso P_perp | E_partial | nu_GDQ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| U-238 | 17.149217 | 17.224558 | 0.075341 | 0.011353 | 0.089145 | 0.329892 | 1.000000 | 0.329892 | 8.972890e+20 |
| U-234 | 12.889155 | 12.792212 | -0.096943 | 0.013318 | 0.126166 | 0.452902 | 1.000000 | 0.452902 | 1.005118e+21 |
| U-232 | 9.337323 | 9.298479 | -0.038844 | 0.015247 | 0.152132 | 0.592319 | 1.000000 | 0.592319 | 1.113476e+21 |
| Th-232 | 17.646780 | 17.708693 | 0.061913 | 0.011150 | 0.138575 | 0.318259 | 1.000000 | 0.318259 | 8.798254e+20 |
| Ra-226 | 10.703224 | 10.624607 | -0.078617 | 0.014272 | 0.240159 | 0.519591 | 1.000000 | 0.519591 | 1.039302e+21 |
| Po-212 | -6.524329 | -6.252298 | 0.272031 | 0.035076 | 1.000000 | 3.066214 | 0.999999 | 3.066212 | 2.346312e+21 |

- RMS contra experimento = `0.129485` décadas
- RMS de referência Gamow + nu_int = `0.303358` décadas
- melhoria relativa = `57.316%`

## Comparação — variante `closure_mobility`

| Núcleo | log10 T_exp | log10 T_GDQ_red | resíduo | chi_curv | shell | lambda_alpha | peso P_perp | E_partial | nu_GDQ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| U-238 | 17.149217 | 17.224558 | 0.075341 | 0.011353 | 0.089145 | 0.329892 | 1.000000 | 0.329892 | 8.972890e+20 |
| U-234 | 12.889155 | 12.792212 | -0.096943 | 0.013318 | 0.126166 | 0.452902 | 1.000000 | 0.452902 | 1.005118e+21 |
| U-232 | 9.337323 | 9.298479 | -0.038844 | 0.015247 | 0.152132 | 0.592319 | 1.000000 | 0.592319 | 1.113476e+21 |
| Th-232 | 17.646780 | 17.708693 | 0.061913 | 0.011150 | 0.138575 | 0.318259 | 1.000000 | 0.318259 | 8.798254e+20 |
| Ra-226 | 10.703224 | 10.624607 | -0.078617 | 0.014272 | 0.240159 | 0.519591 | 1.000000 | 0.519591 | 1.039302e+21 |
| Po-212 | -6.524329 | -6.556893 | -0.032564 | 0.035076 | 1.000000 | 3.066214 | 0.999999 | 3.066212 | 4.731304e+21 |

- RMS contra experimento = `0.067894` décadas
- RMS de referência Gamow + nu_int = `0.303358` décadas
- melhoria relativa = `77.619%`

## Arquivos NPZ gerados

- `npz_backgrounds_reduzidos/U_238_mismatch.npz`
- `npz_backgrounds_reduzidos/U_234_mismatch.npz`
- `npz_backgrounds_reduzidos/U_232_mismatch.npz`
- `npz_backgrounds_reduzidos/Th_232_mismatch.npz`
- `npz_backgrounds_reduzidos/Ra_226_mismatch.npz`
- `npz_backgrounds_reduzidos/Po_212_mismatch.npz`
- `npz_backgrounds_reduzidos/U_238_closure.npz`
- `npz_backgrounds_reduzidos/U_234_closure.npz`
- `npz_backgrounds_reduzidos/U_232_closure.npz`
- `npz_backgrounds_reduzidos/Th_232_closure.npz`
- `npz_backgrounds_reduzidos/Ra_226_closure.npz`
- `npz_backgrounds_reduzidos/Po_212_closure.npz`
- `npz_backgrounds_reduzidos/U_238_closure_mobility.npz`
- `npz_backgrounds_reduzidos/U_234_closure_mobility.npz`
- `npz_backgrounds_reduzidos/U_232_closure_mobility.npz`
- `npz_backgrounds_reduzidos/Th_232_closure_mobility.npz`
- `npz_backgrounds_reduzidos/Ra_226_closure_mobility.npz`
- `npz_backgrounds_reduzidos/Po_212_closure_mobility.npz`

## Veredito

A melhor variante reduzida foi `closure_mobility`, com RMS `0.067894` décadas e melhoria `77.619%` contra Gamow com `nu_int`.

A variante `mismatch` fica preservada como rota falha: ela atribui rigidez pequena ao fechamento Pb-208 de Po-212 e por isso erra fisicamente o canal.

A variante `closure` corrige esse sinal físico ao aumentar a rigidez quando o filho está próximo de camada fechada. A variante `closure_mobility` adiciona a regra de mobilidade de determinante para filho exatamente duplamente fechado. Mesmo quando melhora o RMS, continua sendo uma redução espectral angular, não a Hessiana completa derivada da ação oficial.
O ponto técnico restante é calcular os blocos reais da Hessiana nuclear da ação oficial, em vez de usar a matriz reduzida acima.
