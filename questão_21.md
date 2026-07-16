# Questão 21 — A evolução é unitária?

## 1. Pergunta

A Questão 21 pergunta:

\[
\boxed{
\text{a evolução física da GDQ preserva o produto interno em tempo físico }t?
}
\]

As perguntas obrigatórias de `21-0.md` são:

1. qual operador gera evolução em \(t\)?
2. ele é autoadjunto?
3. a norma é preservada?
4. como uma dinâmica dissipativa em \(\tau\) se relaciona à evolução unitária
   em \(t\)?
5. estados instáveis são descritos por Hamiltoniano efetivo ou teoria aberta?

O critério de resolução é:

\[
\boxed{
\text{provar a conservação do produto interno em tempo físico.}
}
\]

---

## 2. Resposta curta

Sim, a evolução física em \(t\) é unitária desde que o Hamiltoniano reconstruído
no espaço físico seja autoadjunto:

\[
\boxed{
H=H^\dagger.
}
\]

O operador de evolução é:

\[
\boxed{
U(t)=e^{-itH/\hbar}.
}
\]

Pelo teorema de Stone:

\[
\boxed{
U(t)^\dagger U(t)=U(t)U(t)^\dagger=I.
}
\]

Logo:

\[
\boxed{
\langle U(t)\Psi,U(t)\Phi\rangle
=
\langle\Psi,\Phi\rangle.
}
\]

Em particular:

\[
\boxed{
\|\Psi(t)\|^2=\|\Psi(0)\|^2.
}
\]

Portanto:

\[
\boxed{
\text{a evolução em }t\text{ é unitária no setor físico fechado.}
}
\]

---

## 3. Qual operador gera evolução em \(t\)?

Pela Questão 20, o espaço físico é:

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

A evolução física em \(t\) é gerada por um Hamiltoniano:

\[
\boxed{
H:D(H)\subset\mathcal H_{\rm phys}\to\mathcal H_{\rm phys}.
}
\]

Ele é obtido pela reconstrução Osterwalder--Schrader a partir do semigrupo
euclidiano:

\[
\boxed{
T_E(a)=e^{-aH/\hbar},
\qquad a\ge0.
}
\]

Equivalentemente:

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

Esse \(H\) é o gerador das translações no tempo físico \(t\) associado à métrica
lorentziana efetiva \(h\), não o gerador do fluxo geométrico em \(\tau\).

---

## 4. Ele é autoadjunto?

Sim, sob as hipóteses OS já adotadas na Questão 7:

1. invariância euclidiana/local apropriada;
2. simetria;
3. reflexão positiva;
4. regularidade;
5. propriedade de cluster;
6. domínio denso.

O semigrupo euclidiano \(T_E(a)\) é um semigrupo simétrico positivo de
contrações:

\[
\boxed{
T_E(a+b)=T_E(a)T_E(b),
\qquad
\|T_E(a)\|\le1.
}
\]

Pela reconstrução:

\[
\boxed{
T_E(a)=e^{-aH/\hbar}.
}
\]

Da simetria e positividade do semigrupo segue:

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

Esse é o ponto técnico central: a unitariedade não vem apenas do contorno
\(\gamma\), nem apenas da prescrição de Sudarshan. Ela vem da existência de
um \(H\) autoadjunto no espaço físico reconstruído.

---

## 5. Prova direta de conservação do produto interno

Se:

\[
\boxed{
i\hbar\frac{d}{dt}\Psi(t)=H\Psi(t),
}
\]

com:

\[
\boxed{
H=H^\dagger,
}
\]

então:

\[
\frac{d}{dt}\langle\Psi(t),\Phi(t)\rangle
=
\left\langle\frac{d\Psi}{dt},\Phi\right\rangle
+
\left\langle\Psi,\frac{d\Phi}{dt}\right\rangle.
\]

Como:

\[
\frac{d\Psi}{dt}
=
-\frac{i}{\hbar}H\Psi,
\qquad
\frac{d\Phi}{dt}
=
-\frac{i}{\hbar}H\Phi,
\]

temos:

