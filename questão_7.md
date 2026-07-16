# Questão 7 — Como surge o tempo lorentziano?

## 1. Pergunta

A Questão 7 pergunta:

\[
\boxed{
\text{como surge o tempo lorentziano?}
}
\]

A resposta aceitável exige verificar as hipóteses de Osterwalder--Schrader
e reconstruir explicitamente a teoria lorentziana.

Não basta escrever:

\[
t=-i\tau.
\]

Também não basta usar:

\[
J^2=-1.
\]

Essas expressões podem aparecer como heurísticas ou estruturas geométricas,
mas não provam:

1. existência de espaço de Hilbert físico;
2. positividade da norma;
3. unitariedade;
4. existência de Hamiltoniano;
5. autoadjunticidade;
6. espectro limitado inferiormente.

---

## 2. Separação entre dois problemas

Há duas perguntas diferentes que não devem ser misturadas.

### 2.1 Problema A — assinatura lorentziana

A Questão 2 já resolveu a assinatura lorentziana constitutiva.

Temos uma imersão:

\[
X:N\to M,
\]

com:

\[
q=X^*g.
\]

Escolhe-se uma forma-relógio:

\[
u=X^*\omega,
\]

e define-se:

\[
s=q^{-1}(u,u)>0.
\]

A métrica física é:

\[
\boxed{
h_{\mu\nu}
=
q_{\mu\nu}
-2\frac{u_\mu u_\nu}{s}.
}
\]

Num referencial \(q\)-ortonormal adaptado a \(u\):

\[
q=\operatorname{diag}(1,1,1,1),
\qquad
u=(u_0,0,0,0),
\]

logo:

\[
\boxed{
h=\operatorname{diag}(-1,1,1,1).
}
\]

Portanto:

\[
\boxed{
\operatorname{sign}(h)=(-,+,+,+).
}
\]

Isso explica como a assinatura lorentziana aparece no espaço-tempo físico
\(N^4\).

### 2.2 Problema B — reconstrução quântica lorentziana

A Questão 7 trata do segundo problema:

\[
\boxed{
\text{como uma teoria quântica lorentziana unitária é reconstruída a partir
dos dados euclidianos?}
}
\]

Esse problema exige uma camada Osterwalder--Schrader.

---

## 3. Papel correto de \(\tau\), \(t\) e \(z_\tau\)

Pela Questão 6:

\[
\boxed{
\tau\in\mathbb R_+,
\qquad
[\tau]=L^2.
}
\]

\(\tau\) é parâmetro de fluxo geométrico/difusivo, não tempo físico
cronológico.

O tempo físico é \(t\), e a variável causal complexa correta é:

\[
\boxed{
z_\tau=\tau+i\nu_0t,
\qquad
\nu_0=\frac{\hbar}{2m_0}.
}
\]

Assim:

\[
[\tau]=[\nu_0t]=L^2.
\]

Portanto:

\[
\boxed{
t\neq-i\tau.
}
\]

Na Questão 7, \(z_\tau\) entra como compatibilidade causal da GDQ, mas a
unitariedade lorentziana deve vir da reconstrução OS.

---

## 4. Papel correto de Sudarshan

A prescrição de Sudarshan permanece importante.

Ela codifica a seleção causal por meio de:

\[
\gamma\subset\mathbb C_{z_\tau}
\]

e do propagador simétrico:

\[
G_{\rm sym}
=
\frac12(G_{\rm ret}+G_{\rm adv}).
\]

Isso ajuda a:

1. controlar termos de fronteira;
2. selecionar polos físicos;
3. combinar setores avançado e retardado;
4. evitar a leitura ingênua de Wick;
5. manter compatibilidade causal com \(z_\tau\).

Mas:

\[
\boxed{
\text{Sudarshan não substitui os axiomas de Osterwalder--Schrader.}
}
\]

Em particular, a identidade:

\[
\oint_\gamma dF=0
\]

pode cancelar termos exatos de fronteira, mas não prova sozinha reflexão
positiva.

Logo, a estrutura final correta é:

\[
\boxed{
\text{OS reconstrói a teoria lorentziana;}
\qquad
\text{Sudarshan fixa a prescrição causal compatível.}
}
\]

---

## 5. Dados euclidianos da GDQ

Para aplicar OS, escolhe-se uma janela efetiva fixa de escala:

\[
\tau=\tau_0>0.
\]

