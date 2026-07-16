# Q37 — identificação da fórmula cosmológica com a Hessiana global

## 1. Enunciado

O objetivo é decidir se a expressão histórica

$$
\alpha_{\rm hist}
=\frac{9}{8\pi^4}
\left(\frac{\pi^5}{1920}\right)^{1/4}
$$

é uma escrita fechada do coeficiente eletromagnético produzido pela Hessiana
da ação oficial, ou apenas uma fórmula numericamente próxima.

Em unidades naturais, a identidade necessária é

$$
Z_Q^E
=\frac{1}{4\pi\alpha_{\rm hist}}
=10{,}904984951787\ldots.
$$

Nenhum valor experimental de $\alpha$ participa deste teste.

## 2. O que a ação oficial determina

Depois da normalização do gerador elétrico e da eliminação das flutuações
ortogonais, a Hessiana fornece

$$
Z_Q^E
=v^T
\left(
Z_{QQ}-Z_{Q\perp}Z_{\perp\perp}^{-1}Z_{\perp Q}
\right)v.
$$

No background radial já calculado, o canal neutro canonizado antes da colagem
tem

$$
K_0=15{,}162605758555\ldots.
$$

A colagem com o elo normal produz

$$
Z_Q^E
=\frac{K_0K_\partial}{K_0+K_\partial}.
$$

O DtN redondo sem ajuste, $K_\partial=\pi^2R^2$, fornece

$$
Z_{Q,{\rm red}}^E=10{,}950226282632\ldots,
$$

enquanto a identidade histórica exigiria

$$
K_{\partial,{\rm hist}}
=\frac{K_0Z_{Q,{\rm hist}}^E}{K_0-Z_{Q,{\rm hist}}^E}
=38{,}835771227928\ldots.
$$

Esta última equação é diagnóstica: ela não deriva $K_\partial$, apenas mostra
qual autovalor DtN faria as duas expressões coincidirem.

## 3. Identificação correta do inteiro 1920

Existe um grupo matemático natural de ordem $1920$:

$$
W(D_5)
\simeq
(\mathbb Z_2)^4\rtimes S_5,
\qquad
|W(D_5)|=2^4\,5!=1920.
$$

Ele age na rede de cinco ciclos por permutações assinadas com número par de
inversões. Portanto o inteiro não precisa ser tratado como uma cardinalidade
sem nome.

$W(D_5)$ é uma simetria finita da rede toroidal, não o grupo de holonomia da
conexão de Bismut. Chamar sua ordem de “ordem da holonomia” seria incorreto.

Isso, porém, não basta para colocá-lo na ação. O background cosmológico
$T^5\times S^3$ contém uma escolha axial que associa um ciclo de $T^5$ à
estrutura de Hopf de $S^3$. Essa escolha entra em $J$, em $H$ e no gerador
$Q$. Uma transformação de $W(D_5)$ que troca esse ciclo por outro não preserva
automaticamente o conjunto completo

$$
(g_*,J_*,H_*,f_*,\mathcal U_*,Q).
$$

O grupo que pode dividir a integral física é, no máximo, o estabilizador

$$
\Gamma_{\rm phys}
=\operatorname{Stab}_{W(D_5)}
(J_*,H_*,f_*,\mathcal U_*,Q),
$$

e não $W(D_5)$ por mera igualdade de ordem. Em particular, fixar um dos cinco
eixos reduz a parte de permutação de $5!$ para $4!$. O estabilizador de um eixo
orientado tem ordem $2^3 4!=192$; o estabilizador da linha não orientada tem
ordem $2^4 4!=384$. Logo a decomposição antiga

$$
4!\,2^4\,5=1920
$$

reintroduz por multiplicação o número de escolhas do eixo que o próprio
background já selecionou. Isso constitui dupla contagem, salvo prova de que
as cinco escolhas pertencem ao mesmo órbito físico e devem ser somadas, em vez
de identificadas.

## 4. Por que a raiz quarta não segue da ordem do grupo

Para um quociente livre por um grupo finito, uma integral volumétrica obedece

$$
\operatorname{Vol}(K/\Gamma)
=\frac{\operatorname{Vol}(K)}{|\Gamma|}.
$$

A Hessiana quadrática também recebe esse fator linear quando campo, medida e
gerador descem ao quociente. Ela não produz, apenas por quocientar, a raiz

$$
|\Gamma|^{-1/4}.
$$

Uma raiz quarta só pode aparecer se $C$ for definido como uma escala linear
associada a um volume efetivo de quatro dimensões,

$$
C^4=\operatorname{Vol}_4^{\rm eff},
$$

e depois for demonstrado que essa escala, e não o próprio volume, entra em
$Z_Q^E$. Essa passagem ainda não foi obtida da Hessiana oficial.

## 5. O fator $9/(8\pi^4)$

O fator histórico pode ser escrito como

$$
\frac{9}{8\pi^4}
=\frac{1}{2\pi^4}\left(\frac32\right)^2.
$$

