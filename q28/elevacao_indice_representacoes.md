# Q28 — Elevação do índice local às representações de cor e isospin

## 1. Separação entre geração e hipercarga

O protótipo local produziu

$$
\operatorname{ind}_{\rm APS}D_{1,B}^+=1
$$

a partir da linha de Hopf da fatia normal do estômato. Denote essa linha por

$$
L_G,
$$

onde o índice $G$ significa **geracional/geométrico**, não hipercarga.

Ela não deve ser identificada automaticamente com

$$
L_Y.
$$

Se a mesma linha de fluxo fosse usada como hipercarga, o operador acoplado a
uma potência $L_Y^q$ teria índice proporcional ao peso $q$. Os multipletos de
hipercargas diferentes receberiam multiplicidades quirais diferentes, em
conflito com a existência de uma cópia completa da geração.

Assim, a estrutura correta é

$$
\boxed{
\text{multiplicidade geracional}:L_G,
\qquad
\text{representação de gauge}:E_C\oplus E_W\oplus L_Y.
}
$$

Isso não introduz um novo grupo de gauge. $L_G$ é a linha de índice da
geometria normal; $L_Y$ é parte do fibrado interno físico.

## 2. Índice com coeficientes em uma representação

Se $V_R$ é o espaço de uma representação $R$ e sua conexão é topologicamente
trivial no preenchimento local $B^4$, então

$$
D_{G,R}
=D_G\otimes I_{V_R}
$$

e o índice no anel de representações é

$$
\boxed{
\operatorname{Ind}_{G_{\rm gauge}}(D_{G,R}^+)
=\operatorname{ind}(D_G^+)\,[R]
=[R].
}
$$

O índice ordinário, que conta componentes complexas, é

$$
\operatorname{ind}(D_{G,R}^+)=\dim R.
$$

Portanto, “índice 2” para um dubleto não significa duas gerações: significa
uma geração na representação bidimensional.

## 3. Setor fraco

Para

$$
E_W\simeq\mathbb C^2,
$$

segue

$$
\operatorname{Ind}_{SU(2)}(D_G^+\otimes E_W)
=[\mathbf2],
$$

e

$$
\operatorname{ind}(D_G^+\otimes E_W)=2.
$$

Isso produz um dubleto quiral, não dois singletos escolhidos separadamente.

## 4. Setor de cor

Para

$$
E_C\simeq\mathbb C^3,
$$

temos

$$
\operatorname{Ind}_{SU(3)}(D_G^+\otimes E_C)
=[\mathbf3],
$$

e

$$
\operatorname{ind}(D_G^+\otimes E_C)=3.
$$

Para o dual,

$$
\operatorname{Ind}_{SU(3)}(D_G^+\otimes E_C^*)
=[\bar{\mathbf3}].
$$

O índice local não escolhe entre $mathbf3$ e $\bar{\mathbf3}$; essa escolha
vem da orientação/conjugação do fibrado físico.

## 5. Produto cor--fraco

Para o produto tensorial,

$$
E_C\otimes E_W\simeq\mathbb C^6,
$$

segue

$$
\boxed{
\operatorname{Ind}_{SU(3)\times SU(2)}
(D_G^+\otimes E_C\otimes E_W)
=[(\mathbf3,\mathbf2)].
}
$$

O índice ordinário é seis, exatamente o número de componentes internas de um
único multiplet $(3,2)$.

## 6. Uma geração como classe virtual

Supondo já demonstrada a estrutura global do fibrado físico, sua classe de
uma geração é

$$
\mathcal E_{\rm gen}
=
(E_C\otimes E_W\otimes L_Y^{1/6})
\oplus
(E_C^*\otimes L_Y^{-2/3})
$$

$$
\oplus
(E_C^*\otimes L_Y^{1/3})
\oplus
(E_W\otimes L_Y^{-1/2})
\oplus
L_Y.
$$

Como $L_G$ fornece índice unitário comum,

$$
\boxed{
\operatorname{Ind}_{G_{\rm gauge}}
(D_G^+\otimes\mathcal E_{\rm gen})
=\mathcal E_{\rm gen}.
}
$$

Para $N_G$ estômatos orientados equivalentes,

$$
\operatorname{Ind}_{G_{\rm gauge}}
=N_G\mathcal E_{\rm gen}.
$$

Se, e somente se,

$$
N_G=3,
$$

obtemos

$$
\operatorname{Ind}_{G_{\rm gauge}}
=3\mathcal E_{\rm gen}.
$$

## 7. O que foi calculado e o que permanece condicional

Foi calculado:

1. índice local unitário de $L_G$;
2. elevação multiplicativa a $E_W$, $E_C$ e $E_C\otimes E_W$;
3. distinção entre multiplicidade de componentes e multiplicidade de
   gerações;
4. necessidade de separar $L_G$ de $L_Y$.

Permanece condicional:

1. derivar exatamente três estômatos geracionais estáveis;
2. derivar a classe física $\mathcal E_{\rm gen}$ sem usar a tabela alvo;
3. construir globalmente as potências fracionárias de $L_Y$ pelo quociente
   $\mathbb Z_6$;
4. calcular classes não abelianas quando as conexões de $E_C$ e $E_W$ não são
   localmente triviais.

## 8. Status

$$
\boxed{
\text{índice local elevado a }SU(2)\text{ e }SU(3)
\text{ no anel de representações.}
$$

O próximo passo é construir rigorosamente o quociente $\mathbb Z_6$ e mostrar
como as hipercargas fracionárias correspondem a representações honestas do
grupo global, não a potências fracionárias isoladas de uma linha.
