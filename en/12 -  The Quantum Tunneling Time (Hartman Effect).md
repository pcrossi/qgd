# Chapter 12 - The Quantum Tunneling Time (Hartman Effect)

In traditional physics, when a particle crosses a very wide potential barrier ($L$), conventional quantum mechanics predicts that the transit time becomes independent of $L$. This phenomenon, known as the **Hartman Effect**, generates an apparent causal paradox: if the width of the wall doubles, the particle takes the same amount of time to cross, suggesting a superluminal macroscopic coordinate velocity ($v \to \infty$).

Under the QGD formalism, local causality is preserved by means of a dynamic metric contraction of the Kähler manifold, which emerges naturally from the decay of the fluid density.

---

## 12.1 The Fluid Density inside the Barrier

When incident upon a barrier of constant potential $V_0 > E$, the wave function decays exponentially (evanescent regime):
$$\psi(x) = \psi_0 e^{-\kappa x}$$
where $\kappa = \sqrt{2m(V_0 - E)}/\hbar$ is the attenuation constant. The physical probability density of the corresponding fluid is:
$$\rho(x) = \rho_0 e^{-2\kappa x}$$

---

## 12.2 The Kähler-Perelman Metric Coupling

In accordance with the [[02 - The Geometrization of Matter|geometrization of matter]] in the QGD formalism, the spacetime metric is not a rigid Minkowski plane. In the absence of stationary classical currents (where the phase $S_R$ is suppressed in the evanescent transition), the longitudinal metric component $g_{xx}$ couples directly to the fluid density in order to maintain the invariance of the volume measure:
$$g_{xx}(x) = g_0 \frac{\rho(x)}{\rho_0} = g_0 e^{-2\kappa x}$$
where $g_0$ is the unperturbed metric tensor of the asymptotic vacuum (dimensionless, normalized as $g_0 = 1$), and $\rho_0 \equiv \rho(0)$ defines the hydrodynamic probability density immediately at the barrier's incidence interface ($x=0$).

---

## 12.3 The Calculation of Proper Distance and Spatial Contraction

The paradox of the Hartman Effect emerges because the macroscopic observer assumes a rigid Euclidean space of length $L$. However, the coordinate $x$ is a map coordinate. The real physical distance ($D_{\text{proper}}$) traveled by the soliton inside the barrier is shrunk by the metric deformation:
$$D_{\text{proper}} = \int_{0}^{L} \sqrt{g_{xx}(x)} \, dx = \int_{0}^{L} \sqrt{g_0} e^{-\kappa x} \, dx$$

Solving the integral analytically:
$$D_{\text{proper}} = \frac{\sqrt{g_0}}{\kappa} (1 - e^{-\kappa L})$$

In the asymptotic limit of an infinitely thick barrier ($L \to \infty$), the proper distance converges to a strict upper bound:
$$\lim_{L \to \infty} D_{\text{proper}} = \frac{\sqrt{g_0}}{\kappa}$$

---

## 12.4 Transit Time and the Preservation of Local Causality

By [[28 - The Retrocausality Dilemma and the Second Law|Weyl-Cartan local causality]], the quantum flow crosses the deformed mesh maintaining the local physical velocity [[03 - Complex Causality and the End of the Wick Paradox|invariant and limited]] to the relativistic ceiling, such that $v_{\text{proper}} = \sqrt{g_{xx}} \frac{dx}{dt} = v_0 \le c$. Consequently, the coordinate velocity decays as $\frac{dx}{dt} = v_0 (g_{xx})^{-1/2}$, reflecting the inertial drag of the vacuum.

The coordinate transit time ($T$) measured by the laboratory clock is calculated by integrating the temporal advance rate along the contracted channel:
$$T = \int_{0}^{L} \frac{dt}{dx} dx = \int_{0}^{L} \frac{\sqrt{g_{xx}(x)}}{v_0} \, dx = \frac{\sqrt{g_0}}{v_0 \kappa} (1 - e^{-\kappa L})$$

In the asymptotic regime ($L \to \infty$), the transit time saturates identically to the proper distance:
$$\lim_{L \to \infty} T = \frac{\sqrt{g_0}}{v_0 \kappa} = \text{constant}$$

---

## 12.5 Conclusion

The tunneling time becomes independent of $L$ not because the particle travels infinitely fast, but because the **real physical distance that the particle crosses inside the barrier has a maximum bound $\frac{\sqrt{g_0}}{\kappa}$**. Space contracts transitorily under the absence of density, so that geometrically gigantic barriers in the laboratory are topologically minuscule for the QGD soliton, preserving local causality ($v_{\text{proper}} \le c$).

---

## 12.6 Foundation from the Kähler Potential and Action

In a complex one-dimensional Kähler manifold, the metric $g_{z\bar{z}}$ is expressed locally through the second derivative of a [[29 - The fine structure constant|Kähler scalar potential]] $K(z, \bar{z})$:
$$g_{z\bar{z}} = \frac{\partial^2 K}{\partial z \partial \bar{z}}$$

Separating into real coordinates ($z = x + iy$), the purely spatial component reduces to $g_{xx} = \partial_x^2 K$. In the Quantum Geometrodynamics (QGD) formalism, the probability density of the Bohmian ensemble $\rho(x)$ is intrinsically linked to the local volume density of spacetime. The variational action of the geometric system is governed by the Kähler volume functional subject to the local conservation of the probability density.

We formulate the variational principle by defining a functional action $S[K]$ with a Lagrange multiplier $\Lambda(x)$ that imposes the incompressible flow constraint on the volume form ($\det(g) = \text{constant}$ in phase space):
$$S[K] = \int \mathcal{L} \, d^4x = \int \left[ R(g) - \Lambda(x) \left( \det(g_{\mu\nu}) - \rho(x)\sqrt{-g_0} \right) \right] d^4x$$

Where $\rho(x)$ acts as the invariant density source and $g_0$ is the asymptotic Euclidean/Minkowskian metric outside the potential barrier.

### 12.6.1 Variational Minimization and Emergence of the Relation

When we perform the variation of the action with respect to the Kähler potential $K$ in the coordinated spatial subspace $x$, the volume restriction forces the determinant of the submanifold to couple directly to the density distribution of the tunneling wave function. For the one-dimensional case of the Hartman Effect, the spatial metric determinant reduces directly to the $g_{xx}$ component:
$$\frac{\delta S}{\delta K} = 0 \implies \frac{\partial}{\partial x^2} \left( \frac{\partial \mathcal{L}}{\partial g_{xx}} \right) = 0$$

Since the total volume form $\omega \wedge \omega = \det(g_{z\bar{z}})\,dx \wedge dy$ must locally satisfy the complex Monge-Ampère type equation under the matter profile:
$$g_{z\bar{z}} = \frac{\partial^2 K}{\partial z \partial \bar{z}} = \rho(z, \bar{z})$$

Projecting onto the real direction $x$ of one-dimensional tunneling, where the quantum phase and transverse components are in a stationary regime, the variation directly results in the field equation:
$$g_{xx} = g_0 \frac{\rho(x)}{\rho_0}$$

This equivalence proves that the spatial contraction of the metric inside the potential barrier is not an arbitrary postulate: **it is the exact solution of the Monge-Ampère equation for the Kähler potential $K$ when the quantum fluid density acts as the source of the geometric volume.**
