### Definition of $\mathcal{F}_t$ (Filtration)

In the stochastic formalism of Nelson/Itô employed here, the term $\mathcal{F}_t$ is fundamental to the definition of the **filtration**.

$\mathcal{F}_t$ is the **$\sigma$-algebra of complete information** of the system up to time $t$. In practical terms:
- **Complete History:** $\mathcal{F}_t$ represents the entire "past" and "present" of the stochastic soliton's trajectory up to time $t$.
- **The Fluid's "Memory":** It contains all the necessary information for us to determine the state of the system, including the Wiener fluctuations that have occurred up to that point.
- **Causal Filter:** The vertical bar in $\mathbb{E}[\dots | \mathcal{F}_t]$ indicates a **Conditional Expectation**. It tells us that the expected value of the velocity must be calculated *given that we know* everything that has happened in the system up to time $t$.

In classical Newtonian mechanics, the position $x(t)$ and velocity $v(t)$ are sufficient to determine the future. In stochastic mechanics, the trajectory is fractal (Hausdorff dimension equal to 2, $dx \sim \sqrt{dt}$) and is not differentiable in the classical sense. By conditioning on $\mathcal{F}_t$, we are filtering the fractal Wiener noise, which possesses an infinite "roughness", allowing us to extract a regular and well-behaved average velocity. Without the conditioning on $\mathcal{F}_t$, the derivative $\frac{dx}{dt}$ would diverge. With it, the stochastic calculus (Itô/Nelson) stabilizes the average behavior, allowing us to define the current velocity ($\mathbf{v}$) and the osmotic velocity ($\mathbf{u}$).

The use of the $\sigma$-algebra $\mathcal{F}_t$ is what allows the transition from real time to complex time: For the forward derivative ($D_+$), $\mathcal{F}_t$ "looks" into the past; For the backward derivative ($D_-$), we are actually utilizing a filtration that incorporates information from a symmetric propagator, which is essential for preserving the Sudarshan **advanced/retarded causality**.

In summary, $\mathcal{F}_t$ is the foundation of the causal knowledge of the system. Without it, we would lack the formal basis to state that the fluid has a defined velocity, and our formalism would collapse into pure noise with no geometric structure.
