# Ponte global--local — operador DtN interno do estômato

## 1. Problema de interface

Separe a variedade por

$$
M=M_-\cup_YM_+,
\qquad
Y\simeq S^3,
$$

onde $M_-$ é a região interna do estômato e $M_+$ é o colar exterior. As
orientações dos normais satisfazem

$$
\nu_+=-\nu_-.
$$

Os dados de Dirichlet comuns são

$$
X_Y=(a_Y,c_Y,u_Y,v_Y).
$$

O DtN não linear deve associar a esses dados os momentos normais das soluções
on shell em cada lado.

## 2. Momentos derivados da ação oficial

Na notação

$$
\dot X=N^{-1}X',
$$

o funcional radial válido é

$$
I_\tau
=\int Ndr\,e^{-u}
\left\{
\tau\left[Q+4\frac{c^2}{a}\dot a+V\right]
+a^2c(u-4)
\right\},
$$

com

$$
Q
=4a\dot a\dot c-4ac\dot u\dot a-2a^2\dot u\dot c
+a^2c(\dot u^2+\dot v^2).
$$

Os momentos canônicos normais são, exatamente,

$$
\boxed{
\Pi_a
=\tau e^{-u}
\left(4a\dot c-4ac\dot u+4\frac{c^2}{a}\right),
}
$$

$$
\boxed{
\Pi_c
=\tau e^{-u}\left(4a\dot a-2a^2\dot u\right),
}
$$

$$
\boxed{
\Pi_u
=\tau e^{-u}
\left(-4ac\dot a-2a^2\dot c+2a^2c\dot u\right),
}
$$

$$
\boxed{
\Pi_v
=2\tau e^{-u}a^2c\dot v=j_v.
}
$$

Esses momentos, e não coeficientes Robin escolhidos externamente, são as
impedâncias fundamentais da interface.

## 3. Restrição de carga no espaço de traços

A torção de Bismut é

$$
H=h\,\sigma_1\wedge\sigma_2\wedge\sigma_3,
\qquad
h=2c(a\dot a-c).
$$

No bordo,

$$
Q_{\rm st}
=\frac{\mathcal V_\sigma}{2\pi}(h-h_{\rm bg})=q.
$$

Uma perturbação física deve satisfazer

$$
\delta h=0,
$$

isto é,

$$
\boxed{
2(a\dot a-2c)\,\delta c
+2c\dot a\,\delta a
+2ac\,\delta\dot a=0.
}
$$

Essa equação define o subespaço de traços de carga fixa. A carga não é
convertida num potencial ajustável.

## 4. DtN não linear

Para cada dado $X_Y$ admissível e para as cargas fixas $(h_0,j_v)$, resolva as
equações oficiais em $M_-$ com regularidade interna. Denote a solução por

$$
X_-[X_Y;h_0,j_v].
$$

O mapa DtN interno é

$$
\boxed{
\mathcal N_-(X_Y;h_0,j_v)
=\Pi_-[X_-[X_Y;h_0,j_v]]\big|_Y.
}
$$

Analogamente,

$$
\mathcal N_+(X_Y;h_0,j_v)
=\Pi_+[X_+[X_Y;h_0,j_v]]\big|_Y.
$$

Como os normais são opostos, a condição de colagem sem fonte material
independente é

$$
\boxed{
\mathcal N_-(X_Y;h_0,j_v)
+\mathcal N_+(X_Y;h_0,j_v)=0.
}
$$

Se existir uma fonte clássica externa na interface, seu momento aparece no
lado direito. Ela não pertence ao background livre.

## 5. Regularidade da região interna

Há duas possibilidades topologicamente distintas.

### 5.1 Preenchimento suave

Se $M_-$ contém um centro regular modelado em $\mathbb C^2$, então, numa
coordenada própria $s\to0$,

$$
a(s)=s+O(s^3),
\qquad
c(s)=s+O(s^3),
$$

$$
u(s)=u_0+O(s^2),
\qquad
v(s)=v_0+O(s^2).
$$

Consequentemente,

$$
h(s)=2c(a\dot a-c)=O(s^4)\longrightarrow0.
$$

Com $dh=0$, segue $h\equiv0$. Portanto, um preenchimento suave strong-KT não
suporta carga relativa não nula.

### 5.2 Núcleo excisado

Para $q\neq0$, a região física não pode ser um preenchimento suave strong-KT
até $s=0$. O estômato é um bordo interno/excisão ou requer uma fonte
topológica de transgressão. Nesse caso, os dados internos são impostos numa
segunda seção $Y_0$ e transportados até $Y$ pela mesma ação.

