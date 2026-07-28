import GDQ.ConformalTorsionHessian
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

namespace GDQ

noncomputable section

/-!
# Estabilidade eletrofraca geométrica no setor reduzido

Este módulo formaliza somente a camada algébrica já demonstrada no Capítulo 19.
Ele não postula um potencial de Higgs fundamental. O potencial abaixo é a
restrição quartica da ação oficial a uma direção física previamente escolhida.

As entradas `a₂` e `a₄` são coeficientes da segunda e da quarta variações no
background declarado. O módulo prova o que decorre de seus sinais, mas não
atribui valores físicos a eles.
-/

/-! ## 1. Quártica de interface a volume fixo -/

/-- Coeficiente quadrático da expansão da área radial antes do vínculo. -/
def interfaceAreaQuadraticCoeff : ℝ := 9 / 8

/-- Coeficiente quártico da expansão da área radial antes do vínculo. -/
def interfaceAreaQuarticCoeff : ℝ := -5 / 64

/-- Coeficiente quadrático da expansão do volume. -/
def interfaceVolumeQuadraticCoeff : ℝ := 3 / 2

/-- Coeficiente quártico da expansão do volume. -/
def interfaceVolumeQuarticCoeff : ℝ := 1 / 8

/-- Expoente que restaura o volume de uma interface tridimensional. -/
def fixedVolumeScaleExponent : ℝ := -3 / 4

/-- Coeficiente quadrático de `(Vε/V₀)^(-3/4)`. -/
def fixedVolumeScaleQuadraticCoeff : ℝ :=
  fixedVolumeScaleExponent * interfaceVolumeQuadraticCoeff

/-- Coeficiente quártico de `(Vε/V₀)^(-3/4)`. -/
def fixedVolumeScaleQuarticCoeff : ℝ :=
  fixedVolumeScaleExponent * interfaceVolumeQuarticCoeff
    + fixedVolumeScaleExponent * (fixedVolumeScaleExponent - 1) / 2
      * interfaceVolumeQuadraticCoeff ^ 2

theorem fixedVolumeScaleQuadraticCoeff_eq :
    fixedVolumeScaleQuadraticCoeff = -9 / 8 := by
  norm_num [fixedVolumeScaleQuadraticCoeff, fixedVolumeScaleExponent,
    interfaceVolumeQuadraticCoeff]

theorem fixedVolumeScaleQuarticCoeff_eq :
    fixedVolumeScaleQuarticCoeff = 177 / 128 := by
  norm_num [fixedVolumeScaleQuarticCoeff, fixedVolumeScaleExponent,
    interfaceVolumeQuadraticCoeff, interfaceVolumeQuarticCoeff]

/-- Coeficiente quadrático após multiplicar área e correção de escala. -/
def fixedVolumeAreaQuadraticCoeff : ℝ :=
  interfaceAreaQuadraticCoeff + fixedVolumeScaleQuadraticCoeff

/-- Coeficiente quártico após multiplicar área e correção de escala. -/
def fixedVolumeAreaQuarticCoeff : ℝ :=
  interfaceAreaQuarticCoeff
    + fixedVolumeScaleQuarticCoeff
    + interfaceAreaQuadraticCoeff * fixedVolumeScaleQuadraticCoeff

/-- O vínculo de volume cancela exatamente a penalidade quadrática da área. -/
theorem fixedVolumeAreaQuadraticCoeff_eq_zero :
    fixedVolumeAreaQuadraticCoeff = 0 := by
  norm_num [fixedVolumeAreaQuadraticCoeff, interfaceAreaQuadraticCoeff,
    fixedVolumeScaleQuadraticCoeff, fixedVolumeScaleExponent,
    interfaceVolumeQuadraticCoeff]

/-- A primeira penalidade sobrevivente é quártica e tem coeficiente `5/128`. -/
theorem fixedVolumeAreaQuarticCoeff_eq :
    fixedVolumeAreaQuarticCoeff = 5 / 128 := by
  rw [fixedVolumeAreaQuarticCoeff, fixedVolumeScaleQuadraticCoeff_eq,
    fixedVolumeScaleQuarticCoeff_eq]
  norm_num [interfaceAreaQuadraticCoeff, interfaceAreaQuarticCoeff]

