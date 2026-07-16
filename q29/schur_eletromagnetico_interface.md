# Q29 — Complemento de Schur eletromagnético da interface

## 1. Lei de colagem

Seja $A$ o dado eletromagnético externo e $x$ o valor interno na garganta. A
continuidade de potencial e o balanço de fluxo são representados pela energia
quadrática mínima de duas impedâncias em série:

$$
S^{(2)}_{\rm col}
=\frac12K_0x^2
+\frac12K_\partial(A-x)^2.
$$

Essa forma não acrescenta um campo fundamental: $x$ é o traço de interface do
mesmo modo eletromagnético. Ela é a forma variacional da composição de
operadores Dirichlet-to-Neumann.

Na base $(x,A)$,

$$
\mathbb H_{\rm EM}
=\begin{pmatrix}
K_0+K_\partial&-K_\partial\\
-K_\partial&K_\partial
\end{pmatrix}.
$$

## 2. Complemento de Schur

Eliminando $x$,

$$
K_{\rm EM}^{\rm eff}
=K_\partial
-K_\partial(K_0+K_\partial)^{-1}K_\partial
$$

e, portanto,

$$
\boxed{
K_{\rm EM}^{\rm eff}
=\frac{K_0K_\partial}{K_0+K_\partial}.
}
$$

## 3. Identificação da admitância

A admitância de superfície deve ser definida como a razão de compliâncias

$$
\mathcal S_\partial
:=\frac{K_0}{K_\partial}.
$$

Então

$$
\boxed{
K_{\rm EM}^{\rm eff}
=\frac{K_0}{1+\mathcal S_\partial}.
}
$$

Usando

$$
\mathcal S_\partial
=\alpha\left(\frac{3\pi}{2}+\frac{3}{4\pi^3}\right)
=0{,}0345644769503,
$$

segue

$$
\frac{K_{\rm EM}^{\rm eff}}{K_0}
=0{,}966590303209
$$

e

$$
\boxed{\alpha_{\rm EM}^{-1}=132{,}457669022.}
$$

A Hessiana completa possui autovalores positivos, logo a colagem é passiva e
estável.

## 4. Alcance exato

O complemento de Schur e seu sinal estão agora derivados. Permanece uma
hipótese constitutiva localizada: identificar o número topológico/espectral
da Q40 com a razão de compliâncias $K_0/K_\partial$. A Q40 forneceu o número e
sua interpretação como admitância, mas sua segunda variação direta pela ação
oficial ainda está auditada como pendência.

Assim, o resultado é um teorema condicional:

$$
\boxed{
\mathcal S_\partial=K_0/K_\partial
\Longrightarrow
\alpha_{\rm EM}^{-1}=132{,}457669022.
}
$$

Não há mais ambiguidade de álgebra, sinal ou denominador; a única pendência é
a igualdade constitutiva acima.

Uma segunda variação posterior mostrou que o valor Chern--Simons no background
tem Hessiana métrica nula e que a parcela espectral fornece apenas uma rigidez
de volume rank-one. Portanto, a igualdade constitutiva não decorre da
expressão escalar atualmente disponível; ver
`q29/segunda_variacao_transgressao_q40.md`.
