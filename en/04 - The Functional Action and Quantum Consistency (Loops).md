## 4 - The Functional Action and Quantum Consistency (Loops)

### The Unified Lagrangian: Construction of the Action

Up to this point, our conceptualization has swept through microscopic stochastic hydrodynamics ([Section 1][01 - The Initial Problem - The Divergence between the Feynman and Wiener Integrals]), the geometric response of spacetime in the form of curvature and torsion ([Section 2][02 - The Geometrization of Matter]), and the bidirectional causal folding that stabilizes temporal boundaries ([Section 3][03 - Complex Causality and the End of the Wick Paradox]). However, for these blocks to constitute a formal and predictive field theory, they cannot coexist as independent or coupled equations. They must emerge from a single variational principle.

At this point in our construction, we will deduce the **Unified Action ($\mathcal{S}_{\text{QGD}}$)**. This Lagrangian density merges gravitation (Ricci curvature), quantum mechanics (Bohm's phase and potential), statistical mechanics (Wiener's diffusive entropy), and complex causality into a single invariant mathematical expression.

### 1. The Architecture of Field Variables in the Hermitian Domain

To construct the Lagrangian, we first define our configuration space over a complex Kähler manifold $\mathcal{M}_\mathbb{C}$ of complex dimension $n = 4$ (where the real dimension is $2n = 8$). The local metric $g_{\mu\bar{\nu}}$ is symmetric-Hermitian and deduced locally from a real scalar known as the Kähler Potential $K(z, \bar{z})$:
$$g_{\mu\bar{\nu}} = \frac{\partial^2 K}{\partial z^\mu \partial\bar{z}^\nu} = \partial_\mu \partial_{\bar{\nu}} K.$$
On this structure, the quantum field of matter and the very inertia of the flow are not described by abstract wave functions $\psi$, but rather by **Perelman's Complex Flow Field** $f(z, \bar{z}, \tau)$, which we define in terms of the quantum hydrodynamic variables as:
$$f = -\frac{S_I - i S_R}{\hbar},$$
where:
- $S_R$ is Hamilton's Principal Function (the real quantum phase that dictates the current velocity $\mathbf{v}$);
- $S_I$ is the real osmotic potential (associated with the Madelung amplitude via $R = e^{S_I/2\hbar} = \sqrt{\rho} \implies S_I = \hbar \ln \rho$).

> [!note]- Geometric Foundation of the Configuration Space and Complexification of the Field 
> 
> ![[notes/4/note 4.1]]

The statistical probability density of the fluid $\rho$ merges metrically with Perelman's invariant volume measure, establishing the real Boltzmann weight through the real part of the field $f$:
$$\rho(z, \bar{z}) = e^{-\frac{f + \bar{f}}{2}} = e^{S_I/\hbar} = R^2$$

> [!note]- The flow time and the breaking of covariance
> 
> ![[notes/4/note 4.2]]

### 2. The Unified Action and Dimensional Consistency

The basis of our quantum-gravitational Lagrangian extends Perelman's Functional $\mathcal{W}$ to the complex domain. To cure any dimensional ambiguities, we introduce the regularization factor by the Cartan ultraviolet *cut-off* ($\Lambda_C$) and parameterize the flow time $\tau$ (with area dimension $[L^2]$) in relation to the complex causal time $t_{\mathbb{C}}$ through the kinematic viscosity of the vacuum $\nu_0 = \hbar/(2m_0)$, such that $\tau = \nu_0 t_{\mathbb{C}}$.

The Effective Action $\mathcal{S}_{\text{QGD}}$ is expressed by the closed contour integral $\gamma$ with the dimensionless logarithmic invariant measure $\frac{d\tau}{\tau}$:

$$\mathcal{S}_{\text{QGD}} = \int_{\gamma} \left[ \int_{\mathcal{M}_\mathbb{C}} \frac{\hbar}{\Lambda_C^2} \left[ \tau \left( \mathcal{R} + g^{\mu\bar{\nu}} \partial_\mu f \partial_{\bar{\nu}} \bar{f} \right) + \frac{f + \bar{f}}{2} - n \right] \mathcal{U}(z, \bar{z}, \tau) \sqrt{\det(g)} \, d^{2n}z \right] \frac{d\tau}{\tau}$$

