---
title: "Proofs, lemmas, and definitions — Chapter 17"
---

# Proofs, lemmas, and definitions — Chapter 17

This note consolidates the correct line of the GDQ baryonic sector. It preserves the proofs and reduced calculations used in the chapter without importing superseded historical paths.

The physical statement is:

$$
\text{baryon}
=
\text{glued trimodal soliton with integer charge and surface torsion}.
$$

The spectral cycle used to extract invariants is:

$$
\mathcal C_B\simeq T^5_{\rm braided}\times S^3_{\rm hol}.
$$

This cycle is auxiliary. The official local bulk remains $\mathbb R^4\times T^4$.

## 1. Reduced Volume and Dominant Mass

Each baryonic chamber contributes reduced volume:

$$
\operatorname{Vol}(\mathcal F_a)=2\pi^5.
$$

For three stomata,

$$
\mathcal I_B^{\rm bulk}
=
\sum_{a=1}^{3}\operatorname{Vol}(\mathcal F_a)
=
6\pi^5.
$$

In the reduced electronic scale,

$$
E_0=M_ec^2,
\qquad
\frac{M_B}{M_e}=\mathcal I_B.
$$

Therefore the dominant mass of the baryon is:

$$
\left(\frac{M_B}{M_e}\right)_{\rm bulk}
=
6\pi^5.
$$

Numerically,

$$
6\pi^5=1836.118108711688.
$$

## 2. Torsional Surface of the Proton

The reduced surface transgression provides:

$$
\mathcal I_p^\partial
=
\frac{3\alpha(1+2\pi^4)}{4\pi^3}.
$$

Thus,

$$
\frac{M_p}{M_e}
=
6\pi^5+\frac{3\alpha(1+2\pi^4)}{4\pi^3}.
$$

Equivalent form:

$$
\frac{M_p}{M_e}
=
\frac{3\left[\alpha(1+2\pi^4)+8\pi^8\right]}{4\pi^3}.
$$

With $\alpha^{-1}=137.035999177$,

$$
\frac{M_p}{M_e}
=
1836.152673188612.
$$

Subsequent comparison with $1836.152673430000$ gives relative error:

$$
-1.31464\times10^{-10}.
$$

## 3. Torsional Equilibrium of the Neutron

In the proton, the three tensions are co-oriented:

$$
\mathbf t_p=(1,1,1).
$$

In the stationary neutron, the inverted stoma carries twice the opposite torsion:

$$
\mathbf t_n=(1,1,-2).
$$

This configuration satisfies local conservation of the torsional current:

$$
\sum_a(\mathbf t_n)_a=1+1-2=0.
$$

In variational language,

$$
\delta_\vartheta\mathcal S_{\rm GDQ}=0
\quad\Longrightarrow\quad
dJ_{\rm tor}=0.
$$

The physical shear invariant is pairwise:

$$
I_{\rm sh}^2(\mathbf t)
=
\sum_{a<b}(t_a-t_b)^2.
$$

For the proton,

$$
I_{\rm sh}^2(\mathbf t_p)=0.
$$

For the neutron,

$$
I_{\rm sh}^2(\mathbf t_n)
=
(1-1)^2+(1+2)^2+(1+2)^2
=18,
$$

and therefore:

$$
I_{\rm sh}(\mathbf t_n)=3\sqrt2.
$$

## 4. Fredholm–Fano Projection and $\delta_B$

The stoma has three internal torsional channels. The local physical projection occurs in the four-dimensional real continuum. The reduced decomposition uses the $3$-$4$-$5$ triangle:

$$
\cos\theta_c
=
\frac{3}{\sqrt{3^2+4^2}}
=
\frac35.
$$

Since the fundamental variable is complex, the elementary real–imaginary norm is:

$$
\|1+i\|=\sqrt2.
$$

The reduced admittance is:

$$
\chi_B
=
\sqrt2\cos\theta_c
=
\frac{3\sqrt2}{5}.
$$

The boundary of the stoma is $S^3$, with:

$$
\operatorname{Vol}(S^3)=2\pi^2.
$$

Thus the reduced surface entropic energy is:

$$
E_\partial^{(0)}
=
\ln(2\pi^2).
$$

The reduced neutron torsional excess is:

$$
\delta_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5}
=
2.530825921868.
$$

Therefore,

$$
\frac{M_n}{M_e}
=
\frac{M_p}{M_e}+\delta_B
=
1838.683499110479.
$$

Subsequent comparison with $1838.683661730000$ gives relative error:

$$
-8.84434\times10^{-8}.
$$

