import GDQ.ClassicalApparatusResponse
import GDQ.SternGerlachProjectors
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

namespace GDQ

/-!
# Hessiana, interface e resposta reduzida de Stern--Gerlach

Este módulo certifica a camada reduzida já demonstrada no Capítulo 11.
O campo magnético é dado clássico de fonte/contorno; não é acrescentado à
ação oficial. A Hessiana, seu Green físico e os blocos de Schur continuam
dados derivados de um background admissível.

São formalizados:

* a condição livre ponderada do bordo `r_c² = 6 τ`;
* a resposta de cada modo físico positivo da Hessiana;
* a positividade da rigidez textural induzida;
* a decomposição Noether--Zeeman da razão giromagnética;
* a deflexão clássica depois da seleção dos dois canais.
-/

open scoped BigOperators

section FreeBoundary

/-- Resíduo escalar da condição livre ponderada `K - n(F) = 0`. -/
noncomputable def sternGerlachFreeBoundaryResidual
    (τ r : ℝ) : ℝ :=
  -3 / r + r / (2 * τ)

/--
O vínculo geométrico `r_c² = 6τ` anula exatamente o resíduo de bordo.
-/
theorem sternGerlach_freeBoundary_of_radius_constraint
    (τ r : ℝ)
    (hτ : τ ≠ 0)
    (hr : r ≠ 0)
    (hradius : r ^ 2 = 6 * τ) :
    sternGerlachFreeBoundaryResidual τ r = 0 := by
  unfold sternGerlachFreeBoundaryResidual
  field_simp
  nlinarith

/-- Raio cilíndrico reduzido do ramo de Hopf. -/
noncomputable def hopfCylinderRadius (τ : ℝ) : ℝ :=
  2 * Real.sqrt τ

/-- Segunda variação homogênea reduzida do raio cilíndrico. -/
noncomputable def hopfCylinderRadialHessian (τ : ℝ) : ℝ :=
  3 / (2 * τ)

/-- O modo homogêneo de raio é rígido para `τ > 0`. -/
theorem hopfCylinderRadialHessian_pos
    (τ : ℝ) (hτ : 0 < τ) :
    0 < hopfCylinderRadialHessian τ := by
  unfold hopfCylinderRadialHessian
  positivity

/-- Potencial axial do harmônico de Hopf `l = 2`. -/
noncomputable def hopfAxialPotential (τ : ℝ) : ℝ :=
  2 / τ

/-- O potencial axial é positivo para fluxo positivo. -/
theorem hopfAxialPotential_pos
    (τ : ℝ) (hτ : 0 < τ) :
    0 < hopfAxialPotential τ := by
  unfold hopfAxialPotential
  positivity

/--
Forma fechada do valor DtN cilíndrico identificado pela solução do problema
de bordo na prova escrita. Este módulo certifica sua positividade, não
formaliza aqui a teoria analítica da EDO confluentemente hipergeométrica.
-/
noncomputable def cylindricalHopfDtNClosedForm : ℝ :=
  3 * Real.sqrt Real.pi / 4

/-- A forma fechada da impedância DtN cilíndrica reduzida é positiva. -/
theorem cylindricalHopfDtNClosedForm_pos :
    0 < cylindricalHopfDtNClosedForm := by
  unfold cylindricalHopfDtNClosedForm
  have hpi : 0 < Real.sqrt Real.pi := Real.sqrt_pos.2 Real.pi_pos
  positivity

end FreeBoundary

section InterfaceSpecialization

variable
  {B I : Type*}
  [NormedAddCommGroup B] [NormedSpace ℝ B]
  [NormedAddCommGroup I] [NormedSpace ℝ I]

/--
Impedância Stern--Gerlach obtida dos blocos da Hessiana física.
-/
noncomputable def sternGerlachSchurDtN
    (K : InterfaceBlockProblem B I) : B →L[ℝ] B :=
  K.schurResponse

/--
Depois de eliminar o interior estacionário, o resíduo visto pelo magneto é
exatamente a impedância Schur/DtN, sem coeficiente adicional.
-/
theorem sternGerlach_boundaryResidual_eq_schurDtN
    (K : InterfaceBlockProblem B I) (boundaryDatum : B) :
    K.boundaryResidual boundaryDatum =
      sternGerlachSchurDtN K boundaryDatum := by
  exact K.boundaryResidual_eq_schur boundaryDatum

end InterfaceSpecialization

section SpectralResponse

variable {ν : Type*} [Fintype ν]

