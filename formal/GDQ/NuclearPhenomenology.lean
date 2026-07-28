import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Tactic

namespace GDQ

noncomputable section

/-!
# Fenomenologia nuclear, Klein--Nishina e setor neutro

Este módulo formaliza somente o núcleo exato já demonstrado no Capítulo 24:

* positividade da meia-vida alfa reduzida;
* contagem aritmética das capacidades `2j+1` que produz os números mágicos;
* cinemática de Compton, positividade da razão `E'/E` e limite Thomson exato;
* limiar nuclear de produção de pares, positividade das taxas líderes de
  positrônio e do parâmetro magnético;
* positividade e ordenação do espectro neutro candidato;
* cotas probabilísticas da fórmula reduzida de oscilação em dois canais.

O módulo não postula uma Hessiana nuclear, um vértice Compton 8D ou os
coeficientes fenomenológicos do candidato de neutrinos. Esses objetos devem
ser avaliados no background físico antes de qualquer afirmação metrológica.
-/

/-! ## 1. Canal alfa reduzido -/

/-- Meia-vida reduzida após separar frequência de tentativa e expoente. -/
def alphaHalfLife (attemptFrequency exponent : ℝ) : ℝ :=
  Real.log 2 / attemptFrequency * Real.exp exponent

theorem alphaHalfLife_pos
    {attemptFrequency exponent : ℝ}
    (hν : 0 < attemptFrequency) :
    0 < alphaHalfLife attemptFrequency exponent := by
  unfold alphaHalfLife
  have hlog : 0 < Real.log 2 := Real.log_pos (by norm_num)
  positivity

theorem alphaHalfLife_monotone_in_exponent
    {attemptFrequency exponent₁ exponent₂ : ℝ}
    (hν : 0 < attemptFrequency) (hW : exponent₁ ≤ exponent₂) :
    alphaHalfLife attemptFrequency exponent₁
      ≤ alphaHalfLife attemptFrequency exponent₂ := by
  unfold alphaHalfLife
  have hlog : 0 ≤ Real.log 2 / attemptFrequency := by
    have : 0 < Real.log 2 := Real.log_pos (by norm_num)
    positivity
  exact mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr hW) hlog

/-! ## 2. Capacidades angulares e números mágicos -/

/-- Se `j2=2j`, a capacidade do subnível é `2j+1=j2+1`. -/
def angularCapacity (j2 : ℕ) : ℕ := j2 + 1

theorem reduced_magic_number_2 :
    angularCapacity 1 = 2 := by norm_num [angularCapacity]

theorem reduced_magic_number_8 :
    angularCapacity 1 + angularCapacity 3 + angularCapacity 1 = 8 := by
  norm_num [angularCapacity]

theorem reduced_magic_number_20 :
    angularCapacity 1 + angularCapacity 3 + angularCapacity 1
      + angularCapacity 5 + angularCapacity 1 + angularCapacity 3 = 20 := by
  norm_num [angularCapacity]

theorem reduced_magic_number_28 :
    20 + angularCapacity 7 = 28 := by
  norm_num [angularCapacity]

theorem reduced_magic_number_50 :
    28 + angularCapacity 3 + angularCapacity 5
      + angularCapacity 1 + angularCapacity 9 = 50 := by
  norm_num [angularCapacity]

theorem reduced_magic_number_82 :
    50 + angularCapacity 7 + angularCapacity 5
      + angularCapacity 3 + angularCapacity 1 + angularCapacity 11 = 82 := by
  norm_num [angularCapacity]

theorem reduced_magic_number_126 :
    82 + angularCapacity 9 + angularCapacity 7
      + angularCapacity 5 + angularCapacity 3
      + angularCapacity 1 + angularCapacity 13 = 126 := by
  norm_num [angularCapacity]

/-! ## 3. Cinemática de Compton e limite Thomson -/

/-- Razão cinemática `E'/E`, com `x=E/(mₑc²)`. -/
def comptonEnergyRatio (x theta : ℝ) : ℝ :=
  1 / (1 + x * (1 - Real.cos theta))

