import GDQ.ActionDensity
import GDQ.Fields
import GDQ.PhaseQuantization

namespace GDQ

open unitInterval

/-!
# Reconstrução da fase física a partir do potencial oficial

Este módulo fecha o elo constitutivo entre o campo complexo fundamental `f`
e a quantização global já formalizada em `GDQ.PhaseQuantization`.

O conteúdo lógico é deliberadamente separado em três níveis:

1. `f.re` determina a densidade positiva;
2. `f.im` determina uma fase circular por exponenciação;
3. o fechamento global dessa fase ao longo de um laço implica circulação
   inteira.

A ação pontual não escolhe sozinha a topologia do domínio nem um fibrado de
linha. Esses são dados de admissibilidade global. Uma vez que o laço físico é
admissível e fecha em `U(1)`, a integralidade não é um axioma adicional.
-/

/-- Fase física unitária reconstruída da parte imaginária de `f`. -/
noncomputable def unitPhaseFromPotential (f : ℂ) : ℂ :=
  Complex.exp ((f.im : ℂ) * Complex.I)

/--
Estado complexo reconstruído das duas relações constitutivas da GDQ.

Ele não é acrescentado como campo fundamental: é uma função do potencial
oficial `f`.
-/
noncomputable def reconstructedStateFromPotential (f : ℂ) : ℂ :=
  (Real.sqrt (densityFromPotential f) : ℂ) * unitPhaseFromPotential f

/-- A fase reconstruída possui norma unitária. -/
theorem norm_unitPhaseFromPotential (f : ℂ) :
    ‖unitPhaseFromPotential f‖ = 1 := by
  simp [unitPhaseFromPotential, Complex.norm_exp]

/--
A norma quadrada do estado reconstruído coincide exatamente com a densidade
constitutiva oficial.
-/
theorem norm_sq_reconstructedStateFromPotential (f : ℂ) :
    ‖reconstructedStateFromPotential f‖ ^ 2 =
      densityFromPotential f := by
  rw [reconstructedStateFromPotential, norm_mul,
    norm_unitPhaseFromPotential, mul_one]
  simp only [Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (Real.sqrt_nonneg _)]
  exact Real.sq_sqrt (le_of_lt (densityFromPotential_pos f))

/-- O estado reconstruído nunca se anula quando `f` é finito. -/
theorem reconstructedStateFromPotential_ne_zero (f : ℂ) :
    reconstructedStateFromPotential f ≠ 0 := by
  intro hzero
  have hnorm : ‖reconstructedStateFromPotential f‖ ^ 2 = 0 := by
    rw [hzero, norm_zero, zero_pow]
    norm_num
  rw [norm_sq_reconstructedStateFromPotential] at hnorm
  exact (ne_of_gt (densityFromPotential_pos f)) hnorm

/-! ## Deslocamentos imaginários e periodicidade física -/

/-- Deslocamento constante da componente imaginária do potencial. -/
def imaginaryShift (f : ℂ) (c : ℝ) : ℂ :=
  f + (c : ℂ) * Complex.I

/-- Um deslocamento imaginário constante não altera a parte real. -/
@[simp] theorem imaginaryShift_re (f : ℂ) (c : ℝ) :
    (imaginaryShift f c).re = f.re := by
  simp [imaginaryShift]

/-- O mesmo deslocamento soma `c` à parte imaginária. -/
@[simp] theorem imaginaryShift_im (f : ℂ) (c : ℝ) :
    (imaginaryShift f c).im = f.im + c := by
  simp [imaginaryShift]

/-- A densidade oficial é invariante sob deslocamento imaginário constante. -/
@[simp] theorem densityFromPotential_imaginaryShift
    (f : ℂ) (c : ℝ) :
    densityFromPotential (imaginaryShift f c) =
      densityFromPotential f := by
  simp [densityFromPotential]

/-- A fase real constitutiva muda por `ℏ c`. -/
theorem phaseFromPotential_imaginaryShift
    (ℏ : ℝ) (f : ℂ) (c : ℝ) :
    phaseFromPotential ℏ (imaginaryShift f c) =
      phaseFromPotential ℏ f + ℏ * c := by
  simp [phaseFromPotential]
  ring

/--
O termo real não derivativo do colchete oficial é invariável sob o
deslocamento imaginário.

Os argumentos geométricos e o quadrado do gradiente são mantidos explícitos.
Para uma translação *constante*, a igualdade do gradiente pertence à camada
diferencial da formalização; aqui certificamos a parte constitutiva pontual.
-/
theorem officialBracket_imaginaryShift
    (n : Nat) (τ scalarCurvature gradientNormSq : ℝ)
    (f : ℂ) (c : ℝ) :
    officialBracket n τ scalarCurvature gradientNormSq
        (imaginaryShift f c).re =
      officialBracket n τ scalarCurvature gradientNormSq f.re := by
  simp [officialBracket]

/-- O kernel oficial construído da densidade também é invariável. -/
theorem officialFlowKernel_imaginaryShift
    (n : Nat) (f : ℂ) (zτ : ℂ) (c : ℝ) :
    officialFlowKernel n
        (densityFromPotential (imaginaryShift f c)) zτ =
      officialFlowKernel n (densityFromPotential f) zτ := by
  simp

