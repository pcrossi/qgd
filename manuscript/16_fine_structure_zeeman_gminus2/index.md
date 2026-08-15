---
title: "16. Fine Structure, Zeeman and g-2"
---

# 16. Fine Structure, Zeeman and $g-2$

This chapter treats the magnetic response as QGD, not as an import of Dirac theory or QED. The magnetic field is a classical datum of the apparatus: source, boundary, or external constraint. The particle already possesses circulation, charge, and geometric rigidity before measurement.

The construction chain used here is:

$$
J_{\rm app}^{\rm classical}
\to
\delta\Phi_{\rm app}
\to
K_{\rm phys}
\to
\mathsf R_{\rm app}
\to
\text{magnetic response}
\to
\text{readout}.
$$

In the weak and nearly uniform sector, this chain reduces to three results:

1. the fine structure constant enters as a normalization inherited from the global-local bridge;
2. the Zeeman effect comes from the axis selection by Noether and isotropy;
3. the minimal term $g=2$ and the leading correction $\alpha/(2\pi)$ are geometric responses, while the metrological residuals of $g-2$ require upper channels of the Hessian.

The goal is not to claim that all of $g-2$ is already numerically closed. The goal is to show the correct operator that must replace, in QGD, the operational language of vertices:

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

## Sections

- [[16.1 - The inherited fine structure constant]]
- [[16.2 - Circulation, charge and magnetic moment]]
- [[16.3 - Magnetic field as source and boundary]]
- [[16.4 - Zeeman effect by Noether and isotropy]]
- [[16.5 - Why the minimal term is g equals 2]]
- [[16.6 - The factor alpha over 2pi]]
- [[16.7 - The anomaly Hessian operator]]
- [[16.8 - Relation to the leptonic hierarchy]]
- [[16.9 - Comparison, limits and metrological program]]

## Notes called

- [[notes/electromagnetism/einstein_mean_alpha|Alpha as Einstein mean]]
- [[notes/electromagnetism/zeeman_noether_isotropy|Zeeman by Noether and isotropy]]
- [[notes/electromagnetism/coupling_1form_2form_zeeman|Coupling by 1-form and 2-form]]
- [[notes/electromagnetism/g2_noether_protection|Noether protection of g equals 2]]
- [[notes/electromagnetism/factor_1_over_2pi_circulation|Factor 1 over 2 pi]]
- [[notes/electromagnetism/gminus2_transverse_hessian|Transverse Hessian of g-2]]
- [[notes/electromagnetism/upper_channels_gminus2|Upper channels of g-2]]
- [[notes/electromagnetism/gmu2_pending_audit|Pending audit of g-2]]

## Scripts and verifications

- [[scripts/README|Scripts of Chapter 16]]

## Status

| Block | Status | Observation |
|---|---|---|
| $\alpha$ | conditionally closed | Einstein isotropic mean and global-local bridge |
| Zeeman | structurally closed | external source, Noether and isotropy |
| $g=2$ | structurally closed | conserved circulation |
| $\alpha/(2\pi)$ | closed as leading term | norm of the harmonic 1-form |
| direct upper channel uniform | closed negatively | Hodge rule gives $\mu_{2,\ell}^{\rm direct}=0$ |
| upper route | closed as precise program | Hessian mixture mediated by density |
| complete $g_e$ | metrologically open | requires physical 8D saddle and upper contraction |
| complete $g_\mu-2$ | metrologically open | should not be obtained by post-fitting |

[[../15_leptonic_hierarchy_masses/index|← Previous chapter]] | [[../17_baryonic_structure/index|Next chapter →]]
