import GDQ.ActionDensity
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

namespace GDQ

open scoped BigOperators

/-!
# Primeira variação oficial no setor de fase

Este módulo formaliza a parte algébrica local da variação
`S_R ↦ S_R + ε η` depois da decomposição constitutiva
`f = -log ρ + i S_R / ℏ`.

A densidade, a métrica, o volume e o parâmetro de fluxo permanecem fixos.
Não se introduz uma ação diferente: `officialPhaseSectorDensity` é exatamente
a parcela quadrática em `∂S_R` da densidade oficial.
-/

variable {ι : Type*} [Fintype ι]

/-- Contração finita que representa `g^{μ barν} u_μ v_barν`. -/
def phaseGradientContraction
    (metricInv : ι → ι → ℝ) (u v : ι → ℝ) : ℝ :=
  ∑ i, ∑ j, metricInv i j * u i * v j

theorem phaseGradientContraction_add_left
    (metricInv : ι → ι → ℝ) (u v w : ι → ℝ) :
    phaseGradientContraction metricInv (u + v) w =
      phaseGradientContraction metricInv u w +
        phaseGradientContraction metricInv v w := by
  simp only [phaseGradientContraction, Pi.add_apply]
  simp only [mul_add, add_mul, Finset.sum_add_distrib]

theorem phaseGradientContraction_add_right
    (metricInv : ι → ι → ℝ) (u v w : ι → ℝ) :
    phaseGradientContraction metricInv u (v + w) =
      phaseGradientContraction metricInv u v +
        phaseGradientContraction metricInv u w := by
  simp only [phaseGradientContraction, Pi.add_apply]
  simp only [mul_add, Finset.sum_add_distrib]

theorem phaseGradientContraction_smul_left
    (metricInv : ι → ι → ℝ) (a : ℝ) (u v : ι → ℝ) :
    phaseGradientContraction metricInv (a • u) v =
      a * phaseGradientContraction metricInv u v := by
  simp only [phaseGradientContraction, Pi.smul_apply, smul_eq_mul]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i _
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j _
  ring

theorem phaseGradientContraction_smul_right
    (metricInv : ι → ι → ℝ) (a : ℝ) (u v : ι → ℝ) :
    phaseGradientContraction metricInv u (a • v) =
      a * phaseGradientContraction metricInv u v := by
  simp only [phaseGradientContraction, Pi.smul_apply, smul_eq_mul]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i _
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j _
  ring

/-- Simetria da contração na seção real para métrica inversa simétrica. -/
theorem phaseGradientContraction_comm
    (metricInv : ι → ι → ℝ)
    (hmetric : ∀ i j, metricInv i j = metricInv j i)
    (u v : ι → ℝ) :
    phaseGradientContraction metricInv u v =
      phaseGradientContraction metricInv v u := by
  unfold phaseGradientContraction
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro i _
  apply Finset.sum_congr rfl
  intro j _
  rw [hmetric j i]
  ring

/--
Parcela da densidade oficial que depende da fase real. O coeficiente é
literalmente `(ℏ / ΛC²) (τ / ℏ²) U sqrt(det g)`.
-/
noncomputable def officialPhaseSectorDensity
    (ℏ ΛC τ kernel volumeDensity : ℝ)
    (metricInv : ι → ι → ℝ) (phaseGradient : ι → ℝ) : ℝ :=
  (ℏ / ΛC ^ 2) * (τ / ℏ ^ 2) * kernel * volumeDensity *
    phaseGradientContraction metricInv phaseGradient phaseGradient

/--
Ligação literal com `officialPointDensity`: ao decompor a norma de `∇f` em
uma parcela independente da fase e
`g⁻¹(dS_R,dS_R)/ℏ²`, a diferença é exatamente o setor de fase acima.
-/
theorem officialPointDensity_phase_split
    (n : Nat)
    (ℏ ΛC τ scalarCurvature baseGradientNormSq realPotential kernel
      volumeDensity : ℝ)
    (metricInv : ι → ι → ℝ) (phaseGradient : ι → ℝ) :
    officialPointDensity n ℏ ΛC τ scalarCurvature
        (baseGradientNormSq +
          phaseGradientContraction metricInv phaseGradient phaseGradient /
            ℏ ^ 2)
        realPotential kernel volumeDensity =
      officialPointDensity n ℏ ΛC τ scalarCurvature baseGradientNormSq
          realPotential kernel volumeDensity +
        officialPhaseSectorDensity ℏ ΛC τ kernel volumeDensity metricInv
          phaseGradient := by
  unfold officialPointDensity officialBracket officialPhaseSectorDensity
  ring

/-- Primeira variação pontual exata antes da simetria da métrica. -/
noncomputable def officialPhaseFirstVariation
    (ℏ ΛC τ kernel volumeDensity : ℝ)
    (metricInv : ι → ι → ℝ)
    (phaseGradient testGradient : ι → ℝ) : ℝ :=
  (ℏ / ΛC ^ 2) * (τ / ℏ ^ 2) * kernel * volumeDensity *
    (phaseGradientContraction metricInv testGradient phaseGradient +
      phaseGradientContraction metricInv phaseGradient testGradient)

/-- Expansão exata da densidade perturbada, sem resto assintótico. -/
theorem officialPhaseSectorDensity_perturbation_exact
    (ℏ ΛC τ kernel volumeDensity ε : ℝ)
    (metricInv : ι → ι → ℝ)
    (phaseGradient testGradient : ι → ℝ) :
    officialPhaseSectorDensity ℏ ΛC τ kernel volumeDensity metricInv
        (phaseGradient + ε • testGradient) =
      officialPhaseSectorDensity ℏ ΛC τ kernel volumeDensity metricInv
          phaseGradient +
        ε * officialPhaseFirstVariation ℏ ΛC τ kernel volumeDensity
          metricInv phaseGradient testGradient +
        ε ^ 2 *
          officialPhaseSectorDensity ℏ ΛC τ kernel volumeDensity metricInv
            testGradient := by
  simp only [officialPhaseSectorDensity, officialPhaseFirstVariation,
    phaseGradientContraction_add_left,
    phaseGradientContraction_add_right,
    phaseGradientContraction_smul_left,
    phaseGradientContraction_smul_right]
  ring

/-- Os termos conjugados somam duas cópias na seção real simétrica. -/
theorem officialPhaseFirstVariation_eq_twice
    (ℏ ΛC τ kernel volumeDensity : ℝ)
    (metricInv : ι → ι → ℝ)
    (hmetric : ∀ i j, metricInv i j = metricInv j i)
    (phaseGradient testGradient : ι → ℝ) :
    officialPhaseFirstVariation ℏ ΛC τ kernel volumeDensity metricInv
        phaseGradient testGradient =
      2 * (ℏ / ΛC ^ 2) * (τ / ℏ ^ 2) * kernel * volumeDensity *
        phaseGradientContraction metricInv testGradient phaseGradient := by
  rw [officialPhaseFirstVariation,
    phaseGradientContraction_comm metricInv hmetric phaseGradient testGradient]
  ring

end GDQ
