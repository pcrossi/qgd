import GDQ.VariationalHessian
import Mathlib.Analysis.InnerProductSpace.Projection.Basic

namespace GDQ

/-!
# Projetor físico ortogonal e Hessiana comprimida

O espaço físico é construído, e não postulado, como

`V_phys = V_adm ∩ Gᗮ`,

onde `V_adm` contém as variações que respeitam os vínculos linearizados e
`G` contém as direções de gauge. Quando esse subespaço admite projeção
ortogonal, a Mathlib fornece um projetor contínuo canônico.

Em dimensão finita a hipótese de existência é automática. Em dimensão
infinita ela corresponde à completude/fechamento do subespaço físico e
permanece uma obrigação analítica do background.
-/

variable
  {E : Type*}
  [NormedAddCommGroup E]
  [InnerProductSpace ℝ E]

/-- Dados dos subespaços admissível e de gauge, com projeção física existente. -/
structure OrthogonalPhysicalSector (E : Type*)
    [NormedAddCommGroup E] [InnerProductSpace ℝ E] where
  admissible : Submodule ℝ E
  gauge : Submodule ℝ E
  hasOrthogonalProjection :
    (admissible ⊓ gaugeᗮ).HasOrthogonalProjection

/--
Em dimensão finita, o projetor conjunto existe automaticamente para quaisquer
subespaços admissível e de gauge.
-/
noncomputable def finiteDimensionalOrthogonalPhysicalSector
    [FiniteDimensional ℝ E]
    (admissible gauge : Submodule ℝ E) :
    OrthogonalPhysicalSector E where
  admissible := admissible
  gauge := gauge
  hasOrthogonalProjection := by infer_instance

/--
Construtor finito-dimensional a partir do operador linearizado dos vínculos.
O espaço admissível é `ker C`; nenhuma equação proibida é projetada de volta
ao setor físico.
-/
noncomputable def finiteDimensionalConstrainedPhysicalSector
    {Y : Type*}
    [NormedAddCommGroup Y] [NormedSpace ℝ Y]
    [FiniteDimensional ℝ E]
    (constraintLinearization : E →L[ℝ] Y)
    (gauge : Submodule ℝ E) :
    OrthogonalPhysicalSector E :=
  finiteDimensionalOrthogonalPhysicalSector
    constraintLinearization.ker gauge

/-- Interseção das variações admissíveis com o complemento do gauge. -/
noncomputable def OrthogonalPhysicalSector.physicalSubspace
    (S : OrthogonalPhysicalSector E) : Submodule ℝ E :=
  S.admissible ⊓ S.gaugeᗮ

/-- Projetor ortogonal canônico sobre o espaço físico conjunto. -/
noncomputable def OrthogonalPhysicalSector.projector
    (S : OrthogonalPhysicalSector E) : E →L[ℝ] E := by
  letI : S.physicalSubspace.HasOrthogonalProjection := by
    simpa [OrthogonalPhysicalSector.physicalSubspace] using
      S.hasOrthogonalProjection
  exact S.physicalSubspace.starProjection

/-- A imagem do projetor pertence ao espaço físico. -/
theorem OrthogonalPhysicalSector.projector_mem_physical
    (S : OrthogonalPhysicalSector E) (v : E) :
    S.projector v ∈ S.physicalSubspace := by
  letI : S.physicalSubspace.HasOrthogonalProjection := by
    simpa [OrthogonalPhysicalSector.physicalSubspace] using
      S.hasOrthogonalProjection
  change S.physicalSubspace.starProjection v ∈ S.physicalSubspace
  exact Submodule.starProjection_apply_mem S.physicalSubspace v

/-- A imagem do projetor satisfaz todos os vínculos admissíveis. -/
theorem OrthogonalPhysicalSector.projector_mem_admissible
    (S : OrthogonalPhysicalSector E) (v : E) :
    S.projector v ∈ S.admissible :=
  (S.projector_mem_physical v).1

/-- A imagem é ortogonal a todas as direções de gauge. -/
theorem OrthogonalPhysicalSector.projector_mem_gauge_orthogonal
    (S : OrthogonalPhysicalSector E) (v : E) :
    S.projector v ∈ S.gaugeᗮ :=
  (S.projector_mem_physical v).2

/-- O projetor físico é idempotente. -/
theorem OrthogonalPhysicalSector.projector_idempotent
    (S : OrthogonalPhysicalSector E) (v : E) :
    S.projector (S.projector v) = S.projector v := by
  letI : S.physicalSubspace.HasOrthogonalProjection := by
    simpa [OrthogonalPhysicalSector.physicalSubspace] using
      S.hasOrthogonalProjection
  change
    S.physicalSubspace.starProjection
      (S.physicalSubspace.starProjection v) =
        S.physicalSubspace.starProjection v
  exact S.physicalSubspace.starProjection_eq_self_iff.mpr
    (S.projector_mem_physical v)

