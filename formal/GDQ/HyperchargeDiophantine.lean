import Mathlib.Tactic

namespace GDQ

/-!
# Hipercargas: núcleo diofantino

As variáveis inteiras são `y = 6Y`. A orientação primitiva mínima fixa
`q = 1`; as equações linear e cúbica de anomalia, junto da convenção `u ≤ d`,
selecionam a solução orientada `(1,-4,2,-3,6)`.

O módulo prova também diretamente que essa solução satisfaz as congruências
globais de `Z₆` e todas as equações de anomalia usadas no manuscrito.
-/

/-- As quatro equações de anomalia para uma geração orientada. -/
def HyperchargeAnomalyEquations
    (q u d ell e : ℤ) : Prop :=
  2 * q + u + d = 0 ∧
  3 * q + ell = 0 ∧
  6 * q + 3 * u + 3 * d + 2 * ell + e = 0 ∧
  6 * q ^ 3 + 3 * u ^ 3 + 3 * d ^ 3 + 2 * ell ^ 3 + e ^ 3 = 0

/-- Congruências impostas pelo quociente global `Z₆`. -/
def HyperchargeZ6Congruences
    (q u d ell e : ℤ) : Prop :=
  q % 6 = 1 ∧
  u % 6 = 2 ∧
  d % 6 = 2 ∧
  ell % 6 = 3 ∧
  e % 6 = 0

/-- A solução padrão satisfaz exatamente as anomalias. -/
theorem standardHypercharges_anomaly :
    HyperchargeAnomalyEquations 1 (-4) 2 (-3) 6 := by
  norm_num [HyperchargeAnomalyEquations]

/-- A solução padrão satisfaz as congruências globais `Z₆`. -/
theorem standardHypercharges_z6 :
    HyperchargeZ6Congruences 1 (-4) 2 (-3) 6 := by
  norm_num [HyperchargeZ6Congruences]

/--
Unicidade orientada no setor primitivo mínimo. A desigualdade `u ≤ d` apenas
fixa o nome dos dois singletos coloridos; sem ela, as anomalias os permutam.
-/
theorem hypercharge_unique_oriented_minimal
    {q u d ell e : ℤ}
    (hq : q = 1)
    (hanom : HyperchargeAnomalyEquations q u d ell e)
    (horder : u ≤ d) :
    q = 1 ∧ u = -4 ∧ d = 2 ∧ ell = -3 ∧ e = 6 := by
  rcases hanom with ⟨hcolor, hweak, hgrav, hcubic⟩
  have hell : ell = -3 := by omega
  have hd : d = -2 - u := by omega
  have he : e = 6 := by omega
  have hfactor : (u + 4) * (u - 2) = 0 := by
    rw [hq, hell, hd, he] at hcubic
    nlinarith
  rcases mul_eq_zero.mp hfactor with hu | hu
  · have hu' : u = -4 := by omega
    subst u
    omega
  · have hu' : u = 2 := by omega
    subst u
    omega

/-- Conversão dos inteiros selecionados para as hipercargas físicas `Y=y/6`. -/
theorem standardHypercharges_physical :
    ((1 : ℚ) / 6, (-4 : ℚ) / 6, (2 : ℚ) / 6, (-3 : ℚ) / 6, (6 : ℚ) / 6) =
      ((1 : ℚ) / 6, (-2 : ℚ) / 3, (1 : ℚ) / 3, (-1 : ℚ) / 2, 1) := by
  norm_num

end GDQ
