import GDQ.PhaseQuantization
import Mathlib.MeasureTheory.Integral.CircleIntegral

namespace GDQ

/-!
# Meia-monodromia spinorial de Hopf e resíduo de Cauchy

Este módulo porta para Lean a prova já apresentada no capítulo de spin.

O dado geométrico de entrada é a classe local spinorial/Hopf do defeito,
representada numa carta complexa transversal por uma seção com fator
`z^(1/2)`. A sua derivada logarítmica singular é

`Ωₛ = (1/2) dz/z`.

O arquivo não postula que a ação pontual selecione essa classe topológica.
Ele certifica as consequências exatas depois que o setor spinorial/Hopf foi
fixado:

* resíduo normalizado `1/2`;
* circulação física `h/2 = πℏ`;
* holonomia `-1` após uma volta;
* holonomia `+1` após duas voltas.
-/

/--
Coeficiente da forma logarítmica singular da seção local
`s(z) = z^(1/2) s₀(z)`.

A parcela holomorfa `d log s₀` possui integral nula no disco e, portanto, não
altera o resíduo. Aqui isolamos o representante singular que determina a
classe de monodromia.
-/
noncomputable def halfLogConnection (z : ℂ) : ℂ :=
  (2 : ℂ)⁻¹ * z⁻¹

/--
Integral exata da conexão logarítmica spinorial sobre qualquer círculo
positivo centrado no núcleo removido.

Esta é a versão formal de

`∮ (1/2) dz/z = π i`.
-/
theorem circleIntegral_halfLogConnection
    {R : ℝ} (hR : R ≠ 0) :
    (∮ z in C(0, R), halfLogConnection z) =
      (Real.pi : ℂ) * Complex.I := by
  change
    circleIntegral (fun z : ℂ => (2 : ℂ)⁻¹ * z⁻¹) 0 R =
      (Real.pi : ℂ) * Complex.I
  rw [circleIntegral.integral_const_mul]
  have hc :
      (∮ z in C((0 : ℂ), R), z⁻¹) =
        2 * (Real.pi : ℂ) * Complex.I := by
    simpa using
      (circleIntegral.integral_sub_center_inv (0 : ℂ) hR)
  rw [hc]
  norm_num
  ring

/--
Uma parcela regular exata não modifica a meia-monodromia.

`regular` representa `d log s₀` e `primitive` representa `log s₀` na carta.
As hipóteses registram explicitamente o domínio analítico necessário:
integrabilidade sobre o círculo e existência da derivada tangencial complexa.
-/
theorem circleIntegral_halfLogConnection_add_exact
    {R : ℝ} (hR : R ≠ 0)
    {primitive regular : ℂ → ℂ}
    (hhalf : CircleIntegrable halfLogConnection 0 R)
    (hregular : CircleIntegrable regular 0 R)
    (hderiv :
      ∀ z ∈ Metric.sphere (0 : ℂ) |R|,
        HasDerivWithinAt primitive (regular z)
          (Metric.sphere (0 : ℂ) |R|) z) :
    (∮ z in C(0, R), halfLogConnection z + regular z) =
      (Real.pi : ℂ) * Complex.I := by
  rw [circleIntegral.integral_add hhalf hregular,
    circleIntegral_halfLogConnection hR,
    circleIntegral.integral_eq_zero_of_hasDerivWithinAt' hderiv,
    add_zero]

/-- Resíduo normalizado da conexão de meia-monodromia. -/
noncomputable def normalizedHalfResidue (R : ℝ) : ℂ :=
  (2 * (Real.pi : ℂ) * Complex.I)⁻¹ *
    (∮ z in C(0, R), halfLogConnection z)

/--
O teorema de Cauchy aplicado ao representante singular fornece exatamente
o resíduo `1/2`, independentemente do raio do laço.
-/
theorem normalizedHalfResidue_eq_half
    {R : ℝ} (hR : R ≠ 0) :
    normalizedHalfResidue R = (2 : ℂ)⁻¹ := by
  rw [normalizedHalfResidue, circleIntegral_halfLogConnection hR]
  have hpi : (Real.pi : ℂ) ≠ 0 := by
    exact_mod_cast ne_of_gt Real.pi_pos
  field_simp [hpi, Complex.I_ne_zero]

