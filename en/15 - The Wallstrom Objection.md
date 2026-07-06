# Chapter 15 - The Wallstrom Objection

The formulation of stochastic mechanics proposed by Edward Nelson in 1966 allowed the derivation of the linear Schrödinger equation from the Brownian fluctuations of a particle immersed in a stochastic vacuum. However, in 1989 and 1994, Timothy Wallstrom^[11] pointed out a significant conceptual limitation within the scope of stochastic mechanics and classical hydrodynamics: the [[01 - The Initial Problem - The Divergence between the Feynman and Wiener Integrals|Madelung]] equation (and Nelson's formalism) admits solutions where the circulation of the velocity field $\mathbf{v}$ along a closed contour assumes arbitrary and continuous values:
$$\oint_\gamma m \mathbf{v} \cdot d\mathbf{x} = \kappa \cdot h, \quad \kappa \in \mathbb{R}$$

To recover quantum mechanics, in which the circulation is necessarily restricted to discrete integer values ($\kappa \in \mathbb{Z}$), Nelson's mechanics must postulate the uniqueness condition of the complex wave function axiomatically and *ad-hoc*. This axiomatic requirement limits the purely emergent character of stochastic mechanics as a description independent of conventional quantum theory.

Within the scope of the QGD formalism, the Wallstrom objection is circumvented geometrically. The quantization of circulation is no longer an external postulate and emerges as a **rigorous geometric and dynamic consequence of the flow** on the Kähler manifold.

---

## 15.1 The Geometric Structure and Phase Discontinuity

In QGD theory, the physical vacuum and [[02 - The Geometrization of Matter|solitons]] (particles) are described by the complex scalar field $f$ over the Kähler manifold. The potential $f$ is decomposed in terms of the real mechanical ($S_R$) and Nelson's osmotic ($S_I$) actions:
$$f = -\frac{S_I - i S_R}{\hbar}$$

The current velocity field of the quantum fluid is governed by the gradient of the real phase of the action:
$$\mathbf{v} = \frac{\nabla S_R}{m}$$

Let us consider a simply connected closed contour $\gamma$ enclosing a linear topological defect (a vortex or curvature stoma). The generic phase circulation accumulates a quantization error $\epsilon$:
$$\oint_\gamma \nabla_\mu S_R \, dx^\mu = \kappa \cdot h = (n + \frac{\epsilon}{2\pi}) h$$
where $n \in \mathbb{Z}$ represents the winding homotopy class and $\epsilon \in [0, 2\pi)$ is the continuous (non-quantized) deviation of the circulation.

When $\epsilon \neq 0$, the phase field $S_R$ exhibits non-trivial multivaluedness on the contour, which introduces a discontinuity in the [[09 - Spin and Cartan Geometry - The Vorticity of Spacetime|affine connection]] and a deformation by transverse metric shear.

---

## 15.2 The Poisson Summation and the Dirac Comb in the State Space

To describe topological stability from the perspective of integrated paths, we resort to the [[03 - Complex Causality and the End of the Wick Paradox|symmetric propagator]]. The total topological probability amplitude $\Psi_{\text{total}}(\epsilon)$ is constructed by summing the contributions of all homotopy classes (winding numbers) over the fundamental group of the circle $\pi_1(S^1) \cong \mathbb{Z}$:
$$\Psi_{\text{total}}(\epsilon) = \sum_{m=-\infty}^{\infty} e^{im\epsilon}$$

Physical regularity requires that the space of admissible states be the space of smooth test functions of rapid decay (Schwartz space $\mathcal{S}(S^1)$), over which the phase and its momenta are defined. In the space of tempered distributions $\mathcal{S}'(S^1)$, the infinite sum above is the exact definition of the **Dirac Comb**. By the Poisson Summation formula, we have:
$$\sum_{m=-\infty}^{\infty} e^{im\epsilon} = 2\pi \sum_{n=-\infty}^{\infty} \delta(\epsilon - 2\pi n)$$
where $\delta$ is the Dirac delta distribution.

> [!IMPORTANT] Important
> **Topological Verdict:** For any quantization deviation $\epsilon \neq 0 \pmod{2\pi}$, the topological probability amplitude $\Psi_{\text{total}}(\epsilon)$ vanishes exactly under the action of any functional or smooth observable. This means that states with non-quantized circulation possess **strictly null physical support measure** in the topological Hilbert space of the [[12 -  The Quantum Tunneling Time (Hartman Effect)|Kähler vacuum]].

To visualize the physical effect of dissipation under the fluctuating metric, we introduce the kinematic viscosity parameter $\eta > 0$ associated with the flow, defining the Abel regularized sum:
$$\Psi_{\text{reg}}(\epsilon) = \lim_{\check{\eta} \to 0^+} \left[ \sum_{m=0}^{\infty} e^{-\check{\eta} m} e^{im\epsilon} + \sum_{m=1}^{\infty} e^{-\check{\eta} m} e^{-im\epsilon} \right]$$

Summing the geometric series and applying the limit:
$$\Psi_{\text{reg}}(\epsilon) = \lim_{\check{\eta} \to 0^+} \frac{1 - e^{-2\check{\eta}}}{1 - 2e^{-\check{\eta}}\cos(\epsilon) + e^{-2\check{\eta}}} = \begin{cases} \infty & \text{if } \epsilon = 0 \pmod{2\pi} \\ 0 & \text{if } \epsilon \neq 0 \pmod{2\pi} \end{cases}$$

The limit recovers the Dirac Comb. Any intermediate state ($\epsilon \neq 0$) undergoes an infinitely continued destructive interference in the closed circuit, annihilating the local transition probability.

---

## 15.3 Energetic Divergence in the $\mathcal{W}$ Functional

The presence of a circulation deviation $\epsilon \neq 0$ directly affects the internal energy density of the fluid. The integrand of Perelman's entropic functional $\mathcal{W}$ contains the gradient kinetic energy term $|\nabla f|^2$. As we approach the immediate vicinity of the radial vortex core (radius $r \to 0$), the energy density scales as:
$$|\nabla f|^2 \propto \frac{(nh + \epsilon)^2}{r^2}$$

The integration of the $\mathcal{W}$ functional over a region enclosing the vortex results in:
$$\mathcal{W}(g, f, \tau) \propto \int_{\text{vortex}} \frac{(nh + \epsilon)^2}{r^2} \, r \, dr \, d\theta \sim (nh + \epsilon)^2 \ln\left(\frac{R_{\text{ext}}}{r_{\text{core}}}\right)$$

For any deviation $\epsilon \neq 0$, the perturbation introduces an infinite potential energy barrier in the ultraviolet limit ($r_{\text{core}} \to 0$). The stable saddle point that minimizes the entropic action and guarantees the finitude of the functional strictly requires:
$$\frac{\partial \mathcal{W}}{\partial \epsilon} = 0 \implies \epsilon = 0 \implies \kappa = n \in \mathbb{Z}$$

The only stable local minima of the Kähler vacuum action are the purely quantized states.

---

## 15.4 Dynamic Dissipation by the Ricci Flow in Finite Time

If a physical state is artificially prepared in a regime of fractional or irrational circulation ($\epsilon \neq 0$), the asymmetry in the rotation of the metric space generates a non-zero shear stress that excites the degrees of freedom of the transverse curvature. The evolution of the Kähler metric $g_{ij}$ under the flow is expressed by:
$$\frac{\partial g_{ij}}{\partial \tau} = -2\left( R_{ij} + \nabla_i \nabla_j f \right)$$
where $\tau$ is the dimensionless scale parameter of the flow.

Using local harmonic coordinates (via the DeTurck map), the evolutionary dynamics of the mean curvature under Itô's stochastic fluctuation satisfies the quasi-linear differential inequality:
$$\frac{\partial}{\partial \tau} \mathbb{E}[|R_{ij}|^2] \le \Delta_K \mathbb{E}[|R_{ij}|^2] - C_1 \left( \mathbb{E}[|R_{ij}|^2] \right)^{3/2} + \sigma^2_\epsilon$$
where $\sigma^2_\epsilon$ represents the variance and deformation density generated by the phase misalignment $\epsilon$.

The entropy rate along the geometric flow dissipates the shear perturbation through the viscosity tensor:
$$\frac{d\mathcal{W}}{d\tau} = 2 \int_{\mathcal{M}} |R_{ij} + \nabla_i \nabla_j f|^2 e^{-f} dV \ge \lambda_\epsilon > 0$$
where $\lambda_\epsilon$ is a decay rate constant proportional to $|\epsilon|^2$.

The parabolic damping of the flow forces the contraction and strangulation of the transverse metric around the non-quantized circulation filament. The [[13 - Born Rule|Madelung density]] associated with this configuration decays exponentially to zero:
$$\rho(\tau) = \rho_0 \exp\left( - \int_0^\tau \lambda_\epsilon(\tau') d\tau' \right)$$

Since the causal feedback loop does not close for non-integer values, the viscous loss rate consumes the energy of the state, extinguishing the configuration in a finite flow time $\tau_{\text{end}}$:
$$\tau_{\text{end}} \le \frac{\mathcal{W}_{\text{initial}}}{\lambda_\epsilon} < \infty$$

The fractional perturbation is damped and converted into vacuum heat fluctuations (high-frequency metric phonons), restoring the stable integer quantization ($\epsilon = 0$).

---

## 15.5 Conclusion

The Wallstrom objection is completely resolved because, in QGD, the Kähler-Perelman geometry is not a passive plane, but a dynamic, self-regularizing medium. States with non-quantized circulation are mathematically annihilated by distributional interference in the Dirac Comb and dynamically dissipated in finite time by the Ricci Flow. The $nh$ quantization of the circulation acts as a condition for elliptic regularity and topological stability for the manifold's metric.

---

## 15.6 The DeTurck Flow and the Uniqueness of Foliation

The evolution of quantum spacetime and probability density in this model is mapped by the modified Ricci flow by a diffeomorphism generated by the quantum velocity field (DeTurck method or diffeomorphism). The evolution equation of the background Kähler metric under the Ricci-DeTurck flow assumes the form of a strictly elliptic parabolic equation:
$$\frac{\partial g_{\mu\nu}}{\partial t} = -2R_{\mu\nu} + \mathcal{L}_v g_{\mu\nu}$$
where $\mathcal{L}_v$ is the Lie derivative along the gradient field determined by the phase $S$ ($v_\mu = \nabla_\mu S$).

By the Hamilton-DeTurck geometric stability theorem, given an initial condition on the manifold, the flow converges uniquely to a regularized geometric structure. The constant phase surfaces ($S = \text{constant}$) form a **codimension-1 foliation** of the configuration space. The strict ellipticity of the DeTurck flow analytically prevents the crossing or bifurcation of these geometric leaves, locking the local topology.

### 15.6.1 Resolution of the Objection via Smooth Mapping of $S^1$

Given that the Ricci flow stabilizes the submanifold and forces the streamlines to contour zero-density nodes through topologically closed paths in the complex manifold, the phase $S$ ceases to be a free functional and becomes rigidly coupled to the holonomy of the local Cartan connection.

For the codimension-1 foliation to be globally regular and continuous ($C^\infty$), the map that takes the configuration space to the phase along any non-trivial closed curve $\gamma$ must be a smooth covering of the unit circle:
$$S: \gamma \to S^1$$

If there were ambiguities in the circulation (non-integer gaps), DeTurck stability would be violated, introducing pinching singularities in the Kähler metric, which is inconsistent with the asymptotic behavior of the Perelman functional in a vacuum. Therefore, the uniqueness and smoothness of the foliation eliminate the physically inconsistent degree of freedom pointed out by Wallstrom.
