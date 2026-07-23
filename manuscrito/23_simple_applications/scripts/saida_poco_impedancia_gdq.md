---
title: "Saída — poço com impedância GDQ"
---

# Saída — poço com impedância GDQ

- unidades: $L=1$ e $\hbar^2/(2mL^2)=1$;
- altura da parede: `1000`;
- espessura: `0.25L`;
- classificação: teste de consistência/convergência.

| $n$ | Robin/DtN | Barreira direta | Poço infinito | erro direto--DtN | desvio ao infinito |
|---:|---:|---:|---:|---:|---:|
| 1 | `8.7288524345` | `8.7288554342` | `9.8696044011` | `3.437e-07` | `-1.156e-01` |
| 2 | `34.8969392566` | `34.8969493529` | `39.4784176044` | `2.893e-07` | `-1.161e-01` |
| 3 | `78.4467355072` | `78.4467510255` | `88.8264396098` | `1.978e-07` | `-1.169e-01` |
| 4 | `139.2746889920` | `139.2746987325` | `157.9136704174` | `6.994e-08` | `-1.180e-01` |
| 5 | `217.2171167906` | `217.2170964254` | `246.7401100272` | `9.375e-08` | `-1.197e-01` |

| pontos | máximo erro relativo contra Robin/DtN | tempo [s] |
|---:|---:|---:|
| 599 | `8.814e-05` | `0.0012` |
| 1199 | `2.205e-05` | `0.0016` |
| 2399 | `5.514e-06` | `0.0031` |
| 4799 | `1.379e-06` | `0.0057` |
| 9599 | `3.437e-07` | `0.0110` |

- erro máximo na malha mais fina: `3.437e-07`.
- a diferença contra o poço infinito é penetração física na parede.
