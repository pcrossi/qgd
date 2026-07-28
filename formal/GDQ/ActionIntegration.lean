import GDQ.Admissibility
import GDQ.CausalContour
import Mathlib.MeasureTheory.Integral.Bochner.Basic

namespace GDQ

open MeasureTheory

variable [MeasurableSpace LocalPoint]

/-!
# Infraestrutura de integração da ação

Este arquivo formaliza a integral iterada após o pullback do contorno. Um
candidato só é construído quando as integrais interna e externa são
integráveis. A densidade ainda é um argumento: sua identificação com a
densidade pontual oficial será feita após introduzir os invariantes
geométricos necessários.
-/

/-- Dados de medida e densidade para uma integral puxada ao parâmetro real. -/
structure PulledBackActionCandidate where
  bulkMeasure : Measure LocalPoint
  contourMeasure : Measure ℝ
  fields : AdmissibleConfiguration
  contour : CausalContour
  pointDensity : ℝ → LocalPoint → ℂ
  bulkIntegrable :
    ∀ t, Integrable (pointDensity t) bulkMeasure
  contourIntegrable :
    Integrable
      (fun t ↦
        (∫ x, pointDensity t x ∂bulkMeasure) * contour.dlog t)
      contourMeasure

/-- Integral dupla com o pullback explícito de `dτ/τ`. -/
noncomputable def PulledBackActionCandidate.value
    (A : PulledBackActionCandidate) : ℂ :=
  ∫ t,
    (∫ x, A.pointDensity t x ∂A.bulkMeasure) *
      A.contour.dlog t
    ∂A.contourMeasure

/-- A forma expandida da integral é exatamente sua definição. -/
theorem PulledBackActionCandidate.value_unfold
    (A : PulledBackActionCandidate) :
    A.value =
      ∫ t,
        (∫ x, A.pointDensity t x ∂A.bulkMeasure) *
          A.contour.dlog t
        ∂A.contourMeasure := by
  rfl

end GDQ
