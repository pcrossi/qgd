# Questão 20 — Qual é o espaço de Hilbert?

## 1. Pergunta

A Questão 20 pergunta:

\[
\boxed{
\text{qual é o espaço de Hilbert físico da GDQ e como nele entram estados,
operadores, evolução, observáveis e composição de sistemas?}
}
\]

As respostas necessárias de `20-0.md` são:

1. definição do espaço;
2. produto interno;
3. domínio dos operadores;
4. estados físicos;
5. evolução;
6. observáveis;
7. sistemas compostos;
8. regra de produto tensorial.

A resposta correta deve evitar dois erros opostos:

1. tratar o espaço de Hilbert como objeto ontológico primário, apagando a
   proposta geométrica da GDQ;
2. negar o espaço de Hilbert operacional, tornando impossível falar de
   espectro, observáveis, unitariedade, composição e medições.

Na GDQ, a geometria é a camada fundamental. O espaço de Hilbert é a camada
operacional reconstruída.

---

## 2. Resposta curta

O espaço de Hilbert físico da GDQ é:

\[
\boxed{
\mathcal H_{\rm phys}
=
\overline{
\mathcal D_+/
(\mathcal N+\mathcal G)
}.
}
\]

Aqui:

- \(\mathcal D_+\) é o espaço de funcionais cilíndricos, regulares e de
  suporte temporal positivo dos campos geométricos da teoria;
- \(\mathcal N\) é o subespaço de vetores de norma nula produzido pela
  reflexão positiva;
- \(\mathcal G\) representa redundâncias de descrição: difeomorfismos,
  gauge, escolha de seção, modos longitudinais e demais direções não físicas;
- a barra indica completamento na norma induzida pelo produto interno.

O produto interno é:

\[
\boxed{
\langle [F],[G]\rangle_{\mathcal H}
=
\langle \Theta F\,G\rangle_E.
}
\]

Essa é a construção Osterwalder--Schrader já usada na Questão 7. Ela transforma
a medida geométrica euclidiana/complexa regularizada da GDQ em um espaço de
Hilbert lorentziano de norma positiva.

---

## 3. Campos sobre os quais os funcionais atuam

O espaço fundamental de configurações é, setorialmente:

\[
\boxed{
\mathfrak C
=
\{(g_{\mu\bar\nu},f,\bar f;B,A,\psi,\ldots)\ \text{admissíveis}\}.
}
\]

Na ação oficial, os campos fundamentais são:

\[
\boxed{
g_{\mu\bar\nu},\quad f,\quad \bar f.
}
\]

A medida:

\[
\boxed{
\mathcal U
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}
=
\frac{\rho}{(4\pi z_\tau)^n}
}
\]

é derivada, não campo independente.

Em setores efetivos, entram também:

\[
B,\quad A,\quad \psi,\quad \Psi,
\]

onde \(B\) é a camada torsional/Bismut, \(A\) representa conexões de gauge
efetivas, \(\psi\) representa setores spinoriais quando necessários, e:

\[
\boxed{
\Psi=\sqrt\rho\,e^{iS_R/\hbar}
}
\]

é a reconstrução Madelung da amplitude operacional.

Portanto, um vetor de Hilbert não é uma geometria pontual isolada. Ele é uma
classe de funcionais de configurações geométricas.

---

## 4. Domínio regular mínimo

O domínio regular já delimitado na Questão 14 é:

\[
\boxed{
\mathcal D_{\rm reg}
=
\{
(g,f):
g\in C^2,\ 
f\in C^2,\ 
\rho=e^{-(f+\bar f)/2}>0,\ 
S_R=\hbar\operatorname{Im}f
\text{ localmente monovalorado}
\}.
}
\]

Com:

\[
\boxed{
\rho\in C^2,
\qquad
S_R\in C^2,
\qquad
\Psi=\sqrt\rho e^{iS_R/\hbar}.
}
\]

Fora desse domínio, a teoria precisa de extensões setoriais:

1. nós exigem remoção do conjunto nodal ou tratamento distribucional;
2. fases multivaloradas exigem atlas e holonomias;
3. spin exige estrutura spinorial;
4. gauge exige fibrados associados;
5. estados solitônicos singulares exigem condições de bordo/topologia.

Assim:

\[
\boxed{
\mathcal H_{\rm phys}
\text{ é construído por setores.}
}
\]