Esse resultado fixa a topologia do problema:

$$
\boxed{
q\neq0
\quad\Longrightarrow\quad
\text{DtN de anel/colo interno, não DtN da bola suave }B^4.
}
$$

## 6. DtN linearizado

Seja $X_*$ uma solução interna. Para um traço $\eta_Y$, resolva o problema de
Jacobi

$$
K_-\eta_-=0
$$

em $M_-$, com regularidade na segunda ponta e

$$
\eta_-|_Y=\eta_Y,
\qquad
\delta h=0,
\qquad
\delta j_v=0.
$$

O operador DtN linearizado é

$$
\boxed{
\Lambda_-\eta_Y
=\delta\Pi_-[\eta_-]\big|_Y
=D\mathcal N_-(X_{Y,*})\eta_Y.
}
$$

Ele também é a Hessiana da ação interna on shell:

$$
\Lambda_-
=D^2S_-^{\rm on\mbox{-}shell}(X_{Y,*}).
$$

Pela identidade de Green, $\Lambda_-$ é simétrico no espaço de traços
físicos, desde que a realização interna seja auto-adjunta.

## 7. Forma por matriz fundamental

Escreva o sistema de Jacobi de primeira ordem como

$$
\frac d{ds}
\begin{pmatrix}\eta\\\pi\end{pmatrix}
=
\begin{pmatrix}
\mathsf A&\mathsf B\\
\mathsf C&-\mathsf A^\dagger
\end{pmatrix}
\begin{pmatrix}\eta\\\pi\end{pmatrix}.
$$

Se a matriz fundamental física entre $Y_0$ e $Y$ é

$$
\mathsf T_-
=\begin{pmatrix}
T_{11}&T_{12}\\
T_{21}&T_{22}
\end{pmatrix},
$$

e a condição regular na segunda ponta é

$$
\pi_0=R_0\eta_0,
$$

então

$$
\boxed{
\Lambda_-
=(T_{21}+T_{22}R_0)
(T_{11}+T_{12}R_0)^{-1}.
}
$$

Essa fórmula é calculável assim que o background interno for obtido. Ela não
contém parâmetros de Robin livres.

## 8. Operador de interface e projetor físico

O operador espectral colado contém

$$
\boxed{
\Lambda_{\rm glue}
=\Lambda_-+\Lambda_+.
}
$$

O espaço de traços físico é

$$
\mathcal T^{\rm phys}
=\ker DQ_{\rm st}\cap\ker Dj_v
\cap(\text{modos de Noether})^\perp.
$$

Se $P_Y^{\rm phys}$ é a projeção sobre esse espaço, a condição relevante para
o gap de interface é

$$
P_Y^{\rm phys}\Lambda_{\rm glue}P_Y^{\rm phys}>0
$$

no complemento dos zeros exatos.

## 9. Resultado

O DtN interno foi derivado da ação oficial em forma não linear e linearizada.
Também foi demonstrado que uma carga strong-KT não nula exclui o preenchimento
suave por $B^4$: o interior correto é um colo excisado ou uma transgressão
topológica explicitamente derivada.

O cálculo numérico de $\Lambda_-$ requer agora apenas a escolha entre essas
duas topologias e os dados conservados na segunda ponta. Sem essa escolha, não
existe um único DtN numérico bem definido.

## 10. Seleção sem nova fonte: colo mínimo refletido

Para não introduzir uma transgressão fundamental adicional, escolha a rota do
colo excisado. Seja $Y_0\simeq S^3$ a seção mínima do colo e escolha a
coordenada própria $s$ com $s=0$ em $Y_0$.

A minimalidade na direção equatorial impõe

$$
\dot a(0)=0.
$$

Pela conservação de fluxo,

$$
h_0=2c_0(a_0\dot a_0-c_0),
$$

portanto

$$
\boxed{
h_0=-2c_0^2.
}
$$

Com a orientação oposta do normal, o sinal orientado de $h_0$ muda, mas o
raio não. Como

$$
h_0-h_{\rm bg}
=\frac{2\pi q}{\mathcal V_\sigma},
$$

segue

$$
\boxed{
c_0^2
=\frac12\left|
h_{\rm bg}+\frac{2\pi q}{\mathcal V_\sigma}
\right|.
}
$$

Se a seção mínima preserva a isotropia $SU(2)$ antes da deformação exterior,
então

$$
a_0=c_0.
$$

