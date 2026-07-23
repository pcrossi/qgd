# Saída — projetor físico linear

## Classificação

Ilustração linear de quociente físico. Não é previsão física.

## Construção

Dadas direções removidas reunidas em $A$, usa-se:

$$
P=I-A(A^TA)^{-1}A^T
$$

após ortonormalização das colunas.

## Resultado

- Dimensão total: `5`.
- Dimensão física projetada: `2`.
- Erro $P^2-P$: `4.510e-16`.
- Erro $P^T-P$: `0.000e+00`.
- Erro de remoção das direções: `4.661e-16`.
- Autovalores de $P$: `[-1.2720394860383697e-16, 0.0, 4.602708559913833e-16, 1.0, 1.0]`.

## Veredito

A checagem passou.

Esta saída ilustra a álgebra do projetor. No problema GDQ real, $P_{\rm phys}$ depende do domínio, dos vínculos e do contorno.