Não há um único espaço \(L^2\) ingênuo que contenha todos os setores sem
qualificações.

---

## 5. Espaço pré-Hilbert

Define-se \(\mathcal D_+\) como o espaço de funcionais cilíndricos:

\[
\boxed{
F[\Phi]
=
F(\Phi(x_1),\ldots,\Phi(x_k)),
\qquad x_i^0>0,
}
\]

onde:

\[
\Phi
\in
\mathfrak C
\]

representa coletivamente os campos geométricos e efetivos do setor em questão.

O índice \(+\) significa que os funcionais têm suporte no semiespaço temporal
euclidiano positivo. Essa escolha é necessária para aplicar reflexão positiva.

---

## 6. Produto interno

Se \(\Theta\) é a reflexão temporal euclidiana:

\[
\boxed{
\Theta: x_E^0\mapsto -x_E^0,
}
\]

define-se:

\[
\boxed{
(F,G)
=
\langle \Theta F\,G\rangle_E.
}
\]

O valor esperado euclidiano é:

\[
\boxed{
\langle \mathcal O\rangle_E
=
\frac{1}{Z_E}
\int_{\mathfrak C}
\mathcal O[\Phi]\,
e^{-\mathcal S_E[\Phi]/\hbar}\,
D\mu_{\rm GDQ}[\Phi].
}
\]

No formalismo GDQ, \(\mathcal S_E\) é a projeção euclidiana/geométrica
compatível com a ação oficial de contorno em \(\gamma\), e \(D\mu_{\rm GDQ}\)
é a medida geométrica regularizada induzida por:

\[
\boxed{
\mathcal U\sqrt{\det g}\,d^{2n}z\,\frac{d\tau}{\tau}.
}
\]

A condição crucial é:

\[
\boxed{
(F,F)\ge 0.
}
\]

Essa é a reflexão positiva. Sem ela, não existe espaço de Hilbert físico de
norma positiva.

---

## 7. Subespaço nulo e completamento

Define-se:

\[
\boxed{
\mathcal N
=
\{F\in\mathcal D_+:(F,F)=0\}.
}
\]

Então:

\[
\boxed{
\mathcal H_0
=
\mathcal D_+/\mathcal N.
}
\]

O espaço de Hilbert reconstruído é:

\[
\boxed{
\mathcal H
=
\overline{\mathcal H_0}.
}
\]

Após remover redundâncias:

\[
\boxed{
\mathcal H_{\rm phys}
=
\overline{
\mathcal D_+/
(\mathcal N+\mathcal G)
}.
}
\]

Esse é o espaço físico de estados.

---

## 8. Interpretação de \(\mathcal G\)

O subespaço \(\mathcal G\) representa direções que não são estados físicos
distintos.

Inclui:

1. difeomorfismos;
2. transformações de gauge;
3. mudanças de carta;
4. modos longitudinais;
5. modos puros de bordo exato;
6. redundâncias BRST, se a linguagem BRST auxiliar for usada.

Assim, em linguagem de vínculos:

\[
\boxed{
\widehat C_a|\Psi_{\rm phys}\rangle=0.
}
\]

Em linguagem BRST auxiliar:

\[
\boxed{
\mathcal H_{\rm phys}
\simeq
H^0(Q_{\rm BRST})
=
\frac{\ker Q_{\rm BRST}}{\operatorname{im}Q_{\rm BRST}}.
}
\]

Mas isso é uma camada de auditoria/quantização auxiliar, não substitui a ação
oficial.

---

## 9. Representação \(L^2\) no setor regular de uma partícula

No setor regular Madelung, a reconstrução operacional reduz-se ao Hilbert
usual:

\[
\boxed{
\mathcal H_1
=
L^2(N,d\Sigma_h)
}
\]

ou, se houver fibrado interno:

\[
\boxed{
\mathcal H_1
=
L^2(N,E,d\Sigma_h),
}
\]

onde:

- \(N\) é a fatia física lorentziana efetiva;
- \(h\) é a métrica lorentziana constitutiva;
- \(E\) é o fibrado de carga/spin/setor interno;
- \(d\Sigma_h\) é a medida espacial induzida na folha de Cauchy.

O produto interno é:

\[
\boxed{
\langle\Psi,\Phi\rangle
=
\int_\Sigma
\overline{\Psi(x)}\Phi(x)\,
d\Sigma_h(x).
}
\]

