import GDQ.ControlledIntegrability

namespace GDQ

open MeasureTheory

/-!
# Ação oficial sobre contorno causal complexo

Esta camada permite `zτ ∈ ℂ` no colchete e no kernel, mantendo `R`,
`|∇f|²`, `Re f` e `sqrt(det g)` reais. Portanto ela descreve um background
riemanniano real avaliado ao longo de um contorno complexo. A complexificação
independente de todos os campos geométricos ainda não é assumida.
-/

/-- Colchete oficial com parâmetro de fluxo complexo. -/
def complexOfficialBracket
    (n : Nat) (zτ : ℂ)
    (scalarCurvature gradientNormSq realPotential : ℝ) : ℂ :=
  zτ * ((scalarCurvature + gradientNormSq : ℝ) : ℂ) +
    (realPotential : ℂ) - n

/-- Densidade oficial de um background real ao longo do contorno complexo. -/
noncomputable def complexContourOfficialDensity
    (n : Nat)
    (ℏ ΛC : ℝ)
    (zτ : ℂ)
    (scalarCurvature gradientNormSq realPotential ρ volumeDensity : ℝ) : ℂ :=
  ((ℏ / ΛC ^ 2 : ℝ) : ℂ) *
    complexOfficialBracket n zτ scalarCurvature gradientNormSq realPotential *
    officialFlowKernel n ρ zτ *
    (volumeDensity : ℂ)

/-- Restrição da densidade complexa ao eixo real. -/
theorem complexContourOfficialDensity_real_section
    (n : Nat)
    (ℏ ΛC zτ scalarCurvature gradientNormSq realPotential ρ
      volumeDensity : ℝ) :
    complexContourOfficialDensity n ℏ ΛC (zτ : ℂ)
        scalarCurvature gradientNormSq realPotential ρ volumeDensity =
      (officialPointDensity n ℏ ΛC zτ scalarCurvature gradientNormSq
        realPotential (euclideanFlowKernel n ρ zτ) volumeDensity : ℂ) := by
  norm_num [complexContourOfficialDensity, complexOfficialBracket,
    officialFlowKernel, officialPointDensity, officialBracket,
    euclideanFlowKernel]

/-- Densidade pontual produzida por dados geométricos ao longo de `γ`. -/
noncomputable def complexContourPointDensity
    (ℏ ΛC : ℝ)
    (Φ : AdmissibleConfiguration)
    (G : EuclideanGeometricInvariants)
    (γ : CausalContour)
    (t : ℝ) (x : LocalPoint) : ℂ :=
  complexContourOfficialDensity 4 ℏ ΛC (γ.z t)
    (G.scalarCurvature t x)
    (G.gradientNormSq t x)
    (Φ.potential x).re
    (Φ.toGDQFieldConfiguration.rho x)
    (G.volumeDensity t x)

/--
Dados suficientes para a ação oficial de background real sobre um contorno
complexo, com integrabilidade provada por dominação.
-/
structure ControlledComplexContourActionData where
  fields : AdmissibleConfiguration
  contour : CausalContour
  geometry : EuclideanGeometricInvariants
  ℏ : ℝ
  ΛC : ℝ
  ΛC_ne_zero : ΛC ≠ 0
  bulkControl :
    ∀ t,
      IntegrableDomination localBulkReferenceMeasure
        (complexContourPointDensity ℏ ΛC fields geometry contour t)
  contourControl :
    IntegrableDomination (MeasureTheory.volume : Measure ℝ)
      (fun t ↦
        (∫ x,
          complexContourPointDensity ℏ ΛC fields geometry contour t x
          ∂localBulkReferenceMeasure) *
          contour.dlog t)

/-- Construção da integral oficial puxada ao parâmetro real do contorno. -/
noncomputable def ControlledComplexContourActionData.toCandidate
    (A : ControlledComplexContourActionData) :
    PulledBackActionCandidate where
  bulkMeasure := localBulkReferenceMeasure
  contourMeasure := MeasureTheory.volume
  fields := A.fields
  contour := A.contour
  pointDensity :=
    complexContourPointDensity A.ℏ A.ΛC A.fields A.geometry A.contour
  bulkIntegrable := fun t ↦ (A.bulkControl t).integrable
  contourIntegrable := A.contourControl.integrable

/-- Valor da ação oficial no contorno complexo controlado. -/
noncomputable def ControlledComplexContourActionData.value
    (A : ControlledComplexContourActionData) : ℂ :=
  A.toCandidate.value

end GDQ