/-! ## Conversão do resíduo em circulação física -/

/-- Constante de Planck em função de `ℏ`. -/
noncomputable def planckConstant (ℏ : ℝ) : ℝ :=
  2 * Real.pi * ℏ

/-- Circulação física associada à meia-monodromia simples. -/
noncomputable def halfSpinCirculation (ℏ : ℝ) : ℝ :=
  planckConstant ℏ / 2

/-- A meia-circulação `h/2` coincide exatamente com `πℏ`. -/
theorem halfSpinCirculation_eq_pi_hbar (ℏ : ℝ) :
    halfSpinCirculation ℏ = Real.pi * ℏ := by
  simp [halfSpinCirculation, planckConstant]
  ring

/--
Família completa de circulações spinoriais: um enrolamento inteiro somado à
meia-monodromia.
-/
noncomputable def spinorialCirculation (ℏ : ℝ) (n : ℤ) : ℝ :=
  2 * Real.pi * ℏ * ((n : ℝ) + 1 / 2)

/-- A circulação spinorial pertence à classe `(n + 1/2)h`. -/
theorem spinorialCirculation_eq_half_integer_h
    (ℏ : ℝ) (n : ℤ) :
    spinorialCirculation ℏ n =
      ((n : ℝ) + 1 / 2) * planckConstant ℏ := by
  simp [spinorialCirculation, planckConstant]
  ring

/-! ## Holonomia e recobrimento duplo -/

/-- Holonomia de uma circulação expressa em unidades de `ℏ`. -/
noncomputable def phaseHolonomy (ℏ circulation : ℝ) : ℂ :=
  Complex.exp
    ((((circulation / ℏ : ℝ) : ℂ) * Complex.I))

/--
Uma volta no setor de meia-monodromia produz sinal `-1`.

A hipótese `ℏ ≠ 0` apenas garante que a conversão de unidades
`circulation / ℏ` está definida fisicamente.
-/
theorem phaseHolonomy_halfSpinCirculation
    {ℏ : ℝ} (hℏ : ℏ ≠ 0) :
    phaseHolonomy ℏ (halfSpinCirculation ℏ) = -1 := by
  rw [phaseHolonomy, halfSpinCirculation_eq_pi_hbar]
  have hratio : Real.pi * ℏ / ℏ = Real.pi := by
    exact mul_div_cancel_right₀ Real.pi hℏ
  rw [hratio]
  exact Complex.exp_pi_mul_I

/-- Duas voltas restauram o sinal positivo. -/
theorem phaseHolonomy_double_halfSpinCirculation
    {ℏ : ℝ} (hℏ : ℏ ≠ 0) :
    phaseHolonomy ℏ (2 * halfSpinCirculation ℏ) = 1 := by
  rw [phaseHolonomy, halfSpinCirculation_eq_pi_hbar]
  have hratio : 2 * (Real.pi * ℏ) / ℏ = 2 * Real.pi := by
    field_simp [hℏ]
  rw [hratio]
  convert Complex.exp_two_pi_mul_I using 1
  norm_num

/-- Levantamento angular local da meia-monodromia. -/
noncomputable def halfSpinLift (θ : ℝ) : ℂ :=
  Complex.exp ((((θ / 2 : ℝ) : ℂ) * Complex.I))

/-- Uma rotação de `2π` muda o sinal do levantamento spinorial. -/
theorem halfSpinLift_two_pi :
    halfSpinLift (2 * Real.pi) = -1 := by
  rw [halfSpinLift]
  convert Complex.exp_pi_mul_I using 2
  norm_num

/-- Uma rotação de `4π` fecha o levantamento spinorial. -/
theorem halfSpinLift_four_pi :
    halfSpinLift (4 * Real.pi) = 1 := by
  rw [halfSpinLift]
  convert Complex.exp_two_pi_mul_I using 2
  push_cast
  ring

/--
O projetor físico é insensível à troca de sinal do representante spinorial.

Esta identidade algébrica é o núcleo do quociente `u ∼ -u` usado no mapa de
Hopf `P = u u†`.
-/
theorem hopfProjector_sign_invariant (u : ℂ) :
    (-u) * star (-u) = u * star u := by
  simp

end GDQ
