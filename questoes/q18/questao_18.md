# Questão 18 — Existem solítons que possam representar partículas?

## 1. Pergunta

A Questão 18 pergunta:

\[
\boxed{
\text{existem soluções solitônicas das equações da GDQ que possam representar
partículas?}
}
\]

As perguntas obrigatórias de `18-0.md` são:

1. qual é a solução explícita ou numérica?
2. qual é sua energia?
3. a energia é finita?
4. qual é sua carga?
5. qual é seu spin?
6. qual é sua massa?
7. é estável linear e não linearmente?
8. possui modos zero?
9. qual é seu comportamento assintótico?
10. como interage com outro solíton?

O critério de resolução é:

\[
\boxed{
\text{exibir uma solução das equações da GDQ, não um perfil escolhido
externamente.}
}
\]

---

## 2. Resposta curta

Sim, há uma noção matematicamente bem definida de solíton na GDQ: os solítons
são pontos fixos do fluxo geométrico torsional de Ricci--Perelman/Bismut.

A equação estacionária é:

\[
\boxed{
R_{ij}
-\frac14 B_{ik\ell}B_j{}^{k\ell}
+\nabla_i\nabla_j\phi
=
\lambda g_{ij},
}
\]

com:

\[
\boxed{
d^\dagger_\phi B=0,
\qquad
dB=0,
}
\]

onde:

\[
\boxed{
\phi=\operatorname{Re}f,
\qquad
\rho=e^{-\phi}=e^{-(f+\bar f)/2}.
}
\]

A fase:

\[
\boxed{
\chi=\operatorname{Im}f=\frac{S_R}{\hbar}
}
\]

carrega os dados de circulação, carga e spin.

Contudo, a auditoria exige uma distinção importante:

\[
\boxed{
\text{a existência formal de solítons geométricos está fechada;}
}
\]

mas:

\[
\boxed{
\text{a identificação completa de cada partícula física exige resolver o
problema espectral/topológico de cada setor.}
}
\]

Portanto, a Questão 18 fica fechada como estrutura matemática e critério de
validação, mas não autoriza declarar massas/cargas/spins experimentais sem
resolver o setor correspondente.

---

## 3. O que conta como solíton da GDQ?

Um solíton da GDQ é uma configuração:

\[
\boxed{
\mathfrak S=(g,B,f,\bar f)
}
\]

tal que:

1. resolve as equações estacionárias da ação/fluxo;
2. possui energia finita;
3. possui densidade normalizável;
4. tem comportamento assintótico controlado;
5. pertence a um setor topológico definido;
6. possui espectro linear com número finito de modos zero;
7. é estável sob perturbações admissíveis;
8. possui invariantes que possam ser lidos como massa, carga e spin.

O ponto fixo do fluxo em \(\tau\) satisfaz:

\[
\boxed{
\partial_\tau g=0,
\qquad
\partial_\tau B=0,
\qquad
\partial_\tau f=0
}
\]

módulo difeomorfismos e calibres.

Em gauge de DeTurck--Hodge, isso vira um sistema elíptico:

\[
\boxed{
\mathcal E_g(g,B,\phi)=0,
\qquad
\mathcal E_B(g,B,\phi)=0,
\qquad
\mathcal E_\phi(g,B,\phi)=0.
}
\]

Essa é a forma correta. Um perfil gaussiano, um vórtice desenhado ou uma
densidade escolhida externamente não basta, a menos que se verifique que ele
satisfaz essas equações.

---

## 4. Solução explícita mínima: solíton gaussiano neutro

Existe uma solução explícita de referência: o solíton gaussiano encolhedor no
setor sem torção.

Considere:

\[
\boxed{
M=\mathbb R^d,
\qquad
g_{ij}=\delta_{ij},
\qquad
B=0,
}
\]

e:

\[
\boxed{
\phi(x)=\frac{|x|^2}{4\sigma},
\qquad
\sigma>0.
}
\]

Então:

\[
\boxed{
R_{ij}=0,
\qquad
\nabla_i\nabla_j\phi=\frac1{2\sigma}\delta_{ij}.
}
\]

Logo:

\[
\boxed{
R_{ij}+\nabla_i\nabla_j\phi
=
\frac1{2\sigma}g_{ij}.
}
\]

Portanto:

\[
\boxed{
(\mathbb R^d,\delta,\phi)
}
\]

