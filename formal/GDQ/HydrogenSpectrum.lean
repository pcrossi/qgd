import GDQ.ElectroweakStability
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

namespace GDQ

noncomputable section

/-!
# Espectro atômico reduzido e estrutura hiperfina

Este módulo formaliza consequências algébricas do operador espinorial efetivo
obtido como redução da Hessiana física GDQ no background protônico. Ele não
introduz a equação de Dirac como nova ação fundamental.

O código não transforma valores metrológicos, fatores de forma ou blocos
protônicos ainda não avaliados em axiomas. A camada certificada contém:

* massa reduzida;
* simetria `κ ↦ -κ` do espectro Sommerfeld--Dirac;
* degenerescência Coulombiana entre os canais `κ=±1`;
* desdobramento fino líder entre `j=1/2` e `j=3/2`;
* álgebra hiperfina singlete--triplete;
* sinal da correção de Zemach;
* complemento de Schur da superfície protônica.
-/

/-! ## 1. Massa reduzida -/

def reducedMass (m₁ m₂ : ℝ) : ℝ :=
  m₁ * m₂ / (m₁ + m₂)

theorem reducedMass_pos
    {m₁ m₂ : ℝ} (hm₁ : 0 < m₁) (hm₂ : 0 < m₂) :
    0 < reducedMass m₁ m₂ := by
  unfold reducedMass
  exact div_pos (mul_pos hm₁ hm₂) (add_pos hm₁ hm₂)

theorem reducedMass_lt_left
    {m₁ m₂ : ℝ} (hm₁ : 0 < m₁) (hm₂ : 0 < m₂) :
    reducedMass m₁ m₂ < m₁ := by
  unfold reducedMass
  apply (div_lt_iff₀ (add_pos hm₁ hm₂)).2
  nlinarith

theorem reducedMass_lt_right
    {m₁ m₂ : ℝ} (hm₁ : 0 < m₁) (hm₂ : 0 < m₂) :
    reducedMass m₁ m₂ < m₂ := by
  unfold reducedMass
  apply (div_lt_iff₀ (add_pos hm₁ hm₂)).2
  nlinarith

/-! ## 2. Espectro Sommerfeld--Dirac -/

/--
Denominador radial do espectro, escrito para parâmetros reais. Na aplicação,
`n` é inteiro positivo e `κ` é inteiro não nulo.
-/
def sommerfeldRadialDenominator (n κ zα : ℝ) : ℝ :=
  n - |κ| + Real.sqrt (κ ^ 2 - zα ^ 2)

/--
Energia positiva do espectro externo em unidades nas quais `c=1`.
-/
def sommerfeldDiracEnergy (m n κ zα : ℝ) : ℝ :=
  m / Real.sqrt
    (1 + zα ^ 2 / sommerfeldRadialDenominator n κ zα ^ 2)

theorem sommerfeldRadialDenominator_negKappa
    (n κ zα : ℝ) :
    sommerfeldRadialDenominator n (-κ) zα =
      sommerfeldRadialDenominator n κ zα := by
  unfold sommerfeldRadialDenominator
  rw [abs_neg]
  congr 2
  ring

/--
O espectro Coulomb--Dirac depende de `|κ|`, não do sinal de `κ`.
-/
theorem sommerfeldDiracEnergy_negKappa
    (m n κ zα : ℝ) :
    sommerfeldDiracEnergy m n (-κ) zα =
      sommerfeldDiracEnergy m n κ zα := by
  unfold sommerfeldDiracEnergy
  rw [sommerfeldRadialDenominator_negKappa]

/--
Em particular, os canais `κ=-1` e `κ=+1` são degenerados. Para `n=2`, essa
é a igualdade Coulombiana `2s₁/₂ = 2p₁/₂`.
-/
theorem sommerfeld_two_channels_degenerate
    (m n zα : ℝ) :
    sommerfeldDiracEnergy m n (-1) zα =
      sommerfeldDiracEnergy m n 1 zα := by
  simpa using sommerfeldDiracEnergy_negKappa m n 1 zα

/-! ## 3. Estrutura fina líder -/