Nessa janela, a GDQ fornece uma teoria euclidiana efetiva sobre a fatia
riemanniana associada a \(q\).

Os campos efetivos são agrupados como:

\[
\Phi
=
(\Psi,B,A^a,\psi,\ldots),
\]

onde:

- \(\Psi\) é campo escalar efetivo de Madelung;
- \(B\) é a 3-forma torsional efetiva;
- \(A^a\) são campos de calibre \(U(1)^4\);
- \(\psi\) são campos fermiônicos/spinoriais;
- outros campos podem ser incluídos desde que suas regras de reflexão sejam
  especificadas.

O funcional euclidiano efetivo é escrito como:

\[
S_E[\Phi;q,f,B;\tau_0].
\]

A medida formal é:

\[
d\mu_E(\Phi)
=
\frac1{Z_E}
e^{-S_E[\Phi;q,f,B;\tau_0]}
\mathcal D\Phi.
\]

com:

\[
Z_E
=
\int
e^{-S_E[\Phi;q,f,B;\tau_0]}
\mathcal D\Phi.
\]

Essa camada euclidiana não substitui a ação oficial da GDQ. Ela é a camada
efetiva necessária para reconstruir a teoria lorentziana física.

---

## 6. Funções de Schwinger

As funções de Schwinger são definidas por:

\[
\boxed{
S_n^{a_1\cdots a_n}(x_1,\ldots,x_n)
=
\left\langle
\Phi_{a_1}(x_1)\cdots\Phi_{a_n}(x_n)
\right\rangle_E.
}
\]

Explicitamente:

\[
\boxed{
S_n^{a_1\cdots a_n}(x_1,\ldots,x_n)
=
\frac1{Z_E}
\int
\Phi_{a_1}(x_1)\cdots\Phi_{a_n}(x_n)
e^{-S_E[\Phi;q,f,B;\tau_0]}
\mathcal D\Phi.
}
\]

O funcional gerador é:

\[
\boxed{
Z_E[J]
=
\frac1{Z_E[0]}
\int
\exp\left(
-S_E[\Phi]
+\sum_a\int J_a(x)\Phi_a(x)\,dV_q
\right)
\mathcal D\Phi.
}
\]

E:

\[
\boxed{
S_n^{a_1\cdots a_n}(x_1,\ldots,x_n)
=
\left.
\frac{\delta^n Z_E[J]}
{\delta J_{a_1}(x_1)\cdots\delta J_{a_n}(x_n)}
\right|_{J=0}.
}
\]

Essas são as funções que devem ser verificadas pelos axiomas OS.

---

## 7. Reflexão temporal

Escolhe-se uma coordenada euclidiana \(x_E^0\) compatível com a forma-relógio
\(u\).

A reflexão temporal é:

\[
\boxed{
\Theta x_E=(-x_E^0,\mathbf x).
}
\]

Para campos escalares:

\[
\boxed{
(\Theta\Phi)(x)
=
\Phi(\Theta x)^*.
}
\]

Para campos vetoriais euclidianos:

\[
(\Theta A)_0(x)
=
-A_0(\Theta x),
\qquad
(\Theta A)_i(x)
=
A_i(\Theta x).
\]

Para férmions, a reflexão deve incluir a matriz apropriada de conjugação:

\[
\boxed{
(\Theta\psi)(x)
=
C_\Theta\,\bar\psi(\Theta x)^T,
}
\]

onde \(C_\Theta\) é escolhida para preservar a forma euclidiana do termo de
Dirac.

Para a 3-forma \(B\), a regra é a regra tensorial induzida por
\(\Theta\), com sinal \((-1)\) para cada índice temporal refletido.

---

## 8. Axioma OS1 — regularidade

As distribuições:

\[
S_n(x_1,\ldots,x_n)
\]

devem ser distribuições temperadas ou, em background curvo, distribuições
microlocais admissíveis.

Na janela efetiva da GDQ, isso significa:

\[
\boxed{
S_n
\text{ deve estar bem definido para separações não coincidentes e possuir
singularidades locais controladas pelo corte geométrico }\Lambda_C.
}
\]

Esse ponto é compatível com a regularidade estrutural proposta pela GDQ, mas
deve ser verificado no setor efetivo escolhido.

---

## 9. Axioma OS2 — invariância euclidiana

No background plano efetivo, exigir:

\[
\boxed{
S_n(Rx_1+a,\ldots,Rx_n+a)
=
S_n(x_1,\ldots,x_n)
}
\]

