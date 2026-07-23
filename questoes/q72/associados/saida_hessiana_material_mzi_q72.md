# Saída — Q72 Hessiana material reduzida EO-MZI

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

## Imperfeições materiais necessárias para -30 dB

- erro de fase requerido: `delta_phi = 6.322448399238e-02 rad`
- erro equivalente de tensão: `delta_V = 4.920557195241e-02 V`
- erro relativo de tensão: `2.012497830364e-02`
- razão de amplitude requerida isoladamente: `0.938693139937`
- desbalanceamento de amplitude em dB: `-0.549527119802 dB`
- erro diferencial de acoplador requerido: `delta_theta = 3.161224199619e-02 rad`
- split de potência correspondente: `0.531591185416`

## Impedância efetiva equivalente

- `Gamma_target = 3.453877639491`
- `R_target = 3.453877639491` para `||DeltaPhi||^2=2`

## Interpretação

Com Vpi ideal e acopladores 3 dB ideais, o crosstalk estacionário é zero.
O valor finito de -30 dB exige imperfeição material: fase, amplitude, acoplador ou mistura delas.
Portanto, `K_app` explica onde o crosstalk mora: no Hessiano material de fabricação e perdas, não na ação fundamental.
