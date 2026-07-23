# Questão 27 — Como surge a estatística fermiônica?

## 1. Pergunta

A Questão 27 pergunta:

\[
\boxed{
\text{por que setores de spin semi-inteiro obedecem estatística fermiônica na GDQ?}
}
\]

As perguntas obrigatórias de `27-0.md` são:

1. por que campos de spin semi-inteiro anticomutam?
2. a teoria é local?
3. a energia é positiva?
4. a teoria é lorentziana?
5. as hipóteses do teorema spin--estatística são satisfeitas?

O critério de resolução é:

\[
\boxed{
\text{mostrar que o setor spinorial efetivo satisfaz as hipóteses do teorema
spin--estatística.}
}
\]

---

## 2. Resposta curta

Sim, a estatística fermiônica é recuperada na GDQ no setor efetivo local,
lorentziano, spinorial e de energia positiva.

O resultado correto é:

\[
\boxed{
\text{campos de spin semi-inteiro devem ser quantizados por relações de
anticomutação.}
}
\]

Em tempo igual:

\[
\boxed{
\{\widehat\psi_\alpha(t,\mathbf x),
\widehat\psi_\beta^\dagger(t,\mathbf y)\}
=
\delta_{\alpha\beta}\delta^{(3)}(\mathbf x-\mathbf y),
}
\]

\[
\boxed{
\{\widehat\psi_\alpha(t,\mathbf x),
\widehat\psi_\beta(t,\mathbf y)\}
=0.
}
\]

Em separação espacial tipo-espaço:

\[
\boxed{
\{\widehat\psi_\alpha(x),\widehat\psi_\beta(y)\}=0,
\qquad
\{\widehat\psi_\alpha(x),\widehat{\bar\psi}_\beta(y)\}=0,
\qquad
(x-y)^2_h<0.
}
\]

Os observáveis físicos pares, construídos com número par de campos
fermiônicos, comutam em separação tipo-espaço:

\[
\boxed{
[A(O_1),B(O_2)]=0,
\qquad O_1\perp_h O_2.
}
\]

Portanto, a localidade física é preservada como localidade graduada.

---

## 3. O que já estava correto no texto original

O capítulo original `pt-br/11 - A Geometria do Teorema de Spin-Estatística e a
Exclusão de Pauli.md` contém uma ideia geométrica útil:

1. solítons de spin semi-inteiro carregam holonomia torsional;
2. a troca de duas excitações idênticas percorre um laço não trivial no espaço
   de configurações;
3. a fase acumulada pelo transporte paralelo é:

\[
\boxed{
\Delta S=\pi\hbar;
}
\]

4. então:

\[
\boxed{
\Psi(r_2,r_1)
=
e^{i\pi}\Psi(r_1,r_2)
=
-\Psi(r_1,r_2).
}
\]

Essa leitura é compatível com a GDQ e deve ser preservada como interpretação
geométrica:

\[
\boxed{
\text{a antissimetria aparece como holonomia }-1\text{ do setor spinorial.}
}
\]

Também está correta a consequência nodal:

\[
\Psi(r,r)=-\Psi(r,r)
\quad\Longrightarrow\quad
\boxed{
\Psi(r,r)=0.
}
\]

Assim, a barreira de Bohm perto do nó:

\[
Q
=
-\frac{\hbar^2}{2m}
\frac{\nabla^2R}{R}
\]

pode ser interpretada como manifestação geométrica da exclusão.

Mas isso, sozinho, ainda não é o teorema spin--estatística completo.

A holonomia explica o sinal de troca em um setor geométrico. O teorema
spin--estatística exige mais: localidade relativística, positividade de energia,
produto interno positivo e representação spinorial Lorentziana.

---

## 4. Por que campos de spin semi-inteiro anticomutam?

Pela Questão 26, o setor de spin \(1/2\) é descrito por seções de um fibrado
espinorial:

