---
title: "Nelson variable diffusion in GDQ"
---

# Nelson variable diffusion in GDQ

This note records the canonical derivation of variable Nelson diffusion in GDQ. It does not alter the official action: it describes the stochastic reduction on the physical sheet after the global--local reconstruction.

## 1. Data and domain

Let $(\Sigma,h)$ be a Riemannian spatial sheet whose metric is kept fixed during the local stochastic step, and let $\rho>0$ be a normalized density with respect to $dV_h$. If $h$ depends explicitly on $t$, the conservation must also include $\partial_t dV_h$; this contribution cannot be hidden in the drift. We define

$$
\nu_0=\frac{\hbar}{2m_0},
\qquad
\Omega(x,t)=\frac{m(x,t)}{m_0}>0.
$$

We define

$$
D^{ij}(x,t)=\nu_0\Omega^{-1}(x,t)h^{ij}(x).
$$

The forward Itô process is

$$
dX_t^i=b_+^i\,dt+\sigma^i{}_a\,dW_t^a,
\qquad
\sigma^i{}_a\sigma^j{}_a=2D^{ij}.
$$

## 2. Generator and adjoint

For a smooth test function $\varphi$, the forward generator is

$$
\mathcal L_+\varphi
=b_+^i\nabla_i\varphi+D^{ij}\nabla_i\nabla_j\varphi.
$$

The adjoint with respect to $dV_h$ yields

$$
\partial_t\rho
= \mathcal L_+^*\rho
=-\nabla_i(b_+^i\rho)
+\nabla_i\nabla_j(D^{ij}\rho).
$$

Substituting $D^{ij}=\nu_0\Omega^{-1}h^{ij}$ and using metric compatibility,

$$
\partial_t\rho
=-\nabla_i(b_+^i\rho)
+\nu_0\Delta_h(\Omega^{-1}\rho).
$$

The product rule gives

$$
\begin{aligned}
\Delta_h(\Omega^{-1}\rho)={}&
\Omega^{-1}\Delta_h\rho
+2\nabla^i\Omega^{-1}\nabla_i\rho\\
&+\rho\,\Delta_h\Omega^{-1}.
\end{aligned}
$$

This is the precise origin of the Itô terms omitted when variable diffusion is incorrectly treated as constant.

## 3. Backward evolution and osmotic velocity

The compatible backward description uses a drift $b_-^i$. Equating the two Fokker--Planck equations for the same density and imposing a unique physical current, without adding an independent solenoidal part, one obtains

$$
b_+^i-b_-^i
=2D^{ij}\nabla_j\ln\rho+2\nabla_jD^{ij}.
$$

Defining

$$
v^i=\frac{b_+^i+b_-^i}{2},
\qquad
u^i=\frac{b_+^i-b_-^i}{2},
$$

it follows that, in the isotropic case,

$$
u^i
=\nu_0\Omega^{-1}\nabla^i\ln\rho
+\nu_0\nabla^i\Omega^{-1}.
$$

Since

$$
\nabla^i\Omega^{-1}
=-\Omega^{-1}\nabla^i\ln\Omega,
$$

we have

$$
\boxed{
u^i
=\nu_0\Omega^{-1}
\left(\nabla^i\ln\rho-\nabla^i\ln\Omega\right).
}
$$

## 4. Homogeneous limit

If $\Omega$ is constant in a mass sector $m$,

$$
\nabla\Omega=0,
\qquad
\nu_0\Omega^{-1}=\frac{\hbar}{2m}.
$$

Therefore,

$$
\partial_t\rho
=-\nabla_i(b_+^i\rho)
+\frac{\hbar}{2m}\Delta_h\rho,
$$

and

$$
u^i=\frac{\hbar}{2m}\nabla^i\ln\rho.
$$

Thus, Nelson is recovered exactly in the homogeneous sector. What remains conditional is not the stochastic calculation, but the derivation of $\Omega[g,f,\bar f]$ and the scale $m_0$ for each material background from the official action.

## 5. Classification

- Itô and Fokker--Planck equations: exact derivation in the physical reduction;
- corrections by $\nabla\Omega$: exact derivation;
- recovery of $\hbar/(2m)$ for constant $\Omega$: exact identity;
- geometric origin of $\Omega$ and selection of $m_0$: subsequent solitonic and spectral problem.
