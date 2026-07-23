# Questão 12 — A ação produz o fluxo métrico?

## 1. Pergunta

A Questão 12 pergunta:

\[
\boxed{
\text{a ação produz a equação métrica/fluxo métrico da GDQ?}
}
\]

As perguntas obrigatórias de `12-0.md` são:

1. a equação métrica é elíptica, parabólica ou hiperbólica?
2. ela descreve fluxo auxiliar ou evolução física?
3. qual tensor energia-momento é obtido?
4. como aparece o termo de torção?
5. a equação satisfaz identidade de Bianchi?
6. há conservação covariante?

O critério de fechamento é:

\[
\boxed{
\text{fazer a variação completa em }g^{\mu\bar\nu},
\text{ sem inserir o tensor pretendido por analogia.}
}
\]

---

## 2. Resposta curta

Sim. A ação produz a equação métrica quando se varia
\(g^{\mu\bar\nu}\), mantendo \(f,\bar f\) fixos nessa variação.

A equação métrica local é a equação de Euler--Lagrange:

\[
\boxed{
\frac{\delta S_{\rm phys}}{\delta g^{\mu\bar\nu}}=0.
}
\]

Ela é uma equação geométrica de segunda ordem no bulk riemanniano. Após fixação
de difeomorfismo, seu setor estacionário é elíptico.

O fluxo associado de Ricci--Perelman é parabólico em \(\tau\):

\[
\boxed{
\partial_\tau g_{\mu\bar\nu}
=
-2\,\mathcal E_{\mu\bar\nu}^{\rm geom}
}
\]

em calibre de DeTurck/Perelman apropriado.

Esse fluxo em \(\tau\) é auxiliar, geométrico, difusivo e de escala. Ele não é
a evolução física causal. A evolução física causal pertence à camada
lorentziana efetiva \(N^4\), com métrica constitutiva \(h\), tempo físico
\(t\), reconstrução OS e prescrição causal de Sudarshan.

---

## 3. Ação usada

A ação oficial preservada é:

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

Com:

\[
\boxed{
\mathcal U
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}.
}
\]

Na variação métrica:

\[
\boxed{
\delta_g f=0,
\qquad
\delta_g\bar f=0,
\qquad
\delta_g\mathcal U=0.
}
\]

Isto é importante: \(\mathcal U\) depende de \(f,\bar f,z_\tau\), não é
multiplicador independente e não é variada como campo métrico.

Defina:

\[
\boxed{
X
=
g^{\alpha\bar\beta}
\partial_\alpha f
\partial_{\bar\beta}\bar f,
\qquad
\Phi
=
\frac{f+\bar f}{2}.
}
\]

Então o integrando local é:

\[
\boxed{
\mathcal L
=
\frac{\hbar}{\Lambda_C^2}
\mathcal U
\left[
\tau(\mathcal R+X)+\Phi-n
\right]\sqrt g.
}
\]

O fator global \(\hbar/\Lambda_C^2\) e a integral em \(\gamma\) multiplicam a
equação, mas não alteram o coeficiente local da variação métrica.

---

## 4. Variações métricas básicas

Usando variação em relação à métrica inversa:

\[
\delta g^{\mu\bar\nu}
\]

temos:

\[
\boxed{
\delta\sqrt g
=
-\frac12\sqrt g\,
g_{\mu\bar\nu}\delta g^{\mu\bar\nu}.
}
\]

O termo cinético de \(f\) satisfaz:

\[
\boxed{
\delta X
=
\partial_\mu f
\partial_{\bar\nu}\bar f\,
\delta g^{\mu\bar\nu}.
}
\]

O termo escalar \(\Phi-n\) não depende explicitamente de \(g^{\mu\bar\nu}\),
então sua variação métrica vem apenas de \(\sqrt g\).

Para o termo de curvatura ponderado por \(\mathcal U\):

\[
\int \sqrt g\,\mathcal U\,\mathcal R,
\]

a variação padrão dá:

\[
\boxed{
\delta
\int\sqrt g\,\mathcal U\,\mathcal R
=
\int\sqrt g\,
\left[
\mathcal U\,G_{\mu\bar\nu}
+
\left(
g_{\mu\bar\nu}\Delta
-\nabla_\mu\nabla_{\bar\nu}
\right)\mathcal U
\right]
\delta g^{\mu\bar\nu}
+B_g.
}
\]

