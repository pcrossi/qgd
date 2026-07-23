# Q53 — Sensibilidade dos coeficientes neutros

## Escala fixa

- `S_nu = alpha^7 Q_beta^2 = 6.744367477916e-04 eV^2`

## Coeficientes requeridos versus GDQ reduzido

| item | valor |
|---|---:|
| lambda2 requerido | 1.110556330824e-01 |
| lambda2 GDQ reduzido | 1.147804383800e-01 |
| lambda2 erro rel | 3.353999427387e-02 |
| lambda3 requerido | 3.757209268768e+00 |
| lambda3 6pi/5 | 3.769911184308e+00 |
| lambda3 erro rel | 3.380678219244e-03 |
| chi requerido para dm21 | 4.712868194260e-01 |
| chi GDQ | 4.791251159771e-01 |
| fator axial requerido lambda3/(2pi) | 5.979784273551e-01 |
| fator axial GDQ 3/5 | 6.000000000000e-01 |

## Leitura

- O coeficiente superior requerido corresponde a `lambda3/(2pi) = 5.979784273551e-01`, próximo de `3/5 = 0.6`.
- O coeficiente GDQ `6pi/5` gera erro relativo de +3.380678e-03 em `dm31`.
- O canal `chi=(12/25)exp(-alpha/4)` gera erro relativo de +3.353999e-02 em `dm21`.
- Portanto, o gargalo principal é derivar o bloco bicanal de interface que corrige `lambda2`, não o modo superior.
