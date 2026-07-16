# Q28 — Retroação anisotrópica do toro

## 1. Fluxos nos dois planos

Considere uma conexão no subgrupo de Cartan compatível com a colagem global,
com fluxos quantizados

$$
\frac{1}{2\pi}
\int_{T^2_{12}}F=n_{12},
\qquad
\frac{1}{2\pi}
\int_{T^2_{34}}F=n_{34}.
$$

Para comprimentos $L_i$, as componentes homogêneas são

$$
F_{12}=\frac{2\pi n_{12}}{L_1L_2},
\qquad
F_{34}=\frac{2\pi n_{34}}{L_3L_4}.
$$

Com a normalização do gerador absorvida em $\kappa_R$, a classe de grau quatro
é

$$
\boxed{
A=\kappa_R n_{12}n_{34}.
}
$$

## 2. Energia dependente da forma

Defina as áreas

$$
V_{12}=L_1L_2,
\qquad
V_{34}=L_3L_4,
$$

e a razão anisotrópica

$$
x=\frac{V_{34}}{V_{12}}>0.
$$

A forma quadrática induzida pela curvatura da ação oficial possui, a fatores
positivos comuns, a dependência

$$
E(x;n_{12},n_{34})
=C
\left(
n_{12}^2x
+\frac{n_{34}^2}{x}
\right).
$$

Sua equação variacional é

$$
\frac{dE}{dx}
=C\left(
n_{12}^2
-\frac{n_{34}^2}{x^2}
\right)=0.
$$

Portanto,

$$
\boxed{
x_*
=\left|\frac{n_{34}}{n_{12}}\right|.
}
$$

Essa é precisamente a condição de igualdade entre as magnitudes ortonormais
dos dois fluxos, isto é, a condição auto-dual ou anti-auto-dual.

## 3. Ação após eliminar a anisotropia

Substituindo $x_*$,

$$
\boxed{
E_{\rm on\mbox{-}shell}
=2C|n_{12}n_{34}|
=\frac{2C}{|\kappa_R|}|A|.
}
$$

A segunda derivada é

$$
\left.
\frac{d^2E}{dx^2}
\right|_{x_*}
=\frac{2C|n_{12}|^3}{|n_{34}|}>0,
$$

de modo que a forma do toro é estabilizada nesse ponto.

Contudo, depois de estabilizar a anisotropia, a ação continua linear em

$$
|A|.
$$

Logo, a retroação anisotrópica não cria um mínimo em $A=18$.

## 4. Quinto ciclo

O comprimento $L_5$ multiplica a ação reduzida e participa da normalização de
$\mathcal U$. No ansatz homogêneo, a normalização cancela esse fator de volume
na média, deixando apenas sua contribuição ao dilatão normalizado. Como não há
componente de curvatura envolvendo a quinta direção na classe $a_4$, variar
$L_5$ não altera a conclusão

$$
E_{\rm on\mbox{-}shell}\propto|A|.
$$

O quinto ciclo participa separadamente da colagem

$$
b_1\smile u_3,
$$

cujo winding mínimo já forneceu $\nu(g)=1$.

## 5. Dilatão não homogêneo

Para um peso positivo variável

$$
w(\theta)=r^5\mathcal U_B(\theta),
$$

vale o limite

$$
\int_{T^4}w\operatorname{tr}(F\wedge *_4F)
\ge
8\pi^2w_{\min}|A|.
$$

Um perfil não homogêneo pode deslocar ou localizar a densidade de Chern nas
regiões onde $w$ é menor. Mas, se $w$ for um background fixo independente de
$A$, o limite permanece monotônico em $|A|$.

Uma seleção interior só poderia surgir se a solução acoplada

$$
w=w_A
$$

gerasse uma dependência não monotônica suficientemente forte. Isso exige
resolver a equação conjugada do calor/dilatão com a fonte de curvatura, não
apenas escolher um perfil.

## 6. Resultado

$$
\boxed{
\text{a variação anisotrópica estabiliza a forma autodual, mas não seleciona
o número topológico }A=18.
}
$$

Com isso, os módulos homogêneos de raio e forma foram eliminados. A única
retroação contínua ainda capaz de modificar a monotonicidade é o perfil
espacial acoplado de $f$ e da medida $\mathcal U$.
