---
title: "Saída — convergência do raio de superfície"
---

# Saída — convergência do raio de superfície

## Fórmula estrutural

$$
r_p
=
C_r\epsilon_{\rm eff}R_B,
\qquad
C_r=\frac18\left(1+\frac\alpha4\right),
\qquad
R_B=\frac32\Lambda_C.
$$

| quantidade | valor |
|---|---:|
| $\Lambda_C$ | `386.159268` fm |
| $R_B$ | `579.238902000000` fm |
| $\epsilon_{\rm eff}$ | `0.011591040463` |
| $C_r$ | `0.125228042267635` |
| $r_p$ estrutural | `0.840778765431` fm |

## Regularização por meia-gaussiana

| $\sigma/\epsilon_{\rm eff}$ | $r_p(\sigma)$ fm | desvio relativo |
|---:|---:|---:|
| `0.50000000` | `1.092750294041` | `+2.996882639879e-01` |
| `0.25000000` | `0.963543026868` | `+1.460125617871e-01` |
| `0.12500000` | `0.901187728766` | `+7.184882137685e-02` |
| `0.06250000` | `0.870714330840` | `+3.560456881160e-02` |
| `0.03125000` | `0.855675767325` | `+1.771809958443e-02` |
| `0.01562500` | `0.848209103346` | `+8.837447163004e-03` |
| `0.00781250` | `0.844489333592` | `+4.413251516057e-03` |
| `0.00390625` | `0.842632891708` | `+2.205248697091e-03` |
| `delta_surface` | `0.840778765431` | `+0.000000000000e+00` |

## Veredito

A sequência regularizada converge para a delta de superfície. O cálculo
volumétrico radial bruto mede modo interno do bulk, não o raio
eletromagnético observado.
