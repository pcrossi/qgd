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

## $S_I$ local não é o funcional global $\mathcal W$

O campo $S_I$ é local:

$$
S_I=S_I(x,\tau).
$$

O funcional de Perelman, quando usado como referência geométrica, é global:

$$
\mathcal W=\mathcal W[g,F,\tau].
$$

Portanto a expressão

$$
S_I=\hbar\mathcal W
$$

não deve ser usada como identidade ponto a ponto. A relação local correta é

$$
\boxed{
S_I=\hbar\ln\rho=-\hbar\,\operatorname{Re}f.
}
$$

Se for necessário ligar uma quantidade global a uma quantidade local, deve-se
introduzir uma densidade integranda ou uma derivada funcional, por exemplo

$$
\mathcal W=\int_M\mathfrak w\,dV_g
$$

ou

$$
\Pi_I(x)=\frac{\delta\mathcal W}{\delta S_I(x)}.
$$

Mesmo nesses casos, $\mathfrak w$ ou $\Pi_I$ não são o funcional global
$\mathcal W$ inteiro.
