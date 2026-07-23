# Q39 — saída do critério warped/misto

## Fórmulas

$$
m_\perp^2
=
C_\gamma\tau R_{\max}^{-2}
-
\sum_i c_i a_i^2.
$$

$$
j_{\rm mix}=\sum_i b_i a_i.
$$

$$
\Delta_{\rm Schur}
=
\frac{j_{\rm mix}^2}{m_\perp^2}.
$$

Estável/subcrítico se:

$$
\Delta_{\rm Schur}<\lambda_B^{\rm gap}.
$$

## Cenários normalizados

| cenário | m_perp^2 | j_mix | Schur | Schur/gap | status |
|---|---:|---:|---:|---:|---|
| produto | 1 | 0 | 0 | 0 | subcritico |
| fraco_um_canal_0p1 | 0.99 | 0.1 | 0.010101010101 | 0.010101010101 | subcritico |
| quatro_canais_0p1 | 0.96 | 0.4 | 0.166666666667 | 0.166666666667 | subcritico |
| um_canal_critico_lambda1 | 0.5 | 0.707106781187 | 1 | 1 | critico |
| um_canal_supercritico_0p8 | 0.36 | 0.8 | 1.77777777778 | 1.77777777778 | supercritico |

## Limiar de um canal

Para um único canal misto ativo com amplitude `a` e `lambda_B_gap=1`:

$$
a_{\rm crit}=\frac1{\sqrt2}\simeq0.707106781187.
$$

Abaixo desse valor, a mistura warped/mista não altera o índice crítico.
Acima dele, o background pode gerar modo adicional, que deve ser
classificado como ressonância, estado de contorno ou estado composto
até prova de carga primitiva e estabilidade assintótica.
