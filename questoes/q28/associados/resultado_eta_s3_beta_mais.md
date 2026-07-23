# Q28 — Teste espectral no elo $S^3$

## Configuração

- $2j_{\max}=30$;
- raio $a=1$;
- deslocamento torsional de teste $\beta=1.5$.

## Verificação livre

Erro máximo nos primeiros níveis distintos: $0.000e+00$.

## Hopf e assimetria

| $m$ | menor $|\lambda|$ | kernel $h$ | modos negativos | modos positivos | $\bar\eta\pmod 1$ por CS |
|---:|---:|---:|---:|---:|---:|
| -3 | 0.0000000000e+00 | 1 | 9920 | 10911 | 0.500000 |
| -2 | 8.2842712475e-01 | 0 | 9920 | 10912 | 0.000000 |
| -1 | 2.3606797750e-01 | 0 | 9920 | 10912 | 0.500000 |
| 0 | 0.0000000000e+00 | 2 | 9918 | 10912 | 0.000000 |
| 1 | 2.3606797750e-01 | 0 | 9920 | 10912 | 0.500000 |
| 2 | 8.2842712475e-01 | 0 | 9920 | 10912 | 0.000000 |
| 3 | 0.0000000000e+00 | 1 | 9920 | 10911 | 0.500000 |

## Nota de auditoria

A diferença finita entre contagens positivas e negativas depende do cutoff
e não é usada como $\eta(0)$. A parte fracionária apresentada vem da
transgressão APS/Chern--Simons, que é estável módulo fluxo espectral inteiro.
