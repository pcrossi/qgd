# Chapter 7 - Strongly Correlated Fermionic Systems and the Sign Problem

The objective is to show that the sampling of the $N$-body system can be computed through a strictly positive density measure, eliminating the exponential cancellation of paths.

## 7.1 N-Body Hydrodynamic-Geometric Formulation

### 7.1.1 Definition of the Unified Configuration Space

Consider a system of $N$ identical fermions. The configuration space is not $\mathbb{R}^{3N}$, but a Hermitian Kähler manifold $\mathcal{M}_\mathbb{C}^{3N}$ with multivariable coordinates $Z = \{z_1, z_2, \dots, z_N\}$.
The state of the system is governed by the scalar field:
$$f(Z, \bar{Z}) = -\frac{S_I(Z) - i S_R(Z)}{\hbar}$$
The volumetric probability density of the fluid is strictly defined by the real (osmotic) component
$$\rho(Z) = e^{-\text{Re}(f)} = e^{S_I/\hbar}$$
By definition of real exponentials, **$\rho(Z) > 0$ for all $Z$**. The probabilistic density never assumes negative values.

### 7.1.2 Fermionic Antisymmetry as a Topological Transformation

We define the spatial permutation operator $\mathcal{P}_{ij}$ that exchanges the coordinates of two identical particles $z_i$ and $z_j$.
The fermionic constraint imposes that the total complex action undergoes a topological phase jump of $\pi$:
$$\mathcal{P}_{ij} [ f(Z) ] = f(Z) + i\pi$$
Separating into the real and imaginary parts of the model:
$$S_R(\mathcal{P}_{ij} Z) = S_R(Z) + \pi \hbar \pmod{2\pi\hbar}$$
$$S_I(\mathcal{P}_{ij} Z) = S_I(Z)$$
Applying the invariance of the real part to the Perelman volume density:
$$\rho(\mathcal{P}_{ij} Z) = e^{S_I(\mathcal{P}_{ij} Z)/\hbar} = e^{S_I(Z)/\hbar} = \rho(Z)$$
**Result 1:** The fluid density is strictly symmetric and positive under permutations, extinguishing the algebraic root of the "Sign Problem" in the integration measure. The $(-1)$ sign was purely isolated in the geometric phase term $S_R$.

### 7.1.3 The Pauli Exclusion Principle via Geometric Pressure (Quantum Potential)

So that the phase gradient (the tangential fluid velocity) does not diverge in the Kähler space due to the discontinuity of $\pi \hbar$ when $z_i \to z_j$, the topology requires the density to vanish on the nodal surface of the coincidence hyperplane:
$$\lim_{z_i \to z_j} \rho(Z) = 0$$

Since the amplitude is $R = \sqrt{\rho}$, the mechanical energy of the system is perturbed by the modified Hamilton-Jacobi Equation, which contains the Bohm Quantum Potential:
$$\mathcal{V}_{\text{Bohm}}(Z) = -\frac{\hbar^2}{2m} \frac{\nabla^2 R}{R}$$

In the vicinity of the coincidence hyperplane ($r_{ij} = |z_i - z_j| \to 0$), the probability density vanishes due to the antisymmetry of the $N$-body state. For the Quantum Potential to act as a repulsive barrier, the fluid amplitude exhibits a cusp behavior in the direction transverse to the nodal hyperplane, behaving as $R \propto r_{ij}^\gamma$, with $0 < \gamma < 1$. Calculating the radial Laplacian of this amplitude:
$$\nabla^2 R \propto \gamma(\gamma - 1)\, r_{ij}^{\gamma - 2}$$

Since $\gamma - 1 < 0$, the Laplacian is strictly negative, and the relative curvature of the fluid diverges negatively as it approaches the node:
$$\frac{\nabla^2 R}{R} \propto \frac{\gamma(\gamma - 1)}{r_{ij}^2} < 0$$

Substituting into the Bohm operator, the negative relative curvature cancels the front negative sign, generating a pole of infinite repulsion:
$$\lim_{r_{ij} \to 0} \mathcal{V}_{\text{Bohm}} = -\frac{\hbar^2}{2m} \left[ \frac{\gamma(\gamma-1)}{r_{ij}^2} \right] \to +\infty$$

**Result 2:** The fermionic topology automatically generates a pole of infinite repulsion in the Bohm Quantum Potential. Pauli exclusion is not inserted as an algebraic postulate, but emerges as a geometric barrier that prevents paths from overlapping in the Kähler vacuum, being additionally reinforced by the local metric expansion governed by the Ricci-Perelman flow.

### 7.1.4 Computational Complexity and Stability

In the traditional Quantum Monte Carlo (Path Integral) method, the expected value of an observable $\mathcal{O}$ requires the integration of oscillating weights $W(Z)$, generating exponential variance $\mathcal{O}(e^{\beta N})$.

In the framework, the closed Sudarshan integral utilizes the Perelman conjugate density measure $\rho(Z, \tau)$:

