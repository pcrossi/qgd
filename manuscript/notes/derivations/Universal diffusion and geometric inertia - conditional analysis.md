---
title: "Universal diffusion and geometric inertia - conditional analysis"
type: derivation
status: stochastic-derivation-with-conditional-geometric-origin
---

# Universal diffusion and geometric inertia - conditional analysis

## 1. Scale hypothesis

The original proposal introduces a universal diffusion

$$
\nu_0=\frac{\hbar}{2m_0}
$$

and a positive geometric factor

$$
\Omega=\frac{m}{m_0}.
$$

If the local generator contains the effective coefficient

$$
\nu_{\rm eff}=\frac{\nu_0}{\Omega},
$$

then, algebraically,

$$
\nu_{\rm eff}
=\frac{\hbar}{2m_0}\frac{m_0}{m}
=\frac{\hbar}{2m}.
$$

This identity shows that the $1/m$ dependence can be represented by a geometric scale. It does not demonstrate that the official action produces $\Omega$.

## 2. Necessary correction for variable diffusion

For the Itô process

$$
dX_t=b\,dt+\sqrt{2D(X_t,t)}\,dW_t,
$$

the Fokker--Planck equation is

$$
\partial_t\rho
=-\nabla\cdot(b\rho)+\Delta(D\rho),
$$

and not simply

$$
\partial_t\rho
=-\nabla\cdot(b\rho)+D\Delta\rho.
$$

Since

$$
\Delta(D\rho)
=D\Delta\rho
+2\nabla D\cdot\nabla\rho
+\rho\Delta D,
$$

a function $D=\nu_0\Omega^{-1}$ generates additional terms with derivatives of $\Omega$. The original text omitted them.

An alternative geometric formulation can choose the generator in divergence form,

$$
\mathcal L\rho=\nabla\cdot(D\nabla\rho),
$$

but this corresponds to a specific choice of drift, measure, and stochastic convention. This choice needs to be derived or declared.

## 3. Osmotic velocity and retrieval of Nelson

The two compatible forward and backward equations yield

$$
u^i
=\nu_0\Omega^{-1}
\left(\nabla^i\ln\rho-\nabla^i\ln\Omega\right).
$$

Therefore, the variable stochastic dynamics is closed without artificially cancelling $\nabla\Omega$. In the sector where $\Omega$ is constant,

$$
u^i=\frac{\hbar}{2m}\nabla^i\ln\rho,
$$

and Nelson is recovered exactly. The detailed covariant derivation is in [[Nelson variable diffusion in GDQ]].

## 4. What is demonstrated and what remains open

Algebraically demonstrated under the scale hypothesis:

$$
\nu_0\Omega^{-1}=\frac{\hbar}{2m}.
$$

Not yet demonstrated by stochastic reduction:

1. that $m/m_0$ is exactly the geometric factor $\Omega$;
2. that $m_0$ is selected without calibration by the stationary background;
3. that the official action produces this generator for every background;
4. that the stability of the soliton uniquely determines its inertial mass.

Therefore, the calculation of variable diffusion is demonstrated; the geometric emergence of masses remains a distinct solitonic step.
