# Chapter 40 - The Aharonov-Bohm Effect and the Mechanical-Geometric Ontology of Gauge Potentials

## 40.1 Comparison between the Conventional Formulation and the QGD Approach

In quantum mechanics and classical electrodynamics, the Aharonov-Bohm Effect describes a situation in which a charged particle, when moving through a region with a null magnetic field ($\mathbf{B} = \nabla \times \mathbf{A} = 0$), experiences a phase shift in its interference pattern due to the presence of the vector potential $\mathbf{A}$ outside the solenoid. In the conventional interpretation, this effect highlights the physical relevance of gauge potentials in the quantum regime.

Within the framework of [[02 - The Geometrization of Matter|Quantum Geometrodynamics (QGD)]], gauge potentials are interpreted as representations of flows and [[08 - Black Hole Singularity|elastic deformations]] in the vacuum lattice. Under this perspective, the gauge potential $\mathbf{A}$ is related to the local shear velocity of the continuous flow of the lattice.

The magnetic field $\mathbf{B}$ describes the macroscopic [[09 - Spin and Cartan Geometry - The Vorticity of Spacetime|vorticity]] (or metric antisymmetric [[09 - Spin and Cartan Geometry - The Vorticity of Spacetime|Cartan torsion]]) concentrated inside the solenoid. Thus, when circling the solenoid, the behavior of the particle is described by the interaction with the local flow, irrotational yet under elastic tension, of the surrounding vacuum.

---

## 40.2 Hydrodynamic-Geometric Formulation of the Phase Shift

Matter in QGD is described by the polar representation of the flow density function, whose density $\rho = R^2$ maps the invariant volume and the gradient of the phase $S$ determines the local kinematics. In the three-dimensional space outside the solenoid, the region occupied by the electron flow is multiply connected (topology of a punctured cylinder, $M \approx \mathbb{R}^3 \setminus D^2$, where $D^2$ represents the cross-section of the solenoid).

The complex momentum 1-form $\omega$ that dictates the continuous flow of the lattice incorporates the minimal coupling as a primary metric distortion:

$$\omega = p_\mu dx^\mu = \left( \hbar \partial_\mu S - \frac{e}{c} A_\mu \right) dx^\mu$$

Outside the solenoid, the condition that the macroscopic torsion field (classical electromagnetism) vanishes imposes that the curvature of the gauge connection be zero, implying that the 1-form $A = A_\mu dx^\mu$ is locally closed ($dA = 0$). However, due to the non-trivial topology of the manifold ($\pi_1(M) = \mathbb{Z}$), the form is not exact.

The [[10 - Mechanical-Geometric Resolution of the Stern-Gerlach Experiment|continuous flow velocity]] $\mathbf{u}$ is given by the local momentum balance from QGD first principles:

$$\mathbf{u} = \frac{\hbar}{m} \nabla S - \frac{e}{mc} \mathbf{A}$$

Since the fluid is incompressible and stationary in the stable transit region, the circulation of the velocity field along a closed curve $\gamma$ enclosing the solenoid quantifies the topological memory fixed by the entrapment of the relaxing geometric flow.

---

## 40.3 The Holonomy Integral and the Mayer-Vietoris Theorem

By dividing the continuous flow into the two possible routes around the solenoid (Path 1, upper, and Path 2, lower), the configuration space is decomposed via Mayer-Vietoris topological surgery into the open subdomains $U_1$ and $U_2$, whose intersection involves the slit and detection regions.

The total accumulated phase shift $\Delta \phi$ in the interference fringe arises from the geometric action difference between the two flow streams along the gluing boundary:

$$\Delta \phi = \oint_{\gamma} \nabla S \cdot d\mathbf{r} = \int_{\gamma_1} \nabla S \cdot d\mathbf{r} - \int_{\gamma_2} \nabla S \cdot d\mathbf{r}$$

Substituting the definition of the continuous flow velocity $\mathbf{u}$, we extract the intrinsic elastic coupling:

$$\Delta \phi = \frac{m}{\hbar} \oint_{\gamma} \mathbf{u} \cdot d\mathbf{r} + \frac{e}{\hbar c} \oint_{\gamma} \mathbf{A} \cdot d\mathbf{r}$$

In QGD, the [[34 - Monopoles and the Hopf Fibration|Wallstrom-Bohm]] phase quantization condition is natively guaranteed by the holomorphic rigidity of the background elastic lattice, which locks the mechanical circulation of the pure elastic flow ($\oint \mathbf{u} \cdot d\mathbf{r} = 0$) outside the stoma regions (zero vorticity in the vicinity). Consequently:

$$\Delta \phi = \frac{e}{\hbar c} \oint_{\gamma} \mathbf{A} \cdot d\mathbf{r}$$

Using the generalized Stokes' Theorem over the compact submanifold of the solenoid cross-section $\Sigma$ (where the boundary $\partial\Sigma = \gamma$), the integral of the vector potential (vacuum shear) converts identically into the flux of the [[09 - Spin and Cartan Geometry - The Vorticity of Spacetime|Cartan torsion]] 3-form $\mathcal{T}$ (The sequestered magnetic flux $\Phi$):

$$\oint_{\gamma} \mathbf{A} \cdot d\mathbf{r} = \iint_{\Sigma} (\nabla \times \mathbf{A}) \cdot d\mathbf{\Sigma} = \iint_{\Sigma} \mathbf{B} \cdot d\mathbf{\Sigma} = \Phi$$

Therefore, the geometric phase shift is rigidly locked by the topological invariant of the barrier:

$$\Delta \phi = \frac{e \Phi}{\hbar c}$$

---

## 40.4 The Local Mechanism: Vacuum Shear and Impedance

The QGD description of the Aharonov-Bohm Effect is based on two main aspects:

1.  **The Rheological Nature of $\mathbf{A}$**: In QGD, gauge fixing is related to vacuum rheology, such that $\mathbf{A}$ describes the convective drag and the shear deformation of the [[12 -  The Quantum Tunneling Time (Hartman Effect)|Kähler metric]] outside the solenoid, which alters the local metric and connection.
    
2.  **Evolution by the [[17 - Monotonicity under Cartan Torsion|Perelman flow]]**: Although the core of the singularity does not penetrate the region with internal vorticity of the solenoid, the soliton presents a spatial extension associated with the flow. The evolution of the [[17 - Monotonicity under Cartan Torsion|metric entropy functional $\mathcal{W}$]] requires integration over the manifold, such that the impedance at the boundary of the solenoid influences the gradient of the [[10 - Mechanical-Geometric Resolution of the Stern-Gerlach Experiment|Bohm quantum potential]] in the external region.

In this way, the motion of the electron is locally conditioned by a metric deformation that reflects the homological structure arising from the presence of the solenoid, offering a purely geometric interpretation for the Aharonov-Bohm Effect.