/--
A densidade pontual oficial é invariável no setor constitutivo sob
translações imaginárias constantes, desde que o termo de gradiente — que é
invariante após diferenciar uma constante — seja representado pelo mesmo
argumento `gradientNormSq`.
-/
theorem officialPointDensity_imaginaryShift
    (n : Nat)
    (ℏ ΛC τ scalarCurvature gradientNormSq volumeDensity : ℝ)
    (f : ℂ) (c : ℝ) :
    officialPointDensity n ℏ ΛC τ scalarCurvature gradientNormSq
        (imaginaryShift f c).re
        (densityFromPotential (imaginaryShift f c)) volumeDensity =
      officialPointDensity n ℏ ΛC τ scalarCurvature gradientNormSq
        f.re (densityFromPotential f) volumeDensity := by
  simp [officialPointDensity, officialBracket]

/-- Um deslocamento geral atua por uma rotação unitária na fase reconstruída. -/
theorem unitPhaseFromPotential_imaginaryShift
    (f : ℂ) (c : ℝ) :
    unitPhaseFromPotential (imaginaryShift f c) =
      unitPhaseFromPotential f *
        Complex.exp ((c : ℂ) * Complex.I) := by
  simp only [unitPhaseFromPotential, imaginaryShift_im]
  rw [show
    (((f.im + c : ℝ) : ℂ) * Complex.I) =
      (f.im : ℂ) * Complex.I + (c : ℂ) * Complex.I by
        push_cast
        ring]
  exact Complex.exp_add _ _

/--
Deslocamentos por `2πk` não alteram a fase física.

Esta é a identificação periódica concreta que transforma os levantamentos
reais locais em dados `U(1)`.
-/
theorem unitPhaseFromPotential_shift_two_pi_int
    (f : ℂ) (k : ℤ) :
    unitPhaseFromPotential
        (imaginaryShift f (2 * Real.pi * k)) =
      unitPhaseFromPotential f := by
  simpa [unitPhaseFromPotential] using
    complex_exp_phase_add_two_pi_int f.im k

/-- O estado reconstruído também é invariável sob `f ↦ f + 2πki`. -/
theorem reconstructedStateFromPotential_shift_two_pi_int
    (f : ℂ) (k : ℤ) :
    reconstructedStateFromPotential
        (imaginaryShift f (2 * Real.pi * k)) =
      reconstructedStateFromPotential f := by
  simp [reconstructedStateFromPotential,
    unitPhaseFromPotential_shift_two_pi_int]

/-! ## Aplicação às configurações oficiais -/

/-- Estado reconstruído pontualmente de uma configuração GDQ. -/
noncomputable def GDQFieldConfiguration.reconstructedState
    (Φ : GDQFieldConfiguration) (x : LocalPoint) : ℂ :=
  reconstructedStateFromPotential (Φ.potential x)

/--
No locus regular, a norma quadrada do estado reconstruído é a densidade da
própria configuração admissível.
-/
theorem GDQFieldConfiguration.norm_sq_reconstructedState_eq_rho
    (Φ : GDQFieldConfiguration) (x : LocalPoint)
    (hx : Φ.RegularAt x) :
    ‖Φ.reconstructedState x‖ ^ 2 = Φ.rho x := by
  rw [GDQFieldConfiguration.reconstructedState,
    norm_sq_reconstructedStateFromPotential,
    Φ.rho_eq_exp_on_regular x hx]

/-! ## Laços do potencial e circulação -/

/--
Laço físico descrito diretamente pelo potencial complexo.

`phase_closes` é a condição global de admissibilidade: o levantamento real
`Im f` pode mudar, mas sua imagem em `U(1)` retorna ao mesmo ponto.
-/
structure PotentialPhaseLoop where
  potential : C(I, ℂ)
  phase_closes :
    Circle.exp (potential 1).im = Circle.exp (potential 0).im

/-- Incremento da fase real constitutiva ao longo do laço. -/
noncomputable def PotentialPhaseLoop.phaseIncrement
    (ℏ : ℝ) (F : PotentialPhaseLoop) : ℝ :=
  ℏ * ((F.potential 1).im - (F.potential 0).im)

/--
O fechamento global da fase reconstruída força o incremento inteiro.

Não se supõe linearidade do perfil de `f`; a continuidade está contida no
tipo `C(I, ℂ)`.
-/
theorem PotentialPhaseLoop.phaseIncrement_quantized
    (ℏ : ℝ) (F : PotentialPhaseLoop) :
    ∃ n : ℤ,
      F.phaseIncrement ℏ = n * (2 * Real.pi * ℏ) := by
  have hmod :
      (F.potential 1).im ≡ (F.potential 0).im
        [PMOD (2 * Real.pi)] :=
    Circle.exp_inj.mp F.phase_closes
  rw [AddCommGroup.modEq_iff_zsmul'] at hmod
  obtain ⟨m, hm⟩ := hmod
  refine ⟨-m, ?_⟩
  have hm' :
      (F.potential 0).im - (F.potential 1).im =
        (m : ℝ) * (2 * Real.pi) := by
    simpa using hm
  rw [PotentialPhaseLoop.phaseIncrement,
    ← neg_sub (F.potential 0).im (F.potential 1).im, hm']
  push_cast
  ring

/--
Forma em unidades de Planck: se `h = 2πℏ`, a circulação vale `n h`.
-/
theorem PotentialPhaseLoop.phaseIncrement_eq_integer_h
    (ℏ h : ℝ) (F : PotentialPhaseLoop)
    (hh : h = 2 * Real.pi * ℏ) :
    ∃ n : ℤ, F.phaseIncrement ℏ = n * h := by
  obtain ⟨n, hn⟩ := F.phaseIncrement_quantized ℏ
  exact ⟨n, by simpa [hh] using hn⟩

end GDQ
