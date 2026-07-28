import GDQ.DetectorDtNSchur
import Mathlib.Analysis.SpecialFunctions.Exponential
import Mathlib.Data.Complex.Basic
import Mathlib.Order.Filter.AtTopBot.Field
import Mathlib.Tactic

namespace GDQ

/-!
# Transporte, interferência e contorno causal

Este módulo certifica os resultados reduzidos já demonstrados no Capítulo 12:

* atenuação evanescente e saturação geométrica de Hartman;
* identidade exata da densidade de duas amplitudes coerentes;
* limites construtivo e destrutivo do padrão;
* independência do registro em relação a mudanças fora do suporte causal.

A relação `gₓₓ ∝ ρ` continua sendo hipótese do setor evanescente reduzido,
não uma identidade universal da ação oficial.
-/

open scoped BigOperators

section Hartman

/-- Razão de densidade no canal evanescente reduzido. -/
noncomputable def evanescentDensityRatio (κ L : ℝ) : ℝ :=
  Real.exp (-2 * κ * L)

/-- A atenuação evanescente pertence a `(0,1]` para `κ,L ≥ 0`. -/
theorem evanescentDensityRatio_mem
    {κ L : ℝ} (hκ : 0 ≤ κ) (hL : 0 ≤ L) :
    0 < evanescentDensityRatio κ L ∧
      evanescentDensityRatio κ L ≤ 1 := by
  constructor
  · exact Real.exp_pos _
  · unfold evanescentDensityRatio
    rw [Real.exp_le_one_iff]
    have hproduct : 0 ≤ κ * L := mul_nonneg hκ hL
    nlinarith

/--
Distância própria no ansatz reduzido
`gₓₓ = g₀ exp(-2 κ x)`, com `sqrtg₀ = √g₀`.
-/
noncomputable def reducedHartmanDistance
    (sqrtg₀ κ L : ℝ) : ℝ :=
  sqrtg₀ / κ * (1 - Real.exp (-κ * L))

/-- Assíntota geométrica da distância própria. -/
noncomputable def reducedHartmanAsymptote
    (sqrtg₀ κ : ℝ) : ℝ :=
  sqrtg₀ / κ

/-- O erro para a assíntota é exatamente exponencial. -/
theorem reducedHartmanAsymptote_sub_distance
    (sqrtg₀ κ L : ℝ) :
    reducedHartmanAsymptote sqrtg₀ κ -
        reducedHartmanDistance sqrtg₀ κ L =
      sqrtg₀ / κ * Real.exp (-κ * L) := by
  unfold reducedHartmanAsymptote reducedHartmanDistance
  ring

/-- A distância própria é não negativa e limitada pela assíntota. -/
theorem reducedHartmanDistance_mem
    {sqrtg₀ κ L : ℝ}
    (hg : 0 ≤ sqrtg₀) (hκ : 0 < κ) (hL : 0 ≤ L) :
    0 ≤ reducedHartmanDistance sqrtg₀ κ L ∧
      reducedHartmanDistance sqrtg₀ κ L ≤
        reducedHartmanAsymptote sqrtg₀ κ := by
  have hexp_pos : 0 < Real.exp (-κ * L) := Real.exp_pos _
  have hexp_le : Real.exp (-κ * L) ≤ 1 := by
    rw [Real.exp_le_one_iff]
    have hproduct : 0 ≤ κ * L := mul_nonneg hκ.le hL
    nlinarith
  have hfactor : 0 ≤ sqrtg₀ / κ := div_nonneg hg hκ.le
  constructor
  · unfold reducedHartmanDistance
    exact mul_nonneg hfactor (sub_nonneg.mpr hexp_le)
  · rw [← sub_nonneg]
    rw [reducedHartmanAsymptote_sub_distance]
    exact mul_nonneg hfactor hexp_pos.le

/-- Saturação de Hartman: a distância tende à assíntota quando `L → ∞`. -/
theorem reducedHartmanDistance_tendsto
    (sqrtg₀ κ : ℝ) (hκ : 0 < κ) :
    Filter.Tendsto
      (fun L => reducedHartmanDistance sqrtg₀ κ L)
      Filter.atTop
      (nhds (reducedHartmanAsymptote sqrtg₀ κ)) := by
  have hscale :
      Filter.Tendsto (fun L : ℝ => κ * L)
        Filter.atTop Filter.atTop :=
    (Filter.tendsto_const_mul_atTop_of_pos hκ).2 Filter.tendsto_id
  have hexp :
      Filter.Tendsto (fun L : ℝ => Real.exp (-(κ * L)))
        Filter.atTop (nhds 0) :=
    Real.tendsto_exp_neg_atTop_nhds_zero.comp hscale
  have honeSub :
      Filter.Tendsto
        (fun L : ℝ => 1 - Real.exp (-(κ * L)))
        Filter.atTop (nhds 1) := by
    convert tendsto_const_nhds.sub hexp using 1 <;> simp
  have hconstant :
      Filter.Tendsto (fun _ : ℝ => sqrtg₀ / κ)
        Filter.atTop (nhds (sqrtg₀ / κ)) :=
    tendsto_const_nhds
  have hmul := hconstant.mul honeSub
  simpa [reducedHartmanDistance, reducedHartmanAsymptote,
    neg_mul] using hmul

