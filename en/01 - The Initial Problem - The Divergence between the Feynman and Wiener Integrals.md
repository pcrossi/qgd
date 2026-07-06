---
title: Stochastic Torsion Theory of Gravitation
subtitle: "1 - The Initial Problem - The Divergence between the Feynman and Wiener Integrals"
author: Pedro Rossi
version: 0.1
date: 2026-06-20
status: Working Paper
---
## 1 - The Initial Problem - The Divergence between the Feynman and Wiener Integrals

The idea of the Hydrodynamic-Geometric Field Theory is born from a historical paradox at the heart of quantum mechanics and statistical mechanics. The construction begins by questioning the fundamental difference between two mathematical formalisms designed to integrate over a space of paths (trajectories): the Wiener Integral and the Feynman Path Integral.

Although both share a similar mathematical basis, they diverge in the nature of their measure and the physical context in which they operate.

The fundamental difference between the two formalisms lies in the domain of numbers in which their integrands operate:
- **Wiener Integral (Probabilistic Approach):** Developed in the 1920s to mathematically formalize Brownian motion, it deals strictly with real probabilities;
- It is mathematically rigorous, defining a well-behaved probability measure over the space of continuous functions;
- The weight term in the integrand is real and negative, acting as a Gaussian damping factor associated with diffusion equations: $$e^{-\int_{t_0}^{t_1} \frac{1}{2} \left(\frac{dx}{dt}\right)^2 dt}.$$
- **Path Integral (Quantum Approach):** Proposed in the 1940s, it deals with complex probability amplitudes, replacing the single classical trajectory with a sum over all possible trajectories;
- Historically, it lacks rigor in standard measure theory, not possessing a self-consistent complex measure without the application of limits and regularizations;
- The weight of the integrand is a complex oscillatory phase governed by the Classical Action $S[x(t)]$:
    $$e^{\frac{i}{\hbar} \int_{t_0}^{t_1} L(x, \dot{x}, t) dt}.$$
The table below summarizes the central distinctions between the formalisms:

| **Characteristic**     | **Wiener Integral**                  | **Feynman Path Integral**                             |
| ---------------------- | --------------------------------------- | -------------------------------------------------------- |
| **Physical Domain**    | Statistical Physics (Heat / Diffusion)    | Quantum Mechanics / QFT                                  |
| **Mathematical Rigor** | Rigorous (Well-defined measure)          | Formal (Requires regularization)                             |
| **Integrand Weight**   | Real and decreasing ($e^{-\text{Action}}$) | Complex and oscillatory ($e^{i \cdot \text{Action}/\hbar}$) |
| **Associated Equation**| Fokker-Planck / Heat Equation        | Schrödinger Equation                                   |

### The Wick Rotation and the Limits of Equivalence

The mathematical bridge that historically unites these two formalisms is the Wick Rotation. Through an analytic continuation that transforms real time $t$ into an "imaginary time" $\tau$ through the substitution $t = -i\tau$, the Schrödinger equation converts into the heat equation. Consequently, the quantum oscillatory factor $e^{\frac{i}{\hbar}S}$ becomes a real damping factor $e^{-S_E}$, where $S_E$ is the Euclidean Action.
In theory, the uniqueness theorem guarantees that, because they are analytic functions, the transformation preserves the information bijectively, allowing the rigor of the Wiener Integral to be used to solve the Feynman Integral. However, this formal transformation presents structural limitations when analyzed through the lens of gauge theories with boundary terms.

### The Breakdown of Invariance in the Total Derivative

A subtle limitation in the conventional application of the Wick Rotation in Quantum Field Theory arises in the treatment of temporal boundary terms. In classical and quantum mechanics, the action possesses gauge invariance; two Lagrangians are physically equivalent if they differ by a total time derivative:
$$L' = L + \frac{dF(x, t)}{dt}.$$

When integrated, this derivative transforms into a pure boundary term, preserving the original equations of motion. The mathematical problem occurs when we apply the Wick Rotation ($dt = -i d\tau$) to this structure:
- In the Minkowski domain (Feynman), the generated boundary term acts as a purely imaginary phase (unity) in the quantum amplitude, altering the global phase without affecting the probabilistic modulus;
- In the Euclidean domain (Wiener), the mutation of the derivative transforms this same phase into a purely real scale factor ($e^{-F}$), generating an exponential damping or growth at the boundaries of the temporal domain.

The classical invariance is altered because the total derivative generates a non-analytic discontinuity at the complex boundary. A trivial gauge transformation in real time alters the statistical convergence and the Boltzmann weight in the Wiener Integral. The direct correspondence between the Feynman and Wiener measures presents precise mathematical restrictions, showing itself to be strictly equivalent in Lagrangians where the surface terms are null or negligible.

