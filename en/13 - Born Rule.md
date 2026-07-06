# Chapter 13 - Born Rule

In the formalism of the [[02 - The Geometrization of Matter|Hydrodynamic-Geometric Field Theory]], the square of the modulus ceases to be a purely axiomatic postulate and emerges as a structural, topological, and flow conservation necessity.

---

## 13.1 The Constraint of the Perelman Invariant Measure

The geometric starting point is based on the [[03 - Complex Causality and the End of the Wick Paradox|Perelman conjugate volume measure]] ($u \propto e^{-f}$). For this measure to correspond to the real physical density in the complex Kähler plane, the probability density $\rho(z, \bar{z})$ is extracted through the symmetric projection of the scalar field:
$$\rho(z, \bar{z}) = e^{-\frac{f + \bar{f}}{2}}$$

By expanding the field $f$ into its structural hydrodynamic components ([[01 - The Initial Problem - The Divergence between the Feynman and Wiener Integrals|Madelung potentials]]), we have:
$$f = -\frac{S_I}{\hbar} + i \frac{S_R}{\hbar}$$
$$\bar{f} = -\frac{S_I}{\hbar} - i \frac{S_R}{\hbar}$$

The term-by-term addition promotes the analytical annihilation of the real mechanical phase $S_R$, resulting in:
$$f + \bar{f} = -\frac{2 S_I}{\hbar}$$

Substituting this exact result back into the symmetric exponential:
$$\rho(z, \bar{z}) = e^{-\frac{1}{2} \left( -\frac{2 S_I}{\hbar} \right)} = e^{\frac{S_I}{\hbar}}$$

---

## 13.2 Why is the Exponent Exactly the Square ($R_M^2$)?

The mathematical reason for the emergence of the **square** lies in the isomorphic mapping between the geometry of the vacuum and the real fluid. In the traditional polar formalism, the wave function expresses the real amplitude as $R_M$. To project this amplitude into the exponential domain of geometric entropy, the osmotic component of the action ($S_I$) is defined with a scale factor corresponding to half the quantum of action:
$$R_M = e^{\frac{S_I}{2\hbar}}$$

If we isolate and square this physical amplitude, the linear factor of the exponential is canceled:
$$R_M^2 = \left(e^{\frac{S_I}{2\hbar}}\right)^2 = e^{2 \cdot \frac{S_I}{2\hbar}} = e^{\frac{S_I}{\hbar}}$$

Comparing the two analytical paths:
1. The symmetric geometric projection of the field requires half the sum ($e^{-\frac{f+\bar{f}}{2}}$), generating a factor of $2$ in the numerator that results in $e^{\frac{S_I}{\hbar}}$.
2. The osmotic potential of the physical fluid defines the amplitude $R_M$ with a factor of $2$ in the denominator of the exponential ($e^{\frac{S_I}{2\hbar}}$).

> **Conclusion:** The square exponent ($R_M^2 = |\psi|^2$) is the only mathematically admissible value because it harmonically undoes the dynamic scale factor ($1/2$) of the osmotic action. If the probability depended on $|\psi|$ linearly or on $|\psi|^3$, there would be a chronic dimensional and topological incompatibility with the invariant volume measure under the Ricci-Perelman Flow.

---

## 13.3 Mass Conservation and the Global Volumetric Fraction

From the statistical point of view and the [[16 - Measurement Problem|Measurement Problem]], when the system interacts with the detector and undergoes localized elliptical contraction into a [[08 - Black Hole Singularity|Shrinking Ricci Soliton]], the complex coefficients $c_k$ of the expansion in normal modes gain direct physical meaning:
- **Meaning of the Coefficients:** Each initial complex coefficient $c_k$ physically represents the exact fraction of the volume or mass of the original quantum fluid that filled the geometric basin of attraction associated with that specific mode $\psi_k$.
- **Flow Mechanism:** Once the flow is activated, the fluid drains into the geometric potential well to conserve the global Noether flow current. The macroscopic probability $P(k)$ of the system converging to the eigenvalue $\lambda_k$ is the exact measure of the volumetric flow through that cross-section of the Kähler manifold:
    $$\text{P}(k) = |c_k|^2 = \int_{\Omega} \rho_k(x) \, dV_K$$

Since the local fluid density $\rho$ already carries the quadratic character of the amplitude ($R_M^2$) due to the osmotic equilibrium with the geometric vacuum, its integration in macroscopic space preserves this strict quadraticity in the spatial partition coefficients ($|c_k|^2$).
