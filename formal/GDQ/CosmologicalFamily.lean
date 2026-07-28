import GDQ.Spaces
import Mathlib.Data.Fin.Tuple.Basic
import Mathlib.Topology.Algebra.Order.Field

namespace GDQ

/-!
# Família cosmológica apontada

Este módulo não identifica o espaço cosmológico com o bulk local. Ele:

1. decompõe tipadamente `T⁵ × S³` como `T⁴ × S¹ × S³`;
2. registra a família de raios `R`;
3. formaliza a estimativa local `O(R⁻²)`;
4. prova que essa estimativa tende a zero quando `R → ∞`.

A estimativa geométrica é o certificado que vem do cálculo em coordenadas
normais da esfera redonda. A análise de Taylor da métrica ainda não é
reconstruída neste módulo.
-/

/-- O círculo angular que aparece como o quinto fator de `T⁵`. -/
abbrev CircleFactor := Real.Angle

/-- Modelo de produto usado na família apontada. -/
abbrev SplitCosmologicalModel :=
  Torus 4 × (CircleFactor × Sphere3)

/-- Separa funções indexadas por uma soma em um par de funções. -/
def sumPiEquivProdPi (α β γ : Type*) :
    (α ⊕ β → γ) ≃ ((α → γ) × (β → γ)) where
  toFun f := (fun a => f (Sum.inl a), fun b => f (Sum.inr b))
  invFun p := Sum.elim p.1 p.2
  left_inv f := by
    funext x
    cases x <;> rfl
  right_inv p := by
    cases p
    rfl

/-- Uma função em `Fin 1` contém exatamente um valor. -/
def finOnePiEquiv (γ : Type*) : (Fin 1 → γ) ≃ γ where
  toFun f := f 0
  invFun x := fun _ => x
  left_inv f := by
    funext i
    exact Fin.eq_zero i ▸ rfl
  right_inv _ := rfl

/-- Decomposição canônica `T⁵ ≃ T⁴ × S¹`. -/
def torusFiveEquivTorusFourCircle :
    Torus 5 ≃ (Torus 4 × CircleFactor) :=
  (Equiv.piCongrLeft (fun _ : Fin 5 => Real.Angle)
      (finSumFinEquiv : Fin 4 ⊕ Fin 1 ≃ Fin 5)).symm.trans
    ((sumPiEquivProdPi (Fin 4) (Fin 1) Real.Angle).trans
      (Equiv.prodCongr (Equiv.refl (Torus 4))
        (finOnePiEquiv Real.Angle)))

/-- Decomposição tipada do espaço cosmológico. -/
def cosmologicalEquivSplit :
    CosmologicalModel ≃ SplitCosmologicalModel :=
  (Equiv.prodCongr torusFiveEquivTorusFourCircle
    (Equiv.refl Sphere3)).trans
    (Equiv.prodAssoc (Torus 4) CircleFactor Sphere3)

/-- A decomposição não muda a dimensão real total. -/
theorem split_cosmological_real_dimension :
    4 + 1 + 3 = canonicalCosmologicalSpace.realDim := by
  decide

/--
Família geométrica escalada. O tipo subjacente é fixo; `circleRadius` e
`sphereRadius` registram as métricas escaladas, não novas coordenadas.
-/
structure ScaledCosmologicalGeometry where
  circleRadius : ℝ
  sphereRadius : ℝ
  circleRadius_pos : 0 < circleRadius
  sphereRadius_pos : 0 < sphereRadius

/-- Família isotrópica usada nos seis lemas. -/
def isotropicCosmologicalGeometry (R : ℝ) (hR : 0 < R) :
    ScaledCosmologicalGeometry where
  circleRadius := R
  sphereRadius := R
  circleRadius_pos := hR
  sphereRadius_pos := hR

/-- Parametrização equivalente `R_ε = ε⁻¹`. -/
noncomputable def epsilonCosmologicalGeometry (ε : ℝ) (hε : 0 < ε) :
    ScaledCosmologicalGeometry :=
  isotropicCosmologicalGeometry ε⁻¹ (inv_pos.mpr hε)

/-- Majorante abstrata do erro métrico em um compacto fixo. -/
noncomputable def pointedMetricErrorBound (C R : ℝ) : ℝ :=
  C * (R ^ 2)⁻¹

/-- A majorante `C R⁻²` tende a zero quando o raio tende ao infinito. -/
theorem pointedMetricErrorBound_tendsto_zero (C : ℝ) :
    Filter.Tendsto (pointedMetricErrorBound C)
      Filter.atTop (nhds 0) := by
  change Filter.Tendsto (fun R : ℝ => C * (R ^ 2)⁻¹)
    Filter.atTop (nhds 0)
  simpa using
    (tendsto_inv_atTop_zero.pow 2).const_mul C

/--
Certificado da estimativa em cartas normais.

`localError k L R` pode representar qualquer seminorma `Cᵏ` numa bola fixa
de raio `L`.
-/
structure PointedConvergenceCertificate where
  localError : Nat → ℝ → ℝ → ℝ
  constant : Nat → ℝ → ℝ
  constant_nonneg : ∀ k L, 0 ≤ constant k L
  error_nonneg : ∀ k L R, 0 ≤ localError k L R
  error_bound :
    ∀ k L R, 1 ≤ R →
      localError k L R ≤ pointedMetricErrorBound (constant k L) R

/--
Versão quantitativa do Lema 1: o certificado produz a estimativa local
`O(R⁻²)`.
-/
theorem PointedConvergenceCertificate.local_error_is_quadratic
    (P : PointedConvergenceCertificate) (k : Nat) (L R : ℝ)
    (hR : 1 ≤ R) :
    P.localError k L R ≤ P.constant k L * (R ^ 2)⁻¹ :=
  P.error_bound k L R hR

/-- O erro certificado converge efetivamente a zero em cada seminorma local. -/
theorem PointedConvergenceCertificate.local_error_tendsto_zero
    (P : PointedConvergenceCertificate) (k : Nat) (L : ℝ) :
    Filter.Tendsto (fun R => P.localError k L R)
      Filter.atTop (nhds 0) := by
  apply tendsto_of_tendsto_of_tendsto_of_le_of_le'
    tendsto_const_nhds
    (pointedMetricErrorBound_tendsto_zero (P.constant k L))
  · exact Filter.Eventually.of_forall (fun R => P.error_nonneg k L R)
  · exact (Filter.eventually_ge_atTop (1 : ℝ)).mono
      (fun R hR => P.error_bound k L R hR)

/--
O limite geométrico alvo da família é o bulk local oficial, mas somente em
sentido apontado. Esta etiqueta impede uma identificação global por definição.
-/
structure PointedCosmologicalLimit where
  source : GeometrySector := GeometrySector.cosmological
  target : GeometrySector := GeometrySector.local
  source_ne_target : source ≠ target

/-- Instância canônica da direção da ponte. -/
def canonicalPointedLimit : PointedCosmologicalLimit where
  source_ne_target := local_sector_ne_cosmological.symm

end GDQ
