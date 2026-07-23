---
title: "Saída — verificar unitariedade em tempo físico"
---

# Saída — verificar unitariedade em tempo físico

Classificação: teste de consistência algébrica/numerica.

## Dados

- dimensão do setor fechado: 3
- autovalores de $H$: 0.329602635099, 1.087742645439, 2.332654719462
- tempo físico usado: $t=2.7$
- parâmetro euclidiano usado: $a=1.3$

## Resultados

| Quantidade | Valor | Interpretação |
|---|---:|---|
| erro $\|U^\dagger U-I\|$ | 8.153e-16 | deve ser próximo de zero |
| norma inicial $\|\psi\|^2$ | 1.000000000000 | normalizada |
| norma após $U(t)$ | 1.000000000000 | preservada |
| norma espectral de $T_E(a)$ | 0.651496388608 | contração euclidiana |
| norma após $T_E(a)$ | 0.231268588835 | amortecimento em parâmetro euclidiano |
| sobrevivência projetada não Hermitiana | 0.296710014294 | decai no setor parcial |
| $\exp(-\Gamma t/\hbar)$ | 0.296710014294 | referência analítica |
| erro de norma total no modelo Hermitiano ampliado | 2.220e-16 | total fechado preserva norma |
| probabilidade no canal $P$ | 0.449368694702 | canal observado |
| probabilidade vazada para $Q$ | 0.550631305298 | canal não observado |
| erro de balanço $P+Q=1$ | 0.000e+00 | conservação total |

## Leitura física

O teste separa três fatos. O grupo $U(t)$ preserva norma quando $H$ é
Hermitiano. O semigrupo euclidiano $T_E(a)$ é contrativo quando $H\ge0$.
Um setor projetado pode decair sem que a dinâmica total fechada deixe de ser
unitária.