/--
Dados físicos de um modo da Hessiana projetada no setor axial real.

`eigenvalue` é o autovalor positivo, `gradientWeight` é o coeficiente positivo
de `k²` no símbolo tangencial e `coupling₁`, `coupling₂` são as duas
componentes reais do acoplamento ao módulo `CP¹`.
-/
structure SternGerlachPhysicalMode where
  eigenvalue : ℝ
  gradientWeight : ℝ
  coupling₁ : ℝ
  coupling₂ : ℝ
  eigenvalue_pos : 0 < eigenvalue
  gradientWeight_pos : 0 < gradientWeight

/-- Coeficiente da resposta linear de um modo à componente de fonte `j`. -/
noncomputable def SternGerlachPhysicalMode.responseCoefficient
    (mode : SternGerlachPhysicalMode) (j : ℝ) : ℝ :=
  j / mode.eigenvalue

/-- A resposta espectral resolve `λ δΦ = j`. -/
theorem SternGerlachPhysicalMode.responseCoefficient_solves
    (mode : SternGerlachPhysicalMode) (j : ℝ) :
    mode.eigenvalue * mode.responseCoefficient j = j := by
  unfold SternGerlachPhysicalMode.responseCoefficient
  exact mul_div_cancel₀ j (ne_of_gt mode.eigenvalue_pos)

/-- Contribuição modal à rigidez textural axial. -/
noncomputable def SternGerlachPhysicalMode.rigidityContribution
    (mode : SternGerlachPhysicalMode) : ℝ :=
  mode.gradientWeight / mode.eigenvalue ^ 2 *
    (mode.coupling₁ ^ 2 + mode.coupling₂ ^ 2)

/-- Toda contribuição modal física é não negativa. -/
theorem SternGerlachPhysicalMode.rigidityContribution_nonneg
    (mode : SternGerlachPhysicalMode) :
    0 ≤ mode.rigidityContribution := by
  unfold SternGerlachPhysicalMode.rigidityContribution
  have hratio :
      0 ≤ mode.gradientWeight / mode.eigenvalue ^ 2 :=
    div_nonneg (le_of_lt mode.gradientWeight_pos)
      (sq_nonneg mode.eigenvalue)
  have hcouplings :
      0 ≤ mode.coupling₁ ^ 2 + mode.coupling₂ ^ 2 :=
    add_nonneg (sq_nonneg mode.coupling₁) (sq_nonneg mode.coupling₂)
  exact mul_nonneg hratio hcouplings

/-- Um modo que acopla ao menos numa direção fornece rigidez estritamente positiva. -/
theorem SternGerlachPhysicalMode.rigidityContribution_pos
    (mode : SternGerlachPhysicalMode)
    (hcoupling : mode.coupling₁ ≠ 0 ∨ mode.coupling₂ ≠ 0) :
    0 < mode.rigidityContribution := by
  unfold SternGerlachPhysicalMode.rigidityContribution
  have hsum :
      0 < mode.coupling₁ ^ 2 + mode.coupling₂ ^ 2 := by
    rcases hcoupling with h₁ | h₂
    · have hsquare : 0 < mode.coupling₁ ^ 2 := sq_pos_of_ne_zero h₁
      nlinarith [sq_nonneg mode.coupling₂]
    · have hsquare : 0 < mode.coupling₂ ^ 2 := sq_pos_of_ne_zero h₂
      nlinarith [sq_nonneg mode.coupling₁]
  have hratio :
      0 < mode.gradientWeight / mode.eigenvalue ^ 2 := by
    exact div_pos mode.gradientWeight_pos
      (pow_pos mode.eigenvalue_pos 2)
  exact mul_pos hratio hsum

/-- Rigidez isotrópica total no módulo axial bidimensional. -/
noncomputable def sternGerlachTextureRigidity
    (modes : ν → SternGerlachPhysicalMode) : ℝ :=
  (1 / 2 : ℝ) * ∑ mode, (modes mode).rigidityContribution

/-- A Hessiana física positiva induz rigidez textural não negativa. -/
theorem sternGerlachTextureRigidity_nonneg
    (modes : ν → SternGerlachPhysicalMode) :
    0 ≤ sternGerlachTextureRigidity modes := by
  unfold sternGerlachTextureRigidity
  exact mul_nonneg (by norm_num)
    (Finset.sum_nonneg fun mode _ =>
      (modes mode).rigidityContribution_nonneg)

