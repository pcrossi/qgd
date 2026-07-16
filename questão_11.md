# Questão 11 — A ação produz Hamilton--Jacobi--Bohm?

## 1. Pergunta

A Questão 11 pergunta:

\[
\boxed{
\text{a ação produz a equação de Hamilton--Jacobi com potencial de Bohm?}
}
\]

O problema apontado em `11-0.md` é:

1. demonstrar que a variação em relação à densidade produz

\[
\frac{\delta I}{\delta\rho}=0;
\]

2. obter exatamente

\[
\boxed{
\partial_tS
+\frac{|\nabla S|^2}{2m}
+V
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt{\rho}}{\sqrt{\rho}}
=0;
}
\]

3. eliminar a derivada adicional aplicada ao potencial de Bohm, caso ela tenha
   sido usada no capítulo 4 como se fizesse parte da equação de
   Hamilton--Jacobi.

---

## 2. Resposta curta

Sim. A ação produz Hamilton--Jacobi--Bohm quando se usa a mesma redução
Madelung/canônica já fixada na Questão 10.

A variação em \(S_R\) produz a continuidade:

\[
\boxed{
\frac{\delta I}{\delta S_R}=0
\Longrightarrow
\partial_t\rho+\nabla\cdot(\rho v)=0.
}
\]

A variação em \(\rho\) produz a equação de Hamilton--Jacobi--Bohm:

\[
\boxed{
\frac{\delta I}{\delta\rho}=0
\Longrightarrow
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
+Q
=0,
}
\]

com:

\[
\boxed{
Q
=
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt{\rho}}{\sqrt{\rho}}.
}
\]

Portanto:

\[
\boxed{
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt{\rho}}{\sqrt{\rho}}
=0.
}
\]

Essa é exatamente a equação exigida em `11-0.md`.

---

## 3. Variáveis usadas

Na GDQ:

\[
f
=
-\frac{S_I-iS_R}{\hbar}
=
-\frac{S_I}{\hbar}
+i\frac{S_R}{\hbar}.
\]

A densidade é:

\[
\boxed{
\rho
=
e^{S_I/\hbar}
=
e^{-(f+\bar f)/2}.
}
\]

A amplitude real é:

\[
\boxed{
R=\sqrt{\rho}.
}
\]

A função de onda efetiva é:

\[
\boxed{
\Psi=R\,e^{iS_R/\hbar}.
}
\]

A velocidade de Madelung é:

\[
\boxed{
v=\frac{\nabla S_R}{m}.
}
\]

Em métrica efetiva \(G\), substitui-se:

\[
|\nabla S_R|^2
\longrightarrow
G^{AB}\partial_AS_R\partial_BS_R,
\]

e:

\[
\Delta
\longrightarrow
\Delta_G.
\]

---

## 4. Ação reduzida relevante

O setor Madelung da ação física reduzida pode ser escrito como:

\[
\boxed{
I_{\rm Mad}[\rho,S_R]
=
\int dt\int_\Sigma
\left[
\rho
\left(
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
\right)
+\frac{\hbar^2}{8m}
\frac{|\nabla\rho|^2}{\rho}
\right]d^dx.
}
\]

Equivalentemente, usando \(R=\sqrt\rho\):

\[
\boxed{
I_{\rm Mad}[\rho,S_R]
=
\int dt\int_\Sigma
\left[
\rho
\left(
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
\right)
+\frac{\hbar^2}{2m}
|\nabla R|^2
\right]d^dx.
}
\]

Essas duas formas são idênticas, pois:

\[
\nabla R
=
\frac{1}{2\sqrt\rho}\nabla\rho,
\]

logo:

\[
|\nabla R|^2
=
\frac{1}{4}
\frac{|\nabla\rho|^2}{\rho}.
\]

Portanto:

\[
\frac{\hbar^2}{2m}|\nabla R|^2
=
\frac{\hbar^2}{8m}
\frac{|\nabla\rho|^2}{\rho}.
\]

---

## 5. Por que esse termo é o termo de Bohm

O potencial de Bohm é:

\[
\boxed{
Q[\rho]
=
-\frac{\hbar^2}{2m}
\frac{\Delta R}{R}
=
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
}
\]

A energia quântica associada é:

\[
\int_\Sigma \rho Q\,d^dx.
\]

Substituindo \(R=\sqrt\rho\):

\[
\int_\Sigma \rho Q\,d^dx
=
-\frac{\hbar^2}{2m}
\int_\Sigma R^2\frac{\Delta R}{R}\,d^dx
=
-\frac{\hbar^2}{2m}
\int_\Sigma R\Delta R\,d^dx.
\]

Integrando por partes:

\[
\int_\Sigma R\Delta R\,d^dx
=
-\int_\Sigma |\nabla R|^2\,d^dx
+\int_{\partial\Sigma}R\,\nabla R\cdot n\,d\Sigma.
\]

