---
title: "Saída — transporte de medida ponderada"
---

# Saída — transporte de medida ponderada

Classificação: verificação de consistência / toy model de medida.

| escala $a$ | norma com jacobiano | norma sem jacobiano |
|---:|---:|---:|
| 0.5 | 1.000000000000 | 0.500000000000 |
| 1.0 | 1.000000000000 | 1.000000000000 |
| 2.0 | 1.000000000000 | 2.000000000000 |
| 4.0 | 1.000000000000 | 4.000000000000 |

Conclusão: o transporte correto da medida exige o fator jacobiano.
No Capítulo 6, isso corresponde ao cuidado de identificar os espaços de
Hilbert ponderados pela raiz do jacobiano da medida, não apenas puxar
funções entre cartas.
