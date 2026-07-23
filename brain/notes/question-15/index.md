---
title: Question 15 - f, S_I and rho
status: closed
source: questoes/q15/questao_15.md
updated: 2026-07-16
---

# Question 15 - f, S_I and rho

Q15 asks how the complex field $f$, osmotic action $S_I$ and density $\rho$
relate.

The fundamental relation is

$$
f
=
-\frac{S_I-iS_R}{\hbar}
=
-\frac{S_I}{\hbar}
+i\frac{S_R}{\hbar}.
$$

Therefore

$$
\operatorname{Re}f=-\frac{S_I}{\hbar},
\qquad
\operatorname{Im}f=\frac{S_R}{\hbar}.
$$

The positive density is

$$
\rho
=
e^{S_I/\hbar}
=
e^{-(f+\bar f)/2}.
$$

Thus

$$
S_I=\hbar\ln\rho,
\qquad
f=-\ln\rho+i\frac{S_R}{\hbar}.
$$

The official measure is

$$
\mathcal U
=
\frac{\rho}{(4\pi z_\tau)^n}.
$$

## Positivity

Because the measure depends on $f+\bar f$, not on $f$ alone, the phase
$S_R$ does not spoil positivity:

$$
e^{-(f+\bar f)/2}=\rho>0.
$$

## Perelman functional

$S_I=\hbar\mathcal W$ is not a valid local identity. $S_I(x)$ is a local field,
whereas $\mathcal W[g,f,\tau]$ is a global functional. The correct local
identity is

$$
S_I(x)=\hbar\ln\rho(x)=-\hbar\,\operatorname{Re}f(x).
$$

## Status

Q15 is closed. It fixes the ontology of $f$, $S_I$, $\rho$ and $\mathcal U$,
and removes $S_I=\hbar\mathcal W$ as a local identity.

