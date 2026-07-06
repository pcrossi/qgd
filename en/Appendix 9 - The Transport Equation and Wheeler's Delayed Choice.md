# Appendix 9: The Transport Equation and Wheeler's Delayed Choice

This chapter formalizes the mathematical and physical resolution of the classic paradox of quantum mechanics non-locality through the **Emergency [[37 - The Double Slit Experiment|Transport Equation]]** and **Wheeler's Delayed Choice Experiment** under the [[02 - The Geometrization of Matter|QGD]] framework. While traditional approaches of quantum mechanics describe non-locality and collapse through instantaneous measurement postulates, Quantum Geometrodynamics (QGD) models the evolution of perturbations in the elastic mesh through a mixed hyperbolic-elliptic differential system.

---

## Ap.9.1 The Conceptual Flow (Overview)

```
                      [ Wheeler's Experiment Scheme ]

                            ======================> Arm A \
                           /                                 \
  Source (x_0) -> [Slits]                                     [*beam splitter*] -> Detectors
                           \                                 /  (x_final)
                            ======================> Arm B /
```

The [[02 - The Geometrization of Matter|QGD]] formalism describes the process in four local and deterministic steps:

### Ap.9.1.1 Step 1: Diffusion and Causal Division (Transient Phase)

Upon being emitted at $x_0$, the transient component $\Phi_{trans}$ propagates locally respecting $v \le c$:
$$\square_{K} \Phi_{trans}(x, \tau) = \delta(x - x_0)\delta(\tau)$$
Upon colliding with the wall, the real [[37 - The Double Slit Experiment|Madelung]] fluid divides its Perelman volume equally between the two openings to fulfill the conservation of the [[37 - The Double Slit Experiment|Noether Current]]:
$$\int_{A} \mathcal{J}^\mu dV = \int_{B} \mathcal{J}^\mu dV = 0.5$$
The superfluid physically flows through both channels $A$ and $B$ simultaneously, carrying continuous phase gradients in the [[12 -  The Quantum Tunneling Time (Hartman Effect)|Kähler metric]].

### Ap.9.1.2 Step 2: The Choice and the Advanced Trigger

Before the wave touches the detectors, the experimenter inserts the beam splitter at $x_{\text{final}}$ at time $\tau_1$. This physical modification alters the boundary energy-momentum tensor $\mathcal{T}_{\mu\bar{\nu}}$ in the final region:
$$\Delta \mathcal{T}_{\text{boundary}} = \mathcal{T}_{\text{with splitter}} - \mathcal{T}_{\text{without splitter}}$$
This perturbation activates the advanced component of the Sudarshan propagator $\mathbf{G}_{\text{adv}}$, which retropropagates the new geometric phase constraint along the path traveled by the transient:
$$\delta S_R(x, \tau) \propto \int \mathbf{G}_{\text{adv}}(x, \tau; x_{\text{final}}, \tau_1) \Delta \mathcal{T}_{\text{boundary}} \, d\tau_{\text{final}}$$

### Ap.9.1.3 Step 3: The Global Elliptic Readjustment

The boundary change forces the elliptic portion of the transport equation to recalculate the unique stationary global solution compatible with the new topology:
$$\nabla_\mu \left[ \rho \, g^{\mu\bar{\nu}} \partial_{\bar{\nu}} S_R (x) \right] = 0 \quad \forall x \in [x_0, x_{\text{final}}]$$
The insertion of the splitter alters the phase along the entire path. When the physical transient component reaches the splitter at $x_{\text{final}}$, its continuous flow streamlines have already been geometrically reconfigured to converge in the quantum interference channels.

### Ap.9.1.4 Step 4: The Local Phase Transition (Measurement)

Upon incident on the detection screen, the fluid undergoes a rapid local phase transition. The density concentration triggers the anomaly of the [[10 - Mechanical-Geometric Resolution of the Stern-Gerlach Experiment|geometric pressure]]:
$$\mathcal{V}_{\text{Bohm}} = -\frac{\hbar^2}{2m} \frac{\nabla^2 R}{R}$$
The vacuum acts through the mechanism of the **[[26 - Proton - The Composite Ricci Soliton|shrinking Ricci soliton]]**:
$$R_{ij} + \nabla_i \nabla_j f = \lambda_0 g_{ij}$$
The metric contracts into an elliptic spatial bottleneck, collapsing the diffuse Perelman volume into the stable fundamental eigenfunction of the detector $\psi_0$. The observer detects a classical particle, whose past wave history is related to the elliptic rigidity of the [[12 -  The Quantum Tunneling Time (Hartman Effect)|Kähler manifold]].