Com:

\[
\boxed{
\|\Psi\|^2
=
\int_\Sigma |\Psi|^2\,d\Sigma_h
=
\int_\Sigma \rho\,d\Sigma_h
=1.
}
\]

Para espinores:

\[
\boxed{
\langle\psi,\chi\rangle
=
\int_\Sigma
\psi^\dagger\chi\,
d\Sigma_h
}
\]

na representação de uma partícula, ou o produto indefinido covariante com
posterior seleção de subespaço físico em formulações relativísticas.

---

## 10. Estados físicos

Um estado físico pode ser descrito de três formas equivalentes por setor:

### 10.1 Vetor puro

\[
\boxed{
|\Psi\rangle\in\mathcal H_{\rm phys},
\qquad
\|\Psi\|=1.
}
\]

No setor regular:

\[
\boxed{
\Psi(x)=\sqrt\rho\,e^{iS_R/\hbar}.
}
\]

### 10.2 Raio projetivo

Como fases globais não são observáveis:

\[
\boxed{
|\Psi\rangle\sim e^{i\alpha}|\Psi\rangle.
}
\]

O estado físico puro é um raio em:

\[
\boxed{
\mathbb P(\mathcal H_{\rm phys}).
}
\]

### 10.3 Estado misto

Para setores abertos, medições, coarse graining ou subsistemas:

\[
\boxed{
\varrho\ge0,
\qquad
\operatorname{Tr}\varrho=1.
}
\]

Os valores esperados são:

\[
\boxed{
\langle A\rangle_\varrho
=
\operatorname{Tr}(\varrho A).
}
\]

---

## 11. Domínio dos operadores

Operadores físicos não são definidos em todo \(\mathcal H\). Eles são definidos
em domínios densos.

Para um observável \(A\):

\[
\boxed{
A:D(A)\subset\mathcal H_{\rm phys}\to\mathcal H_{\rm phys},
\qquad
D(A)\ \text{denso}.
}
\]

Exemplos:

\[
\boxed{
\widehat x^i\Psi=x^i\Psi,
\qquad
\widehat p_i\Psi=-i\hbar\nabla_i\Psi.
}
\]

Domínios típicos:

\[
\boxed{
D(\widehat p_i)=H^1(\Sigma,E),
\qquad
D(H)=H^2(\Sigma,E)
}
\]

quando o Hamiltoniano é de segunda ordem elíptica no setor não relativístico.

Para operadores geométricos/torsionais:

\[
\boxed{
D(\widehat{\mathcal O})
\subset
\{ \Psi:\mathcal O\Psi\in\mathcal H_{\rm phys}\}.
}
\]

Para que um observável seja aceitável:

\[
\boxed{
A=A^\dagger
}
\]

ou, mais rigorosamente, \(A\) deve ser autoadjunto, não apenas simétrico.

---

## 12. Observáveis

Observáveis são operadores autoadjuntos ou, mais geralmente, elementos
autoadjuntos da álgebra local:

\[
\boxed{
A=A^\dagger,
\qquad
A\in\mathcal A(O).
}
\]

A probabilidade de medir um resultado em \(\Delta\subset\mathbb R\) é dada
pelo projetor espectral:

\[
\boxed{
\mathbb P_A(\Delta)
=
\langle\Psi,E_A(\Delta)\Psi\rangle.
}
\]

Ou, para estados mistos:

\[
\boxed{
\mathbb P_A(\Delta)
=
\operatorname{Tr}(\varrho E_A(\Delta)).
}
\]

A regra de Born aparece como:

\[
\boxed{
\mathbb P(x\in R)
=
\int_R |\Psi(x)|^2\,d\Sigma_h
=
\int_R \rho(x)\,d\Sigma_h.
}
\]

Na linguagem GDQ:

\[
\boxed{
\rho=e^{-(f+\bar f)/2}.
}
\]

Logo a regra de Born é compatível com a parte real positiva do campo \(f\).

---

## 13. Evolução

Há duas evoluções conceitualmente distintas.

### 13.1 Evolução em \(\tau\)

\(\tau\) é parâmetro de fluxo/escala/difusão:

\[
\boxed{
z_\tau=\tau+i\nu_0t,
\qquad
\nu_0=\frac{\hbar}{2m_0}.
}
\]