To resolve this impasse and stabilize the formalism, it becomes advantageous to go beyond the idea of a static background for classical spacetime. The total derivative should not be treated as an isolated boundary, but rather as the flux of a geometric fluid density, suggesting the coupling to the Madelung decomposition.

### The Madelung Fluid: The Separation of the Wave into Amplitude and Phase

In conventional quantum mechanics, the wave function is primarily represented as a vector in an abstract state space. To investigate the correspondence with physical diffusion processes and geometric flows, it is useful to adopt the hydrodynamic representation that makes flow quantities explicit. We do this by applying the hydrodynamic decomposition originally proposed by Erwin Madelung in 1927.

We start from a generic wave equation and propose a solution using its polar form:
$$\psi(\mathbf{x}, t) = R(\mathbf{x}, t) e^{\frac{i}{\hbar} S(\mathbf{x}, t)}$$
In this formulation:
- $R(\mathbf{x}, t)$ represents the real amplitude of the wave;
- $S(\mathbf{x}, t)$ represents the real phase, which we physically identify as Hamilton's Principal Function (the Action).
By substituting this identity into the wave equation and separating the result, the mathematical structure cleanly collapses into two real and complementary equations.

#### The Imaginary Part: The Continuity Equation

By grouping the purely imaginary terms, the phase factor cancels out, revealing the conservation law of our system. To give physical meaning to this result, we make two fundamental definitions:
1. We define the fluid density (or probability) as $\rho = R^2$;
2. We define the local velocity field assuming the classical momentum relationship $\mathbf{p} = \nabla S$, resulting in $\mathbf{v} = \frac{\nabla S}{m}$.
Substituting these variables, the imaginary component instantly collapses into the classical Continuity Equation:
$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0$$
This equation is the gear we will use. It strictly guarantees that the density flux is conserved locally like a compressible fluid in space. It is the statistical component of the model, and it will ensure the diffusive Wiener measure.

#### The Real Part: The Hamilton-Jacobi Equation and the Quantum Potential

On the other hand, when we collect the strictly real terms, we find the equation that governs the mechanical dynamics of the system and its momentum propagation:
$$\frac{\partial S}{\partial t} + \frac{|\nabla S|^2}{2m} + V(\mathbf{x}) - \frac{\hbar^2}{2m} \frac{\nabla^2 R}{R} = 0.$$
If we take the purely classical limit and deactivate the factor $\hbar \to 0$, the last term disappears and we recover exactly the Hamilton-Jacobi Equation. However, quantum mechanics requires the presence of this residual term proportional to $\hbar^2$, which we identify as the **Bohm Quantum Potential**.

This term is not a "phantom force". It acts as an internal curvature pressure of the fluid itself. If the density $\rho$ tries to concentrate to collapse into a single point (a singularity), the Quantum Potential generates a geometric repulsive force that stabilizes the wave peak.

In pure diffusion (classical Wiener Integral), the probabilistic peaks simply collapse and flatten out statically. However, by coupling Continuity with Hamilton-Jacobi, the phase $S$ stores a "momentum memory" and acts as a geometric pressure. The phase gradient pushes the density in such a way that the peak rigidly displaces in spacetime, exactly emulating the behavior we macroscopically see as the "propagation of a wave" in the Feynman Integral.

In this view, the wave ceases to be an abstraction and becomes a ballistic flow governed by pressure and density.

### Non-Differentiability: Use of Wiener Noise

Our next structural obstacle is a fundamental mathematical incompatibility: the Wiener probability measure generates trajectories that are continuous, but non-differentiable. (Think of a fractal curve, where the Hausdorff dimension is 2).
The problem lies in the fact that, for a pure Brownian trajectory $x(t)$, the infinitesimal displacement behaves as $dx \sim \sqrt{dt}$. As a result, the classical temporal derivative $\frac{dx}{dt} \sim \frac{1}{\sqrt{dt}}$ diverges (explodes to infinity) when $dt \to 0$.

If the trajectories do not possess normal derivatives, our definition of the fluid velocity as $\mathbf{v} = \frac{\nabla S}{m}$ would be mathematically doomed. To carefully save Madelung hydrodynamics, we abandon classical differential calculus and adopt **Itô/Nelson Stochastic Calculus**.

#### 1. Nelson's Stochastic Derivatives and Sudarshan's Symmetry

