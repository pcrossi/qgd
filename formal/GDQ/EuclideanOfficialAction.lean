import GDQ.ActionIntegration
import GDQ.GeometricInvariants
import GDQ.ClockHomomorphism

namespace GDQ

open MeasureTheory

/-!
# Ação oficial na seção euclidiana real

Este arquivo liga a densidade oficial à infraestrutura de integração. A
restrição à seção real é uma hipótese declarada, não uma identificação
silenciosa do contorno causal complexo com o eixo positivo.
-/

/--
Testemunho de que o contorno causal considerado permanece na seção real
positiva `zτ(t) > 0`.
-/
structure PositiveRealSection (γ : CausalContour) where
  scale : ℝ → ℝ
  scale_pos : ∀ t, 0 < scale t
  contour_eq : ∀ t, γ.z t = (scale t : ℂ)

/--
Seção positiva canônica determinada pelo homomorfismo causal exponencial.

O mesmo objeto fornece simultaneamente o contorno e a escala de fluxo usada
na densidade, evitando uma normalização duplicada.
-/
noncomputable def exponentialPositiveRealSection
    (τ₀ κ : ℝ) (hτ₀ : 0 < τ₀) :
    PositiveRealSection (exponentialCausalContour τ₀ κ hτ₀) where
  scale := exponentialFlowScale τ₀ κ
  scale_pos := exponentialFlowScale_pos hτ₀ κ
  contour_eq := exponentialCausalContour_z τ₀ κ hτ₀

/-- Nessa seção, o pullback logarítmico usado pela ação é constante. -/
theorem exponentialPositiveRealSection_dlog
    (τ₀ κ : ℝ) (hτ₀ : 0 < τ₀) (t : ℝ) :
    (exponentialCausalContour τ₀ κ hτ₀).dlog t = (κ : ℂ) :=
  exponentialCausalContour_dlog τ₀ κ hτ₀ t

variable [MeasurableSpace LocalPoint]

/--
Dados suficientes para construir a integral oficial na seção euclidiana.

As duas provas de integrabilidade permanecem obrigações explícitas. Portanto,
esta estrutura não declara que todo background admissível possui ação finita.
-/
structure EuclideanOfficialActionData where
  bulkMeasure : Measure LocalPoint
  contourMeasure : Measure ℝ
  fields : AdmissibleConfiguration
  contour : CausalContour
  realSection : PositiveRealSection contour
  geometry : EuclideanGeometricInvariants
  ℏ : ℝ
  ΛC : ℝ
  ΛC_ne_zero : ΛC ≠ 0
  bulkIntegrable :
    ∀ t,
      Integrable
        (fun x ↦
          (euclideanOfficialDensity ℏ ΛC fields geometry
            realSection.scale t x : ℂ))
        bulkMeasure
  contourIntegrable :
    Integrable
      (fun t ↦
        (∫ x,
          (euclideanOfficialDensity ℏ ΛC fields geometry
            realSection.scale t x : ℂ)
          ∂bulkMeasure) *
          contour.dlog t)
      contourMeasure

/-- Conversão canônica para a infraestrutura genérica de integral puxada. -/
noncomputable def EuclideanOfficialActionData.toCandidate
    (A : EuclideanOfficialActionData) :
    PulledBackActionCandidate where
  bulkMeasure := A.bulkMeasure
  contourMeasure := A.contourMeasure
  fields := A.fields
  contour := A.contour
  pointDensity := fun t x ↦
    (euclideanOfficialDensity A.ℏ A.ΛC A.fields A.geometry
      A.realSection.scale t x : ℂ)
  bulkIntegrable := A.bulkIntegrable
  contourIntegrable := A.contourIntegrable

/-- Valor da ação oficial restrita à seção euclidiana positiva. -/
noncomputable def EuclideanOfficialActionData.value
    (A : EuclideanOfficialActionData) : ℂ :=
  A.toCandidate.value

/-- A integral resultante contém exatamente a densidade oficial construída. -/
theorem EuclideanOfficialActionData.value_unfold
    (A : EuclideanOfficialActionData) :
    A.value =
      ∫ t,
        (∫ x,
          (euclideanOfficialDensity A.ℏ A.ΛC A.fields A.geometry
            A.realSection.scale t x : ℂ)
          ∂A.bulkMeasure) *
          A.contour.dlog t
        ∂A.contourMeasure := by
  rfl

end GDQ