é uma solução explícita do sistema de solíton encolhedor de Ricci--Perelman.

Na GDQ, a densidade correspondente é:

\[
\boxed{
\rho(x)=e^{-\phi(x)}
=
\exp\left(-\frac{|x|^2}{4\sigma}\right).
}
\]

Normalizando:

\[
\boxed{
\rho_N(x)
=
\frac{1}{(4\pi\sigma)^{d/2}}
\exp\left(-\frac{|x|^2}{4\sigma}\right).
}
\]

Essa solução é importante porque prova que o formalismo contém solítons
normalizáveis explícitos.

Mas ela é neutra:

\[
\boxed{
B=0,
\qquad
\chi=0,
\qquad
Q=0,
\qquad
S=0.
}
\]

Logo, ela representa o bloco escalar/neutro de referência, não ainda um
férmion carregado.

---

## 5. Energia do solíton de referência

Para o solíton gaussiano, no setor puro de Perelman:

\[
\boxed{
\mathcal W
=
\int_M
\left[
\sigma(R+|\nabla\phi|^2)+\phi-d
\right]
\rho_N\,dV.
}
\]

Como:

\[
R=0,
\qquad
|\nabla\phi|^2=\frac{|x|^2}{4\sigma^2},
\]

temos:

\[
\sigma|\nabla\phi|^2=\frac{|x|^2}{4\sigma}.
\]

Para a gaussiana normalizada:

\[
\boxed{
\left\langle \frac{|x|^2}{4\sigma}\right\rangle=\frac d2.
}
\]

Também:

\[
\boxed{
\langle\phi\rangle=\frac d2.
}
\]

Logo:

\[
\boxed{
\mathcal W
=
\frac d2+\frac d2-d=0.
}
\]

Assim, a energia livre geométrica renormalizada do solíton gaussiano é finita
e igual ao valor crítico:

\[
\boxed{
\mathcal W_{\rm gauss}=0.
}
\]

Uma energia física efetiva pode ser definida por:

\[
\boxed{
E[\mathfrak S]
=
\frac{\hbar}{\Lambda_C^2}
\int_M
\left[
\sigma
\left(
R-\frac1{12}|B|^2+|\nabla f|^2
\right)
+\phi-d
\right]
\mathcal U\,dV.
}
\]

Para setores físicos carregados, a massa de repouso é:

\[
\boxed{
mc^2=E[\mathfrak S]-E[\mathfrak S_{\rm vac}].
}
\]

---

## 6. Energia finita

A energia é finita se:

\[
\boxed{
\rho=e^{-\phi}\in L^1(M),
\qquad
\int_M\rho\,dV=1,
}
\]

e:

\[
\boxed{
\int_M
\left(
|R|+|\nabla f|^2+|B|^2
\right)\rho\,dV<\infty.
}
\]

No solíton gaussiano:

\[
\rho_N\sim e^{-|x|^2/(4\sigma)},
\]

portanto todas as integrais polinomiais ponderadas por \(\rho_N\) são finitas.

Para solítons carregados/spinoriais, o mesmo critério deve ser imposto:

\[
\boxed{
R,\ B,\ \nabla f
\text{ podem ser singulares localmente apenas se a energia ponderada for
integrável.}
}
\]

Nós \(\rho=0\) são tratados como defeitos/topologia ou removidos por cartas,
conforme a Questão 14.

---

## 7. Carga

A carga não é atribuída arbitrariamente. Ela deve ser um invariante de
circulação/holonomia do setor topológico.

Defina a fase:

\[
\boxed{
\chi=\frac{S_R}{\hbar}.
}
\]

A circulação em torno de um ciclo não trivial \(C\) é:

\[
\boxed{
N_C
=
\frac1{2\pi}\oint_C d\chi
\in\mathbb Z.
}
\]

Um candidato a carga elétrica efetiva é:

\[
\boxed{
Q
=
e\,\sum_a q_aN_a,
}
\]

onde \(q_a\) são pesos de projeção do setor de calibre efetivo.

No solíton gaussiano:

\[
\boxed{
\chi=0
\quad\Longrightarrow\quad
Q=0.
}
\]

Para uma partícula carregada, é necessário resolver o sistema com:

\[
\boxed{
\oint_Cd\chi=2\pi N\neq0
}
\]

e verificar que o campo correspondente continua tendo energia finita.

---

## 8. Spin

O spin é lido como holonomia/circulação torsional.

