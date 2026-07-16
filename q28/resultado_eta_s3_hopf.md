# Q28 — Teste espectral no elo $S^3$

## Configuração

- $2j_{\max}=30$;
- raio $a=1$;
- deslocamento torsional de teste $\beta=0$.

## Verificação livre

Erro máximo nos primeiros níveis distintos: $0.000e+00$.

## Hopf e assimetria

| $m$ | menor $|\lambda|$ | kernel $h$ | modos negativos | modos positivos | $\bar\eta\pmod 1$ por CS |
|---:|---:|---:|---:|---:|---:|
| -3 | 5.0000000000e-01 | 0 | 9923 | 10909 | 0.500000 |
| -2 | 5.0000000000e-01 | 0 | 9921 | 10911 | 0.000000 |
| -1 | 5.0000000000e-01 | 0 | 9920 | 10912 | 0.500000 |
| 0 | 1.5000000000e+00 | 0 | 9920 | 10912 | 0.000000 |
| 1 | 5.0000000000e-01 | 0 | 9920 | 10912 | 0.500000 |
| 2 | 5.0000000000e-01 | 0 | 9921 | 10911 | 0.000000 |
| 3 | 5.0000000000e-01 | 0 | 9923 | 10909 | 0.500000 |

## Nota de auditoria

A diferença finita entre contagens positivas e negativas depende do cutoff
e não é usada como $\eta(0)$. A parte fracionária apresentada vem da
transgressão APS/Chern--Simons, que é estável módulo fluxo espectral inteiro.
