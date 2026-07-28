import GDQ.Fields
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace GDQ

/-!
# Kernel de fluxo

Formalização pontual da convenção

`𝒰 = ρ / (4 π z_τ)^n`.

No contorno complexo, `𝒰` é complexo. A positividade é provada separadamente
para a seção euclidiana real positiva.
-/

/-- Kernel complexo oficial em dimensão complexa `n`. -/
noncomputable def officialFlowKernel
    (n : Nat) (ρ : ℝ) (zτ : ℂ) : ℂ :=
  (ρ : ℂ) / (((4 * Real.pi : ℝ) : ℂ) * zτ) ^ n

/-- O denominador do kernel não se anula quando `zτ ≠ 0`. -/
theorem officialFlowKernel_denominator_ne_zero
    (n : Nat) (zτ : ℂ) (hz : zτ ≠ 0) :
    ((((4 * Real.pi : ℝ) : ℂ) * zτ) ^ n) ≠ 0 := by
  apply pow_ne_zero
  apply mul_ne_zero
  · norm_num [Real.pi_ne_zero]
  · exact hz

/-- Restrição euclidiana real do kernel. -/
noncomputable def euclideanFlowKernel
    (n : Nat) (ρ zτ : ℝ) : ℝ :=
  ρ / (4 * Real.pi * zτ) ^ n

/-- Na seção real positiva, o kernel é estritamente positivo. -/
theorem euclideanFlowKernel_pos
    (n : Nat) {ρ zτ : ℝ}
    (hρ : 0 < ρ) (hz : 0 < zτ) :
    0 < euclideanFlowKernel n ρ zτ := by
  apply div_pos hρ
  exact pow_pos (mul_pos (mul_pos (by norm_num) Real.pi_pos) hz) n

end GDQ
