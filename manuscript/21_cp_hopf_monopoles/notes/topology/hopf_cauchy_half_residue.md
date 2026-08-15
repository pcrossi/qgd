---
title: "Hopf--Cauchy and residue 1/2"
---

# Hopf--Cauchy and residue $1/2$

Consider a punctured disk normal to the defect:

$$
D^\ast
=
\{0<|z|<\varepsilon\}.
$$

A local spinorial section can be written:

$$
s(z)
=
z^{1/2}s_0(z),
$$

with $s_0$ holomorphic and non-zero.

The associated logarithmic form is:

$$
\Omega_S
=
d\log s
=
\frac12\frac{dz}{z}
+d\log s_0.
$$

Since $d\log s_0$ is holomorphic:

$$
\operatorname{Res}_{z=0}d\log s_0
=
0.
$$

Therefore:

$$
\operatorname{Res}_{z=0}\Omega_S
=
\frac12.
$$

By the residue theorem:

$$
\frac1{2\pi i}
\oint_\gamma
\Omega_S
=
\frac12.
$$

Converting to real action:

$$
\oint_\gamma dS_R
=
\frac h2
=
\pi\hbar.
$$

Thus:

$$
\exp
\left(
\frac{i}{\hbar}
\oint_\gamma dS_R
\right)
=
-1.
$$

This is the half-monodromy of the spinorial/Hopf sector.