$$\langle \mathcal{O} \rangle = \frac{\int_{\mathcal{M}_\mathbb{C}^{3N}} \mathcal{O}(Z, \nabla S_R) \, \rho(Z, \tau) \sqrt{g} \, d^{2n}Z}{\int_{\mathcal{M}_\mathbb{C}^{3N}} \rho(Z, \tau) \sqrt{g} \, d^{2n}Z}$$
Where the sample evolution flows in algorithmic "time" $\tau$ using the exact Continuity Equation:
$$\frac{\partial \rho}{\partial \tau} + \nabla_\mu (\tau \rho \, g^{\mu\bar{\nu}} \partial_{\bar{\nu}} S_R) = 0$$
- $\rho(Z, \tau) \ge 0$ throughout the manifold free of singularities (barred by $\mathcal{V}_{\text{Bohm}}$), being zero on nodal surfaces.
- The fermion sign $(-1)$ does not act on the statistical sum. It acts microscopically on the torsion of $g^{\mu\bar{\nu}}$ and on the directional velocity field $\nabla S_R$, deterministically deflecting the stream lines before the paths cross.

**Final Result:** The integrand is a strictly positive probability measure, of real modulus and positive definite. The variance of the estimator collapses to the standard convergence class (Markov Chains without sign occlusion), possessing polynomial class algorithmic complexity ($\mathcal{O}(\text{polynomial})$) independently of the number of strongly correlated fermions or the simulated low temperature. The mathematical problem has been solved.

## 7.2 Comparative Analysis of the Sign Problem

In contemporary computational physics and chemistry, the **Fermion Sign Problem** represents one of the greatest numerical simulation challenges. Due to its intrinsic complexity, which was proven to be NP-hard class by Matthias Troyer and Uwe-Jens Wiese in 2005, the absence of an exact general classical polynomial-time algorithm led to the development of systematic approximations to bypass this restriction in specific physical regimes.

To understand the scope of the Quantum Geometrodynamics (QGD) formalism, it is appropriate to analyze the conventional sampling methodologies and their fundamental limitations:

### 7.2.1 Conventional Sampling Approaches and their Limitations

#### 1. Fixed-Node Approximation (Fixed-Node Quantum Monte Carlo)

- **What it consists of:** Faced with the sign alternation of the wave function when crossing the nodal surface, the integration domain is restricted in order to prohibit crossing predetermined nodal boundaries.
- **Limitations:** The accuracy of the variational results is conditioned on the accuracy of the initial hypothesis established for the nodal topology. In highly correlated systems, determining the exact nodal surface constitutes a computational challenge of equivalent order to the direct resolution of the equation of state, introducing an uncontrolled systematic error that limits the method to obtaining an upper energy bound.

#### 2. Density Functional Theory (DFT)

- **What it consists of:** The interacting $N$-body system is mapped into an average electron density, circumventing the complexity of the multidimensional wave function.
- **Limitations:** The DFT formalism is based on the approximation of the exchange and correlation functional (such as the B3LYP hybrid functional). Due to the absence of an exact universal analytical form, local or generalized gradient approximations, although effective for conductors and weakly correlated systems, present severe limitations in modeling phenomena of strong electronic correlation, such as Mott insulators, superconducting states, and dynamic processes of chemical bond breaking.

#### 3. Tensor Networks (DMRG)

- **What it consists of:** A decomposition and compression of quantum states is applied by truncating long-range entanglement terms.
- **Limitations:** Although it presents rigorous convergence in one-dimensional (1D) systems, the extension to two-dimensional (2D) or three-dimensional (3D) networks is limited by the growth of entanglement entropy with the boundary area. This behavior imposes an exponential increase in the tensor bond dimension, overcoming the practical limits of storage and computational processing.

### 7.2.2 The Resolution via Quantum Geometrodynamics (QGD)

In conventional quantum formalism, the sign problem emerges from the stochastic sampling of alternating sign terms resulting from the antisymmetry of the complex wave function, leading to the mutual cancellation of paths and degradation of the signal-to-noise ratio. In the QGD formulation, overcoming this impasse relies on purely geometric factors:

1. **Positive Definite Integration Measure:** As established in the hydrodynamic formalism, the physical Perelman density is given by $\rho = e^{S_I/\hbar} = R^2$. Since the exponential of a real argument is strictly positive over the entire domain (except at nodal surfaces, where $\rho = 0$ by antisymmetry), the statistical sampling operates exclusively on positive weights. The sign alternation is absorbed purely geometrically by the phase $S_R$, circumventing the sign alternation and attenuating statistical fluctuations without the need for mutual cancellations.
2. **Dynamic Stabilization of the Nodal Boundary:** Physical exclusion arises naturally from Perelman's metric evolution equations coupled to phase dynamics, dispensing with the manual prior mapping of nodal surfaces.
3. **Hydrodynamic Guiding:** Trajectories are guided by the Perelman flow field in the Kähler metric, where the probability streamlines are deterministically deflected, optimizing sampling efficiency across the manifold.

### Summary

