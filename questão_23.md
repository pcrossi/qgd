# Questão 23 — Como a objeção de Wallstrom é resolvida?

## 1. Pergunta

A Questão 23 pergunta:

\[
\boxed{
\text{como a GDQ impede circulações contínuas arbitrárias na fase de Madelung?}
}
\]

O problema apontado em `23-0.md` é correto:

\[
\boxed{
\text{a soma de Poisson usada no texto original já soma setores rotulados por
inteiros.}
}
\]

Logo, ela não pode ser a origem da quantização. Ela pode verificar ou
representar a quantização depois que a estrutura global já selecionou
\(\mathbb Z\), mas não pode derivar \(\mathbb Z\) a partir de nada.

As perguntas obrigatórias são:

1. qual estrutura global torna a fase \(S^1\)-valued?
2. qual fibrado de linhas está envolvido?
3. como a integralidade da primeira classe de Chern surge?
4. por que circulações não inteiras não são estados admissíveis?
5. como estados com nós são tratados?

---

## 2. Resposta curta

A objeção de Wallstrom é resolvida se, na GDQ, a fase física não for tratada
como uma função real global arbitrária:

\[
S_R:M\to\mathbb R.
\]

Ela deve ser tratada como uma fase circular:

\[
\boxed{
e^{iS_R/\hbar}:M^\ast\to S^1,
}
\]

ou, de modo mais preciso, como uma seção de um fibrado de linha hermitiano:

\[
\boxed{
\Psi\in\Gamma(L),
\qquad
L\to M^\ast,
}
\]

onde:

\[
\boxed{
M^\ast=M\setminus Z_\rho,
\qquad
Z_\rho=\{x:\rho(x)=0\}.
}
\]

O conjunto nodal \(Z_\rho\) é removido porque em \(\rho=0\):

\[
\ln\rho
\]

diverge e o mapa Madelung deixa de ser regular.

A fase é:

\[
\boxed{
\chi=\frac{S_R}{\hbar}.
}
\]

Como \(\chi\) é coordenada angular de \(S^1\), a holonomia em qualquer ciclo
fechado \(C\subset M^\ast\) satisfaz:

\[
\boxed{
\frac1{2\pi}\oint_C d\chi\in\mathbb Z.
}
\]

Equivalente:

\[
\boxed{
\oint_C\nabla S_R\cdot dx=2\pi\hbar N=Nh,
\qquad N\in\mathbb Z.
}
\]

A integralidade não vem da soma de Poisson. Ela vem da existência de um fibrado
de linha unitário \(L\) com transições \(U(1)\) e primeira classe de Chern:

\[
\boxed{
c_1(L)=\left[\frac{F_A}{2\pi}\right]\in H^2(M^\ast,\mathbb Z).
}
\]

Circulações não inteiras não definem uma seção global admissível de \(L\).
Logo, não são estados físicos do Hilbert reconstruído.

---

## 3. O que é a objeção de Wallstrom

Na formulação Madelung/Nelson, escreve-se:

\[
\boxed{
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
}
\]

O campo de velocidade é:

\[
\boxed{
v=\frac1m\nabla S_R.
}
\]

As equações hidrodinâmicas locais permitem, formalmente:

\[
\boxed{
\oint_C m v\cdot dx
=
\oint_C\nabla S_R\cdot dx
=
\alpha h,
\qquad
\alpha\in\mathbb R.
}
\]

Mas a mecânica quântica exige:

\[
\boxed{
\oint_C\nabla S_R\cdot dx
=
Nh,
\qquad
N\in\mathbb Z.
}
\]

A objeção de Wallstrom é:

\[
\boxed{
\text{as equações locais de Madelung não impõem sozinhas }
\alpha\in\mathbb Z.
}
\]

Se a integralidade for adicionada manualmente, a teoria hidrodinâmica não
derivou completamente a mecânica quântica.

---

## 4. O erro da rota por soma de Poisson

O capítulo original usa uma expressão do tipo:

\[
\boxed{
\sum_{m\in\mathbb Z}e^{im\epsilon}
=
2\pi\sum_{n\in\mathbb Z}\delta(\epsilon-2\pi n).
}
\]