Aqui:

\[
\boxed{
G_{\mu\bar\nu}
=
\mathcal R_{\mu\bar\nu}
-\frac12g_{\mu\bar\nu}\mathcal R.
}
\]

O termo \(B_g\) é termo de bordo. Ele desaparece se:

1. \(M\) é sem bordo físico;
2. as variações têm suporte compacto;
3. há decaimento adequado no setor \(\mathbb R^4\);
4. os termos exatos são cancelados pelo contorno \(\gamma\);
5. ou é adicionado o termo hermitiano de bordo \(S_{\partial M}^{\rm herm}\).

---

## 5. Variação completa em \(g^{\mu\bar\nu}\)

A variação local da ação física é:

\[
\delta_g S_{\rm phys}
=
\operatorname{Re}
\int_\gamma
\int_M
\frac{\hbar}{\Lambda_C^2}
\sqrt g\,
\mathcal E_{\mu\bar\nu}
\delta g^{\mu\bar\nu}
d^{2n}z
\frac{d\tau}{\tau}.
\]

O tensor variacional métrico é:

\[
\boxed{
\mathcal E_{\mu\bar\nu}
=
\tau
\left[
\mathcal U\,G_{\mu\bar\nu}
+
\left(
g_{\mu\bar\nu}\Delta
-\nabla_\mu\nabla_{\bar\nu}
\right)\mathcal U
\right]
+
\tau\mathcal U
\left[
\partial_\mu f\partial_{\bar\nu}\bar f
-\frac12g_{\mu\bar\nu}X
\right]
-\frac12
\mathcal U
g_{\mu\bar\nu}
(\Phi-n).
}
\]

Portanto a equação métrica derivada da ação é:

\[
\boxed{
\mathcal E_{\mu\bar\nu}=0.
}
\]

Esta é a resposta variacional mínima exigida.

Nada foi inserido por analogia: cada termo vem de uma das três variações:

1. \(\delta(\sqrt g\,\mathcal U\mathcal R)\);
2. \(\delta(\sqrt g\,\mathcal U X)\);
3. \(\delta(\sqrt g\,\mathcal U(\Phi-n))\).

---

## 6. Tensor energia-momento obtido

O tensor energia-momento não deve ser postulado. Ele é definido
variacionalmente.

Separe:

\[
S_{\rm phys}
=
S_{\rm geom}+S_f+S_\Phi.
\]

Com:

\[
S_f
=
\operatorname{Re}
\int_\gamma
\int_M
\frac{\hbar}{\Lambda_C^2}
\tau\mathcal U
X\sqrt g\,
d^{2n}z
\frac{d\tau}{\tau},
\]

e:

\[
S_\Phi
=
\operatorname{Re}
\int_\gamma
\int_M
\frac{\hbar}{\Lambda_C^2}
\mathcal U(\Phi-n)\sqrt g\,
d^{2n}z
\frac{d\tau}{\tau}.
\]

Define-se:

\[
\boxed{
T_{\mu\bar\nu}^{(f)}
:=
-\frac{2}{\sqrt g}
\frac{\delta S_f}{\delta g^{\mu\bar\nu}}
}
\]

e:

\[
\boxed{
T_{\mu\bar\nu}^{(\Phi)}
:=
-\frac{2}{\sqrt g}
\frac{\delta S_\Phi}{\delta g^{\mu\bar\nu}}.
}
\]

Aplicando a variação:

\[
\boxed{
T_{\mu\bar\nu}^{(f)}
=
-2
\frac{\hbar}{\Lambda_C^2}
\tau\mathcal U
\left[
\partial_\mu f\partial_{\bar\nu}\bar f
-\frac12g_{\mu\bar\nu}X
\right].
}
\]

E:

\[
\boxed{
T_{\mu\bar\nu}^{(\Phi)}
=
\frac{\hbar}{\Lambda_C^2}
\mathcal U
g_{\mu\bar\nu}
(\Phi-n).
}
\]

Se a convenção adotada para a ação efetiva de matéria trocar o sinal global do
termo cinético, o sinal de \(T^{(f)}\) troca junto. O ponto invariantemente
correto é a definição variacional:

\[
\boxed{
T_{\mu\bar\nu}
=
-\frac{2}{\sqrt g}
\frac{\delta S_{\rm mat}}{\delta g^{\mu\bar\nu}}.
}
\]