\[
\boxed{
\psi\in\Gamma(S\otimes E).
}
\]

O fibrado \(S\) é associado ao fibrado principal:

\[
\boxed{
P_{\rm Spin}(N)\to N.
}
\]

O grupo relevante é:

\[
\boxed{
\mathrm{Spin}^+(3,1)\simeq SL(2,\mathbb C),
}
\]

e o espinor de Dirac pertence à representação:

\[
\boxed{
S_D=S_L\oplus S_R
=
\left(\frac12,0\right)\oplus\left(0,\frac12\right).
}
\]

O operador efetivo é:

\[
\boxed{
\slashed D_{B,A}
=
\gamma^\mu
\left(
\nabla_\mu^{\rm LC}
+\frac18B_{\mu\nu\lambda}\gamma^{\nu\lambda}
-iq_aA_\mu^a
\right).
}
\]

O símbolo principal satisfaz:

\[
\boxed{
(\gamma^\mu k_\mu)^2=h^{\mu\nu}k_\mu k_\nu.
}
\]

Logo, o campo spinorial propaga no cone causal da métrica física \(h\).

No setor local relativístico, se um campo de spin semi-inteiro fosse quantizado
com comutadores bosônicos, uma das hipóteses físicas falharia: ou a localidade,
ou a positividade da energia, ou a positividade da norma.

Portanto, para manter simultaneamente:

1. causalidade local;
2. energia positiva;
3. produto interno positivo;
4. covariância Lorentziana;
5. representação spinorial de \(\mathrm{Spin}(3,1)\);

a quantização correta é por CAR:

\[
\boxed{
\{a(f),a^\dagger(g)\}
=
\langle f,g\rangle_{\mathcal H_1},
\qquad
\{a(f),a(g)\}=0,
\qquad
\{a^\dagger(f),a^\dagger(g)\}=0.
}
\]

O espaço de muitos corpos é a álgebra exterior:

\[
\boxed{
\mathcal F_-(\mathcal H_1)
=
\bigoplus_{n=0}^{\infty}\wedge^n\mathcal H_1.
}
\]

Portanto:

\[
\boxed{
\psi(x)\psi(y)=-\psi(y)\psi(x)
}
\]

para campos ímpares, e estados de duas partículas trocam de sinal:

\[
\boxed{
\Psi(x_1,x_2)=-\Psi(x_2,x_1).
}
\]

---

## 5. Exclusão de Pauli

Das relações CAR:

\[
\boxed{
\{a_i^\dagger,a_j^\dagger\}=0.
}
\]

Tomando \(i=j\):

\[
2(a_i^\dagger)^2=0.
\]

Logo:

\[
\boxed{
(a_i^\dagger)^2=0.
}
\]

Portanto:

\[
\boxed{
\text{não existem dois férmions idênticos no mesmo estado quântico.}
}
\]

Na linguagem de funções de onda:

\[
\Psi(x,x)=0.
\]

Na linguagem geométrica da GDQ, esse nó pode aparecer como uma barreira de
Bohm/torsão:

\[
R\to0
\quad\Longrightarrow\quad
Q\sim-\frac{\hbar^2}{2m}\frac{\nabla^2R}{R}
\text{ torna-se singular.}
\]

Assim:

\[
\boxed{
\text{Pauli é consequência algébrica das CAR; a barreira de Bohm é sua
manifestação geométrica.}
}
\]

Essa distinção é importante. A GDQ não deve substituir a prova algébrica por uma
imagem hidrodinâmica. A imagem hidrodinâmica explica por que a exclusão aparece
como repulsão efetiva no espaço geométrico.

---

## 6. A teoria é local?

Sim, no setor físico efetivo, desde que a localidade seja entendida como
localidade graduada.

Pela Questão 8, todos os campos efetivos compartilham o cone causal de \(h\).
Para escalares, gauge, torção e perturbações gravitacionais:

