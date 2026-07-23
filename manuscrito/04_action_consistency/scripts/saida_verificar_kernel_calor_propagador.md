---
title: "Saída — kernel de calor e propagador GDQ"
---

# Saída — kernel de calor e propagador GDQ

Parâmetros do teste, sem ajuste:

- $\tau=0.25$
- $\widehat\Lambda_\tau=\tau^{-1/2}=2.000000000000$
- $m=0.7$

| $p_E$ | $G_\tau=e^{-\tau p^2}/(p^2+m^2)$ | forma errada $e^{-\tau^2p^2}/(p^2+m^2)$ | razão errada/correta |
|---:|---:|---:|---:|
| `0.000000` | `2.040816326531e+00` | `2.040816326531e+00` | `1.000000000000e+00` |
| `0.500000` | `1.269477111910e+00` | `1.330400590548e+00` | `1.047991002017e+00` |
| `1.000000` | `5.226850893097e-01` | `6.304785656466e-01` | `1.206230249421e+00` |
| `2.000000` | `8.193306039453e-02` | `1.734522902163e-01` | `2.117000016613e+00` |
| `4.000000` | `1.110711879244e-03` | `2.230924446158e-02` | `2.008553692319e+01` |
| `8.000000` | `1.745001933932e-09` | `2.840074257828e-04` | `1.627547914190e+05` |

## Polos

O numerador $e^{-\tau p^2}$ é sempre positivo no eixo real euclidiano.
Logo não cria polos. O denominador zera apenas quando $p_E^2+m^2=0$,
isto é, fora do eixo real euclidiano para $m^2>0$.

## Classificação

Teste de consistência do limite plano do semigrupo de calor; não é previsão metrológica.
