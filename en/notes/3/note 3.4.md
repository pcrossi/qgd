### Global Quantization via Cauchy's Residue Theorem

The transition from local kinematic behavior to global boundary constraints occurs when we integrate the 1-form $\omega$ along a closed contour $\gamma$ circling the analytical poles of the manifold (the vorticity stomata). Applying the Residue Theorem in the complex domain:
$$\oint_\gamma \omega = \oint_\gamma \nabla_\mu S_C dx^\mu = 2\pi i \sum \text{Res}(\omega)$$
Substituting the decomposition of $p_\mu$ into the line integral, we have:
$$\oint_\gamma p_\mu^{\text{corrente}} dx^\mu + i \oint_\gamma u_\mu dx^\mu = 2\pi i \sum \text{Res}(\omega)$$
For the soliton to represent a closed and self-sustaining stationary state, the net osmotic flux through the asymptotic equilibrium contour must vanish ($\oint_\gamma u_\mu dx^\mu = 0$). Only the circulation of the real component remains, which coincides with the homological quantization condition of the action:
$$\oint_\gamma p_\mu^{\text{corrente}} dx^\mu = n h \implies 2\pi i \sum \text{Res}(\omega) = n h, \quad n \in \mathbb{Z}$$

### 1. Geometrically, what are the Residues of $\omega$?

