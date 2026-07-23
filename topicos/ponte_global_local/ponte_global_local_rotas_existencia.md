# Existência bulk--interface — duas rotas a partir da ação oficial

> **Correção de validade.** As Seções 2 e 3.1--3.8 abaixo registram uma
> tentativa histórica que reutilizou a redução da Q29 com uma 3-forma
> $H=h\,\sigma_{123}$ tratada como variável independente. Essa redução não é
> admissível na ponte vigente, onde $H=d_J^c\omega$. Consequentemente, a
> cúbica homogênea, sua continuação e a matriz $\mathsf M(k)$ não constituem
> resultados da ação oficial atual. Elas ficam preservadas apenas para mostrar
> por que a rota foi descartada. A reconstrução válida começa na Seção 6.

## 1. Objetivo

Este documento testa duas estratégias independentes para construir a sela
bulk--interface sem reutilizar como premissa qualquer background anterior:

1. minimização direta na folha conservada;
2. problema de sela com vínculo radial e colagem.

O setor de cohomogeneidade um usa

$$
ds_perp^2
=N(r)^2dr^2+a(r)^2(\sigma_1^2+\sigma_2^2)+c(r)^2\sigma_3^2,
$$

$$
f=f(r),
\qquad
H=h\,\sigma_1\wedge\sigma_2\wedge\sigma_3,
$$

com $h$ fixado pela carga relativa. O lapse $N$ é variado antes da escolha de
coordenada radial.

## 2. Rota A — minimização direta

### 2.1 Forma principal

Após a integração por partes variacionalmente completa, a parte com derivadas
radiais é

$$
T_r
=2ca'^2+4aa'c'-4acf'a'-2a^2f'c'+a^2cf'^2.
$$

Introduza

$$
x=\log a,
\qquad
y=\log c,
$$

e as combinações de volume e anisotropia

$$
u=2x+y=\log(a^2c),
\qquad
v=y-x=\log(c/a).
$$

Então

$$
\frac{T_r}{a^2c}
=f'^2-2f'u'+\frac23u'^2-\frac23v'^2.
$$

Equivalentemente,

$$
\boxed{
\frac{T_r}{a^2c}
=(f'-u')^2-\frac13u'^2-\frac23v'^2.
}
$$

### 2.2 Veredito da rota A

A normalização da medida elimina uma direção global, mas não muda o símbolo
principal local. A carga fixa $h$ e a conservação de fluxo impõe condições de
traço; nenhuma delas muda o coeficiente negativo de $v'^2$.

Portanto, na parametrização radial completa,

$$
\inf \mathcal S_{\rm GDQ}=-\infty
$$

ao longo de sequências oscilatórias de anisotropia, a menos que o vínculo do
lapse seja resolvido antes de definir o espaço físico. Não existe prova de
existência por minimização direta da forma não reduzida.

Esse é um resultado negativo preciso:

$$
\boxed{
\text{Rota A excluída para a ação radial não reduzida.}
}
$$

Ele não exclui a existência de uma sela.

## 3. Rota B — sela vinculada e colagem

### 3.1 Restrição do lapse

A variação em $N$ fornece

$$
-\tau T_r+\tau V_r+a^2c(f-n-\lambda)=0,
$$

com

$$
V_r
=8c-2\frac{c^3}{a^2}-\frac{h^2}{2a^2c}.
$$

Essa equação deve ser imposta antes da análise espectral. Ela remove uma
combinação longitudinal associada à reparametrização radial.

### 3.2 Dados no estômato

No bordo interno $r=r_c$, os dados admissíveis são

$$
a(r_c)=a_c>0,
\qquad
c(r_c)=c_c>0,
\qquad
f(r_c)=f_c,
$$

$$
h=\frac{2\pi q}{\int_{S^3}\sigma_1\wedge\sigma_2\wedge\sigma_3},
$$

e três momentos de bordo. A primeira variação e a conservação das correntes
impõem:

$$
\Pi_+^a=\Pi_-^a,
\qquad
\Pi_+^c=\Pi_-^c,
\qquad
\Pi_+^f=\Pi_-^f,
$$

além da restrição do lapse. Não se prescrevem simultaneamente campo e momento
para a mesma componente.

### 3.3 Dados na ponta global

Na região distante, exige-se aproximação ao background cosmológico suave,
com fluxo líquido relativo nulo fora do setor $q$:

$$
(a,c,f)(r)\longrightarrow(a_\infty,c_\infty,f_\infty),
$$

$$
\Pi(r)\longrightarrow\Pi_\infty,
\qquad
\int\mathcal U,dV=1.
$$

Os valores admissíveis não são parâmetros livres independentes: devem
satisfazer as cargas de Noether globais do espaço cosmológico.

### 3.4 Mapa de colagem