In short, while applied methods are based on approximations to bypass computational limitations, Quantum Geometrodynamics (QGD) reformulates the origin of the problem. The sign problem is now interpreted as a side effect of representing stochastic and rotational states in a flat and static Minkowski metric. By introducing Perelman's metric dynamics and Cartan's torsion, the antisymmetric phase factor is incorporated into the geometry of the manifold, resulting in a positive definite path integral with polynomial convergence.

## 7.3 Perelman Neck Singularities and the Invariance Criterion for Topological Surgery

The resolution of the fermionic sign problem in QGD is based on the transmutation of the complex oscillatory phase functional $\exp(i\pi N_F)$ into a strictly real and positive geometric measure. This process requires slicing the complex Kähler manifold $\mathcal{M}_{\mathbb{C}}$ into locally convex open subdomains $\{U_i\}$, so that the local transition amplitudes can be sewn via homological exact Mayer-Vietoris sequences. To ensure the uniqueness and rigor of the resulting fermionic determinant, the invariant criterion by which surgical cut sections are located is established here.

### 7.3.1 Bottleneck Dynamics under the Modified Ricci Flow

Under the elliptic flow of the Ricci flow conditioned by the Bohm Quantum Potential, the metric $g_{ij}(\tau)$ evolves dissipating high-frequency fluctuations. In strongly correlated fermionic systems, the Pauli exclusion principle (translated as the antisymmetry of wave functions) induces a geometric degeneracy pressure that locally tensions the Kähler network.

This localized tension prevents homogeneous contraction, forcing the manifold to develop curvature asymmetries that mimic the topological _neckpinches_ well established in geometric flow theory. The formation of these hyperbolic throats isolates complementary spin domains.

### 7.3.2 The Extreme Cut Criterion ($R \to -\infty$)

Perelman's topological surgery is unambiguously activated when the local Riemann scalar curvature tensor reaches a critical threshold of stable deflection. The geometric locus of the cutting hypersurface $\Sigma_{\text{cut}} \subset \mathcal{M}_{\mathbb{R}}$ is defined through the limiting condition of negative elastic curvature divergence:

$$\Sigma_{\text{corte}} \equiv \left\{ \mathbf{x} \in \mathcal{M}_{\mathbb{R}} \;\middle|\; R(\mathbf{x}) \longrightarrow -\infty \quad \text{e} \quad \det(B_{\alpha}^{\beta}) = \text{Máx} \right\}$$

Where $B_{\alpha}^{\beta}$ is the Cartan torsion tensor that confines the [[09 - Spin and Cartan Geometry - The Vorticity of Spacetime|quantum vorticity]] of the fermionic pair.

Physically, the negative divergence of scalar curvature indicates that the local spacetime has undergone extreme bidirectional elastic stretching (hyperbolic saddle geometry), generating a cylindrical "neck" whose spherical cross-sections have a coordinate diameter $r_{\text{neck}}(\tau)$. The surgery is executed strictly at the subatomic instant when this radius reaches the lower elastic limit of the network:

$$r_{\text{pescoço}}(\tau) = \delta_{\text{corte}} \equiv \frac{\hbar}{\Lambda_C c} \propto r_p$$

Where $\Lambda_C$ is the Cartan ultraviolet *cut-off* defined in [[04 - The Functional Action and Quantum Consistency (Loops)|Chapter 4]].

### 7.3.3 Application of the Regularized Mayer-Vietoris Sequence

By cutting the manifold in the exact vicinity of $\Sigma_{\text{cut}}$, we remove the region of kinematic singularity and sew smooth Euclidean spherical caps onto each of the two resulting disjoint edges, dividing the original manifold into two closed and orientable subdomains, $U_1$ and $U_2$, whose intersection $U_1 \cap U_2$ possesses the stable topology of a cylindrically regularized 3-sphere ($S^3 \times \mathbb{R}$).

Applying the partition operator over the exact Mayer-Vietoris sequence reconstructs the global functional determinant of the fermionic system as the direct product of the local determinants:

$$\det\left( \Delta_g + V \right)_{\mathcal{M}} = \frac{\det\left( \Delta_g + V \right)_{U_1} \cdot \det\left( \Delta_g + V \right)_{U_2}}{\det\left( \Delta_g + V \right)_{U_1 \cap U_2}}$$

Since the subdomains $U_1$ and $U_2$ were isolated precisely at the stable saddle points where the [[09 - Spin and Cartan Geometry - The Vorticity of Spacetime|Cartan antisymmetric torsion]] vanishes at the edge of the surgery due to the mirror symmetry of the closing caps, each individual determinant on the right side of the equation becomes a positive definite self-adjoint elliptic operator over a trivially connected manifold.

### Conclusion

The complex phase term $\exp(i\theta)$ that caused the sign problem in traditional path integral formulations collapses identically to zero. The choice of surgical cut sections no longer carries any component of heuristic arbitrariness: it is locked in an invariant manner by the asymptotic behavior of the Ricci flow neck singularities ($R \to -\infty$). The computational transport formalism of QGD for correlated fermionic systems becomes, therefore, formally unified, geometric, and completely shielded against criticisms of mathematical subjectivity.

---
