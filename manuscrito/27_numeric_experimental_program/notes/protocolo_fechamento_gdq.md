---
title: "Nota — Protocolo de fechamento GDQ"
---

# Nota — Protocolo de fechamento GDQ

Esta nota fixa o padrão mínimo para transformar uma conta da GDQ em resultado
preservável no manuscrito. Ela não substitui a ação oficial; ela organiza a
forma de usar a ação, os vínculos, a Hessiana e os dados externos do aparelho.

## 1. Enunciado mínimo

Todo cálculo deve começar declarando:

- qual observável será calculado;
- qual background estacionário é usado;
- qual domínio e quais bordos entram;
- quais vínculos são impostos;
- quais parâmetros são universais da GDQ;
- quais parâmetros pertencem ao aparelho, material ou preparação experimental;
- qual dado experimental será usado apenas para comparação.

Sem essa separação, um bom ajuste numérico não distingue predição, comparação
fenomenológica e engenharia inversa.

## 2. Cadeia variacional

A cadeia completa é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_*
\to
C_a[\Phi]=0
\to
P_{\rm phys}
\to
K_{\rm phys}
\to
J_{\rm app}
\to
\delta\Phi
\to
\mathsf R_{\rm app}
\to
\mathcal O_{\rm obs}.
$$

Aqui:

- $\Phi_*$ é solução estacionária admissível;
- $C_a[\Phi]=0$ representa vínculos de carga, fluxo, normalização, gauge e
  bordo;
- $P_{\rm phys}$ remove modos de gauge e variações proibidas;
- $K_{\rm phys}$ é a Hessiana física da ação oficial no setor permitido;
- $J_{\rm app}$ é fonte, sonda, vínculo ou contorno clássico;
- $\mathsf R_{\rm app}$ é a impedância obtida por eliminação variacional;
- $\mathcal O_{\rm obs}$ é o observável comparável.

O elo central é:

$$
K_{\rm phys}
=
P_{\rm phys}^\dagger
\operatorname{Hess}_{\Phi_*}\mathcal S_{\rm GDQ}
P_{\rm phys}.
$$

Se um resultado usa apenas uma redução efetiva desse operador, isso deve ser
dito no próprio texto.

## 3. Projetor físico

Se $D C$ é a matriz dos vínculos linearizados e $G$ é a métrica quadrática no
espaço de flutuações, o projetor físico é:

$$
P_{\rm phys}
=
I
-
G^{-1}D C^\dagger
\left(D C\,G^{-1}D C^\dagger\right)^{-1}
D C.
$$

Ele satisfaz:

$$
D C\,P_{\rm phys}=0,
\qquad
P_{\rm phys}^2=P_{\rm phys}.
$$

O significado físico é simples: só se diagonaliza a Hessiana depois de remover
direções que correspondem a redundâncias, mudanças de coordenada, violação de
normalização ou alteração não autorizada de carga/fluxo.

## 4. Complemento de Schur e DtN

Quando o observável vive em um bordo, detector ou interface, os graus internos
podem ser eliminados. Escrevendo:

$$
K_{\rm phys}
=
\begin{pmatrix}
K_{\partial\partial} & K_{\partial I}\\
K_{I\partial} & K_{II}
\end{pmatrix},
$$

a impedância efetiva é:

$$
\mathsf R_{\rm app}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

Essa fórmula é a versão matricial do operador Dirichlet-to-Neumann. Ela aparece
em detectores, fendas, interfaces magnéticas, superfície do próton, horizontes,
canal nuclear e fronteiras cosmológicas. Em todos os casos, ela deve ser
entendida como eliminação de graus de liberdade da Hessiana, não como novo
termo fundamental.

## 5. Classificação numérica

Todo script deve declarar uma das categorias:

1. avaliação direta de quantidade derivada;
2. teste de convergência;
3. teste de consistência;
4. engenharia inversa;
5. ajuste ou calibração;
6. comparação fenomenológica;
7. previsão cega.

Para pretensão preditiva, os parâmetros devem ser congelados antes da
comparação com o dado aceito.

## 6. Critérios mínimos de aceitação

Um resultado é preservável no manuscrito quando informa:

- equação ou funcional avaliado;
- domínio;
- operador;
- condições de contorno;
- vínculos;
- normalização;
- unidades;
- classificação numérica;
- estudo de tolerância ou malha quando aplicável;
- comparação com limite analítico quando existir;
- comparação com dado aceito quando o capítulo fizer afirmação fenomenológica;
- limitações que permanecem.

## 7. O que não fecha uma questão

Não fecha uma questão:

- escolher coeficiente pelo alvo experimental e chamá-lo de derivado;
- absorver discrepância em efeito térmico, contorno, Fano, loop ou superfície
  sem calcular o termo;
- omitir uma malha ruim;
- trocar a ação oficial por uma teoria externa;
- chamar uma analogia de prova;
- usar uma coincidência numérica para inferir identidade variacional.

Esse protocolo serve exatamente para evitar que resultados corretos fiquem
misturados com rotas superadas.