Resolva localmente as equações de Euler--Lagrange a partir das duas pontas e
transporte os dados até uma seção $r=r_m$. Defina o defeito

$$
\mathfrak F(\mathbf d,\lambda)
=\begin{pmatrix}
X_-(r_m)-X_+(r_m)\\
\Pi_-(r_m)-\Pi_+(r_m)\\
\int\mathcal U,dV-1
\end{pmatrix},
$$

onde $\mathbf d$ contém somente os dados de bordo independentes compatíveis
com carga, fluxo e simetrias.

Uma sela bulk--interface é exatamente um zero de

$$
\boxed{
\mathfrak F(\mathbf d_*,\lambda_*)=0.
}
$$

### 3.5 Existência local e existência global

Enquanto $a,c>0$, as equações formam um sistema regular de EDOs após a
fixação radial e a eliminação do vínculo. Picard--Lindelöf fornece existência
e unicidade local para cada conjunto admissível de dados.

A existência global da sela reduz-se agora a uma afirmação finita e testável:

$$
0\in\mathfrak F(\mathscr D).
$$

Ela pode ser provada por uma das seguintes ferramentas, sem pós-ajuste:

1. grau topológico não nulo de $\mathfrak F$ numa região admissível;
2. mudança de sinal/orientação nas faces de uma caixa de dados;
3. continuação homotópica desde o setor de carga nula, desde que o
   linearizado permaneça Fredholm e não perca o gap transversal.

### 3.6 Sela homogênea de partida derivada da ação

Existe um ponto inicial explícito para a continuação. Tome

$$
a=c=R,
\qquad
a'=c'=f'=0,
$$

mantendo o fluxo $h$ fixado pela carga. Escreva

$$
L=\lambda+n-f.
$$

As equações de $a$ e $c$ coincidem e fornecem

$$
L
=\frac{2\tau}{R^2}+\frac{\tau h^2}{2R^6}.
$$

A equação de $f$ reduz-se a

$$
R^6-4\tau R^4+\tau h^2=0.
$$

Com

$$
x=R^2>0,
$$

obtém-se a cúbica

$$
\boxed{
p_h(x)=x^3-4\tau x^2+\tau h^2=0.
}
$$

Para $h=0$, a raiz não degenerada é

$$
R^2=4\tau.
$$

Para $h\neq0$, o mínimo positivo de $p_h$ ocorre em

$$
x_c=\frac{8\tau}{3},
$$

e

$$
p_h(x_c)
=\tau h^2-\frac{256}{27}\tau^3.
$$

Consequentemente, existem raízes positivas se e somente se

$$
\boxed{
h^2\leq\frac{256}{27}\tau^2.
}
$$

Para desigualdade estrita existem dois ramos positivos; na igualdade eles se
fundem numa sela crítica. Esse resultado é uma existência exata no setor
homogêneo vinculado, deduzida da ação oficial e da carga conservada.

Ele ainda não é a sela localizada do estômato: distribui a torção por toda a
órbita $S^3$. Seu papel legítimo é fornecer o ponto inicial da continuação

$$
X_s=X_{\rm hom}+s\,X_{\rm loc},
\qquad 0\leq s\leq1,
$$

com carga total fixa. O fechamento da existência localizada exige demonstrar
que o ramo não encontra perda de elipticidade, colapso de $a,c$ ou núcleo
físico adicional antes de $s=1$.

### 3.7 Linearização do ramo homogêneo

Considere um modo radial não constante proporcional a $e^{ikr}$:

$$
a=R+A e^{ikr},
\qquad
c=R+C e^{ikr},
\qquad
f=f_0+F e^{ikr}.
$$

Para esse modo, $\delta\lambda=0$. Usando a equação cúbica do background, a
restrição linearizada do lapse reduz-se exatamente a

$$
R^3F=0.
$$

Logo,

$$
F=0
$$

no setor não homogêneo. O sistema restante para $(A,C)$ possui matriz

$$
\mathsf M(k)=
\begin{pmatrix}
-2R^2\tau k^2-2R+16\tau/R
&-R(2\tau k^2+1)\\
-R(2\tau k^2+1)
&-R/2+8\tau/R
\end{pmatrix}.
$$

No modo homogêneo, $k=0$, os menores principais são positivos nos dois ramos
com

$$
R^2<4\tau<\frac{16\tau}{3}.
$$

Entretanto, para $|k|\to\infty$,

$$
\det\mathsf M(k)
=-4R^2\tau^2k^4+O(k^2)<0.
$$

Portanto, os dois autovalores possuem sinais opostos em altas frequências. A
restrição do lapse remove o dilatão não homogêneo, mas não elimina a direção
anisotrópica negativa.

Conclusão:

$$
\boxed{
\text{a sela homogênea existe, mas não tem Hessiana radial semilimitada.}
}
$$

