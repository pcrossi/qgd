import GDQ.TransportInterference
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

namespace GDQ

noncomputable section

/-!
# Aplicações simples da redução GDQ

Este módulo formaliza a camada algébrica já demonstrada no Capítulo 23:

* espectro do poço ideal e sua equivalência com circulação fechada;
* cancelamento do termo quadrático no oscilador gaussiano;
* coeficientes universais de energia e pressão de Casimir;
* eliminação radial que produz a distorção centrífuga do rotor.

Esses resultados são consequências dos operadores reduzidos nos domínios
declarados. O módulo não postula esses operadores como nova ação fundamental
e não calcula impedâncias de materiais ou backgrounds moleculares reais.
-/

/-! ## 1. Poço ideal -/

def infiniteWellEnergy
    (hbar mass length mode : ℝ) : ℝ :=
  hbar ^ 2 * Real.pi ^ 2 * mode ^ 2
    / (2 * mass * length ^ 2)

theorem infiniteWellEnergy_nonneg
    {hbar mass length mode : ℝ}
    (hmass : 0 < mass) (hlength : length ≠ 0) :
    0 ≤ infiniteWellEnergy hbar mass length mode := by
  unfold infiniteWellEnergy
  positivity

theorem infiniteWellEnergy_pos
    {hbar mass length mode : ℝ}
    (hhbar : hbar ≠ 0) (hmass : 0 < mass)
    (hlength : length ≠ 0) (hmode : mode ≠ 0) :
    0 < infiniteWellEnergy hbar mass length mode := by
  unfold infiniteWellEnergy
  positivity

/-- Momento obtido da circulação fechada `2pL=nh`. -/
def closedWellMomentum
    (planck length mode : ℝ) : ℝ :=
  mode * planck / (2 * length)

def nonrelativisticKineticEnergy
    (momentum mass : ℝ) : ℝ :=
  momentum ^ 2 / (2 * mass)

/--
Com `h=2πℏ`, a rota por circulação produz exatamente o mesmo espectro do
problema de Dirichlet.
-/
theorem closed_circulation_recovers_infiniteWellEnergy
    {hbar mass length mode : ℝ}
    (hmass : mass ≠ 0) (hlength : length ≠ 0) :
    nonrelativisticKineticEnergy
        (closedWellMomentum (2 * Real.pi * hbar) length mode) mass
      =
      infiniteWellEnergy hbar mass length mode := by
  unfold nonrelativisticKineticEnergy closedWellMomentum infiniteWellEnergy
  field_simp [hmass, hlength]

/-! ## 2. Oscilador harmônico -/

/-- Razão `R''/R` para `R=A exp(-αx²/2)`. -/
def gaussianSecondDerivativeRatio
    (alpha x : ℝ) : ℝ :=
  alpha ^ 2 * x ^ 2 - alpha

/-- Lado direito estacionário da equação Hamilton--Jacobi--Bohm reduzida. -/
def oscillatorStationaryEnergy
    (hbar mass omega alpha x : ℝ) : ℝ :=
  mass * omega ^ 2 * x ^ 2 / 2
    - hbar ^ 2 / (2 * mass)
      * gaussianSecondDerivativeRatio alpha x

/--
Escolher `α=mω/ℏ` cancela exatamente a dependência em `x` e produz
`E₀=ℏω/2`.
-/
theorem oscillator_gaussian_ground_energy
    {hbar mass omega x : ℝ}
    (hhbar : hbar ≠ 0) (hmass : mass ≠ 0) :
    oscillatorStationaryEnergy
        hbar mass omega (mass * omega / hbar) x
      = hbar * omega / 2 := by
  unfold oscillatorStationaryEnergy gaussianSecondDerivativeRatio
  field_simp [hhbar, hmass]
  ring

def oscillatorLadderEnergy
    (hbar omega mode : ℝ) : ℝ :=
  hbar * omega * (mode + 1 / 2)

theorem oscillatorLadder_spacing
    (hbar omega mode : ℝ) :
    oscillatorLadderEnergy hbar omega (mode + 1)
      - oscillatorLadderEnergy hbar omega mode
      = hbar * omega := by
  unfold oscillatorLadderEnergy
  ring

/-! ## 3. Casimir ideal -/

/--
Coeficiente espectral antes de simplificar, usando duas polarizações,
a integral transversal `-m³/(6π)` e `ζ(-3)=1/120`.
-/
def casimirSpectralCoefficient : ℝ :=
  -(1 / (6 * Real.pi)) * Real.pi ^ 3 * (1 / 120)

