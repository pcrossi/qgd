---
title: "Dimensional scale and calibration"
---

# Dimensional scale and calibration

## 1. Statement

This note fixes the dimensional response used in the chapter. GDQ calculates eigenvalues, stiffnesses, and geometric ratios. The physical unit in MeV or GeV enters by explicit metrological calibration.

This is not a specific deficiency of GDQ. No physical theory determines the operational meaning of "MeV", "meter" or "second" without a measurement convention. The predictive content lies in the dimensionless ratios.

## 2. Operator with physical dimension

If a geometric operator is written in physical coordinates:

$$
L\phi_n=\lambda_n\phi_n,
$$

then:

$$
[\lambda_n]=L^{-2}.
$$

The associated energy is:

$$
M_n c^2
=
\hbar c\sqrt{\lambda_n}.
$$

## 3. Normalized operator

In geometric practice, the internal domain is usually normalized. In this case:

$$
\widehat L\phi_n=\widehat\lambda_n\phi_n,
$$

with:

$$
[\widehat\lambda_n]=1.
$$

To restore units, a calibration length $\ell_0$ is introduced:

$$
\lambda_n
=
\frac{\widehat\lambda_n}{\ell_0^2}.
$$

Then:

$$
M_n c^2
=
\frac{\hbar c}{\ell_0}
\sqrt{\widehat\lambda_n}.
$$

Defining:

$$
E_0
:=
\frac{\hbar c}{\ell_0},
$$

we have:

$$
M_n c^2
=
E_0\sqrt{\widehat\lambda_n}.
$$

## 4. Ratios are scale-independent

For two modes of the same sector:

$$
\frac{M_i}{M_j}
=
\sqrt{
\frac{\widehat\lambda_i}{\widehat\lambda_j}
}.
$$

This is the natural object of the theory. The number $0.511\,\mathrm{MeV}$ depends on how the laboratory defines the unit of energy. Therefore, the chapter must speak of dimensionless ratios.

## 5. Electron calibration

Using $M_e$ as a metrological standard is acceptable when the prediction is:

$$
\frac{M_\mu}{M_e},
\qquad
\frac{M_\tau}{M_e}.
$$

If the electron has a reduced eigenvalue $\widehat\lambda_e$, then:

$$
M_e c^2
=
E_0\sqrt{\widehat\lambda_e}$.
$$

Thus:

$$
E_0
=
\frac{M_ec^2}{\sqrt{\widehat\lambda_e}}.
$$

Substituting:

$$
M_n
=
M_e
\sqrt{
\frac{\widehat\lambda_n}{\widehat\lambda_e}
}.
$$

If the normalization of the electronic sector chooses:

$$
\widehat\lambda_e=1,
$$

then:

$$
E_0=M_ec^2.
$$

This choice does not derive the MeV from nothing. It fixes the ruler. The prediction remains in the ratio:

$$
R_n
=
\sqrt{
\frac{\widehat\lambda_n}{\widehat\lambda_e}
}.
$$

## 6. Cartan scale and sectorial scales

The official action uses the Cartan cutoff parameter in normalized form. The safe notation is:

$$
\ell_C=\frac{\hbar c}{E_C},
\qquad
k_C=\ell_C^{-1},
\qquad
E_C=\hbar c\,k_C.
$$

Do not confuse:

$$
\Lambda_C,
\qquad
\widehat\Lambda_\tau=\tau^{-1/2},
\qquad
m_i,
\qquad
E_0^{(s)}.
$$

In normalized coordinates, $\Lambda_C$ is the cutoff number of the action. The corresponding physical energy requires a metrological choice of $\ell_C$ or $E_C$.

Each sector can have an effective scale:

$$
E_0^{(s)}
=
\frac{\hbar c}{\ell_s}.
$$

If each $\ell_s$ is measured separately, the theory loses predictive power between sectors. The strong goal is to derive the ratios between these scales by gluing, Hessian, and boundary.

## 7. Beta decay bridge

There is also an independent metrological bridge in the baryonic sector. The endpoint of free beta decay can be written as:

$$
Q_\beta
=
\left(
\delta_B-1
\right)
M_ec^2.
$$

Here $\delta_B$ is a dimensionless geometric number. In the coherent legacy route:

$$
\delta_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
$$

Thus:

$$
M_ec^2
=
\frac{Q_\beta}{\delta_B-1}.
$$

This equation does not turn $Q_\beta$ into an axiom of the electron mass. It shows that a dimensional scale can be inherited from a physical metrological boundary when the geometric ratio $\delta_B$ is derived.

## 8. Honesty criterion

Whenever a formula has the form:

$$
M_n
=
M_e R_n^{\rm GDQ},
$$

the predictive result is:

$$
R_n^{\rm GDQ}
=
\frac{M_n}{M_e}.
$$

One should not write "absolute mass calculated ab initio" if a measured scale entered the normalization. The correct form is:

$$
\boxed{
\text{mass obtained as a geometric ratio after metrological calibration}
}
$$

## 9. Status

The dimensional scale is closed in a metrological sense:

$$
\boxed{
\text{GDQ predicts ratios; the physical unit is fixed by calibration}
}
$$

Strong ab initio closure would require deriving $E_C$, $\ell_C$, or each $E_0^{(s)}$ directly from the official action, the background, the Hessian, and the boundary conditions. This is a subsequent program, not a requirement for using already derived dimensionless ratios.