Ela pode ser usada para demonstrar continuação de pontos críticos enquanto
$\det\mathsf M(k)\neq0$, mas não como prova de estabilidade física ou de gap
positivo.

### 3.8 Por que isso não encerra a rota causal

O cálculo acima congelou $\tau$ e omitiu a integral externa ao longo de
$\gamma$. Ele testa a Hessiana de uma fatia radial euclidiana. A ação oficial,
porém, é um funcional de contorno causal:

$$
\int_\gamma(\cdots)\frac{d\tau}{\tau}.
$$

Há, portanto, uma segunda realização possível do operador físico: primeiro
impor o transporte causal, a continuidade das correntes entre as fatias e as
condições de extremidade em $\gamma$; somente depois formar o complemento de
Schur e o espectro. Para essa realização, a direção negativa de uma fatia pode
ser um par canônico de sela, não um modo físico propagante.

Isso não autoriza inverter seu sinal manualmente. É necessário derivar o
operador acoplado $(r,\tau)$ da segunda variação completa.

## 4. Relação com $P^{\rm phys}$

No zero obtido, linearize simultaneamente as equações e os vínculos. O
operador $A_*$ de
`topicos/ponte_global_local/ponte_global_local_sela_projetor_gap.md` é então completamente determinado.
O projetor é

$$
P^{\rm phys}
=I-\mathbb G_*^{-1}A_*^\dagger
\left(A_*\mathbb G_*^{-1}A_*^\dagger\right)^+A_*.
$$

O gap é o primeiro autovalor positivo de

$$
K_*^{\rm phys}
=P^{{\rm phys}\dagger}
D_X^2\mathscr L(X_*,\lambda_*)
P^{\rm phys}.
$$

## 5. Status

- Rota A: concluída negativamente; a forma não reduzida não é coerciva.
- Rota B: problema correto construído; existência local demonstrada e sela
  homogênea carregada obtida exatamente quando
  $h^2\leq256\tau^2/27$.
- Falta para a existência global localizada: calcular o grau ou realizar a
  continuação controlada do mapa $\mathfrak F$ desde essa sela.
- A Hessiana da fatia radial homogênea é indefinida em altas frequências;
  portanto ela não fornece gap positivo.
- O próximo teste independente é a Hessiana completa em $(r,\tau)$ com o
  domínio causal $\gamma$. O cálculo de $P^{\rm phys}$ e do gap físico deve
  ser feito nessa realização, no zero localizado obtido.

## 6. Reinício correto: torção de Bismut dependente

Na classe Hermitiana oficial,