\[
\boxed{
h^{\mu\nu}k_\mu k_\nu=0.
}
\]

Para espinores:

\[
\boxed{
(\gamma^\mu k_\mu)^2=h^{\mu\nu}k_\mu k_\nu.
}
\]

Logo, a propagação frontal é controlada pela métrica física \(h\).

Para observáveis pares:

\[
\boxed{
O_1\perp_h O_2
\quad\Longrightarrow\quad
[\mathcal A_{\rm even}(O_1),\mathcal A_{\rm even}(O_2)]=0.
}
\]

Para campos fermiônicos ímpares:

\[
\boxed{
O_1\perp_h O_2
\quad\Longrightarrow\quad
\{\psi(O_1),\psi(O_2)\}=0.
}
\]

Essa é a forma correta de localidade em teorias com férmions.

Portanto:

\[
\boxed{
\text{a GDQ é local no setor observável e graduadamente local no setor
fermiônico.}
}
\]

---

## 7. A energia é positiva?

Pela Questão 21, o espaço físico \(\mathcal H_{\rm phys}\) é reconstruído por
Osterwalder--Schrader:

\[
\boxed{
\mathcal H_{\rm phys}
=
\overline{\mathcal D_+/(\mathcal N+\mathcal G)}.
}
\]

O semigrupo euclidiano define:

\[
\boxed{
T_E(a)=e^{-aH/\hbar},
\qquad a\ge0.
}
\]

e:

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

Sob reflexão positiva:

\[
\boxed{
H=H^\dagger,
\qquad
H\ge0.
}
\]

No setor fermiônico, a quantização CAR constrói a Fock fermiônica sobre o setor
de energia positiva:

\[
\boxed{
\mathcal F_-(\mathcal H_1^+)
=
\bigoplus_{n=0}^\infty\wedge^n\mathcal H_1^+.
}
\]

Assim, o Hamiltoniano de segunda quantização tem espectro positivo após a
escolha física de setor:

\[
\boxed{
d\Gamma(H_1)\ge0.
}
\]

Logo:

\[
\boxed{
\text{a hipótese de energia positiva é satisfeita condicionalmente à
reconstrução OS e à escolha do setor físico spinorial.}
}
\]

---

## 8. A teoria é lorentziana?

Sim, no setor físico efetivo.

A variedade fundamental da GDQ é Hermitiana/Riemanniana no bulk, mas a física
observável ocorre sobre a métrica Lorentziana constitutiva:

\[
\boxed{
h_{\mu\nu}
=
q_{\mu\nu}
-2\frac{u_\mu u_\nu}{q^{-1}(u,u)}.
}
\]

O setor fermiônico é formulado sobre \((N,h)\), não diretamente como um campo
spinorial livre no bulk euclidiano.

A álgebra de Clifford é:

\[
\boxed{
\{\gamma^\mu,\gamma^\nu\}=2h^{\mu\nu}.
}
\]

O grupo de simetria local é:

\[
\boxed{
\mathrm{Spin}^+(3,1).
}
\]

Portanto:

\[
\boxed{
\text{o teorema spin--estatística aplica-se ao setor efetivo Lorentziano
\((N,h)\).}
}
\]

---

## 9. As hipóteses do teorema spin--estatística são satisfeitas?

As hipóteses ficam satisfeitas no setor efetivo se as condições já fechadas nas
questões anteriores forem mantidas:

| Hipótese | Situação na GDQ |
|---|---|
| Espaço-tempo Lorentziano | Sim, via \((N,h)\). |
| Estrutura spin | Sim, Questão 26. |
| Campo de spin semi-inteiro | Sim, \(\psi\in\Gamma(S\otimes E)\). |
| Localidade/microcausalidade | Sim, como localidade graduada. |
| Energia positiva | Sim, via OS e setor físico \(H\ge0\). |
| Produto interno positivo | Sim, via reconstrução de \(\mathcal H_{\rm phys}\). |
| Covariância local | Sim, sob \(\mathrm{Spin}^+(3,1)\). |
| Cone causal comum | Sim, símbolo principal determinado por \(h\). |

