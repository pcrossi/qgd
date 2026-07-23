# Saída — benchmark reduzido Q51
Classificação: teste de consistência/comparação fenomenológica.
A frequência interna reduzida ainda não é a frequência final da Hessiana; é a primeira substituição não ajustável de `nu0`.
- alpha = `7.297352569283802e-03`
- nu0 efetivo legado = `1.000000e+21 s^-1`
- frequência interna usada: `nu_int = c sqrt(2 Q_alpha/mu)/(2 R_N)`
| Núcleo | Q_alpha (MeV) | log10 T_exp | Gamow nu0 | GDQexp nu0 | Gamow nu_int | GDQexp nu_int | nu_int (s^-1) | Delta W_req | S_alpha_eff |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| U-238 | 4.26975 | 17.149217 | 17.057220 | 17.054243 | 17.166196 | 17.163219 | 7.780799e+20 | -0.039094 | 1.039868 |
| U-234 | 4.85800 | 12.889155 | 12.625651 | 12.623194 | 12.704552 | 12.702095 | 8.338709e+20 | 0.425065 | 0.653727 |
| U-232 | 5.41400 | 9.337323 | 9.120639 | 9.118562 | 9.174973 | 9.172896 | 8.824002e+20 | 0.373825 | 0.688097 |
| Th-232 | 4.08300 | 17.646780 | 17.537339 | 17.534277 | 17.652943 | 17.649881 | 7.662953e+20 | -0.014190 | 1.014291 |
| Ra-226 | 4.87100 | 10.703224 | 10.445651 | 10.443402 | 10.519773 | 10.517523 | 8.430985e+20 | 0.422411 | 0.655465 |
| Po-212 | 8.95400 | -6.524329 | -7.135103 | -7.135801 | -7.200894 | -7.201592 | 1.163565e+21 | 1.557848 | 0.210589 |

| Modelo | RMS décadas | Melhoria contra Gamow nu0 |
| --- | ---: | ---: |
| Gamow_nu0 | 0.309897 | 0.000% |
| GDQexp_nu0 | 0.311361 | -0.473% |
| Gamow_nu_int | 0.303358 | 2.110% |
| GDQexp_nu_int | 0.304249 | 1.823% |

## Veredito numérico

A troca de `nu0` constante por `nu_int` melhora levemente a série, sem usar alvo experimental núcleo por núcleo.

A métrica exponencial legada com expoente `alpha^2 V/Q` continua não produzindo melhora estatística. Portanto, o próximo avanço real deve vir da impedância Schur/DtN alfa--núcleo e não apenas do ansatz exponencial.

## Diagnóstico do termo faltante

`Delta W_req` é a correção de ação necessária para que Gamow com `nu_int` coincida com a meia-vida experimental. Ela não foi usada como ajuste; serve apenas para dimensionar o canal Schur/DtN ausente.

O padrão não é uma constante universal: U-238 e Th-232 já exigem correções muito pequenas, enquanto Po-212 exige correção maior. Isso indica dependência de estrutura nuclear/deformação/canal de contorno.

`S_alpha_eff=exp(-Delta W_req)` é a leitura de overlap/preformação efetiva que a Hessiana de superfície deve substituir por uma previsão direta. Valores maiores que 1 indicam que a frequência, o raio ou o dataset diagnóstico ainda precisam refinamento; não devem ser interpretados literalmente como probabilidade.
