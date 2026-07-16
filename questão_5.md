# Questão 5 — Campos fundamentais da GDQ

## 1. Pergunta

A Questão 5 pergunta:

\[
\boxed{
\text{quais são os campos fundamentais da teoria?}
}
\]

O critério de fechamento é:

\[
\boxed{
\text{nenhum símbolo pode mudar de significado entre capítulos sem mapa explícito.}
}
\]

Portanto, esta questão não fecha ainda a renormalização, a \(\beta\)-função, o
polo de Landau ou a prova perturbativa completa. Ela fecha a ontologia mínima
dos campos: o que é fundamental, o que é estrutura de fundo, o que é derivado,
o que pertence à redução física e o que é apenas ferramenta auxiliar.

---

## 2. Base já fixada pelas questões anteriores

A variedade fundamental é:

\[
M=\mathbb R^4\times T^4,
\qquad
\dim_\mathbb C M=4,
\qquad
\dim_\mathbb R M=8.
\]

A ação oficial permanece:

\[
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
\]

com:

\[
n=4,
\qquad
z_\tau=\tau+i\nu_0t,
\qquad
\nu_0=\frac{\hbar}{2m_0},
\]

e:

\[
\mathcal U
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}.
\]

Esta ação não é substituída pela ação efetiva em \(N^4\). A ação efetiva é uma
redução física posterior.

---

## 3. Classificação ontológica

A teoria deve distinguir quatro níveis.

### 3.1 Campos fundamentais da ação oficial

São os objetos variados diretamente na ação oficial:

\[
\boxed{
g_{\mu\bar\nu},\quad f,\quad \bar f.
}
\]

A medida:

\[
\mathcal U[f,\bar f,z_\tau]
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}
\]

não é um campo independente: ela é funcional de \(f,\bar f\) e do parâmetro
complexo causal \(z_\tau\).

Se a métrica for parametrizada localmente por um potencial \(K\), então:

\[
g_{\mu\bar\nu}=\partial_\mu\partial_{\bar\nu}K
\]

pode ser usado como parametrização local auxiliar. Porém \(K\) não deve ser
tratado como campo fundamental global da teoria geral, pois a formulação final
é hermitiana torsional/Bismut, não Kähler estrita global.

### 3.2 Estruturas e parâmetros de fundo

São necessários para definir a teoria, mas não são campos dinâmicos da ação
oficial:

\[
\boxed{
M,\ J,\ \gamma,\ \tau,\ t,\ z_\tau,\ \Lambda_C,\ \nu_0.
}
\]

Aqui:

- \(M\) fixa topologia e dimensão;
- \(J\) fixa a estrutura complexa;
- \(\gamma\) é o contorno causal de Sudarshan;
- \(\tau\) é parâmetro de fluxo/escala;
- \(t\) é tempo físico;
- \(z_\tau=\tau+i\nu_0t\) combina fluxo e evolução causal;
- \(\Lambda_C\) e \(\nu_0\) são constantes de escala.

### 3.3 Campos derivados ou hidrodinâmicos

São definidos a partir de \(f\), ou aparecem na representação de Madelung:

\[
\boxed{
S_I,\ S_R,\ \rho,\ R,\ \Psi.
}
\]

O mapa obrigatório é:

\[
f
=
-\frac{S_I-iS_R}{\hbar}
=
-\frac{S_I}{\hbar}
+i\frac{S_R}{\hbar}.
\]

Logo:

\[
S_I=-\hbar\,\operatorname{Re}f,
\qquad
S_R=\hbar\,\operatorname{Im}f,
\]

\[
\rho
=
e^{S_I/\hbar}
=
e^{-(f+\bar f)/2},
\qquad
R=\sqrt{\rho},
\]

e:

\[
\Psi
=
R\,e^{iS_R/\hbar}
=
\sqrt{\rho}\,e^{iS_R/\hbar}.
\]

Assim, \(\rho,R,S_I,S_R,\Psi\) não devem ser tratados como novos campos
fundamentais independentes da ação oficial. Eles são variáveis equivalentes,
projeções ou representações efetivas.

### 3.4 Campos da redução física em \(N^4\)

Na redução física para o espaço-tempo \(N^4\), entram campos que não são a
ontologia mínima da ação oficial, mas são necessários para a teoria efetiva:

\[
\boxed{
X,\ h,\ B,\ A^a,\ \psi.
}
\]

Aqui:

- \(X:N\to M\) é a imersão/projeção física;
- \(h\) é a métrica lorentziana induzida/constitutiva em \(N\);
- \(B\) é o campo torsional físico de 3-forma;
- \(A^a\), \(a=1,\ldots,4\), são campos de calibre \(U(1)^4\);
- \(\psi\) são campos fermiônicos/spinoriais.

