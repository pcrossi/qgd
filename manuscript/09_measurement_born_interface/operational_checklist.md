---
title: "Operational checklist — Chapter 9"
---

# Operational checklist — Chapter 9

## 1. Statement

Explain Born's rule and the measurement theory in GDQ without reducing the theory to standard quantum mechanics and without inserting external collapse into the official action.

## 2. Logical status

| Block | Status | Observation |
|---|---|---|
| Positive density | Demonstrated/constitutive | $\rho=e^{-(f+\bar f)/2}$. |
| Representation $\rho=|\Psi|^2$ | Regular sector | Necessary, but not sufficient. |
| Operational Born | Structurally closed | Uses reconstructed Hilbert space and projectors. |
| Apparatus as boundary | Structural | Classical source/boundary, not a new action. |
| Multiparametric calibration | Structurally closed | Schur/DtN, Riccati, identifiability and training-test split. |
| Cesium benchmark | Initial phenomenological validation | Generalizes outside the fit; does not yet derive the magnetic channel from the GDQ Hessian. |
| Decoherence | Effective reduction | Explains diagonalization of records. |
| Unique outcome | Conditionally closed in the Gaussian QND sector | Other sectors depend on the real dynamics of $A+E$. |
| Stern--Gerlach | Structural prototype | Apparatus selects axis. |
| Delayed choice | Structurally closed | Boundary problem, without physical retrocausality. |
| Entanglement | Structural/conditional | Geometric non-factorization; metrological no-signalling remains future work. |

## 3. Deductive chain

$$
\mathcal S_{\rm GDQ}
\to
\rho,S_R
\to
\Phi_\ast
\to
K_{\rm phys}
\to
\text{R}_{\rm app}
\to
\mathcal H_{\rm phys}
\to
\mu(P)=\operatorname{Tr}(\varrho P)
\to
\text{record}.
$$

Technical construction named:

- [[notes/gdq_construction_of_measurement|GDQ construction of measurement]]
- [[notes/multiparametric_calibration_invariant_embedding|Multiparametric calibration by invariant embedding]]
- [[notes/born_theorem_gaussian_qnd_basins|Born-basin theorem for Gaussian QND apparatuses]]

## 4. Optional scripts

| Script | Classification |
|---|---|
| `verify_born_projectors.py` | Consistency test of operational logic: positivity, additivity, unitary bases, composition and marginals. |
| `verify_entanglement_no_signalling.py` | Reduced operational consistency test: non-factorization, marginals and ideal CHSH. |
| `simulate_decoherence_sae.py` | Effective S+A+E reduction, asymptotic gap and ideal repeatability. |
| `detector_response_schur.py` | Toy model of response by Schur complement. |
| `verify_immersion_calibration.py` | Riccati-Schur consistency, convergence and synthetic calibration. |
| `benchmark_cs_fein2022.py` | Separate calibration and validation on digitized real data. |

## 5. Points that must not be forgotten

- Do not declare $\rho=R^2$ as a complete proof of Born.
- Do not treat the apparatus as a manually inserted quantum operator.
- Do not call decoherence a unique outcome without capture dynamics.
- Do not extend the Gaussian QND theorem to demolition or non-Gaussian apparatuses without a new proof.
- Do not use delayed choice as retrocausality.
- Do not assert metrological no-signalling for real apparatuses without calculation.
- Do not call a calibrated instrumental parameter a theory constant.
- Do not use the same set to calibrate and declare prediction.
- Do not confuse validation of the instrumental protocol with exclusive validation of GDQ.

## Didactic review of 2026-07-19

Chapter 9 was verified in the scientific/didactic review phase. The central chain remains:

$$
J_{\rm app}^{\rm classico}
\to
\delta\Phi_{\rm app}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\text{R}_{\rm app}
\to
\text{spectral response}
\to
\text{record}.
$$

The chapter is self-contained and does not depend on historical labels. The scripts were revised to point only to precise internal sources of the chapter itself: Born by projectors, S+A+E decoherence, and reduced detector response by Schur complement. All remain classified as reduced/pedagogical verifications, not metrological predictions.
