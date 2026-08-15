---
title: "Proofs, lemmas and definitions — Chapter 11"
---

# Proofs, lemmas and definitions — Chapter 11

This note preserves the technical construction of Stern--Gerlach in GDQ. The experiment is treated as an interaction between:

1. a soliton that already possesses circulation/spin;
2. a classical magnetic field produced by the apparatus;
3. an interface that selects axis, channels, and response;
4. a screen that registers two separated beams.

The official action is not modified. The apparatus provides the classical source/boundary.

## 1. Physical Statement

Stern--Gerlach requires explaining:

1. why two channels appear;
2. why the axis is that of the apparatus;
3. why the population of the channels depends on the preparation angle;
4. why each channel undergoes mechanical deflection;
5. why sequential measurements along different axes do not reveal a pre-existing table of values.

The GDQ chain is:

$$
J_{\rm SG}^{\rm classical}
\to
\Phi_*^{\rm SG}
\to
K_{\rm GDQ}
\to
P_{\rm phys}^{\dagger}K_{\rm GDQ}P_{\rm phys}
\to
\mathsf R_{\rm SG}
\to
P_{\mathbf n}^{\pm}
\to
\Delta z_\pm
\to
\text{register}.
$$

## 2. Spin Before Measurement

Spin is not created by the apparatus. The object already possesses an internal circulation/Hopf modulus. In the reduced spinorial sector, the orientation is represented by a unit vector $\mathbf a$ and by the density matrix:

$$
\varrho_{\mathbf a}
=
\frac12(I+\mathbf a\cdot\sigma).
$$

The role of the apparatus is to select a direction $\mathbf n$, not to manufacture spin.

## 3. Classical Magnetic Source

The field of the apparatus is an external given:

$$
\mathbf n(\mathbf x)
=
\frac{\mathbf B(\mathbf x)}{|\mathbf B(\mathbf x)|}.
$$

In the regime of approximately uniform gradient,

$$
B_z(z)
\simeq
B_0+z\,\partial_zB_z.
$$

This datum enters as a classical source/boundary:

$$
K_{\rm phys}^{\rm obj}\,\delta\Phi_{\rm SG}
=
J_{\rm SG}^{\rm classical}.
$$

Here $K_{\rm phys}^{\rm obj}$ is the projected physical Hessian of the object. The response $\delta\Phi_{\rm SG}$ is calculated; it is not inserted as a manual quantum operator.

## 4. Hopf/Clifford Projectors

The axis $\mathbf n$ defines two projectors:

$$
P_{\mathbf n}^{\pm}
=
\frac12(I\pm\mathbf n\cdot\sigma).
$$

They satisfy:

$$
(P_{\mathbf n}^{\pm})^2=P_{\mathbf n}^{\pm},
\qquad
P_{\mathbf n}^{+}P_{\mathbf n}^{-}=0,
\qquad
P_{\mathbf n}^{+}+P_{\mathbf n}^{-}=I.
$$

The geometric reason is that the Hopf link of the normal slice possesses two stable eigen-sectors when the apparatus breaks isotropy via a uniaxial axis. In reduced language, these sectors are the eigen-projectors of $\mathbf n\cdot\sigma$.

The script `scripts/verify_sg_hopf_atlas.py` verifies the gluing of charts, the projector, and the Fubini--Study metric in the reduced Hopf model.

## 5. Angular Weights

With preparation $\mathbf a$ and the apparatus along axis $\mathbf n$, operational Born from Chapter 9 yields:

$$
p_\pm(\mathbf n|\mathbf a)
=
\operatorname{Tr}(\varrho_{\mathbf a}P_{\mathbf n}^{\pm}).
$$

Substituting,

$$
p_\pm
=
\operatorname{Tr}
\left[
\frac12(I+\mathbf a\cdot\sigma)
\frac12(I\pm\mathbf n\cdot\sigma)
\right].
$$

Using:

$$
\operatorname{Tr}(\sigma_i)=0,
\qquad
\operatorname{Tr}(\sigma_i\sigma_j)=2\delta_{ij},
$$

we obtain:

$$
p_\pm(\mathbf n|\mathbf a)
=
\frac{1\pm\mathbf a\cdot\mathbf n}{2}.
$$

If $\theta$ is the angle between $\mathbf a$ and $\mathbf n$,

$$
p_+=\cos^2\frac{\theta}{2},
\qquad
p_-=\sin^2\frac{\theta}{2}.
$$

