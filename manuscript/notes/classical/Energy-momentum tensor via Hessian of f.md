---
title: "Energy-momentum tensor via Hessian of f"
---

# Energy-momentum tensor via Hessian of $f$

## Statement

In the macroscopic limit, the effective metric response of GDQ can be organized as an energy-momentum tensor obtained from the variation of the $f$ sector with respect to the metric. This tensor is a reduction, not a new postulate.

## Starting point

Consider the internal sector of the integrand:

$$
\mathcal L_f
=
\tau\,g^{\mu\bar\nu}
\partial_\mu f\,\partial_{\bar\nu}\bar f
\mathcal V(f,\bar f,g),
$$

where $\mathcal V$ includes the weighted terms that do not depend explicitly on derivatives of $f$ in the step under consideration.

The effective material contribution is defined by metric variation:

$$
T_{AB}^{(f)}
=
-\frac{2}{\sqrt g}
\frac{\delta}{\delta g^{AB}}
\int_M
\mathcal L_f\,\mathcal U\sqrt g\,dV.
$$

## Principal variation

Using:

$$
\delta\sqrt g
=
-\frac12\sqrt g\,g_{AB}\delta g^{AB},
$$

and separating the explicit dependence on $g^{AB}$ in the kinetic term, one obtains the structure:

$$
T_{AB}^{(f)}
=
2\tau\,{\rm Re}
\left(
\partial_A f\,\partial_B\bar f
\right)\mathcal U
-g_{AB}\mathcal L_f\mathcal U
+T_{AB}^{(\mathcal U)}.
$$

The term $T_{AB}^{(\mathcal U)}$ appears because $\mathcal U$ depends on $\rho$, and $\rho$ depends on the real part of $f$. When the metric is varied while keeping $f$ fixed, this term may reduce; when the physical variation transports $f$, it must be kept.

## Classical projection

In the Madelung sector:

$$
f
=
-\ln\rho
+\frac{i}{\hbar}S_R,
$$

phase gradients dominate when $\varepsilon_{\rm cl}\ll1$. Then the principal part of the tensor assumes the flow form:

$$
T_{AB}^{\rm cl}
\sim
\rho\,\partial_A S_R\,\partial_B S_R
+\text{geometric pressure terms}.
$$

The geometric pressure terms are those that generate Bohm corrections, torsion tensions, and boundary responses. When they are small or isotropized, the classical effective matter tensor remains.

## Scope

This construction shows how the energy-momentum tensor can emerge from the Hessian and from the metric variation of the $f$ sector. It does not replace the proof of a complete Einstein equation in every background: for this, it is necessary to transport the global--local bridge, fix boundaries, and control gauge modes.
