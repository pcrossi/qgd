---
title: "Saída — limite de tempo longo da Regra de Ouro"
---

# Verificação do kernel de tempo finito

Classificação: teste de consistência e convergência; nenhum parâmetro foi
ajustado a dado experimental.

Unidades do teste: $\hbar=1$ e janela $E\in[-12,12]$.

| $T$ | $\int\delta_T dE$ | gaussiana | erro gaussiana | lorentziana | erro lorentziana |
|---:|---:|---:|---:|---:|---:|
| 5.0 | 0.989437887713 | 0.774352871410 | 2.256e-01 | 0.801323423455 | 1.987e-01 |
| 10.0 | 0.994669776980 | 0.887162083290 | 1.128e-01 | 0.899992141885 | 1.000e-01 |
| 20.0 | 0.997336999738 | 0.943581041645 | 5.642e-02 | 0.949993813699 | 5.001e-02 |
| 40.0 | 0.998671997986 | 0.971790520823 | 2.821e-02 | 0.974996930750 | 2.500e-02 |
| 80.0 | 0.999337524809 | 0.985895260411 | 1.410e-02 | 0.987498475931 | 1.250e-02 |
| 160.0 | 0.999668507801 | 0.992947630206 | 7.052e-03 | 0.993749236207 | 6.251e-03 |
| 320.0 | 0.999834177927 | 0.996473815103 | 3.526e-03 | 0.996874617580 | 3.125e-03 |

As duas funções teste valem exatamente 1 em $E=0$. Portanto, ambas as
integrais devem tender a 1.

## Refinamento da quadratura em $T=320$

| pontos por período | norma | gaussiana | lorentziana |
|---:|---:|---:|---:|
| 40 | 0.999834177982 | 0.996473815103 | 0.996874617581 |
| 80 | 0.999834177927 | 0.996473815103 | 0.996874617580 |
| 160 | 0.999834177913 | 0.996473815103 | 0.996874617580 |

O erro dominante da norma é o truncamento da janela energética. A
estabilidade sob refinamento separa esse efeito do erro de quadratura.
