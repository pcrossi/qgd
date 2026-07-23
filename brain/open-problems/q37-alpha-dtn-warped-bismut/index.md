---
title: Q37 applicability audit for alpha
status: applicability-audit
source: questoes/q37/questao_37.md
updated: 2026-07-17
---

# Q37 applicability audit for alpha

## Problema

A média cosmológica de Einstein já fornece uma origem numérica condicional
para $\alpha$:

$$
(\alpha_E^{\rm mean})^{-1}=137{,}036082448\ldots
$$

O problema aberto não é mais "achar um número" para $\alpha$. Também não é
mais derivar o projetor \(9/(8\pi^4)\) dentro da classe isotrópica de
Einstein: isso foi feito em
`questoes/q37/associados/fechamento_alpha_hessiana_loop.md`.

O loop de 2026-07-17 calculou a contração específica:

$$
\mathcal P_{\rm iso}
=
\frac9{8\pi^4}.
$$

O fator \(1920\), a raiz quarta e o projetor isotrópico Haar/axial têm leitura
geométrica controlada no ensemble de Einstein. O que resta é auditar se o
background global real usado pela GDQ pertence à classe isotrópica exigida
pela prova.

## O que falta

1. verificar que a medida estacionária do background global é efetivamente a
   órbita completa de \(W(D_5)\);
2. verificar que o eixo Hopf axial coerente é selecionado sem quebrar a
   isotropia média dos quatro eixos físicos;
3. verificar que o subespaço físico de quatro direções é irredutível após a
   média;
4. verificar que eventuais anisotropias Hermitiano--Bismut entram como
   refinamentos de aplicabilidade, não como novo ajuste de \(\alpha\).

## Status

Auditoria de aplicabilidade. Não reabre a cadeia estrutural de Q37.
