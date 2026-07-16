---
title: Manuscript chapter 04 called notes
status: active
---

# Manuscript chapter 04 called notes

## Directly called notes

### `manuscrito/notes/action/Dimensão e normalização da ação oficial.md`

Used in sections 04.2 and 04.4.

Main content:

- introduces Cartan-normalized variables;
- confirms that `tau` and `z_tau` have area dimension;
- proves that curvature, weighted measure, volume and `d tau/tau` combine to
  give a dimensionless integrated functional;
- fixes `Lambda_C` as the dimensionless cutoff number in the official action;
- separates physical scales:
  - `ell_C`: length;
  - `k_C`: inverse length/momentum scale;
  - `E_C = hbar c k_C`: energy.

Status: resolved dimensional convention. It preserves the official action and
removes the earlier ambiguity.

### `manuscrito/notes/action/Primeira variação da ação GDQ - estrutura completa.md`

Called by section 04.5.

Main content:

- compact algebra of the first variation;
- product rule including `delta L_0`, `delta U` and `delta dV_g`;
- warning that the signs of `delta dV_g` depend on whether `g^{AB}` or
  `g_{AB}` is varied;
- weighted curvature variation:

$$
\mathcal U\left(
\mathcal R_{AB}-\frac12\mathcal Rg_{AB}
\right)
+g_{AB}\Delta_g\mathcal U
-\nabla_A\nabla_B\mathcal U;
$$

- normalization constraint and the same `lambda(tau)` entering density and
  metric equations;
- final form with bulk Euler-Lagrange coefficients plus boundary concomitant.

Status: compact derivational support for chapters 4 and 5. Full pedagogical
derivation is in chapter 5.

### `manuscrito/notes/action/Quociente físico, fantasmas e identidades de calibre.md`

Called by section 04.7.

Main content:

- defines the physical perturbation space as quotient:

$$
\mathcal V_{\rm phys}
=\ker C\cap\mathcal D_{\rm bordo}/\operatorname{Im}R;
$$

- explains Faddeev-Popov determinant as a coordinate Jacobian after choosing a
  section of the gauge orbit;
- states ghosts as optional Grassmann representation of the Jacobian, not
  GDQ matter;
- derives Ward in the abelian sector from spectral covariance and trace
  cyclicity;
- records Slavnov-Taylor as the non-abelian/background-gauge analogue of the
  quotient identity.

Status: closes the “ghosts are necessary” objection only in the declared
operator/domain sectors. It does not bypass construction of `P_phys`.

### `manuscrito/notes/action/Polarização heat-kernel e ausência do polo de Landau.md`

Called by section 04.7.

Main content:

- separates the direct GDQ loop of the phase mode on `R^4 x T^4` from the
  external U(1) comparison language;
- derives `H_n[A]` from the Hessian of the phase fluctuation on a toroidal
  cycle;
- includes the contact term required by Ward;
- computes the regularized polarization and its UV saturation;
- shows `Pi_tau(0)=0`;
- derives the no-pole condition:

$$
\frac{\alpha_0}{3\pi}E_1(\tau m^2)<1.
$$

Status: sectoral conditional result. It supports UV softening and absence of
Landau pole in the declared heat-kernel comparison sector, not universal GDQ
finiteness.

## Preservation map

`manuscrito/04_action_consistency/preservation_map.md` records the historical
corrections:

- “Kähler with torsion” corrected to Hermitian/KT;
- global Kähler potential not assumed in torsionful case;
- `U` corrected from indeterminate multiplier to constitutive functional;
- Perelman demoted from physical action to auxiliary geometric matrix;
- external propagators demoted to reduction/audit language;
- ghosts demoted to Jacobian representation;
- old Landau beta-function argument rejected in favor of heat-kernel
  polarization;
- old fermionic self-energy not treated as fundamental GDQ loop;
- `Lambda_C` separated from dimensional physical scales.
