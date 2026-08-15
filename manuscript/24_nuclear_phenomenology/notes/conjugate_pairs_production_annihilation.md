---
title: "Note — Production and Annihilation of Conjugate Pairs"
---

# Note — Production and Annihilation of Conjugate Pairs

## 1. Statement and Status

This note extends the asymptotic electromagnetic sector of GDQ to:

$$
e^-+e^+
\longrightarrow
\gamma+\gamma,
$$

$$
\gamma+N
\longrightarrow
e^-+e^++N,
$$

e:

$$
\gamma+B_{\rm ext}
\longrightarrow
e^-+e^++B_{\rm ext}.
$$

The result has two layers that must not be confused:

1. the reciprocity and thresholds are structural consequences of the action, conservations, and domain;
2. the rates presented at the end belong to the projected effective electromagnetic sector and do not replace the evaluation of jets in the 8D background.

The status is:

$$
\boxed{
\text{conditional closure in the effective electromagnetic sector}.
}
$$

## 2. Conjugate Background

We write the constitutive field as:

$$
f
=
F+\frac{i}{\hbar}S_R.
$$

Charge conjugation reverses the orientation of the phase and the charge line:

$$
\mathsf C:
\left(
F,S_R,L_Q
\right)
\longmapsto
\left(
F,-S_R,L_Q^{-1}
\right).
$$

Since:

$$
\rho
=
e^{-F},
$$

the geometric density is preserved:

$$
\rho_{\mathsf C\Phi}
=
\rho_\Phi.
$$

The positron is, therefore, the electronic background in the conjugate class of boundary and holonomy. This does not mean that charge and spin are the same orientation: the Hopf circulation representing spin must be projected separately.

## 3. External Backgrounds

The nucleus and the magnet are not new fundamental terms. They are classical sources and boundary data:

$$
\Phi_N
=
\operatorname{Crit}_{\mathcal C_N}\mathcal S_{\rm GDQ},
$$

$$
\Phi_B
=
\operatorname{Crit}_{\mathcal C_B}\mathcal S_{\rm GDQ}.
$$

In the external limit, the nucleus fixes the charge flux:

$$
\frac{1}{2\pi i}
\oint_{\partial\Sigma_N}
\mathcal A_Q
=
Z,
$$

and the magnet fixes the classical connection, for example:

$$
\mathbf A_B
=
\frac12\mathbf B\times\mathbf r.
$$

These expressions specify the source classes. The complete saddle requires solving the official action in these classes.

## 4. Physical Jets and Reciprocity

After projecting gauge and constraints and eliminating internal modes by Schur, the reduced third variation defines:

$$
C_{\gamma+-}^{(X)}
=
D^3\mathcal S_{\rm red}[\Phi_X]
[\psi_\gamma,\eta_+,\eta_-],
\qquad
X\in\{0,N,B\}.
$$

Fréchet symmetry yields the algebraic permutation:

$$
C_{\gamma+-}^{(X)}
=
C_{+-\gamma}^{(X)}.
$$

For it to be physical reciprocity, the following are also required:

1. preserved causal domain;
2. self-adjoint reconstructed generator;
3. appropriate reality condition;
4. reversal of the magnetic background in reverse processes.

Under these hypotheses:

$$
\mathcal M_{i\to f}[B]
=
\overline{
\mathcal M_{f\to i}[-B]
}.
$$

The amplitudes are related, but the rates do not have to be equal because the phase spaces and sources are different.

## 5. Why Two Photons

A pair at rest has total timelike quadrimomentum:

$$
P^\mu
=
(2m_ec,\mathbf0),
\qquad
P^2>0.
$$

A single photon satisfies $k^2=0$ and cannot carry this quadrimomentum in vacuum. The minimum free channel is:

$$
e^-+e^+
\longrightarrow
\gamma+\gamma.
$$

In the center of mass:

$$
E_{\gamma,1}
=
E_{\gamma,2}
=
m_ec^2.
$$

The physical two-photon channel comes from the fourth variation or from two cubic vertices connected by the resolvent:

$$
\mathcal V_{\gamma\gamma+-}^{\rm phys}
=
D^4\mathcal S_{\rm red}
-
D^3\mathcal S_{\rm red}
G_{\rm int}
D^3\mathcal S_{\rm red}
+\text{permutations}.
$$

In the external Dirac--Bismut limit, the electromagnetic connection enters linearly, and the leading channel is formed by the two cubic insertions. A quartic solitonic contact may exist in the full 8D background and should not be discarded before calculation.

## 6. Selection of Two and Three Photons

If the total conjugate state has conjugation eigenvalue:

$$
\eta_{\mathsf C}
=
(-1)^{N_\gamma},
$$

the even sector allows two photons and the odd sector requires three in the lowest channel. This reading is conditional on the identification between the GDQ circulation eigenvalue and the conjugation of the reconstructed channel. It is not a purely kinematic identity.

## 7. Production in the Nuclear Field

