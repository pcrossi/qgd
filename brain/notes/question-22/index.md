---
title: Question 22 - Born rule
status: structurally_closed
source: questoes/q22/questao_22.md
updated: 2026-07-16
---

# Question 22 - Born rule

Q22 asks how GDQ obtains the Born rule without simply postulating
$|\langle i|\psi\rangle|^2$.

GDQ first supplies the positive conserved density

$$
\rho=e^{-(f+\bar f)/2}
$$

and the effective state

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
$$

But $\rho=|\Psi|^2$ alone proves only the position-density reading, not Born in
arbitrary bases.

In the reconstructed Hilbert space, an event is represented by an orthogonal
projector $P$. A probability measure over projectors satisfying positivity,
normalization, additivity over orthogonal alternatives, operational
noncontextuality and tensor-product compatibility has the form

$$
\mu(P)=\operatorname{Tr}(\varrho P).
$$

For a pure state,

$$
\varrho=|\psi\rangle\langle\psi|,
\qquad
\mu(P)=\langle\psi|P|\psi\rangle.
$$

For $P_i=|i\rangle\langle i|$,

$$
P(i|\psi)=|\langle i|\psi\rangle|^2.
$$

## Status

Q22 is structurally closed. Implementation of a specific measurement basis
belongs to Q24.

