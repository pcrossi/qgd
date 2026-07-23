# Saída — cálculo direto do raio de Zemach Q48

Classificação: avaliação direta do modelo de fatores de forma de superfície Q40.

Fórmula:

$$
r_Z=-\frac4\pi\int_0^\infty\frac{dq}{q^2}
\left[\frac{G_E(q)G_M(q)}{G_M(0)}-1\right].
$$

| caso | r_E (fm) | r_M (fm) | r_Z numérico (fm) | erro quad | referência analítica |
|---|---:|---:|---:|---:|---:|
| casca coincidente Q40 | 0.840778765450 | 0.840778765450 | 1.121038354001 | 2.317e-09 | 1.121038353933 |
| teste rM 5% maior | 0.840778765450 | 0.882817703723 | 1.149731597308 | 4.658e-10 |  |
| teste rM 5% menor | 0.840778765450 | 0.798739827177 | 1.093713043936 | 4.432e-10 |  |

Conclusão: o valor usado na hiperfina, $r_Z=4r_p/3$, é confirmado
diretamente pela integral de fatores de forma quando $r_E=r_M=r_p$.
Separar $r_M$ de $r_E$ é exatamente o próximo refinamento da Hessiana
magnética superior do próton.
