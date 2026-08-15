---
title: "Scripts — Chapter 14"
---

# Scripts — Chapter 14

## Final verifications

- `verify_gaussian_soliton.py`
  - Classification: symbolic-numerical verification of an explicit neutral solution.
  - Verifies the Gaussian soliton equation, $\mathcal W_{\rm gauss}=0$, and the reduced gap of the Ornstein--Uhlenbeck operator.
  - Output: `output_verify_gaussian_soliton.md`.

- `monotonicity_vs_hessian.py`
  - Classification: symbolic-numerical illustration of stability criterion.
  - Shows that a functional can be monotonic along the flow even when the critical point is a saddle; thus the physical Hessian is indispensable.
  - Output: `output_monotonicity_vs_hessian.md`.

| Script | Objective | Classification |
|---|---|---|
| `hypercharges_z6.py` | Search for integer hypercharges $y=6Y$ compatible with $\mathbb Z_6$, anomalies, and primitivity. | Exact symbolic-numerical verification. |
| `aps_index_hopf_bismut.py` | Verify $c_1=m$, fractional $\bar\eta$, torsional kernel, and primitive APS index. | Discrete topological verification. |
| `index_lifting_representations.py` | Count Weyl components per generation and per three index units. | Discrete symbolic verification. |
| `global_product_three_stomata.py` | Confirm Betti/Euler of the global product, flat Berry, and local count by three stomata. | Topological consistency test. |
| `hessian_three_centers.py` | Calculate constrained Hessian of the $C_3$ junction and Schur complement. | Direct verification of reduced construction. |
| `physical_hessian_c3_gap.py` | Calculate physical projector, Schur, and reduced gap of the $C_3$ junction. | Direct evaluation of reduced operator. |
| `couplings_norms.py` | Calculate $I_3$, $I_2$, $I_Y$, $g'^2/g^2$, and $\sin^2\theta_W$. | Direct evaluation of geometric norm. |
| `junction_n_selection.py` | Test selection $N=3$ and null modes for $N>3$ in the horizontal reduced model. | Consistency test of the selection proof. |

All scripts are self-contained and write a Markdown output in the same folder.
