---
title: "Decomposição do campo f em densidade e fase"
tipo: derivacao
status: identidade-exata
---

# Decomposição do campo $f$ em densidade e fase

Se

$$
f=-\frac{S_I}{\hbar}+i\frac{S_R}{\hbar},
\qquad
\bar f=-\frac{S_I}{\hbar}-i\frac{S_R}{\hbar},
$$

então

$$
S_I=-\frac{\hbar}{2}(f+\bar f),
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f).
$$

Pela definição constitucional,

$$
\rho=e^{-(f+\bar f)/2}=e^{S_I/\hbar},
$$

e

$$
\Psi
=\sqrt\rho\,e^{iS_R/\hbar}
=e^{S_I/(2\hbar)}e^{iS_R/\hbar}.
$$

## Termo gradiente

Expandindo $\partial_\mu f\,\partial_{\bar\nu}\bar f$ e tomando a parte real
Hermitiana,

$$
\operatorname{Re}\left(
g^{\mu\bar\nu}
\partial_\mu f
\partial_{\bar\nu}\bar f
\right)
=
\frac1{\hbar^2}g^{\mu\bar\nu}
\left(
\partial_\mu S_I\partial_{\bar\nu}S_I
+\partial_\mu S_R\partial_{\bar\nu}S_R
\right).
$$

Os termos cruzados são imaginários antes da simetrização. A identidade mostra
como densidade e fase contribuem ao mesmo termo sem identificá-las.
