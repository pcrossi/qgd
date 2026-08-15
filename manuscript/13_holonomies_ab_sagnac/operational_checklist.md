---
title: "Operational checklist — Chapter 13"
---

# Operational checklist — Chapter 13

## 1. Statement

Explain AB, Sagnac and interferometric extensions as physical holonomies of distinct connections, preserving the GDQ reading without inventing a hidden local force.

## 2. Logical status

| Block | Status | Observation |
|---|---|---|
| Holonomy | Operational definition | Loop integral of a connection. |
| Ideal AB | Structurally closed | Punctured domain and flat connection. |
| Gauge invariance | Demonstrated | Closed loop holonomy. |
| Potential as connection | GDQ interpretation | Shear/effective gluing. |
| Real solenoid | Metrological program constructed | Corrections by physical Hessian, projector and $\mathsf R_{\rm sol}$. |
| Ideal Sagnac | Structurally closed | Clock holonomy. |
| COW | Reduced extension | Not the core of the chapter. |

## 3. Deductive chain

$$
\text{domain with cycle}
\to
\text{connection}
\to
\text{gluing}
\to
\oint\mathcal A
\to
\text{observable phase or time}.
$$

For a real apparatus, the GDQ chain used in the chapter is:

$$
J_{\rm app}^{\rm classical}
\to
\Phi_\ast
\to
K_{\rm GDQ}
\to
P_{\rm phys}^{\dagger}K_{\rm GDQ}P_{\rm phys}
\to
\mathsf R_{\rm app}
\to
\delta A_{\rm surf}
\to
\Delta\varphi.
$$

## 4. Scripts

| Script | Classification |
|---|---|
| `ab_symbolic_holonomy.py` | Symbolic consistency test of the ideal holonomy. |
| `ab_ideal_phase.py` | Direct evaluation of ideal holonomy. |
| `sagnac_light_matter.py` | Direct evaluation of ideal Sagnac. |
| `reduced_cow_estimation.py` | Reduced/interferometric estimation. |
| `verify_schur_projector.py` | Symbolic-numerical test of the physical projector and Schur complement. |

## 5. Key points to remember

- AB is not a local force where $B=0$.
- Sagnac is not electromagnetic AB.
- Real potential means real connection/holonomy.
- Real solenoid/fiber/apparatus is metrology.
- Casimir does not belong to the core of this chapter.
