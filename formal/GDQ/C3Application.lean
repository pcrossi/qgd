import GDQ.SpectralBridge
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

namespace GDQ

open scoped BigOperators

/-!
# Aplicação à classe estacionária `C₃`

Este módulo formaliza a remoção do modo comum dos três centros e a fórmula do
gap físico reduzido. O valor `1/2` é provado, não inserido como campo de uma
estrutura.
-/

/-- Espaço real dos três modos de centro. -/
abbrev ThreeCenterMode := Fin 3 → ℝ

/-- Média do modo comum. -/
noncomputable def threeCenterMean (v : ThreeCenterMode) : ℝ :=
  (∑ i, v i) / 3

/-- Projetor algébrico que remove a rotação comum. -/
noncomputable def relativeThreeCenterProjector
    (v : ThreeCenterMode) : ThreeCenterMode :=
  fun i => v i - threeCenterMean v

/-- A imagem do projetor relativo possui soma nula. -/
theorem relativeThreeCenterProjector_sum_zero
    (v : ThreeCenterMode) :
    ∑ i, relativeThreeCenterProjector v i = 0 := by
  simp [relativeThreeCenterProjector, threeCenterMean]
  ring_nf

/-- Remover duas vezes o modo comum é igual a removê-lo uma vez. -/
theorem relativeThreeCenterProjector_idempotent
    (v : ThreeCenterMode) :
    relativeThreeCenterProjector
      (relativeThreeCenterProjector v) =
      relativeThreeCenterProjector v := by
  funext i
  simp [relativeThreeCenterProjector, threeCenterMean]
  ring_nf

/--
Gap reduzido da classe `C₃`.

`κT2` abrevia o produto positivo `κ_rel T²`.
-/
noncomputable def c3PhysicalGap (κT2 τ : ℝ) : ℝ :=
  min ((3 / 2 : ℝ) * κT2) (1 / (2 * τ))

/-- O gap `C₃` é positivo quando rigidez relativa e fluxo são positivos. -/
theorem c3PhysicalGap_pos
    {κT2 τ : ℝ} (hκ : 0 < κT2) (hτ : 0 < τ) :
    0 < c3PhysicalGap κT2 τ := by
  rw [c3PhysicalGap, lt_min_iff]
  constructor
  · positivity
  · positivity

/-- Na normalização primitiva, o menor nível físico é exatamente `1/2`. -/
theorem c3PhysicalGap_primitive :
    c3PhysicalGap 1 1 = (1 / 2 : ℝ) := by
  norm_num [c3PhysicalGap, min_eq_right]

/--
Certificado físico mínimo da classe estacionária de três centros.

Ele não afirma que todo background GDQ pertence a `C₃`.
-/
structure C3StationaryBackgroundCertificate where
  κT2 : ℝ
  τ : ℝ
  κT2_pos : 0 < κT2
  τ_pos : 0 < τ
  officialStationaryBackground : Prop
  officialStationaryBackground_proof : officialStationaryBackground
  noetherAndGaugeModesRemoved : Prop
  noetherAndGaugeModesRemoved_proof : noetherAndGaugeModesRemoved

/--
Ligação explícita entre o background `C₃` e a segunda variação da ação
oficial. A desigualdade de coercividade é uma obrigação a ser demonstrada
para os campos concretos, não uma consequência do nome `C₃`.
-/
structure C3OfficialHessianCertificate
    {E : Type*}
    [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (F : OfficialActionVariationFamily E) where
  background : C3StationaryBackgroundCertificate
  hessianData : PhysicalHessianData F
  stationary : hessianData.IsStationary
  coerciveOnPhysicalSector :
    ∀ v, hessianData.projector v = v →
      c3PhysicalGap background.κT2 background.τ * ‖v‖ ^ 2 ≤
        hessianData.secondVariation v

/-- O certificado `C₃` produz um gap local estritamente positivo. -/
theorem C3StationaryBackgroundCertificate.has_positive_gap
    (C : C3StationaryBackgroundCertificate) :
    0 < c3PhysicalGap C.κT2 C.τ :=
  c3PhysicalGap_pos C.κT2_pos C.τ_pos

/-- O certificado Hessiano `C₃` fornece o predicado de gap físico oficial. -/
theorem C3OfficialHessianCertificate.has_official_physical_gap
    {E : Type*}
    [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    {F : OfficialActionVariationFamily E}
    (C : C3OfficialHessianCertificate F) :
    C.hessianData.HasPhysicalGap
      (c3PhysicalGap C.background.κT2 C.background.τ) := by
  exact ⟨C.background.has_positive_gap, C.coerciveOnPhysicalSector⟩

/-- Consequentemente, o background certificado é fisicamente estável. -/
theorem C3OfficialHessianCertificate.is_physically_stable
    {E : Type*}
    [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    {F : OfficialActionVariationFamily E}
    (C : C3OfficialHessianCertificate F) :
    C.hessianData.PhysicallyStable :=
  C.hessianData.stable_of_gap C.has_official_physical_gap

/--
Aplicação dos seis lemas a `C₃`.

Os certificados analíticos de Mosco/Agmon/Riesz permanecem visíveis no
argumento `B`; o cálculo `C₃` fornece a positividade local que os alimenta.
-/
theorem c3_bridge_applies
    {X E : Type*}
    [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (C : C3StationaryBackgroundCertificate)
    (B : SixLemmaBridgeData X E) :
    0 < c3PhysicalGap C.κT2 C.τ ∧
      SixLemmaBridgeConclusion B := by
  exact ⟨C.has_positive_gap, six_lemma_bridge B⟩

end GDQ