Here, **$\mathcal{U}(z, \bar{z}, \tau)$ is strictly treated as an undetermined gauge multiplier function (a test volume measure)**. We do not assume its form *a priori*. The dimensional consistency of the action is perfect: with $[\gamma_C] = \hbar L^{-2}$, the action acquires the correct dimension of quantum angular momentum $[\mathcal{S}_{\text{QGD}}] = [\hbar]$.

Let's dissect the physical anatomy of each component:
#### A. The Geometric-Gravitational Term ($\mathcal{R}$)
The term $\mathcal{R} = g^{\mu\bar{\nu}} \mathcal{R}_{\mu\bar{\nu}}$ represents the Kähler-Ricci scalar curvature. It measures the pure gravitational energy density of spacetime. Under the variation of the metric $g^{\mu\bar{\nu}}$, this term generates the Einstein-Ricci tensor that dictates how the vacuum contracts or expands.
#### B. The Quantum Complex Kinetic Term ($g^{\mu\bar{\nu}} \partial_\mu f \partial_{\bar{\nu}} \bar{f}$)
This is the quantum heart. When we expand the field $f$ into its real hydrodynamic components ($S_R$ and $S_I$), the coupling with the inverse Kähler metric $g^{\mu\bar{\nu}}$ divides neatly:
$$g^{\mu\bar{\nu}} \partial_\mu f \partial_{\bar{\nu}} \bar{f} = \frac{1}{\hbar^2} g^{\mu\bar{\nu}} \left( \partial_\mu S_R \partial_{\bar{\nu}} S_R + \partial_\mu S_I \partial_{\bar{\nu}} S_I \right)$$
- **The Phase Component ($\partial S_R$):** Provides the $|\nabla S_R|^2 / 2m_0$ term of the fluid's kinetic energy, generating the ballistic dynamics of the Hamilton-Jacobi Equation.
- **The Osmotic Component ($\partial S_I$):** Since $S_I = \hbar \ln \rho$, this term translates into $g^{\mu\bar{\nu}} \frac{\partial_\mu \rho \partial_{\bar{\nu}} \rho}{\rho^2}$. Passing through the variational process, this geometric gradient brings forth the **Bohm Quantum Potential** ($\frac{\hbar^2}{2m_0}\frac{\nabla^2 R}{R}$).
#### C. The Invariant Gauge Measure and Isomorphism
The test measure $\mathcal{U}$ acts as the physical volume weight. As demonstrated in Section 3, the variational principle imposes that $\mathcal{U}$ is identically equal to the material probability density of the quantum fluid, $\mathcal{U} \equiv \rho \propto e^{-f_{\text{geom}}}/(4\pi\tau)^{n/2}$, establishing the ab-initio unification between Perelman and Madelung.
#### D. The Causal Boundary Filter ($\int_\gamma \dots \frac{d\tau}{\tau}$)
The integral in $\tau$ along the Sudarshan complex closed contour $\gamma$ projects the surface boundary terms to zero, immunizing the Lagrangian against gauge breaking.

### 3. The Variational Principle: Ab-initio Derivation of the Measure

To prove the consistency of the Action, we apply variational extremization ($\delta \mathcal{S}_{\text{QGD}} = 0$) with respect to the independent degrees of freedom.

#### I. Variation with Respect to the Phase Field ($\delta \mathcal{S}_{\text{QGD}} / \delta (\text{Im } f) = 0$)

The variation of the action with respect to the real phase $S_R$ is equivalent to imposing gauge invariance under local phase transformations (Noether $U(1)$ symmetry). Expanding the complex kinetic term and performing the variation, integration by parts on the Kähler manifold projects the following evolution equation for the multiplier $\mathcal{U}$:

$$\frac{\partial \mathcal{U}}{\partial \tau} + \nabla_\mu \left( \mathcal{U} \cdot g^{\mu\bar{\nu}} \frac{\partial_{\bar{\nu}} S_R}{m_0} \right) = 0$$

Since the current velocity of the quantum fluid is given by $\mathbf{v}^\mu = \frac{1}{m_0} g^{\mu\bar{\nu}} \partial_{\bar{\nu}} S_R$, the equation reduces to a **Continuity Equation for the test measure $\mathcal{U}$**:

$$\frac{\partial \mathcal{U}}{\partial \tau} + \nabla_\mu \left( \mathcal{U} \mathbf{v}^\mu \right) = 0$$

On the other hand, the statistical and physical conservation of matter, deduced microscopically from Nelson's stochastic derivatives in Chapter 1, independently requires that the real density of the fluid ($\rho$) satisfies its own flux conservation law:

$$\frac{\partial \rho}{\partial \tau} + \nabla_\mu \left( \rho \mathbf{v}^\mu \right) = 0$$

Subtracting both differential equations to guarantee variational consistency with quantum hydrodynamics, the uniqueness of the heat kernel solution on the compact manifold imposes that $\mathcal{U}$ and $\rho$ share the same solution space:

$$\frac{\partial (\mathcal{U} - \rho)}{\partial \tau} + \nabla_\mu \left[ (\mathcal{U} - \rho) \mathbf{v}^\mu \right] = 0 \implies \mathcal{U}(z, \bar{z}, \tau) \equiv \rho(z, \bar{z}, \tau)$$

Having demonstrated that the test measure is identically the Madelung density, the solution of the reverse diffusion kernel in the Kähler-Perelman vacuum geometrically fixes the fundamental form:

$$\rho(z, \bar{z}, \tau) = \frac{e^{-f_{\text{geom}}}}{(4\pi\tau)^{n/2}}$$

Breaking definitely the logical leap of identification by analogy.

#### II. Variation with Respect to Density ($\delta \mathcal{S}_{\text{QGD}} / \delta (\text{Re } f) = 0$)

Varying the action with respect to the real component (osmotic potential $S_I$) returns the momentum transport equation. The extended stochastic algebra brings forth the **Generalized Hamilton-Jacobi Equation**:

$$\frac{\partial S_R}{\partial \tau} + \frac{1}{2m_0} g^{\mu\bar{\nu}} \partial_\mu S_R \partial_{\bar{\nu}} S_R + \mathcal{V}_{\text{ext}} - \frac{\hbar^2}{2m_0} \mathcal{D}^\mu \mathcal{D}_\mu \left( \frac{\nabla^2 R}{R} \right) = 0$$

Where $\mathcal{D}_\mu$ represents the covariant derivative extended with the Cartan torsion. The Bohm Quantum Potential emerges naturally as the elastic tension response against the compression of the mesh.

#### III. Variation with Respect to the Complex Metric ($\delta \mathcal{S}_{\text{QGD}} / \delta g^{\mu\bar{\nu}} = 0$)

When we vary the metric mesh of spacetime, we balance the curvature of the universe with the energy-momentum tensor generated by the fluctuations of the quantum fluid. The result is the dynamic equation of the **Extended Ricci Soliton**:
$$\mathcal{R}_{\mu\bar{\nu}} + \nabla_\mu \nabla_{\bar{\nu}} f = \frac{1}{\tau} \mathcal{T}_{\mu\bar{\nu}}^{\text{quântico}}$$
This equation dictates the geometric behavior of the theory: spacetime is neither flat nor static; it deforms and flows ($\mathcal{R}_{\mu\bar{\nu}}$) at the exact rate necessary to accommodate the soliton's quantum pressure gradient ($\nabla_\mu \nabla_{\bar{\nu}} f$), eliminating any possibility of infinite collapse (ultraviolet singularity).

> [!note]- The Geometric Noether Theorem: Proof that Continuity is the Conserved Current of Phase Symmetry
> 
> ![[notes/4/nota 4.3]]

---

### 4.3 Loop Regularization and the Cartan Cut-off Scale $\Lambda_C$

In the evaluation of radiative quantum loop corrections within the QGD Functional Action, the calculation of self-energy diagrams typically suffers from ultraviolet divergences in the high-energy limit (small distances). It is demonstrated here how the Cartan torsion geometry acts as a natural regulator of the vacuum, introducing an intrinsic cut-off scale that replaces artificial regularization schemes.

To avoid ambiguities with the cosmological sector, the distinction between the acting scales is rigorously defined:

- **$\Lambda_C$ (Cartan Ultraviolet Scale):** The upper momentum regulator parameter, determined by the elastic packing density of the Kähler network.
    
