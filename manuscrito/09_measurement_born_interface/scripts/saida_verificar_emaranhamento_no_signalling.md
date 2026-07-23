# Saída — emaranhamento reduzido e no-signalling

Classificação: teste de consistência operacional reduzido.

## Não fatoração

Valores singulares de Schmidt do singlete:

| índice | valor |
|---:|---:|
| 0 | 0.707106781187 |
| 1 | 0.707106781187 |

Como os dois valores são não nulos, o estado não tem posto de Schmidt 1 e não
é produto. O menor valor singular preservado é:

$$
0.707106781187.
$$

## Correlação e marginais

| eixo A | eixo B | $a\cdot b$ | $E(a,b)$ | alvo $-a\cdot b$ | $P(+|a,b)$ em A | $P(+|a,b)$ em B |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 1.000000000000 | -1.000000000000 | -1.000000000000 | 0.500000000000 | 0.500000000000 |
| 0 | 1 | 0.000000000000 | 0.000000000000 | -0.000000000000 | 0.500000000000 | 0.500000000000 |
| 0 | 2 | 0.707106781187 | -0.707106781187 | -0.707106781187 | 0.500000000000 | 0.500000000000 |
| 1 | 0 | 0.000000000000 | 0.000000000000 | -0.000000000000 | 0.500000000000 | 0.500000000000 |
| 1 | 1 | 1.000000000000 | -1.000000000000 | -1.000000000000 | 0.500000000000 | 0.500000000000 |
| 1 | 2 | -0.707106781187 | 0.707106781187 | 0.707106781187 | 0.500000000000 | 0.500000000000 |
| 2 | 0 | 0.707106781187 | -0.707106781187 | -0.707106781187 | 0.500000000000 | 0.500000000000 |
| 2 | 1 | 0.707106781187 | -0.707106781187 | -0.707106781187 | 0.500000000000 | 0.500000000000 |
| 2 | 2 | 0.000000000000 | 0.000000000000 | -0.000000000000 | 0.500000000000 | 0.500000000000 |

## Erros

| teste | valor |
|---|---:|
| erro máximo em $E(a,b)+a\cdot b$ | 0.000000000000e+00 |
| variação máxima da marginal A ao trocar B | 0.000000000000e+00 |
| variação máxima da marginal B ao trocar A | 0.000000000000e+00 |
| valor CHSH reduzido | -2.828427124746 |
| alvo $-2\sqrt 2$ | -2.828427124746 |

## Interpretação

O teste mostra que a correlação conjunta depende dos dois eixos, mas as
marginais locais permanecem iguais a $1/2$. Isso é compatibilidade operacional
com no-signalling no setor projetivo reduzido. A GDQ completa ainda deve
derivar os aparelhos reais por $K_{AB}^{\rm phys}$, $\mathsf R_A$ e
$\mathsf R_B$.
