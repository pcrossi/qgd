import GDQ.ActionDensity
import GDQ.Admissibility

namespace GDQ

/-!
# Invariantes geométricos da densidade oficial

Esta camada introduz, como dados explícitos de um background, as três
quantidades reais que ainda faltavam na densidade pontual:

* a curvatura escalar `R`;
* a norma quadrática `|∇f|²`;
* a densidade de volume `sqrt(det g)`.

Não se afirma ainda que essas funções foram calculadas por uma conexão suave.
As futuras construções diferenciais deverão produzir esta estrutura e provar
suas condições de sinal.
-/

/-- Dados geométricos reais de um background na seção euclidiana. -/
structure EuclideanGeometricInvariants where
  scalarCurvature : ℝ → LocalPoint → ℝ
  gradientNormSq : ℝ → LocalPoint → ℝ
  volumeDensity : ℝ → LocalPoint → ℝ
  gradientNormSq_nonneg :
    ∀ t x, 0 ≤ gradientNormSq t x
  volumeDensity_pos :
    ∀ t x, 0 < volumeDensity t x

/--
Densidade oficial na seção euclidiana, em dimensão complexa quatro.

A parcela `(f + f̄)/2` não é um parâmetro independente: ela é representada
diretamente por `Re f`. O kernel também não é independente, sendo reconstruído
de `ρ` e da escala euclidiana positiva `zτ`.
-/
noncomputable def euclideanOfficialDensity
    (ℏ ΛC : ℝ)
    (Φ : AdmissibleConfiguration)
    (G : EuclideanGeometricInvariants)
    (zτ : ℝ → ℝ)
    (t : ℝ) (x : LocalPoint) : ℝ :=
  officialPointDensity 4 ℏ ΛC (zτ t)
    (G.scalarCurvature t x)
    (G.gradientNormSq t x)
    (Φ.potential x).re
    (euclideanFlowKernel 4
      (Φ.toGDQFieldConfiguration.rho x) (zτ t))
    (G.volumeDensity t x)

/-- Expansão literal da densidade oficial, sem termo fenomenológico extra. -/
theorem euclideanOfficialDensity_unfold
    (ℏ ΛC : ℝ)
    (Φ : AdmissibleConfiguration)
    (G : EuclideanGeometricInvariants)
    (zτ : ℝ → ℝ)
    (t : ℝ) (x : LocalPoint) :
    euclideanOfficialDensity ℏ ΛC Φ G zτ t x =
      (ℏ / ΛC ^ 2) *
        (zτ t * (G.scalarCurvature t x + G.gradientNormSq t x) +
          (Φ.potential x).re - 4) *
        euclideanFlowKernel 4
          (Φ.toGDQFieldConfiguration.rho x) (zτ t) *
        G.volumeDensity t x := by
  rfl

/--
No locus regular e para escala de fluxo positiva, o kernel real que aparece
na densidade oficial é positivo.
-/
theorem euclideanOfficialDensity_kernel_pos
    (Φ : AdmissibleConfiguration)
    (zτ : ℝ → ℝ) (t : ℝ) (x : LocalPoint)
    (hx : Φ.RegularAt x) (hz : 0 < zτ t) :
    0 <
      euclideanFlowKernel 4
        (Φ.toGDQFieldConfiguration.rho x) (zτ t) := by
  exact euclideanFlowKernel_pos 4 hx hz

end GDQ