$$
H=d_J^c\omega
=2c(aa'-c)\,\sigma_1\wedge\sigma_2\wedge\sigma_3.
$$

Portanto, o coeficiente de fluxo é

$$
h(r)=2c(aa'-c),
$$

e não um perfil independente. A conservação do fluxo no setor strong-KT dá

$$
h'(r)=0.
$$

Assim, carga e conservação impõem o vínculo cinemático

$$
\boxed{
a'(r)=\frac{c(r)}{a(r)}+\frac{h_0}{2a(r)c(r)}.
}
$$

Esse vínculo deve ser aplicado antes da Hessiana. Ele remove precisamente uma
das velocidades métricas que havia sido variada indevidamente na tentativa
anterior.

Depois da integração por partes completa do escalar de Levi--Civita, o
funcional de primeira ordem válido, omitindo apenas fatores globais positivos,
é

$$
\begin{aligned}
I_\tau=\int dr\,e^{-u}\Bigg\{\tau\Bigg[&
4aa'c'-4acu'a'-2a^2u'c'
+a^2c\bigl((u')^2+(v')^2\bigr)\\
&+4\frac{c^2}{a}a'
+8c-4\frac{c^3}{a^2}
\Bigg]+a^2c(u-4)\Bigg\}.
\end{aligned}
$$

O termo $2ca'^2$ produzido pela curvatura cancela exatamente com a parcela
quadrática de $-|H|^2/12$. Isso é uma consequência direta de
$H=d_J^c\omega$.

No setor de fluxo conservado, substitui-se a equação de primeira ordem para
$a'$ antes de construir o operador físico. Restam os perfis $(c,u,v)$, a
normalização da medida e as condições de interface. Essa é a nova origem das
duas rotas de existência.

## 7. Lapse, correntes conservadas e redução física

### 7.1 Restauração do lapse

Use

$$
ds_perp^2
=N(r)^2dr^2+a(r)^2(\sigma_1^2+\sigma_2^2)+c(r)^2\sigma_3^2.
$$

Com derivada própria

$$
\dot X=N^{-1}X',
$$

a torção correta é

$$
H
=2c(a\dot a-c)\,\sigma_1\wedge\sigma_2\wedge\sigma_3.
$$

A conservação do fluxo $h_0$ fornece

$$
\boxed{
\dot a=A(a,c;h_0)
=\frac ca+\frac{h_0}{2ac}.
}
$$

### 7.2 Funcional reparametrização-invariante

O funcional corrigido pode ser escrito como

$$
I_\tau
=\int Ndr\,e^{-u}
\left\{
\tau\left[Q(\dot a,\dot c,\dot u,\dot v)
+4\frac{c^2}{a}\dot a+V(a,c)\right]
+a^2c(u-4)
\right\},
$$

onde

$$
Q
=4a\dot a\dot c-4ac\dot u\dot a-2a^2\dot u\dot c
+a^2c\left(\dot u^2+\dot v^2\right),
$$

$$
V(a,c)=8c-4\frac{c^3}{a^2}.
$$

O termo linear $4c^2\dot a/a$ não depende do lapse depois de voltar à
coordenada $r$ e não entra na restrição hamiltoniana.

### 7.3 Corrente de fase

A invariância por translação de $v$ produz

$$
j_v
=2\tau e^{-u}a^2c\dot v,
\qquad
\dot j_v=0.
$$

Logo,

$$
\boxed{
\dot v
=\frac{j_v e^u}{2\tau a^2c}.
}
$$

Essa é a conservação de circulação/probabilidade na redução. $j_v$ é dado de
contorno, não parâmetro ajustável pelo espectro.

### 7.4 Restrição do lapse

A variação de $N$ fornece

$$
\boxed{
-\tau Q+\tau V+a^2c(u-4)=0.
}
$$

Defina

$$
W(a,c,u)
=V(a,c)+\frac{a^2c}{\tau}(u-4).
$$

Substituindo $\dot a=A$ e a corrente $j_v$, a restrição é linear em
$\dot c$:

$$
(4aA-2a^2\dot u)\dot c
-4acA\dot u+a^2c\dot u^2+a^2c\dot v^2
=W.
$$

Quando

$$
2A-a\dot u\neq0,
$$

ela determina

$$
\boxed{
\dot c
=\frac{
W+4acA\dot u-a^2c\dot u^2-a^2c\dot v^2
}{2a(2A-a\dot u)}.
}
$$

Portanto, antes mesmo de usar a equação de $u$, três componentes já estão
determinadas por conservações e vínculo:

$$
\dot a=A(a,c;h_0),
$$

$$
\dot v=\frac{j_ve^u}{2\tau a^2c},
$$

$$
\dot c=\mathcal C(a,c,u,\dot u;h_0,j_v).
$$

### 7.5 Consequência para as duas rotas

Se $\dot c$ e $\dot u$ forem variados como independentes antes da restrição,
a forma principal é indefinida. Logo a minimização direta continua sendo uma
rota inválida.

Depois da redução de Dirac pelo fluxo, corrente e lapse, resta uma equação
dinâmica de segunda ordem para $u$ — ou um sistema de primeira ordem para
$(u,p_u)$ — acoplada às três equações acima. A existência da sela passa a ser
um problema de tiro com os dados independentes

$$
(a_c,c_c,u_c,p_{u,c};h_0,j_v)
$$

sujeitos à carga relativa, normalização e colagem exterior.

O denominador

$$
2A-a\dot u
$$

é a primeira superfície crítica da continuação. Uma prova global deve mostrar
que ele não zera antes da interface externa ou demonstrar que o numerador se
anula simultaneamente e permite continuação regular.

## 8. Estado atual após a correção

Foi derivado, sem usar um background anterior:

1. o vínculo geométrico da torção de Bismut;
2. a conservação da carga/fluxo;
3. a corrente de fase de Noether;
4. a restrição do lapse;
5. a redução do sistema a um problema de tiro de baixa dimensão.

Ainda faltam dois dados que não podem ser inventados:

1. a condição de interface obtida pela variação da região interna do
   estômato, equivalente ao seu operador DtN;
2. os dados globais de Noether na ponta cosmológica.

Uma vez inseridos, o mapa de tiro é completamente determinado e a existência
pode ser testada por grau e por continuação numérica independente.

### 8.1 Correção por multiplicador de fluxo

A implementação usada na integração deve conservar a equação
$2c(a\dot a-c)=h_0$ por um multiplicador local $\beta$. A ação aumentada é

$$
I_{\rm aug}
=I_\tau
+\int ds\,\beta\,[2c(a\dot a-c)-h_0].
$$

Isso corrige o momento de $a$ para

$$
\widetilde\Pi_a=\Pi_a+2\beta ac.
$$

O mapa de tiro deve, portanto, colar os momentos vinculados
$\widetilde\Pi$, e o linearizado deve incluir $(\eta,\delta\beta)$. A
substituição direta de $\dot a$ continua útil para reduzir o bloco algébrico,
mas não deve ser usada para calcular o DtN antes de recuperar $\beta$.