theorem fixedVolumeAreaQuarticCoeff_pos :
    0 < fixedVolumeAreaQuarticCoeff := by
  rw [fixedVolumeAreaQuarticCoeff_eq]
  norm_num

/-! ## 2. Potencial restrito e mínimos não triviais -/

/--
Parte não constante da expansão restrita

`S_eff(β) = S₀ + (a₂/2) β² + (a₄/4) β⁴`.
-/
def electroweakQuarticPotential (a₂ a₄ β : ℝ) : ℝ :=
  a₂ / 2 * β ^ 2 + a₄ / 4 * β ^ 4

/-- Completação exata do quadrado para a quártica reduzida. -/
theorem electroweakQuarticPotential_completeSquare
    {a₂ a₄ β : ℝ} (ha₄ : a₄ ≠ 0) :
    electroweakQuarticPotential a₂ a₄ β =
      a₄ / 4 * (β ^ 2 + a₂ / a₄) ^ 2
        - a₂ ^ 2 / (4 * a₄) := by
  unfold electroweakQuarticPotential
  field_simp [ha₄]
  ring

/--
Se `a₄ > 0`, a forma completada fornece uma cota inferior global.
-/
theorem electroweakQuarticPotential_lowerBound
    {a₂ a₄ β : ℝ} (ha₄ : 0 < a₄) :
    -a₂ ^ 2 / (4 * a₄) ≤ electroweakQuarticPotential a₂ a₄ β := by
  rw [electroweakQuarticPotential_completeSquare ha₄.ne']
  have hnonneg :
      0 ≤ a₄ / 4 * (β ^ 2 + a₂ / a₄) ^ 2 :=
    mul_nonneg (by positivity) (sq_nonneg _)
  have hshift :=
    sub_le_sub_right hnonneg (a₂ ^ 2 / (4 * a₄))
  convert hshift using 1
  · ring

/-- A relação `β²=-a₂/a₄` satura a cota global. -/
theorem electroweakQuarticPotential_eq_lowerBound
    {a₂ a₄ β : ℝ} (ha₄ : a₄ ≠ 0)
    (hβ : β ^ 2 = -a₂ / a₄) :
    electroweakQuarticPotential a₂ a₄ β =
      -a₂ ^ 2 / (4 * a₄) := by
  rw [electroweakQuarticPotential_completeSquare ha₄, hβ]
  ring

/--
Quando `a₂ < 0 < a₄`, existe uma amplitude positiva que satisfaz
`β²=-a₂/a₄`.
-/
theorem exists_positive_electroweakAmplitude
    {a₂ a₄ : ℝ} (ha₂ : a₂ < 0) (ha₄ : 0 < a₄) :
    ∃ β : ℝ, 0 < β ∧ β ^ 2 = -a₂ / a₄ := by
  have hratio : 0 < -a₂ / a₄ := div_pos (neg_pos.mpr ha₂) ha₄
  refine ⟨Real.sqrt (-a₂ / a₄), Real.sqrt_pos.2 hratio, ?_⟩
  exact Real.sq_sqrt hratio.le

/-- A quártica reduzida é par sob reversão da amplitude. -/
theorem electroweakQuarticPotential_neg (a₂ a₄ β : ℝ) :
    electroweakQuarticPotential a₂ a₄ (-β) =
      electroweakQuarticPotential a₂ a₄ β := by
  unfold electroweakQuarticPotential
  ring

/-- Sob os sinais físicos, os dois ramos `±β` saturam a cota global. -/
theorem exists_two_electroweakMinima
    {a₂ a₄ : ℝ} (ha₂ : a₂ < 0) (ha₄ : 0 < a₄) :
    ∃ β : ℝ, 0 < β
      ∧ electroweakQuarticPotential a₂ a₄ β =
          -a₂ ^ 2 / (4 * a₄)
      ∧ electroweakQuarticPotential a₂ a₄ (-β) =
          -a₂ ^ 2 / (4 * a₄) := by
  obtain ⟨β, hβpos, hβsq⟩ :=
    exists_positive_electroweakAmplitude ha₂ ha₄
  refine ⟨β, hβpos, ?_, ?_⟩
  · exact electroweakQuarticPotential_eq_lowerBound ha₄.ne' hβsq
  · rw [electroweakQuarticPotential_neg]
    exact electroweakQuarticPotential_eq_lowerBound ha₄.ne' hβsq

/--
O mínimo não trivial tem energia estritamente menor que o ponto simétrico.
-/
theorem brokenMinimum_below_symmetricPoint
    {a₂ a₄ β : ℝ} (ha₂ : a₂ < 0) (ha₄ : 0 < a₄)
    (hβ : β ^ 2 = -a₂ / a₄) :
    electroweakQuarticPotential a₂ a₄ β
      < electroweakQuarticPotential a₂ a₄ 0 := by
  rw [electroweakQuarticPotential_eq_lowerBound ha₄.ne' hβ]
  unfold electroweakQuarticPotential
  have ha₂sq : 0 < a₂ ^ 2 := sq_pos_of_ne_zero ha₂.ne
  have hden : 0 < 4 * a₄ := mul_pos (by norm_num) ha₄
  have hnegative : -a₂ ^ 2 / (4 * a₄) < 0 :=
    div_neg_of_neg_of_pos (neg_neg_of_pos ha₂sq) hden
  simpa [electroweakQuarticPotential] using hnegative

/-! ## 3. Complemento de Schur da interface eletromagnética -/

/-- Rigidez efetiva depois de eliminar o traço interno da interface. -/
def electromagneticInterfaceSchur (k₀ kBoundary : ℝ) : ℝ :=
  kBoundary - kBoundary ^ 2 / (k₀ + kBoundary)

theorem electromagneticInterfaceSchur_eq
    {k₀ kBoundary : ℝ} (hsum : k₀ + kBoundary ≠ 0) :
    electromagneticInterfaceSchur k₀ kBoundary =
      k₀ * kBoundary / (k₀ + kBoundary) := by
  unfold electromagneticInterfaceSchur
  field_simp [hsum]
  ring

theorem electromagneticInterfaceSchur_pos
    {k₀ kBoundary : ℝ} (hk₀ : 0 < k₀) (hkBoundary : 0 < kBoundary) :
    0 < electromagneticInterfaceSchur k₀ kBoundary := by
  rw [electromagneticInterfaceSchur_eq
    (ne_of_gt (add_pos hk₀ hkBoundary))]
  exact div_pos (mul_pos hk₀ hkBoundary) (add_pos hk₀ hkBoundary)

/-! ## 4. Kernel neutro e modo massivo -/

/--
Ação do bloco neutro sem o fator positivo global `v²/4`:

`[[g²,-g g'],[-g g',g'²]]`.
-/
def neutralMassBlockAction (g g' x y : ℝ) : ℝ × ℝ :=
  (g ^ 2 * x - g * g' * y, -g * g' * x + g' ^ 2 * y)

/-- O vetor `(g',g)` pertence exatamente ao kernel: é o modo do fóton. -/
theorem neutralMassBlock_photonKernel (g g' : ℝ) :
    neutralMassBlockAction g g' g' g = (0, 0) := by
  unfold neutralMassBlockAction
  apply Prod.ext <;> simp <;> ring

/-- O vetor ortogonal `(g,-g')` tem autovalor `g²+g'²`. -/
theorem neutralMassBlock_massiveMode (g g' : ℝ) :
    neutralMassBlockAction g g' g (-g') =
      ((g ^ 2 + g' ^ 2) * g, (g ^ 2 + g' ^ 2) * (-g')) := by
  unfold neutralMassBlockAction
  apply Prod.ext <;> simp <;> ring

/-- O autovalor do modo massivo é positivo se algum acoplamento é não nulo. -/
theorem neutralMassiveEigenvalue_pos
    {g g' : ℝ} (h : g ≠ 0 ∨ g' ≠ 0) :
    0 < g ^ 2 + g' ^ 2 := by
  rcases h with hg | hg'
  · nlinarith [sq_pos_of_ne_zero hg, sq_nonneg g']
  · nlinarith [sq_nonneg g, sq_pos_of_ne_zero hg']

end

end GDQ
