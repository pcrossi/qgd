import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.Tactic

namespace GDQ

/-!
# Regra de Born no setor puro finito

No espaço de Hilbert físico já reconstruído, um canal unitário `φ` recebe o
peso `|⟨φ,ψ⟩|²`. Este arquivo prova positividade, limite unitário e
normalização sobre uma base ortonormal finita.

O resultado é deliberadamente restrito ao setor puro e finito. Ele não afirma
o teorema de Gleason para POVMs gerais nem reconstrói, por si só, o espaço de
Hilbert da ação oficial.
-/

variable {ι E : Type*} [Fintype ι]
  [NormedAddCommGroup E] [InnerProductSpace ℂ E]

/-- Peso de Born de um canal puro `φ` no estado puro `ψ`. -/
noncomputable def pureBornWeight (φ ψ : E) : ℝ :=
  ‖inner ℂ φ ψ‖ ^ 2

/-- Todo peso puro é não negativo. -/
theorem pureBornWeight_nonneg (φ ψ : E) :
    0 ≤ pureBornWeight φ ψ := by
  unfold pureBornWeight
  positivity

/-- Para vetores unitários, o peso pertence ao intervalo `[0,1]`. -/
theorem pureBornWeight_le_one
    (φ ψ : E) (hφ : ‖φ‖ = 1) (hψ : ‖ψ‖ = 1) :
    pureBornWeight φ ψ ≤ 1 := by
  unfold pureBornWeight
  have h := norm_inner_le_norm (𝕜 := ℂ) φ ψ
  rw [hφ, hψ] at h
  norm_num at h ⊢
  nlinarith [norm_nonneg (inner ℂ φ ψ)]

/--
Parseval fornece a normalização de Born: os pesos de todos os canais de uma
base ortonormal finita somam a norma quadrada do estado.
-/
theorem pureBornWeights_sum_norm
    (b : OrthonormalBasis ι ℂ E) (ψ : E) :
    ∑ i, pureBornWeight (b i) ψ = ‖ψ‖ ^ 2 := by
  simpa [pureBornWeight] using b.sum_sq_norm_inner_right ψ

/-- Para um estado normalizado, a soma dos pesos de Born é exatamente `1`. -/
theorem pureBornWeights_sum_one
    (b : OrthonormalBasis ι ℂ E) (ψ : E) (hψ : ‖ψ‖ = 1) :
    ∑ i, pureBornWeight (b i) ψ = 1 := by
  rw [pureBornWeights_sum_norm b ψ, hψ]
  norm_num

end GDQ
