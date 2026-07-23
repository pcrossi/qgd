---
title: "Casimir como Hessiana de contorno"
---

# Casimir como Hessiana de contorno

Status: redução efetiva com contorno ideal.

## Hessiana efetiva

No limite plano:

$$
K_{\rm EM}^{\rm eff}
\sim
-\partial_t^2+c^2(-\Delta_\parallel-\partial_z^2).
$$

Com placas ideais:

$$
k_z=\frac{n\pi}{a}.
$$

As frequências são:

$$
\omega_{n,\mathbf k}
=
c\sqrt{k^2+\left(\frac{n\pi}{a}\right)^2}.
$$

## Determinante

A energia formal é:

$$
\frac{E}{A}
=
\frac{\hbar}{2}
\sum_n
\int\frac{d^2k}{(2\pi)^2}
\omega_{n,\mathbf k}.
$$

O observável é a diferença dependente de $a$ depois de subtrair a referência
sem placas e os termos locais de superfície. A parte universal é:

$$
\frac{\Delta E}{A}
=
-
\frac{\pi^2\hbar c}{720a^3}.
$$

## Derivação do coeficiente universal

Para o campo eletromagnético ideal há duas polarizações transversais. Assim:

$$
\frac{E}{A}
=
\frac{\hbar c}{2}
\cdot 2
\sum_{n=1}^{\infty}
\int
\frac{d^2k}{(2\pi)^2}
\sqrt{
k^2+
\left(\frac{n\pi}{a}\right)^2
}.
$$

Pela continuação dimensional:

$$
\int
\frac{d^2k}{(2\pi)^2}
\sqrt{k^2+m^2}
=
-
\frac{m^3}{6\pi}
$$

como parte finita regularizada. Portanto:

$$
\frac{\Delta E}{A}
=
-
\frac{\hbar c}{6\pi}
\left(
\frac{\pi}{a}
\right)^3
\sum_{n=1}^{\infty}n^3.
$$

A continuação espectral dá:

$$
\sum_{n=1}^{\infty}n^3
\to
\zeta(-3)
=
\frac{1}{120}.
$$

Logo:

$$
\frac{\Delta E}{A}
=
-
\frac{\pi^2\hbar c}{720a^3}.
$$

Essa etapa é uma técnica de extração da parte universal do determinante. Na
GDQ, ela não altera a ação oficial nem transforma a zeta em ontologia física.
O regulador separa a energia universal dependente de $a$ dos termos locais de
superfície.

Logo:

$$
P
=
-
\frac{\pi^2\hbar c}{240a^4}.
$$

## Placas reais

Para placas reais:

$$
\mathsf R_{\rm plate}
=
K_{YY}-K_{YI}K_{II}^{-1}K_{IY}.
$$

A força material real depende de $\mathsf R_{\rm plate}$, não apenas do
coeficiente universal ideal.
