---
title: "Saída — Schur de superfície em escalas atômicas"
---

# Saída — Schur de superfície em escalas atômicas

Classificação: cálculo direto reduzido/no-go setorial.

- $r_p=0.840778765450$ fm
- $\Lambda_E=\sqrt{12}/r_p=4.120110732439$ fm$^{-1}$

$$
\mathsf R_\Sigma(q)
=
-J_\Sigma(q)^T K_\Sigma(q)^{-1}J_\Sigma(q),
\qquad
x=\frac{q^2}{\Lambda_E^2}.
$$

| escala | $q$ [fm$^{-1}$] | $x$ | min eig $K$ | max eig $K$ | $\mathsf R_\Sigma$ |
|---|---:|---:|---:|---:|---:|
| hiperfina 1s | `1.888697509086e-05` | `2.101391825245e-11` | `1.000000000021e+00` | `1.000000000042e+00` | `-2.089031019060e-21` |
| Lamb 2s | `9.443487545431e-06` | `5.253479563111e-12` | `1.000000000005e+00` | `1.000000000011e+00` | `-1.305644386936e-22` |
| hadrônica 1/r_p | `1.189373520232e+00` | `8.333333333333e-02` | `1.083333333333e+00` | `1.173611111111e+00` | `-2.999611553485e-02` |
| espalhamento baixo | `2.500000000000e-01` | `3.681817356415e-03` | `1.003681817356e+00` | `1.007377190492e+00` | `-6.386079337265e-05` |
| espalhamento médio | `1.000000000000e+00` | `5.890907770264e-02` | `1.058909077703e+00` | `1.121288434841e+00` | `-1.538200245154e-02` |

Conclusão: em escala atômica, $x\ll1$ e o Schur coletivo é de ordem
$x^2$. Portanto esse bloco não fecha o resíduo hiperfino de ordem
$10^{-5}$ nem o Lamb shift. Ele pertence ao setor de fatores de forma
em escalas hadrônicas/intermediárias.