Essa identidade é verdadeira como distribuição.

Mas ela já pressupõe:

\[
\boxed{
m\in\mathbb Z.
}
\]

Logo, ela não explica por que o grupo de setores é \(\mathbb Z\). Ela apenas
mostra que, uma vez que a fase vive em \(S^1\), a análise harmônica no círculo
seleciona caracteres inteiros:

\[
\boxed{
e^{im\chi},
\qquad
m\in\mathbb Z.
}
\]

Portanto:

\[
\boxed{
\text{Poisson é consequência da topologia }S^1,\text{ não fundamento dela.}
}
\]

A resolução real deve vir antes: da estrutura global do estado.

---

## 5. Estrutura global correta: fase \(S^1\)-valued

Na GDQ, a fase física é:

\[
\boxed{
e^{iS_R/\hbar}.
}
\]

Portanto, a variável física não é \(S_R\in\mathbb R\) isoladamente, mas:

\[
\boxed{
\chi=\frac{S_R}{\hbar}\quad\text{módulo }2\pi.
}
\]

Assim:

\[
\boxed{
\chi:M^\ast\to\mathbb R/2\pi\mathbb Z\simeq S^1.
}
\]

Em cartas locais \(U_a\):

\[
\boxed{
\Psi_a=\sqrt{\rho}\,e^{i\chi_a}.
}
\]

Em interseções \(U_a\cap U_b\):

\[
\boxed{
\Psi_a=g_{ab}\Psi_b,
\qquad
g_{ab}:U_a\cap U_b\to U(1).
}
\]

Logo:

\[
\boxed{
g_{ab}=e^{i\lambda_{ab}},
}
\]

e:

\[
\boxed{
\chi_a-\chi_b=\lambda_{ab}\quad \text{módulo }2\pi.
}
\]

Essa é a estrutura que torna a fase \(S^1\)-valued.

---

## 6. Qual fibrado de linha está envolvido?

O objeto natural é um fibrado de linha complexo hermitiano:

\[
\boxed{
L\to M^\ast.
}
\]

O estado físico é uma seção:

\[
\boxed{
\Psi\in\Gamma(L).
}
\]

Localmente:

\[
\boxed{
\Psi_a=\sqrt\rho\,e^{i\chi_a}s_a,
}
\]

onde \(s_a\) é um referencial local de \(L\).

Em interseções:

\[
\boxed{
s_a=g_{ab}s_b,
\qquad
g_{ab}:U_a\cap U_b\to U(1).
}
\]

Em triplas interseções:

\[
\boxed{
g_{ab}g_{bc}g_{ca}=1.
}
\]

Esse cociclo \(U(1)\) define a classe topológica do fibrado.

A conexão unitária no fibrado é:

\[
\boxed{
A_a
}
\]

Com a convenção em que \(A_a\) é uma 1-forma real local, sua transição é:

\[
\boxed{
A_a=A_b-d\lambda_{ab},
\qquad
g_{ab}=e^{i\lambda_{ab}},
}
\]

até convenção de sinal para a derivada covariante.

O objeto global é a curvatura:

\[
\boxed{
F_A=dA_a,
}
\]

que é a mesma em todas as cartas.

---

## 7. Como surge a integralidade de \(c_1(L)\)

Para qualquer fibrado de linha complexo:

\[
\boxed{
c_1(L)=\left[\frac{F_A}{2\pi}\right]\in H^2(M^\ast,\mathbb Z).
}
\]

Isso significa que, para toda 2-superfície fechada \(\Sigma\subset M^\ast\):

\[
\boxed{
\frac1{2\pi}\int_\Sigma F_A\in\mathbb Z.
}
\]

Essa é uma propriedade topológica do fibrado, não uma condição dinâmica
adicionada depois.

Se um ciclo \(C\) contorna um defeito/nó, a holonomia é:

\[
\boxed{
\operatorname{Hol}_C(A)
=
\exp\left(i\oint_C A\right).
}
\]

Para uma seção global admissível, a fase após dar a volta deve voltar ao mesmo
ponto da fibra:

\[
\boxed{
\exp\left(i\oint_C d\chi\right)=1.
}
\]

