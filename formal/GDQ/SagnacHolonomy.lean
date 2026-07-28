import Mathlib.Analysis.Complex.Exponential
import Mathlib.Tactic

namespace GDQ

/-!
# Fase orientada de Sagnac

Os dois feixes percorrem o mesmo circuito em orientações opostas. Uma fase
comum de propagação cancela na diferença; o termo ímpar sob reversão soma.
Este é o núcleo universal de holonomia. A conversão do parâmetro `rotation`
em `4 Ω·A/(λc)` ou na forma temporal correspondente depende da métrica e do
contorno do interferômetro real.
-/

/-- Fase de um canal orientado; `orientation = ±1` nos canais físicos. -/
def sagnacOrientedPhase
    (common rotation orientation : ℝ) : ℝ :=
  common + orientation * rotation

/-- Diferença entre os canais de orientação positiva e negativa. -/
theorem sagnac_phase_difference
    (common rotation : ℝ) :
    sagnacOrientedPhase common rotation 1
      - sagnacOrientedPhase common rotation (-1) = 2 * rotation := by
  unfold sagnacOrientedPhase
  ring

/-- A fase comum não participa da diferença interferométrica. -/
theorem sagnac_common_phase_cancels
    (common₁ common₂ rotation : ℝ) :
    (sagnacOrientedPhase common₁ rotation 1
        - sagnacOrientedPhase common₁ rotation (-1))
      =
    (sagnacOrientedPhase common₂ rotation 1
        - sagnacOrientedPhase common₂ rotation (-1)) := by
  rw [sagnac_phase_difference, sagnac_phase_difference]

/-- Inverter a rotação troca o sinal do deslocamento de fase. -/
theorem sagnac_rotation_reversal
    (common rotation : ℝ) :
    sagnacOrientedPhase common (-rotation) 1
        - sagnacOrientedPhase common (-rotation) (-1)
      =
    -(sagnacOrientedPhase common rotation 1
        - sagnacOrientedPhase common rotation (-1)) := by
  rw [sagnac_phase_difference, sagnac_phase_difference]
  ring

/-- Holonomia complexa correspondente a uma fase orientada. -/
noncomputable def sagnacHolonomy
    (common rotation orientation : ℝ) : ℂ :=
  Complex.exp (((sagnacOrientedPhase common rotation orientation : ℝ) : ℂ)
    * Complex.I)

/-- Mesma fase orientada implica a mesma holonomia. -/
theorem sagnacHolonomy_congr
    (common rotation orientation phase : ℝ)
    (hPhase : sagnacOrientedPhase common rotation orientation = phase) :
    sagnacHolonomy common rotation orientation
      = Complex.exp (((phase : ℝ) : ℂ) * Complex.I) := by
  simp [sagnacHolonomy, hPhase]

end GDQ
