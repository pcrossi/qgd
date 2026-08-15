---
title: "Lean Formalization of Reduced Astrophysics and Cosmology"
---

# Lean Formalization of Reduced Astrophysics and Cosmology

The canonical code for this chapter is [AstrophysicsCosmology.lean](../../../formal/GDQ/AstrophysicsCosmology.lean). It reuses the results already certified in [GravityCosmology.lean](../../../formal/GDQ/GravityCosmology.lean), [ElectroweakStability.lean](../../../formal/GDQ/ElectroweakStability.lean), and [HydrogenSpectrum.lean](../../../formal/GDQ/HydrogenSpectrum.lean).

This reuse is important: dark energy, critical acceleration, electroweak minimum, and protonic response are not four new actions. They are projections and conditional reductions of the official action.

## 1. Regular Core

If the central mass profile has leading term:

$$
m(r)=m_3r^3+O(r^5),
$$

then the lapse has leading term:

$$
A(r)
=
1-\frac{2Gm_3}{c^2}r^2+O(r^4).
$$

Defining:

$$
\Lambda_{\rm core}
=
\frac{6Gm_3}{c^2},
$$

Lean proves exactly:

$$
1-\frac{2Gm_3}{c^2}r^2
=
1-\frac{\Lambda_{\rm core}}{3}r^2.
$$

It also certifies the non-negativity of the core curvature expressions for $\Lambda_{\rm core}\geq0$. The existence of a global solution with the above expansion remains a result of the reduced radial saddle, not a purely algebraic consequence.

## 2. Torsion and Schur Stability

From the contraction:

$$
|H|^2=6q_T^2\rho^2
$$

follows the reduced quartic rigidity:

$$
\lambda_T=q_T^2\geq0.
$$

The minimum isotropic normalization of the three channels formally satisfies:

$$
1^2+1^2+1^2=3.
$$

For an eliminated block with gap $\lambda_B>0$, the Schur scalar gap is:

$$
\lambda_{\rm Schur}
=
\lambda_A-\frac{J^2}{\lambda_B}.
$$

The code demonstrates:

$$
J^2<\lambda_A\lambda_B
\quad\Longrightarrow\quad
\lambda_{\rm Schur}>0.
$$

This is the exact condition used to interpret the small Schur ratios of the reduced calculation. The numerical values of the gaps are not Lean axioms.

## 3. Horizon and Information

For positive surface gravity,

$$
T_H=\frac{\kappa_H}{2\pi}>0.
$$

For a channel weight $0\leq w\leq1$, Lean proves:

$$
-w\ln w\geq0,
$$

and, for a pure channel,

$$
-1\ln1=0.
$$

This certifies the entropy algebra used in the unitary toy model. It does not construct a physical Page curve. That curve requires the real spectral projectors of the covariant Hessian of the background with horizon.

## 4. Electroweak Scale and Surface Radius

Under $a_2<0<a_4$, the reduced amplitude:

$$
\beta_*=\sqrt{-\frac{a_2}{a_4}}
$$

satisfies exactly:

$$
\beta_*^2=-\frac{a_2}{a_4}.
$$

The formalization also proves the positivity of the normalizations:

$$
v_{\rm global}
=
M_p\frac{6\pi^5}{7}
$$

for $M_p>0$, and:

$$
r_p^{\rm surf}
=
\frac18
\left(1+\frac{\alpha}{4}\right)
\epsilon_{\rm eff}
\frac{3\Lambda_C}{2}
$$

for $\alpha\geq0$, $\epsilon_{\rm eff}>0$, and $\Lambda_C>0$.

If the contact response scales as $\mu^3$, reduced masses $0\leq\mu_{\rm light}<\mu_{\rm heavy}$ imply:

$$
0
\leq
\left(\frac{\mu_{\rm light}}{\mu_{\rm heavy}}\right)^3
<1.
$$

This formalizes the relative suppression of the electronic probe. The absolute values of $H_p^{\rm surf}$ and $J_{p,\ell}$ still need to be evaluated.

## 5. Neutral Radiative Comb

Conditioned on the existence of the radiative channel between conjugate neutral orientations, the cold energy per photon was defined by:

$$
E_{\gamma,*}^{(ij)}
=
\frac{m_i+m_j}{2}c^2.
$$

Lean proves that this energy is symmetric under $i\leftrightarrow j$ and strictly positive when $m_i+m_j>0$. For $hc>0$, the wavelength:

$$
\lambda_{ij,*}
=
\frac{2hc}{(m_i+m_j)c^2}
$$

is strictly positive. Cosmological transport:

$$
\lambda_0
=
(1+z)\lambda_*
$$

preserves positivity and satisfies $\lambda_0\geq\lambda_*$ for $z\geq0$.

This certifies the kinematic core of the comb and the redshift. It does not prove that the jet $C_{ij\gamma\gamma}^{\rm GDQ}$ is non-zero and does not determine the spectral intensity.

## 6. Limits Preserved

The module does not state:

1. general existence of an 8D saddle with horizon;
2. global geodesic extension;
3. stability of all polar and mixed sectors;
4. physical Page curve;
5. joint solution of CMB, BAO, supernovae, BBN, and lensing;
6. integral derivation of $Z_\beta$;
7. absolute metrology of each probe's radius;
8. existence and value of the torsion--torsion--radiation channel;
9. absolute brightness of the neutral comb and its separation from dust emission.

These points remain explicit in the chapter. The numerical comparisons test the declared reductions; they do not replace the missing functional links.

The modules `GDQ.NuclearPhenomenology` and `GDQ.AstrophysicsCosmology` were jointly compiled; the complete canonical entry point passed in $8747$ tasks. The `#print axioms` audit of the five new theorems of the comb and redshift returned only `propext`, `Classical.choice`, and `Quot.sound`, without any physical `axiom`, `sorry`, or `admit`.