Assim, a equação métrica também pode ser escrita como:

\[
\boxed{
\tau
\left[
\mathcal U\,G_{\mu\bar\nu}
+
\left(
g_{\mu\bar\nu}\Delta
-\nabla_\mu\nabla_{\bar\nu}
\right)\mathcal U
\right]
=
\frac{\Lambda_C^2}{2\hbar}
\left(
T_{\mu\bar\nu}^{(f)}
+T_{\mu\bar\nu}^{(\Phi)}
\right).
}
\]

Essa forma é útil porque mostra que o lado direito foi obtido por variação, não
por analogia.

---

## 7. Relação com Perelman

Como:

\[
\mathcal U
=
\frac{e^{-\Phi}}{(4\pi z_\tau)^n},
\]

temos localmente:

\[
\nabla_\mu\mathcal U
=
-\mathcal U\nabla_\mu\Phi
\]

e:

\[
\nabla_\mu\nabla_{\bar\nu}\mathcal U
=
\mathcal U
\left(
\nabla_\mu\Phi\nabla_{\bar\nu}\Phi
-\nabla_\mu\nabla_{\bar\nu}\Phi
\right).
\]

Assim, o termo:

\[
\left(
g_{\mu\bar\nu}\Delta
-\nabla_\mu\nabla_{\bar\nu}
\right)\mathcal U
\]

é exatamente a origem variacional dos termos tipo Perelman:

\[
\boxed{
\nabla_\mu\nabla_{\bar\nu}\Phi
}
\]

e dos termos quadráticos em \(\nabla\Phi\).

Em calibre de Perelman, ou após reorganizar por difeomorfismos gerados por
\(\nabla\Phi\), a equação métrica assume a forma de solíton/fluxo:

\[
\boxed{
\mathcal R_{\mu\bar\nu}
+\nabla_\mu\nabla_{\bar\nu}\Phi
=
\text{fontes efetivas de matéria, torção e potencial}.
}
\]

Essa é a forma que aparecia heuristicamente no capítulo 4 como:

\[
\mathcal R_{\mu\bar\nu}
+\nabla_\mu\nabla_{\bar\nu}f
=
\frac{1}{\tau}\mathcal T_{\mu\bar\nu}^{\rm quântico}.
\]

A formulação correta é: essa expressão é a forma reorganizada da equação
variacional completa, não uma equação independente colocada à mão.

---

## 8. Tipo da equação: elíptica, parabólica ou hiperbólica?

Há três níveis diferentes.

### 8.1 Equação variacional no bulk

A equação:

\[
\boxed{
\mathcal E_{\mu\bar\nu}=0
}
\]

é uma equação geométrica de segunda ordem para \(g_{\mu\bar\nu}\).

Como o bulk \(M\) é riemanniano/hermitiano, o operador principal, depois de
fixar difeomorfismos, é elíptico.

Portanto:

\[
\boxed{
\text{a equação métrica estacionária da ação é elíptica no bulk.}
}
\]

### 8.2 Fluxo em \(\tau\)

O fluxo associado:

\[
\boxed{
\partial_\tau g_{\mu\bar\nu}
=
-2
\left(
\mathcal R_{\mu\bar\nu}
+\nabla_\mu\nabla_{\bar\nu}\Phi
-\text{fontes}
\right)
}
\]

é do tipo Ricci--Perelman.

Depois da fixação de DeTurck, ele é parabólico.

Portanto:

\[
\boxed{
\text{o fluxo em }\tau\text{ é parabólico.}
}
\]

### 8.3 Evolução física

A evolução física causal não é o fluxo de \(\tau\).

A evolução física ocorre na camada lorentziana efetiva \(N^4\), com métrica:

\[
\boxed{
h_{\mu\nu}
=
q_{\mu\nu}
-2
\frac{u_\mu u_\nu}{q^{-1}(u,u)}.
}
\]

Nessa camada, os campos efetivos têm operador principal hiperbólico:

\[
\boxed{
h^{\mu\nu}k_\mu k_\nu.
}
\]

Portanto:

\[
\boxed{
\text{a causalidade física é hiperbólica em }N^4,
\text{ não no fluxo riemanniano de }\tau.
}
\]

---

## 9. Fluxo auxiliar ou evolução física?

O fluxo:

\[
\partial_\tau g_{\mu\bar\nu}
\]

é:

