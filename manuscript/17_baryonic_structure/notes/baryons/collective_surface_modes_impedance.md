---
title: "Collective surface impedance"
---

# Collective surface impedance

## 1. Why Impedance Enters

The torsional profile $H_n$ provides the leading internal density of the neutron. The scattering observable, however, does not measure this bare density. It measures the response of the baryonic surface to the probe field.

In GDQ, this response must come from the physical surface Hessian, not from a new fundamental term.

## 2. Schur Form

Separate surface fluctuations into:

$$
\delta\Phi_\Sigma
=
\delta\Phi_{\rm obs}
\oplus
\Psi.
$$

Here $\delta\Phi_{\rm obs}$ is the directly probed channel and $\Psi$ are relaxable collective modes. The quadratic form is:

$$
Q_\Sigma
=
\langle\delta\Phi_{\rm obs},K_{oo}\delta\Phi_{\rm obs}\rangle
+
2\operatorname{Re}
\langle\delta\Phi_{\rm obs},J_\Sigma\Psi\rangle
+
\langle\Psi,K_{\Sigma}\Psi\rangle.
$$

Variationally eliminating the collective modes:

$$
K_\Sigma\Psi+J_\Sigma^\dagger\delta\Phi_{\rm obs}=0,
$$

therefore:

$$
\Psi
=
-K_\Sigma^{-1}J_\Sigma^\dagger\delta\Phi_{\rm obs}.
$$

Substituting back:

$$
\mathcal I_\Sigma(q)
=
-J_\Sigma^\dagger(q)
K_\Sigma^{-1}(q)
J_\Sigma(q).
$$

## 3. Three Minimum Modes

In the reduced surface model, we use:

$$
x=\frac{q^2}{\Lambda_E^2},
\qquad
\Lambda_E=\frac{\sqrt{12}}{r_p}.
$$

The minimum coupling vector is:

$$
J_\Sigma(q)
=
x
\begin{pmatrix}
j_0\\
j_1\\
j_2\sqrt{x}
\end{pmatrix}.
$$

The modes are:

1. $j_0$: normal displacement of the shell;
2. $j_1$: shear/magnetization;
3. $j_2$: non-local torsion.

Thus:

$$
\mathcal I_\Sigma(q)
=
-j_0^2\frac{x^2}{1+x}
-j_1^2\frac{x^2}{(1+x)^2}
-j_2^2\frac{x^3}{(1+x)^2}.
$$

Since all terms start at $q^4$, the impedance does not alter:

$$
G_E^n(0),
\qquad
\left.
\frac{dG_E^n}{dq^2}
\right|_0.
$$

It corrects the shape at intermediate $q$.

## 4. Status

The reduced calculation shows that the couplings can be chosen as positive norms of relaxable surface modes. The comparison with Galster is used as a compact shape benchmark, not as an ontological foundation.

For complete metrological closure, the same $j_i$ must be extracted directly from the complete physical baryonic Hessian.

Script:

[[../../scripts/collective_surface_modes|collective_surface_modes.py]]

Output:

[[../../scripts/output_collective_surface_modes|Output — collective surface modes]].
