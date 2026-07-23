# Saída — diagnóstico do overlap de superfície Q51

Classificação: diagnóstico inverso de escala, não previsão.

Usa Gamow com `nu_int` como base radial e calcula o termo de superfície que falta para coincidir com o dado experimental.

Definições:

$$
W_{\rm req}=\ln\left(T_{1/2}^{\rm exp}\nu_{\rm int}/\ln2\right)
$$

$$
\Delta W_{\rm req}=W_{\rm req}-W_{\rm Gamow}
$$

$$
S_\alpha^{\rm eff}=e^{-\Delta W_{\rm req}}
$$

$$
E_{\partial}^{\rm req}=\max(\Delta W_{\rm req},0)
$$

| Núcleo | Delta W_req | S_alpha_eff | E_surface_req | Classificação |
| --- | ---: | ---: | ---: | --- |
| U-238 | -0.039094 | 1.039868 | 0.000000 | radial já lento; refinar raio/frequência/dados |
| U-234 | 0.425065 | 0.653727 | 0.425065 | overlap/preformação reduz taxa |
| U-232 | 0.373825 | 0.688097 | 0.373825 | overlap/preformação reduz taxa |
| Th-232 | -0.014190 | 1.014291 | 0.000000 | radial já lento; refinar raio/frequência/dados |
| Ra-226 | 0.422411 | 0.655465 | 0.422411 | overlap/preformação reduz taxa |
| Po-212 | 1.557848 | 0.210589 | 1.557848 | overlap/preformação reduz taxa |

Resumo dos casos com correção positiva:

- média de `E_surface_req` = `0.694787`
- RMS de `E_surface_req` = `0.855241`

Interpretação GDQ:

O termo a derivar é uma energia quadrática de superfície, não uma constante universal de barreira:

$$
E_{\partial}^{\rm GDQ}[\alpha]
=
\langle P_\perp\Phi_{4N},\mathsf R_{\partial}^{\rm GDQ}P_\perp\Phi_{4N}\rangle_{\partial}
$$

com:

$$
\mathsf R_{\partial}^{\rm GDQ}=K_{\partial\partial}-K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

O próximo passo preditivo é calcular esse operador de superfície no background nuclear, em vez de usar `E_surface_req` como entrada.
