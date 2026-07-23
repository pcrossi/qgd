# Saída — Q55 reconstrução covariante efetiva da sela reduzida

Classificação: teste de consistência / reconstrução efetiva.

Não é solução covariante completa da ação oficial.

## Parâmetros

- eta = `8.0`
- lambda_T = `3.0`
- r_min = `0.0001`
- r_max = `25.0`
- solve_bvp success = `True`
- mu radial = `-1.067957044153e-01`

## Regularidade central

- potência de massa no core = `3.00002651`
- epsilon_core = `9.934478711421e-03`
- p_r_core = `-9.934478711373e-03`
- p_t_core = `-9.934159730822e-03`
- epsilon+p_r = `4.750637265869e-14`
- epsilon+p_t = `3.189805987093e-07`
- SEC combo epsilon+p_r+2p_t = `-1.986831946160e-02`

## Horizontes

- r_H[1] = `4.222352820613e+00`
- r_H[2] = `1.595712272799e+01`

## Invariantes no core

- R_core = `9.987066970693e-01`
- Ricci2_core = `2.493537672591e-01`
- Kretschmann_core = `1.662358472304e-01`

## Conservação efetiva

- RMS do resíduo de conservação anisotrópica no core = `3.283523548786e-10`
- RMS do resíduo em patches estáticos `|A|>5e-2` = `4.232372694767e-10`

## Assintótica

- massa exterior média = `7.999770182907e+00`
- A exterior médio = `2.859734791970e-01`

## Veredito

A sela radial reduzida, quando compactificada acima de eta_crit, gera métrica efetiva com horizontes e core regular.

A leitura de pressões por Einstein efetivo é legítima apenas como camada macroscópica Q54. O fechamento total exige obter Phi(r), epsilon(r), p_r(r) e p_t(r) por variação direta da ação GDQ reduzida.