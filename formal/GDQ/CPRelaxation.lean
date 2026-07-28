import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Tactic

namespace GDQ

/-!
# Relaxação CP no modo torsional reduzido

Formaliza o potencial periódico, seu fluxo gradiente e a identidade de
Lyapunov. A convergência global módulo `2π` requer ainda o teorema dinâmico de
invariância/compacidade usado na prova humana.
-/

/-- Potencial periódico reduzido. -/
noncomputable def cpPotential (chi theta : ℝ) : ℝ :=
  chi * (1 - Real.cos theta)

/-- Gradiente do potencial reduzido. -/
noncomputable def cpGradient (chi theta : ℝ) : ℝ :=
  chi * Real.sin theta

/-- Campo vetorial do fluxo gradiente CP. -/
noncomputable def cpFlow (kappa chi theta : ℝ) : ℝ :=
  -kappa * cpGradient chi theta

/-- Derivada exata do potencial. -/
theorem cpPotential_hasDerivAt (chi theta : ℝ) :
    HasDerivAt (cpPotential chi) (cpGradient chi theta) theta := by
  change HasDerivAt
    (fun x : ℝ => chi * (1 - Real.cos x)) (chi * Real.sin theta) theta
  simpa only [Pi.sub_apply, zero_sub, neg_neg] using
    (((hasDerivAt_const (x := theta) (1 : ℝ)).sub
      (Real.hasDerivAt_cos theta)).const_mul chi)

/-- Identidade pontual de Lyapunov ao longo do fluxo. -/
theorem cp_lyapunov_identity (kappa chi theta : ℝ) :
    cpGradient chi theta * cpFlow kappa chi theta =
      -kappa * (cpGradient chi theta) ^ 2 := by
  unfold cpFlow
  ring

/-- Para mobilidade positiva, a derivada de Lyapunov é não positiva. -/
theorem cp_lyapunov_nonpos
    {kappa chi theta : ℝ} (hkappa : 0 ≤ kappa) :
    cpGradient chi theta * cpFlow kappa chi theta ≤ 0 := by
  rw [cp_lyapunov_identity]
  nlinarith [sq_nonneg (cpGradient chi theta)]

/-- `theta=0` é ponto crítico com potencial mínimo nulo. -/
theorem cp_zero_critical_minimum {chi : ℝ} (hchi : 0 ≤ chi) :
    cpGradient chi 0 = 0 ∧ cpPotential chi 0 = 0 ∧
      ∀ theta, 0 ≤ cpPotential chi theta := by
  constructor
  · simp [cpGradient]
  constructor
  · simp [cpPotential]
  · intro theta
    unfold cpPotential
    have hcos : Real.cos theta ≤ 1 := Real.cos_le_one theta
    positivity

/-- `theta=π` é crítico e tem curvatura negativa para `chi>0`. -/
theorem cp_pi_critical_unstable {chi : ℝ} (hchi : 0 < chi) :
    cpGradient chi Real.pi = 0 ∧
      chi * Real.cos Real.pi < 0 := by
  constructor
  · simp [cpGradient]
  · simp
    exact hchi

end GDQ
