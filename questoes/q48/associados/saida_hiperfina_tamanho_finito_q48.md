# Saída — hiperfina e tamanho finito Q48

## Hiperfina 1s

Classificação: comparação fenomenológica se `mu_p` é experimental.

- mu_p/mu_B = 1.521032202312504e-03
- nu_F(1s) = 1418840090.665555 Hz
- referência 21 cm = 1420405751.768000 Hz
- diferença = -1565661.102445 Hz
- erro relativo = -1.102263e-03

## Correções adicionadas

### 1. Canal magnético líder da GDQ/Q43

- a_e^GDQ,(1) = alpha/(2*pi) = 1.161409732092663e-03
- nu_F * (1 + a_e) = 1420487945.355137 Hz
- diferença após a_e = 82193.587137 Hz
- erro relativo após a_e = 5.786627e-05

### 2. Resposta coletiva de superfície Q40 avaliada na escala atômica

- q_atom ~ 1/a_B* = 1.888697509086102e-05 fm^-1
- x = q_atom^2/Lambda_E^2 = 2.101391825244532e-11
- I_sigma(x) = -2.089031019060285e-21
- nu_F * (1 + a_e) * (1 + I_sigma) = 1420487945.355137 Hz
- diferença após superfície reduzida = 82193.587137 Hz
- erro relativo após superfície reduzida = 5.786627e-05

A correção de superfície coletiva da Q40 começa em q^4. Na escala atômica
ela é praticamente nula. Portanto ela não deve ser usada para absorver o
resíduo hiperfino. O resíduo remanescente exige os canais de recuo,
Zemach/magnetização distribuída e termos superiores da Hessiana magnética.

### 3. Zemach geométrico de casca superficial GDQ

Modelo reduzido: distribuição elétrica e magnética como cascas finas na
superfície protônica. Para duas cascas esféricas idênticas, o raio de
Zemach é a corda média na esfera: r_Z = 4 r_p / 3.

- r_Z^shell = 4 r_p/3 = 1.121038353933 fm
- delta_Z = -2 alpha (mu c/hbar) r_Z = -4.234604693327742e-05
- nu_F * (1 + a_e) * (1 + delta_Z) = 1420427793.305934 Hz
- diferença após a_e + Zemach = 22041.537935 Hz
- erro relativo após a_e + Zemach = 1.551778e-05

### 4. Combinação reduzida adicionada

- nu_F * (1 + a_e) * (1 + I_sigma + delta_Z) = 1420427793.305934 Hz
- diferença após efeitos reduzidos = 22041.537935 Hz
- erro relativo após efeitos reduzidos = 1.551778e-05
- fração residual a ser explicada por recuo/Hessiana magnética superior = -1.551753495565578e-05

## Tamanho finito

| r_p (fm) | Delta E_fs H 2s (eV) | Delta E_fs muH 2s (meV) | amplificação mu/e |
|---:|---:|---:|---:|
| 0.840778765450 | 5.715065938837e-10 | 3.674126161 | 6.428843e+06 |
| 0.875000000000 | 6.189761026743e-10 | 3.979300180 | 6.428843e+06 |
| 0.835400000000 | 5.642177152782e-10 | 3.627267105 | 6.428843e+06 |

O deslocamento cresce como mu^3. Por isso o hidrogênio muônico é muito
mais sensível ao raio/fator de forma do próton.