Essa igualdade é uma condição geométrica do colo redondo, não consequência
da quantização. Uma garganta de Berger exigiria determinar separadamente
$a_0/c_0$ pela equação métrica tangencial.

Para um colo refletido e sem fonte clássica na seção mínima,

$$
\dot c(0)=0,
\qquad
\dot u(0)=0.
$$

A fase pode carregar circulação conservada,

$$
\dot v(0)
=\frac{j_ve^{u_0}}{2\tau a_0^2c_0}.
$$

Os momentos na garganta são então

$$
\Pi_a(0)=4\tau e^{-u_0}\frac{c_0^2}{a_0},
$$

$$
\Pi_c(0)=0,
\qquad
\Pi_u(0)=0,
\qquad
\Pi_v(0)=j_v.
$$

Esses dados determinam $R_0$ no problema linear e eliminam coeficientes Robin
arbitrários.

### Condição de consistência

A restrição do lapse também deve valer em $s=0$. Como

$$
\dot a_0=\dot c_0=\dot u_0=0,
$$

ela fornece

$$
-\tau a_0^2c_0\dot v_0^2
+\tau\left(8c_0-4\frac{c_0^3}{a_0^2}\right)
+a_0^2c_0(u_0-4)=0.
$$

No colo redondo $a_0=c_0=r_0$,

$$
\boxed{
u_0
=4-\frac{4\tau}{r_0^2}+\tau\dot v_0^2.
}
$$

Juntamente com a corrente conservada,

$$
\dot v_0
=\frac{j_ve^{u_0}}{2\tau r_0^3},
$$

essa é uma equação escalar para $u_0$. Logo os dados iniciais internos são
determinados por $(q,j_v,\tau,h_{\rm bg})$, salvo existência e possível
multiplicidade das raízes dessa equação.

### Novo status do DtN

Na rota do colo mínimo redondo, o DtN interno deixou de depender de dados
Robin livres. Falta:

1. provar existência da raiz admissível para $u_0$;
2. integrar o sistema oficial até $Y$;
3. linearizar essa solução para obter numericamente $\Lambda_-$.

## 11. Existência do dado inicial $u_0$

Defina

$$
A_0=4-\frac{4\tau}{r_0^2},
\qquad
B_0=\frac{j_v^2}{4\tau r_0^6}\geq0.
$$

A equação da garganta é

$$
u_0=A_0+B_0e^{2u_0}.
$$

Para $j_v=0$, existe a solução única

$$
u_0=A_0.
$$

Para $j_v\neq0$, considere

$$
F(u)=u-A_0-B_0e^{2u}.
$$

Seu máximo ocorre em

$$
e^{2u_m}=\frac1{2B_0},
$$

e vale

$$
F(u_m)
=\frac12\log\frac1{2B_0}-A_0-\frac12.
$$

Logo existe ao menos uma raiz real se e somente se

$$
\boxed{
B_0\leq\frac12e^{-2A_0-1}.
}
$$

Em termos da corrente,

$$
\boxed{
j_v^2
\leq2\tau r_0^6
\exp\left(-9+\frac{8\tau}{r_0^2}\right).
}
$$

Na desigualdade estrita existem duas raízes. A raiz inferior satisfaz

$$
2B_0e^{2u_0}<1,
$$

enquanto a superior satisfaz a desigualdade oposta. A igualdade crítica
produz uma raiz dupla e um zero no linearizado escalar; portanto não pode
fornecer gap uniforme.

Assim, para a continuação espectral deve-se selecionar a raiz inferior e
exigir margem uniforme

$$
1-2B_0e^{2u_0}\geq\delta_u>0.
$$

Esse é o primeiro gap local, obtido antes da integração do colo.

## 12. Implementação variacional correta do fluxo fixo

Substituir $\dot a=A(a,c;h_0)$ diretamente no funcional antes da variação
pode perder a equação conjugada à carga. A implementação equivalente e
variacionalmente segura usa um multiplicador local $\beta(s)$:

$$
I_{\rm aug}
=I_\tau
+\int ds\,\beta(s)
\left[2c(a\dot a-c)-h_0\right].
$$

$\beta$ não é um novo campo fundamental. Ele é eliminado ao final e funciona
como tensão conjugada ao fluxo conservado.

A variação em $\beta$ devolve

$$
2c(a\dot a-c)=h_0.
$$

Os momentos vinculados corretos são

$$
\boxed{
\widetilde\Pi_a
=\Pi_a+2\beta ac,
}
$$

$$
\widetilde\Pi_c=\Pi_c,
\qquad
\widetilde\Pi_u=\Pi_u,
\qquad
\widetilde\Pi_v=\Pi_v,
$$

