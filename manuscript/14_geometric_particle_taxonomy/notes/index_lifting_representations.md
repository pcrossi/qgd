---
title: "Index lifting to representations"
---

# Index lifting to representations

This note separates three objects that should not be confused:

1. $L_G$, the geometric line carrying the local index unit;
2. $E_C$ and $E_W$, the internal color and weak isospin bundles;
3. $L_Y$, the physical hypercharge line.

The separation is necessary because the index unit of the stoma is not a hypercharge. It counts chiral multiplicity. Hypercharge is a global descent constraint of the effective bundle.

## 1. Local geometric index

The primitive stoma provides:

$$
{\rm ind}D_G^+=1.
$$

If $V_R$ is an internally topologically trivial representation in the local patch, the twisted operator satisfies:

$$
{\rm Ind}_G(D_G^+\otimes V_R)
=
{\rm ind}(D_G^+)\,[R].
$$

Therefore:

$$
{\rm Ind}_G(D_G^+\otimes V_R)
=
[R].
$$

A local index unit creates a chiral copy of each admissible representation. It does not multiply hypercharges.

## 2. Content of one generation

With the admissible internal representations:

$$
E_{\rm gen}
=
(3,2)_{1/6}
\oplus
(\bar3,1)_{-2/3}
\oplus
(\bar3,1)_{1/3}
\oplus
(1,2)_{-1/2}
\oplus
(1,1)_1.
$$

The count of Weyl components is:

$$
6+3+3+2+1=15.
$$

Hence, a co-oriented primitive stoma provides one chiral generation:

$$
{\rm Ind}_{\rm stoma}=1
\quad\Rightarrow\quad
15\ \text{Weyl components}.
$$

With three stomata:

$$
3\times 15=45.
$$

## 3. Why not use the same line as hypercharge

If $L_G$ were identified with $L_Y$, fields with different hypercharges would receive different powers of the index line. This would change the chiral multiplicity of each multiplet and destroy the interpretation of a common generation.

In GDQ, the correct structure is:

$$
E_{\rm int}=E_C\oplus E_W\oplus L_Y,
$$

with $L_G$ only as a topological marker of the local APS unit. Hypercharge enters by global descent:

$$
\frac{
SU(3)_C\times SU(2)_L\times U(1)_Y
}{
\mathbb Z_6
}.
$$

## 4. Computational verification

The script:

$$
{\tt scripts/index_lifting_representations.py}
$$

calculates the component count per multiplet and verifies that one index unit generates $15$ Weyl components, while three units generate $45$.
