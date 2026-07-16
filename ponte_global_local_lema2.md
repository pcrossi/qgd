# Ponte global--local da GDQ — Lema 2: convergência geométrica apontada

> [!important] Atualização arquitetural
> Este lema é agora aplicado diretamente, sem interface entre backgrounds.
> Ver `ponte_global_local_lemas_sem_colar.md`.

## 1. Enunciado preciso

Considere

$$
M_\varepsilon
=T^4\times S^1_{L_\varepsilon}\times S^3_{R_\varepsilon},
$$

com

$$
L_\varepsilon,R_\varepsilon\longrightarrow\infty,
\qquad
0<c_-\leq\frac{L_\varepsilon}{R_\varepsilon}\leq c_+<\infty.
$$

Fixe um ponto-base $p_\varepsilon=(p_T,p_1,p_3)$ e a métrica produto
$g_\varepsilon^{(0)}$ do Lema 1A. Então, para todo compacto

$$
K\Subset T^4\times\mathbb R\times\mathbb R^3,
$$

existem, para $\varepsilon$ suficientemente pequeno, imersões apontadas

$$
\iota_\varepsilon:K\longrightarrow M_\varepsilon
$$

tais que

$$
\iota_\varepsilon^*g_\varepsilon^{(0)}
\longrightarrow g_{T^4}+ds^2+g_{\mathbb R^3}
$$

em $C^k(K)$ para todo $k$ finito. Portanto,

$$
\boxed{
(M_\varepsilon,g_\varepsilon^{(0)},p_\varepsilon)
\longrightarrow
(T^4\times\mathbb R^4,g_P,p_P)
}
$$

em convergência suave apontada de Cheeger--Gromov.

Esse enunciado não afirma equivalência topológica global entre os espaços.

## 2. Abertura do círculo

Escreva a métrica do círculo como

$$
g_{S^1_L}=L^2d\vartheta^2,
\qquad \vartheta\sim\vartheta+2\pi.
$$

Para um intervalo compacto $|s|\leq A$, defina

$$
\vartheta=\frac{s}{L}.
$$

Se $L>A/\pi$, essa carta não se sobrepõe consigo mesma e

$$
L^2d\vartheta^2=ds^2
$$

exatamente. Logo, a contribuição do círculo não possui erro métrico local;
apenas o tamanho da carta cresce com $L$.

## 3. Abertura da esfera

Use coordenadas geodésicas polares em $S^3_R$ em torno de $p_3$:

$$
g_{S^3_R}
=dr^2+R^2\sin^2\left(\frac rR\right)g_{S^2(1)},
\qquad 0\leq r<\pi R.
$$

Em qualquer bola fixa $0\leq r\leq A$,

$$
R\sin\left(\frac rR\right)
=r-\frac{r^3}{6R^2}+O_A(R^{-4}),
$$

e, portanto,

$$
R^2\sin^2\left(\frac rR\right)
=r^2-\frac{r^4}{3R^2}+O_A(R^{-4}).
$$

Como

$$
g_{\mathbb R^3}=dr^2+r^2g_{S^2(1)},
$$

segue a estimativa em coordenadas normais

$$
\left\|
\exp_{p_3}^*g_{S^3_R}-g_{\mathbb R^3}
\right\|_{C^k(B_A)}
\leq C_{A,k}R^{-2}.
$$

A aparente singularidade das coordenadas polares em $r=0$ é apenas
coordenada. Em coordenadas normais cartesianas, a mesma estimativa decorre da
expansão

$$
g_{ij}(x)
=\delta_{ij}-\frac13R_{ikjl}(p_3)x^kx^l+O(|x|^3R^{-3}),
$$

pois a curvatura seccional da esfera é $R^{-2}$ e suas derivadas covariantes
se anulam.

## 4. Imersões apontadas

Para

$$
K\subset T^4\times[-A,A]\times\overline{B_A(0)},
$$

defina

$$
\iota_\varepsilon(y,s,x)
=\left(
y,
\exp_{p_1}(s/L_\varepsilon),
\exp_{p_3}(x)
\right),
$$

onde, no último fator, $x$ é identificado com um vetor tangente de comprimento
físico em $T_{p_3}S^3_{R_\varepsilon}$. Para

$$
A<\min(\pi L_\varepsilon,\pi R_\varepsilon),
$$

a aplicação é injetiva no setor não toroidal e preserva o ponto-base. Pelas
Seções 2 e 3,

$$
\left\|
\iota_\varepsilon^*g_\varepsilon^{(0)}-g_P
\right\|_{C^k(K)}
\leq C_{K,k}R_\varepsilon^{-2}.
$$

Na escolha isotrópica $L_\varepsilon=R_\varepsilon=\varepsilon^{-1}$,

