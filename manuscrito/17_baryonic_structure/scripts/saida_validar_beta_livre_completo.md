# Saída — validação beta livre GDQ

Classificação: avaliação direta, teste de convergência e comparação fenomenológica.

## Parâmetros

- `m_e = 0.51099895069 MeV`
- `DeltaM = 1.29333251 MeV`
- `Q_beta endpoint = 0.782333559310 MeV`
- `Q_beta` é energia disponível máxima, não energia fixa do antineutrino.

## Espaço de fase

- `I_beta analítico = 5.700456936530352e-17 GeV^5`
- `I_beta Simpson = 5.700456308550165e-17, 5.700456714505864e-17, 5.700456858032888e-17 GeV^5`
- `espalhamento de malha = 5.495e-24 GeV^5`
- `erro relativo Simpson fino = 1.377e-08`

## Taxa total

- `alpha^-1 = 137.035999177000`
- `2|C_S|^2+6|C_T|^2 = 8.142351666635048e-10 GeV^-4`
- `sqrt(2|C_S|^2+6|C_T|^2) = 2.853480623139931e-05 GeV^-2`
- `Gamma = 1.137140542406870e-03 s^-1`
- `tau_n = 879.398775004012 s`
- `T_1/2 = 609.552781481901 s`

## Comparação

| referência | tau_ref s | diferença s | diferença relativa | sigma simples |
|---|---:|---:|---:|---:|
| PDG 2024 | 878.400000000000 | 0.998775004012 | 1.137038938994e-03 | 1.997550 |

## Forma espectral reduzida

| E_e MeV | E_antineutrino recoil-zero MeV | forma espectral normalizada |
|---:|---:|---:|
| 0.510998950690 | 0.782333559310 | 0.000000000000 |
| 0.706582340518 | 0.586750169482 | 1.000000000000 |
| 0.902165730345 | 0.391166779655 | 0.864576508054 |
| 1.097749120172 | 0.195583389828 | 0.343679377483 |
| 1.293332510000 | 0.000000000000 | 0.000000000000 |

Interpretação: a cinemática e o espaço de fase são calculados diretamente;
a normalização absoluta da taxa avalia o ansatz histórico alpha^-11.
Forma diferencial fina, recoil, superfície e correlações angulares exigem
a quarta variação física no background 8D.
