# Chapter 8 - The Stabilization of the Black Hole Singularity

In classical General Relativity, the collapse of a star of mass $M$ does not possess a repulsive force that supports the weight when the nuclear fuel runs out. Gravity pulls the radius of the star ($r_c$) to zero ($r_c \to 0$), and the gravitational energy goes to $-\infty$.

It is analytically demonstrated that, in the QGD formalism, the Bohm quantum potential induces a divergent repulsive pressure barrier in the ultraviolet limit.

## 8.1 Gravitational-Quantum Equilibrium Limit

### 8.1.1 Classical Gravitational Energy

For a collapsing spherical mass, the total gravitational potential energy is:
$$U_{\text{grav}} = - \frac{G M^2}{r_c}$$

### 8.1.2 The Geometric Bohm Pressure (QGD)

In the QGD formulation, the collapsing star is described as a [[01 - The Initial Problem - The Divergence between the Feynman and Wiener Integrals|Madelung fluid]]. When the radius $r_c$ decreases, the probability density $\rho(r)$ increases, concentrating as a Gaussian distribution in the center:
$$R(r) = \sqrt{\rho} = A e^{-\frac{r^2}{2r_c^2}}$$
Let's calculate the Bohm Quantum Potential ($\mathcal{V}_{\text{Bohm}} = -\frac{\hbar^2}{2m} \frac{\nabla^2 R}{R}$) for the fermions (mass $m$) that make up the center of the star ($r \to 0$):
- $\nabla^2 R = R \left( \frac{r^2}{r_c^4} - \frac{3}{r_c^2} \right)$
- $\mathcal{V}_{\text{Bohm}}(r \to 0) = -\frac{\hbar^2}{2m} \left( 0 - \frac{3}{r_c^2} \right) = \mathbf{+\frac{3\hbar^2}{2m r_c^2}}$

Since the star has $N = M/m$ particles, the total Topological Repulsion Energy of the core is:
$$U_{\text{Bohm}} = N \cdot \mathcal{V}_{\text{Bohm}} = \left(\frac{M}{m}\right) \frac{3\hbar^2}{2m r_c^2} = \mathbf{\frac{3\hbar^2 M}{2m^2 r_c^2}}$$

### 8.1.3 Equilibrium Point and Collapse Radius

The total energy of the system during the collapse is the sum of the gravitational attraction and the quantum repulsion:
$$E_{\text{total}}(r_c) = U_{\text{grav}} + U_{\text{Bohm}} = - \frac{G M^2}{r_c} + \frac{3\hbar^2 M}{2m^2 r_c^2}$$
To find the radius at which the collapse ceases (the equilibrium state of the [[02 - The Geometrization of Matter|Ricci Soliton]]), we derive the total energy with respect to the radius and set it to zero ($\frac{\partial E}{\partial r_c} = 0$):
$$\frac{G M^2}{r_c^2} - \frac{3\hbar^2 M}{m^2 r_c^3} = 0$$
Isolating the collapse radius $r_c$:
$$\frac{G M^2}{r_c^2} = \frac{3\hbar^2 M}{m^2 r_c^3}$$
$$r_c = \frac{3\hbar^2}{G M m^2}$$

**Mathematical Result:** The collapse radius $r_c$ is strictly greater than zero. The singularity ($r_c = 0$) is mathematically unattainable because geometric repulsion grows with $1/r^2$, while gravitational attraction grows with $1/r$. The collapse ceases at a finite radius, establishing a physically regular, dense, and asymptotically stable core configured as a [[02 - The Geometrization of Matter|Ricci Soliton]].

---

## 8.2 Astrophysical Stability and the Fermi-Bohm Degeneracy Limit

For a self-gravitating system composed of $N$ degenerate fermions under extreme compression, the total Bohm quantum repulsion potential must incorporate the distribution of allowed states in phase space. The integration over the Fermi sphere of kinetic energy for a fermion gas under spherical symmetry of radius $r_c$ provides the quantum pressure energy:
$$U_{\text{Pauli-Bohm}} \approx \frac{3}{10} \frac{\hbar^2}{m} \left( \frac{9\pi}{4} \right)^{2/3} \frac{N^{5/3}}{r_c^2}$$
By equating this degenerate repulsion to the star's Newtonian gravitational attraction ($U_{\text{grav}} = -\frac{3}{5}\frac{GM^2}{r_c}$), where the total mass is approximated by the number of nucleons ($M = N m_n$), the stable equilibrium radius of the Fermi-Bohm soliton is rigorously determined by:
$$r_{\text{equilíbrio}} \approx \frac{\hbar^2 (9\pi/4)^{2/3}}{G m_n^2 m} N^{-1/3} \propto M^{-1/3}$$
This correction re-establishes the scale of classical astrophysical thermodynamic stability ($r_c \propto M^{-1/3}$), anchoring the QGD stellar collapse in the Pauli Exclusion Principle.

---

## 8.3 The Covariant Formalism of the Energy-Momentum Tensor

### 8.3.1 The Covariant Bohm Energy-Momentum Tensor