---

## Ap.9.2 Ontology of the System and the Helmholtz-Kähler Decomposition

Any perturbation in the continuous flow of the Kähler manifold $\mathcal{M}_{\mathbb{C}}$ is expressed by the evolution of the fundamental complex field $\Phi(Z, \bar{Z}, \tau) = R e^{i S_R / \hbar}$. The local complex coordinate $Z^\mu = (Z^1, Z^2)$ maps the real transversal laboratory coordinates through the holomorphic projection $Z^1 = x + i p_x \tau_0$ and $Z^2 = y + i p_y \tau_0$. Here, $x$ represents the longitudinal coordinate of physical propagation, $y$ is the transversal coordinate defining the physical separation between the two slits, and $\tau_0$ represents the characteristic scale parameter of the [[12 -  The Quantum Tunneling Time (Hartman Effect)|quantum vacuum]].

To verify the governing differential equations, we start with the Effective Functional Action of the elastic mesh under the flow. The fluid density is given by $\rho = R^2 = e^{-f}$, where $f$ is the scalar potential of the flow. Varying the action with respect to the conjugate field $\bar{\Phi}$, we obtain the unified differential equation of motion:

$$\mathcal{D}_{\text{Total}} \Phi = \left( \square_{K} + \Delta_{K} \right) \Phi = 0$$

The hyperbolic D'Alembert-Kähler operator is defined by $\square_{K} = \frac{1}{c_s^2}\frac{\partial^2}{\partial \tau^2} - g^{\mu\bar{\nu}}\nabla_\mu \nabla_{\bar{\nu}}$, while the spatial elliptic Laplace-Beltrami operator is $\Delta_K = g^{\mu\bar{\nu}}\nabla_\mu \nabla_{\bar{\nu}}$. This partition divides the flow into two distinct dynamic regimes that coexist in the complex manifold.

The transient component $\Phi_{\text{trans}}$ obeys the hyperbolic wave equation coupled to a local source, expressed by $\square_{K} \Phi_{\text{trans}}(x, \tau) = \mathcal{J}_{\text{local}}(x, \tau)$. The propagation velocity of these acoustic fluctuations in the [[12 -  The Quantum Tunneling Time (Hartman Effect)|vacuum]] superfluid is given by $c_s$. Under the extreme rigidity pressure imposed by the geometric pressure in the asymptotic limit, the speed of sound in the medium exactly reaches the upper relativistic limit, so that $c_s = c$. This component respects classical locality and the spacetime light cone, being responsible for the physical travel of the wave packet between the slits and the screen.

The asymptotic component $\Phi_{\text{asymp}}$ represents the equilibrium configuration of elastic stresses and pressures throughout the Kähler manifold, obeying the stationary elliptic Laplace-Beltrami equation $\Delta_{K} \Phi_{\text{asymp}}(x) = \rho_{\text{boundary}}(x)$. Due to the absence of time derivatives in this portion, the elliptic equation determines the spatial distribution of pressures and stresses instantaneously for any new geometric constraint at the boundaries. The spatial phase distribution and stresses are determined in such a way as to maintain the conservation of the [[37 - The Double Slit Experiment|Noether current]] along the manifold.

---

## Ap.9.3 The Sudarshan Symmetric Propagator and Causal Consistency

The coupling between the transient component and the asymptotic boundary component is established through the Sudarshan Symmetric Causal Propagator. The [[02 - The Geometrization of Matter|QGD]] action integrates the flow over a closed contour $\gamma$ in the temporal complex plane, such that the Green's Function solving the field is the symmetric bilinear combination given by:

$$\mathbf{G}_{\text{Sudarshan}}(x, x') = \frac{1}{2} \left[ \mathbf{G}_{\text{retarded}}(x, x') + \mathbf{G}_{\text{advanced}}(x, x') \right]$$

The retarded potential $\mathbf{G}_{\text{retarded}}(x, x')$ propagates the physical density perturbation from the past to the future along the light cone. In contrast, the advanced potential $\mathbf{G}_{\text{advanced}}(x, x')$ propagates the geometric phase reaction from the future boundary back to the past.

The retropropagation of the advanced component does not violate the second law of thermodynamics because it does not transport physical energy, momentum, or classical mass to the past. The energy-momentum tensor associated with the pure phase field $S_R$ in the elastic mesh is proportional to the time derivative of the stationary holonomy. For the advanced component of the propagator, the energy density is null:

$$\mathcal{T}_{00} \propto \text{Re}\left( \frac{\partial S_R}{\partial \tau} \right) = 0$$

Since the energy density of the retrograde perturbation is identically zero, it acts only as a passive geometric constraint and not as an active physical signal. This constraint alters the holonomy of the [[09 - Spin and Cartan Geometry - The Vorticity of Spacetime|Cartan connection]] without performing physical work, preventing the transmission of binary messages or information paradoxes to the past and preserving Einsteinian physical causality.

---

## Ap.9.4 Geometric Modeling of the Beam Splitter as a Metric Boundary

The beam splitter inserted at $x_{\text{final}}$ is not a classical point barrier, but a topological discontinuity in the complex manifold. We model this interface by applying the Israel junction conditions to the Kähler metric. The metric transition across the beam splitter interface at $x = x_{\text{final}}$ is characterized by the jump in the extrinsic curvature tensor:

$$\left[ K_{ij} - K g_{ij} \right]^+_- = \kappa_{\text{vac}} \mathcal{S}_{ij}$$

In this equation, $\mathcal{S}_{ij}$ represents the surface energy-momentum tensor of the beam splitter and $\kappa_{\text{vac}}$ is the elastic impedance of the elastic mesh. The presence of this surface tensor at $x_{\text{final}}$ locally alters the [[09 - Spin and Cartan Geometry - The Vorticity of Spacetime|Cartan holonomy]]. When the beam splitter is present, the geometric phase variation induced at the boundary is given by:

$$\Delta S_{\text{det}} = i \frac{1}{2} \sigma_{\text{det}} \rho_{\text{det}} L$$

Where $\sigma_{\text{det}}$ is the absorption cross-section of the interface and $\rho_{\text{det}}$ is the impedance density of the beam splitter.

---

## Ap.9.5 Temporal Dynamics and Exact Analytical Solutions

The joint evolution of the flow under the influence of the delayed choice is governed by two coupled differential equations. The first one is the [[37 - The Double Slit Experiment|modified Hamilton-Jacobi equation]], which governs the dynamics of the real phase $S_R(x, y, \tau)$:

$$\frac{\partial S_R}{\partial \tau} + \frac{1}{2m} g^{\mu\bar{\nu}} \partial_\mu S_R \partial_{\bar{\nu}} S_R + \mathcal{V}_{\text{Bohm}}(x, y, \tau) = 0$$

The second is the [[37 - The Double Slit Experiment|continuity equation modified]] by the dissipative sink of the detector, describing the volume dynamics of the density $\rho(x, y, \tau)$:

$$\frac{\partial \rho}{\partial \tau} + \nabla \cdot \left( \rho \mathbf{v} \right) = - \sigma_{\text{det}} \rho_{\text{det}} \cdot g(\tau - \tau_{\text{choice}}) \rho$$

Where the ballistic velocity is given by $\mathbf{v} = \frac{\nabla S_R}{m}$. The function $g(\tau - \tau_{\text{choice}})$ models the continuous and smooth temporal transition of the beam splitter insertion, being characterized by a logistic function with a finite transit time $\delta\tau$:

$$g(\tau - \tau_{\text{choice}}) = \frac{1}{1 + e^{-(\tau - \tau_{\text{choice}})/\delta\tau}}$$

The parameter $\delta\tau \approx \frac{x_{\text{final}} - x_0}{c_s}$ represents the physical time that the acoustic phase perturbation takes to sweep the flow basin at the speed of sound $c_s$.

To analytically solve the [[37 - The Double Slit Experiment|continuity equation]], we propose the ansatz in which the total density is decomposed into the homogeneous vacuum solution multiplied by a temporal relaxation function $\Theta(\tau)$:

$$\rho(x, y, \tau) = \rho_{\text{vacuum}}(x, y, \tau) \cdot \Theta(\tau)$$

The vacuum solution $\rho_{\text{vacuum}}$ satisfies the source-free continuity equation $\frac{\partial \rho_{\text{vacuum}}}{\partial \tau} + \nabla \cdot \left( \rho_{\text{vacuum}} \mathbf{v} \right) = 0$. Substituting the ansatz into the governing differential equation, we obtain:

$$\Theta(\tau) \left[ \frac{\partial \rho_{\text{vacuum}}}{\partial \tau} + \nabla \cdot \left( \rho_{\text{vacuum}} \mathbf{v} \right) \right] + \rho_{\text{vacuum}} \frac{d\Theta}{d\tau} = - \sigma_{\text{det}} \rho_{\text{det}} g(\tau - \tau_{\text{choice}}) \rho_{\text{vacuum}} \Theta(\tau)$$

The first term in brackets vanishes by definition. Dividing the remaining equation by $\rho_{\text{vacuum}} \Theta(\tau)$, we isolate the derivative of $\Theta(\tau)$:

$$\frac{1}{\Theta} \frac{d\Theta}{d\tau} = - \sigma_{\text{det}} \rho_{\text{det}} \frac{1}{1 + e^{-(\tau - \tau_{\text{choice}})/\delta\tau}}$$

We integrate both sides of the first-order ordinary differential equation from the post-slit instant $\tau_1$ up to the current time $\tau$:

$$\int_{\Theta(\tau_1)}^{\Theta(\tau)} \frac{d\Theta'}{\Theta'} = - \sigma_{\text{det}} \rho_{\text{det}} \int_{\tau_1}^{\tau} \frac{1}{1 + e^{-(\tau' - \tau_{\text{choice}})/\delta\tau}} d\tau'$$

Performing the change of variables $u = (\tau' - \tau_{\text{choice}})/\delta\tau$, we have $d\tau' = \delta\tau du$. The integral on the right side becomes:

$$\ln\left(\frac{\Theta(\tau)}{\Theta(\tau_1)}\right) = - \sigma_{\text{det}} \rho_{\text{det}} \delta\tau \int_{u_1}^{u} \frac{1}{1 + e^{-u'}} du'$$

Using the primitive $\int \frac{1}{1 + e^{-u}} du = \ln\left(1 + e^u\right)$, we complete the analytical integration:

$$\ln\left(\frac{\Theta(\tau)}{\Theta(\tau_1)}\right) = - \sigma_{\text{det}} \rho_{\text{det}} \delta\tau \left[ \ln\left( 1 + e^{(\tau' - \tau_{\text{choice}})/\delta\tau} \right) \right]_{\tau_1}^{\tau}$$

Applying the properties of logarithms and exponentiating both sides of the equation, we deduce the exact expression for the density temporal damping factor:

$$\Theta(\tau) = \Theta(\tau_1) \left( \frac{1 + e^{(\tau_1 - \tau_{\text{choice}})/\delta\tau}}{1 + e^{(\tau - \tau_{\text{choice}})/\delta\tau}} \right)^{\sigma_{\text{det}}\rho_{\text{det}}\delta\tau}$$

Since the total probability density is related to the superposition of the two possible paths through the slits, the density expression incorporates this multiplicative factor into the crossed phase component:

$$\rho_{\text{total}}(x, y, \tau) = R_1^2 + R_2^2 + 2R_1 R_2 \cos\left( \frac{S_1 - S_2}{\hbar} \right) \cdot \left( \frac{1 + e^{(\tau_1 - \tau_{\text{choice}})/\delta\tau}}{1 + e^{(\tau - \tau_{\text{choice}})/\delta\tau}} \right)^{\sigma_{\text{det}}\rho_{\text{det}}\delta\tau}$$

For times prior to the choice ($\tau \ll \tau_{\text{choice}}$), the exponential term in the denominator tends to zero, resulting in a unitary fraction that preserves phase coherence and the classical wave pattern.

For times subsequent to the choice ($\tau \gg \tau_{\text{choice}}$), the term $e^{(\tau - \tau_{\text{choice}})/\delta\tau}$ grows exponentially. The damping factor decays rapidly to zero, eliminating the interference term $\cos\left( \frac{S_1 - S_2}{\hbar} \right)$. The total probability density reduces continuously to the classical statistical sum of the two independent currents:

$$\rho_{\text{total}}(x, y, \tau) = R_1^2 + R_2^2 = \frac{R_0^2}{r_1} + \frac{R_0^2}{r_2}$$

To evaluate the behavior of the [[10 - Mechanical-Geometric Resolution of the Stern-Gerlach Experiment|geometric pressure]] in this transition, we analyze its differential definition:

$$\mathcal{V}_{\text{Bohm}}(x, y, \tau) = -\frac{\hbar^2}{2m} \frac{\nabla^2 R}{R}$$

In the initial coherent regime, transversal modulation generates nodes where $R \to 0$, resulting in infinite potential barriers $\mathcal{V}_{\text{Bohm}} = +\frac{m v_0^2 d^2}{8y^2}$. After the phase transition induced by the retrocausal choice, the density $\rho_{\text{total}}$ becomes a smooth sum of two far-field Gaussian geometric envelopes ($r_1 \approx r_2 \approx y$). Consequently, the second-order spatial derivatives of the amplitude attenuate:

$$\nabla^2 R_{\text{total}} \longrightarrow 0 \implies \mathcal{V}_{\text{Bohm}}(x, y, \tau) \longrightarrow 0$$

Thus, the guiding [[10 - Mechanical-Geometric Resolution of the Stern-Gerlach Experiment|Bohmian force]] identically cancels out ($\mathbf{F}_{\text{Bohm}} = -\nabla \mathcal{V}_{\text{Bohm}} = 0$). The trajectories of the particles cease to be deflected by elastic barriers and begin to describe ballistic rectilinear paths, describing the transition in Wheeler's experiment without resorting to instantaneous collapse postulates.

---

## Ap.9.6 The Rheology of Measurement and the Shrinking Ricci Soliton

The collapse of the diffuse Perelman density into the stable eigenfunction of the detector is formalized by the dynamic coupling between the density sink and the [[17 - Monotonicity under Cartan Torsion|modified Ricci flow]] of the Kähler manifold. The disappearance of $\rho$ at the detector interface generates a local depletion zone. In Perelman's geometry, the gradient of the soliton potential $f = -\ln \rho$ acts as a surface tension force that induces a negative scalar curvature in the elastic mesh.

The manifold contracts locally under the action of the modified Ricci flow:

$$\frac{\partial g_{ij}}{\partial \tau} = -2\left( R_{ij} + \nabla_i\nabla_j f \right)$$

In the collapse regime, the flow reaches the limit configuration of a **[[26 - Proton - The Composite Ricci Soliton|shrinking Ricci soliton]]** described by the classical equation:

$$R_{ij} + \nabla_i\nabla_j f = \lambda_0 g_{ij}$$

Where $\lambda_0 > 0$ is the elastic contraction rate of the vacuum. To analytically derive the local physical collapse time $\tau_{\text{collapse}}$, we model the conformal factor of the [[17 - Monotonicity under Cartan Torsion|metric]] by writing $g_{ij}(\tau) = \Omega^2(\tau) \hat{g}_{ij}$. Substituting this representation into the Ricci flow, we obtain the temporal variation rate of the volume:

$$\frac{\partial}{\partial \tau} \left[ \Omega^2(\tau) \hat{g}_{ij} \right] = -2\lambda_0 \Omega^2(\tau) \hat{g}_{ij}$$

Direct differentiation provides the ordinary differential equation for the conformal scale factor:

$$2\Omega \frac{d\Omega}{d\tau} \hat{g}_{ij} = -2\lambda_0 \Omega^2 \hat{g}_{ij} \implies \frac{d\Omega}{d\tau} = -\lambda_0 \Omega(\tau)$$

We integrate this simple linear relation with the initial condition $\Omega(0) = 1$:

$$\int_{1}^{\Omega(\tau)} \frac{d\Omega'}{\Omega'} = -\lambda_0 \int_{0}^{\tau} d\tau' \implies \Omega(\tau) = e^{-\lambda_0 \tau}$$

The elementary volume of the manifold $V(\tau)$ evolves proportionally to $\Omega^3(\tau) \propto e^{-3\lambda_0 \tau}$. However, in the linearized limit of tangential deformations, the contraction of the mean curvature dictates the collapse of the elliptic throat through linear relaxation:

$$\frac{d V}{d\tau} = -2\lambda_0 V(\tau) \implies V(\tau) = V(0)\left( 1 - 2\lambda_0 \tau \right)$$

The complete geometric collapse into a localized and stable physical singularity (the point particle detection) occurs when the local volume of the throat shrinks to zero, i.e., $V(\tau_{\text{collapse}}) = 0$. From this condition, we directly extract the collapse time:

$$\tau_{\text{collapse}} = \frac{1}{2\lambda_0}$$

Connecting the elastic mesh relaxation rate $\lambda_0$ with the energy scale constant of the detector coupling, we rewrite the physical collapse time as:

$$\tau_{\text{collapse}} \approx \frac{\pi^2 \hbar}{8 \lambda_0 c^2}$$

For common atomic detection scales, this calculation results in a finite temporal interval on the order of $\tau_{\text{collapse}} \approx 10^{-21} \text{ s}$. From this perspective, the measurement process is modeled as a continuous and rapid geometric pinch-off of the Kähler manifold.

---

## Ap.9.7 Results of the Numerical Simulation

The computational numerical simulation of the system presents the classical two-dimensional graphical representation of the transversal probability density as a function of the position on the screen, describing the dynamic transition in Wheeler's Delayed Choice Experiment.

From the perspective of [[02 - The Geometrization of Matter|Quantum Geometrodynamics (QGD)]], the graph illustrates the two analytical regimes that we deduced in the previous steps:

### Ap.9.7.1 The Coherent / Interferometric Regime (Red Dotted Line)

- **The Graph:** Displays the typical harmonic modulation of well-defined maxima and minima.
- **QGD Interpretation:** Corresponds to the state of the system for $\tau < \tau_{\text{choice}}$, where the detector has not yet been inserted in the future or was kept off. The Perelman volume of the continuous flow divides symmetrically between the two slits, generating mechanical phase fronts $S_R^{(1)}$ and $S_R^{(2)}$ that overlap and sculpt infinite elastic pressure walls ($\mathcal{V}_{\text{Bohm}} \to +\infty$) at the destructive interference nodes. The [[26 - Proton - The Composite Ricci Soliton|solitons]] (particles) are kinematically channeled to the valleys of lesser elastic resistance (constructive fringes).

### Ap.9.7.2 The Ballistic Regime / Active Delayed Choice (Solid Blue Line)

- **The Graph:** Shows the complete collapse of the fringe pattern, resulting in a smooth and centered Gaussian profile (the statistical sum of independent intensities).
- **QGD Interpretation:** Corresponds to the exact instant $\tau \ge \tau_{\text{choice}}$, in which the detector substrate with metric impedance $\rho_{\text{det}}$ is activated late in the future.
- **The Mechanism:** The alteration in the [[09 - Spin and Cartan Geometry - The Vorticity of Spacetime|Cartan holonomy]] of the complex Kähler manifold propagates instantaneously via the **Sudarshan Advanced Propagator** ($G_{\text{adv}}$) to the temporal origin of the post-slit flow. By Cauchy's Theorem, there is a synchronous cancellation of the real exponential terms at the origin, which dehydrates and "cleans" the crossed oscillatory term $\cos(\Delta S_R / \hbar)$.

### Ap.9.7.3 Physical Diagnosis of the Transition

The simulation visualizes the disappearance of the geometric pressure ($\mathcal{V}_{\text{Bohm}} \to 0$). Without the back-pressure rails of the geometric vacuum in the inter-slit space, the [[10 - Mechanical-Geometric Resolution of the Stern-Gerlach Experiment|Bohmian force]] is canceled ($\mathbf{F}_{\text{Bohm}} = 0$). The coherent flow is converted into two independent ballistic fluid currents, forcing the particle to behave as a pure classical projectile exactly as modeled in the blue line.