theorem casimirSpectralCoefficient_eq :
    casimirSpectralCoefficient = -Real.pi ^ 2 / 720 := by
  unfold casimirSpectralCoefficient
  have hpi : Real.pi ≠ 0 := ne_of_gt Real.pi_pos
  field_simp [hpi]
  ring

def casimirEnergyPerArea
    (hbar c separation : ℝ) : ℝ :=
  -Real.pi ^ 2 * hbar * c / (720 * separation ^ 3)

def casimirPressure
    (hbar c separation : ℝ) : ℝ :=
  -Real.pi ^ 2 * hbar * c / (240 * separation ^ 4)

/--
A fórmula da pressão contém exatamente o fator três produzido pela derivada
da lei `a⁻³`.
-/
theorem casimirPressure_eq_three_energy_over_separation
    {hbar c separation : ℝ} (hsep : separation ≠ 0) :
    casimirPressure hbar c separation
      = 3 * casimirEnergyPerArea hbar c separation / separation := by
  unfold casimirEnergyPerArea casimirPressure
  field_simp [hsep]
  ring

theorem casimirPressure_neg
    {hbar c separation : ℝ}
    (hhbar : 0 < hbar) (hc : 0 < c) (hsep : separation ≠ 0) :
    casimirPressure hbar c separation < 0 := by
  unfold casimirPressure
  have hsep4 : 0 < separation ^ 4 := by positivity
  have hpi : 0 < Real.pi ^ 2 := sq_pos_of_pos Real.pi_pos
  have hprod : 0 < Real.pi ^ 2 * hbar * c :=
    mul_pos (mul_pos hpi hhbar) hc
  have hnum : -Real.pi ^ 2 * hbar * c < 0 := by
    nlinarith
  exact div_neg_of_neg_of_pos hnum
    (mul_pos (by norm_num) hsep4)

/-! ## 4. Rotor molecular e eliminação radial -/

/--
Energia radial quadrática suficiente para obter o termo líder de ordem `L⁴`.
O argumento `angularMomentumSq` representa `L²`.
-/
def rotorQuadraticRadialEnergy
    (angularMomentumSq mass radius omega displacement : ℝ) : ℝ :=
  angularMomentumSq / (2 * mass * radius ^ 2)
    - angularMomentumSq * displacement / (mass * radius ^ 3)
    + (1 / 2 : ℝ) * mass * omega ^ 2 * displacement ^ 2

def rotorRadialShift
    (angularMomentumSq mass radius omega : ℝ) : ℝ :=
  angularMomentumSq / (mass ^ 2 * omega ^ 2 * radius ^ 3)

/-- Substituir o mínimo radial produz o termo centrífugo negativo líder. -/
theorem rotor_energy_at_radial_minimum
    {angularMomentumSq mass radius omega : ℝ}
    (hmass : mass ≠ 0) (hradius : radius ≠ 0) (homega : omega ≠ 0) :
    rotorQuadraticRadialEnergy angularMomentumSq mass radius omega
        (rotorRadialShift angularMomentumSq mass radius omega)
      =
      angularMomentumSq / (2 * mass * radius ^ 2)
        - angularMomentumSq ^ 2
          / (2 * mass ^ 3 * omega ^ 2 * radius ^ 6) := by
  unfold rotorQuadraticRadialEnergy rotorRadialShift
  field_simp [hmass, hradius, homega]
  ring

def rigidRotorConstant
    (hbar mass radius : ℝ) : ℝ :=
  hbar ^ 2 / (2 * mass * radius ^ 2)

def centrifugalDistortionConstant
    (hbar mass radius omega : ℝ) : ℝ :=
  hbar ^ 4 / (2 * mass ^ 3 * omega ^ 2 * radius ^ 6)

/-- Forma espectroscópica equivalente `D=4B³/(ℏ²ω²)`. -/
theorem centrifugalDistortion_eq_four_B_cubed
    {hbar mass radius omega : ℝ}
    (hhbar : hbar ≠ 0) (hmass : mass ≠ 0)
    (hradius : radius ≠ 0) (homega : omega ≠ 0) :
    centrifugalDistortionConstant hbar mass radius omega
      =
      4 * rigidRotorConstant hbar mass radius ^ 3
        / (hbar ^ 2 * omega ^ 2) := by
  unfold centrifugalDistortionConstant rigidRotorConstant
  field_simp [hhbar, hmass, hradius, homega]
  ring

theorem centrifugalDistortionConstant_pos
    {hbar mass radius omega : ℝ}
    (hhbar : hbar ≠ 0) (hmass : 0 < mass)
    (hradius : radius ≠ 0) (homega : omega ≠ 0) :
    0 < centrifugalDistortionConstant hbar mass radius omega := by
  unfold centrifugalDistortionConstant
  positivity

end

end GDQ
