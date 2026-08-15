---
title: "Global product, non-circularity and three stomata"
---

# Global product, non-circularity and three stomata

This note records the separation between the auxiliary global calculation and the local selection of three stomata. It avoids the mistake of choosing a topological class simply because it produces the desired number.

## 1. The global product does not generate three by itself

In the auxiliary cosmological space:

$$
K=T^5\times S^3,
$$

the Betti numbers come from Künneth:

$$
P_{T^5}(t)=(1+t)^5,
\qquad
P_{S^3}(t)=1+t^3.
$$

Hence:

$$
P_K(t)=(1+t)^5(1+t^3).
$$

The Betti numbers are:

$$
(1,5,10,11,10,11,10,5,1).
$$

The Euler characteristic is:

$$
\chi(K)=0.
$$

Thus, the product topology $T^5\times S^3$ does not automatically select three generations. Neither the order three of a subgroup nor the presence of $S^3$ is sufficient.

## 2. Flat Berry kernel

If the torus is treated as a flat product with constant holonomies, the Berry connection of the kernel is flat:

$$
F_B=0.
$$

Then:

$$
c_2(E_G)=0,
\qquad
N_{ab}=0.
$$

This negative result is important: it excludes the circular attempt to obtain three generations from a trivial family of holonomies on the flat torus.

## 3. When a global class can contribute

A real global contribution requires a mixed class:

$$
c_2(E_G)=a_4+b_1\smile u_3,
$$

where $a_4$ lives in the toroidal sector and $u_3$ represents the class of $S^3$. For an $SU(2)$ sector, the index contribution takes the form:

$$
{\rm Ind}
=
\frac16
\langle a_4\smile b_1,[T^5]\rangle.
$$

Define:

$$
N_{ab}=\langle a_4\smile b_1,[T^5]\rangle.
$$

Then:

$$
N_G=\frac{N_{ab}}6.
$$

Choosing $N_{ab}=18$ solely to obtain $N_G=3$ would be reverse engineering. Therefore, the chapter does not use this path as the foundation of the local count.

## 4. Non-circular local selection

Local selection starts from Noether and the Hopf horizontal distribution:

$$
\sum_{a=1}^{N}\mathbf T_a=0,
\qquad
\mathbf T_a\in\mathcal H,
\qquad
\dim_{\mathbb R}\mathcal H=2.
$$

An elementary junction needs to be closed, non-colinear, and isolated. In two horizontal dimensions:

$$
N=1
\quad\text{does not close,}
$$

$$
N=2
\quad\text{is colinear,}
$$

$$
N=3
\quad\text{is the first closed, non-colinear, and isolated.}
$$

For $N>3$, $N-3$ internal null modes appear. Therefore the first stable elementary junction is:

$$
N=3.
$$

With three co-oriented primitive stomata, APS additivity yields:

$$
{\rm Ind}_{\rm total}
=
\sum_{a=1}^{3}{\rm ind}_{a}
=
3.
$$

Since each primitive unit corresponds to six integer units in the $\mathbb Z_6$ gluing:

$$
A=6\,{\rm Ind}_{\rm total}=18,
\qquad
N_G=\frac A6=3.
$$

## 5. Computational verification

The script:

$$
{\tt scripts/global_product_three_stomata.py}
$$

reproduces the Betti numbers of $T^5\times S^3$, confirms $\chi=0$, shows that the flat kernel has $N_{ab}=0$, and verifies the non-circular count by three stomata.
