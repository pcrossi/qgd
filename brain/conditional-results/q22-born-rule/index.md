---
title: Q22 Born rule
status: structural
source: manuscrito/09_measurement_born_interface/notes/born_operacional_gleason_traco.md
updated: 2026-07-21
---

# Q22 Born rule

Given the reconstructed Hilbert space and projective alternatives, positivity,
normalization, additivity over orthogonal projectors, operational
noncontextuality and tensor-product compatibility force

$$
P(P|\varrho)=\operatorname{Tr}(\varrho P).
$$

For pure states and rank-one projectors this gives

$$
P(i|\psi)=|\langle i|\psi\rangle|^2.
$$

Manuscript status: self-contained in Chapter 9, especially
`manuscrito/09_measurement_born_interface/notes/born_operacional_gleason_traco.md`.
The proof now explicitly includes additivity, normalization, arbitrary bases,
tensor products, partial traces and the position-sector recovery
`P(R)=int_R rho dmu_h`. The script
`manuscrito/09_measurement_born_interface/scripts/verificar_born_projetores.py`
checks these finite-dimensional algebraic consequences.