\[
\frac{d}{dt}\langle\Psi,\Phi\rangle
=
\frac{i}{\hbar}\langle H\Psi,\Phi\rangle
-
\frac{i}{\hbar}\langle\Psi,H\Phi\rangle.
\]

Usando \(H=H^\dagger\):

\[
\boxed{
\langle H\Psi,\Phi\rangle
=
\langle\Psi,H\Phi\rangle.
}
\]

Logo:

\[
\boxed{
\frac{d}{dt}\langle\Psi(t),\Phi(t)\rangle=0.
}
\]

Em particular, tomando \(\Phi=\Psi\):

\[
\boxed{
\frac{d}{dt}\|\Psi(t)\|^2=0.
}
\]

Assim:

\[
\boxed{
\|\Psi(t)\|^2=\|\Psi(0)\|^2.
}
\]

Essa é a prova explícita pedida por `21-0.md`.

---

## 6. Forma exponencial da prova

Como:

\[
\boxed{
U(t)=e^{-itH/\hbar},
}
\]

temos:

\[
\boxed{
U(t)^\dagger
=
e^{+itH/\hbar}.
}
\]

Então:

\[
\boxed{
U(t)^\dagger U(t)
=
e^{+itH/\hbar}e^{-itH/\hbar}
=I.
}
\]

Portanto:

\[
\boxed{
\langle U(t)\Psi,U(t)\Phi\rangle
=
\langle\Psi,U(t)^\dagger U(t)\Phi\rangle
=
\langle\Psi,\Phi\rangle.
}
\]

Essa é a formulação global da mesma conservação.

---

## 7. Relação entre \(\tau\) e \(t\)

Na GDQ:

\[
\boxed{
z_\tau=\tau+i\nu_0 t,
\qquad
\nu_0=\frac{\hbar}{2m_0}.
}
\]

A variável \(\tau\) tem dimensão difusiva/de área:

\[
\boxed{
[\tau]=L^2.
}
\]

O tempo físico entra como:

\[
\boxed{
\nu_0t
}
\]

também com dimensão \(L^2\). Assim, \(z_\tau\) combina escala difusiva e tempo
físico dentro da estrutura complexa, mas isso não significa que \(\tau\) e
\(t\) sejam o mesmo parâmetro dinâmico.

O fluxo em \(\tau\) é:

\[
\boxed{
\text{geométrico, difusivo, renormalizacional e geralmente contrativo.}
}
\]

A evolução em \(t\) é:

\[
\boxed{
\text{unitária no espaço físico reconstruído.}
}
\]

Portanto:

\[
\boxed{
\tau\text{ organiza escala/regularização/fluxo;}
\qquad
t\text{ organiza evolução física unitária.}
}
\]

---

## 8. Como uma dinâmica dissipativa em \(\tau\) pode coexistir com
unitariedade em \(t\)?

A coexistência é possível porque as duas dinâmicas vivem em papéis diferentes.

O semigrupo euclidiano:

\[
\boxed{
T_E(a)=e^{-aH/\hbar},
\qquad a\ge0,
}
\]

é contrativo:

\[
\boxed{
\|T_E(a)\|\le1.
}
\]

Ele não é uma evolução unitária em tempo físico. Ele é a evolução
euclidiana/de escala usada para reconstruir \(H\).

Depois da reconstrução:

\[
\boxed{
a\mapsto it
}
\]

produz:

\[
\boxed{
U(t)=e^{-itH/\hbar}.
}
\]

Como \(H\) é autoadjunto, \(U(t)\) é unitário.

Assim:

\[
\boxed{
\text{contração em escala euclidiana}
\not\Rightarrow
\text{perda de norma em tempo físico.}
}
\]

Em linguagem GDQ:

1. \(\tau\) suaviza geometria, seleciona setores estáveis e implementa fluxo;
2. \(t\) descreve propagação física sobre a folha lorentziana;
3. a estrutura complexa conecta as duas projeções;
4. a norma física é definida em \(\mathcal H_{\rm phys}\), não na trajetória
   bruta do fluxo geométrico.

---

## 9. Papel correto de Sudarshan

