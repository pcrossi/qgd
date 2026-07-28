import GDQ.CosmologicalFamily
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

namespace GDQ

noncomputable section

/-!
# Gravitação e cosmologia: camada algébrica exata

Este módulo formaliza somente identidades já demonstradas no Capítulo 20.
Ele não transforma a fórmula reduzida de Newton, a escolha do contorno
cosmológico ou os dados de `H₀` em axiomas da GDQ.

A camada certificada contém:

* reconstrução de `G` a partir do grupo adimensional;
* resposta de horizonte sob a condição global declarada;
* saddle térmico e colagem axial condicional;
* contagem dos 28 canais antissimétricos em oito dimensões;
* identidade exata da diluição radial;
* cancelamento de `c²` na densidade cosmológica reduzida;
* equações de estado `w=-1` e `w=1` nos setores declarados;
* identidade da aceleração crítica `a₀=cH₀/(2π)`.
-/

/-! ## 1. Grupo adimensional de Newton e condição de horizonte -/

/-- Grupo gravitacional adimensional na escala bariônica `M`. -/
def newtonDimensionlessGroup
    (G M hbar c : ℝ) : ℝ :=
  G * M ^ 2 / (hbar * c)

/-- Reconstrução dimensional de `G` depois de conhecido o grupo geométrico. -/
def newtonFromDimensionlessGroup
    (piG M hbar c : ℝ) : ℝ :=
  hbar * c / M ^ 2 * piG

theorem newton_group_reconstruction
    {G M hbar c : ℝ}
    (hM : M ≠ 0) (hhbar : hbar ≠ 0) (hc : c ≠ 0) :
    newtonFromDimensionlessGroup
        (newtonDimensionlessGroup G M hbar c) M hbar c
      = G := by
  unfold newtonFromDimensionlessGroup newtonDimensionlessGroup
  field_simp [hM, hhbar, hc]

/-- Resposta de Newton inferida de um raio e de uma energia de horizonte. -/
def horizonNewtonResponse
    (c radius energy : ℝ) : ℝ :=
  c ^ 4 * radius / (2 * energy)

/--
Se o contorno satisfaz `R=2GE/c⁴`, a resposta de horizonte reconstrói `G`.
O teorema não determina `R` nem `E`; eles continuam dados globais.
-/
theorem horizon_response_recovers_newton
    {G c radius energy : ℝ}
    (hc : c ≠ 0) (henergy : energy ≠ 0)
    (horizon : radius = 2 * G * energy / c ^ 4) :
    horizonNewtonResponse c radius energy = G := by
  unfold horizonNewtonResponse
  rw [horizon]
  field_simp [hc, henergy]

/-! ## 2. Saddle térmico e colagem axial -/

/-- Saddle do primeiro winding do kernel térmico oito-dimensional. -/
def thermalWindingSaddle (beta : ℝ) : ℝ :=
  beta ^ 2 / 16

theorem thermal_saddle_at_euclidean_period
    (radius : ℝ) :
    thermalWindingSaddle (2 * Real.pi * radius)
      = Real.pi ^ 2 * radius ^ 2 / 4 := by
  unfold thermalWindingSaddle
  ring

/-- Primeiro autovalor axial ímpar na esfera de raio `radius`. -/
def axialLowestEigenvalue (radius : ℝ) : ℝ :=
  2 / radius ^ 2

/-- Custo axial reduzido no saddle `tau`. -/
def axialRelativeCost (tau radius : ℝ) : ℝ :=
  tau * Real.pi ^ 2 * axialLowestEigenvalue radius

theorem axial_cost_at_thermal_saddle
    {horizonRadius axialRadius : ℝ} :
    axialRelativeCost
        (thermalWindingSaddle (2 * Real.pi * horizonRadius))
        axialRadius
      =
      Real.pi ^ 4 / 2 * horizonRadius ^ 2 / axialRadius ^ 2 := by
  unfold axialRelativeCost axialLowestEigenvalue thermalWindingSaddle
  ring

/--
A colagem `R=π²√α R_H` implica exatamente o expoente `1/(2α)`.
Essa igualdade é condicional à colagem; ela não deriva a colagem.
-/
theorem axial_cost_eq_inverse_two_alpha_of_gluing
    {alpha horizonRadius axialRadius : ℝ}
    (halpha : 0 < alpha) (hH : horizonRadius ≠ 0)
    (hglue :
      axialRadius = Real.pi ^ 2 * Real.sqrt alpha * horizonRadius) :
    axialRelativeCost
        (thermalWindingSaddle (2 * Real.pi * horizonRadius))
        axialRadius
      = 1 / (2 * alpha) := by
  rw [axial_cost_at_thermal_saddle, hglue]
  have hpi : Real.pi ≠ 0 := ne_of_gt Real.pi_pos
  have hsqrt : Real.sqrt alpha ≠ 0 :=
    ne_of_gt (Real.sqrt_pos.2 halpha)
  have hsqrt_sq : (Real.sqrt alpha) ^ 2 = alpha :=
    Real.sq_sqrt halpha.le
  field_simp [hpi, hsqrt, hH]
  nlinarith

