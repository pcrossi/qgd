---
title: "Saída — Hessiana escalar reduzida"
---

# Saída — Hessiana escalar reduzida

Caso teste: fundo plano, $f_0$ constante, $R_0=0$, domínio periódico.

$$
L_\varphi=2(-\Delta).
$$

Malha: `N=128`, comprimento `2π`.

| índice | esperado $2k^2$ | numérico | erro |
|---:|---:|---:|---:|
| `0` | `0.000000000000e+00` | `1.081841528481e-12` | `1.081841528481e-12` |
| `1` | `2.000000000000e+00` | `1.999598437023e+00` | `-4.015629769234e-04` |
| `2` | `2.000000000000e+00` | `1.999598437024e+00` | `-4.015629758756e-04` |
| `3` | `8.000000000000e+00` | `7.993576540314e+00` | `-6.423459686258e-03` |
| `4` | `8.000000000000e+00` | `7.993576540314e+00` | `-6.423459685615e-03` |
| `5` | `1.800000000000e+01` | `1.796749429161e+01` | `-3.250570838993e-02` |
| `6` | `1.800000000000e+01` | `1.796749429161e+01` | `-3.250570838813e-02` |
| `7` | `3.200000000000e+01` | `3.189732364944e+01` | `-1.026763505617e-01` |
| `8` | `3.200000000000e+01` | `3.189732364944e+01` | `-1.026763505611e-01` |

Conclusão: no fundo plano, a Hessiana escalar reduzida tem símbolo principal positivo proporcional a $p_E^2$.
A diferença finita converge para o espectro contínuo quando a malha é refinada.
