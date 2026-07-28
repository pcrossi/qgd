import GDQ.Spaces
import GDQ.Constitutive

namespace GDQ

/-!
# Campos fundamentais

Esta camada registra a assinatura matemática dos campos da GDQ sobre o bulk
local. Regularidade, conexão de Bismut e integração ainda serão acrescentadas
como estruturas posteriores.
-/

/-- Ponto do modelo local `ℝ⁴ × T⁴`. -/
abbrev LocalPoint := LocalBulkModel

/-- Vetor tangente real no modelo de dimensão oito. -/
abbrev LocalTangent := Fin 8 → ℝ

/-- Vetor complexo no modelo de dimensão complexa quatro. -/
abbrev ComplexTangent := Fin 4 → ℂ

/--
Dados de uma métrica Hermitiana em coordenadas complexas.

A positividade é mantida como obrigação explícita do objeto, e não inferida
apenas da palavra "métrica".
-/
structure HermitianMetricData where
  coeff : LocalPoint → Fin 4 → Fin 4 → ℂ
  hermitian :
    ∀ x μ ν, coeff x μ ν = starRingEnd ℂ (coeff x ν μ)
  positive :
    ∀ x (v : ComplexTangent), v ≠ 0 →
      0 < Complex.re
        (∑ μ, ∑ ν,
          starRingEnd ℂ (v μ) * coeff x μ ν * v ν)

/-- Estrutura complexa quase-complexa, com `J² = -Id`. -/
structure ComplexStructureData where
  act : LocalPoint → LocalTangent → LocalTangent
  square_neg :
    ∀ x v, act x (act x v) = -v

/-- Três-forma real de torção, com antissimetria elementar. -/
structure TorsionData where
  value : LocalPoint → Fin 8 → Fin 8 → Fin 8 → ℝ
  swap₁₂ :
    ∀ x i j k, value x i j k = -value x j i k
  swap₂₃ :
    ∀ x i j k, value x i j k = -value x i k j

/-- Potencial complexo fundamental `f`. -/
abbrev ComplexPotential := LocalPoint → ℂ

/-- Parâmetro de fluxo positivo. -/
structure FlowPoint where
  τ : ℝ
  τ_pos : 0 < τ
  zτ : ℂ
  zτ_ne_zero : zτ ≠ 0

/-- Kernel ponderado antes da introdução de uma medida integral. -/
abbrev FlowKernel := FlowPoint → LocalPoint → ℂ

/-- Configuração dos campos fundamentais da GDQ. -/
structure GDQFieldConfiguration where
  metric : HermitianMetricData
  complexStructure : ComplexStructureData
  torsion : TorsionData
  potential : ComplexPotential
  density : LocalPoint → ℝ
  density_nonneg : ∀ x, 0 ≤ density x
  potential_law :
    ∀ x, 0 < density x →
      density x = densityFromPotential (potential x)
  kernel : FlowKernel

/-- Densidade real pontual da configuração. -/
def GDQFieldConfiguration.rho
    (Φ : GDQFieldConfiguration) (x : LocalPoint) : ℝ :=
  Φ.density x

/-- Locus regular: pontos em que a densidade é estritamente positiva. -/
def GDQFieldConfiguration.RegularAt
    (Φ : GDQFieldConfiguration) (x : LocalPoint) : Prop :=
  0 < Φ.rho x

/-- A densidade é globalmente não negativa, mas pode se anular. -/
theorem GDQFieldConfiguration.rho_nonneg
    (Φ : GDQFieldConfiguration) (x : LocalPoint) :
    0 ≤ Φ.rho x := by
  exact Φ.density_nonneg x

/-- No locus regular, vale a relação constitutiva exponencial. -/
theorem GDQFieldConfiguration.rho_eq_exp_on_regular
    (Φ : GDQFieldConfiguration) (x : LocalPoint)
    (hx : Φ.RegularAt x) :
    Φ.rho x = densityFromPotential (Φ.potential x) := by
  exact Φ.potential_law x hx

/-- Fora do locus regular, a não negatividade força `ρ = 0`. -/
theorem GDQFieldConfiguration.rho_eq_zero_of_not_regular
    (Φ : GDQFieldConfiguration) (x : LocalPoint)
    (hx : ¬ Φ.RegularAt x) :
    Φ.rho x = 0 := by
  exact le_antisymm (not_lt.mp hx) (Φ.rho_nonneg x)

end GDQ