$$
\boxed{
\left\|
\iota_\varepsilon^*g_\varepsilon^{(0)}-g_P
\right\|_{C^k(K)}
\leq C_{K,k}\varepsilon^2.
}
$$

## 5. Curvatura e raio de injetividade

No produto homogêneo,

$$
|\operatorname{Rm}(g_\varepsilon^{(0)})|
=O(R_\varepsilon^{-2}),
$$

e

$$
|\nabla^m\operatorname{Rm}(g_\varepsilon^{(0)})|
=0
$$

nos fatores redondos, salvo a identificação trivial com o produto. O raio de
injetividade no ponto-base é

$$
\operatorname{inj}_{g_\varepsilon^{(0)}}(p_\varepsilon)
=\min\left{
\operatorname{inj}(T^4),
\pi L_\varepsilon,
\pi R_\varepsilon
\right}.
$$

Assim, ele permanece limitado inferiormente por uma constante positiva e,
nos quatro fatores que se abrem, cresce sem limite. O $T^4$ não se abre e
permanece exatamente como o fator compacto do bulk oficial.

## 6. Potenciais radiais

O mesmo limite geométrico transporta o Green radial global. Fora do polo,

$$
V_\varepsilon(r)
=qR_\varepsilon^{-1}
\cot\left(\frac r{R_\varepsilon}\right)
$$

satisfaz, em compactos afastados do núcleo,

$$
V_\varepsilon(r)
=\frac qr-\frac{qr}{3R_\varepsilon^2}
+O_K(R_\varepsilon^{-4}).
$$

Portanto, $V_\varepsilon\to q/r$ em $C^{k,\alpha}_{\rm loc}$ fora da fonte.
No núcleo, a convergência pertence ao domínio do operador com interface e não
ao espaço de funções suaves.

## 7. Inclusão de uma deformação localizada

Escreva

$$
g_\varepsilon
=g_\varepsilon^{(0)}+k_\varepsilon^{\rm st}.
$$

Suponha que, após pullback pelas cartas acima:

1. $k_\varepsilon^{\rm st}$ tenha suporte numa vizinhança física de raio
   uniforme do estômato;
2. para algum $k\geq2$ e $0<\alpha<1$,

   $$
   \iota_\varepsilon^*k_\varepsilon^{\rm st}
   \longrightarrow k_P^{\rm st}
   \quad\text{em }C^{k,\alpha}_{\rm loc};
   $$

3. exista $\lambda_*>0$ tal que

   $$
   g_\varepsilon^{(0)}+k_\varepsilon^{\rm st}
   \geq\lambda_*g_\varepsilon^{(0)};
   $$

4. as condições de interface em $r=r_c$ convirjam no mesmo sistema de
   coordenadas.

Então

$$
\iota_\varepsilon^*g_\varepsilon
\longrightarrow g_P+k_P^{\rm st}
$$

em $C^{k,\alpha}_{\rm loc}$. Essa proposição é uma consequência direta da
convergência do background e da deformação; ela não prova que
$k_\varepsilon^{\rm st}$ satisfaz a ação oficial. A existência variacional
dessa família é precisamente a pendência remanescente do Lema 1B.

## 8. Por que Hölder e $L^2$ aparecem em lugares diferentes

A convergência geométrica e o transporte dos coeficientes dos operadores
requerem controle local em espaços de Hölder:

$$
g_\varepsilon,J_\varepsilon,H_\varepsilon,f_\varepsilon
\quad\text{em}\quad C^{k,\alpha}_{\rm loc}.
$$

Os domínios dos operadores elípticos serão espaços de Sobolev ponderados, e a
teoria espectral viverá em

$$
L^2(M_\varepsilon,E_\varepsilon,
\mathcal U_\varepsilon d\operatorname{vol}_{g_\varepsilon}).
$$

Logo, a condição de Hölder não substitui $L^2$. Ela controla os coeficientes,
os produtos não lineares e a regularidade; $L^2$ controla normalização,
autoadjunticidade, resolventes e projetores espectrais.

## 9. Resultado e status

### Demonstrado

1. A família homogênea converge suavemente e de modo apontado para
   $T^4\times\mathbb R^4$.
2. O erro métrico em compactos é $O(R_\varepsilon^{-2})$.
3. Há controle uniforme de curvatura e raio de injetividade.
4. O potencial cotangente converge para o potencial $1/r$ fora da fonte.
5. Foi formulado o critério suficiente para transportar uma deformação
   localizada.

### Condicional ao Lema 1B

A convergência do background físico completo com carga de estômato depende da
existência e das estimativas uniformes da sela bulk--interface.

### Status

$$
\boxed{
\text{Lema 2A homogêneo: demonstrado;}
\qquad
\text{Lema 2B localizado: condicional ao Lema 1B.}
}
$$

O próximo lema deve transportar $J,H,f,\mathcal U$ e a Hessiana oficial nos
espaços funcionais aqui definidos.
