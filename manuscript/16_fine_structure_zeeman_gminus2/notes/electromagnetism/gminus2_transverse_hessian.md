---
title: "Transverse Hessian of g-2"
---

# Transverse Hessian of $g-2$

The constrained functional is:

$$
\mathscr I[\Phi,\lambda;B]
=
\mathcal S_{\rm GDQ}[\Phi]
-B\,M[\Phi]
-\lambda
\left(
\mathcal C[\Phi]-C_\ell
\right).
$$

Linearizing:

$$
\mathcal C[\Phi_\ell+\eta]
=
C_\ell+\langle c_\ell,\eta\rangle+O(\eta^2),
$$

$$
M[\Phi_\ell+\eta]
=
M[\Phi_\ell]+\langle m_\ell,\eta\rangle+O(\eta^2).
$$

The constrained physical Hessian is:

$$
H_{C,\ell}
=
P_C^\dagger
\left.
\delta^2\mathcal S_{\rm GDQ}
\right|_{\Phi_\ell}
P_C.
$$

Decomposing:

$$
m_\ell
=
\gamma_{0,\ell}c_\ell+m_{\perp,\ell}.
$$

Then:

$$
a_\ell
=
\frac{1}{\gamma_{0,\ell}}
\frac{
\langle c_\ell,H_{C,\ell}^{+}m_{\perp,\ell}\rangle
}{
\langle c_\ell,H_{C,\ell}^{+}c_\ell\rangle
}.
$$

This equation is the operational point of the chapter. It shows exactly what is missing for metrology: to calculate $H_{C,\ell}$ and $m_{\perp,\ell}$ in the real background, without choosing coefficients based on the experimental target.
