# Derivação da fonte clássica e do operador de interface de Stern--Gerlach

## 1. Objetivo e resultado

Este documento executa o primeiro bloco da
`topicos/medida_interface/teoria_interface_classico_quantica_gdq.md`:

\[
J_A^{\rm clássico}
\longrightarrow
\mathsf R_{\rm app}
\]

sem inserir matrizes de Pauli ou projetores de medição como interação
fundamental.

O resultado principal é a separação entre três objetos que não devem ser
confundidos:

\[
\boxed{
\begin{aligned}
J_A&=-\frac{\delta S_{\rm int}}{\delta\Phi},
&&\text{fonte linear gerada pelo aparelho},\\
\mathsf R_A&=\frac{\delta^2S_{\rm int}}
{\delta\varphi^2},
&&\text{Hessiana de interface},\\
\Lambda_Q&=\text{DtN do objeto},
&&\text{resposta interna do sóliton}.
\end{aligned}}
\]

A equação linearizada correta em torno de um background conjunto é

\[
\boxed{(\Lambda_Q+\mathsf R_A)\,\delta\varphi=\delta J_A.}
\]

Uma Robin homogênea aparece apenas quando a fonte é absorvida no background
estacionário ou quando se estudam flutuações sem nova variação externa.

---

## 2. Dados clássicos do aparelho

O eletroímã é caracterizado no espaço-tempo físico por uma corrente
macroscópica prescrita:

\[
j_A^\mu(x),
\qquad
\nabla_\mu j_A^\mu=0.
\]

Ela determina um potencial e uma curvatura clássicos:

\[
F_A=dA_A,
\qquad
dF_A=0,
\qquad
d{*F_A}=*j_A,
\]

no limite clássico efetivo já reconstruído pela GDQ.

Para a derivação da resposta do objeto, \(F_A\) é dado externo do problema.
A GDQ não deve prever a corrente escolhida pelo experimentalista. Deve prever
a resposta do sóliton a essa corrente.

Na região de Stern--Gerlach:

\[
\boldsymbol B_A=\nabla\times\boldsymbol A_A,
\qquad
\nabla|\boldsymbol B_A|\ne0.
\]

---

## 3. Corrente geométrica do objeto

O Capítulo 19 fornece a identidade hidrodinâmica

\[
j_Q^\mu=\nabla_\alpha\mathcal T_Q^{\alpha\mu},
\]

onde \(\mathcal T_Q^{\alpha\mu}\) é a densidade antissimétrica de
spin--torção obtida pela projeção da 3-forma de Bismut/Cartan:

\[
\mathcal T_Q^{\mu\nu}
=u_\lambda H_Q^{\mu\nu\lambda}.
\]

Consequentemente, o acoplamento clássico da corrente com o potencial,

\[
S_{\rm int}^{(1)}
=\frac{q}{c}\int A_{A\mu}j_Q^\mu\,d\mu,
\]

pode ser integrado por partes. Usando a antissimetria de \(\mathcal T_Q\):

\[
S_{\rm int}^{(1)}
=\frac{q}{2c}\int
\mathcal T_Q^{\mu\nu}F^{\rm app}_{\mu\nu}\,d\mu
+S_{\partial}^{A\mathcal T}.
\]

O sinal global depende da convenção adotada para \(F=dA\), orientação e
normal exterior. Ele deve ser fixado uma única vez no dicionário da teoria.
A estrutura bilinear e gauge-invariante não depende dessa escolha.

No bulk completo, deve-se escrever covariantemente:

\[
\boxed{
S_{\rm int}[\Phi;F_A]
=\frac{q}{2c}
\int_{\Omega_{\rm SG}}
\chi_{\rm SG}\,
\mathcal T^{AB}[\Phi]F^{\rm app}_{AB}\,d\mu_\Phi.
}
\]

Os índices \(A,B\) referem-se ao espaço em que a forma clássica foi elevada
ao bulk. O mapa de levantamento da folha física para o bulk deve ser
explicitado no cálculo final. A fórmula acima não autoriza prolongamentos
arbitrários nas direções internas.

