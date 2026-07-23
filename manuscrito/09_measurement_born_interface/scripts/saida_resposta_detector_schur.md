# Saída — resposta reduzida de detector por Schur

Classificação: redução efetiva/aparelho.

## Matriz de impedância

$$
\mathsf R_{\rm app}
=
\begin{pmatrix}
1.876086956522 & 0.132608695652 \\
0.132608695652 & 1.446530100334
\end{pmatrix}.
$$

## Verificações

| teste | valor |
|---|---:|
| autovalor mínimo de R_app | 1.408890543061 |
| autovalor máximo de R_app | 1.913726513796 |
| Gamma_det | 1.528699832776 |
| C_det = exp(-Gamma_det) | 0.216817382993 |

Interpretação: a resposta de detector positiva reduz a coerência por
$\mathcal C_{\rm det}=e^{-\Gamma_{\rm det}}$. Os números são de toy model.
