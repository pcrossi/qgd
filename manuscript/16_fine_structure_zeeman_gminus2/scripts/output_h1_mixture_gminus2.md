# Chapter 16 — reduced derivation of $H_1$ by harmonic mixture

## Classification

Calculation of selection rule and reduced geometric magnitude for the Hessian mixture $H_1$. Does not use experimental values of $g_e$ or $g_\mu-2$.

## 1. Mechanism

The direct upper source is null for a uniform field. The first possible universal correction comes from the Hessian: the quadratic product of the leading mode contains a component in the first upper harmonic.

$$
\cos^2\vartheta
=
\frac12\left(1+\cos2\vartheta\right).
$$

Removing the constant mode already absorbed in the normalization, a component proportional to $\cos2\vartheta$ remains.

## 2. Normalized overlaps

- `beta12 = <u2, u1^2 - mean> = 2.820947917738782e-01`
- `beta11 = <u1, u1^2 - mean> = -2.724897264069244e-17`
- `beta13 = <u3, u1^2 - mean> = -3.814856169696941e-17`

The selection is specific: the square of the leading mode couples to mode 2, but not to mode 1 nor to mode 3 within numerical precision.

## 3. Block $H_C=H_0+\alpha H_1$

It was used:

$$
(H_1)_{12}=(H_1)_{21}=\beta_{12}\sqrt{K_1K_2}.
$$

This is the mixture term allowed by symmetry. The absolute sign and eventual third variation factors depend on the complete 8D Hessian; here the minimal geometric magnitude was fixed.

| lepton | Q39 role | M_l/M_e | K2 | H1_mix | eig_min | a obtained | file |
|---|---|---:|---:|---:|---:|---:|---|
| e | primary torsion | 1.000000000000000e+00 | 8.610225765836003e+02 | 2.428899844539588e+02 | 9.988372364602003e-01 | 1.161414653717859e-03 | `leptonic_h1mix_background_e_gminus2.npz` |
| mu | transverse/bispatial torsion | 2.067685934706287e+02 | 1.780324271066477e+05 | 3.492624481279508e+03 | 9.988372364659019e-01 | 1.161414653717858e-03 | `leptonic_h1mix_background_mu_gminus2.npz` |
| tau | three-dimensional saturation | 3.477446405098381e+03 | 2.994159863649186e+06 | 1.432319253188402e+04 | 9.988372364659279e-01 | 1.161414653717859e-03 | `leptonic_h1mix_background_tau_gminus2.npz` |

## 4. Verdict

The Hessian mixture route exists: $H_1$ is not forbidden by symmetry and its first angular magnitude is determined by $\beta_{12}$.

However, in the minimal block with $m_\perp=(0,1,0)$, this mixture alone does not alter $a$ metrologically, because the upper channel does not yet possess its own source and there is no diagonal/normalization correction derived from the complete third variation.

Conclusion: the next universal coefficient is not a new direct source and is also not closed by the angular mixture alone. It is necessary to evaluate the third/fourth variation of the official action on the 8D background to obtain the tensorial factor that accompanies $\beta_{12}$ and the diagonal corrections of $H_1$.