O fluxo em \(\tau\) é geométrico/renormalizacional. Ele não é, por si só, o
grupo unitário de tempo físico.

### 13.2 Evolução em \(t\)

Pela reconstrução OS:

\[
\boxed{
T_E(a)=e^{-aH/\hbar},
\qquad
H=H^\dagger,
\qquad
H\ge0.
}
\]

A evolução física lorentziana é:

\[
\boxed{
U(t)=e^{-itH/\hbar}.
}
\]

Como \(H\) é autoadjunto:

\[
\boxed{
U(t)^\dagger U(t)=1.
}
\]

Assim, a norma é preservada:

\[
\boxed{
\|U(t)\Psi\|=\|\Psi\|.
}
\]

Essa afirmação será detalhada na Questão 21. Para a Questão 20, basta fixar
que o gerador temporal físico é \(H\) no espaço \(\mathcal H_{\rm phys}\), não
o parâmetro \(\tau\) isolado.

---

## 14. Microcausalidade e álgebra local

Para uma região \(O\), define-se uma álgebra local:

\[
\boxed{
\mathcal A(O)\subset\mathcal B(\mathcal H_{\rm phys})
}
\]

ou, para operadores não limitados, uma álgebra gerada por operadores
essencialmente autoadjuntos em domínio comum denso.

Se duas regiões são separadas espacialmente pela métrica lorentziana efetiva
\(h\):

\[
\boxed{
O_1\perp_h O_2,
}
\]

então:

\[
\boxed{
[\mathcal A(O_1),\mathcal A(O_2)]=0.
}
\]

Esse resultado é compatível com a Questão 8: o propagador simétrico de
Sudarshan entra como restrição global/de contorno, enquanto a resposta física
controlável a fontes locais é retardada.

---

## 15. Sistemas compostos

Para dois sistemas distinguíveis e aproximadamente desacoplados:

\[
\boxed{
\mathcal H_{AB}
=
\mathcal H_A\otimes\mathcal H_B.
}
\]

O produto interno fatoriza:

\[
\boxed{
\langle\psi_A\otimes\psi_B,\phi_A\otimes\phi_B\rangle
=
\langle\psi_A,\phi_A\rangle_A
\langle\psi_B,\phi_B\rangle_B.
}
\]

Estados emaranhados são elementos de:

\[
\boxed{
\mathcal H_A\otimes\mathcal H_B
}
\]

que não podem ser escritos como produto simples:

\[
\boxed{
\Psi_{AB}\ne\psi_A\otimes\psi_B.
}
\]

Na linguagem geométrica, isso significa que a configuração total não fatoriza
em duas geometrias independentes; há correlação global de fase, holonomia ou
contorno.

---

## 16. Sistemas idênticos

Para \(N\) sistemas idênticos, primeiro forma-se:

\[
\boxed{
\mathcal H^{\otimes N}.
}
\]

Depois aplica-se a projeção estatística adequada.

Para bósons:

\[
\boxed{
\mathcal H_N^{(+)}
=
\operatorname{Sym}^N\mathcal H.
}
\]

Para férmions:

\[
\boxed{
\mathcal H_N^{(-)}
=
\wedge^N\mathcal H.
}
\]

No formalismo GDQ, a distinção entre simetrização e antissimetrização deve ser
entendida como consequência da holonomia/topologia/spin do setor. Mas, na
camada operacional de Hilbert, a regra é exatamente a usual:

\[
\boxed{
\Psi(\ldots,x_i,\ldots,x_j,\ldots)
=
\pm
\Psi(\ldots,x_j,\ldots,x_i,\ldots).
}
\]

---

## 17. Regra tensorial para composição de observáveis

Se \(A\) atua em \(\mathcal H_A\) e \(B\) atua em \(\mathcal H_B\), então:

\[
\boxed{
A\mapsto A\otimes I_B,
\qquad
B\mapsto I_A\otimes B.
}
\]

Para observáveis compostos:

\[
\boxed{
A\otimes B
}
\]

com valor esperado:

\[
\boxed{
\langle A\otimes B\rangle_{\Psi_{AB}}
=
\langle\Psi_{AB},(A\otimes B)\Psi_{AB}\rangle.
}
\]

Para estados produto:

\[
\boxed{
\langle A\otimes B\rangle_{\psi_A\otimes\psi_B}
=
\langle A\rangle_{\psi_A}
\langle B\rangle_{\psi_B}
}
\]

