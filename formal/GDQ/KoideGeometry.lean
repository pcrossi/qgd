import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

namespace GDQ

/-!
# Relação de Koide como saturação geométrica

Para amplitudes não negativas `Aᵢ = √Rᵢ`, a condição de igualdade entre as
normas das componentes paralela e perpendicular ao eixo `(1,1,1)` equivale a

`3 ∑ Aᵢ² = 2 (∑ Aᵢ)²`,

isto é, `Q = 2/3` quando a soma das amplitudes é não nula.
-/

/-- Soma quadrática das três amplitudes. -/
def koideQuadratic (a b c : ℝ) : ℝ :=
  a ^ 2 + b ^ 2 + c ^ 2

/-- Quadrado da norma da projeção no eixo unitário `(1,1,1)/√3`. -/
noncomputable def koideParallelSq (a b c : ℝ) : ℝ :=
  (a + b + c) ^ 2 / 3

/-- Quadrado da componente ortogonal, por Pitágoras. -/
noncomputable def koidePerpendicularSq (a b c : ℝ) : ℝ :=
  koideQuadratic a b c - koideParallelSq a b c

/-- A igualdade perpendicular/paralela equivale à forma polinomial de Koide. -/
theorem koide_saturation_iff_polynomial (a b c : ℝ) :
    koidePerpendicularSq a b c = koideParallelSq a b c ↔
      3 * koideQuadratic a b c = 2 * (a + b + c) ^ 2 := by
  unfold koidePerpendicularSq koideParallelSq koideQuadratic
  constructor <;> intro h <;> nlinarith

/-- No setor não degenerado, a saturação fornece exatamente `Q=2/3`. -/
theorem koide_ratio_eq_two_thirds
    {a b c : ℝ}
    (hsum : a + b + c ≠ 0)
    (hsat : koidePerpendicularSq a b c = koideParallelSq a b c) :
    koideQuadratic a b c / (a + b + c) ^ 2 = (2 : ℝ) / 3 := by
  have hpoly := (koide_saturation_iff_polynomial a b c).mp hsat
  have hsq : (a + b + c) ^ 2 ≠ 0 := pow_ne_zero 2 hsum
  field_simp
  nlinarith

/--
O ramo pesado explícito satisfaz a equação de saturação. Aqui `a,b` são as
raízes quadradas das duas razões conhecidas.
-/
theorem koide_heavy_branch_satisfies
    {a b : ℝ} (ha : 0 ≤ a) (hb : 0 ≤ b) :
    let disc := 3 * a ^ 2 + 12 * a * b + 3 * b ^ 2
    let c := 2 * (a + b) + Real.sqrt disc
    3 * koideQuadratic a b c = 2 * (a + b + c) ^ 2 := by
  dsimp
  have hdisc : 0 ≤ 3 * a ^ 2 + 12 * a * b + 3 * b ^ 2 := by
    positivity
  have hsqrt :
      (Real.sqrt (3 * a ^ 2 + 12 * a * b + 3 * b ^ 2)) ^ 2 =
        3 * a ^ 2 + 12 * a * b + 3 * b ^ 2 :=
    Real.sq_sqrt hdisc
  unfold koideQuadratic
  nlinarith

end GDQ
