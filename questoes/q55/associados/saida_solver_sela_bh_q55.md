# Saída — Q55 solver de background regular efetivo

Classificação: teste de consistência numérica do pipeline covariante.
Não é previsão final nem solução completa da ação oficial.

## Parâmetros adimensionais

- M = `1`
- ell = `0.5`
- malha = `20000` pontos em [1e-05, 40]

## Horizontes

| índice | r_H | T_H |
|---:|---:|---:|
| 1 | 2.687007885126e-01 | 4.729466919877e-01 |
| 2 | 1.967716165985e+00 | 3.848312781534e-02 |

## Core

- Lambda_core analítico = `4.800000000000e+01`
- epsilon(0) numérico médio = `1.909859314891e+00`
- p_r(0) numérico médio = `-1.909859313454e+00`
- p_t(0) numérico médio = `-1.909884584961e+00`

## Invariantes no core numérico

| invariante | valor médio r<1e-3 | valor máximo na malha |
|---|---:|---:|
| R | 1.920012699177e+02 | 1.991945189807e+02 |
| Ricci2 | 9.216145380307e+03 | 9.932583042538e+03 |
| K | 6.144128219246e+03 | 6.656325014973e+03 |

Valores analíticos esperados no core de Sitter:

$$
R(0)=4\Lambda_{\rm core},\quad
R_{\mu\nu}R^{\mu\nu}(0)=4\Lambda_{\rm core}^2,\quad
K(0)=\frac83\Lambda_{\rm core}^2.
$$

## Condições de energia no core

- epsilon+p_r = `1.436221588523e-09`
- epsilon+p_t = `-2.527007029078e-05`
- epsilon+p_r+2p_t = `-3.819769168486e+00`

## Geodésicas — diagnóstico de potencial efetivo

- V_timelike_L0_core_min: `9.600970764041e-01`
- V_timelike_L0_core_max: `9.999999984000e-01`
- V_null_L2_core_min: `1.538357447478e+03`
- V_null_L2_core_max: `3.999999993600e+10`

## Estabilidade proxy exterior

- V0_min_exterior: `2.968723677475e-05`
- V0_max_exterior: `2.618797131684e-02`

## Assintótica

- m(r>20)/M médio = `9.999934315982e-01`
- A(r>20) médio = `9.278895797524e-01`

## Veredito

O pipeline confirma que uma fonte GDQ regular com $m(r)\sim r^3$ gera
horizontes, core finito, violação de SEC e temperatura finita/zero no
limite extremal. A sela exata ainda exige derivar o perfil $m(r)$ da
ação oficial.
