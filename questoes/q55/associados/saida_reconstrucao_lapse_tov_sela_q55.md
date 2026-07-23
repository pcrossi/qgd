# Saída — Q55 reconstrução de lapse por TOV efetiva

Classificação: teste de consistência / reconstrução efetiva.

Não é sela covariante completa da ação oficial.

## Parâmetros

- eta = `8.0`
- lambda_T = `3.0`
- solve_bvp success = `True`
- mu radial = `-1.067957044153e-01`
- corte de horizonte `|A|>` = `0.05`

## Horizontes

- r_H[1] = `4.222352820613e+00`
- r_H[2] = `1.595712272799e+01`

## Core

- potência de massa = `3.00002651`
- epsilon_core = `9.934478711421e-03`
- p_r_core input = `-9.934477941512e-03`
- p_r_core métrico = `-9.934477941464e-03`
- p_t_core TOV = `-9.934158191133e-03`
- epsilon+p_r = `7.699092230041e-10`
- epsilon+p_t = `3.205202875438e-07`
- SEC combo = `-1.986831561236e-02`
- R_trace_core = `9.987066003286e-01`

## Lapse

- Phi_core médio = `-6.772283588559e-03`
- Phi exterior médio = `7.482240388239e-07`
- max |Phi| em patches estáticos = `9.292752476883e-03`

## Conservação

- RMS core = `2.104757829586e-16`
- RMS patches estáticos = `9.997320016076e-18`
- max |p_r métrico - p_r input| core = `2.506468990693e-12`

## Veredito

A reconstrução por TOV mostra que, dado o perfil radial reduzido e uma equação de estado GDQ efetiva de core, o lapse pode ser reconstruído por conservação. A identidade de conservação fecha numericamente por construção e a regularidade central é preservada.

A limitação permanece: a equação de estado radial e a compactness ainda precisam ser derivadas da Hessiana oficial, não escolhidas como camada efetiva.