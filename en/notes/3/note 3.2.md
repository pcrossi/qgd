### Contour Closure

To demonstrate this mechanism analytically and deductively, one analyzes the behavior of gauge transformations at the temporal boundaries and how the extension to the complex plane handles the limitations associated with the traditional Wick Rotation.

**1: Gauge Invariance and the Boundary Term in Real Time (Minkowski):** In classical and quantum mechanics, the principle of gauge invariance establishes that two Lagrangians describe the same physics if they differ by a total time derivative of a scalar function $F(x, t)$:
$$L' = L + \frac{dF(x, t)}{dt}$$
By integrating this Lagrangian to obtain the Action ($S = \int L \, dt$), the total derivative projects directly onto the temporal boundaries of the system ($t_0$ and $t_1$), resulting in a boundary term:
$$\Delta S = \int_{t_0}^{t_1} \frac{dF}{dt} \, dt = F(x(t_1), t_1) - F(x(t_0), t_0) = \Delta F$$
In the Feynman Path Integral (in Minkowski spacetime), the probability amplitude is governed by the complex oscillatory weight $e^{\frac{i}{\hbar}S}$. The gauge transformation introduces an imaginary phase:
$$e^{\frac{i}{\hbar} S'} = e^{\frac{i}{\hbar} S} \cdot e^{\frac{i}{\hbar} \Delta F}$$
Since the modulus of a complex phase is unitary ($|e^{i\theta}| = 1$), the probability density ($P \propto |\psi|^2$) remains unaltered.

**2: Analysis of the Wick Rotation in the Euclidean Domain:** To transition to the domain of statistical mechanics and diffusion (Wiener Integral), the classical formulation applies the Wick Rotation ($t = -i\tau$). Under this analytic continuation, the total derivative modifies as follows:
$$\frac{dF}{dt} = \frac{dF}{-i d\tau} = i \frac{dF}{d\tau}$$
When integrated in imaginary time $\tau$, the term that was previously an oscillatory phase now acts in the real domain:
$$e^{-\frac{1}{\hbar} S_E'} = e^{-\frac{1}{\hbar} S_E} \cdot e^{-\frac{1}{\hbar} \Delta F}$$
The boundary factor then behaves as a real exponential modulator. If $F$ assumes arbitrary values at the temporal boundaries, the system may present divergences in the probability measure. To avoid such behaviors, it is customary to impose the condition that the fields vanish at infinity ($\psi(\pm\infty) = 0$), a restriction that can limit the modeling of systems with dynamic topological boundaries.

**3: The Holomorphic Structure of Sudarshan's Symmetric Propagator:** In QGD, it is proposed to extend the evolution to the complex time plane through a symmetric propagator that couples the advanced and retarded components:
$$G_{\text{sym}}(x, t) = \frac{1}{2} \left[ G_{\text{ret}}(x, t) + G_{\text{adv}}(x, t) \right]$$
By adopting this formalism in the Kähler manifold, the time integration is promoted to a closed contour integral $\gamma$ in the complex plane.

**4: Topological Vanishing by Cauchy's Theorem:** The coupling between the advanced and retarded components can be justified using complex analysis theorems. Let the gauge transformation function $F(z)$ be analytic and holomorphic in the domain enclosing the soliton's geometric basin. The integral of the gauge 1-form over a closed contour obeys Cauchy's Theorem:
$$\oint_{\gamma} dF \equiv 0$$
This identity indicates that the total variation at the temporal boundaries along the closed circuit is zero. Consequently, the boundary accumulation from the retarded potential (directed to the future) and the advanced potential (backpropagated from the past) mutually cancel each other out:
$$\Delta F_{\text{ret}} + \Delta F_{\text{adv}} = 0 \implies \Delta F_{\text{adv}} = - \Delta F_{\text{ret}}$$

**5: The Cancellation Mechanism:** Due to the topological condition imposed by the closed contour ($\oint dF = 0$), the transition amplitude associated with the product of the advanced and retarded components incorporates the respective corrections:
- The retarded contribution generates the factor: $e^{-\frac{\Delta F}{\hbar}}$,
- The advanced contribution carries the constraint: $e^{+\frac{\Delta F}{\hbar}}$.

Multiplying the two components:
$$e^{-\frac{\Delta F}{\hbar}} \cdot e^{+\frac{\Delta F}{\hbar}} = e^0 = \mathbf{1}$$

The boundary term, which in the common Wiener Integral would induce divergences, is compensated in the closed integration circuit. This reduces the need to impose the vanishing of the fields at the extremities of the physical domain ($\psi(\pm\infty) = 0$), contributing to the regularization of the vacuum in the complex domain.
