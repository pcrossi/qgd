---
title: "Note — Derivation of the phase current"
---

# Derivation of the phase current

Temporarily fix $g$, $\rho$, $z_\tau$, and the contour. The portion that depends on $S_R$ is:

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

Its variation is:

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

where the real part of the Hermitian contraction was taken. Integrating by parts,

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

For compactly supported variations in the bulk,

$$
\boxed{
\nabla_\mu
\left(
\mathcal U g^{\mu\bar\nu}
\partial_{\bar\nu}S_R
\right)=0.
}
$$

The constant prefactor can be included in the definition of the current without altering its divergence:

$$
J_S^\mu
=\frac{2\tau}{\hbar^2}
\mathcal U g^{\mu\bar\nu}
\partial_{\bar\nu}S_R.
$$

On the boundary, the conjugate momentum is:

$$
\Pi_S
=n_\mu J_S^\mu.
$$

Fixing $S_R$, imposing $\Pi_S=0$, or coupling it to an external current are three different variational problems.
