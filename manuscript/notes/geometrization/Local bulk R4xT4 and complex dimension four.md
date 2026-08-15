---
title: "Local bulk R4xT4 and complex dimension four"
type: derivation
status: verified-definition
---

# Local bulk $\mathbb R^4\times T^4$ and complex dimension four

## 1. Real product

Write

$$
T^4=S^1_1\times S^1_2\times S^1_3\times S^1_4.
$$

Each circle has real dimension one. Therefore

$$
\dim_{\mathbb R}T^4=4.
$$

By the additivity of dimension in products,

$$
\dim_{\mathbb R}(\mathbb R^4\times T^4)=4+4=8.
$$

## 2. Complex structure

Locally, choose eight real coordinates and group them into four pairs:

$$
z^a=x^a+iy^a,
\qquad
a=1,\ldots,4.
$$

The compatible integrable complex structure transforms each real pair into a complex axis. Therefore

$$
\dim_{\mathbb C}M=\frac12\dim_{\mathbb R}M=4.
$$

This calculation verifies the consistency of the definition; it does not dynamically select the number four.

## 3. Orientability, spin and parallelizability

$\mathbb R^4$ and $T^4$ are parallelizable. The product of parallelizable manifolds is also parallelizable, therefore

$$
TM\cong M\times\mathbb R^8.
$$

Consequently, the positive Stiefel--Whitney classes of the tangent bundle vanish, in particular

$$
w_2(TM)=0.
$$

Thus, $M$ admits spin structures. The choice of a spin structure and the relevant antiperiodic sector still constitutes additional data; it does not follow from abstract existence alone.

## 4. Compactness

$T^4$ is compact, but $\mathbb R^4$ is not. Therefore, $M$ is not compact. Global integrals require adequate decay in the $\mathbb R^4$ factor, declared auxiliary compactification, or another explicit functional realization.
