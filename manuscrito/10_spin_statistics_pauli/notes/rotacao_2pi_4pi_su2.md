---
title: "Rotação de 2pi e 4pi em SU(2)"
---

# Rotação de $2\pi$ e $4\pi$ em $SU(2)$

## Enunciado

Na representação spinorial espacial:

$$
U(\theta)
=
\exp\left(
-i\frac{\theta}{2}\mathbf n\cdot\boldsymbol\sigma
\right),
$$

temos:

$$
U(2\pi)=-I,
\qquad
U(4\pi)=I.
$$

## Prova

Para vetor unitário $\mathbf n$:

$$
(\mathbf n\cdot\boldsymbol\sigma)^2=I.
$$

Logo:

$$
\exp(-i a\,\mathbf n\cdot\boldsymbol\sigma)
=
\cos a\,I
-i\sin a\,\mathbf n\cdot\boldsymbol\sigma.
$$

Tomando $a=\theta/2$:

$$
U(\theta)
=
\cos\frac\theta2\,I
-i\sin\frac\theta2\,\mathbf n\cdot\boldsymbol\sigma.
$$

Para $\theta=2\pi$:

$$
U(2\pi)
=
\cos\pi\,I
-i\sin\pi\,\mathbf n\cdot\boldsymbol\sigma
=
-I.
$$

Para $\theta=4\pi$:

$$
U(4\pi)
=
\cos2\pi\,I
-i\sin2\pi\,\mathbf n\cdot\boldsymbol\sigma
=
I.
$$

## Alcance

Essa é a realização matemática da meia-volta spinorial. A GDQ interpreta essa
estrutura por Hopf, circulação e torção, mas o sinal vem do recobrimento duplo
$SU(2)\to SO(3)$.