---

## 4. Por que este acoplamento não insere Pauli

O funcional fundamental de sonda depende apenas de:

1. curvatura clássica \(F_A\);
2. tensor geométrico \(\mathcal T[\Phi]\);
3. medida e métrica da GDQ;
4. carga topológica \(q\), caso já derivada no setor do objeto.

Não aparecem no acoplamento fundamental:

- \(\boldsymbol\sigma\);
- \(P_{\boldsymbol n}^{\pm}\);
- autovalores \(\pm\hbar/2\);
- postulado de projeção.

Essas estruturas só podem aparecer depois de restringir
\(\mathcal T[\Phi]\) ao módulo intrínseco de Hopf já construído.

---

## 5. Variação em relação aos campos GDQ

Seja \(D_\Phi\mathcal T\) a diferencial do tensor de torção e
\(D_\Phi d\mu\) a variação da medida. Para uma perturbação \(\delta\Phi\):

\[
\begin{aligned}
\delta S_{\rm int}
=\frac{q}{2c}\int_{\Omega_{\rm SG}}\chi_{\rm SG}
\bigg[&
\left(D_\Phi\mathcal T\cdot\delta\Phi\right)^{AB}F^{\rm app}_{AB}
\\
&+\mathcal T^{AB}F^{\rm app}_{AB}\,
\delta\log d\mu_\Phi
\bigg]d\mu_\Phi.
\end{aligned}
\]

Portanto, no produto interno definido pela medida oficial, a fonte é

\[
\boxed{
J_A
=-\frac{q}{2c}
\left(D_\Phi\mathcal T\right)^*
(\chi_{\rm SG}F_A)
+J_{\rm medida},
}
\]

com

\[
\langle J_{\rm medida},\delta\Phi\rangle
=-\frac{q}{2c}\int\chi_{\rm SG}
\mathcal T^{AB}F^{\rm app}_{AB}\,
\delta\log d\mu_\Phi\,d\mu_\Phi.
\]

Esta é a versão não circular da fonte anteriormente escrita na Q42 como
\((D_\Phi P)^*(\boldsymbol\sigma\cdot\boldsymbol B)\).

O problema linear do bulk é:

\[
\boxed{
\mathbb H_{\rm GDQ}^{\rm phys}\delta\Phi=J_A,
}
\]

depois da remoção de difeomorfismos, isometrias globais e demais modos zero.

---

## 6. Redução ao módulo de Hopf

### 6.1 Equivariância

No setor de spin semi-inteiro, o módulo de orientações é

\[
\mathcal O\simeq SU(2)/U(1)\simeq S^2\simeq\mathbb{CP}^1.
\]

Se o background livre é isotrópico, o mapa entre orientação e densidade
torsional deve ser equivarante sob rotações:

\[
\mathcal T[UPU^\dagger]
=R(U)\cdot\mathcal T[P].
\]

No setor espacial axial, toda 2-forma antissimétrica é dual a um vetor:

\[
t_i(P)=\frac12\epsilon_{ijk}\mathcal T^{jk}(P).
\]

Um mapa equivarante de \(S^2\) para a representação vetorial, na ordem líder,
tem necessariamente a forma

\[
\boxed{t_i(P)=t_H\,n_i(P),}
\]

onde \(t_H\) é a norma torsional radial e \(\boldsymbol n(P)\) é o vetor de
Hopf. Essa conclusão vem de simetria e do lema de Schur no setor vetorial;
não depende de escolher previamente um eixo de medida.

### 6.2 Forma Zeeman emergente

Como

\[
\frac12\mathcal T^{ij}F^{\rm app}_{ij}
=\boldsymbol t(P)\cdot\boldsymbol B_A,
\]

a integração radial produz

\[
S_{\rm int}^{\rm red}
=\int dt\,
\mu_{\rm GDQ}\,
\boldsymbol n(P)\cdot\boldsymbol B_A,
\]

com

\[
\boxed{
\mu_{\rm GDQ}
=\frac{q}{c}
\int_{\perp}\chi_{\rm SG}\,
t_H(r)\,d\mu_{\perp}.
}
\]

