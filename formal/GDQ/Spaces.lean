import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Angle

namespace GDQ

open scoped BigOperators

/-!
# Espaços fundamentais

Os dois espaços recebem tipos diferentes. Isso impede que um teorema provado
para o espaço cosmológico seja aplicado ao bulk local sem um mapa explícito.

Neste estágio registramos modelos concretos dos produtos e suas dimensões. A
estrutura completa de variedade Hermitiana será acrescentada depois.
-/

/-- Modelo de coordenadas para `ℝ⁴`. -/
abbrev Euclidean4 := Fin 4 → ℝ

/-- Toro angular `Tⁿ = (ℝ / 2πℤ)ⁿ`. -/
abbrev Torus (n : Nat) := Fin n → Real.Angle

/-- Modelo concreto do bulk local `ℝ⁴ × T⁴`. -/
abbrev LocalBulkModel := Euclidean4 × Torus 4

/-- Norma quadrática ambiente usada para definir a esfera unitária. -/
def normSq4 (x : Euclidean4) : ℝ :=
  ∑ i, x i ^ 2

/-- Modelo conjuntista da esfera unitária `S³ ⊂ ℝ⁴`. -/
def Sphere3 := {x : Euclidean4 // normSq4 x = 1}

/-- Modelo concreto do espaço cosmológico `T⁵ × S³`. -/
abbrev CosmologicalModel := Torus 5 × Sphere3

/-- Etiquetas que impedem confundir os dois papéis geométricos. -/
inductive GeometrySector
  | local
  | cosmological
  deriving DecidableEq

theorem local_sector_ne_cosmological :
    GeometrySector.local ≠ GeometrySector.cosmological := by
  decide

/-- Registro dimensional do bulk local oficial. -/
structure LocalBulk where
  realDim : Nat
  complexDim : Nat

/-- Registro dimensional do espaço cosmológico/espectral. -/
structure CosmologicalSpace where
  realDim : Nat
  torusDim : Nat
  sphereDim : Nat

/-- Dimensões canônicas do bulk local oficial. -/
def canonicalLocalBulk : LocalBulk where
  realDim := 8
  complexDim := 4

/-- Dimensões canônicas do espaço cosmológico auxiliar. -/
def canonicalCosmologicalSpace : CosmologicalSpace where
  realDim := 8
  torusDim := 5
  sphereDim := 3

theorem local_real_dimension :
    canonicalLocalBulk.realDim = 8 := by
  rfl

theorem local_complex_dimension :
    canonicalLocalBulk.complexDim = 4 := by
  rfl

theorem local_dimensions_are_compatible :
    canonicalLocalBulk.realDim = 2 * canonicalLocalBulk.complexDim := by
  decide

theorem cosmological_product_dimension :
    canonicalCosmologicalSpace.realDim =
      canonicalCosmologicalSpace.torusDim +
        canonicalCosmologicalSpace.sphereDim := by
  decide

end GDQ
