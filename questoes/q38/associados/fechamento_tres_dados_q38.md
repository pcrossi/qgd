# Q38 — condições de contorno, localização e operadores de colagem

## 1. Princípio de fechamento

O objetivo é determinar os três dados que faltavam usando somente a ação
oficial da GDQ. O resultado abaixo distingue:

- o que decorre da variação;
- o que precisa ser acrescentado como dado de bordo;
- o que é incompatível com a geometria 8D adotada.

Não se usa o valor observado de \(G\) na construção.

---

## 2. Condições de contorno do background

### 2.1 Variação radial

Considere

\[
ds_8^2=e^{2A(r,\tau)}h_{\mu\nu}dx^\mu dx^\nu
+dr^2+R(r,\tau)^2d\Omega_3^2,
\qquad \sigma=\sigma(r,\tau).
\]

Após integração por partes, a variação do funcional de curvatura produz na
fronteira radial a forma simplética

\[
\Theta_{\partial I}
=\frac{\hbar}{\Lambda_C^2}
\int_\gamma d\tau\int_{\partial I\times S^3}
\mathcal U\sqrt q\,
\left(n^I\nabla^J\delta g_{IJ}
-n^I\nabla_I(g^{JK}\delta g_{JK})\right).
\]

A ação de Einstein--Hilbert sem termo análogo a Gibbons--Hawking--York não
admite simultaneamente variações métricas arbitrárias e condições de Robin.
As alternativas bem-postas são:

1. **Dirichlet:** \(\delta A=\delta R=0\) na fronteira;
2. acrescentar um funcional de bordo e então derivar condições de
   Neumann/Robin.

A ação oficial apresentada não contém esse funcional adicional. Portanto,
as condições de Robin do estômato não são determinadas por ela.

### 2.2 Condições regulares selecionadas pela ação sem novo termo

Para um fechamento suave de \(I_r\times S^3\) em \(r=0\), ausência de
singularidade cônica e paridade radial impõem

\[
\boxed{
R(0,\tau)=0,
\quad R'(0,\tau)=1,
\quad A'(0,\tau)=0,
\quad \sigma'(0,\tau)=0.
}
\]

As expansões locais são

\[
R=r+R_3(\tau)r^3+O(r^5),
\quad
A=A_0(\tau)+A_2(\tau)r^2+O(r^4),
\]

\[
\sigma=\sigma_0(\tau)+\sigma_2(\tau)r^2+O(r^4).
\]

Na extremidade externa, normalizabilidade e fluxo nulo da medida requerem

\[
\boxed{
\lim_{r\to r_+}\mathcal U e^{4A}R^3=0,
\qquad
\lim_{r\to r_+}n^r\partial_r
(\mathcal U e^{4A}R^3)=0.
}
\]

Essas condições selecionam o ramo regular, não um polo em \(\tau\).

### 2.3 Compatibilidade com fluxo de torção

Se

\[
H=\frac{2k}{R^3}\operatorname{vol}_{S^3},
\]

então \(|H|^2\propto k^2/R^6\). Um fechamento suave com \(R\to0\) só é
compatível com energia de torção finita se

\[
\boxed{k=0}
\]

nesse ponto, ou se a topologia excluir o ponto \(R=0\) e o substituir por uma
garganta de raio mínimo \(R_c>0\). Para um estômato com fluxo \(k\ne0\), as
condições naturais são, portanto,

\[
\boxed{
R(0,\tau)=R_c(\tau)>0,
\quad R'(0,\tau)=0,
\quad A'(0,\tau)=0,
\quad \sigma'(0,\tau)=0.
}
\]

Porém \(R_c(\tau)\) é dado de Dirichlet; sua evolução não é selecionada pela
ação bulk sem um termo de bordo do estômato.

### 2.4 Resultado do primeiro dado

A ação oficial seleciona univocamente condições regulares de Dirichlet após
escolher a geometria da fronteira. Ela **não seleciona um background singular
meromorfo**. Para selecionar tal ramo é indispensável especificar um
funcional de bordo ou uma condição causal singular independente. Logo, o
primeiro dado não pode ser derivado apenas do bulk oficial.

---

## 3. Identidade de localização do setor instantônico

### 3.1 Comparação dos invariantes

O integrando oficial contém

\[
\mathcal R_B=g^{IJ}\mathcal R^B_{IJ},
\]

que é linear na curvatura contraída. A densidade instantônica seria

\[
\mathcal Q_B=\frac1{8\pi^2}
\operatorname{Tr}(\mathcal F_B\wedge\mathcal F_B),
\]

quadrática na curvatura e uma 4-forma fechada.

Considere uma reescala local da curvatura
\(\mathcal F_B\mapsto t\mathcal F_B\). Então

\[
\mathcal R_B\mapsto t\mathcal R_B,
\qquad
\mathcal Q_B\mapsto t^2\mathcal Q_B.
\]

Portanto não existem constante universal \(C\) e derivada exata \(d\Xi\),
independentes do campo, tais que

\[
\mathcal R_B\mathcal U dV=C\mathcal Q_B+d\Xi
\]

para conexões arbitrárias. A homogeneidade em \(t\) já contradiz essa
identidade.

### 3.2 Consequência

Não é possível derivar da ação oficial, por mera integração por partes, o
funcional

\[
\frac1\alpha\int\mathcal Q_B.
\]

Autodualidade também não resolve o problema: ela relaciona
\(\int|\mathcal F_B|^2\) a \(\int\mathcal F_B\wedge\mathcal F_B\), mas a ação
oficial não contém \(|\mathcal F_B|^2\).

### 3.3 Única identidade topológica disponível sem alterar a ação