Estes campos pertencem à camada física/efetiva/perturbativa. Eles devem ser
compatíveis com a ação oficial, mas não substituem \(g\) e \(f\) como campos
fundamentais da ação geométrica.

### 3.5 Campos auxiliares não fundamentais

Fantasmas de Faddeev--Popov/BRST:

\[
c^a,\quad \bar c^a,\quad b^a
\]

não são campos fundamentais da GDQ.

Eles podem ser usados apenas como ferramenta opcional de auditoria, caso se
queira comparar a quantização da camada efetiva com a quantização covariante
padrão. Na formulação própria da GDQ, a prescrição causal de Sudarshan e a
projeção geométrica dos polos físicos devem dispensar esses campos como
ontologia.

\[
\boxed{
c^a,\bar c^a,b^a
\notin
\text{Campos fundamentais da GDQ}.
}
\]

---

## 4. Tabela final dos objetos

### 4.1 Geometria fundamental

| Símbolo | Domínio | Contradomínio | Unidade | Natureza | Status | Transformação | Dado inicial |
|---|---|---|---|---|---|---|---|
| \(M\) | não se aplica | variedade | coordenadas com escala de comprimento | real 8D com estrutura complexa | fundo/topologia fixa | difeomorfismos admissíveis | escolha \(M=\mathbb R^4\times T^4\) |
| \(J\) | \(TM\) | \(TM\) | adimensional | real, \(J^2=-1\) | estrutura fixa | \(J\mapsto \phi_*J\phi_*^{-1}\) | escolha compatível com \(M\) |
| \(g_{\mu\bar\nu}\) | \(M\) | formas hermitianas positivas | \(L^2\) se coordenadas adimensionais; adimensional se coordenadas carregam comprimento | hermitiano/riemanniano no bulk | fundamental dinâmico | tensor covariante sob difeomorfismos e mudanças complexas admissíveis | \(g|_\Sigma\), ou \(g_*\) para expansão |
| \(\omega_H\) | \(M\) | \(\Lambda^2T^*M\) | mesma unidade de \(g\) | real | derivada de \(g,J\) | 2-forma | \(\omega_H=g(J\cdot,\cdot)\) |
| \(K\) | carta local de \(M\) | \(\mathbb R\) | depende da convenção de \(g\) | real | parametrização local opcional | muda por transformações tipo potencial | não fundamental global |

Observação: \(\omega_H\) não implica que a teoria seja Kähler estrita. A base
geral é hermitiana torsional/Bismut. O caso \(d\omega_H=0\) é limite especial,
aproximação local ou gauge auxiliar.

### 4.2 Campo de Perelman e derivados

| Símbolo | Domínio | Contradomínio | Unidade | Natureza | Status | Transformação | Dado inicial |
|---|---|---|---|---|---|---|---|
| \(f\) | \(M\) com dependência em \(z_\tau\) | \(\mathbb C\) | adimensional | complexo | fundamental dinâmico | escalar sob coordenadas; fase em \(\operatorname{Im}f\) | \(f|_\Sigma\) |
| \(\bar f\) | mesmo de \(f\) | \(\mathbb C\) | adimensional | conjugado complexo | fundamental como par variacional | conjugado de \(f\) | \(\bar f|_\Sigma\) |
| \(S_I\) | mesmo de \(f\) | \(\mathbb R\) | ação | real | derivado | escalar | \(S_I=-\hbar\operatorname{Re}f\) |
| \(S_R\) | mesmo de \(f\) | \(\mathbb R/2\pi\hbar\mathbb Z\) quando fase | ação | real | derivado | \(S_R\mapsto S_R+\hbar\alpha\) sob fase | \(S_R=\hbar\operatorname{Im}f\) |
| \(\rho\) | \(M\), ou \(N\) após redução | \(\mathbb R_{\ge0}\) | depende da medida; \(\rho dV\) adimensional | real não negativa | derivada | densidade relativa à medida | \(\rho=e^{S_I/\hbar}\) |
| \(R\) | mesmo de \(\rho\) | \(\mathbb R_{\ge0}\) | raiz da unidade de \(\rho\) | real | derivado | escalar/densidade conforme normalização | \(R=\sqrt\rho\) |
| \(\Psi\) | \(N\) na EFT | \(\mathbb C\) ou fibrado complexo | definida pela ação efetiva | complexo | representação efetiva | \(\Psi\mapsto e^{iq\lambda}\Psi\) quando acoplado | \(\Psi=\sqrt\rho e^{iS_R/\hbar}\) |
| \(\mathcal U\) | \(M\times\gamma\) | densidade de medida | compatível com \(d^{2n}z\) | complexa via \(z_\tau\) | funcional derivado | densidade escalar | \(\mathcal U=\rho/(4\pi z_\tau)^n\) |

