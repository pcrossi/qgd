---
title: "Heat-kernel polarization and absence of the Landau pole"
---

# Heat-kernel polarization and absence of the Landau pole

This note separates two calculations that must not be confused:

1. the geometric loop of the phase of $f$, derived directly from the official Hessian;
2. the effective $U(1)$ translation used to formulate the Landau pole in the external perturbative language.

Neither constitutes fundamental renormalization by counterterms.

## 1. Geometric loop of the phase on the torus

In the bulk $M=\mathbb R^4\times T^4$, write

$$
f=f_*+i\chi,
\qquad
\bar f=f_*-i\chi.
$$

For constant real $f_*$, $\mathcal U=\mathcal U_*$ in the $\chi$ sector, and the second variation contains

$$
S_\chi^{(2)}
=\frac{Z_\chi}{2}
\int_M g^{MN}\partial_M\chi\partial_N\chi\,dV_g.
$$

With a bundled cycle

$$
ds^2
=h_{\mu\nu}dx^\mu dx^\nu
+R^2(dy+\kappa A_\mu dx^\mu)^2
+ds_{T^3}^2
$$

and decomposition $\chi=\sum_n\chi_ne^{iny}$, we obtain

$$
H_n[A]=-(\partial-iq_nA)^2+m_n^2,
\qquad
q_n=n\kappa,
\qquad
m_n^2=\frac{n^2}{R^2}+\lambda_\perp.
$$

The determinant of the real pair $n,-n$ is

$$
\Gamma_n^{(1)}[A]=\operatorname{Tr}\ln H_n[A].
$$

The bubble and the contact term $A^2|\chi_n|^2$ come from the same Hessian. The contact term is essential for Ward. With proper cutoff $s_0$,

$$
\Pi_{n,s_0}(Q^2)
=\frac{q_n^2}{16\pi^2}
\int_0^1dx\,(1-2x)^2
\left[
E_1(s_0m_n^2)
-E_1\!\left(s_0[m_n^2+x(1-x)Q^2]\right)
\right].
$$

Hence

$$
Q^\mu\Pi_{\mu\nu}^{(n)}=0,
\qquad
\Pi_{n,s_0}(\infty)
=\frac{q_n^2}{48\pi^2}E_1(s_0m_n^2)<\infty.
$$

This calculation satisfies the chain: official action--Hessian--operator--determinant--observable in the declared sector.

## 2. Effective comparison operator and covariant regularization

Let $L_A$ be a positive Laplace-type operator, covariant under $U(1)$. The one-loop functional regularized by the semigroup is

$$
\Gamma_\tau[A]
=\frac12\operatorname{Tr}
\int_\tau^\infty\frac{ds}{s}e^{-sL_A},
\qquad \tau>0.
$$

Since $L_{A^g}=g^{-1}L_Ag$, the regularization preserves Ward. The second variation around $A=0$ has the form

$$
\Pi_{\mu\nu}^{(\tau)}(q)
=(q_\mu q_\nu-q^2\delta_{\mu\nu})\Pi_\tau(q^2).
$$

## 3. Scalar comparison function

After Feynman parameterization and covariant Gaussian integration,

$$
\Pi_\tau(q^2)
=\frac{2\alpha_0}{\pi}
\int_0^1dx\,x(1-x)
\left[
E_1(\tau m^2)
-E_1\!\left(\tau[m^2+x(1-x)q_E^2]\right)
\right],
$$

where

$$
E_1(z)=\int_z^\infty\frac{e^{-u}}{u}\,du.
$$

At $q=0$ the two terms coincide, therefore

$$
\Pi_\tau(0)=0.
$$

This subtraction is the explicit form of the absence of photonic mass in the test.

## 4. Infrared limit

For $\tau q_E^2\ll1$, the difference of exponential integrals tends to the logarithm:

$$
\Pi_\tau(q^2)
\longrightarrow
\frac{2\alpha_0}{\pi}
\int_0^1dx\,x(1-x)
\ln\left(1+\frac{x(1-x)q_E^2}{m^2}\right).
$$

In the interval $m^2\ll q_E^2\ll\tau^{-1}$,

$$
\Pi_\tau(q^2)
=\frac{\alpha_0}{3\pi}\ln\frac{q_E^2}{m^2}
+\text{constant finite}+o(1).
$$

Thus, the external translation recovers the usual perturbative behavior before the geometric scale.

## 5. Ultraviolet saturation

For $q_E^2\to\infty$ and $0<x<1$,

$$
E_1\!\left(\tau[m^2+x(1-x)q_E^2]\right)\to0.
$$

Since

$$
\int_0^1x(1-x)\,dx=\frac16,
$$

it follows that

$$
\Pi_\tau(\infty)
=\frac{\alpha_0}{3\pi}E_1(\tau m^2).
$$

Defining solely for comparison

$$
\alpha_{\rm eff}(q^2)
=\frac{\alpha_0}{1-\Pi_\tau(q^2)},
$$

the ultraviolet limit is finite if

$$
\frac{\alpha_0}{3\pi}E_1(\tau m^2)<1.
$$

Under this condition,

$$
\alpha_{\rm eff}(\infty)
=\frac{\alpha_0}
{1-\frac{\alpha_0}{3\pi}E_1(\tau m^2)}
$$

and there is no physical pole in the smoothed sector.

## 6. What the proof does not use

The demonstration does not use the old postulated beta function

$$
-b_0\alpha^2+\gamma_C\alpha^3e^{-\Lambda_C^2/Q^2}.
$$

This expression had sign problems and did not derive the supposed fixed point. It is also not enough to say that the Bohm potential makes $r=0$ inaccessible. The closure arises from the covariant operator, the Ward identity, the calculation of $\Pi_\tau$, and its saturation.

## 7. Status

- geometric loop of the phase on the torus: derived from the official action;
- finiteness of $\Pi_\tau$ for $\tau>0$ in the effective translation: demonstrated;
- Ward and $\Pi_\tau(0)=0$: demonstrated;
- infrared recovery: demonstrated in the declared regime;
- absence of the pole: conditional on the spectral inequality;
- non-perturbative finiteness of the entire GDQ: not demonstrated by this test;
- extension to any background: requires the operator and the domain of that background.