theorem comptonEnergyRatio_pos
    {x theta : ℝ} (hx : 0 ≤ x) :
    0 < comptonEnergyRatio x theta := by
  unfold comptonEnergyRatio
  have hcos : 0 ≤ 1 - Real.cos theta := sub_nonneg.mpr (Real.cos_le_one theta)
  have hden : 0 < 1 + x * (1 - Real.cos theta) := by positivity
  positivity

theorem comptonEnergyRatio_le_one
    {x theta : ℝ} (hx : 0 ≤ x) :
    comptonEnergyRatio x theta ≤ 1 := by
  unfold comptonEnergyRatio
  have hcos : 0 ≤ 1 - Real.cos theta := sub_nonneg.mpr (Real.cos_le_one theta)
  have hprod : 0 ≤ x * (1 - Real.cos theta) := mul_nonneg hx hcos
  have hden : 1 ≤ 1 + x * (1 - Real.cos theta) := by linarith
  simpa using one_div_le_one_div_of_le (show (0 : ℝ) < 1 by norm_num) hden

theorem comptonEnergyRatio_zero (theta : ℝ) :
    comptonEnergyRatio 0 theta = 1 := by
  simp [comptonEnergyRatio]

/-- Seção diferencial de Klein--Nishina em unidades de `rₑ²`. -/
def kleinNishinaNormalized (x theta : ℝ) : ℝ :=
  let r := comptonEnergyRatio x theta
  (1 / 2 : ℝ) * r ^ 2
    * (r + 1 / r - Real.sin theta ^ 2)

/-- Distribuição angular de Thomson em unidades de `rₑ²`. -/
def thomsonNormalized (theta : ℝ) : ℝ :=
  (1 / 2 : ℝ) * (1 + Real.cos theta ^ 2)

theorem kleinNishina_at_zero_eq_thomson (theta : ℝ) :
    kleinNishinaNormalized 0 theta = thomsonNormalized theta := by
  unfold kleinNishinaNormalized thomsonNormalized
  simp [comptonEnergyRatio]
  nlinarith [Real.sin_sq_add_cos_sq theta]

/-! ## 4. Produção e aniquilação de pares no setor reduzido -/

/--
Limiar de produção de um par por um fóton sobre um alvo inicialmente em
repouso. As entradas são energias de repouso, portanto possuem a mesma
dimensão.
-/
def nuclearPairThreshold
    (electronRestEnergy nucleusRestEnergy : ℝ) : ℝ :=
  2 * electronRestEnergy
    * (1 + electronRestEnergy / nucleusRestEnergy)

theorem nuclearPairThreshold_gt_free
    {electronRestEnergy nucleusRestEnergy : ℝ}
    (he : 0 < electronRestEnergy) (hN : 0 < nucleusRestEnergy) :
    2 * electronRestEnergy
      < nuclearPairThreshold electronRestEnergy nucleusRestEnergy := by
  unfold nuclearPairThreshold
  have hratio : 0 < electronRestEnergy / nucleusRestEnergy := div_pos he hN
  nlinarith

theorem nuclearPairThreshold_recoil
    {electronRestEnergy nucleusRestEnergy : ℝ}
    (hN : nucleusRestEnergy ≠ 0) :
    nuclearPairThreshold electronRestEnergy nucleusRestEnergy
        - 2 * electronRestEnergy
      =
      2 * electronRestEnergy ^ 2 / nucleusRestEnergy := by
  unfold nuclearPairThreshold
  field_simp [hN]
  ring

/-- Taxa líder do canal para-positrônio em unidades de frequência. -/
def paraPositroniumRate (alpha electronFrequency : ℝ) : ℝ :=
  (1 / 2 : ℝ) * alpha ^ 5 * electronFrequency

/-- Taxa líder do canal orto-positrônio em unidades de frequência. -/
def orthoPositroniumRate (alpha electronFrequency : ℝ) : ℝ :=
  2 * (Real.pi ^ 2 - 9) / (9 * Real.pi)
    * alpha ^ 6 * electronFrequency

theorem paraPositroniumRate_pos
    {alpha electronFrequency : ℝ}
    (hα : 0 < alpha) (hω : 0 < electronFrequency) :
    0 < paraPositroniumRate alpha electronFrequency := by
  unfold paraPositroniumRate
  positivity