### 4.3 Parâmetros causais e de fluxo

| Símbolo | Domínio | Contradomínio | Unidade | Natureza | Status | Transformação | Dado inicial |
|---|---|---|---|---|---|---|---|
| \(t\) | evolução física em \(N\) | \(\mathbb R\) | tempo | real | parâmetro, não campo | reparametrizações compatíveis | escolha de tempo/folheação |
| \(\tau\) | fluxo/escala | \(\mathbb R_+\) | \(L^2\) | real | parâmetro, não campo | escala de fluxo | janela de fluxo |
| \(z_\tau\) | contorno \(\gamma\) | \(\mathbb C\) | \(L^2\) | complexo | parâmetro causal | prescrição de Sudarshan | \(z_\tau=\tau+i\nu_0t\) |
| \(\gamma\) | plano de \(z_\tau\) | caminho/contorno | não se aplica | geométrico-causal | prescrição, não campo | deformações que preservam polos físicos | escolha causal |
| \(\nu_0\) | constante | \(\mathbb R_+\) | \(L^2/T\) | real | parâmetro fixo | invariante | \(\nu_0=\hbar/(2m_0)\) |
| \(\Lambda_C\) | constante | \(\mathbb R_+\) | comprimento | real | escala fixa | invariante | escala da ação |

### 4.4 Redução física e campos efetivos em \(N^4\)

| Símbolo | Domínio | Contradomínio | Unidade | Natureza | Status | Transformação | Dado inicial |
|---|---|---|---|---|---|---|---|
| \(X\) | \(N\) | \(M\) | coordenadas de \(M\) | mapa geométrico | redução/projeção | \(X\mapsto \phi\circ X\) | imersão inicial |
| \(h\) | \(N\) | métricas lorentzianas | conforme convenção de coordenadas | real lorentziano | efetivo/constitutivo | tensor sob difeomorfismos de \(N\) | \(h|_\Sigma\) |
| \(B\) | \(N\) | \(\Lambda^3T^*N\) | compatível com \(B^2d^4x\) | real | campo torsional efetivo | 3-forma; se \(B=d\mathcal A+B_{\rm top}\), \(\mathcal A\mapsto\mathcal A+d\Lambda\) | \(B|_\Sigma\), fluxos topológicos |
| \(A^a\) | \(N\) | \(\Omega^1(N)\otimes\mathbb R^4\) | depende do acoplamento | real | calibre efetivo | \(A^a\mapsto A^a+d\lambda^a\) | \(A^a|_\Sigma\) e campo conjugado, módulo gauge |
| \(\psi\) | \(N\) | \(\Gamma(S\otimes E)\) | dimensão \(3/2\) em 4D natural | complexo/Grassmann na quantização | fermiônico efetivo | spinorial sob \(Spin(3,1)\), carregado sob \(U(1)^4\) | dados espinoriais em \(\Sigma\) |

### 4.5 Auxiliares de auditoria perturbativa

| Símbolo | Domínio | Contradomínio | Unidade | Natureza | Status | Transformação | Dado inicial |
|---|---|---|---|---|---|---|---|
| \(c^a\) | \(N\) | álgebra de gauge | depende do gauge fixing | Grassmann | auxiliar opcional | \(sA^a=d c^a\), \(sc^a=0\) em \(U(1)^4\) | não é estado físico |
| \(\bar c^a\) | \(N\) | álgebra de gauge | depende do gauge fixing | Grassmann | auxiliar opcional | \(s\bar c^a=b^a\) | não é estado físico |
| \(b^a\) | \(N\) | álgebra de gauge | depende do gauge fixing | bosônico | auxiliar opcional | \(sb^a=0\) | não é estado físico |

Estes três símbolos só devem aparecer se for feita uma comparação com
Faddeev--Popov/BRST. Eles não pertencem ao conjunto de campos fundamentais.

---

## 5. Resolução dos conflitos de notação

### 5.1 \(n=2,D=4\) versus \(n=4,D=8\)

A teoria fundamental usa:

\[
\boxed{
n=4,
\qquad
D=8.
}
\]

Trechos com:

\[
n=2,
\qquad
D=4
\]

só podem ser interpretados como setor físico reduzido \(N^4\), modelo antigo
ou aproximação local. Eles não definem o bulk oficial.

### 5.2 \(B\) ou \(H\)

Para evitar ambiguidade, a notação final deve usar:

\[
\boxed{
B\in\Omega^3(N)
}
\]

