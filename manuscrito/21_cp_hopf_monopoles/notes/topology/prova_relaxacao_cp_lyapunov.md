---
title: "Prova de relaxação CP por Lyapunov"
---

# Prova de relaxação CP por Lyapunov

Defina:

$$
V(\theta)
=
\chi(1-\cos\theta),
\qquad
\chi>0.
$$

O fluxo reduzido é:

$$
\dot\theta
=
-\kappa
\frac{dV}{d\theta},
\qquad
\kappa>0.
$$

Como:

$$
\frac{dV}{d\theta}
=
\chi\sin\theta,
$$

temos:

$$
\dot\theta
=
-\kappa\chi\sin\theta.
$$

Agora:

$$
\frac{dV}{d\tau}
=
\frac{dV}{d\theta}
\dot\theta
=
-\kappa
\left(
\frac{dV}{d\theta}
\right)^2
\le0.
$$

Logo $V$ é uma função de Lyapunov.

Os pontos críticos são:

$$
\sin\theta=0
\quad\Rightarrow\quad
\theta=n\pi.
$$

A segunda derivada é:

$$
\frac{d^2V}{d\theta^2}
=
\chi\cos\theta.
$$

Portanto:

$$
\theta=0\pmod{2\pi}
$$

é mínimo estável, e:

$$
\theta=\pi\pmod{2\pi}
$$

é máximo instável.

Assim, para qualquer condição inicial fora do máximo instável:

$$
\theta(\tau)\to0\pmod{2\pi}.
$$

Esta prova usa apenas periodicidade, positividade de $\chi$ e fluxo gradiente
dissipativo do modo torsional.
