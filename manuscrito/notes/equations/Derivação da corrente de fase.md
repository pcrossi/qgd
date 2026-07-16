---
title: "Nota — Derivação da corrente de fase"
---

# Derivação da corrente de fase

Fixe temporariamente $g$, $\rho$, $z_\tau$ e o contorno. A parcela que depende
de $S_R$ é

$$
S_S
=\int_\gamma\int_M
\frac{\hbar}{\Lambda_C^2}
\frac{\tau}{\hbar^2}
\mathcal U\,
g^{\mu\bar\nu}
\partial_\mu S_R
\partial_{\bar\nu}S_R
\,dV_g\,
\frac{d\tau}{\tau}.
$$

Sua variação é

$$
\delta S_S
=\int_\gamma\int_M
\frac{2\tau}{\hbar\Lambda_C^2}
\mathcal U\,
g^{\mu\bar\nu}
\partial_\mu(\delta S_R)
\partial_{\bar\nu}S_R
\,dV_g\,
\frac{d\tau}{\tau},
$$

onde se tomou a parte real da contração Hermitiana. Integrando por partes,

$$
\delta S_S
=-\int_\gamma\int_M
\frac{2\tau}{\hbar\Lambda_C^2}
\delta S_R\,
\nabla_\mu
\left(
\mathcal U g^{\mu\bar\nu}
\partial_{\bar\nu}S_R
\right)
\,dV_g\,
\frac{d\tau}{\tau}
+\delta S_S\big|_{\partial M}.
$$

Para variações compactamente suportadas no bulk,

$$
\boxed{
\nabla_\mu
\left(
\mathcal U g^{\mu\bar\nu}
\partial_{\bar\nu}S_R
\right)=0.
}
$$

O prefator constante pode ser incluído na definição da corrente sem alterar
sua divergência:

$$
J_S^\mu
=\frac{2\tau}{\hbar^2}
\mathcal U g^{\mu\bar\nu}
\partial_{\bar\nu}S_R.
$$

No bordo, o momento conjugado é

$$
\Pi_S
=n_\mu J_S^\mu.
$$

Fixar $S_R$, impor $\Pi_S=0$ ou acoplá-lo a uma corrente externa são três
problemas variacionais diferentes.
