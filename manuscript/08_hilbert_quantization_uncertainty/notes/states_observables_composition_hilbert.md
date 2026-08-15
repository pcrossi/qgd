---
title: "States, observables, and composition in the reconstructed Hilbert"
---

# States, observables, and composition in the reconstructed Hilbert

This note completes the operational construction of the physical Hilbert space. It does not introduce the Hilbert space as primary ontology. It shows how the geometric layer of GDQ speaks the operational language of states, observables, evolution, and composite systems when the sector admits reflection positivity, quotienting by null states, and the removal of redundancies.

## 1. Physical Space

The starting point is the reconstructed space:

$$
\mathcal H_{\rm phys}
=
\overline{
\mathcal D_+/
(\mathcal N+\mathcal G)
}.
$$

Here $\mathcal D_+$ is the domain of functionals with positive temporal support, $\mathcal N$ is the zero-norm subspace, and $\mathcal G$ gathers geometric redundancies, such as diffeomorphisms, choices of section, longitudinal modes, and exact boundary modes.

The physical inner product is:

$$
\langle [F],[G]\rangle_{\mathcal H}
=
\langle \Theta F\,G\rangle_E.
$$

In the single-particle regular sector, the same structure reduces to:

$$
\mathcal H_1
=
L^2(N,E,d\Sigma_h),
$$

with:

$$
\Psi
=
\sqrt{\rho}\,e^{iS_R/\hbar},
\qquad
\rho=e^{-(f+\bar f)/2}.
$$

## 2. Physical States

A pure state is a normalized vector:

$$
|\Psi\rangle\in\mathcal H_{\rm phys},
\qquad
\|\Psi\|=1.
$$

Since the global phase does not change any observable, the pure physical state is the ray:

$$
|\Psi\rangle
\sim
e^{i\alpha}|\Psi\rangle.
$$

In open sectors, subsystems, coarse graining, or interaction with an apparatus, the correct description is a density matrix:

$$
\varrho\ge0,
\qquad
\operatorname{Tr}\varrho=1.
$$

This density matrix does not replace geometry. It is the operational description of the reconstructed sector after ignoring unmonitored degrees of freedom or after conditioning the system to the apparatus.

## 3. Observables

A physical observable is a densely defined self-adjoint operator:

$$
A:D(A)\subset\mathcal H_{\rm phys}\to\mathcal H_{\rm phys},
\qquad
A=A^\dagger.
$$

In a more general form, it can be treated as a self-adjoint element of a local algebra:

$$
A\in\mathcal A(O),
\qquad
A=A^\dagger.
$$

The domain is part of the definition. A formal expression that does not possess a dense domain, a self-adjoint closure, and compatible boundary conditions is not yet a closed physical observable.

By the spectral theorem, if $E_A(\Delta)$ is the spectral projector associated with the interval $\Delta\subset\mathbb R$, then:

$$
\mathbb P_A(\Delta)
=
\langle\Psi,E_A(\Delta)\Psi\rangle
$$

for a pure state, and:

$$
\mathbb P_A(\Delta)
=
\operatorname{Tr}(\varrho E_A(\Delta))
$$

for a mixed state.

In the position sector:

$$
\mathbb P(x\in R)
=
\int_R |\Psi(x)|^2\,d\Sigma_h
=
\int_R \rho(x)\,d\Sigma_h.
$$

Thus, the positive geometric density $\rho$ becomes the Born density only after the operational reconstruction of the regular sector.

## 4. Evolution

The parameter $\tau$ is a geometric flow parameter. It is not, by itself, the unitary group of physical time.

When the reconstruction in physical time provides a self-adjoint Hamiltonian:

$$
H=H^\dagger,
$$

the evolution is:

$$
U(t)=e^{-itH/\hbar}.
$$

By the spectral theorem:

$$
U(t)^\dagger U(t)=I.
$$

Therefore:

$$
\text{||}U(t)\Psi\text{||}=\text{||}\Psi\text{||}.
$$

This is a conditional theorem of the reconstructed sector: it requires domain, self-adjointness, and physical positivity.

## 5. Composite Systems

For two distinguishable and approximately decoupled systems, the operational composition is:

$$
\mathcal H_{AB}
=
\mathcal H_A\otimes\mathcal H_B.
$$

The inner product factorizes:

$$
\langle
\psi_A\otimes\psi_B,
\phi_A\otimes\phi_B
\rangle_{AB}
=
\langle\psi_A,\phi_A\rangle_A
\langle\psi_B,\phi_B\rangle_B.
$$

An entangled state is a vector in $\mathcal H_A\otimes\mathcal H_B$ that does not admit simple factorization:

$$
\Psi_{AB}\ne\psi_A\otimes\psi_B.
$$

In GDQ language, this means that the total geometric configuration does not separate into two independent geometries. There is a global correlation of phase, holonomy, boundary, or measure.

For observables:

$$
A
\mapsto
A\otimes I_B,
\qquad
B
\mapsto
I_A\otimes B.
$$

For product states:

$$
\langle A\otimes B\rangle_{\psi_A\otimes\psi_B}
=
\langle A\rangle_{\psi_A}
\langle B\rangle_{\psi_B}.
$$

## 6. Identical Systems

For $N$ identical systems, first $\mathcal H^{\otimes N}$ is formed. Then, it is projected onto the appropriate statistical sector.

For bosons:

$$
\mathcal H_N^{(+)}
=
\operatorname{Sym}^N\mathcal H.
$$

For fermions:

$$
\mathcal H_N^{(-)}
=
\wedge^N\mathcal H.
$$

In GDQ, this operational rule must be compatible with the holonomy, spin structure, and topology of the sector. It is not taken as a substitute for the geometric explanation of spin-statistics; it is the Hilbertian form after reconstruction.

## 7. Status

The result is structurally closed:

$$
\text{Geometric GDQ}
\to
\text{sectorial measure and positivity}
\to
\mathcal H_{\rm phys}
\to
\text{states, observables, evolution, and composition}.
$$

The complete closure of each sector still requires verifying the existence of the measure, reflection positivity, cluster, essential self-adjointness, a dense common domain, consistent removal of redundancies, and tensor factorization for asymptotically separated systems.