In pure mathematical terms, the Kähler 1-form is given by $\omega = \nabla_\mu S_C dx^\mu$. If the Kähler manifold were perfectly smooth and hole-free, any integral of this form along a closed path $\gamma$ would be strictly **zero** (by Stokes' Theorem).

However, the model establishes that the quantum vacuum contains **stomata**. From a geometric and analytical standpoint, stomata are not ordinary points: they are **analytical poles (essential singularities)** where the fluid velocity diverges ($v \to \infty$) and the density collapses to zero ($\rho = 0$).

The **residue** is the exact measure of the "geometric obstruction" or "topological defect" contained within that singularity. When calculating the residue of $\omega$ at a stoma, we are measuring how much geometric information (complex area, accumulated torsion) is retained and "hidden" within that cut in the manifold, impossible to be eliminated by continuous deformations of the path.

### 2. Analytical Deduction: Why is the value $\frac{nh}{2\pi i}$?

The reason why the sum of the residues assumes the exact value of $\frac{nh}{2\pi i}$ stems from the forced marriage between **Cauchy's Residue Theorem** and the **Wave Function Monodromy (Single-valuedness) Condition**.

#### Step A: Cauchy's Theorem

By Cauchy's Residue Theorem, the line integral of a complex 1-form $\omega$ along a closed contour $\gamma$ enclosing these singularities is proportional to the sum of the residues of the internal poles:

$$\oint_\gamma \omega = 2\pi i \sum \text{Res}(\omega)$$

#### Step B: The Quantum Phase Condition

On the other hand, the Madelung fluid is described by the wave function $\Psi = e^{\frac{i}{\hbar} S_C}$. For the wave function $\Psi$ to have a stable physical meaning in spacetime, it must be **single-valued** (monodromic). This means that if an observer circulates along the closed loop $\gamma$ and returns to the same starting point, the wave function cannot have two different values.

For $\Psi_{\text{final}} = \Psi_{\text{inicial}}$, the phase factor accumulated in the circulation of the complex action must compulsorily be an integer multiple of $2\pi$:

$$\exp\left( \frac{i}{\hbar} \oint_\gamma \nabla_\mu S_C dx^\mu \right) = e^{2\pi i n}, \quad n \in \mathbb{Z}$$

Therefore, the line integral of the 1-form $\omega$ is forced by quantum mechanics to assume the value of an integer number of times Planck's constant ($h = 2\pi\hbar$):

$$\oint_\gamma \omega = n h$$

#### Step C: Residue Isolation

Now, we equate the two independent expressions we obtained for the same line integral $\oint_\gamma \omega$:

$$2\pi i \sum \text{Res}(\omega) = n h$$

Algebraically isolating the sum of the residues, the factor $2\pi i$ goes to divide the opposite side:

$$\sum \text{Res}(\omega) = \frac{nh}{2\pi i}$$

If we expand $h = 2\pi\hbar$ in this fraction, the cancellation operates cleanly:

$$\sum \text{Res}(\omega) = \frac{n(2\pi\hbar)}{2\pi i} = \frac{n\hbar}{i} = -i n\hbar$$

### 3. The Deep Physical Meaning of $-i n\hbar$

To say that the residue is worth $\frac{nh}{2\pi i}$ is the same as saying it is worth **$-i n\hbar$**. This mathematical signature carries three physical implications:

#### A. The Imaginary Nature of the Residue and the Osmotic Momentum

Note that the residue is **purely imaginary** (multiplied by $-i$). In the momentum expansion, the real term ($p_\mu^{\text{c}} = \nabla_\mu S_R$) dictates ballistic transport, while the imaginary term ($i u_\mu = -i \frac{\hbar}{2\rho}\nabla_\mu \rho$) dictates the vacuum's diffusive osmotic momentum.

The fact that the residue is imaginary means that the stoma's singularity injects **pure stochastic diffusion and quantum fluctuation** into the center of the hadron. It is the imaginary component of the residue that prevents matter from collapsing into a singular point of infinite density, acting as an internal geometric pressure.

#### B. The Integer $n$ as Topological Charge and Baryonic Index

The number $n \in \mathbb{Z}$ is not an arbitrary quantum number; it is the **winding number** or the **total net vorticity** trapped in the singularities.

- In the **Proton** model, we have 3 stomata whose summed residues result in a stable net topological index ($n=1$, total charge $+1$).
- In the **Neutron**, the counter-rotating configuration of the stomata causes their individual local residues to cancel asymptotically at a distance ($\sum \text{Res} = 0 \implies n=0$), zeroing the global electric charge, although the internal structure remains highly tensioned by Cartan friction.

#### C. Connection to Cartan Torsion and Retrocausality

Physically, the presence of the factor $i$ in the denominator ($\frac{nh}{2\pi i}$) indicates that the rotation of the quantum phase is coupled to the antisymmetric part of the complex Kähler metric (the bivector $B_{\mu\nu}$) and to the Cartan torsion.

Sudarshan's closed circuit establishes that time operates bidirectionally (retrocausally) at the soliton scale. If the integral surrounds the stoma and encounters a fractional residue ($\frac{nh}{2\pi i} + \epsilon$), the phase undergoes a mismatch at each temporal cycle. The retrocausality circuit mathematically amplifies this infinite mismatch through a destructive geometric sum, triggering the Perelman flow to dissipate the density ($\rho \to 0$), dissolving any anomalous geometry.

### Summary of what we extracted:

The value $\frac{nh}{2\pi i}$ is the **seal of guarantee of matter stability**. It proves that stomata are not merely "particles", but rather the geometric axes around which the spacetime fabric twists in a perfectly quantized manner. If the residue deviated even by a millionth from this value, the destructive interference of the quantum vacuum would instantaneously dissolve the hadron.

#### Step 4: Mathematical Deduction of Geometric Frustration

Let us suppose that the spacetime metric attempts to tension the quantum fluid to assume an energy-momentum configuration where the circulation integral fails to reach an integer eigenvalue. We introduce a non-integer phase perturbation $\epsilon$ (where $0 < |\epsilon| < 1$):
$$\oint_\gamma \nabla_\mu S_C dx^\mu = (n + \epsilon)h$$

We evaluate the effect of this perturbation on the wave function $\Psi$ upon completing a closed circuit of spatial or temporal translation. The transport operator along the loop acts as:

$$\Psi_{\text{final}} = \Psi_{\text{inicial}} \exp\left( \frac{i}{\hbar} \oint_\gamma \nabla_\mu S_C dx^\mu \right)$$

Substituting the perturbed integral value:

$$\Psi_{\text{final}} = \Psi_{\text{inicial}} \exp\left( \frac{i}{\hbar} (n + \epsilon) 2\pi\hbar \right) = \Psi_{\text{inicial}} e^{2\pi i n} e^{2\pi i \epsilon}$$

Since $n \in \mathbb{Z}$, the factor $e^{2\pi i n} = 1$. Therefore, the wave function undergoes a phase mismatch and does not return to its original value:

$$\Psi_{\text{final}} = \Psi_{\text{inicial}} e^{2\pi i \epsilon}$$

In the QGD model, the Sudarshan circuit establishes a regime of continuous retrocausality, where the field interacts with itself across multiple cycles of temporal feedback. The total amplitude after $m$ circulations is given by the geometric sum of the overlapping amplitudes:

$$\Psi_{\text{total}} = \sum_{m=0}^{\infty} \left( e^{2\pi i \epsilon} \right)^m \Psi_0$$

For $\epsilon \neq 0$, the sum of rotated phase vectors generates catastrophic macroscopic destructive interference. The crests and troughs of the phase density enter in direct opposition at each retrocausality cycle, nullifying the soliton's wave support.

#### Step 5: Dissolution Dynamics by the Perelman Flow ($\rho \to 0$)

The geometric stress generated by the failure of phase closure generates a symmetry breaking in the fluid's energy-momentum tensor, injecting a non-zero imaginary shear component into the metric's temporal evolution. The Ricci/Perelman Flow equation coupled to hydrodynamics reacts to this mismatch by modifying the continuity equation of the Madelung density $\rho$:

$$\frac{\partial \rho}{\partial t} = \mathcal{D} \nabla^2 \rho - \alpha(\epsilon)\rho$$

Where $\mathcal{D}$ is the vacuum's diffusion coefficient and $\alpha(\epsilon)$ represents the immediate damping factor extracted directly from the destructive interference component of the Sudarshan circuit, satisfying the conditions:

$$\begin{cases} \alpha(\epsilon) = 0, & \text{se } \epsilon = 0 \\ \alpha(\epsilon) > 0, & \text{se } \epsilon \neq 0 \end{cases}$$

When solving the evolutionary differential equation for a frustrated state ($\epsilon \neq 0$), the damping term dominates the asymptotic exponential dynamics:

$$\rho(t, x) = \rho_0(x) e^{-\alpha(\epsilon) t}$$

Applying the continuous time limit over the temporal loop's quantum relaxation scale:

$$\lim_{t \to \infty} \rho(t, x) = 0$$

This deductive result mathematically proves that any energy or torsion fluctuation that violates the homological barrier of the Residue Theorem instantaneously activates the Perelman Flow as a dissipative filter. The Madelung density collapses to zero, dissolving the soliton structure into the vacuum's background stochastic noise and guaranteeing that only perfectly quantized geometries ($n \in \mathbb{Z}$) survive as stable matter.