para a 3-forma torsional física.

Se for necessário escrever um potencial:

\[
B=d\mathcal A+B_{\rm top}.
\]

O símbolo \(H\) pode aparecer apenas como sinônimo local ou em comparação com
literatura externa. No documento final, \(B\) deve ser o símbolo principal.

### 5.3 Kähler estrito versus hermitiano torsional

A formulação geral não deve assumir globalmente:

\[
d\omega_H=0.
\]

A estrutura correta é hermitiana torsional/Bismut. O caso Kähler estrito entra
apenas como:

1. limite \(B=0\);
2. aproximação local;
3. parametrização auxiliar;
4. setor simplificado.

### 5.4 \(\Psi\) não substitui \(f\)

O campo:

\[
\Psi=\sqrt\rho e^{iS_R/\hbar}
\]

é útil na ação efetiva e na leitura quântica de Madelung. Porém, na ação
oficial, o campo fundamental é \(f\), não \(\Psi\).

O mapa correto é:

\[
f
\longrightarrow
(S_I,S_R)
\longrightarrow
(\rho,R,\Psi).
\]

Não se deve inverter esse mapa sem declarar que se está passando para a
representação efetiva.

### 5.5 Fantasmas não são necessários como ontologia

A afirmação:

\[
\boxed{
\text{fantasmas não são necessários na GDQ}
}
\]

é aceitável se entendida no sentido correto:

1. em QFT covariante padrão, fantasmas são ferramenta de gauge fixing;
2. na GDQ, a causalidade de Sudarshan e a geometria devem selecionar os modos
   físicos diretamente;
3. portanto, fantasmas não são campos fundamentais;
4. eles podem ser introduzidos apenas como camada opcional de auditoria para
   comparar com a formulação perturbativa padrão.

Logo, a resposta rigorosa é:

\[
\boxed{
\text{dispensáveis como ontologia; opcionais como ferramenta técnica.}
}
\]

---

## 6. Conjunto mínimo final

O conjunto mínimo de campos fundamentais da ação oficial é:

\[
\boxed{
\mathcal F_{\rm fund}
=
\{g_{\mu\bar\nu},\,f,\,\bar f\}.
}
\]

A medida é funcional derivado:

\[
\boxed{
\mathcal U
=
\mathcal U[f,\bar f,z_\tau].
}
\]

As estruturas de definição são:

\[
\boxed{
\mathcal B
=
\{M,J,\gamma,\tau,t,z_\tau,\Lambda_C,\nu_0\}.
}
\]

Os derivados hidrodinâmicos são:

\[
\boxed{
\mathcal D
=
\{S_I,S_R,\rho,R,\Psi\}.
}
\]

Os campos físicos efetivos são:

\[
\boxed{
\mathcal E
=
\{X,h,B,A^a,\psi\}.
}
\]

Os auxiliares opcionais de auditoria são:

\[
\boxed{
\mathcal A_{\rm aux}
=
\{c^a,\bar c^a,b^a\},
\qquad
\mathcal A_{\rm aux}
\cap
\mathcal F_{\rm fund}
=
\varnothing.
}
\]

---

## 7. Consequência lógica

Com este dicionário, a teoria fica livre da ambiguidade principal da Questão
5:

1. \(g\) não alterna entre métrica bulk e métrica física: \(g\) é bulk;
   \(h\) é física em \(N\).
2. \(f\) não alterna com \(\Psi\): \(f\) é fundamental; \(\Psi\) é
   representação efetiva.
3. \(S_I,S_R,\rho,R\) não são novos campos independentes: são componentes ou
   derivados de \(f\).
4. \(t,\tau,z_\tau,\gamma\) não são campos: são parâmetros/prescrições.
5. \(J\) é estrutura fixa atual, não campo dinâmico.
6. \(B\) é campo torsional efetivo em \(N\), com possível origem geométrica no
   bulk.
7. \(A^a\) e \(\psi\) pertencem à camada física/perturbativa, não à ontologia
   mínima da ação oficial.
8. Fantasmas BRST não pertencem à GDQ fundamental.

---

## 8. Status da Questão 5

\[
\boxed{
\text{Questão 5 fechada como dicionário formal dos campos da GDQ.}
}
\]

O que permanece para questões posteriores não é a definição dos campos, mas:

1. a derivação completa das \(\beta\)-funções geométricas;
2. a prova perturbativa de regularidade/ausência de divergências;
3. a demonstração explícita de que a prescrição causal de Sudarshan projeta
   todos os modos não físicos sem necessidade ontológica de fantasmas;
4. o cálculo dos acoplamentos efetivos e constantes observáveis a partir da
   geometria.

