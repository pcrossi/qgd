# Saída — Q57: escalas de aceleração

| Quantidade | Valor [m/s²] | Erro relativo vs 1.20e-10 |
| --- | ---: | ---: |
| c H0 Planck | 6.548322413981e-10 | — |
| c H0 Planck / 2pi | 1.042197881145e-10 | -13.150177% |
| c H0 local / 2pi | 1.128789989964e-10 | -5.934168% |
| c H0 sqrt(Omega_Lambda) | 5.418514229171e-10 | — |
| c H0 sqrt(Omega_Lambda) / 2pi | 8.623833237863e-11 | -28.134723% |

Correção aritmética explícita:
(c H0 sqrt(Omega_Lambda))/(2pi) = 8.623833237863e-11 m/s²
Portanto, se o numerador for 5.46e-10, a divisão por 2pi dá ~8.69e-11,
não 1.21e-10.

Rota GDQ adotada para Q57:
a0_GDQ = c^2/(2pi R_H) = c H0/(2pi), usando o mesmo horizonte R_H da Q56.
Com H0=67.4 km/s/Mpc: a0_GDQ = 1.042197881145e-10 m/s².
