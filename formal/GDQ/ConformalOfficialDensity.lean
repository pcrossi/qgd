import GDQ.ConformalBismutInvariants

namespace GDQ

/-!
# Densidade da ação oficial no background material torsional

Esta camada insere somente os invariantes já derivados na densidade da ação
oficial. Em particular, não adiciona um termo separado `|H|²`: a torção entra
pela conexão de Bismut e por sua curvatura escalar, em conformidade com a ação
oficial preservada.
-/

/-- Densidade pontual oficial no background material torsional. -/
noncomputable def conformalMaterialOfficialDensity
    (ℏ ΛC a τ f₀ : ℝ)
    (zτ : ℝ → ℝ) (t : ℝ) (x : LocalPoint) : ℝ :=
  euclideanOfficialDensity ℏ ΛC
    (conformalMaterialAdmissible a τ f₀)
    (conformalBismutInvariants a τ f₀)
    zτ t x

/--
Expansão exata da densidade torsional oficial.

Os três fatores geométricos novos são derivados:

* `Rᴮ=-60 a² e^{-2φ}`;
* `|∇f|²=e^{-2φ}|∇f|²_flat`;
* `sqrt(det g)=e^{8φ}`.
-/
theorem conformalMaterialOfficialDensity_eq
    (ℏ ΛC a τ f₀ : ℝ)
    (zτ : ℝ → ℝ) (t : ℝ) (x : LocalPoint) :
    conformalMaterialOfficialDensity ℏ ΛC a τ f₀ zτ t x =
      (ℏ / ΛC ^ 2) *
        (zτ t *
            (-60 * a ^ 2 * (conformalScale a x)⁻¹ +
              (conformalScale a x)⁻¹ *
                gaussianGradientNormSq τ x.1) +
          gaussianPotentialRe τ f₀ x.1 - 4) *
        euclideanFlowKernel 4
          (gaussianDensity τ f₀ x.1) (zτ t) *
        (conformalScale a x) ^ 4 := by
  rw [conformalMaterialOfficialDensity,
    euclideanOfficialDensity_unfold]
  rw [conformalBismutInvariants_scalarCurvature,
    conformalBismutInvariants_gradientNormSq,
    conformalBismutInvariants_volumeDensity]
  change
    (ℏ / ΛC ^ 2) *
        (zτ t *
            (-60 * a ^ 2 * (conformalScale a x)⁻¹ +
              (conformalScale a x)⁻¹ *
                gaussianGradientNormSq τ x.1) +
          gaussianPotentialRe τ f₀ x.1 - 4) *
        euclideanFlowKernel 4
          (gaussianDensity τ f₀ x.1) (zτ t) *
        conformalScale a x ^ 4 =
      _
  rfl

/--
A parcela geométrica `Rᴮ+|∇f|²` possui um fator inverso conforme comum.
-/
theorem conformalMaterial_geometricBracket_factor
    (a τ : ℝ) (x : LocalPoint) :
    -60 * a ^ 2 * (conformalScale a x)⁻¹ +
        (conformalScale a x)⁻¹ * gaussianGradientNormSq τ x.1 =
      (conformalScale a x)⁻¹ *
        (gaussianGradientNormSq τ x.1 - 60 * a ^ 2) := by
  ring

end GDQ