/--
Expansão até ordem `α⁴`, sem o resto `O(α⁶)`, em unidades `c=1`.
-/
def fineStructureEnergyApprox
    (m α n j : ℝ) : ℝ :=
  m
    - m * α ^ 2 / (2 * n ^ 2)
    - m * α ^ 4 / (2 * n ^ 4) * (n / (j + 1 / 2) - 3 / 4)

/--
Para `n=2`, o desdobramento líder entre `j=3/2` e `j=1/2` é
`m α⁴/32`.
-/
theorem fineStructure_n2_spinOrbitSplitting
    (m α : ℝ) :
    fineStructureEnergyApprox m α 2 (3 / 2) -
        fineStructureEnergyApprox m α 2 (1 / 2)
      = m * α ^ 4 / 32 := by
  unfold fineStructureEnergyApprox
  ring

theorem fineStructure_n2_spinOrbitSplitting_pos
    {m α : ℝ} (hm : 0 < m) (hα : α ≠ 0) :
    0 <
      fineStructureEnergyApprox m α 2 (3 / 2) -
        fineStructureEnergyApprox m α 2 (1 / 2) := by
  rw [fineStructure_n2_spinOrbitSplitting]
  have hα4 : 0 < α ^ 4 := by positivity
  exact div_pos (mul_pos hm hα4) (by norm_num)

/-! ## 4. Álgebra hiperfina -/

/--
Autovalor de `I·S` no canal de momento total `F`, em unidades de `ℏ²`.
-/
def spinDotEigenvalue (F I S : ℝ) : ℝ :=
  (F * (F + 1) - I * (I + 1) - S * (S + 1)) / 2

theorem hydrogenTriplet_spinDot :
    spinDotEigenvalue 1 (1 / 2) (1 / 2) = 1 / 4 := by
  norm_num [spinDotEigenvalue]

theorem hydrogenSinglet_spinDot :
    spinDotEigenvalue 0 (1 / 2) (1 / 2) = -3 / 4 := by
  norm_num [spinDotEigenvalue]

/-- A separação angular singlete--triplete é uma unidade do acoplamento. -/
theorem hydrogenHyperfine_angularSplitting :
    spinDotEigenvalue 1 (1 / 2) (1 / 2)
      - spinDotEigenvalue 0 (1 / 2) (1 / 2) = 1 := by
  rw [hydrogenTriplet_spinDot, hydrogenSinglet_spinDot]
  norm_num

/-! ## 5. Correção de Zemach e Schur protônico -/

def zemachRelativeCorrection
    (α μ c hbar rZ : ℝ) : ℝ :=
  -2 * α * (μ * c / hbar) * rZ

theorem zemachRelativeCorrection_neg
    {α μ c hbar rZ : ℝ}
    (hα : 0 < α) (hμ : 0 < μ) (hc : 0 < c)
    (hhbar : 0 < hbar) (hrZ : 0 < rZ) :
    zemachRelativeCorrection α μ c hbar rZ < 0 := by
  unfold zemachRelativeCorrection
  have hratio : 0 < μ * c / hbar :=
    div_pos (mul_pos hμ hc) hhbar
  have hproduct : 0 < 2 * α * (μ * c / hbar) * rZ :=
    mul_pos (mul_pos (mul_pos (by norm_num) hα) hratio) hrZ
  nlinarith

/--
Bloco de superfície depois de eliminar os graus internos do próton.
É a mesma identidade de Schur usada em outras interfaces GDQ, agora com nomes
atômicos.
-/
def protonSurfaceSchur
    (kYY kYI kII : ℝ) : ℝ :=
  kYY - kYI ^ 2 / kII

theorem protonSurfaceSchur_pos
    {kYY kYI kII : ℝ}
    (hkII : 0 < kII)
    (hmargin : kYI ^ 2 < kYY * kII) :
    0 < protonSurfaceSchur kYY kYI kII := by
  unfold protonSurfaceSchur
  rw [sub_pos, div_lt_iff₀ hkII]
  simpa [mul_comm] using hmargin

end

end GDQ
