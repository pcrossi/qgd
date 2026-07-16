# Q28 — Teste espectral no elo $S^3$

## Configuração

- $2j_{\max}=30$;
- raio $a=1$;
- deslocamento torsional de teste $\beta=-1.5$.

## Verificação livre

Erro máximo nos primeiros níveis distintos: $0.000e+00$.

## Hopf e assimetria

| $m$ | menor $|\lambda|$ | kernel $h$ | modos negativos | modos positivos | $\bar\eta\pmod 1$ por CS |
|---:|---:|---:|---:|---:|---:|
| -3 | 0.0000000000e+00 | 4 | 9926 | 10902 | 0.500000 |
| -2 | 0.0000000000e+00 | 3 | 9923 | 10906 | 0.000000 |
| -1 | 0.0000000000e+00 | 2 | 9921 | 10909 | 0.500000 |
| 0 | 0.0000000000e+00 | 2 | 9920 | 10910 | 0.000000 |
| 1 | 0.0000000000e+00 | 2 | 9921 | 10909 | 0.500000 |
| 2 | 0.0000000000e+00 | 3 | 9923 | 10906 | 0.000000 |
| 3 | 0.0000000000e+00 | 4 | 9926 | 10902 | 0.500000 |

## Nota de auditoria

A diferença finita entre contagens positivas e negativas depende do cutoff
e não é usada como $\eta(0)$. A parte fracionária apresentada vem da
transgressão APS/Chern--Simons, que é estável módulo fluxo espectral inteiro.
