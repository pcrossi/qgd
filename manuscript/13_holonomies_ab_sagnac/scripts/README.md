---
title: "Scripts — Chapter 13"
---

# Scripts — Chapter 13

| Script | Objective | Classification |
|---|---|---|
| `ab_symbolic_holonomy.py` | Symbolically verify $dA_{\rm harm}=0$, $\oint A=\Phi$ and the holonomy. | Symbolic consistency test of the ideal holonomy. |
| `ab_ideal_phase.py` | Calculate ideal AB phase as a function of flux. | Direct evaluation of ideal holonomy. |
| `sagnac_light_matter.py` | Calculate Sagnac for light and matter. | Direct ideal evaluation. |
| `reduced_cow_estimation.py` | Estimate reduced COW phase. | Reduced phenomenological estimation. |
| `verify_schur_projector.py` | Verify the construction $P_{\rm phys}^{\dagger}KP_{\rm phys}$ and $\mathsf R=K_{YY}-K_{YI}K_{II}^{-1}K_{IY}$ in a self-contained matrix. | Symbolic-numerical consistency test. |

## Note on self-containment

The scripts in this directory do not depend on the questions files. Each script declares the evaluated equation, the physical parameters used, the classification of the calculation and the corresponding output file.