Logo:

\[
\boxed{
\oint_C d\chi=2\pi N,
\qquad
N\in\mathbb Z.
}
\]

Multiplicando por \(\hbar\):

\[
\boxed{
\oint_C dS_R=2\pi\hbar N=Nh.
}
\]

Assim, a integralidade surge da topologia do fibrado de linha e da exigência de
seção global, não de uma restrição hidrodinâmica local arbitrária.

---

## 8. Por que circulações não inteiras não são estados admissíveis?

Suponha:

\[
\boxed{
\oint_C d\chi=2\pi\alpha,
\qquad
\alpha\notin\mathbb Z.
}
\]

Então:

\[
\boxed{
e^{i\oint_C d\chi}=e^{i2\pi\alpha}\ne1.
}
\]

Logo, após transportar a seção ao redor de \(C\), obtém-se:

\[
\boxed{
\Psi\mapsto e^{i2\pi\alpha}\Psi\ne\Psi.
}
\]

Isso significa que \(\Psi\) não é uma seção global monovalorada do fibrado
escolhido.

No Hilbert físico:

\[
\boxed{
\mathcal H_{\rm phys}
=
\overline{\mathcal D_+/(\mathcal N+\mathcal G)},
}
\]

os estados admissíveis devem ser seções globalmente compatíveis do setor
topológico. Um objeto com monodromia fracionária arbitrária:

1. não pertence ao domínio do operador de fase/momento naquele setor;
2. não satisfaz as transições \(U(1)\) do fibrado;
3. não tem produto interno global bem definido como estado daquele setor;
4. não preserva a condição de single-valuedness da amplitude física.

Portanto:

\[
\boxed{
\alpha\notin\mathbb Z
\quad\Rightarrow\quad
\text{não é estado físico admissível no setor }L.
}
\]

---

## 9. Como estados com nós são tratados

Nós são pontos ou subvariedades onde:

\[
\boxed{
\rho=0.
}
\]

Neles:

\[
\boxed{
\ln\rho
}
\]

diverge, e:

\[
\boxed{
f=-\ln\rho+iS_R/\hbar
}
\]

fica singular.

Portanto, o domínio regular não inclui os nós:

\[
\boxed{
M^\ast=M\setminus Z_\rho,
\qquad
Z_\rho=\{x:\rho(x)=0\}.
}
\]

O procedimento correto é:

1. remover \(Z_\rho\);
2. trabalhar em cartas de \(M^\ast\);
3. classificar ciclos não contráteis em torno de \(Z_\rho\);
4. impor holonomia inteira em torno desses ciclos;
5. controlar a energia de Fisher/Bohm perto dos nós;
6. permitir que nós sejam defeitos, vórtices, estômatos ou singularidades
   topológicas.

Assim:

\[
\boxed{
\text{nós não invalidam a teoria; eles definem a topologia do domínio onde a
fase vive.}
}
\]

Na verdade, são justamente os nós que permitem ciclos não triviais e
quantização de circulação.

---

## 10. Relação com spin meio-inteiro

A condição acima produz circulação inteira para seções de linha escalar:

\[
\boxed{
\oint_C dS_R=Nh.
}
\]

Setores spinoriais são diferentes. Neles o estado é seção de um fibrado
espinorial \(S\), possivelmente tensorizado por \(L\):

\[
\boxed{
\psi\in\Gamma(S\otimes L).
}
\]

Em um ciclo antiperiódico:

\[
\boxed{
\psi(\theta+2\pi)=-\psi(\theta).
}
\]

Logo os modos são:

\[
\boxed{
\psi_n(\theta)\propto e^{i(n+1/2)\theta}.
}
\]

e:

\[
\boxed{
\oint p_\theta\,d\theta=h\left(n+\frac12\right).
}
\]

Essa circulação meio-inteira não contradiz Wallstrom. Ela vem da estrutura
spin escolhida, não de uma circulação escalar arbitrária.

Como já foi fixado na Questão 2:

\[
\boxed{
\text{a soma de Poisson pode transferir a monodromia para o espectro, mas não
seleciona sozinha a estrutura spin.}
}
\]

---