para:

\[
(a,R)\in E(4)=\mathbb R^4\rtimes SO(4).
\]

Em background curvo, a forma global \(E(4)\) é substituída por:

1. covariância por difeomorfismos euclidianos admissíveis;
2. invariância local em cartas normais;
3. recuperação de \(E(4)\) no background plano.

Portanto, a afirmação final é:

\[
\boxed{
\text{OS global vale no setor plano/estacionário;}
\quad
\text{em background curvo usa-se a versão local/covariante.}
}
\]

---

## 10. Axioma OS3 — simetria por permutação

Para campos bosônicos:

\[
\boxed{
S_n(\ldots,x_i,x_{i+1},\ldots)
=
S_n(\ldots,x_{i+1},x_i,\ldots).
}
\]

Para férmions:

\[
\boxed{
S_n(\ldots,x_i,x_{i+1},\ldots)
=
-S_n(\ldots,x_{i+1},x_i,\ldots)
}
\]

quando dois campos fermiônicos adjacentes são permutados.

Em geral, a regra é graduada:

\[
\boxed{
S_n(\ldots,\Phi_i,\Phi_j,\ldots)
=
(-1)^{|\Phi_i||\Phi_j|}
S_n(\ldots,\Phi_j,\Phi_i,\ldots).
}
\]

---

## 11. Axioma OS4 — reflexão positiva

Este é o ponto central.

Seja \(\mathcal D_+\) o conjunto dos funcionais polinomiais dos campos com
suporte em tempos euclidianos positivos:

\[
\mathcal D_+
=
\{F[\Phi]:\operatorname{supp}F\subset x_E^0>0\}.
\]

A reflexão positiva exige:

\[
\boxed{
\langle \Theta F\,F\rangle_E\ge0
\qquad
\forall F\in\mathcal D_+.
}
\]

Em termos de funções de Schwinger, para:

\[
F=\sum_i c_i
\Phi_{a_{i1}}(x_{i1})\cdots\Phi_{a_{im_i}}(x_{im_i}),
\qquad
x_{ik}^0>0,
\]

deve valer:

\[
\boxed{
\sum_{i,j}
\bar c_i c_j\,
S_{m_i+m_j}
(\Theta x_{i m_i},\ldots,\Theta x_{i1},
x_{j1},\ldots,x_{jm_j})
\ge0.
}
\]

Essa condição não segue apenas de \(J^2=-1\), nem de \(t=-i\tau\), nem de
\(\oint_\gamma dF=0\).

Na GDQ, a condição deve ser imposta/verificada na medida efetiva:

\[
d\mu_E(\Phi)
=
\frac1{Z_E}
e^{-S_E[\Phi]}
\mathcal D\Phi.
\]

Critério suficiente de trabalho:

\[
\boxed{
S_E
\text{ deve ser real, limitado inferiormente e invariante sob }\Theta,
\text{ e a medida deve fatorar positivamente em torno da fatia }x_E^0=0.
}
\]

Isso é o que permite a reconstrução de norma positiva.

---

## 12. Axioma OS5 — propriedade de cluster

Para dois conjuntos de pontos \(X=(x_1,\ldots,x_m)\) e
\(Y=(y_1,\ldots,y_n)\), exige-se:

\[
\boxed{
\lim_{|a|\to\infty}
S_{m+n}(X,Y+a)
=
S_m(X)S_n(Y).
}
\]

Fisicamente, isso significa que correlações entre regiões muito separadas
fatoram.

Na GDQ, isso deve ser lido como:

\[
\boxed{
\text{solítons ou excitações separadas por distância muito maior que }
\ell_C
\text{ devem desacoplar no setor efetivo.}
}
\]

A propriedade de cluster garante unicidade do vácuo reconstruído no setor
considerado.

---

## 13. Construção do espaço de Hilbert

Assumindo OS1--OS5, constrói-se o espaço pré-Hilbert a partir de
\(\mathcal D_+\).

Define-se o produto interno:

\[
\boxed{
(F,G)
=
\langle \Theta F\,G\rangle_E.
}
\]

Pela reflexão positiva:

\[
(F,F)\ge0.
\]

Define-se o subespaço nulo:

\[
\boxed{
\mathcal N
=
\{F\in\mathcal D_+:(F,F)=0\}.
}
\]

O espaço de Hilbert físico é:

\[
\boxed{
\mathcal H
=
\overline{\mathcal D_+/\mathcal N}.
}
\]

Esse é o espaço de estados lorentziano reconstruído.

---

## 14. Reconstrução do vácuo

O funcional constante:

\[
1\in\mathcal D_+
\]

define o vetor de vácuo:

\[
\boxed{
\Omega=[1]\in\mathcal H.
}
\]

A normalização:

\[
Z_E[0]=1
\]

implica:

\[
\boxed{
\|\Omega\|^2=1.
}
\]

Pela propriedade de cluster, esse vácuo é único no setor reconstruído.

---

## 15. Reconstrução do semigrupo temporal

Translações euclidianas positivas no tempo preservam \(\mathcal D_+\):

\[
(T_E(a)F)[\Phi]
=
F[\Phi(\cdot+a e_0)],
\qquad
a\ge0.
\]

Elas definem um semigrupo de contrações em \(\mathcal H\):

\[
\boxed{
T_E(a+b)=T_E(a)T_E(b),
\qquad
\|T_E(a)\|\le1.
}
\]

Pelo teorema de Hille--Yosida, existe um operador autoadjunto positivo \(H\)
tal que:

\[
\boxed{
T_E(a)=e^{-aH/\hbar}.
}
\]

Assim:

\[
\boxed{
H
=
-\hbar
\left.
\frac{d}{da}T_E(a)
\right|_{a=0^+}.
}
\]

Esse é o Hamiltoniano lorentziano reconstruído.

---

## 16. Autoadjunticidade e positividade do Hamiltoniano

Como \(T_E(a)\) é um semigrupo simétrico positivo de contrações:

\[
\boxed{
H=H^\dagger.
}
\]

E como:

\[
T_E(a)=e^{-aH/\hbar}
\]

é contração para \(a\ge0\), segue:

\[
\boxed{
H\ge0.
}
\]

Portanto, o espectro é limitado inferiormente:

\[
\boxed{
\operatorname{spec}(H)\subset[0,\infty).
}
\]

Esse é o resultado que substitui a afirmação heurística de que o tempo surge
por uma rotação de Wick.

---

## 17. Evolução lorentziana

Depois de reconstruído \(H\), a evolução física em tempo lorentziano é:

\[
\boxed{
U(t)=e^{-itH/\hbar}.
}
\]

Como \(H=H^\dagger\), pelo teorema de Stone:

\[
\boxed{
U(t)^\dagger U(t)=1.
}
\]

Logo, a evolução lorentziana é unitária.

O tempo físico \(t\) é o parâmetro do grupo unitário \(U(t)\), não o mesmo
objeto que \(\tau\).

---

## 18. Relação com a métrica lorentziana \(h\)

A reconstrução OS fornece o espaço de Hilbert e o Hamiltoniano.

A Questão 2 fornece a métrica lorentziana física:

\[
h_{\mu\nu}
=
q_{\mu\nu}
-2\frac{u_\mu u_\nu}{q^{-1}(u,u)}.
\]

Portanto, a teoria lorentziana reconstruída propaga campos sobre:

\[
\boxed{
(N,h).
}
\]

No setor plano:

\[
\boxed{
h=-dt^2+d\mathbf x^2.
}
\]

O Hamiltoniano \(H\) é o gerador das translações no tempo físico \(t\)
associado à forma-relógio \(u\).

---

## 19. Relação com \(z_\tau\) e \(\gamma\)

A variável causal da GDQ permanece:

\[
z_\tau=\tau+i\nu_0t.
\]

Depois da reconstrução OS, a continuação para o tempo físico é interpretada
assim:

1. \(\tau\) fixa a janela difusiva/de escala;
2. \(t\) é o parâmetro do grupo unitário \(U(t)\);
3. \(z_\tau\) organiza a compatibilidade complexa entre escala e evolução;
4. \(\gamma\) seleciona a prescrição causal Sudarshan;
5. a positividade da norma vem de OS, não de \(\gamma\) sozinho.

Em forma curta:

\[
\boxed{
\text{OS dá }(\mathcal H,H,U(t));
\qquad
\text{Sudarshan dá a prescrição causal em }z_\tau.
}
\]

---

## 20. Resposta às perguntas obrigatórias

### 20.1 Quais funções de Schwinger são construídas?

São:

\[
\boxed{
S_n^{a_1\cdots a_n}(x_1,\ldots,x_n)
=
\frac1{Z_E}
\int
\Phi_{a_1}(x_1)\cdots\Phi_{a_n}(x_n)
e^{-S_E[\Phi]}
\mathcal D\Phi.
}
\]

com \(\Phi=(\Psi,B,A^a,\psi,\ldots)\) na janela efetiva \(\tau=\tau_0\).

### 20.2 Elas satisfazem reflexão positiva?

Devem satisfazer:

\[
\boxed{
\langle\Theta F\,F\rangle_E\ge0
\qquad
\forall F\in\mathcal D_+.
}
\]

Esta é uma hipótese/verificação obrigatória da camada efetiva GDQ.

### 20.3 Há invariância euclidiana?

No setor plano/estacionário:

\[
\boxed{
S_n(Rx_1+a,\ldots,Rx_n+a)=S_n(x_1,\ldots,x_n).
}
\]

Em background curvo, substitui-se por covariância local e recuperação de
\(E(4)\) em cartas normais/background plano.

### 20.4 Há simetria por permutação?

Sim, no sentido graduado:

\[
\boxed{
S_n(\ldots,\Phi_i,\Phi_j,\ldots)
=
(-1)^{|\Phi_i||\Phi_j|}
S_n(\ldots,\Phi_j,\Phi_i,\ldots).
}
\]

### 20.5 Há propriedade de cluster?

Exige-se:

\[
\boxed{
\lim_{|a|\to\infty}
S_{m+n}(X,Y+a)
=
S_m(X)S_n(Y).
}
\]

Na GDQ, isso expressa desacoplamento de excitações separadas por distâncias
muito maiores que \(\ell_C\).

### 20.6 Qual Hamiltoniano lorentziano é reconstruído?

O Hamiltoniano é o gerador do semigrupo euclidiano:

\[
\boxed{
T_E(a)=e^{-aH/\hbar}.
}
\]

Logo:

\[
\boxed{
H
=
-\hbar
\left.
\frac{d}{da}T_E(a)
\right|_{a=0^+}.
}
\]

Ele gera a evolução lorentziana:

\[
\boxed{
U(t)=e^{-itH/\hbar}.
}
\]

### 20.7 Ele é autoadjunto e limitado inferiormente?

Sim, desde que a reflexão positiva OS seja satisfeita:

\[
\boxed{
H=H^\dagger,
\qquad
H\ge0.
}
\]

Portanto:

\[
\boxed{
\operatorname{spec}(H)\subset[0,\infty).
}
\]

---

## 21. Consequência lógica

A emergência do tempo lorentziano na GDQ deve ser formulada em três camadas:

### Camada 1 — assinatura

\[
\boxed{
h_{\mu\nu}
=
q_{\mu\nu}
-2\frac{u_\mu u_\nu}{q^{-1}(u,u)}
}
\]

gera:

\[
\boxed{
\operatorname{sign}(h)=(-,+,+,+).
}
\]

### Camada 2 — reconstrução OS

As funções de Schwinger satisfazendo OS geram:

\[
\boxed{
\mathcal H,\quad
\Omega,\quad
H\ge0.
}
\]

### Camada 3 — evolução causal

O tempo físico é o parâmetro do grupo unitário:

\[
\boxed{
U(t)=e^{-itH/\hbar}.
}
\]

e a causalidade GDQ é organizada por:

\[
\boxed{
z_\tau=\tau+i\nu_0t,
\qquad
\gamma\subset\mathbb C_{z_\tau}.
}
\]

---

## 22. Status da Questão 7

A Questão 7 fica resolvida no seguinte sentido rigoroso:

\[
\boxed{
\text{o tempo lorentziano surge pela reconstrução Osterwalder--Schrader da
camada euclidiana efetiva da GDQ, propagando-se sobre a métrica constitutiva }
h.
}
\]

O que é necessário assumir/verificar em cada setor efetivo:

\[
\boxed{
\text{as funções de Schwinger da medida euclidiana GDQ satisfazem OS1--OS5.}
}
\]

Sob essa condição:

\[
\boxed{
\mathcal H
=
\overline{\mathcal D_+/\mathcal N},
\qquad
T_E(a)=e^{-aH/\hbar},
\qquad
U(t)=e^{-itH/\hbar},
\qquad
H=H^\dagger\ge0.
}
\]

Portanto:

\[
\boxed{
\text{Questão 7 fechada como critério OS de emergência do tempo
lorentziano.}
}

