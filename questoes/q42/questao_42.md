# Questão 42 — Stern–Gerlach

## 1. Veredito inicial

O Capítulo 10 já contém uma explicação mecânico-geométrica para a separação de
um feixe em dois ramos quando o campo define o eixo (z). Ele ainda não resolve,
por si só, o experimento de Stern–Gerlach completo.

O que já está estabelecido é:

1. a circulação estável possui duas orientações, rotuladas por
   \(\kappa=\pm1\);
2. o acoplamento magnético separa essas orientações;
3. a força no centro do sóliton produz duas deflexões discretas.

O que precisa ser acrescentado é a dependência da orientação do aparelho, as
probabilidades angulares, a atualização após a seleção de um feixe e as
sequências de medidas incompatíveis. Esses elementos não podem ser obtidos
tratando \(\kappa\) como um sinal absoluto preexistente para todos os eixos.

## 2. Setor geométrico mínimo

Seja \(\boldsymbol n\in S^2\) a direção local do campo do aparelho. A dupla
orientação da circulação deve ser realizada por uma cobertura dupla do espaço
de direções. Localmente, essa cobertura pode ser representada por uma fibra
complexa de dimensão dois, com estado normalizado \(u\in\mathbb C^2\),
\(u^\dagger u=1\), e mapa geométrico

\[
 \boldsymbol a=u^\dagger\boldsymbol\sigma u\in S^2.
\]

Aqui, \(\boldsymbol\sigma\) é apenas a representação matricial local da álgebra
da cobertura dupla. Na GDQ, ela deve ser entendida como descrição efetiva da
holonomia/orientação do estômato, e não como a introdução de um campo
fundamental independente ou como substituição da ação oficial.

Para uma direção \(\boldsymbol n\), definem-se os dois projetores geométricos

\[
 P_{\boldsymbol n}^{\pm}
 =\frac12\bigl(I\pm\boldsymbol n\cdot\boldsymbol\sigma\bigr).
\]

Eles satisfazem

\[
 (P_{\boldsymbol n}^{\pm})^2=P_{\boldsymbol n}^{\pm},\qquad
 P_{\boldsymbol n}^{+}P_{\boldsymbol n}^{-}=0,\qquad
 P_{\boldsymbol n}^{+}+P_{\boldsymbol n}^{-}=I.
\]

Esta é a estrutura mínima que a construção global Hopf/Kähler–Bismut deverá
derivar. O uso local desses projetores permite verificar todas as exigências
experimentais sem afirmar que a derivação global já foi concluída.

## 3. Derivação dos dois autovalores

O observável de circulação ao longo do eixo selecionado pelo aparelho é

\[
 S_{\boldsymbol n}=\frac{\hbar}{2}\,
 \boldsymbol n\cdot\boldsymbol\sigma.
\]

Como

\[
 (\boldsymbol n\cdot\boldsymbol\sigma)^2=I,
\]

seu polinômio mínimo é \(x^2-1\). Portanto,

\[
 \operatorname{spec}(S_{\boldsymbol n})
 =\left\{-\frac\hbar2,+\frac\hbar2\right\}.
\]

Equivalentemente,

\[
 S_{\boldsymbol n}P_{\boldsymbol n}^{\pm}
 =\pm\frac\hbar2P_{\boldsymbol n}^{\pm}.
\]

Assim, \(\kappa=\pm1\) não é um terceiro postulado: ele é o rótulo dos dois
autofibrados selecionados pela direção \(\boldsymbol n\).

## 4. Acoplamento e deflexão para direção arbitrária

O termo de interface do capítulo deve ser escrito de modo covariante como

\[
 V_{\rm SG}=-\boldsymbol\mu\cdot\boldsymbol B,
 \qquad
 \boldsymbol\mu=\gamma_s\boldsymbol S.
\]

No regime adiabático, em que a orientação interna acompanha a direção local
\(\boldsymbol n(\boldsymbol x)=\boldsymbol B/|\boldsymbol B|\), os dois canais
possuem energias

\[
 E_\pm(\boldsymbol x)=\mp\mu\,|\boldsymbol B(\boldsymbol x)|
\]

e forças

\[
 \boldsymbol F_\pm=-\boldsymbol\nabla E_\pm
 =\pm\mu\,\boldsymbol\nabla|\boldsymbol B|.
\]

Para campo aproximadamente alinhado com \(z\), recupera-se a equação do
capítulo. A condição adiabática é essencial: se a direção do campo variar
rapidamente, aparecem transições entre os dois canais e a simples trajetória
com \(\kappa\) fixo deixa de ser válida.

## 5. Probabilidades

Considere um feixe preparado com orientação geométrica \(\boldsymbol a\),
descrito por

\[
 \varrho_{\boldsymbol a}
 =\frac12(I+\boldsymbol a\cdot\boldsymbol\sigma).
\]

Usando a regra operacional já consolidada na Questão 22, a fração detectada em
cada canal é

\[
 p_\pm(\boldsymbol n|\boldsymbol a)
 =\operatorname{Tr}\bigl(
 \varrho_{\boldsymbol a}P_{\boldsymbol n}^{\pm}\bigr)
 =\frac{1\pm\boldsymbol a\cdot\boldsymbol n}{2}.
\]

Se \(\theta\) é o ângulo entre preparação e aparelho,

\[
 p_+=\cos^2\frac\theta2,
 \qquad
 p_-=\sin^2\frac\theta2.
\]

Para feixe não polarizado, \(\varrho=I/2\), obtém-se

\[
 p_+=p_-=\frac12.
\]

Logo, a existência de dois canais não implica automaticamente pesos iguais.
Os pesos dependem da preparação e do eixo do aparelho.

## 6. Medições sequenciais incompatíveis

Depois de selecionar o resultado \(s=\pm1\) ao longo de \(\boldsymbol a\), o
subfeixe transmitido está no setor

\[
 \varrho_{\boldsymbol a,s}
 =P_{\boldsymbol a}^{s}.
\]

Uma medida posterior ao longo de \(\boldsymbol b\) fornece

