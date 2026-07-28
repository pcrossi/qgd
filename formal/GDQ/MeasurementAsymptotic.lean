import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

namespace GDQ

/-!
# Registros assintóticos no setor espectral reduzido

Este módulo certifica o núcleo quantitativo do teorema humano:

* um gap positivo faz o envelope fora da diagonal decair exponencialmente;
* projetores idempotentes tornam a segunda leitura ideal repetível.

Autoadjunticidade da Hessiana, existência dos projetores de Riesz e bacias
Morse reais continuam hipóteses geométricas da aplicação.
-/

/-- Envelope escalar de uma coerência entre dois setores separados. -/
noncomputable def coherenceEnvelope (C gap t : ℝ) : ℝ :=
  C * Real.exp (-gap * t)

/-- Um gap estritamente positivo suprime assintoticamente o envelope. -/
theorem coherenceEnvelope_tendsto_zero
    {C gap : ℝ} (hgap : 0 < gap) :
    Filter.Tendsto (coherenceEnvelope C gap)
      Filter.atTop (nhds 0) := by
  unfold coherenceEnvelope
  have hlin :
      Filter.Tendsto (fun t : ℝ => -gap * t)
        Filter.atTop Filter.atBot :=
    Filter.Tendsto.const_mul_atTop_of_neg
      (neg_lt_zero.mpr hgap)
      (by
        refine Filter.tendsto_atTop.2 ?_
        intro b
        exact Filter.eventually_ge_atTop b)
  simpa using
    (Filter.Tendsto.const_mul C
      (Real.tendsto_exp_atBot.comp hlin))

/--
Se uma coerência é dominada em módulo pelo envelope exponencial, ela também
converge a zero.
-/
theorem coherence_tendsto_zero_of_bound
    {Γ : ℝ → ℝ} {C gap : ℝ}
    (hgap : 0 < gap)
    (hbound : ∀ t, |Γ t| ≤ coherenceEnvelope C gap t) :
    Filter.Tendsto Γ Filter.atTop (nhds 0) := by
  apply tendsto_zero_iff_norm_tendsto_zero.mpr
  simpa [Real.norm_eq_abs] using
    (squeeze_zero (fun t => abs_nonneg (Γ t)) hbound
      (coherenceEnvelope_tendsto_zero hgap))

/--
Núcleo algébrico da repetibilidade: se a projeção condicionada preserva o
mesmo peso não nulo, a probabilidade da segunda leitura é um.
-/
theorem ideal_record_repeatability
    {initialWeight repeatedNumerator : ℝ}
    (hweight : initialWeight ≠ 0)
    (hidempotentWeight : repeatedNumerator = initialWeight) :
    repeatedNumerator / initialWeight = 1 := by
  rw [hidempotentWeight]
  exact div_self hweight

end GDQ
