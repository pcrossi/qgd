---
title: "Spin, Hopf and Cauchy residue"
---

# Spin, Hopf and Cauchy residue

## 1. Statement

This note formalizes the GDQ reading of spin $1/2$ as a Hopf half-monodromy and Cauchy residue. It does not replace the main proof by spin structure, Clifford, and double covering; it explains why the physical language of circulation is compatible with that proof.

The main proof of the chapter is:

$$
P_{\rm Spin}(N)\to N,
\qquad
\psi\in\Gamma(S\otimes E),
\qquad
U(2\pi)=-I,
\qquad
U(4\pi)=I.
$$

The reading of this note is:

$$
\operatorname{Res}_{z=0}\Omega_S
=
\frac12
\quad
\Longrightarrow
\quad
\oint dS_R
=
\frac h2
\quad
\Longrightarrow
\quad
\operatorname{Hol}=-1.
$$

## 2. Geometric data used

We assume a complex normal neighborhood of the stoma. Locally, we choose a transverse complex coordinate $z$ in a punctured disk:

$$
D^\ast
=
{0<|z|<\varepsilon}.
$$

The point $z=0$ represents the removed core of the topological defect. The circulation boundary is the simple loop:

$$
\gamma_r:
|z|=r.
$$

In the Hopf description, the full normal slice is compatible with:

$$
S^3\subset\mathbb C^2,
\qquad
S^1\hookrightarrow S^3\to S^2\simeq\mathbb{CP}^1.
$$

The normalized spinor lives in:

$$
u\in S^3\simeq SU(2),
$$

and the physical observable direction is the projector:

$$
P=uu^\dagger\in\mathbb{CP}^1\simeq S^2.
$$

Since:

$$
u\sim -u
$$

represents the same physical projector, the observable orientation lives in the projective quotient. This is the geometric origin of the double covering.

## 3. Meromorphic form of half-monodromy

A local spinor sector can be represented by a section with square-root behavior around the defect:

$$
s(z)=z^{1/2}s_0(z),
$$

where $s_0$ is holomorphic and non-zero in the disk. The associated logarithmic connection is:

$$
\Omega_S
=
d\log s
=
\frac12\frac{dz}{z}
+
d\log s_0.
$$

Since $d\log s_0$ is holomorphic inside $\gamma_r$, its residue is zero:

$$
\operatorname{Res}_{z=0}d\log s_0
=
0.
$$

Thus:

$$
\operatorname{Res}_{z=0}\Omega_S
=
\frac12.
$$

By the Cauchy residue theorem:

$$
\frac{1}{2\pi i}\oint_{\gamma_r}\Omega_S
=
\operatorname{Res}_{z=0}\Omega_S
=
\frac12.
$$

Thus, the normalized spinor circulation number is:

$$
N_S(\gamma_r)
:=
\frac{1}{2\pi i}\oint_{\gamma_r}\Omega_S
=
\frac12.
$$

This value is topological: deformations of $\gamma_r$ that do not cross the core of the stoma do not alter the residue.

## 4. Conversion to physical phase

In GDQ,

$$
S_R
=
\frac{\hbar}{2i}(f-\bar f).
$$

If the normal spinor sector carries half-monodromy, the circulation of the real phase around the stoma is:

$$
\oint_{\gamma_r}dS_R
=
h\,N_S(\gamma_r)
=
\frac h2
=
\pi\hbar.
$$

The physical phase holonomy is:

$$
\operatorname{Hol}_{\gamma_r}
=
\exp\left(
\frac{i}{\hbar}\oint_{\gamma_r}dS_R
\right)
=
\exp(i\pi)
=
-1.
$$

For two turns:

$$
\operatorname{Hol}_{\gamma_r^2}
=
(-1)^2
=
1.
$$

Therefore:

$$
2\pi\mapsto -1,
\qquad
4\pi\mapsto +1.
$$

This is exactly the behavior of spin $1/2$.

## 5. Relation with Hopf

The Hopf fibration geometrically realizes the same structure. The map:

$$
SU(2)\to SO(3)
$$

is double. A physical rotation of $2\pi$ closes in $SO(3)$, but its lift in $SU(2)$ maps:

$$
u\mapsto -u.
$$

Only a rotation of $4\pi$ returns:

$$
u\mapsto u.
$$

In local coordinates, this double lift appears as the square-root section $z^{1/2}$. The logarithmic connection of this root is the meromorphic form with residue $1/2$.

Thus:

$$
\text{Hopf/double covering}
\quad\Longleftrightarrow\quad
\text{local square root}
\quad\Longleftrightarrow\quad
\operatorname{Res}\Omega_S=\frac12.
$$

## 6. Relation with the official action

The residue reading does not change the official action of GDQ. It identifies an admissible class of boundary and spinor sector of the stoma.

The role of the official action is to select backgrounds and physical Hessians. The role of the residue is to classify the permitted normal monodromy when the defect already has a Hopf/spinor class.

Therefore:

$$
\boxed{
\text{Cauchy's theorem proves the topological quantization of the half-circulation, once the Hopf/spinor class of the defect is fixed.}
}
$$

## 7. What was proven and what was not proven

What was proven:

1. if the local section around the stoma is spinor/Hopf, then its logarithmic form has residue $1/2$;
2. by Cauchy's theorem, the normalized circulation is rigidly $1/2$;
3. the physical phase satisfies $2\pi\mapsto -1$ and $4\pi\mapsto +1$;
4. the interpretation by circulation is compatible with the spinor proof of the chapter.

What was not proven in this note:

1. which of the internal spin structures is dynamically selected;
2. which specific soliton realizes the Dirac sector of the electron;
3. the complete spectrum of masses, charges, and spinor modes.

These items belong to the subsequent dynamic problem of sector selection, not to the Hopf/residues gap.
