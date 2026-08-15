---
title: "Beta decay and fourth variation"
---

# Beta decay and fourth variation

Beta decay is treated as a transition between backgrounds:

$$
n\to p+e^-+\bar\nu_e.
$$

The antineutrino is a neutral torsional mode:

$$
\psi_{\bar\nu}
\in
\ker D_{0,-3/2}^{(0)}.
$$

## 1. Physical Statement

The error to avoid is treating:

$$
Q_\beta
=
M_n-M_p-m_e
$$

as a fixed antineutrino energy. The correct balance is:

$$
M_nc^2-M_pc^2
=
E_e+E_{\bar\nu}+E_{\rm recoil}.
$$

In the leading limit where proton recoil is neglected:

$$
E_{\bar\nu}
=
\Delta M-E_e,
\qquad
m_e\le E_e\le\Delta M.
$$

Thus, GDQ must reproduce a continuous spectrum of electrons, not a monoenergetic line.

## 2. Variational Origin of the Amplitude

The effective amplitude is:

$$
\mathcal V_{\rm eff}^{(4)}
=
\mathcal S_{\rm GDQ}^{(4)}
-
\mathcal S_{\rm GDQ}^{(3)}K_\perp^{-1}
\mathcal S_{\rm GDQ}^{(3)}
+
\text{permutations}.
$$

Here:

- $\mathcal S_{\rm GDQ}^{(4)}$ is the fourth physical variation of the official action in the baryonic background;
- $\mathcal S_{\rm GDQ}^{(3)}K_\perp^{-1}\mathcal S_{\rm GDQ}^{(3)}$ is the elimination of unobserved transverse modes by Schur complement;
- $K_\perp$ is the physical Hessian in the modes orthogonal to the matching submanifold;
- the permutations impose the symmetrization compatible with the torsional orientations of the channels.

Therefore, GDQ does not add a fundamental Fermi vertex. The effective vertex is the local residue of the fourth variation projected onto the torsional surgery.

## 3. Reduction by Symmetries

Time homogeneity, energy conservation, charge conservation, torsional flux conservation, and residual isotropy restrict the unpolarized sector to two invariants:

$$
\mathcal M_0
=
C_SS+C_TT.
$$

In the unpolarized sector:

$$
\frac12\sum_{\rm spins}|\mathcal M_0|^2
=
2|C_S|^2+6|C_T|^2.
$$

We define:

$$
\mathcal J_3^2
:=
2|C_S|^2+6|C_T|^2.
$$

This is the contracted norm that enters the total rate. It does not determine the angular correlations on its own, since these depend on the relative ratio and phase between $C_S$ and $C_T$.

The reduced coefficients are causal residues:

$$
C_A
=
\frac{\hbar}{\Lambda_C^2}
\frac{2\pi i}{(4\pi)^4}
[z^3]F_A,
\qquad
A\in\{S,T\}.
$$

## 4. Continuous Phase Space

The leading phase space is:

$$
I_\beta
=
\int_{m_e}^{\Delta M}
p_eE_e(\Delta M-E_e)^2\,dE_e,
\qquad
p_e=\sqrt{E_e^2-m_e^2}.
$$

The minimum differential form is:

$$
\frac{d\Gamma}{dE_e}
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}
p_eE_e(\Delta M-E_e)^2.
$$

If surface and recoil effects are included, the correct form is:

$$
\frac{d\Gamma}{dE_e}
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}
p_eE_e(\Delta M-E_e)^2
\mathcal C_{\rm geom}(E_e),
$$

with:

$$
\mathcal C_{\rm geom}
=
1+\delta_{\rm surf}
+\delta_{\rm recoil}
+\delta_{\rm rad}
+\delta_{\rm tors}
+\cdots .
$$

These terms are geometric responses of the charged channel, surface, recoil, and torsion. They do not alter the official action.

## 5. Status

The beta block is closed for:

1. endpoint correction;
2. GDQ channels $p$, $e^-$, and $\bar\nu_e$;
3. reduced effective amplitude;
4. minimum continuous spectrum;
5. total rate.

It remains conditional for:

1. individual separation of $C_S$ and $C_T$;
2. angular correlations and polarized observables;
3. recoil and metrological fine differential shape;
4. higher-order surface responses.

Self-contained verification:
[[../../scripts/output_validate_free_beta_complete|Output — beta decay validation GDQ]].