A prescrição de Sudarshan permanece relevante:

\[
\boxed{
G_{\rm sym}
=
\frac12(G_{\rm ret}+G_{\rm adv}).
}
\]

Ela organiza:

1. fechamento de contorno;
2. seleção de polos físicos;
3. cancelamento de termos exatos de bordo;
4. consistência avançado-retardada;
5. restrições globais de fase/holonomia.

Mas:

\[
\boxed{
\text{Sudarshan sozinho não prova unitariedade.}
}
\]

A unitariedade operacional exige:

\[
\boxed{
\mathcal H_{\rm phys}
\text{ de norma positiva}
\quad\text{e}\quad
H=H^\dagger.
}
\]

Logo, a função de \(\gamma\) e da prescrição de Sudarshan é compatibilizar a
causalidade complexa e selecionar setores físicos; a conservação da norma vem
do Hamiltoniano autoadjunto no Hilbert físico.

---

## 10. Estados instáveis

Estados instáveis não devem ser descritos como violação da unitariedade
fundamental.

Eles aparecem quando se projeta o sistema fechado em um subespaço efetivo.

Se:

\[
\boxed{
\mathcal H_{\rm total}
=
\mathcal H_P\oplus\mathcal H_Q,
}
\]

onde \(P\) é o setor observado e \(Q\) é o contínuo/vácuo/ambiente, então a
evolução total é:

\[
\boxed{
U_{\rm total}(t)=e^{-itH_{\rm total}/\hbar},
\qquad
H_{\rm total}=H_{\rm total}^\dagger.
}
\]

Logo:

\[
\boxed{
U_{\rm total}(t)^\dagger U_{\rm total}(t)=I.
}
\]

Mas, no subespaço projetado \(P\), pode surgir um Hamiltoniano efetivo:

\[
\boxed{
H_{\rm eff}
=
H_{PP}
-
\frac{i}{2}\Gamma
+\Delta H,
}
\]

com:

\[
\boxed{
\Gamma\ge0.
}
\]

Esse operador não é autoadjunto:

\[
\boxed{
H_{\rm eff}\ne H_{\rm eff}^\dagger.
}
\]

Então a norma projetada pode decair:

\[
\boxed{
\|P\Psi(t)\|^2<\|P\Psi(0)\|^2.
}
\]

Mas isso significa apenas que probabilidade saiu do setor \(P\) para o setor
\(Q\), não que a teoria fechada perdeu unitariedade.

---

## 11. Estados instáveis como teoria aberta

Para subsistemas, a descrição correta é por matriz densidade:

\[
\boxed{
\rho_P(t)=\operatorname{Tr}_Q\rho_{\rm total}(t).
}
\]

A evolução total é unitária:

\[
\boxed{
\rho_{\rm total}(t)
=
U_{\rm total}(t)\rho_{\rm total}(0)U_{\rm total}(t)^\dagger.
}
\]

Mas a evolução reduzida pode ser dissipativa:

\[
\boxed{
\frac{d\rho_P}{dt}
=
-\frac{i}{\hbar}[H_P,\rho_P]
+
\sum_\alpha
\left(
L_\alpha\rho_P L_\alpha^\dagger
-
\frac12\{L_\alpha^\dagger L_\alpha,\rho_P\}
\right).
}
\]

Essa é a forma de teoria aberta Markoviana. Ela preserva o traço do estado
reduzido se todos os canais efetivos do subsistema forem incluídos:

\[
\boxed{
\operatorname{Tr}\rho_P(t)=1.
}
\]

Quando se observa apenas a amplitude de sobrevivência de uma ressonância, ou
apenas um canal parcial, essa probabilidade pode decair. Isso é uma perda
efetiva por projeção/coarse-graining, não quebra fundamental de unitariedade.

---

## 12. Relação com NESS e irreversibilidade

O capítulo `pt-br/21 - O Problema dos NESS.md` é útil aqui, mas deve ser lido
com cuidado.

Ele descreve a tensão entre:

\[
\boxed{
\text{estabilidade unitária microscópica}
}
\]

e:

\[
\boxed{
\text{irreversibilidade macroscópica após coarse-graining.}
}
\]

Essa distinção é correta.

No nível microscópico fechado:

\[
\boxed{
\frac{d}{dt}\|\Psi(t)\|^2=0.
}
\]

No nível macroscópico projetado:

\[
\boxed{
\frac{dS_{\rm macro}}{dt}\ge0
}
\]

pode emergir por perda de informação fina, memória, espalhamento para o
contínuo e projeção sobre variáveis coletivas.

Portanto:

\[
\boxed{
\text{irreversibilidade efetiva não contradiz unitariedade fundamental.}
}
\]

---

## 13. Forma correta da afirmação para a GDQ

A afirmação defensável é:

\[
\boxed{
\text{A GDQ é unitária no setor físico fechado se a reconstrução OS fornece
um Hamiltoniano autoadjunto }H\text{ em }\mathcal H_{\rm phys}.
}
\]

E:

\[
\boxed{
\text{dissipação em }\tau,\text{ NESS, Fano, coarse-graining e decaimentos
são descrições efetivas/projetadas.}
}
\]

Não se deve afirmar que qualquer Hamiltoniano efetivo não hermitiano seja
fundamental.

Também não se deve afirmar que a monotonicidade de Perelman por si só prova
unitariedade. Ela fornece estrutura de fluxo e seleção/estabilidade geométrica,
mas a unitariedade física exige autoadjunticidade de \(H\).

---

## 14. Checklist da Questão 21

### 14.1 Qual operador gera evolução em \(t\)?

\[
\boxed{
H
=
-\hbar
\left.
\frac{d}{da}T_E(a)
\right|_{a=0^+}
}
\]

e:

\[
\boxed{
U(t)=e^{-itH/\hbar}.
}
\]

### 14.2 Ele é autoadjunto?

Sim, sob reconstrução OS/reflexão positiva:

\[
\boxed{
H=H^\dagger.
}
\]

### 14.3 A norma é preservada?

Sim:

\[
\boxed{
\frac{d}{dt}\|\Psi(t)\|^2=0,
\qquad
\|\Psi(t)\|=\|\Psi(0)\|.
}
\]

### 14.4 Como a dissipação em \(\tau\) se relaciona à unitariedade em \(t\)?

\[
\boxed{
e^{-aH/\hbar}
\text{ é semigrupo euclidiano contrativo;}
\qquad
e^{-itH/\hbar}
\text{ é grupo unitário lorentziano.}
}
\]

### 14.5 Estados instáveis são Hamiltoniano efetivo ou teoria aberta?

Ambos são descrições efetivas equivalentes por projeção:

\[
\boxed{
H_{\rm eff}=H_{PP}+\Delta H-\frac{i}{2}\Gamma
}
\]

ou:

\[
\boxed{
\rho_P(t)=\operatorname{Tr}_Q\rho_{\rm total}(t).
}
\]

A teoria total fechada permanece unitária.

---

## 15. Resposta final da Questão 21

\[
\boxed{
\text{Sim: a evolução física em }t\text{ é unitária no setor físico fechado.}
}
\]

O gerador é:

\[
\boxed{
H=H^\dagger
}
\]

no espaço:

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

A evolução é:

\[
\boxed{
U(t)=e^{-itH/\hbar}.
}
\]

E preserva produto interno:

\[
\boxed{
\langle U(t)\Psi,U(t)\Phi\rangle
=
\langle\Psi,\Phi\rangle.
}
\]

Em particular:

\[
\boxed{
\|\Psi(t)\|^2=\|\Psi(0)\|^2.
}
\]

A dinâmica dissipativa em \(\tau\) é fluxo geométrico/renormalizacional e não
é a evolução unitária física. Estados instáveis, NESS, decaimentos e
irreversibilidade são descritos por Hamiltonianos efetivos ou teoria aberta
após projeção/coarse-graining.

Logo:

\[
\boxed{
\text{Questão 21 fechada estruturalmente, condicionada à verificação OS
setorial já explicitada nas Questões 7 e 20.}
}
\]
