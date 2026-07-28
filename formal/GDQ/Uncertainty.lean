import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Analysis.Complex.Norm
import Mathlib.Tactic

namespace GDQ

/-!
# Núcleo geométrico das desigualdades de incerteza

Depois da reconstrução do espaço de Hilbert físico, os vetores de flutuação
centrados `u = (A-⟨A⟩)ψ` e `v = (B-⟨B⟩)ψ` satisfazem Cauchy--Schwarz. As
partes real e imaginária do produto interno são, respectivamente, os canais
simétrico e antissimétrico da desigualdade de Robertson--Schrödinger.

Este módulo prova essa etapa universal. Domínio comum, auto-adjunticidade e
identificação dos vetores com observáveis físicos permanecem hipóteses da
aplicação, e não são ocultados por este resultado.
-/

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E]

/-- Forma de Cauchy da incerteza para dois vetores de flutuação. -/
theorem cauchy_uncertainty (u v : E) :
    ‖inner ℂ u v‖ ^ 2 ≤ ‖u‖ ^ 2 * ‖v‖ ^ 2 := by
  have h := norm_inner_le_norm (𝕜 := ℂ) u v
  nlinarith [norm_nonneg (inner ℂ u v), norm_nonneg u, norm_nonneg v]

/--
Núcleo de Robertson--Schrödinger: a covariância simétrica e o canal
antissimétrico aparecem como as partes real e imaginária do mesmo produto
interno.
-/
theorem robertson_schrodinger_core (u v : E) :
    (inner ℂ u v).re ^ 2 + (inner ℂ u v).im ^ 2
      ≤ ‖u‖ ^ 2 * ‖v‖ ^ 2 := by
  have h := cauchy_uncertainty u v
  rw [Complex.sq_norm, Complex.normSq_apply] at h
  simpa [pow_two] using h

/--
Versão com nomes físicos abstratos. Se `varianceA = ‖u‖²` e
`varianceB = ‖v‖²`, o produto das variâncias domina os dois canais.
-/
theorem uncertainty_from_variance_vectors
    (u v : E) (varianceA varianceB : ℝ)
    (hA : varianceA = ‖u‖ ^ 2)
    (hB : varianceB = ‖v‖ ^ 2) :
    (inner ℂ u v).re ^ 2 + (inner ℂ u v).im ^ 2
      ≤ varianceA * varianceB := by
  rw [hA, hB]
  exact robertson_schrodinger_core u v

end GDQ
