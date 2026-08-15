---
title: "09. Born's rule, measurement and the classical-quantum interface"
---

# 09. Born's rule, measurement and the classical-quantum interface

GDQ does not take Born's rule as a primary axiom. The theory starts with geometric density, phase, weighted measure, official action, boundaries, and physical Hessian. The probability rule appears when this structure is observed by a macroscopic apparatus and projected onto the physical Hilbert space reconstructed in Chapter 8.

The goal of this chapter is to carefully separate three assertions that are often confused:

1. GDQ has a conserved positive density;
2. in the regular sector, this density can be written as $|\Psi|^2$;
3. a real measurement requires apparatus, boundary, record, and an operational rule for mutually exclusive alternatives.

The first assertion is geometric. The second is a local representation. The third is measurement theory.

## Roadmap

- [[09.1 - Why Born is not just rho equal to R squared]]
- [[09.2 - Conserved positive density of GDQ]]
- [[09.3 - Operational probabilities in the reconstructed Hilbert space]]
- [[09.4 - System, apparatus, environment and records]]
- [[09.5 - The apparatus as source and boundary]]
- [[09.5A - Multiparametric calibration and invariant embedding]]
- [[09.6 - Decoherence, dynamical basins and unique outcome]]
- [[09.7 - Stern-Gerlach as axis measurement]]
- [[09.8 - Delayed choice as boundary change]]
- [[09.9 - Entanglement as geometric non-factorization]]
- [[09.10 - Limits and metrological program]]

## Central result

The measurement chain used in this chapter is:

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

The apparatus does not modify the official action. It provides classical external data: source, constraint, impedance, or boundary. These data select the effective domain of the problem and, therefore, the observed pointer basis.

In the reconstructed physical Hilbert space,

$$
\mathcal H_{\rm phys}
=
\overline{\mathcal D_+/(\mathcal N+\mathcal G)},
$$

the admissible operational rule for projective alternatives is:

$$
\mu(P)=\operatorname{Tr}(\varrho P).
$$

For a pure state and projector $P_i=|i\rangle\langle i|$, it reduces to:

$$
P(i|\psi)=|\langle i|\psi\rangle|^2.
$$

Thus, Born is not introduced as a patch. It is the operational rule in the reconstructed sector, while GDQ provides the density, phase, boundary, and interface dynamics that make a measurement physical.

With this, the quantum mechanics of projectors is recovered as a particular case of measurement: when the apparatus reduces the interface to orthogonal alternatives in $\mathcal H_{\rm phys}$, the record obeys Born's rule. But GDQ does not reduce to this case. The action still describes the classical source, boundary, impedance, physical Hessian, and the process by which the projective domain is selected.

In condensed form:

$$
\boxed{
\text{Born/projectors}
=
\text{operational reading of a sector of GDQ, not a primary axiom of GDQ.}
}
$$

## Status of the result

| Block | Status | Observation |
|---|---|---|
| Positive density $\rho$ | Derived/constitutive | Comes from $f$ and the GDQ measure. |
| $\rho=|\Psi|^2$ local | Demonstrated in the regular sector | Not sufficient for full Born. |
| Operational Born | Structurally closed | Depends on the reconstructed physical Hilbert space. |
| Apparatus as boundary/source | Structural | Does not change the official action. |
| Calibration by invariant embedding | Structurally closed; initial validation | Cesium benchmark generalizes outside the fit; magnetic channel is still an operational input. |
| Decoherence and records | Effective reduction | Explains diagonal mixing and repeatability. |
| Unique individual outcome | Conditionally closed in the Gaussian QND sector | Outside this sector, depends on real basins and specific dynamics. |
| Stern--Gerlach | Structural prototype | Spin/orientation exist; apparatus selects axis. |
| Delayed choice | Structurally closed | Boundary change, not retrocausality. |
| Entanglement | Structural/conditional | Non-factorization in configuration space; metrological Bell/no-signalling remains future work. |

## Editorial control

- [[operational_checklist|Operational checklist of the chapter]]
- [[notes/proofs_lemmas_definitions|Associated proofs, lemmas, and definitions]]
- [[notes/gdq_construction_of_measurement|GDQ construction of measurement]]
- [[notes/operational_born_gleason_trace|Operational Born by measurement on projectors]]
- [[notes/apparatus_as_boundary_hessian_schur|Apparatus as boundary and Schur complement]]
- [[notes/multiparametric_calibration_invariant_embedding|Multiparametric calibration by invariant embedding]]
- [[notes/ohmic_detector_born_capture|Ohmic detector, causal filtering and Born capture]]
- [[notes/dynamical_basins_unique_outcome|Dynamical basins and unique outcome]]
- [[notes/born_theorem_gaussian_qnd_basins|Born-basin theorem for Gaussian QND apparatuses]]
- [[notes/entanglement_non_factorization_no_signalling|Entanglement, non-factorization and no-signalling]]

[[../index|← Home]] | [[09.1 - Why Born is not just rho equal to R squared|Next →]]