Logo:

\[
\boxed{
\text{sim, as hipóteses do teorema spin--estatística são satisfeitas no setor
spinorial efetivo da GDQ.}
}
\]

Com isso:

\[
\boxed{
\text{spin semi-inteiro}\quad\Longrightarrow\quad\text{estatística
fermiônica}.
}
\]

---

## 10. Relação com a holonomia de Cartan

A GDQ possui uma interpretação geométrica adicional:

\[
\boxed{
\text{a troca de dois férmions corresponde a uma holonomia }-1.
}
\]

Em termos de fase:

\[
\boxed{
\operatorname{Hol}_\gamma
=
\exp\left(\frac{i}{\hbar}\oint_\gamma dS_R\right)
=-1.
}
\]

Equivalentemente:

\[
\boxed{
\oint_\gamma dS_R=(2k+1)\pi\hbar.
}
\]

Essa holonomia é compatível com:

1. a estrutura spinorial de \(S\);
2. a transformação \(2\pi\mapsto -1\);
3. a transformação \(4\pi\mapsto +1\);
4. a antissimetria de troca;
5. a leitura hidrodinâmica por vorticidade/torsão de Cartan.

Mas a ordem lógica correta é:

\[
\boxed{
\text{estrutura spinorial + localidade + energia positiva}
\Rightarrow
\text{CAR}
\Rightarrow
\text{Pauli}.
}
\]

A holonomia de Cartan fornece a interpretação geométrica dessa álgebra:

\[
\boxed{
\text{CAR é a forma algébrica; holonomia }-1\text{ é a forma geométrica.}
}
\]

---

## 11. O que não deve ser afirmado

Não se deve afirmar que:

\[
\boxed{
\text{circulação clássica meio-inteira, sozinha, prova anticomutação.}
}
\]

Ela não prova.

Circulação ou holonomia podem mostrar uma fase de troca em um setor
topológico, mas não constroem automaticamente:

1. a álgebra CAR local;
2. a positividade da energia;
3. o espaço de Fock fermiônico;
4. a microcausalidade graduada;
5. o produto interno positivo.

Também não se deve transformar a GDQ no Modelo Padrão. Aqui foi usado apenas o
setor spinorial efetivo necessário para recuperar o teorema spin--estatística:

\[
\boxed{
\text{GDQ recupera a estrutura fermiônica efetiva; não postula o Modelo
Padrão inteiro.}
}
\]

---

## 12. Resposta final da Questão 27

A estatística fermiônica surge porque o setor de spin semi-inteiro da GDQ é um
setor spinorial local, Lorentziano, de energia positiva e produto interno
positivo.

Nesse setor, o teorema spin--estatística exige relações de anticomutação:

\[
\boxed{
\{\widehat\psi_\alpha(t,\mathbf x),
\widehat\psi_\beta^\dagger(t,\mathbf y)\}
=
\delta_{\alpha\beta}\delta^{(3)}(\mathbf x-\mathbf y),
}
\]

\[
\boxed{
\{\widehat\psi_\alpha,\widehat\psi_\beta\}=0.
}
\]

Consequentemente:

\[
\boxed{
(a_i^\dagger)^2=0,
}
\]

e o princípio de exclusão de Pauli segue imediatamente.

A contribuição específica da GDQ é interpretar o sinal fermiônico como
holonomia geométrica:

\[
\boxed{
\operatorname{Hol}_\gamma=-1,
}
\]

ou:

\[
\boxed{
\Psi(r_2,r_1)=-\Psi(r_1,r_2).
}
\]

Portanto:

\[
\boxed{
\text{Questão 27 fechada estruturalmente, condicionada ao setor efetivo
spinorial local reconstruído nas Questões 20, 21 e 26.}
}
\]