se \(A\otimes B\) for interpretado como produto de observáveis:

\[
\boxed{
\langle\psi_A\otimes\psi_B,
(A\otimes B)
\psi_A\otimes\psi_B\rangle
=
\langle A\rangle_{\psi_A}\langle B\rangle_{\psi_B}.
}
\]

Para Hamiltonianos desacoplados:

\[
\boxed{
H_{AB}
=
H_A\otimes I_B+I_A\otimes H_B.
}
\]

Com interação:

\[
\boxed{
H_{AB}
=
H_A\otimes I_B+I_A\otimes H_B+H_{\rm int}.
}
\]

Na GDQ, \(H_{\rm int}\) é a projeção operacional da interação geométrica entre
solítons, torções, holonomias e campos efetivos.

---

## 18. Relação com a ação oficial

A ação oficial permanece:

\[
\boxed{
\mathcal{S}_{\rm GDQ}=
\int_{\gamma}\left[\int_{\mathcal M_\mathbb C}\frac{\hbar}{\Lambda_C^2}
\left[\tau(\mathcal R+g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f)+\frac{f+\bar f}{2}-n\right]
\mathcal U\sqrt{\det g}\,d^{2n}z\right]\frac{d\tau}{\tau}.
}
\]

O espaço de Hilbert não altera essa ação.

Ele é reconstruído a partir:

1. da medida definida pela ação;
2. da positividade da densidade \(\rho\);
3. da reflexão positiva;
4. do quociente por nulos;
5. do quociente por redundâncias/gauge;
6. da continuação para o tempo físico \(t\).

Assim:

\[
\boxed{
\text{ação geométrica fundamental}
\quad\Longrightarrow\quad
\text{medida}
\quad\Longrightarrow\quad
\text{correladores}
\quad\Longrightarrow\quad
\mathcal H_{\rm phys}.
}
\]

---

## 19. O que ainda precisa ser provado para fechamento matemático total

A resposta estrutural acima fecha a Questão 20 no nível conceitual e
operacional. Mas o fechamento matemático completo exige verificar, em cada
setor:

1. existência da medida \(D\mu_{\rm GDQ}\);
2. normalização \(Z_E[0]<\infty\);
3. reflexão positiva;
4. propriedade de cluster;
5. domínio denso comum para os operadores principais;
6. autoadjunticidade essencial de \(H\) e dos observáveis;
7. remoção consistente de redundâncias;
8. fatorização tensorial para sistemas assintoticamente separados;
9. compatibilidade da estatística com a holonomia/spin do setor.

Portanto, a Questão 20 fica resolvida como estrutura canônica da teoria. A
verificação setor por setor permanece como trabalho técnico quando forem
tratadas partículas específicas.

---

## 20. Resposta final da Questão 20

\[
\boxed{
\mathcal H_{\rm phys}
=
\overline{
\mathcal D_+/
(\mathcal N+\mathcal G)
}
}
\]

com produto interno:

\[
\boxed{
\langle [F],[G]\rangle
=
\langle \Theta F\,G\rangle_E.
}
\]

No setor regular de uma partícula:

\[
\boxed{
\mathcal H_1=L^2(N,E,d\Sigma_h),
\qquad
\Psi=\sqrt\rho e^{iS_R/\hbar}.
}
\]

Estados físicos são vetores normalizados, raios projetivos ou matrizes
densidade em \(\mathcal H_{\rm phys}\), após remoção de nulos e redundâncias.

Observáveis são operadores autoadjuntos em domínios densos ou elementos
autoadjuntos das álgebras locais \(\mathcal A(O)\).

A evolução física em \(t\) é:

\[
\boxed{
U(t)=e^{-itH/\hbar},
\qquad
H=H^\dagger.
}
\]

Sistemas compostos distinguíveis obedecem:

\[
\boxed{
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B.
}
\]

Sistemas idênticos usam os subespaços:

\[
\boxed{
\operatorname{Sym}^N\mathcal H
\quad\text{ou}\quad
\wedge^N\mathcal H.
}
\]

Logo:

\[
\boxed{
\text{Questão 20 fechada estruturalmente.}
}
\]

O ponto que migra naturalmente para a Questão 21 é provar explicitamente que
o operador \(H\) reconstruído gera evolução unitária em tempo físico \(t\).

