---
title: "Operational checklist — Chapter 16"
---

# Operational checklist — Chapter 16

## 1. Statement

Construct, in QGD language, the inherited fine structure constant, the Zeeman effect, the minimal term $g=2$, the leading term $\alpha/(2\pi)$, and the Hessian operator that defines the magnetic anomaly.

## 2. Constructive chain

$$
J_{\rm app}^{\rm classical}
\to
\delta\Phi_{\rm app}
\to
K_{\rm phys}
\to
\mathsf R_{\rm app}
\to
\Delta E_{\rm Zeeman}
\to
a_\ell.
$$

## 3. Logical status

| Block | Status | Observation |
|---|---|---|
| $\alpha$ | conditionally closed | Einstein mean and global-local bridge |
| Zeeman | structurally closed | Noether, isotropy and external source |
| $g=2$ | structurally closed | circulation and magnetic normalization |
| $\alpha/(2\pi)$ | closed as leading term | norm of the harmonic 1-form |
| operational Hessian | constructed | defines the calculation of $a_\ell$ |
| metrological residuals | open | require upper channels of $H_{C,\ell}$ |

## 4. Final/reduced scripts

| Script | Classification |
|---|---|
| `calculate_einstein_mean_alpha.py` | Direct evaluation of the inherited geometric mean. |
| `calculate_iso_hessian_projector.py` | Direct evaluation of the isotropic projector of the mean Hessian. |
| `test_schur_dtn_alpha.py` | Schur/DtN diagnostic without adjustment of round impedance. |
| `zeeman_linear_response.py` | Symbolic-numerical verification of the Zeeman response. |
| `gminus2_leading_term.py` | Direct evaluation of $a^{(1)}=\alpha/(2\pi)$. |
| `evaluate_anomaly_hessian.py` | Consistency test of the leading Hessian block. |
| `test_hierarchy_does_not_replace_gminus2.py` | Diagnostic separating the leptonic hierarchy from the Zeeman/g-2 sector. |

## 5. Preserved points

- The magnetic field is an apparatus source/boundary, not a new fundamental term.
- $g=2$ is not imported from Dirac.
- $\alpha/(2\pi)$ is not called an ontological loop.
- the leptonic hierarchy provides leptonic background, not complete magnetic response.
- Historical `required` blocks of the Zeeman/g-2 sector are not migrated as prediction.
- Phenomenological formulas of $g_\mu-2$ remain as future program until the upper Hessian.