O sinal físico de energia é fixado pela convenção entre ação e Hamiltoniano:

\[
V_Z(P)=-\mu_{\rm GDQ}
\boldsymbol n(P)\cdot\boldsymbol B_A.
\]

As matrizes de Pauli podem então ser usadas apenas como coordenadas do
projetor:

\[
P=\frac12(I+\boldsymbol n\cdot\boldsymbol\sigma),
\]

e não como dados fundamentais do aparelho.

### 6.3 O coeficiente ainda não avaliado

A estrutura de \(\mu_{\rm GDQ}\) foi obtida, mas seu valor exige:

1. perfil estacionário \(H_Q\) ou \(\mathcal T_Q\);
2. normalização da medida oficial;
3. mapa de projeção da 3-forma para a folha física;
4. carga \(q\) fixada pelo setor topológico;
5. domínio radial e condição do estômato.

Não se deve substituir antecipadamente \(\mu_{\rm GDQ}\) por \(\mu_B\) e
depois declarar o magneton derivado.

---

## 7. Termo de bordo e operador de interface

### 7.1 Fonte de bordo

Quando a integração por partes encontra a fronteira do estômato, surge

\[
S_{\partial}^{A\mathcal T}
=\frac{q}{c}
\int_\Sigma A_{A\mu}\,
n_\alpha\mathcal T^{\alpha\mu}\,d\Sigma.
\]

Sua primeira variação fornece um fluxo imposto pelo aparelho:

\[
\Pi_A^{(1)}=-J_{A,\partial}.
\]

Assim, antes de expandir em torno do novo equilíbrio, a condição é
inomogênea:

\[
\boxed{
\Pi_Q(\varphi)=J_{A,\partial}.
}
\]

Essa é a forma correta quando o campo externo é ligado sobre um background
livre.

### 7.2 Linearização em torno do background acoplado

Se \(\varphi_*[F_A]\) resolve a equação com o aparelho presente, escreva

\[
\varphi=\varphi_*+\delta\varphi,
\qquad
F_A=F_{A*}+\delta F_A.
\]

Linearizando:

\[
\boxed{
(\Lambda_Q+\mathsf R_A)\delta\varphi
=\delta J_{A,\partial},
}

onde

\[
\boxed{
\mathsf R_A
=\left.
\frac{\delta^2S_{\rm int}}
{\delta\varphi^2}
\right|_{\varphi_*,F_{A*}}.
}

Para flutuações com o aparelho mantido fixo,
\(\delta J_{A,\partial}=0\), obtém-se a condição homogênea:

\[
(\Lambda_Q+\mathsf R_A)\delta\varphi=0.
\]

Portanto, \(\mathsf R_A\) é Hessiana de resposta, não a própria fonte linear.

---

## 8. Hessiana no módulo de orientações

Para

\[
V_Z(P)=-\mu_{\rm GDQ}B\,\boldsymbol n(P)\cdot\hat{\boldsymbol z},
\]

os polos \(\boldsymbol n=\pm\hat{\boldsymbol z}\) são pontos críticos. Em
coordenadas tangentes \(\eta\):

\[
\operatorname{Hess}V_Z|_+
=+\mu_{\rm GDQ}B\,I_2,
\]

\[
\operatorname{Hess}V_Z|_-
=-\mu_{\rm GDQ}B\,I_2.
\]

Isso estabelece:

1. o campo levanta a degenerescência;
2. o ramo paralelo é mínimo da energia Zeeman;
3. o ramo antiparalelo é máximo no módulo puramente orientacional.

Consequência importante:

\[
\boxed{
\text{um potencial Zeeman dissipativo isolado não possui dois mínimos.}
}
\]

Os dois feixes de Stern--Gerlach correspondem a dois canais unitários/adiabáticos
do Hamiltoniano efetivo, mas não podem ser identificados automaticamente com
duas bacias dissipativas equivalentes do mesmo potencial estático.

Para uma teoria de resultado individual com dois registros estáveis, é
necessário incluir os graus do aparelho. O funcional conjunto deve possuir
duas bacias macroscópicas correlacionadas, mesmo que as energias internas dos
dois canais sejam diferentes.

---

## 9. Complemento de Schur e origem da impedância

No background acoplado, considere a Hessiana física:

\[
\mathbb K=
\begin{pmatrix}
K_Q & J_{QA}\\
J_{AQ} & K_A
\end{pmatrix}.
\]

Eliminando os modos internos do aparelho:

\[
\boxed{
K_Q^{\rm eff}
=K_Q-J_{QA}K_A^{-1}J_{AQ}.
}

A restrição desse operador ao traço de fronteira produz a impedância dinâmica
efetiva. Em frequência real, deve-se usar \(K_A^{-1}\to G_A^{\rm ret}\):

\[
\mathsf R_A(\omega)
=\mathsf R_A^{(0)}
-J_{\partial A}G_A^{\rm ret}(\omega)J_{A\partial}.
\]

Assim:

\[
\operatorname{Re}\mathsf R_A
\to\text{rigidez e deslocamento},
\]

\[
\operatorname{Im}\mathsf R_A
\to\text{dissipação e largura}.
\]

Essa é a origem correta, em princípio, de
\(\kappa_H^{\rm SG}\) e \(\Gamma_{\rm SG}\).

---

## 10. Força de Stern--Gerlach

Depois de obtida a energia reduzida:

\[
E_\pm(\boldsymbol x)
=\mp\mu_{\rm GDQ}|\boldsymbol B_A(\boldsymbol x)|,
\]

a força sobre o centro do sóliton é

\[
\boxed{
\boldsymbol F_\pm
=-\boldsymbol\nabla E_\pm
=\pm\mu_{\rm GDQ}\boldsymbol\nabla|\boldsymbol B_A|.
}
\]

Essa passagem recupera o resultado mecânico do Capítulo 10, mas agora deixa
claro que:

- a forma da força segue da redução torsional;
- os dois canais vêm do setor intrínseco;
- o valor do momento magnético ainda deve ser avaliado da geometria;
- a seleção individual requer a dinâmica completa do aparelho.

---

## 11. O que foi derivado e o que permanece aberto

### 11.1 Derivado estruturalmente

1. fonte clássica expressa por \(F_A\), sem projetores;
2. acoplamento gauge-invariante \(\mathcal T:F_A\);
3. fonte linear \(J_A\) por variação;
4. forma Zeeman por redução equivarante ao módulo de Hopf;
5. fórmula geométrica para \(\mu_{\rm GDQ}\);
6. distinção entre fonte, Hessiana de interface e DtN;
7. condição linearizada
   \((\Lambda_Q+\mathsf R_A)\delta\varphi=\delta J_A\);
8. complemento de Schur como origem da impedância dinâmica;
9. força oposta nos dois canais.

### 11.2 Ainda aberto

1. levantamento único de \(F_A\) da folha física ao bulk;
2. perfil estacionário da torção do objeto;
3. avaliação de \(\mu_{\rm GDQ}\) sem usar \(\mu_B\) como entrada;
4. Hessiana completa do aparelho;
5. kernel retardado e mobilidade;
6. duas bacias macroscópicas de registro;
7. derivação de \(\Gamma_{\rm SG}\);
8. processo condicionado e captura individual.

---

## 12. Próximo passo

O próximo bloco deve modelar o aparelho mínimo sem importar uma teoria
quântica de medição:

\[
\boxed{
\text{modo coletivo de magnetização }X
+\text{banho geométrico }\{y_\nu\}
+\text{objeto Hopf }P.
}
\]

Deve-se derivar da expansão da ação:

\[
S^{(2)}[P,X,y_\nu],
\]

calcular o kernel retardado do aparelho e determinar as condições sob as quais
o funcional conjunto possui dois registros metastáveis correlacionados aos
dois canais do objeto.

## 13. Status

\[
\boxed{
\text{Primeiro bloco da teoria de interface fechado estruturalmente;}
\quad
\mu_{\rm GDQ}\text{ e a dinâmica do aparelho permanecem por avaliar.}
}
\]