No setor de fase:

\[
\boxed{
S_{\rm circ}
=
\oint_C\nabla S_R\cdot dx
=
\hbar\oint_Cd\chi.
}
\]

Para setores spinoriais, a condição meio-inteira vem da estrutura spin já
fixada nas questões anteriores:

\[
\boxed{
\Psi\mapsto-\Psi
\quad
\text{sob rotação }2\pi,
}
\]

e:

\[
\boxed{
\Psi\mapsto\Psi
\quad
\text{sob rotação }4\pi.
}
\]

Na linguagem torsional, uma definição integral de spin é:

\[
\boxed{
J_i
=
\int_{\Sigma}
\epsilon_{ijk}x^jT^k{}_{\ell m}u^\ell n^m\,
\rho\,d\mu_h,
}
\]

ou, de forma equivalente no setor efetivo:

\[
\boxed{
\mathbf J
=
\int_\Sigma \rho\,\mathbf x\times\nabla S_R\,d\mu_h
+\mathbf J_{\rm torsion}.
}
\]

No solíton gaussiano sem fase e sem torção:

\[
\boxed{
J=0.
}
\]

Um férmion exige setor com holonomia spinorial:

\[
\boxed{
J=\frac{\hbar}{2}
}
\]

e essa condição deve ser verificada como invariante topológico, não ajustada
por perfil externo.

---

## 9. Massa

A massa efetiva é definida pelo excesso de energia do solíton em relação ao
vácuo:

\[
\boxed{
m[\mathfrak S]
=
\frac{1}{c^2}
\left(
E[\mathfrak S]-E[\mathfrak S_{\rm vac}]
\right).
}
\]

Na redução estocástica da Questão 16, a mesma massa aparece no fator:

\[
\boxed{
\Omega[\mathfrak S]=\frac{m[\mathfrak S]}{m_0},
\qquad
\nu_{\rm eff}=\nu_0\Omega^{-1}.
}
\]

Assim, a massa não é um parâmetro primitivo do vácuo. Ela é um funcional da
geometria solitônica:

\[
\boxed{
m=m[g,B,f,\bar f,\text{setor topológico}].
}
\]

Para o solíton gaussiano puro, sem escala física adicional, obtém-se apenas a
escala crítica normalizada. Para partículas reais, é preciso resolver o
problema espectral com as condições de contorno, topologia e setor de calibre.

---

## 10. Estabilidade linear

Linearize o sistema em torno do solíton:

\[
\boxed{
g=g_\ast+h,
\qquad
B=B_\ast+\beta,
\qquad
f=f_\ast+\eta.
}
\]

No gauge fixado, a linearização tem forma:

\[
\boxed{
\partial_\tau
\begin{pmatrix}
h\\
\beta\\
\eta
\end{pmatrix}
=
-\mathcal L_{\mathfrak S}
\begin{pmatrix}
h\\
\beta\\
\eta
\end{pmatrix}
+\text{termos quadráticos}.
}
\]

O operador \(\mathcal L_{\mathfrak S}\) é o Hessiano do funcional geométrico
ponderado no ponto crítico.

A estabilidade linear exige:

\[
\boxed{
\langle U,\mathcal L_{\mathfrak S}U\rangle_\rho\ge0
}
\]

para perturbações \(U=(h,\beta,\eta)\) ortogonais aos modos de gauge e aos
modos zero físicos.

Para o solíton gaussiano, o operador reduz ao operador de Ornstein--Uhlenbeck
ponderado:

\[
\boxed{
\mathcal L_{\rm gauss}
=
-\Delta+\frac{x}{2\sigma}\cdot\nabla+\text{constante},
}
\]

cujo espectro é discreto e não negativo no espaço \(L^2(\rho_NdV)\), após
remover translações, dilatações e difeomorfismos.

Logo, o solíton gaussiano é linearmente estável módulo simetrias.

---

## 11. Estabilidade não linear

A estabilidade não linear segue da monotonicidade do funcional torsional:

\[
\boxed{
\frac{d\mathcal F_T}{d\tau}\ge0,
\qquad
\frac{d\mathcal W_T}{d\tau}\ge0.
}
\]

Se o solíton é um mínimo local estrito do funcional modulado por simetrias, há
estabilidade orbital:

\[
\boxed{
\|U(0)-U_\ast\|\ll1
\quad\Longrightarrow\quad
U(\tau)\to\mathcal O(U_\ast)
}
\]