/--
Se ao menos um modo físico acopla ao módulo axial, a rigidez total é
estritamente positiva.
-/
theorem sternGerlachTextureRigidity_pos
    (modes : ν → SternGerlachPhysicalMode)
    (mode₀ : ν)
    (hcoupling :
      (modes mode₀).coupling₁ ≠ 0 ∨
        (modes mode₀).coupling₂ ≠ 0) :
    0 < sternGerlachTextureRigidity modes := by
  unfold sternGerlachTextureRigidity
  have hterm :
      0 < (modes mode₀).rigidityContribution :=
    (modes mode₀).rigidityContribution_pos hcoupling
  have hsum :
      0 < ∑ mode, (modes mode).rigidityContribution := by
    exact Finset.sum_pos'
      (fun mode _ => (modes mode).rigidityContribution_nonneg)
      ⟨mode₀, Finset.mem_univ mode₀, hterm⟩
  positivity

end SpectralResponse

section NoetherZeeman

/--
Razão giromagnética efetiva no setor escalar da Hessiana vinculada.
-/
noncomputable def noetherZeemanEffectiveRatio
    (c inverseHessian m : ℝ) : ℝ :=
  c * inverseHessian * m / (c * inverseHessian * c)

/--
Separar a fonte magnética numa parte protegida por Noether e numa parte
transversal separa exatamente a razão efetiva.
-/
theorem noetherZeemanEffectiveRatio_decomposition
    (c inverseHessian γ₀ mPerp : ℝ)
    (hden : c * inverseHessian * c ≠ 0) :
    noetherZeemanEffectiveRatio c inverseHessian
        (γ₀ * c + mPerp) =
      γ₀ +
        noetherZeemanEffectiveRatio c inverseHessian mPerp := by
  unfold noetherZeemanEffectiveRatio
  apply (div_eq_iff hden).2
  rw [add_mul]
  rw [div_mul_cancel₀ _ hden]
  ring

/--
Sem resposta transversal, a componente protegida reproduz exatamente `γ₀`.
-/
theorem noetherZeemanEffectiveRatio_protected
    (c inverseHessian γ₀ : ℝ)
    (hden : c * inverseHessian * c ≠ 0) :
    noetherZeemanEffectiveRatio c inverseHessian (γ₀ * c) = γ₀ := by
  rw [show γ₀ * c = γ₀ * c + 0 by ring]
  rw [noetherZeemanEffectiveRatio_decomposition c inverseHessian γ₀ 0 hden]
  simp [noetherZeemanEffectiveRatio]

end NoetherZeeman

section ClassicalDeflection

/-- Tempo de trânsito pela região magnética. -/
noncomputable def sternGerlachTransitTime
    (length longitudinalVelocity : ℝ) : ℝ :=
  length / longitudinalVelocity

/-- Aceleração transversal num canal `κ = ±1`. -/
noncomputable def sternGerlachChannelAcceleration
    (κ magneticMoment fieldGradient mass : ℝ) : ℝ :=
  κ * magneticMoment * fieldGradient / mass

/-- Deflexão durante o trânsito com aceleração constante. -/
noncomputable def sternGerlachChannelDeflection
    (κ magneticMoment fieldGradient mass length
      longitudinalVelocity : ℝ) : ℝ :=
  (1 / 2 : ℝ) *
    sternGerlachChannelAcceleration κ magneticMoment fieldGradient mass *
    sternGerlachTransitTime length longitudinalVelocity ^ 2

/-- Forma fechada da deflexão clássica usada no capítulo. -/
theorem sternGerlachChannelDeflection_eq
    (κ magneticMoment fieldGradient mass length
      longitudinalVelocity : ℝ) :
    sternGerlachChannelDeflection κ magneticMoment fieldGradient mass
        length longitudinalVelocity =
      κ * magneticMoment * length ^ 2 * fieldGradient /
        (2 * mass * longitudinalVelocity ^ 2) := by
  unfold sternGerlachChannelDeflection
    sternGerlachChannelAcceleration sternGerlachTransitTime
  ring

/-- Os dois canais possuem deflexões opostas. -/
theorem sternGerlach_deflections_opposite
    (magneticMoment fieldGradient mass length
      longitudinalVelocity : ℝ) :
    sternGerlachChannelDeflection (-1) magneticMoment fieldGradient mass
        length longitudinalVelocity =
      -sternGerlachChannelDeflection 1 magneticMoment fieldGradient mass
        length longitudinalVelocity := by
  unfold sternGerlachChannelDeflection sternGerlachChannelAcceleration
  ring

end ClassicalDeflection

end GDQ