To circumvent the divergence, we replace the ordinary derivative of a trajectory with **two mean stochastic derivatives** conditioned on the history of the fluid: one calculated for the future and another for the past. This division immediately evokes the bidirectional symmetry (advanced/retarded) of Sudarshan's Theorem in the complex plane.

- **Forward Derivative ($D_+$):** Measures the future tendency (retarded potential):$$D_+ x(t) = \lim_{\Delta t \to 0^+} \mathbb{E} \left[ \frac{x(t + \Delta t) - x(t)}{\Delta t} \Bigg| \mathcal{F}_t \right] = \mathbf{v}_+;$$- **Backward Derivative ($D_-$):** Measures the past tendency (advanced potential): $$D_- x(t) = \lim_{\Delta t \to 0^+} \mathbb{E} \left[ \frac{x(t) - x(t - \Delta t)}{\Delta t} \Bigg| \mathcal{P}_t \right] = \mathbf{v}_-.$$
Due to the harshness of the fractal Wiener noise, the forward-looking velocity is not equal to the backward-looking one ($\mathbf{v}_+ \neq \mathbf{v}_-$). However, we notice that, although the individual trajectory is chaotic, the mean functions $\mathbf{v}_+$ and $\mathbf{v}_-$ are perfectly regular, differentiable and well-behaved.

> [!note]- Definition of $\mathcal{F}_t$ (Filtration)
> 
> ![[notes/1/note 1.1]]

#### 2. The Separation of Velocities: Current and Diffusion

By linearly combining these two velocities of Nelson's calculus, the behavior of the fluid neatly decomposes into two natures:
1. **Current Velocity ($\mathbf{v}$):** It is the symmetric mean, the real physical velocity that rigidly transports the wave peak (the component associated with Madelung conservation).
$$\mathbf{v} = \frac{\mathbf{v}_+ + \mathbf{v}_-}{2}.$$
2. **Diffusion Velocity ($\mathbf{u}$):** It is the osmotic velocity that spreads and broadens the density (the component associated with Wiener diffusion and Perelman entropy).    $$\mathbf{u} = \frac{\mathbf{v}_+ - \mathbf{v}_-}{2}.$$
Following Fick's Law of Diffusion, this osmotic velocity $\mathbf{u}$ responds directly to the local probability gradient $\rho$:
$$\mathbf{u} = \nu \frac{\nabla \rho}{\rho} = 2\nu \frac{\nabla R}{R}.$$
Where we define $\nu = \frac{\hbar}{2m}$ as the intrinsic stochastic diffusion coefficient of the quantum vacuum.

#### 3. The Action and the Bohm Potential

With this, the gradient of the Hamilton-Jacobi action begins to act exclusively on the Mean Current Velocity ($\mathbf{v} = \frac{\nabla S}{m}$), ignoring the roughness of the microscopic trajectory.

The real detail occurs when we calculate the stochastic acceleration of the system by combining the derivatives $D_+$ and $D_-$ quadratically. The microscopic Wiener divergences cancel each other out and result in our Modified Hamilton-Jacobi Equation:
$$\frac{\partial S}{\partial t} + \frac{|\nabla S|^2}{2m} + V(x) - \left( \frac{1}{2} m \mathbf{u}^2 + \nu m \nabla \cdot \mathbf{u} \right) = 0.$$
If we take the "Stochastic Pressure Term" generated by the vacuum noise and substitute $\mathbf{u} = \frac{\hbar}{2m} \frac{\nabla \rho}{\rho}$, the algebra collapses yielding an exact result:
$$\frac{1}{2} m \mathbf{u}^2 + \nu m \nabla \cdot \mathbf{u} = \frac{\hbar^2}{2m} \frac{\nabla^2 R}{R},$$
which is the Bohm Quantum Potential (with a negative sign in the Hamilton-Jacobi Equation to act as a repulsive energy barrier).

> [!note]- The Derivation of Pressure Terms
> 
> ![[notes/1/note 1.2]]

In this way, the non-differentiability problem is solved. The quantum velocity $\mathbf{v}$ did not need to describe the vector of an individual trajectory, but rather the mean velocity field of a statistical ensemble of paths in diffusion.

---

### 1.2 Universalization of the Kähler Diffusion Coefficient and the Emergence of Solitonic Inertia

The classical formulation of stochastic calculus applied to quantum mechanics, introduced by Edward Nelson, defines the forward ($D_+$) and backward ($D_-$) temporal derivatives of a Brownian fluctuation coordinate $x(t)$ through a diffusion coefficient $\nu$ fixed as:

$$\nu = \frac{\hbar}{2m}$$

