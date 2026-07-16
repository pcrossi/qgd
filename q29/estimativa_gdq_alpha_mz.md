# Q29 — Estimativa GDQ reduzida de $\alpha^{-1}(M_Z)$

## Hipóteses mínimas

Esta é uma estimativa, não a avaliação do determinante completo. Ela usa:

1. três limiares do espectro geracional dos estômatos;
2. o gerador $Q=T_3+Y$ da representação geométrica da Q28;
3. a soma de cargas quadráticas por geração;
4. o peso $2/3$ do setor colorido no equilíbrio torsional confinado.

Por geração, o canal leptônico carregado fornece

$$
\sum_{\ell}q^2=1,
$$

e os três canais coloridos fornecem

$$
\sum_Cq^2
=3\left[\left(\frac23\right)^2+\left(\frac13\right)^2\right]
=\frac53.
$$

O equilíbrio torsional com dois canais alinhados e um canal compensador é
representado, nesta redução, pela transmissão

$$
\mathcal T_C=\frac23.
$$

Esse valor é fixado antes do cálculo; não é escolhido para produzir $128$.

## Resposta espectral

Para um limiar geracional $m_g$, usamos a resposta finita

$$
\mathcal P_g(Q)
=\frac2\pi\int_0^1
x(1-x)
\ln\left[1+\frac{Q^2}{m_g^2}x(1-x)\right]dx.
$$

Nos três limiares, em $Q=M_Z$, resulta

$$
(\mathcal P_1,\mathcal P_2,\mathcal P_3)
=(2{,}3891764154,1{,}2577768737,0{,}6590867830).
$$

Portanto,

$$
\mathcal P_L=4{,}3060400722,
$$

$$
\mathcal P_C^{\rm efetiva}
=\frac23\frac53\mathcal P_L
=4{,}7844889691,
$$

e

$$
\Delta\alpha^{-1}
=-(\mathcal P_L+\mathcal P_C^{\rm efetiva})
=-9{,}0905290412.
$$

Partindo do valor geométrico de baixa energia,

$$
\boxed{
\alpha^{-1}(M_Z)
=137{,}035999084-9{,}090529041
=127{,}945470043.
}
$$

O desvio em relação a $128$ é

$$
-0{,}054529957,
$$

ou aproximadamente $0{,}043\%$.

## Interpretação

A estimativa mostra que a estrutura GDQ de três estômatos, cargas geométricas
e equilíbrio torsional $2/3$ possui a intensidade espectral correta para
transportar $\alpha^{-1}$ da região $137$ para a região $128$.

O resultado ainda é condicional à identificação da transmissão $2/3$ com o
peso do traço de calor colorido. O cálculo definitivo deve substituir esse
peso reduzido pela função de transmissão espectral do operador confinado.
