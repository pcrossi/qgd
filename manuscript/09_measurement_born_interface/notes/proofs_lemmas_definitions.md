---
title: "Proofs, lemmas and definitions — Chapter 9"
---

# Proofs, lemmas and definitions — Chapter 9

This note gathers the technical chain of Chapter 9. The central point is to separate three layers:

1. the positive geometric density of GDQ;
2. the operational Born rule in the reconstructed physical Hilbert space;
3. the real dynamics of apparatus, interface, decoherence, and record.

None of these layers alters the official action. The apparatus enters as classical data of source, constraint, or boundary of a physical problem.

## 1. Geometric density and regular local sector

The current constitutive definition is

$$
\rho=e^{-(f+\bar f)/2}.
$$

The real phase is

$$
S_R=\frac{\hbar}{2i}(f-\bar f).
$$

In the regular local sector, we define the projective representation

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
$$

Hence,

$$
|\Psi|^2=\rho.
$$

This identity is important, but its scope is limited: it identifies the spatial density in a regular representation. It does not select the basis of a detector and does not prove, on its own, Born for any observable.

## 2. Operational Born rule in the reconstructed physical Hilbert space

After the reconstruction of the physical space, an operational measurement is a measure on a family of orthogonal projectors

$$
P_iP_j=\delta_{ij}P_i,
\qquad
\sum_iP_i=I.
$$

An operational probability rule must satisfy:

1. positivity, $\mu(P)\ge0$;
2. normalization, $\mu(I)=1$;
3. additivity over orthogonal projectors;
4. operational non-contextuality for the same projector;
5. compatibility with composition and marginals.

In the complex physical Hilbert space, these conditions lead to the form

$$
\mu(P)=\operatorname{Tr}(\varrho P).
$$

For a pure state $\varrho=|\psi\rangle\langle\psi|$,

$$
\mu(P_i)=\langle\psi|P_i|\psi\rangle.
$$

If $P_i=|i\rangle\langle i|$,

$$
\mu(P_i)=|\langle i|\psi\rangle|^2.
$$

In the case of position, for a region $R$,

$$
P(R)=\int_R\rho\,d\mu_h.
$$

Therefore Born is structurally closed as an operational rule in the reconstructed physical Hilbert space. GDQ remains deeper than this layer: it still needs to say how the apparatus defines the real projectors.

## 3. Apparatus as source, constraint, or boundary

A classical apparatus is not a quantum operator inserted into the theory. It provides physical data:

$$
J_{\rm app}^{\rm classico},
\qquad
C_{\rm app},
\qquad
\partial M_{\rm app}.
$$

The correct GDQ chain is

$$
J_{\rm app}^{\rm classico}
\to
\delta\Phi_{\rm app}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\Omega = \text{R}_{\rm app}
\to
\text{spectral response}
\to
\text{record}.
$$

The background with the apparatus is a stationary solution of the variational problem with these boundary data:

$$
\left.
\frac{\delta}
{\delta\Phi}
\left(
\mathcal S_{\rm GDQ}
+\mathcal S_{\rm source/boundary}
\right)
\right|_{\Phi_*}
=0.
$$

The term $\mathcal S_{\rm source/boundary}$ is not a new fundamental action. It encodes the physical fact that the experimentalist built an apparatus with specific fields, materials, and boundaries.

## 4. Physical Hessian and interface response

On the background $\Phi_*$, the projected physical Hessian is

$$
K_{\rm phys}
=
P_{\rm phys}^{\dagger}
\left.
\frac{\delta^2\mathcal S_{\rm GDQ}}
{\delta\Phi\,\delta\Phi}
\right|_{\Phi_*}
P_{\rm phys}.
$$

The projector $P_{\rm phys}$ removes constraints, gauge redundancies, and Noether modes that do not correspond to observable deformations of the record.

Split the degrees of freedom into boundary $\partial$ and interior $I$:

$$
K_{\rm phys}
=
\begin{pmatrix}
K_{\partial\partial} & K_{\partial I}\\
K_{I\partial} & K_{II}
\end{pmatrix}.
$$

The stationary interior satisfies

$$
K_{I\partial}\delta\Phi_\partial
+K_{II}\delta\Phi_I=0.
$$

If $K_{II}$ is invertible in the physical sector,

$$
\delta\Phi_I
=-K_{II}^{-1}K_{I\partial}\delta\Phi_\partial.
$$

Substituting, the effective response seen at the interface is

$$
\text{R}_{\rm app}
=
K_{\partial\partial}
-K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

This is the Schur/DtN form of the apparatus impedance. It contains geometry, stiffness, losses, and material. It is not a new fundamental parameter.

