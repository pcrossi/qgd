---
title: "Saída — simular decoerência S+A+E"
---

# Saída — simular decoerência S+A+E

Classificação: redução efetiva de medição.

## Coeficientes iniciais

- $|c_0|^2 = 0.370000000000$
- $|c_1|^2 = 0.630000000000$

## Supressão por ortogonalização ambiental

| sobreposição ambiental eta | coerência reduzida | p0 | p1 |
|---:|---:|---:|---:|
| 1.000 | 0.482804308183 | 0.370000000000 | 0.630000000000 |
| 0.500 | 0.241402154091 | 0.370000000000 | 0.630000000000 |
| 0.100 | 0.048280430818 | 0.370000000000 | 0.630000000000 |
| 0.010 | 0.004828043082 | 0.370000000000 | 0.630000000000 |
| 0.000 | 0.000000000000 | 0.370000000000 | 0.630000000000 |

## Decaimento por gap setorial

Usando $|\Gamma_{01}(\tau)|\le C e^{-\Delta_{\rm meas}\tau}$ com
$C=1.000$ e $\Delta_{\rm meas}=1.750$:

| tau | limite para $|\Gamma_{01}|$ |
|---:|---:|
| 0.000 | 1.000000000000e+00 |
| 0.500 | 4.168620196785e-01 |
| 1.000 | 1.737739434504e-01 |
| 2.000 | 3.019738342232e-02 |
| 4.000 | 9.118819655545e-04 |

## Repetibilidade ideal

Após condicionar no registro 0:

| teste | valor |
|---|---:|
| $p_0=\operatorname{Tr}(\rho_S P_0)$ | 0.370000000000 |
| $\operatorname{Tr}(\rho_{S|0}P_0)$ | 1.000000000000 |
| erro de repetibilidade | 0.000000000000e+00 |

## Interpretação

Quando a sobreposição ambiental tende a zero, os termos de interferência
desaparecem, mas os pesos diagonais permanecem iguais aos pesos operacionais
de Born. O gap setorial fornece supressão exponencial assintótica. Após
condicionamento em um registro, a repetição ideal do mesmo projetor dá
probabilidade 1.

Isso ainda não seleciona sozinho o evento individual; a seleção ontológica
exige bacias reais do aparelho/ambiente.