Status: this is a reduced derivation conditional on the validity of the $3$-$4$-$5$ Fredholm–Fano projection of the torsional sector. The accepted value does not enter the derivation; it enters only afterward, as a comparison.

## 5. Charge as Integer Residue

The effective baryonic charge is obtained as the Cauchy residue of a connection form on the boundary cycle. Schematically,

$$
Q
=
\frac{1}{2\pi i}
\oint_\Gamma\mathcal A.
$$

Since $\Gamma$ involves singularities/stomata of the bundle, the integral belongs to the corresponding integer class:

$$
Q\in\mathbb Z.
$$

This reading explains why the observed total charge is integer at the global boundary. The internal distribution of tensions can be non-uniform without changing the total residue.

## 6. Torsional Profile of the Neutron

The neutron has zero total charge:

$$
G_E^n(0)=0.
$$

But the internal density does not have to be zero. Use the surface coordinate:

$$
\xi=r-r_p.
$$

The leading torsional separation is:

$$
\xi_+
=
-\frac12r_p\alpha_{\rm tor}^{(2)},
\qquad
\xi_-
=
\frac12r_p\alpha_{\rm tor}^{(2)},
$$

with:

$$
\alpha_{\rm tor}^{(2)}
=
2\alpha\ln(2\pi^2).
$$

The leading variational profile resolves Perelman's heat equation in the layer:

$$
\left(
\partial_\tau-\partial_\xi^2
\right)H_n(\xi,\tau)=0.
$$

With a dipolar initial condition,

$$
H_n(\xi,0)
=
|\mu_n|
\left[
\delta(\xi-\xi_+)-\delta(\xi-\xi_-)
\right],
$$

the solution is:

$$
H_n(\xi,\tau_n)
=
|\mu_n|
\left[
K_{\tau_n}(\xi,\xi_+)
-K_{\tau_n}(\xi,\xi_-)
\right],
$$

where:

$$
K_\tau(\xi,\xi_0)
=
\frac1{\sqrt{4\pi\tau}}
\exp\left[-{\frac{(\xi-\xi_0)^2}{4\tau}}\right].
$$

The natural width is:

$$
\sqrt{2\tau_n}
=
\frac12r_p\alpha_{\rm tor}^{(2)}.
$$

The leading electrical factor is:

$$
G_E^n(q^2)
=
\int H_n(\xi,\tau_n)
j_0(q(r_p+\xi))\,d\xi.
$$

Since,

$$
\int H_n\,d\xi=0,
$$

it follows that:

$$
G_E^n(0)=0.
$$

Low-energy expansion:

$$
j_0(qr)=1-\frac{q^2r^2}{6}+O(q^4).
$$

Thus,

$$
-6\left.\frac{dG_E^n}{dq^2}\right|_0
=
\int H_n(\xi,\tau_n)(r_p+\xi)^2\,d\xi.
$$

In the leading limit,

$$
\langle r_n^2\rangle
=
-2|\mu_n|\alpha_{\rm tor}^{(2)}r_p^2.
$$

The script `neutron_torsional_profile.py` preserves the calculation. The output records:

$$
\int H_n\,d\xi\simeq -9.535541374287\times10^{-18},
$$

compatible with zero total charge within the numerical error.

## 7. Beta Decay as Fourth Variation

The channel is:

$$
n\to p+e^-+\bar\nu_e.
$$

The antineutrino is the neutral torsional mode:

$$
\psi_{\bar\nu}\in\ker D_{0,-3/2}^{(0)}.
$$

The endpoint,

$$
Q_\beta=M_n-M_p-m_e,
$$

is not a fixed antineutrino energy. The correct balance is:

$$
M_nc^2-M_pc^2
=
E_e+E_{\bar\nu}+E_{\rm recoil}.
$$

In the leading limit without recoil:

$$
E_{\bar\nu}=\Delta M-E_e,
\qquad
m_e\le E_e\le\Delta M.
$$

The effective amplitude comes from the projected fourth variation of the official action:

$$
\mathcal V_{\rm eff}^{(4)}
=
\mathcal S_{\rm GDQ}^{(4)}
-
\mathcal S_{\rm GDQ}^{(3)}
K_\perp^{-1}
\mathcal S_{\rm GDQ}^{(3)}
+\text{permutations}.
$$

In the unpolarized sector, symmetries reduce the amplitude to two invariants:

$$
\mathcal M_0=C_SS+C_TT.
$$

The spin average yields:

$$
\frac12\sum_{\rm spins}|\mathcal M_0|^2
=
2|C_S|^2+6|C_T|^2.
$$

Define the contracted norm:

$$
\mathcal J_3^2
=
2|C_S|^2+6|C_T|^2.
$$

