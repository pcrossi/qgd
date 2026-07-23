---
title: Question 24 - Measurement problem
status: conditionally_closed_asymptotic_record_and_basin_theorem
source: questoes/q24/questao_24.md; questoes/q24/associados/teorema_assintotico_registros_q24.md; questoes/q24/associados/resultado_unico_bacias_microgeometria.md
updated: 2026-07-16
---

# Question 24 - Measurement problem

Q24 asks how GDQ describes a full measurement without hiding the Born rule in a
partition function.

Measurement is modeled as an open process

$$
S+A+E,
$$

where $S$ is the system, $A$ the apparatus, $E$ the environment and $R_i$ the
macroscopic records.

An ideal interaction correlates eigenstates with pointer states:

$$
|s_i\rangle|A_0\rangle|E_0\rangle
\longmapsto
|s_i\rangle|A_i\rangle|E_i\rangle.
$$

For

$$
|\psi\rangle=\sum_i c_i|s_i\rangle,
$$

unitarity gives

$$
|\Psi_{SAE}\rangle
=
\sum_i c_i|s_i\rangle|A_i\rangle|E_i\rangle.
$$

If apparatus/environment states decohere,

$$
\rho_{SA}
\approx
\sum_i |c_i|^2
|s_i,A_i\rangle\langle s_i,A_i|.
$$

Probabilities come from Q22:

$$
P(i)=\operatorname{Tr}(\rho_SP_i).
$$

The pointer basis is selected by the interaction and stability/decoherence of
the apparatus states, not by Born.

## Unique outcome

Decoherence alone gives an improper mixture. A unique ontological result
requires the GDQ hypothesis that the real microgeometry of apparatus and
environment selects one basin of attraction $R_i$. With that hypothesis,
collapse is an effective, continuous, open-sector geometric transition
compatible with global unitarity.

## Status

Q24 is conditionally closed as an asymptotic theorem of records and real
basins. Under a self-adjoint GDQ measurement Hessian with apparatus boundary
conditions, well-defined sectors \(R_i\) and a positive measurement gap,
coherences between different records decay exponentially. If the
microgeometry \(A+E\) also satisfies the Morse/Lyapunov basin hypotheses,
almost every event converges to a unique record. Decoherence alone is still
not identified with ontological branch selection; the basin theorem supplies
the extra conditional dynamics.
