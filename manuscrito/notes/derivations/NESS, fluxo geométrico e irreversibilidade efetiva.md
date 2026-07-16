---
title: "NESS, fluxo geométrico e irreversibilidade efetiva"
---

# NESS, fluxo geométrico e irreversibilidade efetiva

## 1. Três evoluções que não devem ser identificadas

Na GDQ aparecem três estruturas distintas:

1. o parâmetro $\tau$ do fluxo geométrico;
2. o tempo físico $t$ reconstruído na folha do laboratório;
3. a evolução reduzida de variáveis macroscópicas depois de uma projeção.

O fluxo em $\tau$ pode possuir funcionais monótonos. A evolução física fechada
em $t$, quando reconstruída por um Hamiltoniano autoadjunto, preserva norma:

$$
\frac{d}{dt}\lVert\Psi(t)\rVert^2=0.
$$

Essas afirmações não se contradizem porque se referem a geradores e espaços de
estado diferentes.

## 2. Projeção e dinâmica reduzida

Se $P$ projeta sobre observáveis monitorados e $Q=1-P$, a eliminação formal do
setor $Q$ produz uma equação de Nakajima--Zwanzig do tipo

$$
\frac{d}{dt}P\varrho(t)
=PLP\varrho(t)
+\int_0^tK(t-s)P\varrho(s)\,ds
+I(t),
$$

onde $L$ é o gerador microscópico, $K$ é um kernel de memória e $I$ depende
das correlações iniciais não monitoradas. Mesmo que $L$ gere uma evolução
reversível, a equação projetada pode ser dissipativa.

No limite de memória curta, o kernel pode reduzir-se a um termo local. A
entropia macroscópica então pode satisfazer

$$
\frac{dS_{\rm macro}}{dt}\ge0,
$$

sem que a norma microscópica deixe de ser conservada.

## 3. Definição operacional de NESS

Um NESS é um estado reduzido $\varrho_{\rm ss}$ tal que

$$
\frac{d}{dt}\langle O_a\rangle_{\rm ss}=0
$$

para o conjunto de observáveis macroscópicos escolhido, mas que pode sustentar
correntes

$$
J_a\neq0.
$$

“Estacionário” não significa equilíbrio termodinâmico nem ausência de fluxo.
Também não significa que o universo-bloco evolui literalmente numa quinta
dimensão física.

## 4. Uso correto na GDQ

A GDQ fornece candidatos naturais aos elementos da redução:

- a medida $\mathcal U$ e as correntes de Noether definem as quantidades
  conservadas;
- a Hessiana separa modos lentos, rápidos, ligados e contínuos;
- o aparelho e a interface determinam quais graus são monitorados;
- a mobilidade causal fornece a escala temporal em $t$;
- o fluxo em $\tau$ organiza relaxamento geométrico, mas não prova sozinho a
  irreversibilidade física.

Portanto NESS é uma redução efetiva admissível da GDQ. Para um aparelho
específico, a dissipação deve ser derivada do acoplamento e do kernel de
influência, não postulada pela simples monotonicidade de Perelman.