For a nucleus initially at rest:

$$
\gamma+N
\longrightarrow
e^-+e^++N,
$$

the conservation of quadrimomentum yields:

$$
\boxed{
E_{\gamma,\rm th}^{(N)}
=
2m_ec^2
\left(
1+\frac{m_e}{M_N}
\right).
}
$$

In the heavy nucleus limit:

$$
E_{\gamma,\rm th}^{(N)}
\simeq
1.0219979\ {\rm MeV}.
$$

The nucleus provides recoil and interface impedance; the rest energy of the pair comes from the photon.

## 8. Production in a Magnetic Field

For propagation with angle $\theta$ relative to the field:

$$
E_\gamma\sin\theta
\geq
2m_ec^2.
$$

The correct critical scale in SI is:

$$
B_Q
=
\frac{m_e^2c^2}{e\hbar}
=
4.4140052\times10^9\ {\rm T}.
$$

The dimensionless parameter is:

$$
\chi_\gamma
=
\frac{E_\gamma}{2m_ec^2}
\frac{B\sin\theta}{B_Q}.
$$

A purely static magnetic field does not provide the rest energy on its own. It absorbs transverse momentum and modifies the spectrum; the photon provides energy.

## 9. Leading Rates in the Projected Sector

With the inherited $U(1)_Q$ normalization and the bound state of positronium:

$$
\Gamma_{2\gamma}^{(0)}
=
\frac12
\alpha^5
\frac{m_ec^2}{\hbar},
$$

$$
\Gamma_{3\gamma}^{(0)}
=
\frac{2(\pi^2-9)}{9\pi}
\alpha^6
\frac{m_ec^2}{\hbar}.
$$

The leading lifetimes are:

| Channel | reduced calculation | experimental reference | error |
|---|---:|---:|---:|
| $p$-Ps $\to2\gamma$ | $124.494196935$ ps | $125.142349422$ ps | $-0.517932\%$ |
| $o$-Ps $\to3\gamma$ | $138.673807699$ ns | $142.050000000$ ns | $-2.376763\%$ |

The residuals are not absorbed in parameters. They mark higher-order corrections and material response absent from the leading formula.

## 10. Nuclear Benchmark

In the limit of complete shielding:

$$
\sigma_N
=
\frac{28}{9}
Z^2\alpha r_e^2
\left[
\ln\left(183Z^{-1/3}\right)
-f_C(Z\alpha)
-\frac1{42}
\right],
$$

with:

$$
\regular_C(a)
=
a^2
\sum_{n=1}^{\infty}
\frac{1}{n(n^2+a^2)}.
$$

For $2.5$ GeV photons:

| Target | asymptotic calculation | measurement | deviation |
|---|---:|---:|---:|
| Al | $1.316166251$ barn | $1.22\pm0.17$ barn | $+0.566\sigma$ |
| Pb | $41.034539221$ barn | $34.6\pm6.6$ barn | $+0.975\sigma$ |

The comparison tests the electromagnetic reduction; it does not replace the complete nuclear structure.

## 11. Asymptotic Magnetic Opacity

In the regime $\chi_\gamma\ll1$, the asymptotic reduction is:

$$
\kappa_B
\simeq
0.23
\frac{\alpha}{\bar\lambda_C}
\frac{B_\perp}{B_Q}
\exp\left(
-\frac{4}{3\chi_\gamma}
\right).
$$

It demonstrates the exponential sensitivity, but is not an independent experimental comparison.

## 12. What Was Demonstrated

Established:

1. the conjugate positron background;
2. the nuclear and magnetic source function;
3. the impossibility of the single-photon channel in vacuum;
4. the nuclear and magnetic thresholds;
5. the variational form of the vertices;
6. the Ward identity in the projected limit;
7. leading rates and benchmarks without post-fitting.

In extension:

1. full 8D $\Phi_N$ and $\Phi_B$;
2. $P_{\rm phys}$ and the normalized modes in those backgrounds;
3. direct evaluation of $D^3\mathcal S_{\rm GDQ}$ and $D^4\mathcal S_{\rm GDQ}$;
4. polarizations, solitonic contacts, and higher-order corrections.

The script [[../scripts/reduced_electromagnetic_pairs.py]] reproduces thresholds, Ward identity, rates, and benchmarks.

## 13. Comparison References

- A. Ishida, “Precise measurement of positronium,” *Progress of Theoretical and Experimental Physics* **2012**, 04D003: <https://doi.org/10.1093/ptep/pts073>.
- J. M. Brabant, R. W. Kenney and R. Wallace, “Electron Pair-Production Cross Sections at 2.5 Bev,” *Physical Review* **107**, 604 (1957): <https://doi.org/10.1103/PhysRev.107.604>.
- T. Erber, “High-Energy Electromagnetic Conversion Processes in Intense Magnetic Fields,” *Reviews of Modern Physics* **38**, 626 (1966): <https://doi.org/10.1103/RevModPhys.38.626>.