onde \(\mathcal O(U_\ast)\) é a órbita por difeomorfismos, calibres e
simetrias globais.

Para solítons carregados, a estabilidade não linear precisa ser verificada
setor por setor, porque pode haver:

1. modos de separação entre núcleos;
2. modos de rotação;
3. modos de calibre;
4. modos de escala;
5. canais de decaimento topológico.

Portanto:

\[
\boxed{
\text{estabilidade não linear não pode ser declarada por analogia;}
}
\]

ela deve vir do Hessiano e da monotonicidade no setor topológico fixado.

---

## 12. Como determinar a estabilidade na prática

O material já existente no texto aponta para um procedimento em quatro níveis.

### 12.1 Primeiro nível: ponto crítico verdadeiro

Antes de falar em estabilidade, a configuração candidata precisa satisfazer:

\[
\boxed{
\mathcal E_g(g_\ast,B_\ast,f_\ast)=0,
\qquad
\mathcal E_B(g_\ast,B_\ast,f_\ast)=0,
\qquad
\mathcal E_f(g_\ast,B_\ast,f_\ast)=0.
}
\]

Equivalente:

\[
\boxed{
\nabla\mathcal I_T(g_\ast,B_\ast,f_\ast)=0
}
\]

no setor de gauge e topologia escolhido, onde:

\[
\boxed{
\mathcal I_T=\mathcal F_T
\quad\text{para escala fixa,}
\qquad
\mathcal I_T=\mathcal W_T
\quad\text{para escala variável.}
}
\]

Se o resíduo:

\[
\boxed{
\mathcal R_\ast
:=
\|\mathcal E_g\|^2+\|\mathcal E_B\|^2+\|\mathcal E_f\|^2
}
\]

não tende a zero analiticamente ou numericamente, não há ainda solíton validado.

### 12.2 Segundo nível: Hessiana ou operador de Jacobi

Perturbe:

\[
\boxed{
g=g_\ast+h,
\qquad
B=B_\ast+\beta,
\qquad
f=f_\ast+\eta.
}
\]

Após gauge de DeTurck--Hodge, define-se:

\[
\boxed{
U=(h,\beta,\eta).
}
\]

A segunda variação é:

\[
\boxed{
\delta^2\mathcal I_T[U,U]
=
\langle U,\mathcal J_{\mathfrak S}U\rangle_{\rho_\ast},
}
\]

onde:

\[
\boxed{
\mathcal J_{\mathfrak S}
=
D^2\mathcal I_T|_{\mathfrak S}
}
\]

é o operador de Jacobi/Hessiano do solíton.

A estabilidade linear exige:

\[
\boxed{
\operatorname{spec}(\mathcal J_{\mathfrak S})
\subseteq[0,\infty)
}
\]

depois de remover:

1. difeomorfismos;
2. modos de gauge de \(B\);
3. translações;
4. rotações;
5. dilatações;
6. moduli topológicos legítimos.

Se existe:

\[
\boxed{
\lambda_{\min}<0,
}
\]

há direção instável.

Se:

\[
\boxed{
\lambda_{\min}=0
}
\]

é preciso decidir se o modo zero é simetria/modulus ou instabilidade marginal.

Se:

\[
\boxed{
\lambda_{\min}>0
}
\]

no complemento dos modos zero, o solíton é linearmente estável.

### 12.3 Terceiro nível: monotonicidade como Lyapunov

O capítulo 17 fornece o funcional de Lyapunov:

\[
\boxed{
\frac{d\mathcal F_T}{d\tau}\ge0,
\qquad
\frac{d\mathcal W_T}{d\tau}\ge0.
}
\]

Isso mostra que o fluxo tem direção entrópica controlada. Mas, como já estava
no plano de auditoria:

\[
\boxed{
\text{monotonicidade não implica automaticamente estabilidade de partículas.}
}
\]

A monotonicidade vira estabilidade não linear apenas quando combinada com:

1. ponto crítico isolado módulo simetrias;
2. Hessiana sem autovalores negativos;
3. controle dos modos zero;
4. preservação do setor topológico;
5. critério de continuação do fluxo.

Então:

\[
\boxed{
\mathcal W_T(U(\tau))-\mathcal W_T(U_\ast)
}
\]

funciona como distância energética ao atrator.

### 12.4 Quarto nível: teste numérico obrigatório

