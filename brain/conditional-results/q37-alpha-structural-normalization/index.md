---
title: Q37 structural alpha normalization
status: conditionally-closed-einstein-isotropic-class
source: questoes/q37/questao_37.md
updated: 2026-07-17
---

# Q37 structural alpha normalization

## Enunciado

$\alpha$ é a normalização efetiva do canal eletromagnético primitivo $U(1)_Q$,
não um número derivado por análise dimensional simples.

## Fórmula estrutural

$$
Z_Q^E
=
\frac{\hbar}{\Lambda_C^2}
\mathfrak P_\gamma
\left[
\tau\int_K\mathcal U_*\lVert\xi_Q\rVert^2dV_{q_*}
\right]
+\Delta Z_Q^E.
$$

Com:

$$
\alpha_E
=
\frac{(\mathbf q_{\min}^Tv_\gamma)^2}
{4\pi\hbar c\,v_\gamma^T\mathbf Z v_\gamma}.
$$

## Origem numérica cosmológica

A origem numérica adotada no estado vigente é a média cosmológica de Einstein:

$$
\alpha_E^{\rm mean}
=
\frac{9}{8\pi^4}
\left(
\frac{\pi^5}{1920}
\right)^{1/4}.
$$

Numericamente:

$$
(\alpha_E^{\rm mean})^{-1}
=
137{,}036082448\ldots
$$

Essa fórmula não usa CODATA como entrada. Ela depende do ensemble isotrópico
de Einstein, da câmara fundamental \(W(D_5)\), da medida de Haar na seção
física real de dimensão quatro e do autovetor Hopf axial coerente.

O loop de 2026-07-17 registrou em
`questoes/q37/associados/fechamento_alpha_hessiana_loop.md`:

1. \(1920=|W(D_5)|\) é válido como peso da órbita cosmológica completa quando
   o background inteiro é transportado por pullback;
2. a raiz quarta é a média geométrica do tensor de complacência nas quatro
   direções físicas;
3. o fator \(9/(8\pi^4)\) é obtido como contração da Hessiana média/corrente
   simplética no setor axial coerente: por Schur,
   \(K_{\rm phys}|_{\mathscr H^{(4)}}=\lambda_E\mathbf 1_4\), de modo que
   \(K_{\rm phys}^{-1}\) cancela na razão do projetor; resta
   \(\pi^{-4}\langle(n\cdot u)^4\rangle_{S^3}3^2
   =\pi^{-4}(1/8)9\).

Pelos lemas da ponte global--local, se a normalização do canal fotônico é
transportada sem fuga,

$$
\alpha_{\rm lab}=\alpha_E^{\rm mean}.
$$

## Status

Fechada condicionalmente na classe de Einstein isotrópica:

$$
\alpha_E^{\rm mean}=\alpha_E[Z_Q^E].
$$

A condição remanescente é auditar a aplicabilidade dessa classe ao background
global real, não encontrar ou ajustar novamente o número.
