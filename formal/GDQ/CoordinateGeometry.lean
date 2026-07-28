import GDQ.GeometricInvariants
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic

namespace GDQ

open scoped BigOperators

/-!
# Geometria coordenada e equações de Bismut

Esta camada trabalha com o jato coordenado dos campos em dimensão real oito.
As derivadas de primeira ordem e as derivadas da conexão são dados do jato;
as identidades abaixo são equações verificáveis, e não nomes proposicionais
abstratos.

Uma etapa posterior deverá construir esses jatos a partir de cartas suaves.
-/

abbrev Index8 := Fin 8
abbrev RealMatrix8 := Matrix Index8 Index8 ℝ

/--
Jato coordenado de um background GDQ admissível.

Convenção para a conexão:
`connection x k i j = Γ^k_{ij}`.
-/
structure CoordinateBismutBackground
    (Φ : AdmissibleConfiguration) where
  metric : LocalPoint → RealMatrix8
  inverseMetric : LocalPoint → RealMatrix8
  metricDerivative : LocalPoint → Index8 → Index8 → Index8 → ℝ
  connection : LocalPoint → Index8 → Index8 → Index8 → ℝ
  connectionDerivative :
    LocalPoint → Index8 → Index8 → Index8 → Index8 → ℝ
  complexCoeff : LocalPoint → Index8 → Index8 → ℝ
  complexDerivative : LocalPoint → Index8 → Index8 → Index8 → ℝ
  potentialDerivativeRe : LocalPoint → Index8 → ℝ
  potentialDerivativeIm : LocalPoint → Index8 → ℝ
  metric_symmetric :
    ∀ x i j, metric x i j = metric x j i
  metric_positive :
    ∀ x (v : Index8 → ℝ), v ≠ 0 →
      0 < ∑ i, ∑ j, v i * metric x i j * v j
  metric_det_pos :
    ∀ x, 0 < Matrix.det (metric x)
  inverse_law :
    ∀ x i j,
      ∑ k, inverseMetric x i k * metric x k j =
        if i = j then 1 else 0
  complex_square_neg :
    ∀ x i j,
      ∑ k, complexCoeff x i k * complexCoeff x k j =
        if i = j then -1 else 0
  complex_integrable :
    ∀ x i j k,
      (∑ p,
          complexCoeff x p i * complexDerivative x p k j -
          complexCoeff x p j * complexDerivative x p k i) -
        ∑ p,
          complexCoeff x k p *
            (complexDerivative x i p j - complexDerivative x j p i) = 0
  metric_compatible :
    ∀ x i a b,
      metricDerivative x i a b -
        (∑ m, connection x m i a * metric x m b) -
        (∑ m, connection x m i b * metric x a m) = 0
  complex_compatible :
    ∀ x i a b,
      complexDerivative x i a b +
        (∑ m, connection x a i m * complexCoeff x m b) -
        (∑ m, connection x m i b * complexCoeff x a m) = 0
  torsion_matches :
    ∀ x i j k,
      (∑ m,
          metric x k m *
            (connection x m i j - connection x m j i)) =
        Φ.torsion.value x i j k
  gradientNormSq_nonneg :
    ∀ x,
      0 ≤
        ∑ i, ∑ j,
          inverseMetric x i j *
            (potentialDerivativeRe x i * potentialDerivativeRe x j +
              potentialDerivativeIm x i * potentialDerivativeIm x j)

/-- Curvatura de Riemann coordenada `R^l_{kij}`. -/
def CoordinateBismutBackground.riemann
    {Φ : AdmissibleConfiguration}
    (B : CoordinateBismutBackground Φ)
    (x : LocalPoint) (l k i j : Index8) : ℝ :=
  B.connectionDerivative x i l j k -
    B.connectionDerivative x j l i k +
    ∑ m,
      (B.connection x l i m * B.connection x m j k -
        B.connection x l j m * B.connection x m i k)

/-- Tensor de Ricci coordenado `Ric_{kj}=R^l_{klj}`. -/
def CoordinateBismutBackground.ricci
    {Φ : AdmissibleConfiguration}
    (B : CoordinateBismutBackground Φ)
    (x : LocalPoint) (k j : Index8) : ℝ :=
  ∑ l, B.riemann x l k l j

/-- Curvatura escalar obtida por contração com a métrica inversa. -/
def CoordinateBismutBackground.scalarCurvature
    {Φ : AdmissibleConfiguration}
    (B : CoordinateBismutBackground Φ)
    (x : LocalPoint) : ℝ :=
  ∑ i, ∑ j, B.inverseMetric x i j * B.ricci x i j

/--
Norma real coordenada do diferencial do potencial complexo.

A expressão soma as normas das partes real e imaginária. A equivalência com
a notação Hermitiana `g^{μν̄} ∂μf ∂ν̄f̄` depende da convenção real--complexa
fixada pelas cartas.
-/
def CoordinateBismutBackground.gradientNormSq
    {Φ : AdmissibleConfiguration}
    (B : CoordinateBismutBackground Φ)
    (x : LocalPoint) : ℝ :=
  ∑ i, ∑ j,
    B.inverseMetric x i j *
      (B.potentialDerivativeRe x i * B.potentialDerivativeRe x j +
        B.potentialDerivativeIm x i * B.potentialDerivativeIm x j)

/-- Densidade volumétrica coordenada derivada do determinante métrico. -/
noncomputable def CoordinateBismutBackground.volumeDensity
    {Φ : AdmissibleConfiguration}
    (B : CoordinateBismutBackground Φ)
    (x : LocalPoint) : ℝ :=
  Real.sqrt (Matrix.det (B.metric x))

/-- A densidade volumétrica derivada é estritamente positiva. -/
theorem CoordinateBismutBackground.volumeDensity_pos
    {Φ : AdmissibleConfiguration}
    (B : CoordinateBismutBackground Φ)
    (x : LocalPoint) :
    0 < B.volumeDensity x := by
  exact Real.sqrt_pos.2 (B.metric_det_pos x)

/-- Os invariantes oficiais derivados do jato coordenado. -/
noncomputable def CoordinateBismutBackground.toGeometricInvariants
    {Φ : AdmissibleConfiguration}
    (B : CoordinateBismutBackground Φ) :
    EuclideanGeometricInvariants where
  scalarCurvature := fun _ x ↦ B.scalarCurvature x
  gradientNormSq := fun _ x ↦ B.gradientNormSq x
  volumeDensity := fun _ x ↦ B.volumeDensity x
  gradientNormSq_nonneg := fun _ x ↦ B.gradientNormSq_nonneg x
  volumeDensity_pos := fun _ x ↦ B.volumeDensity_pos x

end GDQ
