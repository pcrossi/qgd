### Theoretical Addendum: The Problem of the Arrow of Time and Thermodynamic Causality

The problem of the arrow of time and the origin of macroscopic irreversibility from microscopic laws reversible under time inversion ($T$) constitute a central debate topic in mathematical physics (being formalized through discussions such as the Poincaré recurrence theorem and Loschmidt's paradox). In conventional quantum mechanics, irreversibility is frequently associated with the measurement postulate and wave packet reduction (Born's rule), whose local physical mechanism remains the subject of diverse interpretations.

Within the QGD framework, one investigates how macroscopic temporal asymmetry can be described from the geometric and rheological flow of the Hermitian vacuum under the Bismut Connection. It is proposed that, although the Riemannian metric component admits reversibility under $T$ inversion, the coupling with the antisymmetric Cartan torsion 3-form ($\mathcal{T}$) and the evolution under Perelman's entropy functional ($\mathcal{W}$) introduce a dissipative behavior at the microscopic level, whose statistical manifestation at the macroscopic scale correlates with the Second Law of Thermodynamics.

### 1. Physical Mechanism: The Asymmetry of Ricci Flow and Torsion

In general relativity and the Standard Model, spacetime is traditionally modeled by symmetric Riemannian geometry without torsion, ensuring the reversibility of geodesics under temporal reversal. In QGD, the presence of intrinsic angular momenta and quantum gauge currents is formulated by resorting to a Bismut mesh enriched with Cartan Torsion.

The equation describing the evolution of the metric and the Madelung-Perelman fluid assumes a parabolic character, directed by the gradient of the entropy functional $\mathcal{W}(g, \mathcal{T}, f)$. The evolution rate of the metric $g_{ij}$ and the torsion tensor $\mathcal{T}_{ijk}$ with respect to the flow scale parameter $\tau$ is expressed by:

$$\frac{\partial g_{ij}}{\partial \tau} = -2\left( R_{ij} + \nabla_i\nabla_j f - \frac{1}{4} \mathcal{T}_{ikm}\mathcal{T}_{j}^{\phantom{j}km} \right)$$

$$\frac{\partial \mathcal{T}_{ijk}}{\partial \tau} = \Delta_{\text{LB}} \mathcal{T}_{ijk} + \mathcal{R}_{i}^{\phantom{i}m} \mathcal{T}_{mjk} + \mathcal{L}_{\mathbf{v}} \mathcal{T}_{ijk}$$

The presence of the Laplace-Beltrami Laplacian ($\Delta_{\text{LB}}$) in the torsional tensor's evolution confers a diffusive behavior to this sector. Cartan torsion acts analogously to a viscoelastic vorticity in the lattice. Local fluctuations or solitonic excitations that deform the vacuum mesh dissipate residual metric energy in the form of high-frequency elastic torsional oscillations. Given that Perelman's functional is monotonically increasing along the flow ($\frac{d\mathcal{W}}{d\tau} \geq 0$), the system's dynamics is oriented towards the flow's stable states, disfavoring the spontaneous return to configurations of lower geometric entropy.

### 2. Relation to Macroscopic Irreversibility ($t$)

To correlate the flow evolution parameter $\tau$ with the macroscopic coordinate time $t$ measured by thermal systems, one adopts the parametrization of time $t$ associated with the advance of the phase fronts of the functional action $\mathcal{S}_{\text{QGD}}$ in Madelung hydrodynamics.

When analyzing the statistical behavior of a solitonic configuration in a three-dimensional complex submanifold, the rate of change of macroscopic entropy ($S_{\text{macro}}$) can be related to the norm of the torsion integrated over the volume:

$$\frac{dS_{\text{macro}}}{dt} = \lim_{V \to \infty} \frac{1}{V} \int_{\mathcal{M}} \left( \mathcal{T}_{ijk} \mathcal{T}^{ijk} \right) e^{-f} \sqrt{\det g} \, d^3x$$

Since the norm $\mathcal{T}_{ijk}\mathcal{T}^{ijk}$ is positive-definite by the background Hermitian metric and the Madelung density $\rho = e^{-f}$ is positive, the macroscopic rate of change satisfies the condition:

$$\frac{dS_{\text{macro}}}{dt} \geq 0$$

Strict equality is achieved only in idealized flat vacuum configurations devoid of torsion ($\mathcal{T} = 0$). In the presence of matter or during topological transition processes (Perelman surgeries), the dynamics involves the rearrangement of microscopic torsion in the lattice.

In this model, macroscopic irreversibility is described as the system's tendency to evolve towards the elastic and dissipative equilibrium dictated by the monotonicity of Perelman's functional. The local dissipation of spacetime torsion in the microscopic regime acts as a channel for the emergence of unidirectional dynamics at the macroscopic scale.
