---
title: "Detector DtN/Schur and visibility"
---

# Detector DtN/Schur and visibility

## Statement

In a reduced linear detector:

$$
K_{\rm det}
=
-\partial_s^2+\lambda^2,
\qquad
s\in[0,L],
$$

with $\varphi(0)=\varphi_0$ and $\varphi(L)=0$, the DtN impedance is:

$$
\textsf{R}_{\rm det}=\lambda\coth(\lambda L).
$$

## Proof

The stationary solution of:

$$
(-\partial_s^2+\lambda^2)\varphi=0
$$

with $\varphi(0)=\varphi_0$ and $\varphi(L)=0$ is:

$$
\varphi(s)=
\varphi_0
\frac{\sinh(\lambda(L-s))}{\sinh(\lambda L)}.
$$

Differentiating:

$$
\partial_s\varphi(0)
=
-\lambda\coth(\lambda L)\varphi_0.
$$

The normal outward flux is:

$$
-\partial_s\varphi(0)
=
\lambda\coth(\lambda L)\varphi_0.
$$

Thus:

$$
\textsf{R}_{\rm det}=\lambda\coth(\lambda L).
$$

## Visibility

If the detector distinguishes paths by $\Delta\Phi_\partial$, then:

$$
\Gamma_{\rm det}
=
\frac12
\langle
\Delta\Phi_\partial,
\textsf{R}_{\rm det}
\Delta\Phi_\partial
\rangle.
$$

The coherence coefficient is:

$$
\mathcal C_{\rm det}=e^{-\Gamma_{\rm det}}.
$$

For two normalized path-markers $w_1$ and $w_2$ on the boundary:

$$
\Delta\Phi_\partial
=
\zeta_{\rm det}(w_1-w_2),
$$

with:

$$
\int_{\partial\Omega}(w_1-w_2)^2d\Sigma=C_{\rm path}.
$$

Then:

$$
\Gamma_{\rm det}
=
\frac12
\zeta_{\rm det}^2
C_{\rm path}
\lambda\coth(\lambda L).
$$

For a primitive marker:

$$
C_{\rm path}=1.
$$

The observed pattern is:

$$
\rho_{\rm det}
=
I_1+I_2
+
2e^{-\Gamma_{\rm det}}
\sqrt{I_1I_2}\cos\Delta\phi.
$$

## Preserved numerical validation

In the self-contained reduced test of the chapter, the following were used:

$$
\lambda_{\rm det}=1.1,
\qquad
L=1,
\qquad
C_{\rm path}=1.
$$

Thus:

$$
\textsf{R}_{\rm det}
=
\lambda_{\rm det}\coth(\lambda_{\rm det}L)
=
1.37414284103.
$$

For $N=8000$:

| $\zeta_{\rm det}$ | $\Gamma_{\rm det}$ | $e^{-\Gamma_{\rm det}}$ | raw central visibility |
|---:|---:|---:|---:|
| $0$ | $0$ | $1$ | $0.987400675$ |
| $0.5$ | $0.171767855$ | $0.842174657$ | $0.893408543$ |
| $1.25$ | $1.073549095$ | $0.341793305$ | $0.547559863$ |
| $2.5$ | $4.294196378$ | $0.013647535$ | $0.270891364$ |

Mesh refinement from $N=1000$ to $N=8000$ preserves $\Gamma_{\rm det}$ and shows stability of the raw central visibility.

The observable directly controlled by the reduced GDQ is $e^{-\Gamma_{\rm det}}$, not the raw visibility, since the latter also contains the incoherent envelope $I_1+I_2$.

## Comparison with the standard operational description

The standard coherent limit corresponds to:

$$
\Gamma_{\rm det}=0.
$$

The standard limit with a perfect path-marker corresponds to:

$$
\Gamma_{\rm det}\gg1.
$$

The reduced GDQ provides the intermediate curve:

$$
\mathcal C_{\rm det}(\zeta_{\rm det})
=
\exp\left[
-\frac12
\zeta_{\rm det}^2
C_{\rm path}
\lambda_{\rm det}\coth(\lambda_{\rm det}L)
\right].
$$

This curve is the distinctive element of the treatment: one does not change the official action; the loss of coherence is calculated via the interface impedance of the apparatus.

## Scope

This is a structural closure for a reduced linear detector. A real detector requires calculating $\lambda$, $L$, and couplings from the apparatus.
