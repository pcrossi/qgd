---
title: "Saída — Hessiana material EO-MZI"
---

# Saída — Hessiana material reduzida EO-MZI

Classificação: modelo material reduzido de engenharia.

## Dados congelados

- lambda = `1.550000e-06 m`
- Vpi = `2.445000 V`
- tau_sw = `1.810000e-11 s`
- alvo de referência para comparação: `-30.0 dB`

## Transferência ideal

- fase em Vpi: `3.141592653590 rad`
- potência porto escuro ideal: `3.749399456655e-33`
- potência porto claro ideal: `1.000000000000e+00`
- crosstalk ideal: `3.749399456655e-33`

## Imperfeições materiais equivalentes a -30 dB

- erro de fase requerido: `delta_phi = 6.322448399238e-02 rad`
- erro equivalente de tensão: `delta_V = 4.920557195241e-02 V`
- erro relativo de tensão: `2.012497830364e-02`
- razão de amplitude requerida isoladamente: `0.938693139937`
- desbalanceamento de amplitude: `-0.549527119802 dB`
- erro diferencial de acoplador: `delta_theta = 3.161224199619e-02 rad`
- split de potência correspondente: `0.531591185416`

## Impedância efetiva equivalente

- `Gamma_target = 3.453877639491`
- `R_target = 3.453877639491` para `||DeltaPhi||^2=2`

## Interpretação

Com Vpi ideal e acopladores de 3 dB ideais, o crosstalk estacionário é zero.
O valor finito de -30 dB exige imperfeição material: fase, amplitude, acoplador ou mistura delas.
Logo, o crosstalk pertence a delta K_app material/fabricação/perdas, não à ação fundamental.