pois o vínculo contém $\dot a$, mas não contém $\dot c$, $\dot u$ ou
$\dot v$.

Consequentemente, a condição de colagem correta é

$$
\widetilde{\mathcal N}_-
+\widetilde{\mathcal N}_+=0.
$$

O termo $2\beta ac$ desaparece apenas se a solução determinar $\beta=0$ no
bordo; isso não pode ser presumido.

## 13. Sistema diferencial--algébrico do colo

Defina

$$
X=(a,c,u,v),
$$

e

$$
\mathscr L_{\rm aug}(X,\dot X,\beta,N)
=\mathscr L_{\rm GDQ}
+\beta\left[2c(a\dot a-c)-h_0\right].
$$

O background interno é determinado por

$$
\frac d{ds}
\frac{\partial\mathscr L_{\rm aug}}{\partial\dot X^A}
-\frac{\partial\mathscr L_{\rm aug}}{\partial X^A}=0,
$$

$$
\frac{\partial\mathscr L_{\rm aug}}{\partial\beta}=0,
$$

$$
\frac{\partial\mathscr L_{\rm aug}}{\partial N}=0,
$$

mais a normalização global. Depois de variar, escolhe-se $N=1$.

Em forma de primeira ordem, use

$$
Y=(a,c,u,v,\widetilde\Pi_a,Pi_c,Pi_u,Pi_v,\beta).
$$

As quatro relações momento--velocidade, o vínculo de fluxo e a restrição do
lapse formam o bloco algébrico. As quatro equações de Euler--Lagrange formam o
bloco diferencial. A corrente de fase reduz uma delas a

$$
\dot\Pi_v=0.
$$

Esse DAE é de índice um sempre que a Jacobiana do bloco algébrico em relação
a $(\dot X,\beta,N)$ é inversível no espaço físico. A perda dessa
invertibilidade é exatamente uma bifurcação/zero da Hessiana, não um problema
que possa ser removido numericamente.

## 14. DtN linearizado com o multiplicador

As perturbações agora incluem $\delta\beta$. O sistema de Jacobi vinculado é

$$
\begin{pmatrix}
K_{XX}&C_h^\dagger\\
C_h&0
\end{pmatrix}
\begin{pmatrix}
\eta\\
\delta\beta
\end{pmatrix}=0,
$$

onde

$$
C_h\eta
=\delta\left[2c(a\dot a-c)-h_0\right].
$$

Eliminando $\delta\beta$ no complemento da restrição, obtém-se a Hessiana
física do setor de carga fixa. O DtN linearizado é calculado com o momento
$\delta\widetilde\Pi_a$, não com $\delta\Pi_a$ isolado.

Essa correção completa a formulação variacional necessária para integrar o
colo sem tratar a conservação como substituição ad hoc.

## 15. Eliminação exata do bloco algébrico

Denote os momentos vinculados por

$$
(p_a,p_c,p_u,p_v)
=(\widetilde\Pi_a,\Pi_c,\Pi_u,\Pi_v).
$$

As relações momento--velocidade e o vínculo de fluxo podem ser invertidos
algebricamente. O multiplicador é

$$
\boxed{
\beta
=\frac{
a p_a e^u+4c^2\tau+4h_0\tau+2p_u e^u
}{2a^2c e^u}.
}
$$

As velocidades físicas tornam-se

$$
\boxed{
\dot a=\frac{2c^2+h_0}{2ac},
}
$$

$$
\boxed{
\dot c
=-\frac{(cp_c+p_u)e^u}{2a^2\tau},
}
$$

$$
\boxed{
\dot u
=\frac{4c^2\tau-cp_c e^u+2h_0\tau}
{2a^2c\tau},
}
$$

$$
\boxed{
\dot v
=\frac{p_v e^u}{2a^2c\tau},
\qquad
\dot p_v=0.
}
$$

A restrição do lapse recebe também a contribuição do multiplicador. Em
coordenada arbitrária, o termo vinculado é

