---
title: "OS criterion for operational Lorentzian time"
---

# OS criterion for operational Lorentzian time

This note records the secure part of the operational Lorentzian reconstruction. It does not state that every GDQ background automatically satisfies the Osterwalder--Schrader axioms. It asserts the conditional theorem: if an effective Euclidean sector of GDQ satisfies the OS hypotheses, then there exists a physical Hilbert space, a positive Hamiltonian, and unitary evolution in physical time.

## 1. Separation between Signature and Quantum Reconstruction

The Lorentzian signature of the physical leaf is obtained by the reflection of a Riemannian metric $q$ on an admissible clock-form $u$:

$$
h_{\mu\nu}
=
q_{\mu\nu}
-2\frac{u_\mu u_\nu}{q^{-1}(u,u)}.
$$

In a $q$-orthonormal frame adapted to $u$, this expression gives

$$
\operatorname{sign}(h)=(-,+,+,+).
$$

This resolves the signature. But it does not prove, by itself, a positive inner product, unitariety, or a self-adjoint Hamiltonian. These points belong to the operational reconstruction.

## 2. Euclidean Data of the Sector

Fix an effective GDQ window and an admissible background. From it, we consider Schwinger functions of effective fields of the sector:

$$
S_n^{a_1\cdots a_n}(x_1,\ldots,x_n)
=
\left\langle
\Phi_{a_1}(x_1)\cdots\Phi_{a_n}(x_n)
\right\rangle_E.
$$

Formally,

$$
S_n^{a_1\cdots a_n}(x_1,\ldots,x_n)
=
\frac1{Z_E}
\int
\Phi_{a_1}(x_1)\cdots\Phi_{a_n}(x_n)
e^{-S_E[\Phi]}
\mathcal D\Phi.
$$

Here $S_E$ is an effective Euclidean action induced by the GDQ sector. It does not replace the official action; it is the reconstructed layer used to test operational positivity.

## 3. Required OS Hypotheses

The sector must satisfy:

1. regularity of the distributions $S_n$;
2. Euclidean invariance in the flat sector, or local covariance in a curved background with flat recovery;
3. graded permutation symmetry;
4. reflection positivity;
5. cluster property.

The central condition is reflection positivity. Let $\mathcal D_+$ be the space of functionals supported on positive Euclidean times, and let $\Theta$ be the temporal reflection of the sector. We require

$$
\langle \Theta F\,F\rangle_E\ge0
\qquad
\forall F\in\mathcal D_+.
$$

In terms of Schwinger functions, for polynomial functionals

$$
F
=
\sum_i c_i
\Phi_{a_{i1}}(x_{i1})\cdots\Phi_{a_{im_i}}(x_{im_i}),
\qquad
x_{ik}^0>0,
$$

the condition is

$$
\sum_{i,j}
\bar c_i c_j\,
S_{m_i+m_j}
(\Theta x_{i m_i},\ldots,\Theta x_{i1},
x_{j1},\ldots,x_{jm_j})
\ge0.
$$

This positivity does not follow solely from $J^2=-1$, nor from the historical writing $t=-i\tau$, nor from the cancellation of exact forms on the causal boundary.

## 4. Hilbert Space and Hamiltonian

We define the semidefinite product:

$$
(F,G)
=
\langle \Theta F\,G\rangle_E.
$$

The null subspace is

$$
\mathcal N
=
\{F\in\mathcal D_+:(F,F)=0\}.
$$

After quotienting null norms and geometric redundancies $\mathcal G$, we obtain

$$
\mathcal H_{\rm phys}
=
\overline{
\mathcal D_+/
(\mathcal N+\mathcal G)
}.
$$

The positive Euclidean translations in time induce a contraction semigroup:

$$
T_E(a+b)=T_E(a)T_E(b),
\qquad
\|T_E(a)\|\le1,
\qquad
a\ge0.
$$

By the reconstruction theorem, there exists a positive self-adjoint operator $H$ such that

$$
T_E(a)=e^{-aH/\hbar},
\qquad
H=H^\dagger,
\qquad
H\ge0.
$$

The evolution in the reconstructed physical time is then

$$
U(t)=e^{-itH/\hbar}.
$$

By the spectral theorem, $U(t)$ is unitary.

## 5. Relationship with $\tau$, $t$, $z_\tau$, and $\gamma$

Physical time $t$ is not identified with $\tau$. The complex causal variable of GDQ remains

$$
z_\tau
=
\tau+i\nu_0t.
$$

The contour $\gamma\subset\mathbb C_{z_\tau}$ organizes the causal prescription, including retarded and advanced branches when applicable. The positivity of the norm, however, comes from the OS condition of the effective sector, not from $\gamma$ in isolation.

Therefore, the secure formulation is:

$$
\boxed{
\text{OS provides }(\mathcal H_{\rm phys},H,U(t));
\qquad
\gamma\text{ provides the compatible causal prescription in }z_\tau.
}
$$

## 6. Status

This is a sectorial conditional theorem. For each concrete sector, it is still necessary to verify regularity, positivity, domain, cluster, and the removal of null/gauge modes. When these hypotheses hold, the operational Lorentzian reconstruction is closed.
