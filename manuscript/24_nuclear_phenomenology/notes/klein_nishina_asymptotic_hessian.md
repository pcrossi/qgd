---
title: "Note — Klein--Nishina as asymptotic reduction"
---

# Note — Klein--Nishina as asymptotic reduction

This note records the complete construction used in the main text. It is an asymptotic reduction of GDQ, not a replacement of the official action with QED.

## 1. Problem data

The process is:

$$
\gamma(k,\epsilon)+e(p,s)
\longrightarrow
\gamma(k',\epsilon')+e(p',s').
$$

In the asymptotically flat laboratory domain:

$$
p^2=p'^2=m_e^2c^2,
\qquad
k^2=k'^2=0,
\qquad
p+k=p'+k'.
$$

At the initial rest frame of the electronic soliton:

$$
p=(m_ec,\mathbf 0),
\qquad
x=\frac{E}{m_ec^2}.
$$

From Noether conservation:

$$
(p+k-k')^2=p'^2=m_e^2c^2.
$$

Canceling $p^2=m_e^2c^2$ and using $k^2=k'^2=0$ yields:

$$
2p\cdot(k-k')-2k\cdot k'=0.
$$

In the rest frame:

$$
p\cdot k=m_ecE,
\qquad
p\cdot k'=m_ecE',
\qquad
k\cdot k'=\frac{EE'}{c^2}(1-\cos\theta).
$$

Hence:

$$
m_ec(E-E')
=
\frac{EE'}{c^2}(1-\cos\theta).
$$

Dividing by $EE'$:

$$
\frac{1}{E'}-\frac{1}{E}
=
\frac{1-\cos\theta}{m_ec^2}.
$$

Therefore:

$$
\frac{E'}{E}
=
\frac{1}{1+x(1-\cos\theta)}.
$$

## 2. Expansion of the official action

In the asymptotic sector of the electron, the expansion of the official action yields:

$$
\mathcal S_{\rm GDQ}[\Phi_e^*+\delta\Phi]
=
\mathcal S_*
+
\frac12
\langle\delta\Phi,K_e^{\rm phys}\delta\Phi\rangle
+
\frac{1}{3!}\mathcal V_e^{(3)}[\delta\Phi^3]
+
\frac{1}{4!}\mathcal V_e^{(4)}[\delta\Phi^4]
+
\cdots.
$$

Here $\Phi_e^*$ is the stationary electronic background:

$$
\Phi_e^*
=
(g_e^*,J_e^*,H_e^*,f_e^*,\mathcal U_e^*).
$$

The physical operator is obtained by removing redundant gauge, longitudinal, and boundary modes:

$$
K_e^{\rm phys}
=
P_{\rm phys}
\operatorname{Hess}_{\Phi_e^*}\mathcal S_{\rm GDQ}
P_{\rm phys}.
$$

The photon channel is the massless transverse subspace:

$$
P_\gamma K_e^{\rm phys}P_\gamma
=
0
\quad
\text{in the asymptotic limit}.
$$

As a spectral operator:

$$
P_\gamma
=
\frac{1}{2\pi i}
\oint_{\mathcal C_\gamma}
(z-K_e^{\rm phys})^{-1}\,dz.
$$

The effective Compton vertex is:

$$
\mathcal V_{\gamma e\gamma}^{\rm eff}
=
P_\gamma
\mathcal V_e^{(3)}
G_e^{\rm phys}
\mathcal V_e^{(3)}
P_\gamma
+
P_\gamma\mathcal V_e^{(4)}P_\gamma.
$$

With:

$$
\mathcal V_e^{(3)}
=
\left.
\frac{\delta^3\mathcal S_{\rm GDQ}}
{\delta\Phi\,\delta\Phi\,\delta\Phi}
\right|_{\Phi_e^*},
\qquad
\mathcal V_e^{(4)}
=
\left.
\frac{\delta^4\mathcal S_{\rm GDQ}}
{\delta\Phi\,\delta\Phi\,\delta\Phi\,\delta\Phi}
\right|_{\Phi_e^*}.
$$

The two terms with the physical propagator generate the two causal branches:

$$
G_e^{\rm phys}(p+k)
\sim
\frac{1}{(p+k)^2-m_e^2c^2}
=
\frac{1}{2p\cdot k},
$$

$$
G_e^{\rm phys}(p-k')
\sim
\frac{1}{(p-k')^2-m_e^2c^2}
=
\frac{1}{-2p\cdot k'}.
$$

These are the $s$ and $u$ channels of the operational reduction.

## 3. Photonic projector and transversality

The Noether identity of the $U(1)_Q$ channel implies transversality:

$$
k_\mu\mathcal M^{\mu\nu}=0,
\qquad
k'_\nu\mathcal M^{\mu\nu}=0.
$$

In the flat limit, for an auxiliary vector $n^\mu$ with $k\cdot n\ne0$, the transverse projector is:

$$
\Pi_{\mu\nu}^{\perp}(k;n)
=
-\eta_{\mu\nu}
+
\frac{k_\mu n_\nu+n_\mu k_\nu}{k\cdot n}
-
\frac{n^2k_\mu k_\nu}{(k\cdot n)^2}.
$$

Since the terms proportional to $k_\mu$ or $k'_\nu$ are annihilated by Noether, physical observables can be calculated using only the transverse class:

$$
\sum_{\lambda=1}^{2}
\epsilon_\mu^{(\lambda)}(k)
\epsilon_\nu^{(\lambda)}(k)^*
=
\Pi_{\mu\nu}^{\perp}(k;n).
$$

## 4. Circulation/spin projector

The electronic spin in GDQ is the stable circulation/Hopf structure of the stoma. In the asymptotic Dirac--Bismut limit, the projector for an orientation is:

$$
P_s(p)
=
\frac12
(\slashed p+m_ec)
(1+\gamma^5\slashed S_s),
$$

with:

$$
S_s\cdot p=0,
\qquad
S_s^2=-1.
$$

For an unpolarized beam, the average of the two circulation states cancels the axial part:

$$
\frac12\sum_{s=\pm}P_s(p)
=
\frac12(\slashed p+m_ec).
$$

This is the asymptotic completeness of Hopf modes; it is not an additional postulate.

## 5. Unpolarized contraction

The reduced asymptotic amplitude has the form:

$$
\mathcal M
=
-e^2
\bar u(p')
\left[
\slashed\epsilon'^{\,*}
\frac{\slashed p+\slashed k+m_ec}{2p\cdot k}
\slashed\epsilon
+
\slashed\epsilon
\frac{\slashed p-\slashed k'+m_ec}{-2p\cdot k'}
\slashed\epsilon'^{\,*}
\right]
u(p).
$$

The observable quantity is:

$$
\overline{|\mathcal M|^2}
=
\frac12
\sum_{s,s'}
\frac12
\sum_{\lambda,\lambda'}
|\mathcal M|^2.
$$

With the projectors, this becomes the contraction:

$$
\overline{|\mathcal M|^2}
=
\frac{e^4}{4}
\operatorname{Tr}
\left[
(\slashed p'+m_ec)
\mathcal A_{\mu\nu}
(\slashed p+m_ec)
\overline{\mathcal A}_{\rho\sigma}
\right]
\Pi_\perp^{\mu\rho}(k')
\Pi_\perp^{\nu\sigma}(k),
$$

where:

$$
\mathcal A_{\mu\nu}
=
\gamma_\mu
\frac{\slashed p+\slashed k+m_ec}{2p\cdot k}
\gamma_\nu
+
\gamma_\nu
\frac{\slashed p-\slashed k'+m_ec}{-2p\cdot k'}
\gamma_\mu.
$$

Using:

$$
p+k=p'+k',
\qquad
p^2=p'^2=m_e^2c^2,
\qquad
k^2=k'^2=0,
$$

and removing the longitudinal components using physical projectors, the reduced angular part is:

$$
T_{\rm KN}
=
\frac{E'}{E}
+
\frac{E}{E'}
-
\sin^2\theta.
$$

## 6. Flux normalization

The cross section is the ratio between the scattered flux per solid angle and the incident flux:

$$
\frac{d\sigma}{d\Omega}
=
\frac{d\Phi_{\rm out}/d\Omega}{\Phi_{\rm in}}.
$$

In GDQ, the flux is the reconstructed current:

$$
J^\mu_{\rm GDQ}
=
\rho v^\mu.
$$

Integrating the Noether conservation yields the kinematic Jacobian:

$$
\left(\frac{E'}{E}\right)^2.
$$

The asymptotic prefactor is:

$$
r_e^2
=
\alpha^2
\left(\frac{\hbar}{m_ec}\right)^2.
$$

In this reduction, $\alpha$ and $m_e$ enter as quantities already inherited from geometry in previous chapters. The strongest metrological closure is to recalculate the same prefactor directly from $\mathcal V_{\gamma e\gamma}^{\rm eff}$ and the fluxes of the 8D background.

Thus:

$$
\frac{d\sigma}{d\Omega}
=
\frac{r_e^2}{2}
\left(\frac{E'}{E}\right)^2
\left(
\frac{E'}{E}
+
\frac{E}{E'}
-
\sin^2\theta
\right).
$$

## 7. Total cross section

Integrating over the solid angle yields the total formula:

$$
\sigma_{\rm KN}(x)
=
2\pi r_e^2
\left[
\frac{1+x}{x^3}
\left(
\frac{2x(1+x)}{1+2x}
-
\ln(1+2x)
\right)
+
\frac{\ln(1+2x)}{2x}
-
\frac{1+3x}{(1+2x)^2}
\right].
$$

In the limit $x\to0$:

$$
\sigma_{\rm KN}
\longrightarrow
\sigma_T
=
\frac{8\pi}{3}r_e^2.
$$

For numerical evaluation at very low energy, the stable expansion of the same total expression is used:

$$
\frac{\sigma_{\rm KN}}{\sigma_T}
=
1-2x+\frac{26}{5}x^2+O(x^3).
$$

The script [[../scripts/total_and_flux_klein_nishina.py]] verifies the equality between the angular numerical integration and the analytical total expression.

## 8. Status

What is closed in this note:

1. Compton kinematics via Noether;
2. $s/u$ channels as branches of the physical propagator;
3. spin/polarization sum as completeness of projectors in the asymptotic reduction;
4. flux normalization and Thomson limit;
5. angular and total numerical comparison.

What remains conditional:

1. constructing $P_\gamma$ directly in the 8D electronic background;
2. constructing $P_s$ directly from the Hopf/circulation operator of the Hessian;
3. evaluating $\mathcal V_{\gamma e\gamma}^{\rm eff}$ via the official action without passing through the asymptotic form;
4. extracting $r_e^2$ via the complete GDQ flux, not just the reduced form.
