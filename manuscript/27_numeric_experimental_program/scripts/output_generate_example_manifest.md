# Output — minimal GDQ script manifest

Classification: documentary tool.

| Field | Expected Content |
|---|---|
| Equation/functional | What part of S_GDQ or which reduction is being evaluated. |
| Background Phi_* | Solution, reduced ansatz, or declared fixture. |
| Domain | Interval, manifold, mesh, or spectral space. |
| Boundary | Dirichlet, Neumann, Robin, DtN/Schur, or external data. |
| Constraints | Charge, flux, normalization, gauge, phase, boundaries. |
| Operator/Hessian | K_phys, Jacobi, DtN, Schur, or reduced operator. |
| Physical projector | How gauge/coordinate modes are removed. |
| Source/apparatus | J_app or independent external parameter. |
| Observable | Quantity compared or diagnosed. |
| Universal parameters | Constants coming from the theory. |
| Apparatus parameters | Independent data from the experiment/material. |
| Numerical parameters | Mesh, tolerance, solver, seed. |
| Data usage | Whether the experimental target entered prior to comparison. |
| Classification | Evaluation, convergence, consistency, fit, comparison, or prediction. |

## Verdict

A script that cannot fill these fields is still exploratory.