1. fluxo geométrico;
2. fluxo difusivo;
3. fluxo de escala/resolução;
4. relaxação para solítons;
5. ferramenta de renormalização geométrica.

Ele não é:

1. tempo físico;
2. evolução causal lorentziana;
3. propagação de sinais;
4. dinâmica operacional de observadores.

Portanto:

\[
\boxed{
\tau\text{ descreve fluxo auxiliar geométrico, não evolução física direta.}
}
\]

O tempo físico entra por:

\[
\boxed{
z_\tau=\tau+i\nu_0t.
}
\]

e a causalidade operacional é fixada por \(h\), por Sudarshan e pela
reconstrução OS já tratada nas Questões 7 e 8.

---

## 10. Como aparece a torção?

A GDQ não deve misturar Kähler estrito global com torção não nula. A estrutura
correta é hermitiana com conexão de Bismut.

Se a conexão usada na curvatura é:

\[
\boxed{
\nabla^B=\nabla^{LC}+\frac12H,
}
\]

onde \(H\) é a 3-forma de torção, então:

\[
\boxed{
\mathcal R
\longrightarrow
\mathcal R_B.
}
\]

Em convenção padrão:

\[
\boxed{
\mathcal R_B
=
\mathcal R_{LC}
-\frac{1}{12}H_{ABC}H^{ABC}
+\text{divergência}.
}
\]

Algumas convenções de Bismut usam coeficiente diferente no termo \(H^2\). O
coeficiente numérico deve seguir a normalização escolhida para \(H\). O ponto
estrutural é:

\[
\boxed{
\text{a torção entra pela curvatura da conexão de Bismut e por }H^2.
}
\]

O setor torsional efetivo pode ser escrito como:

\[
\boxed{
S_H
=
-\frac{1}{12}
\int
\sqrt g\,\mathcal U\,H_{ABC}H^{ABC}.
}
\]

Sua variação métrica gera:

\[
\boxed{
T_{AB}^{(H)}
=
\mathcal U
\left(
\frac12H_{A CD}H_B{}^{CD}
-\frac{1}{12}g_{AB}H_{CDE}H^{CDE}
\right).
}
\]

Em índices hermitianos, essa expressão é projetada para:

\[
\boxed{
T_{\mu\bar\nu}^{(H)}
=
\mathcal U
\left(
\frac12H_{\mu CD}H_{\bar\nu}{}^{CD}
-\frac{1}{12}g_{\mu\bar\nu}H^2
\right).
}
\]

Logo a equação métrica com torção fica, esquematicamente:

\[
\boxed{
\mathcal E_{\mu\bar\nu}
=
\mathcal E_{\mu\bar\nu}^{LC}
+\mathcal E_{\mu\bar\nu}^{H}
=0.
}
\]

Ou:

\[
\boxed{
\mathcal R^B_{\mu\bar\nu}
+\nabla_\mu^B\nabla_{\bar\nu}^B\Phi
=
\text{fontes efetivas}.
}
\]

Essa é a forma Ricci--Bismut/Perelman da equação.

---

## 11. Identidade de Bianchi

Como a ação é invariante por difeomorfismos do bulk, a identidade de Noether
associada implica:

\[
\boxed{
\nabla^A\mathcal E_{AB}
+
\mathcal E_f\nabla_Bf
+
\mathcal E_{\bar f}\nabla_B\bar f
+
\mathcal E_H\cdot\iota_BH
=0.
}
\]

Aqui:

1. \(\mathcal E_{AB}=0\) é a equação métrica;
2. \(\mathcal E_f=0\) é a equação de \(f\);
3. \(\mathcal E_{\bar f}=0\) é a equação de \(\bar f\);
4. \(\mathcal E_H=0\) é a equação do setor torsional, quando \(H\) é tratado
   como campo efetivo independente.

Portanto, quando as equações de matéria/torção são satisfeitas:

\[
\boxed{
\nabla^A\mathcal E_{AB}=0.
}
\]

No setor com conexão de Bismut, a identidade correspondente é:

\[
\boxed{
\nabla^{B\,A}\mathcal E_{AB}=0
}
\]

com a derivada compatível com a conexão torsional escolhida.

Isso é a versão GDQ da identidade de Bianchi.

---

## 12. Conservação covariante

Da identidade anterior segue que o tensor energia-momento efetivo satisfaz
conservação covariante on shell:

\[
\boxed{
\nabla^A T_{AB}^{\rm eff}=0
}
\]

ou, no setor Bismut:

\[
\boxed{
\nabla^{B\,A} T_{AB}^{\rm eff}=0.
}
\]

Na projeção física lorentziana \(N^4\), a conservação operacional é:

\[
\boxed{
\nabla_h^\mu T_{\mu\nu}^{\rm eff}=0,
}
\]

desde que:

1. os campos efetivos satisfaçam suas equações de movimento;
2. a projeção \(M\to N^4\) preserve o acoplamento covariante;
3. não haja fluxo de energia atravessando bordos físicos não contabilizados.

Fora da casca, ou se \(f,\bar f,H\) não satisfazem suas equações, a divergência
de \(T_{\mu\nu}\) não precisa ser zero isoladamente. Ela é compensada pelos
termos:

\[
\mathcal E_f\nabla_\nu f,
\qquad
\mathcal E_{\bar f}\nabla_\nu\bar f,
\qquad
\mathcal E_H\cdot\iota_\nu H.
\]

Essa distinção é obrigatória para evitar uma falsa prova de conservação.

---

## 13. Forma final consolidada

A resposta final da Questão 12 pode ser resumida assim:

\[
\boxed{
\frac{\delta S_{\rm phys}}{\delta g^{\mu\bar\nu}}=0
\Longrightarrow
\mathcal E_{\mu\bar\nu}=0,
}
\]

com:

\[
\boxed{
\mathcal E_{\mu\bar\nu}
=
\tau
\left[
\mathcal U\,G_{\mu\bar\nu}
+
\left(
g_{\mu\bar\nu}\Delta
-\nabla_\mu\nabla_{\bar\nu}
\right)\mathcal U
\right]
+
\tau\mathcal U
\left[
\partial_\mu f\partial_{\bar\nu}\bar f
-\frac12g_{\mu\bar\nu}X
\right]
-\frac12
\mathcal U
g_{\mu\bar\nu}
(\Phi-n)
+\mathcal E_{\mu\bar\nu}^{H}.
}
\]

Se \(H=0\), remove-se \(\mathcal E_{\mu\bar\nu}^{H}\).

Se a conexão usada é Bismut, substitui-se:

\[
\boxed{
\mathcal R\to\mathcal R_B,
\qquad
G_{\mu\bar\nu}\to G_{\mu\bar\nu}^{B},
\qquad
\nabla\to\nabla^B.
}
\]

O fluxo associado é:

\[
\boxed{
\partial_\tau g_{\mu\bar\nu}
=
-2
\left(
\mathcal R_{\mu\bar\nu}^{B}
+\nabla_\mu^B\nabla_{\bar\nu}^B\Phi
-\text{fontes}
\right).
}
\]

Após calibre de DeTurck, esse fluxo é parabólico.

---

## 14. Status da Questão 12

\[
\boxed{
\text{Questão 12 fechada estruturalmente no setor variacional declarado.}
}
\]

A ação produz a equação métrica por variação completa em
\(g^{\mu\bar\nu}\).

O tensor energia-momento é obtido por:

\[
\boxed{
T_{\mu\bar\nu}
=
-\frac{2}{\sqrt g}
\frac{\delta S_{\rm mat}}{\delta g^{\mu\bar\nu}},
}
\]

e não por analogia.

A equação estacionária no bulk é elíptica após fixação de gauge.

O fluxo em \(\tau\) é parabólico e auxiliar.

A evolução física causal é hiperbólica somente na camada efetiva \(N^4\), com
métrica \(h\).

A torção entra pela conexão de Bismut e pelo termo \(H^2\).

A identidade de Bianchi decorre da invariância por difeomorfismos, e a
conservação covariante vale on shell:

\[
\boxed{
\nabla^A T_{AB}^{\rm eff}=0
\quad
\text{ou}
\quad
\nabla^{B\,A}T_{AB}^{\rm eff}=0
}
\]

conforme se use Levi--Civita ou Bismut.

O fechamento é estrutural, não uma prova automática de estabilidade de todos
os backgrounds materiais. Para cada solução física concreta ainda é necessário
especificar domínio, classe Hermitiano--Bismut, condições de bordo, projetor de
gauge e Hessiana física. Essa exigência não reabre a derivação da equação
métrica; ela apenas separa estacionariedade variacional de estabilidade
espectral.
