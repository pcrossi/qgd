# Q28 — Auditoria das identidades de localização para $k=3$

## 1. Objetivo

Depois das reduções anteriores,

$$
A=6k,
\qquad
N_G=k.
$$

O objetivo é verificar se o background cosmológico suave já contém uma
identidade que obrigue $k=3$.

## 2. Poincaré--Hopf no espaço fechado

Para uma seção vetorial com zeros isolados em uma variedade fechada,

$$
\sum_p\operatorname{ind}_p(X)=\chi(M).
$$

Como

$$
\chi(T^5\times S^3)
=\chi(T^5)\chi(S^3)
=0,
$$

segue

$$
\boxed{
\sum_p\operatorname{ind}_p(X)=0.
}
$$

Logo, o índice de zeros de um campo global suave no produto fechado não pode
fornecer $k=3$.

## 3. Localização no ciclo térmico

Uma função suave periódica em $S^1_\beta$ possui pontos críticos alternados.
Para um campo gradiente genérico,

$$
\sum_{p\in S^1_\beta}\operatorname{ind}_p(\nabla h)
=\chi(S^1)=0.
$$

Assim, a temperatura ou periodicidade térmica escolhe a direção $e^5$, mas
não produz três unidades líquidas de carga.

## 4. Soma de resíduos

Numa compactificação complexa sem bordo, o teorema global dos resíduos impõe

$$
\sum_p\operatorname{Res}_p\omega=0.
$$

É possível ter três resíduos positivos locais somente se houver uma
contribuição compensadora, por exemplo um polo no infinito, uma fronteira ou
uma punção cosmológica com resíduo total negativo. Portanto, escrever três
estômatos sem calcular o termo compensador não constitui uma localização
global de $k=3$.

## 5. Geometrização de Perelman

O número três não é fornecido pela geometrização. Em particular:

1. a dimensão da variedade é três;
2. as geometrias homogêneas de Thurston não formam um conjunto de três;
3. cirurgia admite números variáveis de necks e componentes;
4. Perelman controla evolução, não colapso e estabilidade por setor, mas não
   fixa a carga inicial $k$.

Logo,

$$
\boxed{
\text{dimensão }3\not\Rightarrow k=3.
}
$$

A afirmação histórica da Nota 29.2 de que Perelman classificaria exatamente
três classes estáveis não pode ser usada como teorema de contagem.

## 6. Transgressão no produto suave

Para uma família de conexões $\mathcal A(\tau)$ que permanece no mesmo
fibrado,

$$
\frac{d}{d\tau}c_2(E_{\mathcal A(\tau)})=0
$$

em cohomologia. A transgressão altera o representante por uma forma exata,
mas não muda $k$. Portanto, a dinâmica suave da ação oficial conserva a
carga e não seleciona seu valor inicial.

## 7. Única localização ainda admissível: problema relativo

Considere um cobordismo cosmológico $W_9$ entre duas fatias

$$
M_8^-
\quad\text{e}\quad
M_8^+,
$$

permitindo singularidades cirúrgicas isoladas. Para uma família de operadores
de fronteira $D_\tau$, a fórmula APS relativa tem a forma

$$
\operatorname{SF}(D_\tau)
=\operatorname{Ind}_{\rm APS}(\mathscr D_{W_9})
=\int_{W_9}\mathcal I_9
-\frac{\eta_+-\eta_-}{2},
$$

com as correções de modos zero apropriadas. A mudança da carga satisfaria

$$
\boxed{
k_+-k_-=\operatorname{SF}(D_\tau).
}
$$

Se o estado inicial for topologicamente trivial,

$$
k_-=0,
$$

então três gerações exigiriam demonstrar, sem usar o alvo, que

$$
\operatorname{SF}(D_\tau)=3.
$$

Essa formulação permite carga líquida não nula porque o problema possui duas
fronteiras e atravessa eventos de cirurgia. Ela não contradiz os teoremas de
soma zero do espaço fechado.

## 8. Dados necessários para calcular o fluxo espectral

O cálculo exige:

1. um cobordismo $W_9$ explicitamente definido pela história cosmológica;
2. a conexão de Bismut e o dilatão estacionário em cada extremo;
3. o operador tangencial $D_\tau$ derivado da Hessiana oficial;
4. condições APS nas duas fronteiras;
5. a lista de instantes em que autovalores atravessam zero;
6. a multiplicidade e orientação de cada cruzamento.

Sem esses dados, declarar três cirurgias ou três cruzamentos apenas transfere
o número desejado para a hipótese.

## 9. Veredito

As três localizações naturais no background fechado dão

$$
\boxed{
\chi=0,
\qquad
\sum\operatorname{Res}=0,
\qquad
\Delta k_{\rm suave}=0.
}
$$

Portanto, o produto cosmológico suave não deriva $k=3$. A única rota ainda
compatível com a estrutura já construída é um índice APS **relativo** de uma
história cosmológica com cirurgia. O próximo cálculo deve construir
$W_9$ e seu operador tangencial; não deve voltar a minimizações locais nem à
contagem informal de três dimensões.