## 5. Decoherence as effective reduction

If macroscopic alternatives $i$ and $j$ induce distinct apparatus responses, the reduced coherence has the form

$$
\rho_{ij}^{\rm red}(t)
=
\rho_{ij}^{\rm red}(0)\,e^{-\Gamma_{ij}(t)}.
$$

In a regime with a measurement gap $\Delta_{\rm meas}$,

$$
|\rho_{ij}^{\rm red}(t)|
\le
C\,e^{-\Delta_{\rm meas}t}.
$$

This explains the operational suppression of interference between records. Even so, decoherence is not, on its own, a unique individual outcome; it makes the macroscopic decomposition robust.

The script `scripts/simulate_decoherence_sae.py` verifies this decay in a reduced $S+A+E$ model and makes explicit that the test is effective.

## 6. Unique outcome by real basins

An individual event requires real basins of the object--apparatus--environment microgeometry. Let $\mathfrak F_{\rm meas}$ be the effective measurement functional in the reduced open sector. A record $R_i$ is stable if

$$
\nabla\mathfrak F_{\rm meas}(R_i)=0,
\qquad
\operatorname{Hess}_{R_i}^{\rm phys}\mathfrak F_{\rm meas}>0.
$$

The associated basin is

$$
\mathcal B_i
=
\left\{
\Phi_0:
\big.
\lim_{t\to\infty}\Phi(t;\Phi_0)=R_i
\right\}.
$$

If the boundaries between basins are stable manifolds of saddles, they have measure zero. Then almost every microscopic initial condition falls into a single basin. Born compatibility requires

$$
\mu_{\rm micro}(\mathcal B_i)
=
\operatorname{Tr}(\varrho P_i).
$$

This is the conservative status: Born provides the operational frequencies; the uniqueness of each event is a theorem conditional on real basins of the apparatus and environment.

## 7. Entanglement and no-signalling in the reduced sector

Entanglement is non-factorization of the physical state in configuration space. In the reconstructed Hilbert sector, for the ideal singlet,

$$
E(\mathbf a,\mathbf b)=-\mathbf a\cdot\mathbf b.
$$

The local marginals are independent of the remote axis:

$$
\sum_{\beta=\pm1}
p(\alpha,\beta|\mathbf a,\mathbf b)
=
p(\alpha|\mathbf a).
$$

The script `scripts/verify_entanglement_no_signalling.py` verifies, in the ideal reduced sector:

- Schmidt values $0.707106781187,0.707106781187$;
- maximum error in $E+\mathbf a\cdot\mathbf b$ equal to $0$;
- local marginal variations equal to $0$;
- ideal CHSH value $-2.828427124746$.

This test confirms reduced operational consistency. It does not replace the multiparticle Hessian of real apparatuses.

## 8. Non-Hermitian extensions

By eliminating unobserved degrees of freedom of a dissipative apparatus, the effective record operator can be non-Hermitian. This does not mean that the official action has become non-Hermitian. It only means that the observed sector is open.

Schematically,

$$
K_{\rm eff}(z)
=
K_{QQ}
-K_{QI}(K_{II}-z)^{-1}K_{IQ}.
$$

If the complement possesses dissipative or continuous channels, $K_{\rm eff}$ can have an effective imaginary part. This is an extension of open dynamics and belongs to the metrology of real apparatuses.

## 9. Self-contained scripts of the chapter

| Script | Role | Classification |
|---|---|---|
| `verify_born_projectors.py` | Positivity, additivity, basis change, composition, and marginals. | Operational test. |
| `verify_entanglement_no_signalling.py` | Singlet, CHSH, and marginals. | Reduced test. |
| `simulate_decoherence_sae.py` | Exponential suppression of coherences. | Effective reduction. |
| `detector_response_schur.py` | Calculation of $\text{R}_{\rm app}$ and $\Gamma_{\rm det}$ in reduced detector. | Interface toy model. |

The scripts are pedagogical verifications. They do not replace the calculation of a complete material Hessian.

## 10. Status

| Outcome | Status | Limit |
|---|---|---|
| Local $\rho=|\Psi|^2$ | Proven in the regular sector | Does not select detector. |
| Operational Born | Structurally closed | Depends on the reconstructed physical Hilbert space. |
| Apparatus as Schur/DtN | Structurally closed | Metrology depends on material. |
| Decoherence | Effective reduction | Is not alone a unique outcome. |
| Individual outcome | Conditional | Requires real basins. |
| Effective non-Hermitian | Extension program | Does not alter the official action. |
