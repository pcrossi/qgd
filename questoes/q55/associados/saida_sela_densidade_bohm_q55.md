# Saída — Q55 sela reduzida densidade/Bohm/torção

Classificação: teste de consistência de uma redução efetiva radial da GDQ.

Não é a sela covariante completa da ação oficial.

## Configuração

- r_min = `0.0001`
- r_max = `25.0`
- n_mesh inicial = `900`
- lambda_T = `3.0`
- compactness eta = `1.0`
- solve_bvp success = `True`
- solve_bvp status = `0`
- mensagem = `The algorithm converged to the desired accuracy.`
- mu = `-1.067957044153e-01`
- nós finais = `2068`

## Regularidade do core

- rho(0) aproximado = `1.560554371867e-02`
- epsilon_core médio = `1.241810996804e-03`
- potência ajustada de M(r) no core = `2.99999076`

O valor esperado para core regular é `M(r) ~ r^3`.

## Horizontes efetivos

- nenhum horizonte para a compactness escolhida

## Varredura de compactness


- eta_crit aproximado = `5.188522012681e+00`

| eta | min A | número de horizontes | horizontes |
|---:|---:|---:|---|
| 0.5 | 9.036334e-01 | 0 | — |
| 1 | 8.072669e-01 | 0 | — |
| 2 | 6.145338e-01 | 0 | — |
| 3 | 4.218007e-01 | 0 | — |
| 5 | 3.633443e-02 | 0 | — |
| 8 | -5.418649e-01 | 2 | 4.222353e+00, 1.595712e+01 |
| 13 | -1.505530e+00 | 1 | 3.013818e+00 |
| 21 | -3.047395e+00 | 1 | 2.269252e+00 |
| 34 | -5.552926e+00 | 1 | 1.741033e+00 |

## Invariantes efetivos no core

- R_core médio = `1.244318737081e-01`
- Ricci2_core médio = `3.875131043925e-03`
- Kretschmann_core médio = `2.591474380081e-03`

## Estabilidade proxy

- V_proxy_min exterior = `4.081637846228e-02`

## Veredito

A redução radial produz uma densidade estacionária regular com `M(r) ~ r^3`, portanto confirma dinamicamente o requisito mínimo do core regular sem escolher o perfil de massa à mão.

O fechamento total da Q55 continua exigindo a sela covariante completa `X_*=(g_*,f_*,H_*)` e a Hessiana física `K_BH^phys`.