The coefficients are causal residues:

$$
C_A
=
\frac{\hbar}{\Lambda_C^2}
\frac{2\pi i}{(4\pi)^4}
[z^3]F_A,
\qquad
A\in\{S,T\}.
$$

## 8. Phase Space and Total Rate

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

The total rate is:

$$
\Gamma_n
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}I_\beta.
$$

The current reduced closure uses the GDQ relaxation law:

$$
\tau_n
=
\frac{32}{15}\alpha^{-11}
\frac{\hbar}{m_ec^2}.
$$

Equivalent in energy:

$$
\Gamma_E
=
\frac{\hbar}{\tau_n}
=
\frac{15}{32}\alpha^{11}m_ec^2.
$$

Equating with:

$$
\Gamma_E
=
\frac{\mathcal J_3^2}{2\pi^3}I_\beta,
$$

we obtain:

$$
\mathcal J_3^2
=
\frac{15\pi^3}{16}
\frac{\alpha^{11}m_ec^2}{I_\beta}.
$$

With:

$$
m_e=0.51099895069\,{\rm MeV},
\qquad
\Delta M=1.29333251\,{\rm MeV},
$$

the script `validate_free_beta_complete.py` finds:

$$
I_\beta
=
5.700456936530352\times10^{-17}\,{\rm GeV}^5,
$$

$$
\mathcal J_3^2
=
8.142351666635048\times10^{-10}\,{\rm GeV}^{-4},
$$

$$
\sqrt{\mathcal J_3^2}
=
2.853480623139931\times10^{-5}\,{\rm GeV}^{-2}.
$$

So,

$$
\Gamma_n
=
1.137140542406870\times10^{-3}\,{\rm s}^{-1},
$$

$$
\tau_n
=
879.398775004012\,{\rm s},
$$

and:

$$
T_{1/2}
=
609.552781481901\,{\rm s}.
$$

Posterior comparison:

| reference | $\tau_{\rm ref}$ s | difference s | relative difference |
|---|---:|---:|---:|
| average used 2026 | 878.300000000000 | 1.098775004013 | $1.251024711388\times10^{-3}$ |
| average used 2024/2025 | 878.400000000000 | 0.998775004012 | $1.137038938994\times10^{-3}$ |

Status: total reduced rate conditionally closed. The fine differential shape, recoil, angular correlations, and individual separation of $C_S$ and $C_T$ remain future metrology.

## 9. Paths That Do Not Enter as Positive Foundation

Do not use as proof:

- WKB coefficients $A_2,C_4,M_r$ without all gluing data;
- transplant of static stiffnesses from another sector as a third causal jet;
- arbitrary guess of parameters that has no return point;
- separated causal jets $[z^3]F_S$ and $[z^3]F_T$ when only the contracted norm is determined;
- absolute half-life obtained by adjusting coefficients to the experimental target.

These paths serve as audit or future program, not as positive line of the manuscript.

## 10. Self-Contained Scripts

| Script | Role | Classification |
|---|---|---|
| `derive_baryon_deltas.py` | Derives $\delta_B=\ln(2\pi^2)3\sqrt2/5$. | Reduced derivation. |
| `symbolic_derivation_baryon_masses.py` | Symbolically derives $M_p/M_e$, $\delta_B$ and $M_n/M_e$. | Self-contained symbolic derivation. |
| `calculate_baryon_masses.py` | Evaluates reduced masses. | Direct evaluation. |
| `neutron_torsional_profile.py` | Calculates $H_n$ and leading $G_E^n$. | Reduced variational profile. |
| `validate_free_beta_complete.py` | Calculates $I_\beta$, $\mathcal J_3$, $\tau_n$, $T_{1/2}$ and continuous spectrum. | Direct evaluation/convergence test/comparison. |
| `compare_neutron_tau.py` | Compares the reduced lifetime. | Phenomenological comparison. |

All of them write Markdown output to the same `scripts/` folder.

## 11. Status

| Block | Status | Limit |
|---|---|---|
| Three stomata | Structurally closed | Trimodal background. |
| $6\pi^5$ volume | Reduced closed | Mass ratio. |
| Proton | Closed in surface reduction | Fine metrology requires full Hessian. |
| Neutron | Structurally closed | Antiparallel shear. |
| $\delta_B$ | Conditionally closed | Depends on Fredholm–Fano projection. |
| $H_n$ profile | Closed as leading profile | Complete form factor requires real probe. |
| Continuous beta | Closed | Endpoint is not a fixed energy. |
| Lifetime | Conditionally closed | $10^{-3}$ level; future differential. |
