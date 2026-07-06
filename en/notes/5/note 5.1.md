## Conformal Symmetry

## 1. Conformal Symmetry in Classical Physics

A **conformal symmetry** is an extension of scale symmetry (or dilation). A theory is conformally invariant if its equations remain unchanged when we apply a **conformal transformation** — that is, a transformation that preserves angles between vectors, but not necessarily distances. This includes:
- **Dilations** (zoom): multiplying all coordinates by a factor $\lambda$
- **Special conformal transformations** (analogous to boosts, but for scale)

In Maxwell's electromagnetism in a vacuum, the only constants are the speed of light $c$ and the electric permittivity $\varepsilon_0$. There is no characteristic length (such as an atomic radius, Planck length, etc.) embedded in the theory. If you "zoom in" on a Maxwell solution — say, multiply all distances by 2 and times by 2 — you get another valid solution. The theory **does not distinguish** between 1 meter and 1 nanometer.

## 2. What happens in Quantization?

When we quantize electromagnetism, we introduce quantum fields that can fluctuate in the vacuum. These fluctuations occur at **all energy/momentum scales** simultaneously.

Here arises the problem: in a quantum field theory, the interaction between the field and these vacuum fluctuations produces **divergences** (infinities) when we calculate physical quantities such as vacuum energy or the effective charge of a particle.

To deal with these infinities, we need a process called **regularization and renormalization**. And this requires introducing a **cutoff** (maximum energy limit) or, equivalently, a **minimum length scale** — something that pure classical theory did not possess.

## 3. The Conformal Anomaly (Trace Anomaly)

Now comes the crucial point: the need to introduce a mass (or energy) scale in the quantum theory **explicitly breaks the scale symmetry** that existed classically.
This breaking is called the **conformal anomaly** or **trace anomaly**.
In conformal classical theory, the **energy-momentum tensor** $T^{\mu\nu}$ satisfies a special condition: its **trace** (sum of diagonal elements) is zero:
$$T^\mu_\mu = 0 \quad \text{(classical)}.$$
This is a direct consequence of conformal invariance. Physically, it means that the theory has no "scale" — there is no trace pressure to define a characteristic length.
In renormalized quantum theory, however, this condition is violated:
$$T^\mu_\mu \neq 0 \quad \text{(quantum)}.$$
The trace of the energy-momentum tensor becomes proportional to the **beta function** $\beta(g)$ of the theory, which describes how the coupling constant $g$ varies with the energy scale:
$$T^\mu_\mu \propto \beta(g).$$
## 4. The Beta Function and Physical Meaning

The **beta function** $\beta(g)$ is the heart of the **renormalization group equation**. It tells us how the interaction "strength" (the effective charge) changes when we change the energy scale at which we observe the theory.

- If $\beta(g) = 0$, the theory is **scale-free** (scale-invariant) — the charge does not change with energy.
- If $\beta(g) \neq 0$, the effective charge **depends on the energy scale**, which means the theory "feels" the scale.

Therefore, the relation $T^\mu_\mu \propto \beta(g)$ tells us that:

**The trace of the energy-momentum tensor measures exactly how much the quantum theory "knows" about the energy scale** — that is, how much the classical conformal symmetry was broken by quantization.

## 5. Simple Analogy

Imagine a photograph of a fractal (like the Mandelbrot set). Classically, the fractal **looks the same** at any zoom — there is no preferred scale. That is conformal symmetry.

Now imagine that, when trying to print this photo digitally, your printer can only work with a **minimum pixel resolution** (the cutoff). Suddenly, the fractal is no longer perfectly self-similar: when you zoom in enough, you see the pixels. The "imperfection" introduced by the finite resolution is the conformal anomaly — the minimum scale (mass/energy of the cutoff) broke the perfect scale invariance.