The script `scripts/calculate_sg_weights.py` preserves this calculation and generates the angular weights table.

## 6. Force and Deflection in the Fixed Channel

In the fixed adiabatic channel, the reduced interface energy is:

$$
E_\pm(z)
=
\mp\mu B_z(z).
$$

The force is:

$$
F_z^\pm
=
-\partial_zE_\pm
=
\pm\mu\,\partial_zB_z.
$$

If the particle crosses a region of length $L$ with longitudinal velocity $v_y$, the interaction time is:

$$
t_{\rm int}=\frac{L}{v_y}.
$$

The deflection inside the field region is:

$$
\Delta z_\pm
=
\frac12\frac{F_z^\pm}{m}t_{\rm int}^2.
$$

Therefore:

$$
\Delta z_\pm
=
\pm
\frac{\mu L^2}{2mv_y^2}
\partial_zB_z.
$$

After the field region, an additional free segment adds displacement due to the acquired transverse velocity. The script `scripts/simulate_sg_deflection.py` implements the reduced version.

## 7. Sequential Measurements

If two apparatuses measure along axes $\mathbf n$ and $\mathbf m$, the projectors generally do not commute:

$$
[P_{\mathbf n}^{+},P_{\mathbf m}^{+}]
\ne0
\quad
\text{if}
\quad
\mathbf n\times\mathbf m\ne0.
$$

Therefore, a sequence $z\to x\to z$ does not measure the same decomposition twice. The intermediate apparatus redefines the stable decomposition. For orthogonal axes, after selecting $z+$ and measuring $x$, a new measurement of $z$ once again yields:

$$
p(z+)=p(z-)=\frac12.
$$

The scripts `scripts/test_sg_sequences.py` and `scripts/simulate_sg_sequences.py` verify this operational behavior.

## 8. Adiabatic Condition

The proof of two clean channels assumes that the effective axis changes slowly on the scale of the gap between channels. In reduced form,

$$
\frac{|\langle -|\dot H|+\rangle|}
{\Delta E^2}
\ll1.
$$

If this condition fails, non-adiabatic transitions appear. The population ceases to be a simple QND martingale and the complete interface dynamics must be resolved. This delimits the scope of the proof, rather than contradicting it.

The script `scripts/simulate_nonadiabatic_sg.py` preserves this limit via a reduced Landau--Zener test.

## 9. Magnetic Apparatus as Schur/DtN

For fine metrology, the impedance of the apparatus is:

$$
\mathsf R_{\rm SG}
=
K_{YY}-K_{YI}K_{II}^{-1}K_{IY}.
$$

Block $Y$ represents the measured interface; block $I$ represents unmonitored internal degrees of freedom. The form is equivalent to a Dirichlet-to-Neumann operator: given the trace on the interface, the interior is solved and the conjugate normal momentum is returned.

This expression defines how to calculate $\kappa_H^{\rm SG}$, $\Gamma_{\rm SG}$, and losses of a real apparatus. Without real geometry/material/field profile, there is no universal metrological number.

## 10. Preserved Numerical Results

The scripts of the chapter are classified into three groups:

| Group | Examples | Use |
|---|---|---|
| Structural identities | `calculate_sg_weights.py`, `verify_sg_hopf_atlas.py`, `test_sg_sequences.py` | Preserve projectors, weights, and composition. |
| Apparatus reductions | `simulate_sg_deflection.py`, `simulate_complete_sg_beam.py`, `solve_sg_cylindrical_hopf_dtn.py` | Verify reduced formulas. |
| Diagnostics/limits | `simulate_nonadiabatic_sg.py`, `test_sg_gaussian_zh.py`, `test_sg_background_pipeline.py` | Delimit scope; are not the final physical prediction. |

Scripts marked as fixture, method test, or negative diagnostic must not be cited as metrological validation of GDQ.

## 11. Status

| Item | Status | Limit |
|---|---|---|
| Spin/circulation before measurement | Structurally closed | Comes from Chapter 10. |
| Apparatus axis | Closed | Is a classical source/boundary. |
| Two channels | Structurally closed | Hopf/Clifford projectors. |
| Angular weights | Operationally closed | Born from Chapter 9. |
| Deflection | Closed in the reduced channel | Uses given classical field. |
| Incompatible sequences | Operationally closed | Projectors do not commute. |
| Real $\mathsf R_{\rm SG}$ | Metrological program | Requires real apparatus/material. |
