---
title: "Lean Formalization of Simple Applications"
---

# Lean Formalization of Simple Applications

The new module [SimpleApplications.lean](../../../../formal/GDQ/SimpleApplications.lean) certifies the algebraic identities specific to this chapter. The wall and Hartman results reuse canonical modules already employed in Chapter 12:

- [DetectorDtNSchur.lean](../../../../formal/GDQ/DetectorDtNSchur.lean);
- [TransportInterference.lean](../../../../formal/GDQ/TransportInterference.lean).

This reuse avoids presenting the same theorem as if it were a new physical hypothesis.

## 1. Ideal Well

The reduced spectrum is defined by:

$$
E_n
=
\frac{\hbar^2\pi^2n^2}{2mL^2}.
$$

The module proves its non-negativity for $m>0$ and $L\neq0$, and its positivity when also $\hbar\neq0$ and $n\neq0$.

The circulation route uses:

$$
2pL=nh,
\qquad
p=\frac{nh}{2L}.
$$

With $h=2\pi\hbar$:

$$
\frac{p^2}{2m}
=
\frac{\hbar^2\pi^2n^2}{2mL^2}.
$$

Thus, Dirichlet quantization and circulation closure provide exactly the same energy in the ideal domain.

## 2. Gaussian Oscillator

For:

$$
R(x)=Ae^{-\alpha x^2/2},
$$

we have:

$$
\frac{R''}{R}
=
\alpha^2x^2-\alpha.
$$

The reduced stationary energy is:

$$
E(x)
=
\frac{1}{2}m\omega^2x^2
-
\frac{\hbar^2}{2m}
\left(
\alpha^2x^2-\alpha
\right).
$$

The module proves that:

$$
\alpha=\frac{m\omega}{\hbar}
$$

exactly cancels the dependence on $x$ and yields:

$$
E_0=\frac{1}{2}\hbar\omega.
$$

It also certifies the constant spacing:

$$
E_{n+1}-E_n=\hbar\omega
$$

for the reduced ladder $E_n=\hbar\omega(n+1/2)$.

## 3. Ideal Casimir

Using the transverse finite part and the spectral value:

$$
-\frac{1}{6\pi}
\pi^3
\frac{1}{120},
$$

the module simplifies exactly:

$$
-\frac{1}{6\pi}
\pi^3
\frac{1}{120}
=
-\frac{\pi^2}{720}.
$$

Consequently:

$$
\frac{\Delta E}{A}
=
-\frac{\pi^2\hbar c}{720a^3}.
$$

The algebraic relation to pressure is:

$$
P(a)
=
\frac{3}{a}\frac{\Delta E}{A}
=
-\frac{\pi^2\hbar c}{240a^4}.
$$

For $\hbar>0$, $c>0$, and $a\neq0$, the module proves $P<0$. The dimensional continuation and $\zeta(-3)=1/120$ continue the declared spectral technique of the human proof; Lean certifies the algebra leading to the coefficients $720$ and $240$.

## 4. Molecular Rotor

In the order necessary to obtain the $L^4$ term, the radial energy is:

$$
E(x)
=
\frac{L^2}{2\mu R_0^2}
-
\frac{L^2}{\mu R_0^3}x
+
\frac{1}{2}\mu\omega_e^2x^2.
$$

The stationary displacement is:

$$
x_\ast
=
\frac{L^2}{\mu^2\omega_e^2R_0^3}.
$$

Substituting:

$$
E(x_\ast)
=
\frac{L^2}{2\mu R_0^2}
-
\frac{L^4}{2\mu^3\omega_e^2R_0^6}.
$$

With $L^2=\hbar^2J(J+1)$:

$$
B
=
\frac{\hbar^2}{2\mu R_0^2},
\qquad
D
=
\frac{\hbar^4}{2\mu^3\omega_e^2R_0^6}.
$$

The module also proves:

$$
D
=
\frac{4B^3}{\hbar^2\omega_e^2}.
$$

These identities do not calculate $\mu$, $R_0$, or $\omega_e$ of a real molecule. These data must be obtained from the Hessian of the molecular background for the result to become an absolute prediction.

## 5. Wall and Hartman

The existing modules prove:

1. the profile of the reduced wall;
2. the positive impedance $\lambda\coth(\lambda L)$;
3. the non-negativity of the interface Schur under the physical hypotheses;
4. the saturation:

$$
D_{\rm prop}(L)
\longrightarrow
\frac{\sqrt{g_0}}{\kappa}.
$$

The relation $g_{xx}\propto\rho$ remains a hypothesis of the reduced evanescent channel. The formalization does not promote it to a universal identity of the official action.

## 6. Scope

The formalization certifies ideal correspondence and reductions. It does not claim to have calculated:

1. the impedance of a specific material wall;
2. the time packet and detector of a real barrier;
3. the dispersive response of real plates;
4. the complete molecular background;
5. new fundamental parameters.