## 11. Relação com a GDQ

Na GDQ:

\[
\boxed{
f=-\ln\rho+i\frac{S_R}{\hbar}.
}
\]

A parte real fixa a densidade:

\[
\boxed{
\rho=e^{-(f+\bar f)/2}.
}
\]

A parte imaginária fixa a fase:

\[
\boxed{
\chi=\operatorname{Im}f=\frac{S_R}{\hbar}.
}
\]

O ponto decisivo é:

\[
\boxed{
e^{i\chi}
}
\]

deve ser uma seção global admissível do fibrado de linha \(L\).

Logo, a quantização da circulação é condição de existência global do estado,
não postulado extra de Madelung.

---

## 12. Papel correto da dinâmica de Perelman

A topologia do fibrado fornece a seleção primária dos estados admissíveis.

A dinâmica de Perelman/Bismut pode então atuar como filtro de estabilidade:

1. setores admissíveis podem ou não possuir energia finita;
2. defeitos podem ou não ser estáveis;
3. configurações incompatíveis podem sair do domínio regular;
4. a ação pode penalizar singularidades de energia infinita;
5. o fluxo pode selecionar solitons estáveis.

Mas a dinâmica não deve ser usada como substituto da estrutura global:

\[
\boxed{
\text{primeiro vem o fibrado/setor admissível; depois vem estabilidade
dinâmica.}
}
\]

Assim, a soma de Poisson e os argumentos de dissipação do capítulo original
podem ser mantidos apenas como consequências ou filtros secundários.

---

## 13. Checklist da Questão 23

### 13.1 Qual estrutura global torna a fase \(S^1\)-valued?

\[
\boxed{
e^{iS_R/\hbar}:M^\ast\to S^1
}
\]

ou, mais precisamente:

\[
\boxed{
\Psi\in\Gamma(L).
}
\]

### 13.2 Qual fibrado de linhas está envolvido?

\[
\boxed{
L\to M^\ast
}
\]

fibrado de linha complexo hermitiano com grupo estrutural \(U(1)\).

### 13.3 Como a integralidade de \(c_1\) surge?

\[
\boxed{
c_1(L)=\left[\frac{F_A}{2\pi}\right]\in H^2(M^\ast,\mathbb Z).
}
\]

Logo:

\[
\boxed{
\frac1{2\pi}\int_\Sigma F_A\in\mathbb Z.
}
\]

### 13.4 Por que circulações não inteiras não são admissíveis?

Porque:

\[
\boxed{
\oint_Cd\chi=2\pi\alpha,\quad\alpha\notin\mathbb Z
}
\]

implica:

\[
\boxed{
e^{i\oint_Cd\chi}\ne1,
}
\]

logo a seção não fecha globalmente no setor escolhido.

### 13.5 Como estados com nós são tratados?

Remove-se o conjunto nodal:

\[
\boxed{
M^\ast=M\setminus Z_\rho.
}
\]

Os nós viram defeitos/topologia de bordo, e a fase é tratada por cartas e
holonomias em \(M^\ast\).

---

## 14. Resposta final da Questão 23

A objeção de Wallstrom é resolvida quando a fase da GDQ é tratada como dado
global de um fibrado:

\[
\boxed{
\Psi=\sqrt\rho\,e^{iS_R/\hbar}\in\Gamma(L),
\qquad
L\to M^\ast.
}
\]

Com:

\[
\boxed{
M^\ast=M\setminus\{\rho=0\}.
}
\]

A integralidade vem de:

\[
\boxed{
c_1(L)=\left[\frac{F_A}{2\pi}\right]\in H^2(M^\ast,\mathbb Z).
}
\]

E a circulação admissível satisfaz:

\[
\boxed{
\oint_C\nabla S_R\cdot dx=Nh,
\qquad
N\in\mathbb Z.
}
\]

Circulações não inteiras não são estados físicos porque não definem seção
global monovalorada do fibrado de linha do setor.

Portanto:

\[
\boxed{
\text{Questão 23 fechada estruturalmente.}
}
\]

A soma de Poisson do texto original deve ser rebaixada para consequência
analítica da topologia \(S^1\), não usada como origem da quantização.
