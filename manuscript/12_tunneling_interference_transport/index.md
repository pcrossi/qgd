---
title: "12. Tunneling, double slit, delayed choice and transport"
---

# 12. Tunneling, double slit, delayed choice and transport

This chapter addresses phenomena that seem paradoxical when described as point particles traversing a rigid space: tunneling, double slit, loss of fringes by a detector, and delayed choice.

In GDQ, the correct interpretation is via density, phase, boundary, and transport. The official action is not altered. Barriers, slits, detectors, and recombiners enter as external apparatus data:

$$
J_{\rm app}^{\rm classical}
\to
\delta\Phi_{\rm app}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\mathsf R_{\rm app}
\to
\text{transport response}
\to
\text{readout}.
$$

## Outline

- [[12.1 - Tunneling and the Hartman paradox]]
- [[12.2 - Reduced geometric model of the barrier]]
- [[12.3 - Double slit as a boundary value problem]]
- [[12.4 - Density, phase and Bohm pressure in the fringes]]
- [[12.5 - Detector as interface impedance]]
- [[12.6 - Loss of visibility via Schur complement]]
- [[12.7 - Delayed choice without signaling to the past]]
- [[12.8 - What has been demonstrated and what is apparatus metrology]]

## Central Result

The reduced density of two slits with a detector can be written as:

$$
\rho_{\rm det}
=
I_1+I_2
+
2e^{-\Gamma_{\rm det}}
\sqrt{I_1I_2}
\cos\Delta\phi.
$$

The coherence factor is not postulated:

$$
\mathcal C_{\rm det}=e^{-\Gamma_{\rm det}}.
$$

It comes from the boundary impedance of the detector:

$$
\Gamma_{\rm det}
=
\frac12
\left\langle
\Delta\Phi_\partial,
\mathsf R_{\rm det}
\Delta\Phi_\partial
\right\rangle,
$$

with:

$$
\mathsf R_{\rm det}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

For delayed choice, what changes is:

$$
\mathsf R_{\rm old}\to\mathsf R_{\rm new}.
$$

There is no physical signal to the past. There is a boundary change effectively realized before final registration.

## Status of the Result

| Block | Status | Observation |
|---|---|---|
| Hartman via saturated proper distance | Conditional reduced theorem | $g_{xx}\propto\rho$ holds in the declared evanescent channel, not universally. |
| Double slit without detector | Closed in the flat Madelung sector | Recovers known operational interference. |
| Nodes as Bohm barrier | Effective reduction | Geometric manifestation of the zeros of $\rho$. |
| Linear detector | Structurally closed | DtN/Schur in a reduced channel. |
| Loss of visibility | Conditionally closed | $\exp(-\Gamma_{\rm det})$. |
| Delayed choice | Structurally closed | Boundary/transport, without physical retrocausality. |
| Complete real detector | Metrological program | Requires material, geometry and full Hessian. |

In the validated reduced case for a double slit with a detector:

$$
\lambda_{\rm det}=1.1,
\qquad
L=1,
\qquad
\mathsf R_{\rm det}=1.37414284103,
$$

and the coherence decays from $1$ to $0.013647535$ when $\zeta_{\rm det}$ goes from $0$ to $2.5$.

## Editorial Control

- [[operational_checklist|Operational checklist of the chapter]]
- [[notes/proofs_lemmas_definitions|Associated proofs, lemmas and definitions]]
- [[notes/gdq_construction_transport_interference|GDQ construction of transport and interference]]
- [[notes/hartman_one_dimensional_conformal_ansatz|Hartman as a one-dimensional conformal ansatz]]
- [[notes/detector_dtn_schur_visibility|DtN/Schur detector and visibility]]
- [[notes/electro_optic_mzi_delayed_choice|EO-MZI interferometer and delayed choice]]
- [[notes/delayed_choice_boundary_not_retrocausal|Delayed choice as boundary]]
- [[scripts/README|Chapter 12 Scripts]]

[[../index|← Home]] | [[12.1 - Tunneling and the Hartman paradox|Next →]]
