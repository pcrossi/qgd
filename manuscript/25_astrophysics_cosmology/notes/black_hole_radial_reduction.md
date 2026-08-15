---
title: "Note — Radial reduction of the regular black hole"
---

# Note — Radial reduction of the regular black hole

This note records the construction that transforms the idea of a regular core into a testable variational reduction. It does not replace the complete 8D covariant saddle of the official action; it is the smallest radial reduction that preserves density, Bohm stiffness, and Bismut torsion.

## 1. Physical variable

The constitutive density of GDQ is:

$$
\rho=e^{-f_R}.
$$

In the radial sector we use:

$$
u(r)=\sqrt\rho.
$$

The choice of $u$ is not an external quantum mechanics convention. It merely makes explicit the amplitude stiffness that already appears when the official action is written in density variables.

## 2. Reduced functional

The minimal radial functional tested was:

$$
E[u,\phi]
=
\frac{1}{2}\int|\nabla u|^2\,dV
+
\frac{\lambda_T}{2}\int u^4\,dV
+
\frac{1}{2}\int\phi u^2\,dV.
$$

The three terms represent, respectively:

1. amplitude/Bohm stiffness;
2. effective torsional repulsion;
3. reduced gravitational geometric feedback.

The variable $\phi$ satisfies:

$$
\Delta\phi=u^2.
$$

With normalization:

$$
\int u^2\,dV=1,
$$

we introduce the multiplier $\mu$ and obtain:

$$
-\frac{1}{2}\Delta u
+
(\phi+\lambda_Tu^2)u
=
\mu u.
$$

In spherical symmetry:

$$
u'=v,
$$

$$
v'
=
2(\phi+\lambda_Tu^2-\mu)u
-\frac{2}{r}v,
$$

$$
\phi'=\frac{M(r)}{r^2},
\qquad
M'=r^2u^2.
$$

The conditions used were:

$$
u'(0)=0,
\qquad
M(0)=0,
\qquad
u(R)=0,
\qquad
M(R)=1,
\qquad
\phi(R)=-\frac{1}{R}.
$$

## 3. Regular core

The reduced solution returns:

$$
\mu=-1.067957044153\times10^{-1}.
$$

At the center:

$$
M(r)\sim r^{2.99999076}.
$$

This result is the essential check. If:

$$
M(r)=m_3r^3+O(r^5),
$$

then:

$$
A(r)=1-\frac{2\eta M(r)}{r}
=
1-2\eta m_3r^2+O(r^4).
$$

Therefore, the center is regular, of effective de Sitter type, and not Schwarzschild singular.

## 4. Compactness and horizons

The parameter:

$$
\eta=\frac{GM_{\rm ADM}}{c^2R_0}
$$

is boundary ADM/compactness data of the solution. It is not a free constant of the action.

The horizon condition is:

$$
A(r_H)=0.
$$

Since:

$$
A(r)=1-\frac{2\eta M_{\rm red}(r)}{r},
$$

the threshold is:

$$
\eta_{\rm crit}
=
\min_r\frac{r}{2M_{\rm red}(r)}.
$$

Numerically:

$$
\eta_{\rm crit}=5.188522012681.
$$

For $\eta=8$, there emerge:

$$
r_{H,1}=4.222352820613,
\qquad
r_{H,2}=15.95712272799.
$$

## 5. Effective reconstruction by conservation

We write:

$$
g_{tt}=-A(r)e^{2\Phi(r)}.
$$

Defining:

$$
\nu'
=
\partial_r\log\sqrt{-g_{tt}}
=
\Phi'+\frac{A'}{2A},
$$

the effective radial conservation yields:

$$
\nu'
=
\frac{m+4\pi r^3p_r}{r^2A}.
$$

Therefore:

$$
\Phi'
=
\frac{m+4\pi r^3p_r}{r^2A}
-
\frac{A'}{2A}.
$$

In the tested reduction:

$$
p_r
=
-\epsilon+\frac{(u')^2}{8\pi}.
$$

The tangential component is reconstructed by:

$$
p_t
=
p_r
+
\frac{r}{2}
\left[
p_r'
+
(\epsilon+p_r)
\left[
\Phi'+\frac{A'}{2A}
\right]
\right].
$$

With $\eta=8$ and $\lambda_T=3$, we obtained:

$$
\epsilon_{\rm core}
=
9.934478711421\times10^{-3},
$$

$$
p_{r,\rm core}
=
-9.934477941512\times10^{-3},
$$

$$
p_{t,\rm core}
=
-9.934158191133\times10^{-3}.
$$

The comparison between metric $p_r$ and input $p_r$ gave:

$$
\max_{\rm core}|p_r^{\rm metric}-p_r^{\rm input}|
=
2.506468990693\times10^{-12}.
$$

The conservation residue was:

$$
{\rm RMS}_{\rm core}
=
2.104757829586\times10^{-16},
$$

and on the static patches:

$$
{\rm RMS}_{|A|>5\times10^{-2}}
=
9.997320016076\times10^{-18}.
$$

## 6. Energy conditions

In the core:

$$
\epsilon+p_r
\simeq
0,
$$

$$
\epsilon+p_t
\simeq
3.205202875438\times10^{-7},
$$

and:

$$
\epsilon+p_r+2p_t
=
-1.986831561236\times10^{-2}.
$$

Thus, NEC/WEC are saturated and SEC is violated. This violation is necessary to escape the classical singularity theorems; in GDQ it comes from the geometric pressure of density, Bohm, and torsion, not from external exotic matter.
