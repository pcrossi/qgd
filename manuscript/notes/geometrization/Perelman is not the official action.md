---
title: "Perelman is not the official action"
---

# Perelman is not the official action

## Statement

Perelman's functional is used in GDQ as an auxiliary geometric matrix to organize the weighted measure, geometric entropy, flow, and stability. It does not replace the official physical action.

## Official action

The fundamental physical action remains:

$$
\mathcal S_{\rm GDQ}
=
\int_\gamma
\left[
\int_{\mathcal M_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left(
\tau\left(
\mathcal R
+g^{\mu\bar\nu}\partial_\mu f\,\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}
-n
\right)
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]
\frac{d\tau}{\tau}.
$$

Here, $\Lambda_C$ is the dimensionless cutoff number in coordinates normalized by the Cartan scale, and the restoration of physical units uses separate scales, such as $k_C=\ell_C^{-1}$ and $E_C=\hbar c k_C$.

## Auxiliary Perelman functional

Perelman's functional, in its usual geometric form, organizes expressions of the type:

$$
\mathcal F(g,\sigma)
=
\int_M
\left(
R+|\nabla\sigma|^2
\right)e^{-\sigma}\,dV_g.
$$

It also appears in entropic versions weighted by $\tau$. The formal similarity with the internal integrand of GDQ is deliberate: both structures measure curvature, logarithmic gradient of density, and entropic weight.

But GDQ contains additional data that are not mere details:

1. the complex field $f$;
2. the constitutive density $\rho=e^{-(f+\bar f)/2}$;
3. the real phase $S_R=\hbar(f-\bar f)/(2i)$;
4. the measure $\mathcal U=\rho/(4\pi z_\tau)^n$;
5. the causal boundary $\gamma$;
6. the Hermitian/Bismut connection when $H\neq0$;
7. the physical constraints and boundary conditions of the stomata.

Therefore, Perelman provides the geometric grammar of the flow, but it is not the physical action.

## Correct use

It is correct to use Perelman to:

- identify geometric monotonicity;
- study soliton stability;
- organize the weighted measure;
- interpret conjugate heat flows;
- construct auxiliary Lyapunov functionals;
- compare singularities and surgeries in factored three-dimensional sectors.

It is not correct to use Perelman to:

- change the official action;
- erase the phase $S_R$;
- replace the physical Hessian of GDQ;
- automatically declare the existence of material backgrounds;
- transport three-dimensional theorems to the entire 8D bulk without the sectorial factorization hypothesis.

## Consequence for the writing of the manuscript

When the text says that "Perelman enters", it should read:

> Perelman's entropic structure provides the auxiliary geometric matrix of GDQ.

It should not read:

> the physical action of GDQ has been replaced by Perelman's functional.

This distinction preserves the identity of the theory and avoids mixing a geometric tool with the fundamental variational principle.