$$
\beta\left[2caa'-N(2c^2+h_0)\right],
$$

de modo que a variação em $N$ contém
$-\beta(2c^2+h_0)$. Depois da eliminação algébrica, a restrição correta é

$$
\boxed{
\begin{aligned}
\mathscr H={}&
4a^4c^2\tau(u-4)
+32a^2c^2\tau^2
-4ac^2p_a\tau e^u-2ah_0p_a\tau e^u\\
&-16c^4\tau^2-8c^2h_0\tau^2
-4h_0^2\tau^2+c^2p_c^2e^{2u}\\
&-8c^2p_u\tau e^u+2cp_cp_u e^{2u}
-4h_0p_u\tau e^u-p_v^2e^{2u}=0,
\end{aligned}
}
$$

após remover o denominador positivo comum $4a^2c\tau$.

Na garganta mínima, $2c_0^2+h_0=0$; por isso a parcela de $\beta$ desaparece
e a equação escalar de $u_0$ derivada anteriormente permanece inalterada.

Os três momentos restantes obedecem a

$$
\boxed{
\begin{aligned}
\dot p_a={e^{-u}\over2a^3c\tau}\Big[&
4a^4c^2\tau(u-4)
+2ac^2p_a\tau e^u+ah_0p_a\tau e^u\\
&+16c^4\tau^2+8c^2h_0\tau^2
-c^2p_c^2e^{2u}+8c^2p_u\tau e^u\\
&-2cp_cp_u e^{2u}+4h_0^2\tau^2
+4h_0p_u\tau e^u+p_v^2e^{2u}
\Big],
\end{aligned}
}
$$

$$
\boxed{
\begin{aligned}
\dot p_c={e^{-u}\over4a^2c^2\tau}\Big[&
4a^4c^2\tau(u-4)+32a^2c^2\tau^2
-4ac^2p_a\tau e^u\\
&+2ah_0p_a\tau e^u-48c^4\tau^2
-8c^2h_0\tau^2+c^2p_c^2e^{2u}\\
&-8c^2p_u\tau e^u+4h_0^2\tau^2
+4h_0p_u\tau e^u+p_v^2e^{2u}
\Big],
\end{aligned}
}
$$

$$
\boxed{
\begin{aligned}
\dot p_u=-{e^{-u}\over4a^2c\tau}\Big[&
4a^4c^2\tau(u-5)+32a^2c^2\tau^2
-16c^4\tau^2-8c^2h_0\tau^2\\
&-c^2p_c^2e^{2u}-2cp_cp_u e^{2u}
-4h_0^2\tau^2+p_v^2e^{2u}
\Big].
\end{aligned}
}
$$

Essas equações são a forma explícita do problema interno em gauge própria.
Não contêm coeficientes fenomenológicos.

## 16. Dados iniciais e único parâmetro de tiro interno

No colo redondo mínimo,

$$
a_0=c_0=r_0,
\qquad
h_0=-2r_0^2,
$$

$$
p_{c,0}=p_{u,0}=0,
\qquad
p_{v,0}=j_v.
$$

$u_0$ é a raiz inferior não degenerada da Seção 11. Resta

$$
p_{a,0}
$$

como parâmetro de tiro. Equivalentemente, ele determina $\beta_0$ por

$$
\beta_0
=\frac{r_0p_{a,0}e^{u_0}-4r_0^2\tau}
{2r_0^3e^{u_0}},
$$

onde foi usado $h_0=-2r_0^2$ e $p_{u,0}=0$.

Esse parâmetro não é livre fisicamente: a equação de colagem

$$
\widetilde{\mathcal N}_-+widetilde{\mathcal N}_+=0
$$

deve determiná-lo. Portanto, o problema interno está reduzido a uma família
uniparamétrica, e o DtN exterior seleciona seu único membro físico.

## 17. Circulação de Hopf omitida pelo ansatz radial

O momento $p_v$ das seções anteriores mede fluxo radial. Para um background
estacionário sem vazamento através do estômato,

$$
p_v=0.
$$

Como $S_R=\hbar v$, a circulação quantizada deve ser representada por

$$
v(s,\Omega)=v_0(s)+m\psi,
\qquad m\in\mathbb Z,
$$

de modo que

$$
\oint dS_R=2\pi\hbar m.
$$

Na métrica de Berger,

$$
|dv|^2
=\dot v_0^2+\kappa_\psi\frac{m^2}{c^2}.
$$

O potencial reduzido recebe

$$
\boxed{
V_m(a,c)
=V(a,c)+\kappa_\psi\frac{a^2m^2}{c}.
}
$$

Na garganta geral, com $p_v=0$, a equação do lapse torna-se

$$
\boxed{
u_0
=4-\frac{8\tau}{a_0^2}
+\frac{4\tau c_0^2}{a_0^4}
-\tau\kappa_\psi\frac{m^2}{c_0^2}.
}
$$

O termo angular deve ser incluído nas equações dos momentos e na Hessiana
antes do próximo tiro. Logo o controle já executado com $m=0$ não testa o
setor físico elementar $m=1$.
