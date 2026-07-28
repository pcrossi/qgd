import GDQ.ComplexContourAction
import Mathlib.Analysis.Calculus.FDeriv.Basic
import Mathlib.Analysis.InnerProductSpace.Basic

namespace GDQ

/-!
# Variações admissíveis, Hessiana e projetor físico

A ação variada nesta camada é sempre a parte real do valor produzido por uma
família de dados da ação oficial. A Hessiana não é introduzida como operador
independente: ela deve ser a derivada de Fréchet do gradiente que representa
a primeira variação.
-/

variable
  {E : Type*}
  [NormedAddCommGroup E]
  [InnerProductSpace ℝ E]

/--
Família de configurações da ação oficial parametrizada por um espaço real de
variações.
-/
structure OfficialActionVariationFamily (E : Type*)
    [NormedAddCommGroup E] [InnerProductSpace ℝ E] where
  configuration : E → ControlledComplexContourActionData

/-- Funcional real variado, obtido da ação oficial no contorno. -/
noncomputable def OfficialActionVariationFamily.action
    (F : OfficialActionVariationFamily E) (u : E) : ℝ :=
  (F.configuration u).value.re

/-- A ação da família é, por definição, a parte real da ação oficial. -/
theorem OfficialActionVariationFamily.action_eq_official
    (F : OfficialActionVariationFamily E) (u : E) :
    F.action u = (F.configuration u).value.re := by
  rfl

/--
Dados da primeira e da segunda variações físicas.

As condições de auto-adjunticidade, remoção de gauge e preservação do espaço
admissível são obrigações explícitas.
-/
structure PhysicalHessianData
    (F : OfficialActionVariationFamily E) where
  background : E
  admissible : Submodule ℝ E
  gauge : Submodule ℝ E
  projector : E →L[ℝ] E
  projector_idempotent :
    ∀ v, projector (projector v) = projector v
  projector_selfAdjoint :
    ∀ u v, inner ℝ (projector u) v = inner ℝ u (projector v)
  projector_range_admissible :
    ∀ v, projector v ∈ admissible
  projector_kills_gauge :
    ∀ v, v ∈ gauge → projector v = 0
  action_differentiable :
    DifferentiableAt ℝ F.action background
  gradient : E → E
  gradient_represents_first_variation :
    ∀ u v,
      fderiv ℝ F.action u v = inner ℝ (gradient u) v
  hessian : E →L[ℝ] E
  hessian_is_gradient_derivative :
    HasFDerivAt gradient hessian background
  hessian_selfAdjoint :
    ∀ u v, inner ℝ (hessian u) v = inner ℝ u (hessian v)

/-- Estacionariedade restrita às variações admissíveis. -/
def PhysicalHessianData.IsStationary
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) : Prop :=
  ∀ v, v ∈ H.admissible →
    fderiv ℝ F.action H.background v = 0

/-- Operador Hessiano comprimido ao setor físico. -/
noncomputable def PhysicalHessianData.physicalHessian
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) : E →L[ℝ] E :=
  H.projector.comp (H.hessian.comp H.projector)

/-- Forma quadrática da segunda variação física. -/
noncomputable def PhysicalHessianData.secondVariation
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) (v : E) : ℝ :=
  inner ℝ v (H.physicalHessian v)

/-- Um gap físico positivo no setor projetado. -/
def PhysicalHessianData.HasPhysicalGap
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) (Δ : ℝ) : Prop :=
  0 < Δ ∧
    ∀ v, H.projector v = v →
      Δ * ‖v‖ ^ 2 ≤ H.secondVariation v

/-- Estabilidade estrita dos modos físicos não nulos. -/
def PhysicalHessianData.PhysicallyStable
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) : Prop :=
  ∀ v, H.projector v = v → v ≠ 0 →
    0 < H.secondVariation v

/-- Um gap positivo implica estabilidade física estrita. -/
theorem PhysicalHessianData.stable_of_gap
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) {Δ : ℝ}
    (hgap : H.HasPhysicalGap Δ) :
    H.PhysicallyStable := by
  intro v hv hne
  have hnorm : 0 < ‖v‖ ^ 2 := sq_pos_of_pos (norm_pos_iff.mpr hne)
  exact lt_of_lt_of_le (mul_pos hgap.1 hnorm) (hgap.2 v hv)

/-- O Hessiano físico elimina automaticamente todo modo de gauge. -/
theorem PhysicalHessianData.physicalHessian_kills_gauge
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F)
    (v : E) (hv : v ∈ H.gauge) :
    H.physicalHessian v = 0 := by
  simp [PhysicalHessianData.physicalHessian,
    H.projector_kills_gauge v hv]

end GDQ
