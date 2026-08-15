---
title: "Operational checklist — Chapter 1"
---

# Operational checklist — Chapter 1

This checklist follows the methodological protocol of Chapter 27, without reopening the theory and without anticipating results of subsequent chapters.

## 1. Goal of the chapter

Chapter 1 must fulfill a foundational and pedagogical function:

1. show mathematical effectiveness as a methodological problem;
2. separate the Wiener integral and the Feynman integral;
3. explain why Wick is a conditional continuation, not an automatic physical identity;
4. show that boundary terms and gauge matter;
5. introduce Madelung as a decomposition of density and phase;
6. introduce Nelson as a treatment of non-differentiable paths;
7. motivate the transition to weighted geometry without yet declaring the complete GDQ as demonstrated.

Chapter status: **foundational and pedagogical**.

It should not prove by itself:

- the official action;
- the Lorentzian reconstruction;
- the Born rule;
- the physical Hilbert space;
- the global–local bridge;
- the complete origin of masses;
- the variational emergence of all stochastic coefficients.

## 2. Status of the main body

| Section | Status | Observation |
|---|---|---|
| `01.1` | ready in first version | Introduces Wigner and the methodological motivation. |
| `01.2` | ready in first version | Defines vocabulary and avoids confusion between GDQ, reductions, and historical terms. |
| `01.3` | ready in first version | Correctly separates Wiener and Feynman. |
| `01.4` | ready in first version | Treats Wick by spectrum, domain, and contour. |
| `01.5` | ready in first version | Explains total derivatives, gauge, and boundary. |
| `01.6` | ready in first version | Derives Madelung as a decomposition, not as final ontology. |
| `01.7` | ready in first version | Introduces Nelson and non-differentiable paths with caution. |
| `01.8` | ready conditionally | Universal diffusion is presented as a hypothesis/conditional bridge. |
| `01.9` | ready in first version | Motivates geometry and Perelman as an auxiliary arena, not as the official action. |

## 3. Called notes and logical function

| Note | Called by | Status |
|---|---|---|
| `[[../notes/analysis/Measures and integrals in path spaces\|Measures and integrals in path spaces]]` | `01.3` | Pedagogical note. |
| `[[../notes/derivations/Spectral continuation from unitary group to semigroup\|Spectral continuation from unitary group to semigroup]]` | `01.4` | Mathematical derivation. |
| `[[../notes/analysis/Elliptic, parabolic, hyperbolic and dispersive equations\|Elliptic, parabolic, hyperbolic and dispersive equations]]` | `01.4`, `01.9` | Pedagogical/analytical note. |
| `[[../notes/derivations/Total derivative, boundary and Euclidean continuation\|Total derivative, boundary and Euclidean continuation]]` | `01.5` | Derivation. |
| `[[../notes/derivations/Madelung decomposition step by step\|Madelung decomposition step by step]]` | `01.6` | Derivation. |
| `[[../notes/derivations/Nelson derivatives and continuity equation\|Nelson derivatives and continuity equation]]` | `01.7` | Stochastic derivation. |
| `[[../notes/derivations/Identity between osmotic velocity and quantum potential\|Identity between osmotic velocity and quantum potential]]` | `01.7` | Local derivation. |
| `[[../notes/derivations/Universal diffusion and geometric inertia - conditional analysis\|Universal diffusion and geometric inertia - conditional analysis]]` | `01.8` | Theorem/conditional bridge. |
| `[[../notes/derivations/Nelson variable diffusion in GDQ\|Nelson variable diffusion in GDQ]]` | `01.8` | Derivation in stochastic reduction. |
| `[[../notes/derivations/NESS, geometric flow and effective irreversibility\|NESS, geometric flow and effective irreversibility]]` | `01.9` | Conditioned conceptual note. |

Assessment: the main calls exist. The chapter is already suitable for the "didactic body + proof in note" format.

## 4. Preserved legacy material

Main legacy source:

the corresponding legacy chapter

Preserved blocks in the new chapter:

1. Wiener/Feynman contrast;
2. Wick rotation;
3. total derivative and boundary;
4. Madelung;
5. Nelson;
6. velocity decomposition;
7. universal diffusion;
8. geometric motivation via flow.

Status corrections compared to the legacy:

1. equivalence by Wick was downgraded to a conditional continuation;
2. the boundary term is not treated as an automatic breaking of invariance, but as a joint transformation datum of kernel, states, and observables;
3. universal diffusion is not declared as closed by the official action in this chapter;
4. Perelman is presented as an auxiliary geometric matrix/motivation, not as the fundamental physical action of GDQ.

## 5. Necessary references

Files already present in `manuscript/ref/`:

- `Wigner 1960 - The Unreasonable Effectiveness of Mathematics.md`;
- `Wiener 1923 - Differential-Space.md`;
- `Feynman 1948 - Space-Time Approach to Non-Relativistic Quantum Mechanics.md`;
- `Kac 1949 - On Distributions of Certain Wiener Functionals.md`;
- `Wick 1954 - Properties of Bethe-Salpeter Wave Functions.md`;
- `Osterwalder and Schrader 1973 - Axioms for Euclidean Green Functions.md`;
- `Madelung 1927 - Quantentheorie in hydrodynamischer Form.md`;
- `Nelson 1966 - Derivation of the Schrodinger Equation from Newtonian Mechanics.md`;
- `Nelson 1967 - Dynamical Theories of Brownian Motion.md`;
- `Hamilton 1982 - Three-manifolds with positive Ricci curvature.md`;
- `Perelman 2002 - The Entropy Formula for the Ricci Flow.md`.

Editorial pending: when the complete OCR is available for all references, review cited pages and keep only short files in the public text.

## 6. Numerical and symbolic scripts

Mandatory scripts for scientific closure of Chapter 1: **none**.

Reason: the chapter is conceptual and foundational. It does not make metrological predictions. The central calculations are analytical and are already in notes.

Scripts preserved in this version:

1. `scripts/comparar_kernel_wiener_feynman.py`  
   Illustrates the difference between positive Gaussian weight and oscillatory phase.

2. `scripts/verificar_termo_osmotico_bohm.py`  
   Verifies the identity between osmotic energy, osmotic divergence, and Bohm term in the regular sector.

3. `scripts/verificar_difusao_variavel_ito.py`  
   Verifies the Itô expansion for variable diffusion $D=\nu_0\Omega^{-1}$, the equivalence between conservative and expanded Fokker–Planck, and the osmotic velocity with the term $-\nu\nabla\ln\Omega$.

Classification: **pedagogical consistency verification**, not physical prediction and not independent proof of GDQ.

Possible future script, if useful pedagogically: a finite Hermitian matrix showing the formal transition from unitary group to damped semigroup. This script is not necessary for the closure of the chapter because the analytical derivation is already in the spectral note.

## 7. Pedagogical points to review in the final reading

Before considering Chapter 1 editorially ready:

1. verify if the text flows as a chapter, not as a presentation of topics;
2. maintain the transition sentences between `01.5`, `01.6`, `01.7`, `01.8`, and `01.9`;
3. maintain the distinction between "geometric motivation" and "derivation of the official action";
4. ensure that section `01.8` does not sound like a complete closure of mass or universal diffusion;
5. review if the analogies with fluid, fabric, and mesh remain subordinate to the definitions;
6. check Quartz rendering;
7. check Obsidian links.

## 8. Operational verdict

Chapter 1 is **structurally assembled and preserves the essential content of the legacy**.

What is still missing is editorial, not conceptual:

1. human review of fine fluidity;
2. final checking of reference pages when OCRs are stabilized;
3. final check of links and rendering in Quartz.

Therefore, the chapter can be used as a basis for the final rewriting, provided the called notes remain associated with the text.
