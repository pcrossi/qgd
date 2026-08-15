---
title: "Chiral selection Hopf--Bismut"
---

# Chiral selection Hopf--Bismut

## 1. Statement

This note establishes which internal space carries the axial Hopf vector used in the geometric Stern--Gerlach.

The technical point is simple: the apparatus chooses a direction $\mathbf n$; it does not choose the three-dimensional space where this direction lives. This space already comes from the normal complex structure of the stoma and from the Bismut connection.

## 2. Normal Slice

The regular normal slice of a primitive stoma is locally:

$$
\mathbb C^2\simeq\mathbb R^4.
$$

Write:

$$
z_1=x^1+ix^2,
\qquad
z_2=x^3+ix^4.
$$

With orthonormal coframe $e^a=dx^a$, we adopt the official complex orientation:

$$
e^1\wedge e^2\wedge e^3\wedge e^4>0.
$$

The elementary Hermitian form is:

$$
\Omega_1
=
e^1\wedge e^2
+
e^3\wedge e^4.
$$

In this orientation:

$$
*\Omega_1=\Omega_1.
$$

## 3. Hyperkähler Triplet

The quaternionic structure of $\mathbb R^4$ provides three 2-forms:

$$
\begin{aligned}
\Omega_1&=e^1\wedge e^2+e^3\wedge e^4,\\
\Omega_2&=e^1\wedge e^3-e^2\wedge e^4,\\
\Omega_3&=e^1\wedge e^4+e^2\wedge e^3.
\end{aligned}
$$

Applying the Hodge operator of the above orientation:

$$
*\Omega_i=+\Omega_i.
$$

Therefore, the natural axial triplet is the self-dual triplet:

$$
\Sigma_i^+=\frac{\Omega_i}{\sqrt2},
\qquad
i=1,2,3.
$$

The normalized basis satisfies:

$$
\langle\Sigma_i^+,\Sigma_j^+\rangle=\delta_{ij}.
$$

## 4. Relationship with Hopf

For $u=(z_1,z_2)^T\in S^3\subset\mathbb C^2$, the Hopf map is:

$$
n_i(u)=u^\dagger\sigma_i u,
\qquad
\mathbf n(u)\in S^2.
$$

The axial form associated with the internal state is:

$$
\Omega_{\rm Hopf}(u)
=
n^i(u)\Sigma_i^+.
$$

Thus, the internal orientation of the soliton is a direction within $\operatorname{span}\{\Sigma_1^+,\Sigma_2^+,\Sigma_3^+\}$.

This is the geometric version of the operational fact that a normalized spinor defines a point in $\mathbb CP^1\simeq S^2$.

## 5. Role of the Bismut Connection

The Bismut connection preserves the metric and the complex structure:

$$
\nabla^B g=0,
\qquad
\nabla^B J=0.
$$

Therefore, as long as the admissible evolution does not invert the complex orientation or cross a degeneracy, it can rotate and dress the internal basis, but it does not automatically swap the $SU(2)_+$ sector for the $SU(2)_-$ sector.

The sector used by the apparatus is therefore:

$$
\omega_{\rm SG}(P)
=
n^i(P)\Sigma_i^+.
$$

## 6. What the Apparatus Does

The classical field of the apparatus provides a magnetic source lifted to the bulk. Projecting this source onto the triplet above, one obtains an interface vector $\mathbf j_{\rm SG}$.

The effective direction of the Stern--Gerlach is:

$$
\mathbf n_{\rm app}
=
\frac{\mathbf j_{\rm SG}}{|\mathbf j_{\rm SG}|}.
$$

The two channels are then the projectors:

$$
P_{\mathbf n_{\rm app}}^\pm
=
\frac12
\left(
I\pm \mathbf n_{\rm app}\cdot\sigma
\right).
$$

This chain preserves the essential distinction:

$$
\boxed{
\text{the complex structure selects the triplet;}
\qquad
\text{the apparatus selects a direction within the triplet.}
}
$$

## 7. Limits

The result above does not calculate the metrological intensity of the apparatus response by itself. This intensity depends on the real classical source, the DtN operator of the interface, and the causal mobility. What is demonstrated here is the correct geometric domain of the axial coupling.

## 8. Symbolic Verification

The script `scripts/verify_sg_hopf_bismut_triplet.py` calculates the Hodge operator on the basis of 2-forms of $\mathbb R^4$, verifies that the three forms $\Omega_i$ are self-dual, and confirms that the basis $\Sigma_i^+$ is orthonormal.
