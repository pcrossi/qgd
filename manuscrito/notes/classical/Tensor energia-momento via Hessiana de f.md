---
title: "Tensor energia-momento via Hessiana de f"
---

# Tensor energia-momento via Hessiana de $f$

## Enunciado

No limite macroscópico, a resposta métrica efetiva da GDQ pode ser organizada
como um tensor energia-momento obtido da variação do setor de $f$ em relação à
métrica. Esse tensor é uma redução, não um novo postulado.

## Ponto de partida

Considere o setor interno do integrando:

$$
\mathcal L_f
=
\tau\,g^{\mu\bar\nu}
\partial_\mu f\,\partial_{\bar\nu}\bar f
\mathcal V(f,\bar f,g),
$$

onde $\mathcal V$ inclui os termos ponderados que não dependem explicitamente
de derivadas de $f$ na passagem considerada.

A contribuição material efetiva é definida por variação métrica:

$$
T_{AB}^{(f)}
=
-\frac{2}{\sqrt g}
\frac{\delta}{\delta g^{AB}}
\int_M
\mathcal L_f\,\mathcal U\sqrt g\,dV.
$$

## Variação principal

Usando:

$$
\delta\sqrt g
=
-\frac12\sqrt g\,g_{AB}\delta g^{AB},
$$

e separando a dependência explícita de $g^{AB}$ no termo cinético, obtém-se a
estrutura:

$$
T_{AB}^{(f)}
=
2\tau\,{\rm Re}
\left(
\partial_A f\,\partial_B\bar f
\right)\mathcal U
-g_{AB}\mathcal L_f\mathcal U
+T_{AB}^{(\mathcal U)}.
$$

O termo $T_{AB}^{(\mathcal U)}$ aparece porque $\mathcal U$ depende de $\rho$,
e $\rho$ depende da parte real de $f$. Quando a métrica é variada mantendo
$f$ fixo, esse termo pode se reduzir; quando a variação física transporta
$f$, ele deve ser mantido.

## Projeção clássica

No setor de Madelung:

$$
f
=
-\ln\rho
+\frac{i}{\hbar}S_R,
$$

os gradientes de fase dominam quando $\varepsilon_{\rm cl}\ll1$. Então a parte
principal do tensor assume a forma de fluxo:

$$
T_{AB}^{\rm cl}
\sim
\rho\,\partial_A S_R\,\partial_B S_R
+\text{termos de pressão geométrica}.
$$

Os termos de pressão geométrica são os que geram correções de Bohm, tensões de
torção e respostas de borda. Quando eles são pequenos ou isotropizados, resta o
tensor clássico de matéria efetiva.

## Alcance

Essa construção mostra como o tensor energia-momento pode emergir da Hessiana e
da variação métrica do setor de $f$. Ela não substitui a prova de uma equação
de Einstein completa em todo background: para isso é necessário transportar a
ponte global--local, fixar contornos e controlar os modos de gauge.