/-- O projetor físico é autoadjunto. -/
theorem OrthogonalPhysicalSector.projector_selfAdjoint
    (S : OrthogonalPhysicalSector E) (u v : E) :
    inner ℝ (S.projector u) v = inner ℝ u (S.projector v) := by
  letI : S.physicalSubspace.HasOrthogonalProjection := by
    simpa [OrthogonalPhysicalSector.physicalSubspace] using
      S.hasOrthogonalProjection
  change
    inner ℝ (S.physicalSubspace.starProjection u) v =
      inner ℝ u (S.physicalSubspace.starProjection v)
  exact S.physicalSubspace.inner_starProjection_left_eq_right u v

/-- Toda direção de gauge é anulada pelo projetor conjunto. -/
theorem OrthogonalPhysicalSector.projector_kills_gauge
    (S : OrthogonalPhysicalSector E) (v : E) (hv : v ∈ S.gauge) :
    S.projector v = 0 := by
  letI : S.physicalSubspace.HasOrthogonalProjection := by
    simpa [OrthogonalPhysicalSector.physicalSubspace] using
      S.hasOrthogonalProjection
  change S.physicalSubspace.starProjection v = 0
  rw [Submodule.starProjection_apply_eq_zero_iff]
  rw [Submodule.mem_orthogonal]
  intro w hw
  have hwGaugeOrthogonal : w ∈ S.gaugeᗮ := hw.2
  exact inner_eq_zero_symm.mpr
    ((S.gauge.mem_orthogonal w).mp hwGaugeOrthogonal v hv)

/-- Vetores fixos pelo projetor são exatamente as variações físicas. -/
theorem OrthogonalPhysicalSector.projector_eq_self_iff
    (S : OrthogonalPhysicalSector E) (v : E) :
    S.projector v = v ↔ v ∈ S.physicalSubspace := by
  letI : S.physicalSubspace.HasOrthogonalProjection := by
    simpa [OrthogonalPhysicalSector.physicalSubspace] using
      S.hasOrthogonalProjection
  change S.physicalSubspace.starProjection v = v ↔
    v ∈ S.physicalSubspace
  exact S.physicalSubspace.starProjection_eq_self_iff

/--
Dados variacionais em que o projetor não é um campo independente: ele será
construído canonicamente a partir de `sector`.
-/
structure OrthogonallyProjectedHessianData
    (F : OfficialActionVariationFamily E) where
  sector : OrthogonalPhysicalSector E
  background : E
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

/-- Constrói `PhysicalHessianData` sem assumir separadamente um projetor. -/
noncomputable def OrthogonallyProjectedHessianData.toPhysicalHessianData
    {F : OfficialActionVariationFamily E}
    (D : OrthogonallyProjectedHessianData F) :
    PhysicalHessianData F where
  background := D.background
  admissible := D.sector.admissible
  gauge := D.sector.gauge
  projector := D.sector.projector
  projector_idempotent := D.sector.projector_idempotent
  projector_selfAdjoint := D.sector.projector_selfAdjoint
  projector_range_admissible := D.sector.projector_mem_admissible
  projector_kills_gauge := D.sector.projector_kills_gauge
  action_differentiable := D.action_differentiable
  gradient := D.gradient
  gradient_represents_first_variation :=
    D.gradient_represents_first_variation
  hessian := D.hessian
  hessian_is_gradient_derivative := D.hessian_is_gradient_derivative
  hessian_selfAdjoint := D.hessian_selfAdjoint

/-- A compressão `P H P` de uma Hessiana autoadjunta é autoadjunta. -/
theorem PhysicalHessianData.physicalHessian_selfAdjoint
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) (u v : E) :
    inner ℝ (H.physicalHessian u) v =
      inner ℝ u (H.physicalHessian v) := by
  change
    inner ℝ (H.projector (H.hessian (H.projector u))) v =
      inner ℝ u (H.projector (H.hessian (H.projector v)))
  rw [H.projector_selfAdjoint]
  rw [H.hessian_selfAdjoint]
  rw [H.projector_selfAdjoint]

/-- Em vetores físicos, a forma comprimida coincide com a forma Hessiana bruta. -/
theorem PhysicalHessianData.secondVariation_eq_raw_of_physical
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) (v : E)
    (hv : H.projector v = v) :
    H.secondVariation v = inner ℝ v (H.hessian v) := by
  unfold PhysicalHessianData.secondVariation
  rw [PhysicalHessianData.physicalHessian,
    ContinuousLinearMap.comp_apply, ContinuousLinearMap.comp_apply, hv]
  rw [← H.projector_selfAdjoint]
  rw [hv]

/-- Coercividade da Hessiana bruta restrita ao setor físico. -/
def PhysicalHessianData.RawCoerciveOnPhysical
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) (Δ : ℝ) : Prop :=
  ∀ v, H.projector v = v →
    Δ * ‖v‖ ^ 2 ≤ inner ℝ v (H.hessian v)

/-- Coercividade restrita positiva fornece o gap da Hessiana comprimida. -/
theorem PhysicalHessianData.hasPhysicalGap_of_rawCoercive
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) {Δ : ℝ}
    (hΔ : 0 < Δ)
    (hcoercive : H.RawCoerciveOnPhysical Δ) :
    H.HasPhysicalGap Δ := by
  refine ⟨hΔ, ?_⟩
  intro v hv
  rw [H.secondVariation_eq_raw_of_physical v hv]
  exact hcoercive v hv

end GDQ