Para uma solução numérica, a estabilidade deve ser demonstrada por:

1. convergência de malha;
2. resíduo estacionário \(\mathcal R_\ast\to0\);
3. conservação de carga, spin e setor topológico;
4. cálculo da matriz Hessiana discreta;
5. espectro dos autovalores;
6. identificação dos modos zero;
7. evolução temporal de perturbações pequenas;
8. verificação de retorno ao mesmo atrator, módulo simetrias.

Em forma operacional:

\[
\boxed{
\text{estável}
\Longleftrightarrow
\mathcal R_\ast\approx0,
\quad
\lambda_{\rm neg}=0,
\quad
\text{modos zero explicados},
\quad
\delta U(\tau)\to0
\text{ módulo simetrias.}
}
\]

Esse é o teste que deve ser exigido do Apêndice 8 ou de qualquer solver
posterior.

---

## 13. Modos zero

Todo solíton possui modos zero associados a simetrias.

Para o solíton gaussiano em \(\mathbb R^d\):

\[
\boxed{
\text{translações: }d\text{ modos zero;}
}
\]

\[
\boxed{
\text{rotações: }\frac{d(d-1)}2\text{ modos, se o setor não fixa orientação;}
}
\]

\[
\boxed{
\text{escala: }1\text{ modo marginal associado a }\sigma.
}
\]

Além disso, há modos de difeomorfismo, removidos pelo gauge de DeTurck.

Para solítons com \(B\) e fase:

\[
\boxed{
\text{há também modos zero de calibre e modos de moduli topológicos.}
}
\]

A regra correta é:

\[
\boxed{
\ker\mathcal L_{\mathfrak S}
=
\text{simetrias}
\oplus
\text{moduli físicos}.
}
\]

Se aparecer modo negativo, o solíton não é estável. Se aparecer modo zero
físico não controlado, o solíton pertence a uma família contínua e a massa não
é isolada.

---

## 14. Comportamento assintótico

Para energia finita em setor aberto, exige-se:

\[
\boxed{
g_{ij}\to g^{\rm vac}_{ij},
\qquad
B\to0,
\qquad
\nabla f\to0
\quad
\text{ou decaimento gaussiano ponderado},
}
\]

com:

\[
\boxed{
\rho\to0
}
\]

rápido o suficiente para normalização.

No solíton gaussiano:

\[
\boxed{
\rho_N(x)\sim e^{-|x|^2/(4\sigma)}.
}
\]

Para setores carregados, a fase pode ter comportamento assintótico de
holonomia:

\[
\boxed{
\chi\sim N\theta
}
\]

em torno de ciclos não triviais, desde que:

\[
\boxed{
\int|\nabla\chi|^2\rho\,dV<\infty.
}
\]

Esse peso por \(\rho\) é o que permite circulação topológica sem energia
infinita.

---

## 15. Interação entre dois solítons

Dois solítons bem separados:

\[
\boxed{
\mathfrak S_1,\mathfrak S_2
}
\]

interagem pelo termo cruzado da energia:

