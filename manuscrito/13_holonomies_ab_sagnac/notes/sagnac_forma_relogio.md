---
title: "Sagnac como forma-relógio"
---

# Sagnac como forma-relógio

## Enunciado

O efeito Sagnac é a holonomia da forma de simultaneidade em um contorno
rotativo.

## Prova reduzida

Para rotação angular $\boldsymbol\Omega$:

$$
\mathbf v_{\rm rot}
=
\boldsymbol\Omega\times\mathbf r.
$$

A diferença temporal é:

$$
\Delta t_{\rm Sag}
=
\frac{2}{c^2}
\oint_\gamma
\left(
\boldsymbol\Omega\times\mathbf r
\right)\cdot d\mathbf r.
$$

Por Stokes:

$$
\oint_\gamma
\left(
\boldsymbol\Omega\times\mathbf r
\right)\cdot d\mathbf r
=
2\boldsymbol\Omega\cdot\mathbf A.
$$

Logo:

$$
\Delta t_{\rm Sag}
=
\frac{4\boldsymbol\Omega\cdot\mathbf A}{c^2}.
$$

O fator quatro possui duas origens separadas:

1. a circulação do campo rotacional fornece
   $2\boldsymbol\Omega\cdot\mathbf A$;
2. a diferença entre os dois sentidos de propagação fornece o segundo fator
   dois.

Essa composição é certificada em
[HolonomyPatchingStokes.lean](../../../formal/GDQ/HolonomyPatchingStokes.lean),
enquanto o cancelamento da fase comum e a inversão de sinal são certificados
em [SagnacHolonomy.lean](../../../formal/GDQ/SagnacHolonomy.lean).

A forma-relógio reduzida é:

$$
\Theta_t
=
dt
-
\frac{1}{c^2}
\left(
\boldsymbol\Omega\times\mathbf r
\right)\cdot d\mathbf r.
$$

## Alcance

$\boldsymbol\Omega$ pertence ao aparelho/contorno rotativo. Não é novo termo
da ação oficial.