\[
 p(s'|s;\boldsymbol b,\boldsymbol a)
 =\operatorname{Tr}
 \bigl(P_{\boldsymbol a}^{s}P_{\boldsymbol b}^{s'}\bigr)
 =\frac{1+ss'\boldsymbol a\cdot\boldsymbol b}{2}.
\]

Consequências imediatas:

1. \(z+\) seguido de \(z\) produz \(z+\) com probabilidade um;
2. \(z+\) seguido de \(x\) produz \(x\pm\) com probabilidade \(1/2\);
3. selecionando depois \(x+\) e medindo novamente \(z\), surgem \(z\pm\) com
   probabilidade \(1/2\).

Isso decorre de

\[
 [S_{\boldsymbol a},S_{\boldsymbol b}]
 =i\hbar S_{\boldsymbol a\times\boldsymbol b}.
\]

Geometricamente, o aparelho intermediário altera a decomposição do estado nos
dois autofibrados. Portanto, ele não apenas revela um sinal \(\kappa\) que já
estaria simultaneamente definido para todos os eixos.

## 7. Contextualidade

A contextualidade necessária aqui tem sentido operacional preciso: o resultado
é definido relativamente à direção e à geometria completa do aparelho. O par
de ramos \(\kappa_{\boldsymbol n}=\pm1\) pertence à decomposição escolhida por
\(\boldsymbol n\), e não constitui uma tabela de valores absolutos
\(\kappa_x,\kappa_y,\kappa_z\) simultaneamente mensuráveis.

Isso é compatível com causalidade: a orientação do campo entra localmente no
termo de interface e modifica a dinâmica da fronteira durante a interação. Não
é necessário que o resultado futuro determine retroativamente a preparação.

Também é importante não invocar de forma imprecisa o teorema de
Kochen–Specker: um único sistema de dimensão complexa dois não satisfaz a
hipótese dimensional usual desse teorema. A incompatibilidade sequencial acima
já é demonstrável no Stern–Gerlach; uma afirmação mais forte de contextualidade
de Kochen–Specker exigiria ampliar explicitamente o sistema ou o conjunto de
observáveis.

## 8. O que o capítulo atual precisa corrigir

1. substituir \(B_z\) por uma formulação covariante em
   \(\boldsymbol n=\boldsymbol B/|\boldsymbol B|\);
2. interpretar \(\kappa\) como rótulo relativo ao eixo do aparelho, não como
   orientação absoluta para todos os eixos;
3. remover a afirmação de que a aceleração “deixa de depender de
   probabilidades”: a trajetória em cada canal é determinística, mas a fração
   que entra em cada canal obedece às probabilidades acima;
4. separar a quantização dos dois ramos da distribuição estatística entre eles;
5. incluir a condição adiabática e reconhecer possíveis transições fora dela;
6. não atribuir à causalidade, por si só, a origem dos pesos de Born.

## 9. Ponte global: do contorno \(S^3\) à fibração de Hopf

Esta seção elimina a introdução independente das matrizes de Pauli. Considere
o setor de um estômato cujo elo normalizado é a 3-esfera e escreva suas duas
coordenadas complexas de Kähler como

\[
 u=\begin{pmatrix}z_1\\z_2\end{pmatrix}\in\mathbb C^2,
 \qquad |z_1|^2+|z_2|^2=1.
\]

Logo, \(u\in S^3\). A fase comum não altera a orientação física do eixo de
circulação:

\[
 u\sim e^{i\varphi}u.
\]

O quociente é

\[
 S^3/U(1)=\mathbb{CP}^1\simeq S^2,
\]

portanto o fibrado axial é necessariamente, nesse setor de contorno,

\[
 \boxed{S^1\hookrightarrow S^3\xrightarrow{\pi_H}S^2}.
\]

Uma expressão que não depende da carta para a projeção é

\[
 P(u)=uu^\dagger.
\]

Como \(P=P^\dagger=P^2\) e
\(\operatorname{Tr}P=1\), toda matriz desse tipo admite a decomposição única

\[
 P(u)=\frac12(I+\boldsymbol n\cdot\boldsymbol\sigma),
 \qquad
 n_i=\operatorname{Tr}(P\sigma_i)=u^\dagger\sigma_i u.
\]

De \(P^2=P\) segue \(\boldsymbol n^2=1\). Assim, as três matrizes que aparecem
localmente não são novos campos fundamentais: elas são uma base do espaço
real das matrizes hermitianas \(2\times2\) sem traço, induzida pelas duas
coordenadas complexas do elo \(S^3\subset\mathbb C^2\).

## 10. Conexão de Hopf, curvatura e seleção dos dois autofibrados

A conexão hermitiana canônica no fibrado é

\[
 \mathcal A_H=-i\,u^\dagger du,
\]

e sua curvatura é

\[
 \mathcal F_H=d\mathcal A_H
 =\frac14\epsilon_{ijk}n_i\,dn_j\wedge dn_k
\]

na convenção em que

\[
 \frac1{2\pi}\int_{S^2}\mathcal F_H=1.
\]

Portanto, o fibrado de Hopf elementar possui \(c_1=1\); sua orientação
conjugada possui \(c_1=-1\). Para cada direção do aparelho

\[
 P_{\boldsymbol n}^{+}=P(u)
 =\frac12(I+\boldsymbol n\cdot\boldsymbol\sigma),
 \qquad
 P_{\boldsymbol n}^{-}=I-P(u)
 =\frac12(I-\boldsymbol n\cdot\boldsymbol\sigma).
\]

Logo, os dois canais são os dois fibrados de linha ortogonais selecionados
pelo aparelho. Não há um terceiro canal porque uma fibra complexa de posto
dois decompõe-se aqui em dois projetores de posto um complementares.

## 11. Cobertura dupla, meia circulação e normalização

Identificando \(S^3\simeq SU(2)\), uma rotação física de ângulo \(\theta\) em
torno de \(\boldsymbol n\) levanta-se a

\[
 U(\theta)=
 \exp\!\left(-\frac{i\theta}{2}\boldsymbol n\cdot\boldsymbol\sigma\right).
\]

Consequentemente,

\[
 U(2\pi)=-I,
 \qquad U(4\pi)=I.
\]

Isso dá a interpretação precisa da monodromia já usada no Capítulo 9: uma
volta no espaço de orientações leva \(u\) a \(-u\), e somente duas voltas
fecham o levantamento em \(S^3\). A circulação meio-inteira e a cobertura
dupla são, portanto, duas descrições do mesmo levantamento topológico; não se
deve obtê-las dividindo \(h\) por dois apenas por analogia.

Fixada pela integração de circulação da GDQ a unidade elementar
\(\hbar/2\), o gerador infinitesimal é

\[
 S_i=\frac\hbar2\sigma_i.
\]

A composição dos endomorfismos da base hermitiana fornece

\[
 \sigma_i\sigma_j=\delta_{ij}I+i\epsilon_{ijk}\sigma_k,
\]

e, portanto,

\[
 [S_i,S_j]=i\hbar\epsilon_{ijk}S_k,
 \qquad
 (\boldsymbol n\cdot\boldsymbol S)^2=\frac{\hbar^2}{4}I.
\]

Assim ficam derivados, em uma mesma cadeia, os dois autovalores, os
projetores dependentes do aparelho, a não comutatividade de eixos distintos e
a monodromia \(4\pi\).

## 12. Relação precisa com a ação oficial da GDQ

A ação oficial determina a métrica hermitiana, o campo complexo, a medida e a
conexão torsional no bulk. Restringida a um elo de estômato já demonstrado
como \(S^3\subset\mathbb C^2\), sua conexão hermitiana induz a conexão acima.
Variações que preservam o contorno não mudam

\[
 c_1=\frac1{2\pi}\int_{S^2}\mathcal F_H,
\]

pois esse número é inteiro e constante em cada componente topológica. Nesse
sentido, uma vez escolhido o setor elementar \(c_1=\pm1\), o fluxo
Ricci--Bismut pode deformar a métrica e a distribuição local de torção, mas
não pode destruir a dupla cobertura sem atravessar uma singularidade ou mudar
as condições de contorno.

É necessário, entretanto, distinguir preservação de seleção. O funcional
bulk, escrito sem condições topológicas de fronteira, preserva cada setor mas
não prova sozinho que o defeito físico ocupa \(c_1=\pm1\), em vez do setor
trivial ou de um enrolamento superior. A seleção elementar requer a condição
de contorno de carga mínima não nula:

\[
 \boxed{|c_1|=1.}
\]

Essa condição é compatível com o princípio variacional: entre setores não
triviais, o representante de menor ação/energia torsional é o de menor
\(|c_1|\), desde que o termo quadrático positivo da Hessiana de fronteira seja
estabelecido. A prova inteiramente a partir da ação oficial fica reduzida,
portanto, a verificar essa positividade e a existência do elo \(S^3\) para a
solução estacionária considerada; ela não exige postular a álgebra de Pauli.

### 12.1 Duas topologias que não devem ser confundidas

O termo de fase da ação oficial,

\[
 \mathcal E_{\rm fase}
 =
 C_\gamma\frac{\tau}{\hbar^2}
 \int\mathcal U\,|dS_R|_g^2\,dV_g,
\]

possui Hessiana não negativa no ramo euclidiano
\((C_\gamma>0,\mathcal U>0,g>0)\). Ele seleciona o menor enrolamento não nulo
quando o defeito tem uma fatia normal real bidimensional: o elo normal é
\(S^1\), \(\pi_1(S^1)=\mathbb Z\), e

\[
 \frac1{2\pi\hbar}\oint_{S^1}dS_R=k.
\]

Nesse caso Cauchy--Schwarz dá \(\mathcal E_k\geq Kk^2\), de modo que os
setores não triviais mínimos são \(k=\pm1\).

Isso, porém, não é ainda a seleção do fibrado de Hopf. Um defeito isolado em
uma fatia \(\mathbb C^2\simeq\mathbb R^4\) tem elo \(S^3\), e

\[
 \pi_1(S^3)=0.
\]

Logo não existe um círculo gerador de \(\pi_1(S^3)\). As fibras \(S^1\) da
aplicação de Hopf são círculos geométricos, mas são contráteis no espaço total
\(S^3\). Usá-las diretamente como o ciclo de circulação de um escalar global
confundiria dois invariantes diferentes.

### 12.2 A classificação correta do setor de Hopf

O número de Chern é calculado na base \(S^2\), não como enrolamento de uma
função escalar global em \(S^3\). Cobrindo \(S^2\) pelas cartas norte e sul,
a função de transição no equador é

\[
 g_{NS}:S^1\longrightarrow U(1),
 \qquad
 c_1(L)=\deg(g_{NS})
 =\frac1{2\pi i}\oint g_{NS}^{-1}dg_{NS}.
\]

Equivalentemente, para uma conexão \(\mathcal A\),

\[
 c_1(L)=\frac1{2\pi}\int_{S^2}\mathcal F,
 \qquad \mathcal F=d\mathcal A.
\]

O fibrado de Hopf corresponde a \(c_1=\pm1\). A construção das Seções
9--11 prova todas as consequências de Stern--Gerlach uma vez escolhido esse
setor, mas a preferência energética por \(|c_1|=1\) requer uma energia que
veja \(d\mathcal A\) ou, de modo equivalente, as derivadas do projetor
\(P:S^2\to\mathbb{CP}^1\).

### 12.3 Hessiana que realmente falta

Se a redução da ação oficial no elo produzir o funcional sigma-modelo

\[
 \mathcal E_H[P]
 =
 \kappa_H
 \int_{S^2}\operatorname{Tr}(dP\wedge *dP),
 \qquad \kappa_H>0,
\]

então vale a cota topológica

\[
 \boxed{\mathcal E_H[P]\geq4\pi\kappa_H|c_1(P)|}
\]

com igualdade para os mapas holomorfos ou anti-holomorfos elementares. Entre
os setores não triviais, os mínimos são precisamente \(c_1=\pm1\). A
segunda variação, depois de remover os modos de isometria e de fase, é o
operador de Jacobi do mapa harmônico e deve ser não negativa no representante
elementar.

Essa é a seleção variacional correta. O que ainda precisa ser calculado é o
coeficiente \(\kappa_H\) e o operador de Jacobi obtidos pela restrição da
Hessiana métrico--dilatônica da ação oficial ao ansatz
\(P=uu^\dagger\). O termo escalar \(|dS_R|^2\), sozinho, prova a estabilidade
da circulação numa fatia normal \(S^1\), mas não gera automaticamente a
curvatura de Chern do fibrado de Hopf.

### 12.4 Geometria local do elo

Se o estômato for um defeito isolado numa fatia normal complexa de dimensão
dois, uma vizinhança perfurada é localmente

\[
 \mathbb C^2\setminus\{0\}
 \simeq \mathbb R_+\times S^3,
\]

e o elo \(S^3\) segue sem hipótese topológica adicional. O corpus afirma uma
fronteira tridimensional \(S^3\), mas ainda não fornece uma demonstração
uniforme de que todo estômato fermiônico tenha precisamente codimensão real
quatro. Essa codimensão deve ser fixada na definição do defeito, ou derivada
da análise local das soluções estacionárias.

## 13. Cálculo local da fatia normal

Seja \(Z\) o conjunto singular que representa o estômato numa variedade
complexa \(M\) de dimensão complexa quatro. Suponha que, perto de
\(p\in Z\), existam duas funções holomorfas

\[
 F=(F_1,F_2):M\longrightarrow\mathbb C^2
\]

tais que

\[
 Z\cap U=F^{-1}(0),
 \qquad \operatorname{rank}_{\mathbb C}dF_p=2.
\]

Pelo teorema holomorfo da função implícita, existem coordenadas
\((w^1,w^2,z^1,z^2)\) nas quais

\[
 Z\cap U=\{z^1=z^2=0\}.
\]

Consequentemente,

\[
 N^{1,0}_{Z/M,p}
 \simeq
 \operatorname{span}_{\mathbb C}
 \left\{\frac{\partial}{\partial z^1},
 \frac{\partial}{\partial z^2}\right\}
 \simeq\mathbb C^2.
\]

Para uma métrica hermitiana, a fronteira do tubo normal de raio
\(\varepsilon\) é

\[
 \boxed{
 \operatorname{Link}_p(Z)
 =
 \{|z^1|^2+|z^2|^2=\varepsilon^2\}
 \simeq S^3.
 }
\]

Isso demonstra rigorosamente
\(\mathbb C^2\Rightarrow S^3\), mas identifica a hipótese dinâmica: o
estômato deve ser uma interseção completa complexa transversal de
codimensão dois.

### 13.1 Teste da definição atual

O corpus define inicialmente apenas

\[
 Z_\rho=\{\rho=0\}.
\]

Se esse nó for o zero regular de uma única amplitude complexa \(\Psi\), ele
tem codimensão complexa um, fatia normal \(\mathbb C\) e elo \(S^1\).
Portanto,

\[
 \boxed{Z_\rho=\{\rho=0\}\not\Rightarrow N_{Z/M}\simeq\mathbb C^2.}
\]

Para obter o elo de Hopf é necessária uma segunda restrição complexa
independente. Uma possibilidade compatível com a interpretação da GDQ é

\[
 F_1=\Psi=0,\qquad F_2=\Xi_B=0,\qquad
 d\Psi\wedge d\Xi_B\ne0,
\]

onde \(\Xi_B\) seria uma componente complexa transversal da condição
estacionária de Bismut/colagem. Isso só se torna uma derivação da GDQ quando
\(\Xi_B\) for extraída das equações da solução, e não simplesmente definida
para obter a codimensão desejada.

Assim, há dois objetos distintos:

1. nó simples de Madelung: elo \(S^1\) e circulação inteira;
2. estômato axial de Hopf: elo \(S^3\), condicionado à transversalidade de
   duas equações complexas.

## 14. Projeção da Hessiana oficial no ansatz \(P=uu^\dagger\)

Agrupe os campos fundamentais em

\[
 \Phi=(g_{\mu\bar\nu},f,\bar f)
\]

e denote por \(\mathbb H_{\rm GDQ}\) a Hessiana oficial em blocos, após a
fixação dos difeomorfismos. O projetor

\[
 P=uu^\dagger=\frac12(I+n_i\sigma_i)
\]

tem variações tangentes

\[
 \delta P=\frac12\sigma_i\delta n_i,\qquad n_i\delta n_i=0.
\]

Para inseri-lo na ação é indispensável um mapa de moduli

\[
 \iota:\mathbb{CP}^1\longrightarrow\{(g,f,\bar f)\},
 \qquad P\longmapsto\Phi(P).
\]

Em coordenadas \(q^A\) de \(\mathbb{CP}^1\), defina

\[
 T_A=\frac{\partial\Phi(P)}{\partial q^A}
 =
 \left(
 \frac{\partial g}{\partial q^A},
 \frac{\partial f}{\partial q^A},
 \frac{\partial\bar f}{\partial q^A}
 \right).
\]

A Hessiana induzida é exatamente o pullback

\[
 \boxed{
 \mathbb H^H_{AB}
 =
 \langle T_A,\mathbb H_{\rm GDQ}T_B\rangle_{\mathcal U_0}.
 }
\]

No setor isotrópico de \(SU(2)\), seu símbolo principal é proporcional à
métrica de Fubini--Study. O coeficiente é

\[
 \boxed{
 \kappa_HG^{\rm FS}_{AB}
 =
 \int_\gamma\frac{d\tau}{\tau}
 \int_{\mathcal N_\perp}d\mu_{\sigma_0}\,
 \mathfrak p_2
 \bigl(T_A,\mathbb H_{\rm GDQ}T_B\bigr),
 }
\]

onde \(\mathfrak p_2\) retém a parte de duas derivadas tangenciais. Esta é a
expressão formal de \(\kappa_H\) diretamente em termos da Hessiana oficial.

### 14.1 Funcional reduzido e cota topológica

Como

\[
 \operatorname{Tr}(\partial_aP\,\partial^aP)
 =\frac12\partial_an_i\partial^an_i,
\]

um pullback isotrópico positivo produz

\[
 \boxed{
 \mathcal E_H[P]
 =
 \kappa_H\int_{S^2}\operatorname{Tr}(dP\wedge*dP)
 =
 \frac{\kappa_H}{2}\int_{S^2}|dn|^2d\Omega.
 }
\]

Completando o quadrado,

\[
 \mathcal E_H
 =
 \frac{\kappa_H}{4}
 \int|dn\mp*n\times dn|^2d\Omega
 \pm4\pi\kappa_HQ,
\]

e, portanto,

\[
 \boxed{\mathcal E_H\geq4\pi\kappa_H|Q|},
 \qquad Q=c_1(P).
\]

Se \(\kappa_H>0\), os mínimos não triviais são \(Q=\pm1\).

### 14.2 Operador de Jacobi

Para um representante harmônico \(n_0:S^2\to S^2\) e uma flutuação
\(\xi\in\Gamma(n_0^*TS^2)\), \(\xi\cdot n_0=0\), a segunda variação é

\[
 \delta^2\mathcal E_H[\xi,\xi]
 =
 \kappa_H\int_{S^2}
 \langle\xi,\mathcal J_{n_0}\xi\rangle d\Omega,
\]

onde

\[
 \boxed{
 \mathcal J_{n_0}\xi
 =
 D^*D\xi
 -
 \sum_{a=1}^{2}
 R^{S^2}(\xi,dn_0(e_a))dn_0(e_a)
 +\kappa_H^{-1}V\xi.
 }
\]

\(V\) representa a parte de ordem zero induzida pelos blocos potenciais e
mistos da Hessiana oficial. Para esferas unitárias, representante identidade
\(n_0(x)=x\) e \(V=0\),

\[
 \sum_aR^{S^2}(\xi,e_a)e_a=\xi,
\qquad
 \boxed{\mathcal J_{\rm id}=D^*D-1.}
\]

Os modos zero movem o representante dentro da família de mínimos. Após sua
fixação, a forma quadrática é não negativa, também como consequência da
saturação da cota topológica.

### 14.3 O resultado que a ação atual permite

A substituição determina a forma do funcional, a cota e o operador de Jacobi,
mas os documentos atuais não especificam

\[
 P\longmapsto(g(P),f(P),\bar f(P)).
\]

Como \(P\) não é variável independente da ação oficial, inseri-lo sem esse
mapa dá \(T_A=0\) e \(\kappa_H=0\). Não é lícito acrescentar um termo de
Yang--Mills para obter o resultado.

O dado ainda necessário é um ansatz axial derivado da solução de estômato,
por exemplo

\[
 g(P)=g_0+h_in_i(P),\qquad
 f(P)=f_0+\phi_in_i(P),
\]

com \(h_i,\phi_i\) calculados pelas equações estacionárias. Só então a fórmula
em caixa avalia \(\kappa_H\), incluindo seu sinal, e determina o potencial
\(V\).

## 15. Estado da questão

A Q42 fica **fechada como reconstrução efetiva e teste de consistência**, desde
que sejam usados conjuntamente:

1. a dupla orientação de circulação já estabelecida no setor de spin;
2. a estrutura operacional de Hilbert e Born consolidada na Questão 22;
3. a representação local da cobertura dupla acima.

Ela permanece **condicional como derivação puramente global a partir da ação
oficial** em dois dados dinâmicos agora precisamente identificados:

1. obter das equações estacionárias a segunda restrição complexa
   \(\Xi_B=0\) e provar \(d\Psi\wedge d\Xi_B\ne0\); isso transforma o teorema
   local da Seção 13 numa prova de que o estômato físico possui elo \(S^3\);
2. obter da mesma solução o mapa de moduli
   \(P\mapsto(g(P),f(P),\bar f(P))\); isso permite avaliar a fórmula de
   \(\kappa_H\), provar seu sinal e calcular o termo \(V\) do operador de
   Jacobi.

Com \(\kappa_H>0\), a cota já demonstrada seleciona \(|c_1|=1\). A cobertura
de Hopf, seus autofibrados, os projetores e a álgebra local seguem então sem
postulado matricial independente.

Portanto, o resultado honesto é: a GDQ reproduz todos os resultados
operacionais de Stern–Gerlach e a cadeia geométrica foi reduzida a uma
condição topológica elementar de fronteira. O manuscrito ainda não pode
apresentar a variável \(\kappa=\pm1\), isoladamente, como derivação completa;
deve explicitar o elo \(S^3\), a conexão de Hopf e a seleção \(|c_1|=1\).

## 16. Redução axial estacionária diretamente na GDQ

### 16.1 Ansatz mínimo

Considere uma vizinhança tubular de uma folha material \(Z\) com duas
coordenadas normais complexas

\[
 (z_1,z_2)=r\,u,\qquad
 u^\dagger u=1,\qquad u\in S^3.
\]

Nas órbitas \(r=\mathrm{constante}\), use a 1-forma de Hopf

\[
 \eta=d\psi+\cos\theta\,d\phi,\qquad
 d\eta=-\Omega_2,\qquad
 \Omega_2=\sin\theta\,d\theta\wedge d\phi.
\]

O ansatz hermitiano de cohomogeneidade um mais geral com simetria axial
\(SU(2)\times U(1)\) é

\[
 \boxed{
 ds_\perp^2
 =
 a(r)^2dr^2+b(r)^2\eta^2+
 c(r)^2(d\theta^2+\sin^2\theta\,d\phi^2).
 }
\]

O background completo é

\[
 g_*=g_Z\oplus g_\perp,\qquad
 f_*=F(r)+i\Theta(r),
\]

com medida oficial

\[
 \mathcal U_*=
 \frac{e^{-F(r)}}{(4\pi\tau)^n}.
\]

No coframe

\[
 e^0=a\,dr,\quad e^3=b\,\eta,\quad
 e^1=c\,d\theta,\quad e^2=c\sin\theta\,d\phi,
\]

escolha a estrutura hermitiana

\[
 Je^0=e^3,\qquad Je^1=e^2.
\]

A forma fundamental é

\[
 \omega_*=ab\,dr\wedge\eta+c^2\Omega_2.
\]

Logo,

\[
 d\omega_*=
 Q(r)\,dr\wedge\Omega_2,\qquad
 Q(r):=(c^2)'-ab,
\]

e a torção não é um campo acrescentado:

\[
 \boxed{
 H_*=d^c\omega_*
 =
 \varsigma\,\frac{b}{a}Q(r)\,
 \eta\wedge\Omega_2,
 }
\]

onde \(\varsigma=\pm1\) fixa a convenção de \(d^c\). Esta é a inserção
Kähler--Bismut compatível com a ação oficial.

As condições locais de núcleo suave são

\[
 b(r)=r+O(r^3),\qquad
 c(r)=r+O(r^3),\qquad
 a(r)=1+O(r^2),
\]

para um centro regular. Um estômato cirúrgico de raio \(r_c>0\) substitui
essas condições por Robin em \(r=r_c\). No exterior,

\[
 a\to1,\qquad b/r\to1,\qquad c/r\to1,\qquad
 F',\Theta',H_*\to0.
\]

### 16.2 Ação radial reduzida

Denote por \(\mathcal R^B[a,b,c]\) o escalar da conexão de Bismut associado
ao par \((g_\perp,J)\) acima. Integrando as órbitas de Hopf e as direções
tangentes homogêneas, a ação oficial reduz-se a

\[
 \boxed{
 S_{\rm 1D}
 =
 C_Z\int_\gamma\frac{d\tau}{\tau}
 \int dr\,
 abc^2e^{-F}
 \left[
 \tau\left(
 \mathcal R^B+
 \frac{F'^2+\Theta'^2}{a^2}
 \right)
 +F-n
 \right],
 }
\]

onde

\[
 C_Z=
 \frac{\hbar\,\operatorname{Vol}(Z)
 \operatorname{Vol}(S^3_{\rm unit})}
 {\Lambda_C^2(4\pi\tau)^n}
\]

com a normalização angular adotada. Nenhum termo de Yang--Mills foi
introduzido.

### 16.3 Equações estacionárias

Depois de remover por integração por partes as derivadas segundas contidas em
\(\mathcal R^B\), denote o integrando radial por
\(\mathscr L_{\rm 1D}(a,b,c,F,\Theta;a',b',c',F',\Theta')\). As equações
completas no ansatz são

\[
 \boxed{
 \mathcal E_q:=
 \frac{d}{dr}\frac{\partial\mathscr L_{\rm 1D}}{\partial q'}
 -
 \frac{\partial\mathscr L_{\rm 1D}}{\partial q}=0,
 \qquad
 q\in\{b,c,F,\Theta\},
 }
\]

e

\[
 \boxed{\mathcal E_a:=\frac{\partial\mathscr L_{\rm 1D}}{\partial a}=0,}
\]

que é o vínculo radial. A equação de fase é explícita e possui primeira
integral:

\[
 \frac{d}{dr}
 \left(
 e^{-F}\frac{bc^2}{a}\Theta'
 \right)=0,
\qquad
 \boxed{
 e^{-F}\frac{bc^2}{a}\Theta'=J_\Theta.
 }
\]

Regularidade num centro com \(bc^2\sim r^3\) força \(J_\Theta=0\), salvo se
houver uma fonte ou condição singular de estômato. Portanto, a circulação
não nula exige precisamente o ramo de contorno cirúrgico; ela não emerge de
uma solução central inteiramente suave.

## 17. Teste da codimensão e da segunda restrição

No ansatz, \(r=0\) significa simultaneamente

\[
 z_1=0,\qquad z_2=0.
\]

Assim, se \(r=0\) fizer parte do domínio e for selecionado como núcleo pela
solução, a fatia normal é \(\mathbb C^2\) e o elo de qualquer tubo
\(r=\varepsilon\) é \(S^3\).

Isso não deriva uma segunda equação holomorfa da ação: ela foi incorporada ao
escolher um centro de codimensão complexa dois. A equação de fase acima
mostra ainda que um núcleo suave elimina a corrente. Para um estômato físico,
o domínio correto deve ser

\[
 r\ge r_c>0
\]

com dados de salto/Robin. A segunda condição complexa deve então vir do mapa
de colagem da borda, não de \(\rho=0\) isoladamente.

Consequentemente, o passo 3 produz o seguinte resultado negativo rigoroso:

\[
 \boxed{
 \text{a ação bulk e }Z_\rho=\{\rho=0\}\text{ não derivam, sozinhos,
 uma segunda restrição holomorfa transversal.}
 }
\]

É necessário especificar na definição do estômato o mapa de colagem
\[
 G=(G_1,G_2):\partial\mathcal N(Z)\longrightarrow\mathbb C^2
\]
com posto complexo dois, ou derivá-lo de um termo de fronteira já presente.
Projetar artificialmente uma componente de \(H_*\) como
\(\Xi_B\) não resolve o problema, porque \(H_*\) é uma 3-forma real
determinada por \(g\), não uma segunda função holomorfa independente.

## 18. Positividade, operador de Jacobi e seleção

Para o ansatz axial, a orientação global \(u\mapsto Uu\),
\(U\in SU(2)\), é uma isometria. Por isso suas variações globais são modos
zero da Hessiana. Uma textura \(P(x)\) só adquire rigidez se a solução
\((a,b,c,F,\Theta)\) depender de \(P\) quando a orientação varia ao longo da
base física.

Denotando essa solução por \(\Phi_*(P)\), o coeficiente continua sendo

\[
 \kappa_HG^{\rm FS}_{AB}
 =
 \langle\partial_A\Phi_*,
 \mathfrak p_2(\mathbb H_{\rm GDQ})
 \partial_B\Phi_*\rangle_{\mathcal U_*}.
\]

No setor euclidiano físico, o símbolo principal dos blocos escalar e
transversal métrico é não negativo depois da fixação de DeTurck e da remoção
do modo conforme. Portanto,

\[
 \boxed{\kappa_H\ge0.}
\]

A desigualdade estrita

\[
 \kappa_H>0
\]

vale se, e somente se, \(\partial_A\Phi_*\) não for um difeomorfismo,
isometria global ou modo nulo. No ansatz homogêneo escrito acima,
\(\partial_A\Phi_*\) é precisamente uma isometria; logo

\[
 \boxed{\kappa_H=0\quad\text{para a orientação global homogênea}.}
\]

Assim, não é possível provar \(\kappa_H>0\) sem construir a retroação local
do aparelho/campo magnético, que quebra a isometria e transforma \(P(x)\) em
textura física. Quando essa retroação gera \(\kappa_H>0\), o operador de
Jacobi é

\[
 \mathcal J_{n_0}
 =
 D^*D-
 \sum_aR^{S^2}(\,\cdot\,,dn_0(e_a))dn_0(e_a)
 +\kappa_H^{-1}V,
\]

e, no representante identidade sem potencial anisotrópico,

\[
 \mathcal J_{\rm id}=D^*D-1.
\]

Finalmente,

\[
 \mathcal E_H\ge4\pi\kappa_H|c_1|
\]

seleciona \(c_1=\pm1\) somente quando \(\kappa_H>0\). Para
\(\kappa_H=0\), todos os setores ficam degenerados e a seleção não ocorre.

Portanto, os passos 5 e 6 não podem ser encerrados pelo background axial
homogêneo. O ingrediente mínimo ainda ausente é a solução de resposta linear
ao campo do aparelho,

\[
 \mathbb H_{\rm GDQ}\,\delta\Phi_P
 =
 J_{\rm SG}[P,\boldsymbol B],
\]

com condições Robin no estômato. Ela fornece
\(\partial_A\Phi_*=\partial_A\delta\Phi_P\), permite avaliar
\(\kappa_H\) e decide a seleção topológica sem acrescentar campos
fundamentais à ação.

## 19. Fonte de Stern--Gerlach e resposta linear

### 19.1 Funcional de sonda

O acoplamento do aparelho não altera a ação fundamental. Ele é um funcional
externo, suportado na região de interação \(\Sigma_{\rm SG}\):

\[
 \boxed{
 S_{\rm probe}[\Phi;\boldsymbol B]
 =
 -\mu
 \int_{\Sigma_{\rm SG}}
 d\mu_\Sigma(\Phi)\,
 \operatorname{Tr}
 \bigl[P(\Phi)\,\boldsymbol\sigma\cdot\boldsymbol B(x)\bigr].
 }
\]

Aqui \(\Phi=(g,f,\bar f)\), \(P(\Phi)\) é o projetor axial reconstruído da
geometria local e \(\mu\) é o momento magnético já presente no tratamento
fenomenológico de Stern--Gerlach. Defina a diferencial geométrica

\[
 \mathcal D_\Phi P:
 \delta\Phi\longmapsto\delta P
\]

e seu adjunto em relação aos produtos internos ponderados por
\(\mathcal U_*\). A variação da medida também deve ser mantida. A fonte
completa é

\[
 \boxed{
 J_{\rm SG}
 :=
 -\left.
 \frac{\delta S_{\rm probe}}{\delta\Phi}
 \right|_{\Phi_*}
 =
 \mu(\mathcal D_\Phi P)^*
 \bigl(\boldsymbol\sigma\cdot\boldsymbol B\bigr)
 +J_{\rm vol},
 }
\]

com

\[
 J_{\rm vol}\cdot\delta\Phi
 =
 \mu\int_{\Sigma_{\rm SG}}
 \operatorname{Tr}(P_*\boldsymbol\sigma\cdot\boldsymbol B)\,
 \delta(d\mu_\Sigma).
\]

Para flutuações puramente orientacionais, que preservam o volume na primeira
ordem, \(J_{\rm vol}=0\). Em coordenadas \(q^A\) de \(\mathbb{CP}^1\),

\[
 j_A(r,x)
 =
 \mu\,\chi_{\rm SG}(x)\,
 \mathcal R_\Sigma(r)\,
 \operatorname{Tr}
 \left(
 \frac{\partial P}{\partial q^A}
 \boldsymbol\sigma\cdot\boldsymbol B(x)
 \right),
\]

onde \(\chi_{\rm SG}\) restringe a região do aparelho e
\(\mathcal R_\Sigma\) é o perfil radial com que a sonda alcança a fronteira
do estômato.

### 19.2 Problema de Robin--regularidade

Seja \(\mathbb H_R\) a Hessiana oficial com:

\[
 (\nabla_n+\mathsf R)\delta\Phi|_{r=r_c}=0,
\qquad
 \delta\Phi\ \text{regular no exterior/antípoda}.
\]

Depois de remover difeomorfismos, fase global e isometrias, suponha que
\(\mathbb H_R\) possua gap positivo no subespaço físico. A equação linear é

\[
 \boxed{\mathbb H_R\,\delta\Phi_P=J_{\rm SG}.}
\]

Sua solução causal/euclidiana é

\[
 \boxed{
 \delta\Phi_P(X)
 =
 \int G_R(X,Y)J_{\rm SG}(Y)\,d\mu_*(Y),
 \qquad
 G_R=\mathbb H_R^{-1}.
 }
\]

Essa é a resposta linear única no complemento dos modos zero.

### 19.3 Solução espectral

Decomponha o operador radial--transversal em autofunções normalizadas:

\[
 \mathbb H_R(0)\Psi_\nu=\lambda_\nu\Psi_\nu,
 \qquad
 0<\lambda_1\leq\lambda_2\leq\cdots,
\]

com as condições Robin acima. Projetando a fonte,

\[
 j_{\nu A}(x)
 =
 \langle\Psi_\nu,j_A(\,\cdot\,,x)\rangle_{\perp},
\]

obtém-se, para momento tangencial \(k\),

\[
 \boxed{
 \delta\Phi_A(k,r)
 =
 \sum_\nu
 \frac{j_{\nu A}(k)}
 {\lambda_\nu+Z_\nu k^2+O(k^4)}
 \Psi_\nu(r),
 }
\]

onde \(Z_\nu>0\) é o coeficiente do símbolo principal tangencial da Hessiana
física.

## 20. Avaliação de \(\kappa_H\)

Substituir a solução na ação quadrática fornece

\[
 S_{\rm ind}^{(2)}
 =
 -\frac12
 \langle J_{\rm SG},\mathbb H_R^{-1}J_{\rm SG}\rangle.
\]

Expandindo em pequenos momentos,

\[
 \frac1{\lambda_\nu+Z_\nu k^2}
 =
 \frac1{\lambda_\nu}
 -
 \frac{Z_\nu}{\lambda_\nu^2}k^2
 +O(k^4).
\]

O primeiro termo é a energia local de alinhamento. O segundo é a rigidez
positiva da textura. Comparando com

\[
 S_{\rm eff}^{(2)}
 \supset
 \frac12
 \int
 \kappa_{AB}^{\rm SG}
 \partial_aq^A\partial^aq^B\,dV,
\]

resulta

\[
 \boxed{
 \kappa_{AB}^{\rm SG}
 =
 \sum_{\nu}
 \frac{Z_\nu}{\lambda_\nu^2}
 j_{\nu A}^*j_{\nu B}.
 }
\]

No background isotrópico,

\[
 \kappa_{AB}^{\rm SG}
 =
 \kappa_H^{\rm SG}G^{\rm FS}_{AB},
\]

e, contraindo com a métrica inversa de Fubini--Study,

\[
 \boxed{
 \kappa_H^{\rm SG}
 =
 \frac12
 (G_{\rm FS})^{AB}
 \sum_\nu
 \frac{Z_\nu}{\lambda_\nu^2}
 j_{\nu A}^*j_{\nu B}
 >0
 }
\]

sempre que a sonda acoplar a pelo menos um modo físico
\((j_{\nu A}\ne0)\). Como \(j_{\nu A}\propto\mu B\),

\[
 \kappa_H^{\rm SG}=O(\mu^2B^2).
\]

Essa é a avaliação espectral de \(\kappa_H\) sem ajuste. Ela mostra também
que

\[
 \lim_{\boldsymbol B\to0}\kappa_H^{\rm SG}=0,
\]

como exige a simetria global do background homogêneo.

### 20.1 Potencial anisotrópico e Jacobi final

O termo de ordem \(k^0\) induz

\[
 V_{\rm SG}(P)
 =
 -\frac12
 \sum_\nu
 \frac{|j_\nu(P)|^2}{\lambda_\nu}
 -
 \mu\operatorname{Tr}
 (P\boldsymbol\sigma\cdot\boldsymbol B),
\]

e sua Hessiana tangente é

\[
 (M_{\rm SG})_{AB}
 =
 \nabla_A\nabla_BV_{\rm SG}.
\]

O operador de Jacobi completo fica

\[
 \boxed{
 \mathcal J_{\rm SG}\xi
 =
 \kappa_H^{\rm SG}
 \left[
 D^*D\xi
 -
 \sum_a
 R^{S^2}(\xi,dn_0(e_a))dn_0(e_a)
 \right]
 +
 M_{\rm SG}\xi.
 }
\]

Para campo localmente uniforme, os pontos estacionários são os dois
autofibrados instantâneos de
\(\boldsymbol n_B\cdot\boldsymbol\sigma\) (um ramo de menor e outro de maior
energia); o gradiente de
\(|\boldsymbol B|\) produz as forças opostas já derivadas na Seção 4.

### 20.2 Alcance e dado numérico ainda necessário

A fonte, a solução linear e \(\kappa_H\) estão agora determinados
formalmente pela ação e pelo perfil experimental. Para obter um número é
necessário fornecer:

1. a solução radial \(a,b,c,F,\Theta\);
2. a matriz Robin \(\mathsf R\);
3. os autovalores \(\lambda_\nu\) e pesos \(Z_\nu\);
4. o perfil físico \(\mathcal R_\Sigma(r)\boldsymbol B(x)\);
5. o mapa geométrico \(\mathcal D_\Phi P\).

Sem esses dados, qualquer valor numérico de \(\kappa_H\) seria calibração.
O resultado analítico já suficiente para a Q42 é o sinal:

\[
 \boxed{
 \boldsymbol B\ne0,\ j_{\nu A}\ne0,\ \lambda_\nu>0,\ Z_\nu>0
 \quad\Longrightarrow\quad
 \kappa_H^{\rm SG}>0.
 }
\]

Sob essas condições, a resposta ao aparelho é rígida e os projetores de Hopf
reproduzem os dois canais de Stern--Gerlach.

Essa conclusão não deve ser confundida com a seleção intrínseca do setor
topológico da partícula livre. Como
\(\kappa_H^{\rm SG}\to0\) quando \(B\to0\), a sonda não pode ser a origem de
\(|c_1|=1\); ela apenas torna observável e seleciona uma decomposição
direcional de um setor que já deve existir no sóliton incidente. A prova
intrínseca de \(|c_1|=1\) continua dependendo da rigidez do mapa de colagem do
estômato sem campo externo.

## 21. Auditoria final da fundamentação intrínseca

### 21.1 Teorema de não seleção topológica pela ação bulk local

Considere a ação oficial no domínio regular \(M^\ast\):

\[
 S_{\rm GDQ}[g,f]
 =
 \int_\gamma\frac{d\tau}{\tau}
 \int_{M^\ast}
 \left[
 \tau\left(\mathcal R+
 g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f\right)
 +\frac{f+\bar f}{2}-n
 \right]\mathcal U\,dV_g.
\]

Se \(f:M^\ast\to\mathbb C\) é uma função global, então \(e^{-f}\) é uma
seção do fibrado trivial \(L_0=M^\ast\times\mathbb C\), e

\[
 \boxed{c_1(L_0)=0.}
\]

Se \(e^{-f}\) for uma seção local de um fibrado não trivial, em duas cartas
deverá valer

\[
 e^{-f_\beta}=e^{i\chi_{\alpha\beta}}e^{-f_\alpha},
\qquad
 f_\beta=f_\alpha-i\chi_{\alpha\beta}.
\]

Então

\[
 df_\beta=df_\alpha-i\,d\chi_{\alpha\beta}.
\]

O termo oficial \(|df|^2\) não é invariante quando
\(d\chi_{\alpha\beta}\ne0\). Para torná-lo global seria necessária uma
conexão local \(A_\alpha\) com

\[
 A_\beta=A_\alpha+d\chi_{\alpha\beta},
\qquad
 Df_\alpha=df_\alpha-iA_\alpha,
\]

ou uma formulação equivalente em termos da conexão hermitiana induzida. Essa
estrutura não aparece explicitamente no funcional oficial.

Portanto,

\[
 \boxed{
 \text{a ação oficial, tomada literalmente com }f\text{ global, só descreve
 o setor }c_1=0.
 }
\]

Além disso, uma equação de Euler--Lagrange local preserva a topologia do
domínio: ela não cria por si só um fibrado com \(c_1=\pm1\), nem transforma
um nó genérico de codimensão real dois num defeito de codimensão real quatro.

### 21.2 Resultado dos passos solicitados

#### A. Codimensão

Foi provado:

\[
 F=(F_1,F_2),\quad
 \operatorname{rank}_{\mathbb C}dF=2
 \Longrightarrow
 N_{Z/M}\simeq\mathbb C^2,\quad
 \operatorname{Link}(Z)=S^3.
\]

Não foi derivado da ação que o estômato satisfaça essas duas equações.
\(\rho=0\), isoladamente, é insuficiente.

#### B. Colagem e classe de Chern

Foi construído o mapa de Hopf e demonstrado:

\[
 c_1(L)
 =
 \deg g_{NS}
 =
 \frac1{2\pi}\int_{S^2}\mathcal F_H.
\]

Para o mapa elementar, \(c_1=\pm1\). Escolher esse mapa, porém, é escolher um
setor topológico de fronteira; o bulk não o seleciona.

#### C. Rigidez intrínseca

Para a orientação global homogênea,

\[
 \kappa_H^{(0)}=0,
\]

porque \(SU(2)\) age por isometrias. Uma rigidez positiva para texturas
exigiria que \(P(x)\) fosse um grau de liberdade induzido de
\((g,f,\bar f)\). Sem o mapa \(P\mapsto(g(P),f(P),\bar f(P))\), esse setor não
existe na Hessiana oficial.

#### D. Bismut e circulação

A conexão de Hopf

\[
 \mathcal A_H=-iu^\dagger du
\]

e a torção de Bismut

\[
 H=d^c\omega
\]

têm graus diferentes: a primeira é uma 1-forma de conexão \(U(1)\), e a
segunda é uma 3-forma real. Uma igualdade direta é impossível. A ponte deve
ser uma redução ou transgressão explícita, por exemplo

\[
 \mathcal F_{\rm eff}
 =
 \pi_*H,
\]

onde \(\pi_*\) é a integração na fibra \(S^1\), com fibra, normalização e
orientação especificadas; localmente
\(d\mathcal A_{\rm eff}=\mathcal F_{\rm eff}\). Essa transgressão ainda não
foi dada no manuscrito.

### 21.3 Menor fechamento mantendo a ação oficial intacta

Não é necessário alterar o integrando bulk. É necessário completar o espaço
de configurações e as condições de fronteira:

1. declarar o estômato fermiônico como interseção completa complexa de
   codimensão dois;
2. remover seu tubo normal e impor na fronteira \(S^3\) o fibrado de Hopf
   elementar \(L_{\pm1}\to S^2\);
3. tratar \(f_\alpha\) por cartas e interpretar sua derivada global através
   da conexão hermitiana Kähler--Bismut induzida;
4. fornecer a transgressão que relaciona \(H\) a \(\mathcal A_H\);
5. tratar \(c_1=\pm1\) como condição topológica admissível de carga mínima,
   preservada pelo fluxo, e não como número criado pela variação local.

Com esses dados, a ação oficial permanece formalmente igual em cada
trivialização local, mas o problema global passa a estar bem definido.

### 21.4 Veredito

\[
 \boxed{
 \begin{aligned}
 &\text{Hopf, projetores, álgebra, Born e resposta SG: derivados;}\\
 &\mathbb C^2\Rightarrow S^3:\text{ provado sob transversalidade;}\\
 &c_1=\pm1:\text{ calculado para o mapa elementar;}\\
 &\text{seleção intrínseca pela ação bulk atual: impossível.}
 \end{aligned}
 }
\]

Os passos foram levados até o limite lógico da ação oficial. Declarar que
ela, sem dados globais adicionais, deriva \(c_1=\pm1\) seria incorreto.

## 22. Interação clássica como modificação do contorno

### 22.1 Ação de fronteira do aparelho

Seja \(\Phi_\partial\) a restrição dos modos físicos do sóliton à fronteira
do estômato. O ímã é tratado como fonte clássica externa por meio do
funcional de interface

\[
 \boxed{
 S_{\partial,{\rm SG}}
 =
 \frac12\int_{\partial\mathcal N_{r_c}}
 \Phi_\partial^\dagger
 \mathsf R(\boldsymbol B)
 \Phi_\partial\,d\Sigma,
 }
\]

com operador hermitiano

\[
 \boxed{
 \mathsf R(\boldsymbol B)
 =
 \mathsf R_0I+
 r_B(\boldsymbol x)\,
 \boldsymbol n(\boldsymbol x)\cdot\boldsymbol\sigma,
 \qquad
 \boldsymbol n=\frac{\boldsymbol B}{|\boldsymbol B|}.
 }
\]

A variação da soma da ação bulk com \(S_{\partial,{\rm SG}}\) fornece

\[
 \boxed{
 \left(
 \nabla_r+\mathsf R(\boldsymbol B)
 \right)\Phi_\partial=0.
 }
\]

Como \(\mathsf R=\mathsf R^\dagger\), essa condição anula a forma de Green no
bordo e define uma extensão auto-adjunta do operador de flutuações.

### 22.2 Diagonalização em dois canais

Usando

\[
 P_{\boldsymbol n}^{\pm}
 =
 \frac12(I\pm\boldsymbol n\cdot\boldsymbol\sigma),
\]

temos

\[
 \mathsf R(\boldsymbol B)
 =
 (\mathsf R_0+r_B)P_{\boldsymbol n}^{+}
 +
 (\mathsf R_0-r_B)P_{\boldsymbol n}^{-}.
\]

Portanto,

\[
 \Phi_\partial=\Phi_++\Phi_-,
\qquad
 \Phi_\pm=P_{\boldsymbol n}^{\pm}\Phi_\partial,
\]

e as condições desacoplam:

\[
 \boxed{
 (\nabla_r+\mathsf R_0\pm r_B)\Phi_\pm=0.
 }
\]

Os dois canais são soluções estacionárias ortogonais. Eles não precisam ser
dois mínimos equivalentes: o campo desloca suas energias em sentidos
opostos. A estabilidade exige separadamente que os menores autovalores dos
dois operadores Robin permaneçam não negativos.

## 23. Conservação da medida e pesos de entrada

Para um estado incidente \(u_{\boldsymbol a}\),

\[
 u_{\boldsymbol a}
 =
 P_{\boldsymbol n}^{+}u_{\boldsymbol a}
 +
 P_{\boldsymbol n}^{-}u_{\boldsymbol a}.
\]

Como os projetores são ortogonais,

\[
 \|u_{\boldsymbol a}\|^2
 =
 \|P_{\boldsymbol n}^{+}u_{\boldsymbol a}\|^2+
 \|P_{\boldsymbol n}^{-}u_{\boldsymbol a}\|^2.
\]

Identificando a norma com a medida conservada da Q22:

\[
 p_\pm
 =
 \int\mathcal U_\pm\,dV
 =
 \|P_{\boldsymbol n}^{\pm}u_{\boldsymbol a}\|^2,
\]

resulta

\[
 \boxed{
 p_\pm
 =
 \frac{1\pm\boldsymbol a\cdot\boldsymbol n}{2}.
 }
\]

Assim, a alteração Robin escolhe a decomposição, mas não altera
arbitrariamente os pesos de entrada.

## 24. Decoerência produzida pelo instrumento

Inclua um estado macroscópico do aparelho \(A_0\). A evolução conjunta
produz

\[
 u_{\boldsymbol a}\otimes A_0
 \longrightarrow
 c_+\Phi_+\otimes A_+
 +
 c_-\Phi_-\otimes A_-,
\]

com

\[
 |c_\pm|^2=p_\pm.
\]

Ao eliminar os graus macroscópicos, o termo de interferência é multiplicado
por

\[
 D(t)=\langle A_-(t)|A_+(t)\rangle.
\]

Para um aparelho macroscópico,

\[
 |D(t)|\longrightarrow0,
\]

e a matriz reduzida torna-se

\[
 \rho_{\rm red}
 \longrightarrow
 p_+|\Phi_+\rangle\langle\Phi_+|
 +
 p_-|\Phi_-\rangle\langle\Phi_-|.
\]

Uma parametrização efetiva compatível com positividade é

\[
 \dot\rho
 =
 -\frac{i}{\hbar}[H_{\rm eff},\rho]
 -
 \frac{\Gamma_{\rm SG}}{2}
 [S_{\boldsymbol n},[S_{\boldsymbol n},\rho]],
\]

que fornece

\[
 \rho_{+-}(t)
 =
 e^{-\Gamma_{\rm SG}t}\rho_{+-}(0).
\]

\(\Gamma_{\rm SG}\) ainda deve ser calculada pelo espectro da Hessiana
acoplada ao aparelho; ela não deve ser escolhida para reproduzir o resultado.

## 25. Registro único como captura estocástica

A decoerência explica a mistura efetiva, mas não seleciona sozinha um único
registro. A GDQ já possui uma dinâmica difusiva da medida, permitindo
formular a seleção como um problema de primeiro alcance.

Sejam \(D_+\) e \(D_-\) as duas regiões absorventes do detector. Para uma
trajetória individual \(X_t\), defina

\[
 T_\pm=\inf\{t:X_t\in D_\pm\}.
\]

O registro é

\[
 R=
 \begin{cases}
 +,&T_+<T_-,\\
 -,&T_-<T_+.
 \end{cases}
\]

Se \(\mathcal L_{\rm GDQ}\) é o gerador estocástico efetivo depois da
separação dos canais, a probabilidade de captura superior é a solução do
problema de Dirichlet:

\[
 \boxed{
 \mathcal L_{\rm GDQ}h_+=0,
 \qquad
 h_+|_{D_+}=1,
 \qquad
 h_+|_{D_-}=0.
 }
\]

Então

\[
 \mathbb P(R=+|X_0=x)=h_+(x),
\qquad h_-=1-h_+.
\]

Para reproduzir Born sem hipótese adicional é necessário demonstrar que a
quantidade

\[
 M_t=
 \operatorname{Tr}
 \bigl(\rho_tP_{\boldsymbol n}^{+}\bigr)
\]

é um martingal até o tempo de captura. Pelo teorema da parada opcional:

\[
 \mathbb E[M_T]=M_0.
\]

Como no detector \(M_T\in\{0,1\}\),

\[
 \boxed{
 \mathbb P(R=+)
 =
 M_0
 =
 \operatorname{Tr}
 (\rho_0P_{\boldsymbol n}^{+})
 =
 \cos^2\frac{\theta}{2}.
 }
\]

Analogamente,

\[
 \mathbb P(R=-)=\sin^2\frac{\theta}{2}.
\]

Esse mecanismo produz um único evento por trajetória e a distribuição de
Born no conjunto, sem fazer todos os estados relaxarem para o ramo de menor
energia.

### 25.1 Pendência matemática exata

Para transformar a captura em teorema da GDQ, falta:

1. derivar \(\mathcal L_{\rm GDQ}\) da ação e da medida após a condição
   Robin matricial;
2. provar existência e unicidade do processo absorvente;
3. demonstrar \(\mathcal L_{\rm GDQ}M=0\), isto é, a propriedade de
   martingal;
4. verificar as hipóteses de integrabilidade do teorema da parada opcional;
5. calcular \(\Gamma_{\rm SG}\) e o tempo médio de captura.

Essa é agora a formulação precisa do problema de resultado único.

## 26. Gerador estocástico condicionado da GDQ

### 26.1 Limite de medição contínua

No interior do aparelho, as flutuações rápidas da impedância Robin são
escritas como

\[
 \mathsf R(t)
 =
 \overline{\mathsf R}
 +
 \xi(t)\,\boldsymbol n\cdot\boldsymbol\sigma,
\qquad
 \mathbb E[\xi(t)]=0.
\]

No limite de correlação curta da medida de Wiener da GDQ,

\[
 \mathbb E[\xi(t)\xi(t')]
 =
 2D_R\delta(t-t').
\]

Depois de eliminar os modos de fronteira, a dinâmica condicionada do setor
de dois canais assume a forma de Itô

\[
 \boxed{
 \begin{aligned}
 d\rho_t={}&
 -\frac{i}{\hbar}[H_{\rm ad},\rho_t]dt
 +\Gamma_{\rm SG}
 \left(
 \sigma_{\boldsymbol n}\rho_t\sigma_{\boldsymbol n}-\rho_t
 \right)dt\\
 &+
 \sqrt{\eta\Gamma_{\rm SG}}\,
 \left[
 \sigma_{\boldsymbol n}\rho_t+
 \rho_t\sigma_{\boldsymbol n}
 -
 2\langle\sigma_{\boldsymbol n}\rangle_t\rho_t
 \right]dW_t,
 \end{aligned}
 }
\]

onde

\[
 \sigma_{\boldsymbol n}
 =
 \boldsymbol n\cdot\boldsymbol\sigma,
\qquad
 dW_t^2=dt.
\]

\(\eta=1\) descreve o condicionamento pela totalidade do ambiente/aparelho;
\(0<\eta<1\) representa perda de informação no registro observado. O termo
determinístico preserva traço e positividade e elimina coerências entre os
dois projetores.

### 26.2 Origem espectral de \(\Gamma_{\rm SG}\)

Se \(X_R(t)\) é a flutuação efetiva da impedância acoplada a
\(\sigma_{\boldsymbol n}\), sua correlação estacionária possui decomposição

\[
 C_R(t)
 =
 \langle X_R(t)X_R(0)\rangle
 =
 \sum_\nu C_\nu e^{-\lambda_\nu|t|},
\qquad C_\nu\ge0.
\]

No limite markoviano,

\[
 \boxed{
 \Gamma_{\rm SG}
 =
 \frac{\mu^2}{\hbar^2}
 \int_0^\infty C_R(t)\,dt
 =
 \frac{\mu^2}{\hbar^2}
 \sum_\nu\frac{C_\nu}{\lambda_\nu}
 >0.
 }
\]

Os pesos \(C_\nu\) são quadráticos nas projeções \(j_{\nu A}\) da fonte
Robin. Portanto, \(\Gamma_{\rm SG}\) e \(\kappa_H^{\rm SG}\) vêm do mesmo
espectro positivo, embora sejam momentos espectrais diferentes.

## 27. Prova do martingal de Born

Defina

\[
 p_t
 =
 \operatorname{Tr}(P_{\boldsymbol n}^{+}\rho_t)
 =
 \frac{1+\langle\sigma_{\boldsymbol n}\rangle_t}{2}.
\]

No regime adiabático,

\[
 [H_{\rm ad},P_{\boldsymbol n}^{+}]=0.
\]

Aplicando o traço da equação de Itô:

1. o comutador não contribui;
2. o termo de decoerência não modifica as populações diagonais;
3. resta apenas o termo de inovação.

Obtém-se

\[
 \boxed{
 dp_t
 =
 4\sqrt{\eta\Gamma_{\rm SG}}\,
 p_t(1-p_t)\,dW_t.
 }
\]

Não existe termo proporcional a \(dt\). Portanto, para o gerador de Itô
\(\mathscr L_{\rm meas}\),

\[
 \boxed{\mathscr L_{\rm meas}p=0.}
\]

Como \(0\le p_t\le1\), \(p_t\) é um martingal limitado e uniformemente
integrável:

\[
 \mathbb E[p_t|\mathcal F_s]=p_s,
\qquad
 \mathbb E[p_t]=p_0.
\]

### 27.1 Convergência para um resultado

Para \(\eta=1\), a variância condicional da inovação é

\[
 d[p]_t
 =
 16\Gamma_{\rm SG}p_t^2(1-p_t)^2dt.
\]

A observação contínua acumula informação enquanto
\(0<p_t<1\). O teorema de convergência de martingais garante a existência de
\(p_\infty\). Se a medição permanece ativa por tempo arbitrariamente longo,
um limite no interior manteria variância quadrática positiva e não poderia
ser estacionário. Assim,

\[
 \boxed{p_\infty\in\{0,1\}\quad\text{quase certamente}.}
\]

Como a esperança é conservada,

\[
 \mathbb P(p_\infty=1)
 =
 \mathbb E[p_\infty]
 =
 \mathbb E[p_0]
 =
 p_0.
\]

Logo,

\[
 \boxed{
 \mathbb P(+)
 =
 p_0
 =
 \operatorname{Tr}(\rho_0P_{\boldsymbol n}^{+})
 =
 \cos^2\frac{\theta}{2},
 }
\]

e

\[
 \boxed{
 \mathbb P(-)=1-p_0=\sin^2\frac{\theta}{2}.
 }
\]

Matematicamente, o limite \(0\) ou \(1\) é assintótico. Um detector físico
registra o resultado quando \(p_t\) atravessa um limiar
\(\varepsilon\) ou \(1-\varepsilon\); o tempo de registro é então finito com
probabilidade arbitrariamente próxima de um.

### 27.2 Condições de validade

A prova exige:

1. \(\Gamma_{\rm SG}>0\);
2. eficiência física total \(\eta=1\) quando todos os canais ambientais são
   incluídos;
3. regime adiabático
   \([H_{\rm ad},P_{\boldsymbol n}^{\pm}]=0\);
4. ausência de termos de deriva que transfiram população entre os canais;
5. validade do limite markoviano durante a janela de medição.

Fora do regime adiabático aparecem transições de Landau--Zener entre os
canais, e \(p_t\) deixa de ser martingal para o projetor instantâneo. Isso é
uma previsão física, não uma falha do mecanismo.

## 28. Significado geométrico do resultado único

O processo não destrói globalmente a solução nem força todos os sólitons ao
nível de menor energia. Em cada realização, as flutuações da impedância
Robin transferem informação continuamente para o aparelho. A condição de
fronteira efetiva converge para um dos setores:

\[
 \mathsf R_{\rm eff}
 \longrightarrow
 \begin{cases}
 \mathsf R_0+r_B,&p_\infty=1,\\
 \mathsf R_0-r_B,&p_\infty=0.
 \end{cases}
\]

O “colapso” é, assim, a convergência condicionada da solução de contorno em
uma trajetória individual. A média não condicionada continua sendo a mistura
decoerente com pesos de Born.

O ponto ainda não calculado numericamente é o valor de
\(\Gamma_{\rm SG}\) **em unidades físicas**, que requer o espectro Robin do
background GDQ estacionário. Um espectro radial reduzido já foi calculado
como teste do método, mas não deve ser confundido com essa previsão. A
regra de Born e o caráter de resultado único, entretanto, seguem do sinal
positivo e da estrutura martingal, não do valor particular dessa taxa.

## 29. Verificação numérica do limite não adiabático

Para tornar explícita a terceira condição da Seção 27.2, foi integrado o
Hamiltoniano reduzido

\[
 H(t)=\frac12\left(vt\,\sigma_z+\Delta\,\sigma_x\right),
 \qquad \hbar=1.
\]

Partindo do estado fundamental instantâneo antes do cruzamento, a
probabilidade de terminar no ramo excitado satisfaz, no limite de varredura
assintótica,

\[
 P_{\rm LZ}=\exp\!\left(-\frac{\pi\Delta^2}{2v}\right).
\]

O solver em `questoes/q42/associados/simulate_nonadiabatic_q42.py`, para \(\Delta=1\) e
\(v\in[0.2,3.2]\), reproduziu essa expressão com erro absoluto máximo
\(2.92\times10^{-4}\). A troca de ramo cresce com \(v\), como esperado.

Além disso, a evolução de
\(p_z=\operatorname{Tr}(P_z^+\rho)\) contém o termo

\[
 \left.dp_z\right|_H
 =-i\operatorname{Tr}\!\left(P_z^+[H,\rho]\right)dt.
\]

O teste forneceu \(\|[H,P_z^+]\|=1/\sqrt2\) e, para um estado de prova,
\(dp_z/dt=1/2\). Portanto, fora do setor QND/adiabático, \(p_z\) não é
martingal e a demonstração de primeiro alcance não se aplica literalmente.
Isso delimita com precisão o resultado: a geometria de contorno ainda define
os dois canais, porém uma passagem rápida pode transferir população entre
eles antes da captura.

O cálculo não constitui ainda uma previsão dimensional da GDQ. Para isso,
\(\Delta\) e \(v\) devem ser obtidos, respectivamente, da separação espectral
Robin física e do perfil espaço-temporal do campo do aparelho sobre o
background GDQ.

## 30. Coeficientes dimensionais e contrato do background GDQ

Com a convenção física

\[
 H_2=\frac{\hbar}{2}
 (\omega_\parallel\sigma_z+\omega_\perp\sigma_x),
 \qquad
 H_Z=-\frac{g_{\rm geom}\mu_B}{2}\boldsymbol\sigma\cdot\boldsymbol B,
\]

os parâmetros de Landau--Zener são

\[
 \boxed{\Delta=
 \frac{|g_{\rm geom}|\mu_B}{\hbar}|B_\perp|},
 \qquad
 \boxed{v=
 \frac{|g_{\rm geom}|\mu_B}{\hbar}
 |\partial_tB_\parallel+\boldsymbol u\cdot\nabla B_\parallel|}.
\]

Assim, \(\Delta\) e \(v\) são derivados do acoplamento Zeeman geométrico e
das condições externas do aparelho. Não devem ser extraídos por ajuste das
frequências de saída.

Para o setor de resposta do background, sejam \(\lambda_\nu\) os autovalores
positivos da Hessiana estática, \(Z_\nu\) seus coeficientes tangenciais e
\(j_{\nu A}\) as projeções da fonte. Então

\[
 \boxed{\kappa_H^{\rm SG}=
 \frac12(G_{\rm FS})^{AB}
 \sum_\nu\frac{Z_\nu j_{\nu A}^*j_{\nu B}}{\lambda_\nu^2}}.
\]

Se \(C_\nu\) são os pesos da covariância da impedância e
\(\gamma_\nu\) as taxas de relaxação causal,

\[
 \boxed{\Gamma_{\rm SG}=
 \frac{\mu^2}{\hbar^2}\sum_\nu\frac{C_\nu}{\gamma_\nu}}.
\]

Não se deve identificar automaticamente \(\gamma_\nu\) com
\(\lambda_\nu\): a primeira é uma taxa e a segunda é curvatura da ação. A
relação entre ambas exige a mobilidade/métrica cinética do fluxo causal.

### 30.1 Auditoria da possibilidade de avaliação

A busca integral no manuscrito mostra que o background radial mencionado na
Seção 20.2 não foi ainda construído. Os perfis
\(a(r),b(r),c(r),F(r),\Theta(r)\) não possuem ansatz métrico definido,
equações radiais, dados Robin e solução normalizada em outro documento. Da
mesma forma, não estão dados os pesos \(C_\nu\) nem a mobilidade causal.

Consequentemente, substituir agora os números reduzidos por números chamados
“físicos” seria uma calibração não derivada. Os testes antigos foram mantidos
como histórico. A nova camada numérica contém:

1. `test_physical_zeeman_q42.py`, que calcula \(\Delta\) e \(v\) em SI para
   dados explícitos do aparelho;
2. `evaluate_gdq_background_q42.py`, que avalia
   \(\kappa_H^{\rm SG}\) e \(\Gamma_{\rm SG}\) somente ao receber o espectro
   físico completo;
3. `test_background_pipeline_q42.py`, que valida a álgebra com dados
   sintéticos claramente marcados como não físicos.

O contrato mínimo do futuro arquivo `background_q42.npz` é:

\[
 \{\lambda_\nu,Z_\nu,j_{\nu1},j_{\nu2},\gamma_\nu,C_\nu\}.
\]

A substituição definitiva estará concluída quando esse arquivo for produzido
pela solução estacionária e pela Hessiana da ação oficial, não por uma
escolha manual de potencial.

## 31. Construção explícita do background estacionário de bulk

Na fatia normal \(\mathbb C^2\), tome

\[
 ds_\perp^2=dr^2+a(r)^2d\Omega_3^2,
 \qquad f=F(r)\in\mathbb R.
\]

A equação estacionária métrico--dilatônica reduz-se a

\[
 -3\frac{a''}{a}+F''=\frac1{2\tau},
\]

\[
 \frac{2(1-a'^2)-aa''}{a^2}
 +\frac{F'a'}a=\frac1{2\tau}.
\]

Ambas são resolvidas exatamente por

\[
 \boxed{a_*(r)=r},
 \qquad
 \boxed{F_*(r)=\frac{r^2}{4\tau}+F_0}.
\]

Para o exterior excisado \(r\ge r_c\), a normalização determina

\[
 x_c=\frac{r_c^2}{4\tau},
 \qquad
 \boxed{F_0=\log[e^{-x_c}(1+x_c)]}.
\]

O programa `questoes/q42/associados/build_stationary_background_q42.py` verificou, para
\(\tau=1\), \(r_c=0.1\) e \(r_{\max}=12\):

\[
 \max|\mathrm{Ric}+\nabla^2F-g/(2\tau)|=0,
\]

e normalização truncada \(0.9999999972457\). Portanto, este é um background
estacionário real da ação no bulk, e substitui legitimamente o potencial
gaussiano arbitrário usado no primeiro teste de código.

### 31.1 Obstrução de bordo encontrada pela construção

No bordo interior, a normal exterior é \(n=-\partial_r\), de modo que

\[
 \boxed{n\cdot\nabla F_*=-\frac{r_c}{2\tau}\ne0.}
\]

Na execução acima, esse fluxo vale \(-0.05\). Logo, a excisão produz um termo
de primeira variação no estômato. A ação oficial de bulk não declara um termo
de contorno nem quais dados métrico--dilatônicos são fixados ali. Ela não
seleciona, por si só, uma matriz Robin \(\mathsf R_0\).

Este resultado separa rigorosamente duas afirmações:

1. o background estacionário do **bulk** foi construído e verificado;
2. o background estacionário do **estômato como problema de bordo** continua
   subdeterminado até fixar uma classe variacional: Dirichlet, Robin externo
   ou uma ação de contorno GDQ bem posta.

Sem esse domínio auto-adjunto não existem \(\lambda_\nu\) físicos únicos.
Sem a mobilidade causal e a covariância térmica também não existem
\(\gamma_\nu,C_\nu\) únicos. Consequentemente, \(\Delta\) e \(v\) já podem
ser avaliados para um aparelho especificado, enquanto
\(\kappa_H^{\rm SG}\) e \(\Gamma_{\rm SG}\) permanecem formalmente derivados,
mas numericamente condicionados à conclusão variacional do contorno.

## 32. Completação variacional e seleção do raio

Para que a variação do termo \(e^{-F}R\) seja bem posta na variedade
excisada, acrescenta-se a completação de Gibbons--Hawking ponderada

\[
 S_{\partial}=2C_\tau
 \int_{\partial M_*}e^{-F}K\,dA.
\]

Ela não modifica as equações da ação oficial no bulk. Sob um deslocamento
normal livre da fronteira, a primeira variação é proporcional à curvatura
média ponderada

\[
 K_F=K-nF.
\]

No bordo interior do background gaussiano,

\[
 K=-\frac3{r_c},
 \qquad nF=-\frac{r_c}{2\tau}.
\]

Logo a condição estacionária \(K_F=0\) fornece

\[
 \boxed{r_c=\sqrt{6\tau}}.
\]

Para \(\tau=1\), o teste numérico encontrou

\[
 r_c=2.449489742783,
 \quad K=nF=-1.224744871392,
 \quad |K_F|=2.22\times10^{-16}.
\]

Assim, o raio do ramo de bordo livre foi derivado, em vez de calibrado. A
condição linearizada da Hessiana é

\[
 \boxed{\mathcal B_F(h,\varphi)
 =\delta K[h]-n\varphi-\delta n[h](F_*)=0.}
\]

Ela é uma Robin matricial métrico--dilatônica. Para métrica congelada,
reduz-se a Neumann para \(\varphi\). O aparelho acrescenta a parte axial
\(\pm r_B\), mas a intensidade \(r_B\) ainda depende da segunda variação de
\(S_{\rm probe}\) e do mapa geométrico \(\mathcal D_\Phi P\); não é produzida
pelo termo Gibbons--Hawking comum.

## 33. Segunda variação da sonda e separação dos canais

Para \(\boldsymbol B=B\hat z\), o potencial sobre o espaço de projetores é

\[
 V_Z(P)=-\mu B\,\boldsymbol n(P)\cdot\hat z.
\]

Em coordenadas tangentes \(\eta\) nos dois polos de \(S^2\),

\[
 V_Z[n_+]=-mu B+\frac{\mu B}{2}|\eta|^2+O(|\eta|^4),
\]

\[
 V_Z[n_-]=+\mu B-\frac{\mu B}{2}|\eta|^2+O(|\eta|^4).
\]

Portanto,

\[
 \boxed{\operatorname{Hess}V_Z|_+=+\mu B I_2},
 \qquad
 \boxed{\operatorname{Hess}V_Z|_-=-\mu B I_2}.
\]

Se \(\mathsf Z_\partial\) é a forma principal da Hessiana no traço dos modos
localizados, a variação de bordo fornece

\[
 -\mathsf Z_\partial\partial_r\eta_\pm
 +\operatorname{Hess}_P S_{\rm probe}|_\pm\eta_\pm=0,
\]

isto é,

\[
 \boxed{
 \mathsf R_{\rm SG}^{\pm}
 =\mathsf Z_\partial^{-1}
 \operatorname{Hess}_P S_{\rm probe}|_\pm},
 \qquad
 \boxed{(-\partial_r+\mathsf R_{\rm SG}^{\pm})\eta_\pm=0.}
\]

Na coordenada \(x=r/\sqrt\tau\), o parâmetro espectral é

\[
 \boxed{\beta_B=\sqrt\tau\,r_B}
\]

para cada autovalor escalar \(r_B\) do operador localizado. Assim, o sinal e
a dependência em campo foram derivados sem dividir pela rigidez global. Uma
orientação global do background isotrópico é modo zero; ela não é a
normalização de traço \(\mathsf Z_\partial\).

### 33.1 Primeiro espectro sobre o background derivado

Com o peso exato

\[
 w(x)=x^3e^{-x^2/4},
 \qquad x_c=\sqrt6,
\]

foi discretizado o operador mínimo

\[
 L_\pm=-\frac1w\partial_x(w\partial_x),
\]

mantendo \(V_H=0\) para isolar o símbolo principal. No teste diagnóstico
\(\beta_B=0.05\), com 2400 pontos,

\[
 \lambda_1^+=0.03562212208,
 \qquad
 \lambda_1^-=-0.03790647948.
\]

O sinal confirma diretamente a análise da segunda variação: o canal alinhado
é mínimo, enquanto o antiparalelo é um ramo estacionário excitado. Portanto,
os dois resultados de Stern--Gerlach não podem ser explicados como dois
mínimos equivalentes de relaxação. A dinâmica unitária/condicionada e a
captura do detector são essenciais para preservar e registrar o ramo
excitado.

O valor \(\beta_B=0.05\) serve apenas para testar o operador; não é uma
previsão física. A avaliação quantitativa vem diretamente da resposta
localizada do estômato.

## 34. Avaliação direta de \(Z_H\) no background gaussiano

Fixando uma orientação unitária no bordo, \(Z_H\) é o operador
Dirichlet--to--Neumann da Hessiana axial minimizada no exterior. Para o
símbolo principal do shrinker gaussiano,

\[
 Q[\eta]=\frac{Z_{\rm bulk}}2
 \int_{r_c}^{\infty}r^3e^{-r^2/(4\tau)}|\eta'|^2dr.
\]

A equação é

\[
 (r^3e^{-r^2/(4\tau)}\eta')'=0.
\]

Entretanto,

\[
 \int_r^\infty s^{-3}e^{s^2/(4\tau)}ds=\infty,
\]

de modo que não existe solução clássica localizada de energia mínima com
\(\eta(r_c)=1\) e \(\eta(\infty)=0\). Além disso, uma sequência que mantém
\(\eta=1\) até \(R\) e realiza a transição numa camada posterior satisfaz

\[
 Q[\eta_R]\longrightarrow0.
\]

Logo,

\[
 \boxed{Z_H^{\rm gaussiano}=0.}
\]

O teste numérico deslocou a camada de \(3\sqrt\tau\) para
\(9\sqrt\tau\), reduzindo a energia de \(1.003877\) para
\(1.3500\times10^{-7}\), uma razão \(1.3448\times10^{-7}\).

Este resultado corrige o alcance da Seção 31: o shrinker gaussiano é uma
solução exata do bulk e fixa a geometria normal mínima, mas não é um estômato
físico completo capaz de localizar a orientação de spin. A rotação global
continua sendo modo zero.

Para obter uma resposta localizada positiva, a Hessiana da solução não
homogênea deve produzir

\[
 L_H=-w^{-1}\partial_r(w\partial_r)+V_H(r)
\]

com potencial axial, conexão não trivial ou termo cinético de bordo que
remova o modo zero. Somente então

\[
 Z_H=Z_{\rm bulk}[-n\cdot D\eta(r_c)]>0
\]

e o operador Robin localizado se torna finito. Portanto, o próximo passo é
derivar \(V_H\) dos blocos acoplados da Hessiana métrico--dilatônica de uma
solução de estômato não homogênea; não há valor físico de \(Z_H\) no ramo
gaussiano puro.

## 35. Ramo cilíndrico com garganta de Hopf

A ação estacionária admite também o background

\[
 M_\perp=\mathbb R_+\times S^3_a,
 \qquad
 ds^2=dr^2+a^2d\Omega_3^2,
 \qquad
 F=\frac{r^2}{4\tau}+F_0.
\]

As componentes radial e esférica de
\(\operatorname{Ric}+\nabla^2F=g/(2\tau)\) fornecem

\[
 \boxed{a=2\sqrt\tau}.
\]

No bordo \(r=0\), \(K=0=nF\), de modo que a condição variacional ponderada
é satisfeita automaticamente. A normalização determina

\[
 \boxed{F_0=\frac12\log\pi}.
\]

As componentes do mapa de Hopf são harmônicos de grau \(l=2\) em \(S^3\).
Consequentemente,

\[
 -\Delta_{S^3_a}n_i
 =\frac8{a^2}n_i
 =\frac2\tau n_i,
\]

e a Hessiana axial contém o potencial geométrico

\[
 \boxed{V_H=\frac2\tau>0}.
\]

Esse termo remove o modo zero encontrado no ramo gaussiano. Em
\(x=r/\sqrt\tau\), o perfil Dirichlet--to--Neumann satisfaz

\[
 -\eta''+\frac{x}{2}\eta'+2\eta=0,
 \quad \eta(0)=1,
 \quad \eta(\infty)=0.
\]

A solução é proporcional a
\(U(2,\tfrac12,x^2/4)\), e fornece exatamente

\[
 \boxed{z_H=-\eta'(0)=\frac{3\sqrt\pi}{4}}
 =1.329340388179\ldots
\]

O solver convergiu para esse valor já em \(x_{\max}=8\), com estabilidade em
12 casas nas extensões até \(x_{\max}=12\). Portanto,

\[
 \boxed{\mathcal N_H=\frac{\mathsf Z_\partial}{\sqrt\tau}
 \frac{3\sqrt\pi}{4}},
\]

\[
 \boxed{
 \mathsf R_{\rm SG}^{\pm}
 =\pm\mathcal N_H^{-1}
 \operatorname{Hess}_P S_{\rm probe}|_\pm}.
\]

O fator radial universal de resposta foi assim obtido sem ajuste. A matriz
\(\mathsf Z_\partial\) é calculada nos modos localizados da Hessiana, não no
modo global de isometria. Além disso, a seleção do ramo cilíndrico em relação ao ramo
gaussiano exige comparação on-shell e análise completa de estabilidade.

## 36. Comparação on-shell dos dois ramos

Incluindo a completação de bordo, o funcional normal reduzido é

\[
 \mathcal W_4=
 \int_M[\tau(R+|\nabla F|^2)+F-4]d\mu
 +2\tau\int_{\partial M}\mathcal U K\,dA.
\]

Para o exterior gaussiano livre, \(x_c=3/2\), e

\[
 \mathcal W_{\rm G}^{\rm bulk}=1.216290731874,
 \qquad
 \mathcal W_{\rm G}^{\partial}=-1.8,
\]

portanto

\[
 \boxed{\mathcal W_{\rm G}=-0.583709268126}.
\]

Para o cilindro de Hopf, \(K=0\), e

\[
 \boxed{\mathcal W_{\rm cyl}
 =\frac12\log\pi-\frac32
 =-0.927635057075}.
\]

Assim,

\[
 \boxed{\mathcal W_{\rm cyl}-\mathcal W_{\rm G}
 =-0.343925788950<0}.
\]

O ramo cilíndrico é variacionalmente preferido entre esses dois backgrounds
na redução normalizada adotada. Esta comparação não equivale a uma prova de
estabilidade total: ainda é necessário calcular os blocos métricos radiais e
contar eventuais modos negativos de neckpinch. No setor axial de Hopf, a
positividade já segue de \(V_H=2/\tau\).

### 36.1 Limite atual da extração de \(Z_{\rm bulk}\)

O prefator da ação oficial fornece a escala da Hessiana depois de conhecido o
mapa

\[
 T_A=\partial_A(g(P),f(P),\bar f(P)).
\]

Esse mapa ainda não está definido globalmente. Identificar as três
componentes \(n_i\) do mapa de Hopf com o único escalar complexo global
\(f\) violaria a estrutura em dois patches e a classificação de Chern já
demonstrada. Logo não é lícito declarar simplesmente
\(Z_{\rm bulk}=\hbar\tau/\Lambda_C^2\).

O fechamento exige construir \(T_A\) como deformação da métrica/conexão nos
dois patches do fibrado e avaliar seu pullback na Hessiana. O número radial
universal \(3\sqrt\pi/4\) permanece válido independentemente dessa
normalização.

## 37. Estabilidade homogênea da garganta na GDQ

Sem introduzir campos externos à ação, considere a família cilíndrica
normalizada de raio \(a\). A normalização determina

\[
 F_0(a)=3\log\!\left(\frac{a}{2\sqrt\tau}\right)
 +\frac12\log\pi.
\]

O funcional GDQ reduzido é

\[
 \mathcal W_{\rm hom}(a)
 =\frac{6\tau}{a^2}
 +3\log\!\left(\frac{a}{2\sqrt\tau}\right)
 +\frac12\log\pi-3.
\]

Suas duas primeiras derivadas no ponto crítico são

\[
 \boxed{\mathcal W_{\rm hom}'(2\sqrt\tau)=0},
\]

\[
 \boxed{\mathcal W_{\rm hom}''(2\sqrt\tau)
 =\frac{3}{2\tau}>0}.
\]

Para \(\tau=1\), a diferença finita forneceu
\(1.500000035293\), contra \(1.5\) analítico. Portanto, o modo homogêneo de
expansão/contração da garganta é estritamente estável.

O resultado não usa a estabilidade de Higgs, Yang--Mills ou Dirac. Ele vem
apenas de \(R\), \(F\), \(\mathcal U\) e da normalização da ação GDQ.

Ainda devem ser analisados:

1. modos radiais não homogêneos \(u(r),\varphi(r)\);
2. modos tensoriais não isotrópicos em \(S^3\);
3. remoção explícita dos difeomorfismos radiais;
4. restrição linearizada da medida
   \(\int d\mu_*(3u/a-\varphi)=0\).

## 38. Atlas axial calculado e valor do pullback global

As duas seções locais do fibrado de Hopf podem ser escolhidas como

\[
 u_N(w)=\frac{(1,w)^T}{\sqrt{1+|w|^2}},
 \qquad
 u_S(w')=\frac{(w',1)^T}{\sqrt{1+|w'|^2}},
 \quad w'=1/w.
\]

No overlap,

\[
 u_S=e^{-i\arg w}u_N,
\]

enquanto \(P=uu^\dagger\) é global. A conexão muda por gauge e a curvatura
possui \(c_1=\pm1\). Além disso,

\[
 \boxed{
 \operatorname{Tr}(dP,dP)
 =\frac{2\,dw,d\bar w}{(1+|w|^2)^2}},
\]

fixando a normalização de Fubini--Study.

O teste numérico encontrou erro máximo \(2.89\times10^{-16}\) entre os
projetores nas duas cartas e erro \(1.28\times10^{-16}\) na lei de transição.

No cilindro redondo, uma orientação global atua por \(SU(2)\) isométrico:

\[
 P\mapsto UPU^\dagger,
 \qquad U^*g=g,
 \qquad U^*F=F.
\]

Logo seu vetor tangente no espaço dos campos fundamentais é

\[
 T_A=(\mathcal L_{X_A}g,\mathcal L_{X_A}F,
 \mathcal L_{X_A}\bar F)=0,
\]

ou pertence ao setor de difeomorfismos eliminado por
\(\Pi_{\rm phys}\). Portanto o pullback calculado é

\[
 \boxed{Z_{\rm bulk}^{\rm orientação\ global}=0.}
\]

Isso corrige a pendência anterior: não deve existir uma rigidez positiva
universal para uma rotação global de um background isotrópico. A rigidez
positiva relevante aparece somente para:

1. texturas não homogêneas, cujo harmônico de Hopf fornece
   \(V_H=2/\tau\);
2. resposta localizada ao aparelho,
   \(\mathbb H_R\delta\Phi_P=J_{\rm SG}\).

Consequentemente, não se deve usar
\(r_B=\mu B/Z_{\rm bulk}^{\rm global}\). O coeficiente experimental é obtido
do funcional de resposta da Seção 20, e satisfaz
\(\kappa_H^{\rm SG}\to0\) quando \(B\to0\). O atlas axial está construído; a
próxima quantidade física é a projeção localizada da fonte, não uma norma de
uma isometria global.