We introduce the quantum contribution to spacetime by means of an effective quantum ideal fluid derived from the covariant Hamilton-Jacobi-Bohm formulation. The energy-momentum tensor associated with the quantum potential $Q$, denoted by $T_{\mu\nu}^{(\text{Bohm})}$, is defined as:
$$T_{\mu\nu}^{(\text{Bohm})} = (\rho_{\text{Bohm}} + P_Q) u_\mu u_\nu + P_Q g_{\mu\nu}$$
Where:
- $u_\mu$ is the four-velocity of the quantum fluid (normalized such that $u_\mu u^\mu = -1$).
- $\rho_{\text{Bohm}}$ is the energy density induced by the quantum field.
- $P_Q$ is the **repulsive quantum pressure**, explicitly given as a function of the Bohm quantum potential $Q$:
$$P_Q = - \rho_0 Q = \rho_0 \left( \frac{\hbar^2}{2m} \frac{\Box \sqrt{\rho_0}}{\sqrt{\rho_0}} \right)$$
where $\rho_0$ is the invariant probability density of the ensemble and $\Box \equiv g^{\alpha\beta}\nabla_\alpha\nabla_\beta$ is the covariant d'Alembertian operator in the background metric $g_{\mu\nu}$.

### 8.3.2 Coupling in the Einstein Equations and the Regime Transition

The modified field equations assume the form:
$$G_{\mu\nu} \equiv R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} = \kappa \left( T_{\mu\nu}^{(\text{Clássico})} + T_{\mu\nu}^{(\text{Bohm})} \right)$$

In the external asymptotic regime ($r \gg \ell_{\text{Planck}}$ or $r > r_s$), the probability density $\rho_0$ tends to a spatially homogeneous or evanescent distribution on the quantum scale, causing the gradients of $\sqrt{\rho_0}$ to collapse: $\nabla_\alpha \sqrt{\rho_0} \to 0 \implies Q \to 0$ and $P_Q \to 0$. Thus, $T_{\mu\nu}^{(\text{Bohm})} \to 0$, identically recovering the classical vacuum energy-momentum tensor ($T_{\mu\nu}^{(\text{Classical})} = 0$) and, consequently, the external [[28 - The Classical Limit and the Correspondence Principle|pure Schwarzschild metric]].

In the internal regime ($r \to 0$), the thickening of the collapse wave function generates an extreme gradient in $\rho_0$. The quantum potential $Q$ diverges positively with an inverted sign, triggering an **isotropic negative/repulsive quantum pressure** ($P_Q \ll 0$) that acts as a dynamic local cosmological constant, violating the Hawking-Penrose Strong Energy Condition (SEC). It is this strict geometric violation that prevents the formation of the point singularity, replacing it with a stable regular core of minimum radius $r_{\text{min}} \sim \ell_{\text{Planck}}$ (where $\ell_{\text{Planck}}$ is the [[04 - The Functional Action and Quantum Consistency (Loops)|Planck scale]]).

### 8.3.3 Proof of Conservation of the Energy-Momentum Tensor ($\nabla^\mu T_{\mu\nu} = 0$)

To guarantee physical consistency, the Bianchi identity ($\nabla^\mu G_{\mu\nu} = 0$) requires that $\nabla^\mu (T_{\mu\nu}^{(\text{Classical})} + T_{\mu\nu}^{(\text{Bohm})}) = 0$. Inside the horizon, where the classical term is negligible compared to the quantum magnitude, the divergence of $T_{\mu\nu}^{(\text{Bohm})}$ expands as:
$$\nabla^\mu T_{\mu\nu}^{(\text{Bohm})} = \nabla^\mu \left[ (\rho_{\text{Bohm}} + P_Q) u_\mu u_\nu \right] + \nabla_\nu P_Q = 0$$

Projecting this equation in the direction parallel and perpendicular to the four-velocity $u_\mu$:

1. **Longitudinal Projection ($u^\nu \nabla^\mu T_{\mu\nu} = 0$):** Results in the continuity equation for the Bohmian fluid, showing that the quantum energy flow is perfectly conserved along the fluid geodesics:
    $$u^\mu \nabla_\mu \rho_{\text{Bohm}} + (\rho_{\text{Bohm}} + P_Q) \nabla^\mu u_\mu = 0$$

2. **Transverse Projection (Modified Euler Equation):**
    $$(\rho_{\text{Bohm}} + P_Q) u^\mu \nabla^\mu u_\nu = - \left( g_{\nu\mu} + u_\nu u_\mu \right) \nabla^\mu P_Q$$

This last relation proves that the acceleration of the fluid geodesics ($u^\mu \nabla^\mu u_\nu$) is balanced exactly by the gradient of the quantum pressure $\nabla^\mu P_Q$. As the collapse advances, the quantum pressure gradient grows in the opposite direction to the classical gravitational attraction, zeroing the net acceleration exactly at $r = r_{\text{min}}$.

Since the transition between the tensor components is analytically mediated by the smooth and continuous variation of the wave function $\psi = \sqrt{\rho_0}e^{iS/\hbar}$ under the action of the $\Box$ operator, the regime transition is perfectly smooth ($C^\infty$), eliminating any physical "gap" or discontinuity in the metric structure of spacetime.

> [!note]- Addendum: Unitarity and Resolution of the Information Loss Paradox via Ricochet Flow
> 
> ![[notes/8/nota_8.5_informacao_bn.md]]