\[
\boxed{
E_{\rm int}(R)
=
E[\mathfrak S_1\#_R\mathfrak S_2]
-E[\mathfrak S_1]
-E[\mathfrak S_2].
}
\]

Para separação grande \(R\), a interação é controlada pelas caudas:

\[
\boxed{
E_{\rm int}(R)
\sim
\int
\left(
\langle\nabla f_1,\nabla f_2\rangle
-\frac16\langle B_1,B_2\rangle
+\text{termos de fase}
\right)
\rho_{12}\,dV.
}
\]

Consequências:

1. caudas gaussianas produzem interação exponencialmente pequena;
2. caudas de fase/topologia produzem interação de longo alcance;
3. torção alinhada pode produzir atração ou repulsão;
4. setores de carga oposta podem formar estados ligados;
5. setores topológicos incompatíveis sofrem dissipação pelo fluxo.

Uma lei de força quantitativa exige resolver o problema de dois corpos no
setor correspondente.

---

## 16. O que o capítulo original 18 realmente prova

O capítulo original `18 - Princípio da Incerteza Geométrico.md` não responde
diretamente à Questão 18 de auditoria.

Ele fornece argumentos úteis para:

1. finitude de energia por desigualdade de incerteza;
2. estabilidade contra colapso ultravioleta;
3. papel da positividade hermitiana;
4. limite de localização mínima;
5. relação entre \(\rho\), \(f\) e entropia.

Mas ele não exibe, por si só:

1. solução carregada explícita;
2. massa calculada como autovalor;
3. carga topológica verificada;
4. spin verificado;
5. espectro linear do Hessiano;
6. interação entre dois solítons.

Portanto, o capítulo 18 original é evidência de estabilidade/regularização,
não prova completa de existência de partículas solitônicas.

---

## 17. O que o Apêndice 8 fornece

O `Apêndice 8 - Simulação Numérica do Solíton de Ricci Bariônico.md` fornece
um protótipo numérico útil, mas ainda precisa ser elevado ao padrão de
validação exigido por `18-0.md`.

Ele contém:

1. uma evolução numérica de densidade;
2. termos de Bohm e Cartan;
3. normalização de \(\rho\);
4. extração aproximada de energia/massa;
5. extração aproximada de vorticidade/spin.

Mas, para fechar como prova numérica, faltam:

1. declarar exatamente qual sistema discreto aproxima a ação oficial;
2. demonstrar convergência com refinamento de malha;
3. monitorar resíduo das equações estacionárias;
4. mostrar conservação de invariantes topológicos;
5. calcular espectro do operador linearizado;
6. separar modos zero de modos instáveis;
7. fornecer tabela final de energia, massa, carga e spin;
8. comparar diferentes condições de contorno.

Assim, o Apêndice 8 é aproveitável como ponto de partida computacional, mas não
deve ser citado como prova final sem esses testes.

---

## 18. Critério final de validação de uma partícula

Para declarar que uma partícula \(P\) foi obtida como solíton da GDQ, deve-se
fornecer uma ficha:

\[
\boxed{
\mathfrak S_P=(g_P,B_P,f_P,\bar f_P)
}
\]

com:

| Item | Exigência |
|---|---|
| Equação | \(\mathcal E_g=\mathcal E_B=\mathcal E_f=0\) |
| Energia | \(E[\mathfrak S_P]<\infty\) |
| Massa | \(m_P=(E[\mathfrak S_P]-E_{\rm vac})/c^2\) |
| Carga | \(Q_P=e\sum q_aN_a\) |
| Spin | holonomia/circulação torsional ou estrutura spin |
| Estabilidade linear | Hessiano sem modos negativos |
| Estabilidade não linear | mínimo local módulo simetrias |
| Modos zero | apenas simetrias/moduli físicos |
| Assintótica | decaimento suficiente para energia finita |
| Interação | \(E_{\rm int}(R)\) ou espalhamento efetivo |

Sem essa ficha, a partícula ainda é uma interpretação, não uma solução
validada.

---

## 19. Relação com a ação oficial

A ação fundamental permanece a ação oficial da GDQ:

\[
\boxed{
\mathcal{S}_{\rm GDQ}
=
\int_{\gamma}
\left[
\int_{\mathcal M_\mathbb C}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau
\left(
\mathcal R
+g^{\mu\bar\nu}
\partial_\mu f
\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}
-n
\right]
\mathcal U
\sqrt{\det g}\,
d^{2n}z
\right]
\frac{d\tau}{\tau}.
}
\]

com:

\[
\boxed{
\mathcal U
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}
=
\frac{\rho}{(4\pi z_\tau)^n}.
}
\]

O solíton não é introduzido por uma nova ação. Ele é uma solução estacionária
ou assintótica das equações extraídas da ação oficial e de sua camada
torsional/Bismut compatível.

---

## 20. Veredito

\[
\boxed{
\text{Questão 18 fechada como critério matemático e solução neutra mínima.}
}
\]

O que fica fechado:

1. a definição correta de solíton da GDQ;
2. a equação estacionária que ele deve satisfazer;
3. uma solução explícita neutra, o solíton gaussiano;
4. energia finita para essa solução;
5. critério de carga, spin e massa;
6. critério de estabilidade linear/não linear;
7. procedimento explícito para determinar estabilidade;
8. modos zero esperados;
9. comportamento assintótico;
10. forma geral da interação entre solítons;
11. protocolo para validar numericamente solítons físicos.

O que não deve ser afirmado sem cálculo adicional:

\[
\boxed{
\text{``o elétron/próton/nêutron já foi rigorosamente obtido como solução
completa''}
}
\]

salvo se for anexada a solução explícita ou numérica com resíduo, energia,
carga, spin, massa, espectro linear e teste de estabilidade.
