# Saída — validação Q50 beta livre GDQ

Comando:

```bash
python3 questoes/q50/associados/validar_beta_livre_q50.py
```

Saída:

```text
# Saída — validação Q50 beta livre GDQ

m_e = 0.51099895069 MeV
DeltaM = 1.29333251 MeV
Q_beta endpoint = 0.782333559310 MeV
Observação: Q_beta é energia disponível máxima, não energia fixa do antineutrino.

I_beta analítico = 5.700456936530352e-17 GeV^5
I_beta Simpson = 5.700456308550165e-17, 5.700456714505864e-17, 5.700456858032888e-17 GeV^5
espalhamento de malha = 5.495e-24 GeV^5
erro relativo Simpson fino = 1.377e-08

alpha^-1 = 137.035999177000
2|C_S|^2+6|C_T|^2 = 8.142351666635048e-10 GeV^-4
sqrt(2|C_S|^2+6|C_T|^2) = 2.853480623139931e-05 GeV^-2
Gamma = 1.137140542406870e-03 s^-1
vida média tau_n = 879.398775004012 s
meia-vida T_1/2 = 609.552781481901 s

| E_e (MeV) | E_nu recoil-zero (MeV) | forma espectral normalizada |
|---:|---:|---:|
| 0.510998950690 | 0.782333559310 | 0.000000000000 |
| 0.706582340518 | 0.586750169482 | 1.000000000000 |
| 0.902165730345 | 0.391166779655 | 0.864576508054 |
| 1.097749120172 | 0.195583389828 | 0.343679377483 |
| 1.293332510000 | 0.000000000000 | 0.000000000000 |
```

Classificação:

- integral analítica: avaliação direta;
- Simpson em três malhas: teste independente de consistência;
- vida média: avaliação do fechamento GDQ contraído \(\alpha^{-11}\);
- espectro tabulado: forma mínima sem recoil/correções diferenciais.
