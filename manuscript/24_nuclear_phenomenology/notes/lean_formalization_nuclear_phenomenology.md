---
title: "Lean Formalization of Reduced Nuclear Phenomenology"
---

# Lean Formalization of Reduced Nuclear Phenomenology

This note records the exact boundary between formal proof, effective reduction, and numerical comparison in Chapter 24. The canonical code is [NuclearPhenomenology.lean](../../../formal/GDQ/NuclearPhenomenology.lean).

## 1. What Was Formalized

### 1.1 Alpha Channel

Having defined the reduced form:

$$
T_{1/2}(\nu,W)
=
\frac{\ln 2}{\nu}e^W,
$$

Lean proves that $T_{1/2}>0$ for $\nu>0$ and that the half-life grows monotonically with the exponent $W$. These are exact consequences of the reduced form. The code does not claim that the frequency $\nu$ or the exponent $W$ have already been calculated by the full nuclear Hessian.

### 1.2 Spin-Torsion Shells

For each sublevel with $j_2=2j$, the capacity is:

$$
d(j_2)=j_2+1=2j+1.
$$

Lean verifies the cumulative sums in the reduced spectral order:

$$
2,\ 8,\ 20,\ 28,\ 50,\ 82,\ 126.
$$

The proof is arithmetic and exact once the order of the sublevels is declared. The selection of this order by the angular Bismut spin-torsion Hessian remains a reduced derivation written in the chapter, not an 8D nuclear diagonalization internalized by the assistant.

### 1.3 Klein-Nishina and Thomson

The kinematic ratio:

$$
r(x,\theta)
=
\frac{1}{1+x(1-\cos\theta)}
$$

is strictly positive and satisfies $r\leq1$ for $x\geq0$. The normalized distribution:

$$
\mathcal K(x,\theta)
=
\frac12r^2
\left(
r+\frac1r-\sin^2\theta
\right)
$$

exactly obeys:

$$
\mathcal K(0,\theta)
=
\frac12(1+\cos^2\theta).
$$

The last step uses only $\sin^2\theta+\cos^2\theta=1$. Therefore, the Thomson limit is not a numerical coincidence. The 8D origin of the vertex and the $r_e^2$ prefactor remains conditional on the evaluation of the photonic projector and the higher variations of the official action.

### 1.4 Neutral Sector

For the reduced candidate:

$$
\chi_\nu
=
\frac{12}{25}e^{-\alpha/4},
\qquad
\lambda_2=\frac{\chi_\nu^2}{2},
\qquad
\lambda_3=\frac{6\pi}{5},
$$

Lean proves:

$$
\chi_\nu>0,
\qquad
\lambda_2>0,
\qquad
\lambda_3>0.
$$

Consequently, for a scale $S_\nu>0$, the candidate differences $S_\nu\lambda_2$ and $S_\nu\lambda_3$ are positive. This certifies the algebraic consistency of the candidate; it does not derive the coefficients $12/25$, $1/2$, or $6\pi/5$ from the neutral Hessian.

In the two-channel model, the operational factor:

$$
\mathcal P(\vartheta,\phi)
=
\sin^2(2\vartheta)\sin^2\phi
$$

formally satisfies:

$$
0\leq\mathcal P\leq1.
$$

### 1.5 Pair Production and Annihilation

For positive rest energies $E_e=m_ec^2$ and $E_N=M_Nc^2$, the nuclear threshold was formalized:

$$
E_{\gamma,\mathrm{th}}^{(N)}
=
2E_e
\left(
1+\frac{E_e}{E_N}
\right).
$$

Lean proves exactly:

$$
E_{\gamma,\mathrm{th}}^{(N)}
>
2E_e
$$

and:

$$
E_{\gamma,\mathrm{th}}^{(N)}
-2E_e
=
\frac{2E_e^2}{E_N}.
$$

The two leading rates were also formalized:

$$
\Gamma_{2\gamma}^{(0)}
=
\frac12\alpha^5\omega_e,
$$

$$
\Gamma_{3\gamma}^{(0)}
=
\frac{2(\pi^2-9)}{9\pi}
\alpha^6\omega_e,
$$

with proof of positivity for $\alpha>0$ and $\omega_e>0$. Finally, the reduced magnetic parameter:

$$
\chi_\gamma
=
\frac{E_\gamma}{2E_e}
\frac{B_\perp}{B_Q}
$$

is formally non-negative for non-negative physical inputs.

These proofs certify kinematics and signs. They do not calculate the $D^3\mathcal S_{\rm GDQ}$ and $D^4\mathcal S_{\rm GDQ}$ jets in the 8D background, nor do they promote positronium comparisons and nuclear production to action theorems.

## 2. What Was Not Promoted to a Theorem

The following were not transformed into Lean axioms:

1. the reduced blocks used in the alpha benchmark;
2. the RMS error of $0.067894$ decades;
3. the full spectral origin of the order of nuclear levels;
4. the photonic projector, the 8D Compton vertex, and the $r_e^2$ prefactor;
5. the coefficients of the neutral candidate;
6. the agreement of $\Delta m^2$ with reference values;
7. the historical $\delta_{\rm CP}$ phase;
8. the experimental positronium lifetimes and nuclear cross sections;
9. the asymptotic coefficient of magnetic opacity;
10. the value of the production and annihilation jets in the 8D background.

These items continue to be classified in the body of the chapter as proof of concept, asymptotic reduction, reduced candidate, or future metrological work.

## 3. Relation to the Official Action

The module does not define a new nuclear action. The physical chain remains:

$$
\mathcal S_{\rm ...}
\longrightarrow
\Phi_*
\longrightarrow
K^{\rm phys}
\longrightarrow
\text{projectors and boundary operators}
\longrightarrow
\text{observable}.
$$

Lean certifies exact consequences once the reduced operator has been obtained. The existence of the background and the functional evaluation of the Hessian blocks belong to the analytical and numerical proof of the physical domain.

The modules `GDQ.NuclearPhenomenology` and `GDQ.AstrophysicsCosmology` were jointly compiled; the complete canonical entry point passed in $8747$ tasks. The `#print axioms` audit of the five new theorems in this chapter returned only `propext`, `Classical.choice`, and `Quot.sound`, without any physical `axiom`, `sorry`, or `admit`.
