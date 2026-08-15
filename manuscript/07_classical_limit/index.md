---
title: "07. The classical limit and the correspondence principle"
---

# 07. The classical limit and the correspondence principle

A theory of matter is not complete simply because it describes microscopic phenomena. It must also explain why macroscopic bodies can be treated via trajectories, why the Hamilton–Jacobi action reappears, and under what conditions interference ceases to dominate the observed motion.

The classical limit of QGD will not be presented as the formal replacement of $\hbar$ by zero. The constant $\hbar$ does not change when we go from an electron to a planet. What changes is a dimensionless ratio: the phase variation scale becomes much smaller than the scale of variation of the amplitude and of external fields. In this situation, the Bohm correction becomes small compared to the kinetic energy, and the classical Hamilton–Jacobi equation governs the phase.

The chapter starts from the Madelung sector identified in Chapters 5 and 6. This choice is important: the official action has a larger Cauchy space, and quantum hydrodynamic mechanics is a physical polarization of this space. Thus, the result demonstrated here is a correspondence theorem **within this sector**, not a statement that every off-shell solution of QGD is classical or quantum in the usual sense.

## Roadmap

- [[07.1 - What it means to take the classical limit]]
- [[07.2 - The starting Hamilton–Jacobi–Bohm system]]
- [[07.3 - The dimensionless parameter controlling the limit]]
- [[07.4 - From the quantum to the classical Hamilton–Jacobi equation]]
- [[07.5 - From phase fronts to Newton's trajectories]]
- [[07.6 - Continuity, ensemble, and the Liouville equation]]
- [[07.7 - WKB, stationary phase, and caustics]]
- [[07.8 - From the global cotangent potential to the Kepler potential]]
- [[07.9 - Noether and the constants of classical motion]]
- [[07.10 - Torsion, classical fields, and the scope of correspondence]]
- [[07.11 - Macroscopic electromagnetic correspondence]]
- [[07.12 - Metric correspondence and classical gravitation]]

## Central result

If $R=\sqrt\rho$ varies on a scale $L_\rho$, if the typical momentum is $p=|\nabla S_R|$, and if

$$
\varepsilon_{\rm cl}
=\frac{\hbar}{pL_\rho}
\ll1,
$$

then, in node-free regions and before the formation of caustics,

$$
\frac{|Q_B|}{T_{\rm cl}}
=O(\varepsilon_{\rm cl}^2),
$$

and the Hamilton–Jacobi–Bohm equation reduces to the classical Hamilton–Jacobi equation. Its characteristics satisfy Hamilton's equations and, for $H=p^2/(2m)+V$, Newton's second law.

The limit is controlled and has an explicit domain of validity. It does not require a reverse Wick rotation: the physical time has already been selected and transported by the causal reconstruction and by the global--local bridge.

After the scalar proof, the chapter also incorporates the vector and metric sectors. These transitions are not derived again from the Hamilton–Jacobi equation: they use the connections, symmetries, torsion, and metric response already constructed in previous chapters, detailing the hypotheses necessary to obtain Maxwell and Einstein as macroscopic correspondences.

## Editorial control

- [[operational_checklist|Operational checklist of the chapter]]
- [[notes/proofs_lemmas_definitions|Associated proofs, lemmas, and definitions]]
- [[scripts/README|Self-contained optional scripts]]

[[../index|← Home]] | [[07.1 - What it means to take the classical limit|Next →]]
