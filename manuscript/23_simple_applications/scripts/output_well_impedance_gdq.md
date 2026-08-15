---
title: "Output — Well with GDQ Impedance"
---

# Output — Well with GDQ Impedance

- units: $L=1$ and $\hbar^2/(2mL^2)=1$;
- wall height: `1000`;
- thickness: `0.25L`;
- classification: consistency/convergence test.

| $n$ | Robin/DtN | Direct barrier | Infinite well | direct--DtN error | deviation to infinite |
|---:|---:|---:|---:|---:|---:|
| 1 | `8.7288524345` | `8.7288554342` | `9.8696044011` | `3.437e-07` | `-1.156e-01` |
| 2 | `34.8969392566` | `34.8969493529` | `39.4784176044` | `2.893e-07` | `-1.161e-01` |
| 3 | `78.4467355072` | `78.4467510255` | `88.8264396098` | `1.978e-07` | `-1.169e-01` |
| 4 | `139.2746889920` | `139.2746987325` | `157.9136704174` | `6.994e-08` | `-1.180e-01` |
| 5 | `217.2171167906` | `217.2170964254` | `246.7401100272` | `9.375e-08` | `-1.197e-01` |

| points | maximum relative error against Robin/DtN | time [s] |
|---:|---:|---:|
| 599 | `8.814e-05` | `0.0012` |
| 1199 | `2.205e-05` | `0.0016` |
| 2399 | `5.514e-06` | `0.0031` |
| 4799 | `1.379e-06` | `0.0057` |
| 9599 | `3.437e-07` | `0.0110` |

- maximum error in the finest mesh: `3.437e-07`.
- the difference against the infinite well is physical wall penetration.