theorem orthoPositroniumRate_pos
    {alpha electronFrequency : ℝ}
    (hα : 0 < alpha) (hω : 0 < electronFrequency) :
    0 < orthoPositroniumRate alpha electronFrequency := by
  unfold orthoPositroniumRate
  have hpi : 0 < Real.pi := Real.pi_pos
  have hpi3 : 3 < Real.pi := Real.pi_gt_three
  have hsquare : 9 < Real.pi ^ 2 := by nlinarith
  positivity

/-- Parâmetro adimensional magnético do fóton no background externo. -/
def magneticPairParameter
    (photonEnergy electronRestEnergy transverseField criticalField : ℝ) : ℝ :=
  photonEnergy / (2 * electronRestEnergy)
    * (transverseField / criticalField)

theorem magneticPairParameter_nonneg
    {photonEnergy electronRestEnergy transverseField criticalField : ℝ}
    (hE : 0 ≤ photonEnergy) (he : 0 < electronRestEnergy)
    (hB : 0 ≤ transverseField) (hBQ : 0 < criticalField) :
    0 ≤ magneticPairParameter photonEnergy electronRestEnergy
      transverseField criticalField := by
  unfold magneticPairParameter
  positivity

/-! ## 5. Espectro neutro candidato -/

/-- Impedância neutra reduzida usada no candidato do capítulo. -/
def neutralImpedance (alpha : ℝ) : ℝ :=
  (12 / 25 : ℝ) * Real.exp (-alpha / 4)

def neutralLambda₂ (alpha : ℝ) : ℝ :=
  neutralImpedance alpha ^ 2 / 2

def neutralLambda₃ : ℝ := 6 * Real.pi / 5

theorem neutralImpedance_pos (alpha : ℝ) :
    0 < neutralImpedance alpha := by
  unfold neutralImpedance
  positivity

theorem neutralLambda₂_pos (alpha : ℝ) :
    0 < neutralLambda₂ alpha := by
  unfold neutralLambda₂
  have hχ := neutralImpedance_pos alpha
  positivity

theorem neutralLambda₃_pos :
    0 < neutralLambda₃ := by
  unfold neutralLambda₃
  positivity

/--
Com escala positiva, as duas diferenças quadradas candidatas são positivas.
Isto é uma consequência do espectro declarado, não uma derivação do espectro
a partir da Hessiana neutra.
-/
theorem neutral_candidate_mass_splittings_pos
    {scale alpha : ℝ} (hscale : 0 < scale) :
    0 < scale * neutralLambda₂ alpha
      ∧ 0 < scale * neutralLambda₃ := by
  constructor
  · exact mul_pos hscale (neutralLambda₂_pos alpha)
  · exact mul_pos hscale neutralLambda₃_pos

/-! ## 6. Cota operacional de oscilação -/

/-- Fator de transição em dois canais, sem o termo de sobrevivência `1-P`. -/
def twoChannelOscillationFactor (mixing phase : ℝ) : ℝ :=
  Real.sin (2 * mixing) ^ 2 * Real.sin phase ^ 2

theorem twoChannelOscillationFactor_bounds (mixing phase : ℝ) :
    0 ≤ twoChannelOscillationFactor mixing phase
      ∧ twoChannelOscillationFactor mixing phase ≤ 1 := by
  have hmlo : 0 ≤ Real.sin (2 * mixing) ^ 2 := sq_nonneg _
  have hplo : 0 ≤ Real.sin phase ^ 2 := sq_nonneg _
  have hmhi : Real.sin (2 * mixing) ^ 2 ≤ 1 := by
    nlinarith [Real.neg_one_le_sin (2 * mixing), Real.sin_le_one (2 * mixing)]
  have hphi : Real.sin phase ^ 2 ≤ 1 := by
    nlinarith [Real.neg_one_le_sin phase, Real.sin_le_one phase]
  constructor
  · exact mul_nonneg hmlo hplo
  · calc
      Real.sin (2 * mixing) ^ 2 * Real.sin phase ^ 2
          ≤ 1 * Real.sin phase ^ 2 :=
            mul_le_mul_of_nonneg_right hmhi hplo
      _ ≤ 1 := by simpa using hphi

end

end GDQ
