---
title: "Born operacional por medida em projetores"
---

# Born operacional por medida em projetores

## Enunciado

No espaço de Hilbert físico reconstruído, toda regra operacional de
probabilidade para alternativas projetivas que seja positiva, normalizada,
aditiva em alternativas exclusivas e compatível com composição tem a forma:

$$
\mu(P)=\operatorname{Tr}(\varrho P).
$$

Para estado puro e projetor unidimensional, isso dá:

$$
P(i|\psi)=|\langle i|\psi\rangle|^2.
$$

## Status

Teorema operacional condicional. Ele depende de:

1. reconstrução do Hilbert físico;
2. positividade do produto interno;
3. projetores como alternativas experimentais;
4. aditividade operacional;
5. compatibilidade de composição.

## Prova

Seja $\mathcal H_{\rm phys}$ o Hilbert físico reconstruído:

$$
\mathcal H_{\rm phys}
=
\overline{\mathcal D_+/(\mathcal N+\mathcal G)}.
$$

Uma alternativa experimental elementar é um projetor:

$$
P=P^\dagger=P^2.
$$

Alternativas exclusivas obedecem:

$$
P_iP_j=0
\quad
(i\ne j).
$$

Uma medida operacional deve satisfazer:

$$
\mu(P)\ge0,
\qquad
\mu(I)=1,
$$

e:

$$
\mu\left(\sum_iP_i\right)=\sum_i\mu(P_i)
$$

para projetores ortogonais. Sob a hipótese usual de não contextualidade
operacional da alternativa projetiva e compatibilidade com composição, a forma
positiva e aditiva é representada por um operador positivo de traço um:

$$
\varrho\ge0,
\qquad
\operatorname{Tr}\varrho=1.
$$

Então:

$$
\mu(P)=\operatorname{Tr}(\varrho P).
$$

Essa é a etapa estrutural. Em dimensão $\dim\mathcal H\ge3$, ela é a forma
usual do teorema de Gleason: uma medida finitamente aditiva, positiva,
normalizada e não contextual sobre projetores é representada por um operador
densidade. Em setores bidimensionais isolados, a mesma forma é selecionada
quando se exige continuidade física, compatibilidade com POVMs ou composição
com um aparelho/ambiente auxiliar. Essa ressalva é importante porque um qubit
real nunca é observado sem graus de liberdade adicionais do aparelho.

Para estado puro:

$$
\varrho=|\psi\rangle\langle\psi|.
$$

Logo:

$$
\mu(P)
=
\operatorname{Tr}(|\psi\rangle\langle\psi|P)
=
\langle\psi|P|\psi\rangle.
$$

Se:

$$
P_i=|i\rangle\langle i|,
$$

então:

$$
\mu(P_i)
=
\langle\psi|i\rangle\langle i|\psi\rangle
=
|\langle i|\psi\rangle|^2.
$$

## Aditividade e normalização

Se $P_iP_j=0$, então $P_i+P_j$ representa a alternativa exclusiva
"$i$ ou $j$". Pela linearidade do traço:

$$
\mu(P_i+P_j)
=
\operatorname{Tr}(\varrho(P_i+P_j))
=
\operatorname{Tr}(\varrho P_i)
+
\operatorname{Tr}(\varrho P_j).
$$

Logo:

$$
\mu(P_i+P_j)=\mu(P_i)+\mu(P_j).
$$

Para uma decomposição completa,

$$
\sum_iP_i=I,
$$

temos:

$$
\sum_i\mu(P_i)
=
\operatorname{Tr}\left(\varrho\sum_iP_i\right)
=
\operatorname{Tr}(\varrho)
=1.
$$

## Bases arbitrárias

A base de medição é determinada pelo aparelho, não pela regra de Born. Se o
aparelho seleciona uma base ortonormal $\{|a_i\rangle\}$, os projetores são:

$$
P_i^{(a)}
=
|a_i\rangle\langle a_i|.
$$

A probabilidade é:

$$
P(a_i|\psi)
=
\langle\psi|P_i^{(a)}|\psi\rangle
=
|\langle a_i|\psi\rangle|^2.
$$

Se outra base é obtida por uma transformação unitária,

$$
|b_j\rangle
=
\sum_i U_{ji}|a_i\rangle,
\qquad
U^\dagger U=I,
$$

então:

$$
P(b_j|\psi)
=
|\langle b_j|\psi\rangle|^2.
$$

A regra é a mesma porque depende do projetor, não das coordenadas escolhidas
para escrevê-lo.

## Sistemas compostos

Para sistemas distinguíveis reconstruídos em setores físicos,

$$
\mathcal H_{AB}
=
\mathcal H_A\otimes\mathcal H_B.
$$

Se o estado é produto,

$$
\varrho_{AB}
=
\varrho_A\otimes\varrho_B,
$$

e o evento composto é

$$
P_{A\land B}
=
P_A\otimes P_B,
$$

então:

$$
P(A\land B)
=
\operatorname{Tr}_{AB}
\left[
(\varrho_A\otimes\varrho_B)(P_A\otimes P_B)
\right].
$$

Pela fatoração do traço:

$$
P(A\land B)
=
\operatorname{Tr}_A(\varrho_AP_A)
\operatorname{Tr}_B(\varrho_BP_B).
$$

Portanto:

$$
P(A\land B)=P(A)P(B)
$$

para estados produto.

Para estados não fatoráveis,

$$
\varrho_{AB}\ne\varrho_A\otimes\varrho_B,
$$

a regra geral é:

$$
P(a,b)
=
\operatorname{Tr}_{AB}
\left[
\varrho_{AB}(P_a\otimes Q_b)
\right].
$$

As probabilidades marginais são obtidas pelo traço parcial:

$$
\varrho_A=\operatorname{Tr}_B\varrho_{AB},
\qquad
P(a)=\operatorname{Tr}_A(\varrho_AP_a).
$$

Isso preserva a compatibilidade operacional com composição e evita que Born
seja apenas uma regra de coordenadas para uma partícula isolada.

## Observáveis contínuos e posição

Para um observável autoadjunto $A$, a alternativa "$A$ pertence ao conjunto
$\Delta$" é representada pela medida espectral $E_A(\Delta)$:

$$
P(A\in\Delta|\varrho)
=
\operatorname{Tr}(\varrho E_A(\Delta)).
$$

No caso de posição,

$$
P(x\in R|\psi)
=
\int_R|\psi(x)|^2\,d\mu_h.
$$

Como, no setor regular da GDQ,

$$
\Psi(x)
=
\sqrt{\rho(x)}e^{iS_R(x)/\hbar},
$$

segue que:

$$
|\Psi(x)|^2=\rho(x).
$$

Portanto:

$$
P(x\in R)
=
\int_R\rho(x)\,d\mu_h.
$$

Essa é a recuperação da densidade geométrica local como probabilidade de
posição.

## Alcance

Essa nota prova a forma operacional de Born no Hilbert reconstruído. Ela não
substitui a dinâmica do aparelho. O aparelho ainda é necessário para selecionar
quais projetores são fisicamente realizados.
