---
title: "Questão 32 — memória curta"
status: structural-closed
updated: 2026-07-21
---

# Questão 32 — memória curta

## Enunciado preservado

Responder se o propagador modificado da GDQ pode ser obtido da ação oficial,
sem inserir um regulador ad hoc e sem gerar fantasmas ou polos artificiais.

## Resposta vigente

Sim, no setor estrutural declarado. A Hessiana de segunda variação contém um
fator de fluxo que deve ser separado do gerador do semigrupo:

$$
\mathcal O_{\rm Hess}^{(2)}=\tau L_{\rm GDQ}^{(2)}.
$$

O kernel correto é:

$$
e^{-\tau L_{\rm GDQ}^{(2)}}.
$$

No fundo plano, isso reproduz o fator gaussiano:

$$
e^{-\tau p_E^2}
=
e^{-p_E^2/\widehat\Lambda_\tau^2}.
$$

## Cuidados

Não usar a forma de dupla contagem $e^{-\tau^2L}$. Não declarar finitude em
todas as ordens a partir do setor plano. Não substituir a GDQ por QFT externa.