Em dimensão quatro, a combinação de Gauss--Bonnet

\[
\mathcal E_4=|\operatorname{Riem}|^2-4|\operatorname{Ric}|^2+\mathcal R^2
\]

tem integral topológica, mas ela também é quadrática e não coincide com
\(\mathcal R_B\). Usá-la exigiria um termo novo ou demonstrar que o
determinante quântico efetivo o gera. Isso ultrapassa a ação clássica oficial.

### 3.4 Resultado do segundo dado

\[
\boxed{
\text{não existe identidade de localização que transforme o termo escalar
oficial no termo instantônico para campos gerais.}
}
\]

Assim, \(e^{-1/(2\alpha)}\) não pode ser consequência da ação oficial na forma
atual. Ele pode surgir de um determinante/Hessiana quântica já derivado da
GDQ, mas esse operador adicional precisa ser apresentado explicitamente.

---

## 4. Operadores espectrais da colagem

### 4.1 Geometria coerente da fronteira

Uma hipersuperfície de uma variedade real 8D tem dimensão sete. Para
\(N_4\times I_r\times S^3\), a seção \(r={\rm const}\) é

\[
\Sigma_7=N_4\times S^3.
\]

Já \(S^3\times T^5\) possui dimensão oito e não pode ser a fronteira dessa
variedade 8D. Portanto, a colagem \(S^3\times T^5\) pertence a outro setor
(por exemplo, cosmológico interno) e não pode ser inserida nesta redução sem
redefinir a dimensionalidade.

### 4.2 Operadores no produto 8D adotado

Para flutuações escalares normalizadas na esfera, o operador de Hopf mínimo é

\[
\boxed{
K_H=-R_c^{-2}\Delta_{S^3}+V_H,
}
\]

com autofunções \(Y_{\ell mn}\) e espectro

\[
K_HY_{\ell mn}
=\left[\frac{\ell(\ell+2)}{R_c^2}+V_H\right]Y_{\ell mn},
\quad
\operatorname{deg}(\ell)=(\ell+1)^2.
\]

O operador radial/tangencial externo é

\[
\boxed{
K_N=-e^{-2A_c}\Box_{N_4}-\partial_r^2
-\left(4A'+3\frac{R'}R-\sigma'\right)\partial_r+V_N.
}
\]

O acoplamento misto é, por definição,

\[
\boxed{
J=\left.
\frac{\delta^2S_{\rm GDQ}}
{\delta\phi_H\,\delta\phi_N}
\right|_{g_*,\sigma_*}.
}
\]

Num background produto com \(A'=R'=\sigma'=0\) no colar e Hessiana
bloco-diagonal, a variação mista se anula:

\[
\boxed{J=0.}
\]

Então

\[
K_{\rm eff}=K_H,
\qquad
\chi_{\rm Fano}=0,
\]

e não \(3\sqrt2/5\). Um fator de Fano não nulo requer um background não
produto ou um termo de colagem que gere explicitamente \(J\ne0\).

### 4.3 Se o setor toroidal \(T^5\) for mantido separadamente

Num toro retangular com comprimentos \(L_i\), o operador mínimo é

\[
\boxed{
K_T=-\Delta_{T^5}+V_T,
}
\]

\[
K_Te_{\mathbf n}
=\lambda_{\mathbf n}e_{\mathbf n},
\qquad
\lambda_{\mathbf n}
=4\pi^2\sum_{i=1}^5\frac{n_i^2}{L_i^2}+V_T.
\]

Para uma kernel de colagem \(j(y,\theta)\),

\[
J_{\ell mn,\mathbf n}
=\int_{S^3\times T^5}
\overline{Y_{\ell mn}(y)}j(y,\theta)e_{\mathbf n}(\theta)
\,d\Omega_3d^5\theta.
\]

O complemento de Schur explícito é

\[
\boxed{
(K_{\rm eff})_{aa'}
=(K_H)_{aa'}-
\sum_{\mathbf n:\lambda_{\mathbf n}\ne0}
\frac{J_{a\mathbf n}\overline{J_{a'\mathbf n}}}
{\lambda_{\mathbf n}}.
}
\]

Essas fórmulas são espectralmente completas, mas o valor numérico depende de
\(L_i,V_T,V_H\) e da kernel \(j\), nenhum dos quais é fixado pela ação bulk
reduzida.

### 4.4 Resultado do terceiro dado

Os operadores livres e seus espectros podem ser escritos explicitamente. O
operador misto que produziria Fano é zero no produto e indeterminado fora
dele até que a ação/condição de colagem seja especificada. Consequentemente,
\(3\sqrt2/5\) não é derivável da ação oficial atualmente fornecida.

---

## 5. Veredito conjunto

Os três cálculos dão um resultado definido:

1. as condições naturais do bulk selecionam o ramo regular, não o singular;
2. o escalar de Bismut não localiza no número de Pontryagin;
3. a Hessiana do background produto tem \(J=0\), e a colagem
   \(S^3\times T^5\) é dimensionalmente incompatível com a redução 8D.

Portanto,

\[
\boxed{
\text{os três dados desejados não são consequências da ação oficial tal como
ela está escrita.}
}
\]

Para obtê-los sem pós-ajuste existem duas rotas logicamente legítimas:

- encontrar no manuscrito termos de bordo/Hessianas já pertencentes à GDQ e
  incluí-los explicitamente na redução;
- declarar condições causais e de colagem como axiomas constitutivos
  independentes, testando-os depois em outros observáveis.

Não é matematicamente legítimo declarar que os valores foram derivados do
bulk quando o cálculo acima mostra que o bulk seleciona o ramo oposto ou não
contém o invariante necessário.