/-! ## 3. Canais antissimétricos e diluição radial -/

/-- Número de componentes independentes de uma 2-forma em oito dimensões. -/
def cartanChannelCount : Nat :=
  Nat.choose 8 2

theorem cartanChannelCount_eq :
    cartanChannelCount = 28 := by
  decide

/-- Integral radial ponderada por `e⁻ᶠ=r_p/r`. -/
def weightedRadialIntegral
    (protonRadius horizonRadius : ℝ) : ℝ :=
  protonRadius / 2 * (horizonRadius ^ 2 - protonRadius ^ 2)

/-- Integral radial sem peso, com fatores angulares cancelados. -/
def unweightedRadialIntegral
    (horizonRadius : ℝ) : ℝ :=
  horizonRadius ^ 3 / 3

/--
Razão radial exata antes de absorver a normalização de ordem um no projetor
global.
-/
theorem exact_linear_dilution_ratio
    {protonRadius horizonRadius : ℝ}
    (hH : horizonRadius ≠ 0) :
    weightedRadialIntegral protonRadius horizonRadius
        / unweightedRadialIntegral horizonRadius
      =
      (3 / 2 : ℝ) * (protonRadius / horizonRadius)
        * (1 - protonRadius ^ 2 / horizonRadius ^ 2) := by
  unfold weightedRadialIntegral unweightedRadialIntegral
  field_simp [hH]

/-! ## 4. Densidade cosmológica reduzida -/

def protonVolume (protonRadius : ℝ) : ℝ :=
  (4 * Real.pi / 3) * protonRadius ^ 3

def protonUltravioletEnergyDensity
    (protonMass c protonRadius : ℝ) : ℝ :=
  protonMass * c ^ 2 / protonVolume protonRadius

/--
Densidade de massa cosmológica reduzida antes de simplificar o fator `c²`.
-/
def reducedCosmologicalMassDensity
    (alpha channelCount protonMass c protonRadius horizonRadius : ℝ) : ℝ :=
  alpha ^ 2 * channelCount
    * protonUltravioletEnergyDensity protonMass c protonRadius
    * (protonRadius / horizonRadius) / c ^ 2

/-- O fator de conversão `c²` cancela exatamente quando `c ≠ 0`. -/
theorem reducedCosmologicalMassDensity_cancel_c
    {alpha channelCount protonMass c protonRadius horizonRadius : ℝ}
    (hc : c ≠ 0) :
    reducedCosmologicalMassDensity
        alpha channelCount protonMass c protonRadius horizonRadius
      =
      alpha ^ 2 * channelCount
        * (protonMass / protonVolume protonRadius)
        * (protonRadius / horizonRadius) := by
  unfold reducedCosmologicalMassDensity
    protonUltravioletEnergyDensity
  field_simp [hc]

/-! ## 5. Equações de estado -/

def equationOfStateParameter
    (pressure massDensity c : ℝ) : ℝ :=
  pressure / (massDensity * c ^ 2)

theorem vacuum_equationOfState_eq_minus_one
    {massDensity c : ℝ}
    (hrho : massDensity ≠ 0) (hc : c ≠ 0) :
    equationOfStateParameter
        (-massDensity * c ^ 2) massDensity c = -1 := by
  unfold equationOfStateParameter
  field_simp [hrho, hc]

/--
No setor homogêneo estacionário, `w=-1` anula o termo de diluição da equação
de continuidade.
-/
theorem vacuum_continuity_source_zero
    (H massDensity : ℝ) :
    3 * H * (1 + (-1 : ℝ)) * massDensity = 0 := by
  ring

/--
Uma densidade que dilui como `a⁻⁶`, isto é, `ρ̇=-6Hρ`, e satisfaz a
continuidade de fluido perfeito tem `p=ρ`, desde que `H ≠ 0`.
-/
theorem stiff_pressure_of_sixth_power_dilution
    {H rho pressure rhoDot : ℝ}
    (hH : H ≠ 0)
    (hdilution : rhoDot = -6 * H * rho)
    (hcontinuity : rhoDot + 3 * H * (rho + pressure) = 0) :
    pressure = rho := by
  rw [hdilution] at hcontinuity
  apply (mul_left_cancel₀ hH)
  nlinarith

/-! ## 6. Aceleração crítica de horizonte -/

def criticalHorizonAcceleration
    (c horizonRadius : ℝ) : ℝ :=
  c ^ 2 / (2 * Real.pi * horizonRadius)

theorem critical_acceleration_eq_cH_over_two_pi
    {c H horizonRadius : ℝ}
    (hc : c ≠ 0) (hH : H ≠ 0)
    (horizon : horizonRadius = c / H) :
    criticalHorizonAcceleration c horizonRadius
      = c * H / (2 * Real.pi) := by
  unfold criticalHorizonAcceleration
  rw [horizon]
  have hpi : Real.pi ≠ 0 := ne_of_gt Real.pi_pos
  field_simp [hc, hH, hpi]

end

end GDQ