Com bordo nulo, suporte compacto, periodicidade, ou condição de no-flux:

\[
\int_{\partial\Sigma}R\,\nabla R\cdot n\,d\Sigma=0.
\]

Assim:

\[
\boxed{
\int_\Sigma \rho Q\,d^dx
=
\frac{\hbar^2}{2m}
\int_\Sigma |\nabla R|^2\,d^dx
=
\frac{\hbar^2}{8m}
\int_\Sigma
\frac{|\nabla\rho|^2}{\rho}\,d^dx.
}
\]

Logo, o termo Fisher:

\[
\boxed{
\frac{\hbar^2}{8m}
\frac{|\nabla\rho|^2}{\rho}
}
\]

é exatamente a forma integrada por partes do potencial quântico de Bohm.

---

## 6. Variação em relação a \(\rho\)

Defina:

\[
A
=
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V.
\]

A ação fica:

\[
I_{\rm Mad}
=
\int dt\int_\Sigma
\left[
\rho A
+\frac{\hbar^2}{8m}
\frac{|\nabla\rho|^2}{\rho}
\right]d^dx.
\]

Faça:

\[
\rho\mapsto\rho+\varepsilon\eta,
\qquad
\delta\rho=\eta.
\]

A variação do primeiro termo é:

\[
\delta\int\rho A\,d^dx
=
\int A\eta\,d^dx.
\]

Agora varie o termo de Fisher:

\[
F[\rho]
=
\frac{\hbar^2}{8m}
\int
\frac{|\nabla\rho|^2}{\rho}
d^dx.
\]

Temos:

\[
\delta F
=
\frac{\hbar^2}{8m}
\int
\left[
\frac{2\nabla\rho\cdot\nabla\eta}{\rho}
-
\frac{|\nabla\rho|^2}{\rho^2}\eta
\right]d^dx.
\]

Integre o primeiro termo por partes:

\[
\int
\frac{2\nabla\rho\cdot\nabla\eta}{\rho}
d^dx
=
-\int
2\nabla\cdot
\left(
\frac{\nabla\rho}{\rho}
\right)
\eta\,d^dx
+B_\rho.
\]

Com condições de bordo adequadas:

\[
B_\rho=0.
\]

Portanto:

\[
\delta F
=
\frac{\hbar^2}{8m}
\int
\left[
-2\nabla\cdot
\left(
\frac{\nabla\rho}{\rho}
\right)
-
\frac{|\nabla\rho|^2}{\rho^2}
\right]\eta\,d^dx.
\]

Como:

\[
\nabla\cdot
\left(
\frac{\nabla\rho}{\rho}
\right)
=
\frac{\Delta\rho}{\rho}
-
\frac{|\nabla\rho|^2}{\rho^2},
\]

obtemos:

\[
\delta F
=
\int
\left[
-\frac{\hbar^2}{4m}
\frac{\Delta\rho}{\rho}
+
\frac{\hbar^2}{8m}
\frac{|\nabla\rho|^2}{\rho^2}
\right]\eta\,d^dx.
\]

Mas:

\[
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=
\frac{1}{2}
\frac{\Delta\rho}{\rho}
-
\frac{1}{4}
\frac{|\nabla\rho|^2}{\rho^2}.
\]

Logo:

\[
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=
-\frac{\hbar^2}{4m}
\frac{\Delta\rho}{\rho}
+
\frac{\hbar^2}{8m}
\frac{|\nabla\rho|^2}{\rho^2}.
\]

Assim:

\[
\boxed{
\frac{\delta F}{\delta\rho}
=
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=Q.
}
\]

A variação total é:

\[
\delta I_{\rm Mad}
=
\int dt\int_\Sigma
\left[
A+Q
\right]\eta\,d^dx.
\]

Como \(\eta\) é arbitrária:

\[
\boxed{
A+Q=0.
}
\]

Portanto:

\[
\boxed{
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=0.
}
\]

Essa é a equação de Hamilton--Jacobi--Bohm.

---

## 7. Forma covariante geométrica

No setor geométrico da GDQ, substitui-se a métrica plana pela métrica efetiva
do setor físico.

A ação reduzida fica:

\[
\boxed{
I_{\rm Mad}^{G}
=
\int d\lambda
\int_{\Sigma_\lambda}
\left[
\rho
\left(
\partial_\lambda S_R
+\frac{1}{2m}
G^{AB}\partial_AS_R\partial_BS_R
+V_{\rm geom}
\right)
+\frac{\hbar^2}{8m}
\frac{G^{AB}\partial_A\rho\partial_B\rho}{\rho}
\right]d\mu_G.
}
\]

A variação em \(\rho\) produz:

\[
\boxed{
\partial_\lambda S_R
+\frac{1}{2m}
G^{AB}\partial_AS_R\partial_BS_R
+V_{\rm geom}
-\frac{\hbar^2}{2m}
\frac{\Delta_G\sqrt\rho}{\sqrt\rho}
=0.
}
\]

