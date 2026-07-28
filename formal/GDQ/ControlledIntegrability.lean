import GDQ.EuclideanOfficialAction
import GDQ.LocalMeasure

namespace GDQ

open MeasureTheory

/-!
# Integrabilidade controlada

Em vez de assumir diretamente `Integrable f μ`, esta camada exige uma função
dominante integrável e prova a integrabilidade pelo teorema de dominação.
-/

variable {α : Type*} [MeasurableSpace α]

/-- Certificado de integrabilidade por uma função dominante. -/
structure IntegrableDomination
    (μ : Measure α) (f : α → ℂ) where
  stronglyMeasurable : AEStronglyMeasurable f μ
  envelope : α → ℂ
  envelope_integrable : Integrable envelope μ
  norm_le : ∀ᵐ x ∂μ, ‖f x‖ ≤ ‖envelope x‖

/-- Uma dominação integrável fornece a integrabilidade da função alvo. -/
theorem IntegrableDomination.integrable
    {μ : Measure α} {f : α → ℂ}
    (D : IntegrableDomination μ f) :
    Integrable f μ :=
  D.envelope_integrable.mono D.stronglyMeasurable D.norm_le

/--
Dados controlados da ação oficial euclidiana com a medida concreta do bulk.

O contorno usa a medida de Lebesgue no parâmetro real.
-/
structure ControlledEuclideanOfficialActionData where
  fields : AdmissibleConfiguration
  contour : CausalContour
  realSection : PositiveRealSection contour
  geometry : EuclideanGeometricInvariants
  ℏ : ℝ
  ΛC : ℝ
  ΛC_ne_zero : ΛC ≠ 0
  bulkControl :
    ∀ t,
      IntegrableDomination localBulkReferenceMeasure
        (fun x ↦
          (euclideanOfficialDensity ℏ ΛC fields geometry
            realSection.scale t x : ℂ))
  contourControl :
    IntegrableDomination (MeasureTheory.volume : Measure ℝ)
      (fun t ↦
        (∫ x,
          (euclideanOfficialDensity ℏ ΛC fields geometry
            realSection.scale t x : ℂ)
          ∂localBulkReferenceMeasure) *
          contour.dlog t)

/-- Construção da ação oficial a partir dos certificados de dominação. -/
noncomputable def ControlledEuclideanOfficialActionData.toOfficialAction
    (A : ControlledEuclideanOfficialActionData) :
    EuclideanOfficialActionData where
  bulkMeasure := localBulkReferenceMeasure
  contourMeasure := MeasureTheory.volume
  fields := A.fields
  contour := A.contour
  realSection := A.realSection
  geometry := A.geometry
  ℏ := A.ℏ
  ΛC := A.ΛC
  ΛC_ne_zero := A.ΛC_ne_zero
  bulkIntegrable := fun t ↦ (A.bulkControl t).integrable
  contourIntegrable := A.contourControl.integrable

end GDQ