/-- Tempo próprio reduzido para velocidade local constante positiva. -/
noncomputable def reducedHartmanTime
    (sqrtg₀ velocity κ L : ℝ) : ℝ :=
  reducedHartmanDistance sqrtg₀ κ L / velocity

/-- O tempo próprio satura junto com a distância própria. -/
theorem reducedHartmanTime_tendsto
    (sqrtg₀ velocity κ : ℝ) (hκ : 0 < κ) :
    Filter.Tendsto
      (fun L => reducedHartmanTime sqrtg₀ velocity κ L)
      Filter.atTop
      (nhds (reducedHartmanAsymptote sqrtg₀ κ / velocity)) := by
  exact (reducedHartmanDistance_tendsto sqrtg₀ κ hκ).div_const velocity

end Hartman

section Interference

/--
Densidade coerente exata de duas amplitudes complexas.
-/
theorem coherentTwoPathDensity (ψ₁ ψ₂ : ℂ) :
    Complex.normSq (ψ₁ + ψ₂) =
      Complex.normSq ψ₁ + Complex.normSq ψ₂ +
        2 * (ψ₁ * (starRingEnd ℂ) ψ₂).re :=
  Complex.normSq_add ψ₁ ψ₂

/-- Intensidade reduzida escrita em amplitudes reais e diferença de fase. -/
noncomputable def twoPathIntensity
    (amplitude₁ amplitude₂ phase : ℝ) : ℝ :=
  amplitude₁ ^ 2 + amplitude₂ ^ 2 +
    2 * amplitude₁ * amplitude₂ * Real.cos phase

/-- Limite destrutivo do padrão para amplitudes não negativas. -/
theorem twoPathIntensity_lower_bound
    {amplitude₁ amplitude₂ phase : ℝ}
    (h₁ : 0 ≤ amplitude₁) (h₂ : 0 ≤ amplitude₂) :
    (amplitude₁ - amplitude₂) ^ 2 ≤
      twoPathIntensity amplitude₁ amplitude₂ phase := by
  unfold twoPathIntensity
  have hcos : -1 ≤ Real.cos phase := Real.neg_one_le_cos phase
  have hab : 0 ≤ 2 * amplitude₁ * amplitude₂ := by positivity
  have hphase : 0 ≤ Real.cos phase + 1 := by linarith
  have hproduct :
      0 ≤ (2 * amplitude₁ * amplitude₂) *
        (Real.cos phase + 1) :=
    mul_nonneg hab hphase
  nlinarith

/-- Limite construtivo do padrão para amplitudes não negativas. -/
theorem twoPathIntensity_upper_bound
    {amplitude₁ amplitude₂ phase : ℝ}
    (h₁ : 0 ≤ amplitude₁) (h₂ : 0 ≤ amplitude₂) :
    twoPathIntensity amplitude₁ amplitude₂ phase ≤
      (amplitude₁ + amplitude₂) ^ 2 := by
  unfold twoPathIntensity
  have hcos := Real.cos_le_one phase
  have hab : 0 ≤ 2 * amplitude₁ * amplitude₂ := by positivity
  have hphase : 0 ≤ 1 - Real.cos phase := by linarith
  have hproduct :
      0 ≤ (2 * amplitude₁ * amplitude₂) *
        (1 - Real.cos phase) :=
    mul_nonneg hab hphase
  nlinarith

/-- Fase igual produz o máximo construtivo. -/
theorem twoPathIntensity_zero_phase
    (amplitude₁ amplitude₂ : ℝ) :
    twoPathIntensity amplitude₁ amplitude₂ 0 =
      (amplitude₁ + amplitude₂) ^ 2 := by
  simp [twoPathIntensity]
  ring

/-- Fase oposta produz o mínimo destrutivo. -/
theorem twoPathIntensity_pi_phase
    (amplitude₁ amplitude₂ : ℝ) :
    twoPathIntensity amplitude₁ amplitude₂ Real.pi =
      (amplitude₁ - amplitude₂) ^ 2 := by
  simp [twoPathIntensity]
  ring

end Interference

section DelayedChoice

variable {T : Type*} [Fintype T]

/--
Kernel causal finito: `future t` marca dados posteriores ao registro e seus
pesos devem desaparecer.
-/
structure FiniteCausalReadoutKernel (T : Type*)
    [Fintype T] where
  weight : T → ℝ
  future : T → Prop
  zero_on_future : ∀ t, future t → weight t = 0

/-- Registro linear produzido pelo histórico acessível ao kernel. -/
noncomputable def FiniteCausalReadoutKernel.record
    (K : FiniteCausalReadoutKernel T) (response : T → ℝ) : ℝ :=
  ∑ t, K.weight t * response t

/--
Alterar apenas os dados posteriores ao registro não muda o resultado causal.
-/
theorem FiniteCausalReadoutKernel.record_eq_of_past_eq
    (K : FiniteCausalReadoutKernel T)
    (oldResponse newResponse : T → ℝ)
    (hPast :
      ∀ t, ¬K.future t → oldResponse t = newResponse t) :
    K.record oldResponse = K.record newResponse := by
  unfold FiniteCausalReadoutKernel.record
  apply Finset.sum_congr rfl
  intro t _
  by_cases hFuture : K.future t
  · rw [K.zero_on_future t hFuture]
    simp
  · rw [hPast t hFuture]

end DelayedChoice

end GDQ
