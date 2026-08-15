---
title: "Operational checklist — Chapter 6"
---

# Operational checklist — Chapter 6

This checklist records the consolidation state of Chapter 6 and separates what has been demonstrated, what is conditional, and what must be addressed in subsequent chapters or appendices.

The chapter does not globally identify Einstein's cosmological universe with GDQ's local bulk. It constructs a controlled bridge between the two regimes.

## 1. Chapter Statement

The problem is to show when results obtained in the auxiliary cosmological space

$$
T^5\times S^3
$$

can be transported to the official local bulk

$$
\mathbb R^4\times T^4
$$

without confusing the two spaces.

The bridge must transport more than an intuition of a flat limit. It must control:

- pointed geometry;
- fields $g$, $J$, and $f$;
- Bismut torsion reconstructed as $H=d_J^c\omega$;
- weighted measure $\mathcal U$;
- physical Hessian;
- domain of the operators;
- constraints and gauge modes;
- physical gap;
- resolvents and spectral projectors;
- separation between topological invariants and continuous normalizations.

## 2. Logical status

| Block | Status | Observation |
|---|---|---|
| Pointed limit | Demonstrated | The family $M_\varepsilon$ converges locally to $T^4\times\mathbb R^4$. |
| Transport of fields and measure | Conditional | Requires admissible background, regularity, uniform domination, and cutoff correction. |
| Physical Hessian | Conditional | Depends on the joint removal of constraints, redundancies, and zero modes. |
| Localization and gap | Conditional | The relevant gap is physical/local, not the compactification gap. |
| Resolvents and Riesz | Conditional | Follows from Mosco, uniform gap, and localization. |
| Separation topology/normalization | Demonstrated | Topology transports integers/classes; continuous normalizations require their own calculation. |
| Reduced $C_3$ sector | Applied theorem | In the trimodal stationary background, the primitive gap is $\Delta_0=1/2$. |
| Canonical Madelung identity | Conditional | It is not an off-shell identity of the official action; it holds in the polarized/reduced sector. |

## 3. Current deductive chain

A cadeia do capítulo é:

$$
M_\varepsilon
\to
\text{pointed limit}
\to
\text{transport of }(g,J,f,\mathcal U)
\to
P^{\rm phys}
\to
K^{\rm phys}
\to
\text{local gap}
\to
\text{Riesz projectors}
\to
\text{local spectral inheritance}.
$$

This chain is sufficient to justify the global-local transition in localized sectors that satisfy the declared hypotheses.

It does not automatically calculate continuous constants, absolute scales, detector responses, or normalizations of massless channels.

## 4. Points that the chapter must already preserve

- The cosmological space $T^5\times S^3$ is auxiliary/global/spectral.
- The official local bulk is $\mathbb R^4\times T^4$.
- There is no physical collar between cosmology and laboratory.
- DtN operators and Schur complements belong to the material boundary of the stoma, not to a cosmology-laboratory wall.
- Torsion is not transported as an independent field; it is reconstructed from $g$ and $J$.
- The physical projector must be joint. Products of separate projectors can fail when the subspaces do not commute.
- Decompactification eliminates artificial compactification gaps; only the gap of the physical Hessian of the defect counts.
- Spectral projectors, not isolated eigenvectors, are the correct objects of inheritance.
- Charge normalization, $\alpha$, apparatus responses, and energy units require calculations of flux, Hessian, DtN, or boundary.

## 5. Notes called and their function

The chapter calls the note:

[[../notes/equations/Audit of the canonical term rho d_t S_R|Audit of the canonical term rho d_t S_R]]

This note must remain as a conceptual audit of the canonical term. Its function is to avoid the incorrect assertion that

$$
\Pi_{S_R}^{\rm lab}=\rho_{\rm lab}
$$

is an off-shell identity of the official action.

The correct status is:

- the phase current follows from the official action;
- the local continuity follows after reconstruction of the laboratory sector;
- the canonical Madelung polarization is a conditional physical reduction;
- the condition can be selected by a stationary sector with connected support, primitive charge, and Routh minimum;
- the complete proof of the apparatus dynamics belongs to measurement theory.

## 6. Recommended optional scripts

The scripts of this chapter must be only educational and reproducible verifications. They do not replace the proofs of the lemmas.

It is recommended to create, if necessary, the folder:

`manuscript/06_global_local_bridge/scripts/`

with the following self-contained tests:

| Script | Function |
|---|---|
| `verificar_limite_apontado_torus_esfera.py` | Numerically shows that $S^1_R$ and $S^3_R$ become flat in fixed windows as $R\to\infty$. |
| `verificar_transporte_medida_ponderada.py` | Tests the normalization of a weighted density under a chart change with the correct Jacobian. |
| `verificar_gap_localizacao_toy.py` | Illustrates that a bound mode preserves the local gap while the external volume grows. |
| `verificar_resolvente_riesz_toy.py` | Compares resolvents and Riesz projectors in a family of finite operators. |
| `verificar_homomorfismo_relogio.py` | Verifies the form $\tau_\gamma(t)=\tau_0 e^{\kappa t}$ from the homomorphism between translations and dilations. |

Each script must save its output in Markdown, declare whether it is a toy model, consistency check, or direct evaluation, and must not be used to tune physical constants.

## 7. Extensions that do not reopen the chapter

These extensions do not invalidate the global-local bridge as a structural chapter:

- final metrological calculation of $\alpha$;
- absolute calculation of $G$;
- response of a specific real apparatus;
- complete normalization of massless channels;
- complete spectrum of warped/mixed backgrounds;
- Page curve, black holes, or non-linear detectors.

These problems use the bridge, but are not the bridge itself.

## 8. Closure criteria for Chapter 6

Chapter 6 is ready for the manuscript if:

1. the two geometries are always distinguished;
2. the six lemmas are kept with their correct status;
3. spectral inheritance is presented as conditional on the gap;
4. the $C_3$ sector is presented as a demonstrated application, not as a proof for all backgrounds;
5. the identity $\Pi_{S_R}=\rho$ is described as a conditional polarization/reduction;
6. continuous normalizations are referred to their own calculations of flux, Hessian, DtN, or boundary.

With these precautions, the chapter can serve as a technical bridge between the foundational chapters and the subsequent chapters on spectrum, particles, measurement, and metrology.

## Didactic review of 2026-07-19

Chapter 6 was checked during the scientific/didactic review phase. The terminology of the checklist was adjusted to separate metrological extensions from foundational gaps: $\alpha$, $G$, massless channels, detectors, and warped/mixed backgrounds use the bridge, but are not the bridge itself.

The script `verificar_homomorfismo_relogio.py` was updated to the standard self-contained header: objective, theoretical source, classification, equation, domain, parameters, and output. All scripts of the chapter must remain as educational checks, not physical predictions.
