# Saída — pipeline reduzido de buraco negro GDQ

Classificação: avaliação reduzida / diagnóstico espectral e de acoplamentos.

## 1. Parâmetros e status

- lambda_T = `3.000000`
- eta = `8.000000`
- eta_crit = `5.188522012681e+00`
- mu = `-1.067957044153e-01`
- expoente central de massa = `3.00002651`
- status: redução efetiva testada; covariante 8D completo permanece futuro.

## 2. Core e condições de energia

- epsilon_core = `9.934478711421e-03`
- p_r_core = `-9.934477941512e-03`
- p_t_core = `-9.934158191133e-03`
- epsilon+p_r = `7.699090011359e-10`
- epsilon+p_t = `3.205202880000e-07`
- epsilon+p_r+2p_t = `-1.986831561236e-02`
- max |p_r_metric - p_r_input| core = `2.506468990693e-12`
- RMS conservação core = `2.104757829586e-16`
- RMS conservação patches estáticos = `9.997320016076e-18`

Interpretação: NEC/WEC são saturadas no core e SEC é violada.

## 3. Invariantes de curvatura finitos

- R_core = `9.987066970693e-01`
- Ricci2_core = `2.493537672591e-01`
- Kretschmann_core = `1.662358472304e-01`

## 4. Horizontes e temperaturas

| horizonte | r_H | kappa_H | T_H=kappa_H/(2pi) |
|---:|---:|---:|---:|
| 1 | 4.222352820613e+00 | 1.465301433319e-01 | 2.332099662324e-02 |
| 2 | 1.595712272799e+01 | 3.044070699662e-02 | 4.844788989724e-03 |

## 5. Virial e modo coletivo

- K = `3.167552271297e-01`
- U_T = `9.808336775055e-02`
- W = `-9.274781821674e-01`
- 2K+3U_T+W = `2.823753435869e-04`
- resíduo relativo = `1.522043161064e-04`
- d2E/da2 em a=1 = `1.193971365853e+00`

## 6. Projetor radial e Hessiana reduzida

- lambda_raw[1] = `-1.927437459951e-01`
- lambda_phys[1] após projeção = `-5.982003087324e-13`
- lambda_phys[2] = `3.651456961676e-02`

| setor | menor modo físico reduzido |
|---|---:|
| amplitude radial projetada | 3.651456961676e-02 |
| amplitude escalar nao homogenea | 1.909625790263e-03 |
| fase/circulacao nao-zero | 6.572554660398e-02 |
| torcao reduzida | 1.475541776890e-01 |
| metrico axial exterior | 1.493545907614e-01 |

## 7. Acoplamentos cruzados por Schur

- ||K_gf|| reduzido = `6.166879064740e-04`
- ||K_gH|| reduzido = `8.076881453156e-06`
- chi_gf = `1.333410946325e-03`
- chi_gH = `2.960174621482e-09`

Interpretação: os acoplamentos reduzidos são pequenos e não fecham os gaps diagonais.

## 8. Page toy

- pesos = `[0.9999980969946938, 1.90300515759935e-06, 8.794135715905771e-14, 6.064588145332285e-14]`
- entropia dos pesos = `2.696953704284e-05`
- classificação: toy unitário, não Page curve física covariante.

## Veredito

A redução efetiva mostra core regular, horizontes, conservação efetiva, gaps positivos e Schur controlado.
O fechamento covariante 8D completo exige setor métrico polar, coordenadas atravessantes de horizonte, matriz acoplada 8D e Page curve física.
