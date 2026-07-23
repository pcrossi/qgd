# Regime não adiabático — Capítulo 11

Hamiltoniano: `H(t)=(v t sigma_z + Delta sigma_x)/2`, com `Delta=1` e `hbar=1`.

| v | P_exc numérica | Landau–Zener | erro absoluto |
|---:|---:|---:|---:|
| 0.200 | 0.000387351 | 0.000388203 | 8.521e-07 |
| 0.400 | 0.019708490 | 0.019702873 | 5.617e-06 |
| 0.800 | 0.140436139 | 0.140366923 | 6.922e-05 |
| 1.600 | 0.374824101 | 0.374655739 | 1.684e-04 |
| 3.200 | 0.612383265 | 0.612091283 | 2.920e-04 |

- maior erro numérico/assintótico: `2.920e-04`;
- norma de `[H,P_z+]` no teste: `0.707106781`;
- deriva instantânea `dp_z/dt` no estado de teste: `0.500000000`.

## Interpretação

A probabilidade de troca de canal cresce com a velocidade da varredura. Logo, a identificação imediata dos canais com os projetores instantâneos exige a condição adiabática.

Quando `[H,P_n] != 0`, `p_n=Tr(P_n rho)` recebe a deriva `-i Tr(P_n[H,rho]) dt` e deixa de ser martingal. Portanto, a prova de primeiro alcance da regra de Born continua válida no setor de medição adiabática/QND documentado, mas não pode ser transportada sem alteração para um aparelho cuja direção varia rapidamente.

Este teste valida a dinâmica reduzida de dois níveis. Ele ainda não fixa `Delta` ou `v` em unidades físicas a partir do background GDQ.