- **$\rho_\Lambda$ (Infrared Cosmological Constant):** The residual elastic energy density observable at the macroscopic Hubble scale.
    

#### A. The Propagator Modified by Cartan Torsion

The presence of the completely antisymmetric Cartan torsion tensor, $B_{\mu\nu\lambda}$, introduces a non-local gauge coupling that modifies the fermionic field's Green function (propagator). The regularized propagator in momentum space $p^\mu$ incorporates the rigidity of the elastic network through a geometric damping factor:

$$S_F(p) = \frac{1}{\gamma^\mu p_\mu - m_0 - i \Pi_{\text{torsão}}(p^2)}$$

Where the torsional self-energy operator $\Pi_{\text{torsão}}(p^2)$ functions as a topological low-pass filter. For momenta that exceed the critical vibration frequency of the Kähler network, torsion generates a dissipative potential barrier. This behavior is parameterized analytically by introducing the smooth cut-off function based on the invariant $\Lambda_C$:

$$\Pi_{\text{torsão}}(p^2) \propto \exp\left( \frac{p^2}{\Lambda_C^2} \right)$$

#### B. First-Order Loop Resolution (Electron Self-Energy)

Consider the calculation of the loop diagram of an ordinary quantum vertex, whose momentum integral in 4-dimensional Euclidean space would traditionally diverge logarithmically:

$$\Sigma(p) = e^2 \int \frac{d^4 k}{(2\pi)^4} \gamma^\mu S_F(p - k) \gamma^\nu D_{\mu\nu}(k)$$

Substituting the modified QGD propagator, the presence of the scale $\Lambda_C$ in the denominator of the integrand acts as a smooth limiter that suppresses the infinite momentum contributions ($k \to \infty$). The integral becomes strictly bounded and perfectly convergent:

$$\Sigma(p) = e^2 \int_0^{\Lambda_C} \frac{k^3 \, dk}{8\pi^2} \frac{2m_0 - \cancel{k}}{k^2 + m_0^2} \cdot \exp\left( -\frac{k^2}{\Lambda_C^2} \right)$$

The direct integration of this expression under the saddle point of the Perelman functional $\text{Min}(\mathcal{W})$ distills the result into the regular regularized form:

$$\Sigma(p) = \frac{e^2 m_0}{4\pi^2} \left[ \ln\left( \frac{\Lambda_C^2}{m_0^2} \right) - \gamma_E + \mathcal{O}\left(\frac{m_0^2}{\Lambda_C^2}\right) \right]$$

Where $\gamma_E$ is the Euler-Mascheroni constant.

#### C. Scale Independence: $\Lambda_C$ vs. $\rho_\Lambda$

It becomes evident from this formalism that the _cut-off_ $\Lambda_C$ is a quantity of the ultraviolet sector ($\Lambda_C \approx 1 \text{ GeV}$), determined by the finite size of the geometric stoma of the fundamental soliton ($r_p \propto 1/\Lambda_C$).

In contrast, the macroscopic cosmological constant $\Lambda$ arises only after the one-dimensional holographic dilution process (as demonstrated in Chapter 22), operating at the opposite end of the spectrum (the cosmological infrared):

$$\rho_\Lambda = \rho_{\text{rede}} \left( \frac{r_p}{R_H} \right) \propto \frac{\Lambda_C^4}{R_H}$$

This explicit notational separation eliminates the ambiguity pointed out by the review. It is proven that loop regularization in QGD is a direct consequence of the intrinsic and finite geometry of the Kähler network at scale $\Lambda_C$, without implying a massive or divergent value for the cosmic dark energy $\rho_\Lambda$.

> [!note]- Convergence Theorem: Analytical demonstration of the absence of Blow-Up in the geometric flow
> 
> ![[notes/4/nota_4.4_convergencia_fluxo]]

> [!note]- Addendum: The Topological Derivation of Quantized Charge via Mayer-Vietoris Surgery
> 
> ![[notes/4/nota_4.9_carga_quantizada.md]]

> [!note]- Addendum: Rheological Ontology of the Quadripotential and Locality in the Aharonov-Bohm Effect
> 
> ![[notes/4/nota_4.10_aharonov_bohm.md]]