Aqui:

\[
\boxed{
\Delta_G R
=
\nabla_A\nabla^A R
=
\frac{1}{\sqrt{|G|}}
\partial_A
\left(
\sqrt{|G|}G^{AB}\partial_BR
\right).
}
\]

Essa é a versão geométrica da Hamilton--Jacobi--Bohm.

---

## 8. Relação com a ação oficial da GDQ

A ação oficial permanece a ação preservada nas Questões 4 e 9:

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

A Questão 11 não altera essa ação.

Ela explica sua redução local no par:

\[
\boxed{
(\rho,S_R).
}
\]

O mapeamento é:

\[
\boxed{
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f).
}
\]

O termo:

\[
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f
\]

contém, ao decompor \(f\) em parte real e fase:

\[
\boxed{
\text{termo cinético de fase}
+
\text{termo osmótico/Fisher da densidade}.
}
\]

O setor osmótico/Fisher é exatamente o setor que gera:

\[
\boxed{
Q
=
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
}
\]

Portanto, a Hamilton--Jacobi--Bohm não é adicionada como postulado externo; ela
é a forma hidrodinâmica da variação real da ação reduzida.

---

## 9. Correção da derivada extra do potencial de Bohm

A equação de Hamilton--Jacobi--Bohm contém \(Q\), não \(\nabla Q\):

\[
\boxed{
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
+Q
=0.
}
\]

Com:

\[
\boxed{
Q
=
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
}
\]

Se em algum trecho do capítulo 4 aparece uma derivada adicional aplicada ao
potencial de Bohm dentro da própria equação de Hamilton--Jacobi, a forma deve
ser corrigida.

A forma incorreta seria algo do tipo:

\[
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
+\nabla Q
=0,
\]

ou:

\[
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
+\Delta Q
=0.
\]

Essas expressões estão dimensionalmente e variacionalmente erradas para a
equação escalar de Hamilton--Jacobi.

A derivada de \(Q\) aparece apenas quando se toma o gradiente da equação de
Hamilton--Jacobi para obter a equação de Euler/Madelung.

Tomando:

\[
v=\frac{\nabla S_R}{m},
\]

o gradiente de:

\[
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
+Q
=0
\]

gera:

\[
\boxed{
m
\left(
\partial_t+v\cdot\nabla
\right)v
=
-\nabla(V+Q).
}
\]

Portanto:

\[
\boxed{
\nabla Q
\text{ pertence à equação de força/Euler, não à equação de Hamilton--Jacobi.}
}
\]

Essa é a correção necessária indicada em `11-0.md`.

---

## 10. Condições de bordo

A derivação usa integração por partes. Os termos de bordo desaparecem se vale
uma das condições:

1. \(\delta\rho=0\) no bordo;
2. \(R=\sqrt\rho\) decai suficientemente rápido no infinito;
3. o domínio é compacto sem bordo;
4. há periodicidade no toro interno;
5. o contorno causal \(\gamma\) fecha os termos de extremidade;
6. impõe-se condição de no-flux:

\[
\boxed{
\nabla R\cdot n=0
\quad
\text{ou}
\quad
\nabla\rho\cdot n=0.
}
\]

Sem uma dessas condições, a variação produz também uma condição natural de
bordo. Isso não altera a equação local, mas precisa ser declarado para a prova
ficar completa.

---

## 11. Consequência lógica

Com as Questões 10 e 11, o par Madelung fica fechado:

\[
\boxed{
\frac{\delta I}{\delta S_R}=0
\Longrightarrow
\partial_t\rho+\nabla\cdot(\rho v)=0.
}
\]

e:

\[
\boxed{
\frac{\delta I}{\delta\rho}=0
\Longrightarrow
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
+Q
=0.
}
\]

Juntas, essas duas equações são equivalentes à equação de Schrödinger no setor
não relativístico quando:

\[
\boxed{
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
}
\]

Explicitamente:

\[
i\hbar\partial_t\Psi
=
\left(
-\frac{\hbar^2}{2m}\Delta+V
\right)\Psi.
\]

Assim, a GDQ recupera o setor quântico não relativístico padrão por redução
Madelung.

---

## 12. Status da Questão 11

\[
\boxed{
\text{Questão 11 fechada oficialmente.}
}
\]

A ação produz Hamilton--Jacobi--Bohm porque a variação da densidade no setor
Madelung reduzido gera:

\[
\boxed{
\frac{\delta I}{\delta\rho}=0
\Longrightarrow
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=0.
}
\]

A correção necessária é:

\[
\boxed{
Q
=
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
\text{ entra sem derivada adicional na Hamilton--Jacobi.}
}
\]

A derivada:

\[
\boxed{
\nabla Q
}
\]

aparece somente depois, na equação de Euler/Madelung para a força quântica.
