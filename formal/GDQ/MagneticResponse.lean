import GDQ.SternGerlachInterface
import Mathlib.Tactic

namespace GDQ

/-!
# Resposta magnética reduzida da GDQ

Este módulo certifica a camada algébrica fechada do Capítulo 16:

* a normalização mínima `γ₀ = q/(mc)` implica `g₀ = 2`;
* a norma do representante harmônico unitário do ciclo de comprimento `2π`
  vale `1/(2π)`;
* o termo líder correspondente é `α/(2π)`;
* a fonte protegida por Noether e a fonte transversal separam-se na resposta
  da Hessiana vinculada;
* o bloco Hessiano reduzido usado como verificador realiza exatamente a
  resposta `α/(2π)`.

O módulo não deriva a normalização cosmológica de `α`, não constrói a sela
leptônica 8D e não calcula os canais superiores de `g-2`. Em particular, o
bloco líder abaixo é uma realização reduzida do termo já identificado, não
uma prova de que toda Hessiana física da ação oficial tenha essa matriz.
-/

/-- Fator `g` associado a uma razão giromagnética `γ`. -/
noncomputable def magneticGFactor
    (q mass lightSpeed γ : ℝ) : ℝ :=
  2 * mass * lightSpeed * γ / q

/--
A razão giromagnética mínima `q/(mc)` reproduz exatamente `g₀ = 2`, desde que
carga, massa e velocidade de conversão sejam não nulas.
-/
theorem magneticGFactor_minimal_eq_two
    {q mass lightSpeed : ℝ}
    (hq : q ≠ 0) (hmass : mass ≠ 0) (hc : lightSpeed ≠ 0) :
    magneticGFactor q mass lightSpeed
        (q / (mass * lightSpeed)) = 2 := by
  unfold magneticGFactor
  field_simp [hq, hmass, hc]

/--
Norma quadrática do representante constante de período unitário num ciclo de
comprimento `2π`: comprimento vezes densidade quadrática.
-/
noncomputable def unitHarmonicCircleNormSq : ℝ :=
  (2 * Real.pi) * (1 / (2 * Real.pi)) ^ 2

/-- A norma harmônica unitária no ciclo vale `1/(2π)`. -/
theorem unitHarmonicCircleNormSq_eq :
    unitHarmonicCircleNormSq = 1 / (2 * Real.pi) := by
  unfold unitHarmonicCircleNormSq
  field_simp [Real.pi_ne_zero]

/-- Termo líder geométrico da anomalia no setor reduzido. -/
noncomputable def leadingMagneticAnomaly (alpha : ℝ) : ℝ :=
  alpha * unitHarmonicCircleNormSq

/-- A projeção harmônica reduz-se exatamente a `α/(2π)`. -/
theorem leadingMagneticAnomaly_eq
    (alpha : ℝ) :
    leadingMagneticAnomaly alpha = alpha / (2 * Real.pi) := by
  rw [leadingMagneticAnomaly, unitHarmonicCircleNormSq_eq]
  ring

/-- Fator `g` reconstruído a partir de uma anomalia `a`. -/
def magneticGFromAnomaly (a : ℝ) : ℝ := 2 * (1 + a)

/-- Fórmula líder do fator magnético reduzido. -/
theorem magneticGFromLeadingAnomaly_eq
    (alpha : ℝ) :
    magneticGFromAnomaly (leadingMagneticAnomaly alpha) =
      2 * (1 + alpha / (2 * Real.pi)) := by
  rw [leadingMagneticAnomaly_eq]
  rfl

/--
Anomalia transversal definida pela resposta escalar da Hessiana vinculada.
Esta é a versão escalar da contração
`⟨c,H⁺m⊥⟩ /(γ₀⟨c,H⁺c⟩)`.
-/
noncomputable def constrainedMagneticAnomaly
    (c inverseHessian γ₀ mPerp : ℝ) : ℝ :=
  noetherZeemanEffectiveRatio c inverseHessian mPerp / γ₀

/--
A fonte `m = γ₀c + m⊥` separa exatamente a resposta protegida da anomalia
transversal.
-/
theorem effectiveMagneticRatio_eq_minimal_plus_anomaly
    (c inverseHessian γ₀ mPerp : ℝ)
    (hden : c * inverseHessian * c ≠ 0)
    (hγ : γ₀ ≠ 0) :
    noetherZeemanEffectiveRatio c inverseHessian
        (γ₀ * c + mPerp) =
      γ₀ * (1 +
        constrainedMagneticAnomaly c inverseHessian γ₀ mPerp) := by
  rw [noetherZeemanEffectiveRatio_decomposition c inverseHessian γ₀ mPerp hden]
  unfold constrainedMagneticAnomaly
  field_simp [hγ]

/-- Rigidez transversal escolhida no verificador Hessiano líder. -/
noncomputable def leadingTransverseRigidity (alpha : ℝ) : ℝ :=
  2 * Real.pi / alpha

/--
Resposta do bloco líder depois de inverter
`[[1,-1],[-1,K]]`: a razão relevante é
`(1/(K-1))/(K/(K-1))`.
-/
noncomputable def leadingBlockResponse (alpha : ℝ) : ℝ :=
  let K := leadingTransverseRigidity alpha
  (1 / (K - 1)) / (K / (K - 1))

/--
O bloco líder realiza `α/(2π)` quando é inversível. Isso certifica a álgebra
do verificador, não deriva o bloco a partir de uma sela 8D.
-/
theorem leadingBlockResponse_eq
    {alpha : ℝ}
    (halpha : alpha ≠ 0)
    (hinv : 2 * Real.pi / alpha ≠ 1) :
    leadingBlockResponse alpha = alpha / (2 * Real.pi) := by
  unfold leadingBlockResponse leadingTransverseRigidity
  dsimp
  have hpi : Real.pi ≠ 0 := Real.pi_ne_zero
  have hK : 2 * Real.pi / alpha ≠ 0 := by
    exact div_ne_zero (mul_ne_zero (by norm_num) hpi) halpha
  have hKsub : 2 * Real.pi / alpha - 1 ≠ 0 := sub_ne_zero.mpr hinv
  have hdiff : 2 * Real.pi - alpha ≠ 0 := by
    intro hz
    apply hinv
    apply (div_eq_one_iff_eq halpha).2
    linarith
  field_simp [halpha, hpi, hK, hKsub, hdiff]

/--
Uma fonte superior diretamente ortogonal ao modo harmônico não contribui à
resposta linear protegida.
-/
theorem directOrthogonalChannel_vanishes
    {overlap coupling : ℝ}
    (hortho : overlap = 0) :
    coupling * overlap = 0 := by
  simp [hortho]

end GDQ