Entretanto, a Hessiana não contém uma identidade universal que imponha a
razão de tensões $3/2$ em cada um de dois planos complexos. No cálculo
variacional vigente, os fatores legítimos são:

1. a norma do gerador, que já produziu o fator de Gram $1/4$;
2. o autovalor do DtN normal;
3. o complemento de Schur dos campos ortogonais;
4. a normalização da medida causal.

Substituir esses operadores por $(3/2)^2/2$ seria uma nova hipótese
constitutiva. Portanto $9/(8\pi^4)$ ainda não foi identificado como uma
contração da Hessiana.

## 6. Veredito

A fórmula histórica possui duas propriedades distintas:

1. é aritmeticamente correta e prevê um número extremamente próximo do valor
   observado;
2. não foi ainda demonstrada como identidade da Hessiana oficial.

O avanço desta auditoria é preciso:

- $1920$ admite a identificação algébrica $|W(D_5)|$;
- a identificação física exige calcular $\Gamma_{\rm phys}$, o estabilizador
  simultâneo de $J,H,f,\mathcal U$ e $Q$;
- a raiz quarta não decorre automaticamente do quociente;
- o fator $9/8$ não substitui o DtN e o complemento de Schur.

Assim, o ponto 3 não fecha a fórmula histórica como teorema. Ele reduz a
pendência à identidade espectral concreta

$$
\boxed{
K_{\partial}^{\rm WB}[Q]
=38{,}835771227928\ldots
}
$$

ou, preferencialmente, à obtenção simbólica desse autovalor sem usar o lado
direito como condição de ajuste. Até essa avaliação, a expressão histórica é
uma **conjectura geométrica fortemente corroborada pela estimativa DtN
redonda**, não uma derivação fechada.

## 7. Avaliação do refinamento warped disponível

É possível decidir sem um novo ajuste se o warp escalar já calculado pode
produzir a diferença. Na fatia normal real de dimensão quatro, mantendo fixa
a métrica induzida no bordo, escreva

$$
g_{\rm WB}=e^{2A(r)}g_{\rm red}.
$$

Para uma 2-forma $F$, a transformação conforme fornece

$$
\sqrt{g_{\rm WB}}=e^{4A}\sqrt{g_{\rm red}},
\qquad
F_{ab}F^{ab}_{\rm WB}=e^{-4A}F_{ab}F^{ab}_{\rm red}.
$$

Logo a forma quadrática fotônica é exatamente invariante:

$$
\int_{B^4}\sqrt{g_{\rm WB}}\,F_{ab}F^{ab}_{\rm WB}
=\int_{B^4}\sqrt{g_{\rm red}}\,F_{ab}F^{ab}_{\rm red}.
$$

O operador DtN pode mudar sua representação pontual sob uma redefinição da
normal unitária, mas a rigidez integrada que entra no complemento de Schur é
a mesma. Portanto

$$
\boxed{K_{\partial}^{\rm conformal}=\pi^2R^2.}
$$

A torção de Bismut também não corrige automaticamente esse termo. A curvatura
abeliana direta é $F=dA_Q$ e não usa a conexão afim. Na truncagem conformal
disponível, a dependência calculada é do tipo $Z(\eta)F^2$; em torno de
$A_Q=0$ ela começa na ordem $\eta A_Q^2$ e não gera bloco quadrático
escalar--fóton.

Essa conclusão não decorre apenas de Ward. Uma Hessiana torsional mais geral
poderia conter uma mistura gauge-invariante entre $F$ e uma 2-forma de
background. Esse bloco transversal não foi calculado e não pode ser declarado
nulo apenas pela simetria $U(1)_Q$.

Consequentemente, o warp conformal e a torção puramente axial já disponíveis
não transformam $39{,}415718607388\ldots$ em
$38{,}835771227928\ldots$. Uma correção legítima exigiria pelo menos um dos
seguintes dados, ainda não calculados no elo normal:

1. métrica Hermitiana anisotrópica, não conformal;
2. mistura cinética entre direções internas que preserve Ward, mas altere a
   matriz de Gram do gerador físico;
3. termo de interface transversal produzido pelo background completo.

Nenhum desses termos pode ser inferido do resíduo numérico.

## 8. Resultado final desta conta

Para a classe efetivamente avaliada — elo redondo ou conformalmente warped
com métrica induzida fixa, gerador canonizado e truncagem sem mistura
transversal — o resultado é

$$
\boxed{
K_\partial=39{,}415718607388\ldots,
\qquad
\alpha^{-1}=137{,}604601778653\ldots.
}
$$

Esse resultado é estável sob o refinamento conformal e não coincide com a
fórmula histórica. Portanto a conta está terminada para essa classe de
backgrounds, com resultado negativo. A previsão $137{,}036082448\ldots$ só
poderá ser reaberta por um background normal anisotrópico obtido da ação
oficial; não por um warp escalar.