Where $m$ represents the mass of the particle under analysis. From the perspective of Quantum Geometrodynamics (QGD), this formulation presents a conceptual limitation, since the mechanical and transport properties of the Kähler vacuum (the fundamental network) cannot be regulated by parameters of exogenous particles.

To cure this conceptual gap, we define that the Kähler vacuum possesses an **intrinsic universal diffusion constant $\nu_0$**, associated with the kinematic flow viscosity of the vacuum fluid:

$$\nu_0 \equiv \frac{\hbar}{2m_0}$$

Here, the cut-off mass scale $m_0$ does not act as a free empirical constant ("seed") postulated ad-hoc. In the Directed Acyclic Graph (DAG) of the causal consistency of QGD, the mass $m_0$ is rigorously deduced as a **dynamic attractor (low-energy output) resulting from the conformal confinement horizon**. It represents the physical scale at which the Perelman-Madelung flow stabilizes the fundamental baryonic soliton (the neutron) against collapse, emerging directly from metric rigidity and the compactified holonomy group.

#### A. The Scaling Density of the Metric

When a particle or local excitation manifests in the network, it does not represent the insertion of an external point mass, but rather a **local volumetric deformation and contraction of the Kähler metric $g_{ij}$ itself** guided by the minimum of the functional $\mathcal{W}$. We define the local elastic compression factor $\Omega(\mathbf{x}, t)$ as the ratio between the energy density of the local perturbation and the baseline density of the network:

$$\Omega(\mathbf{x}, t) \equiv \frac{m(\mathbf{x}, t)}{m_0}$$

Where $m(\mathbf{x}, t)$ is the locally observed effective inertial mass. In this light, the localized inertia of a particle is the direct measure of how much elastic rigidity of the network was tensioned to trap the quantum vortex.

#### B. Generalization of the Stochastic Diffusion Equations

The introduction of the universal coefficient $\nu_0$ requires that Nelson's kinematic equations for the forward ($b_+$) and backward ($b_-$) translation velocity field be modulated by the geometric scale factor $\Omega$. The differential kinematic stochastic process for the network fluctuation is covariantly rewritten as:

$$dx^i(t) = b_\pm^i(x(t), t)dt + \sqrt{2\nu_0 \cdot \Omega^{-1}} \, dW^i(t)$$

Where $dW^i(t)$ is the standard Gaussian Wiener process with zero mean and variance $dt$.

Calculating the generalized stochastic derivatives through the modified Fokker-Planck equation, the mean flow velocity $v^i = \frac{1}{2}(b_+^i + b_-^i)$ and the diffusion or osmotic velocity $u^i = \frac{1}{2}(b_+^i - b_-^i)$ begin to incorporate the compressible geometry of the manifold:

$$u^i = \nu_0 \Omega^{-1} \nabla^i \ln \rho$$

Where $\rho$ is the hydrodynamic probability density of the fluid.

#### C. Momentum Conservation and the Emergence of the Bohm Potential

By applying Nelson's second stochastic law for the mean acceleration $a^i = \frac{1}{2}(D_+ b_-^i + D_- b_+^i) = \partial_t v^i + v^j \nabla_j v^i - u^j \nabla_j u^i - \nu_0 \Omega^{-1} \Delta u^i$, the vacuum force dynamics converges exactly and rigorously to:

$$m_0 \Omega \left( \frac{\partial v^i}{\partial t} + v^j \nabla_j v^i \right) = -\nabla^i \left( V_{\text{classical}} + Q_{\text{Bohm}} \right)$$

Substituting $\Omega = m/m_0$ and expanding the diffusive term, the term $m_0 \Omega$ simplifies directly into the local effective inertial mass $m$, restoring the classical Hamilton-Jacobi-Bohm equation:

$$m \left( \frac{\partial v^i}{\partial t} + v^j \nabla_j v^i \right) = -\nabla^i V_{\text{classical}} + \nabla^i \left( \frac{\hbar^2}{2m} \frac{\nabla^2 \sqrt{\rho}}{\sqrt{\rho}} \right)$$

#### Conclusion

This derivation proves analytically that the dependence of the mass $m$ in the Bohm potential and the effective diffusion coefficient is not a primitive or fundamental property of the vacuum. The vacuum diffuses information in a perfectly homogeneous and universal manner via $\nu_0$. The apparent variation of $\nu$ from particle to particle is an **illusion of scale caused by local metric contraction**: regions with higher effective inertia $m$ locally contract the tangent space of the Kähler manifold, proportionally decreasing the amplitude of local Brownian fluctuations by a factor of $\Omega^{-1}$. Nelson's conceptual gap is, therefore, formally resolved under the geometric paradigm of QGD.

---
