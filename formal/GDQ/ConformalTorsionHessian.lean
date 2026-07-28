import GDQ.ConformalTorsionSaddle
import Mathlib.Tactic

namespace GDQ

/-!
# Hessiana restrita e critério de acoplamento

Este módulo não declara que a Hessiana física 8D completa já foi calculada.
Ele separa dois resultados:

1. o bloco conformal normalizado, já derivado da ação oficial, é positivo na
   sela torsional;
2. para um segundo modo real acoplado, a positividade da matriz `2 × 2`
   equivale à positividade do complemento de Schur.

O segundo item é um critério a ser preenchido pelos coeficientes físicos das
flutuações métrica, dilatônica e de estrutura complexa. Não é um certificado
de que esses coeficientes já tenham sido avaliados.
-/

/-- Hessiana exata da ação reduzida em `u=τa²`. -/
noncomputable def normalizedTorsionHessianU (q u : ℝ) : ℝ :=
  normalizedTorsionSlopeDerivative q u

theorem normalizedTorsionHessianU_eq_secondDerivative
    (q fBase u : ℝ) :
    deriv (deriv (normalizedTorsionReducedAction q fBase)) u =
      normalizedTorsionHessianU q u := by
  have hfirst :
      deriv (normalizedTorsionReducedAction q fBase) =
        normalizedTorsionSlope q := by
    funext x
    exact
      (normalizedTorsionReducedAction_hasDerivAt q fBase x).deriv
  rw [hfirst, normalizedTorsionHessianU,
    (normalizedTorsionSlope_hasDerivAt q u).deriv]

/-- O bloco Hessiano em `u` é positivo em toda a região física que contém a
raiz torsional. -/
theorem normalizedTorsionHessianU_pos
    {q u : ℝ} (hq : 0 < q) (huU : u ≤ 5 / 42) :
    0 < normalizedTorsionHessianU q u := by
  exact normalizedTorsionSlopeDerivative_pos hq huU

/-- Forma quadrática real de dois blocos escalares acoplados. -/
def coupledHessianQuadratic
    (kaa kab kbb x y : ℝ) : ℝ :=
  kaa * x ^ 2 + 2 * kab * x * y + kbb * y ^ 2

/-- Identidade de completar o quadrado que produz o complemento de Schur. -/
theorem coupledHessianQuadratic_schur
    {kaa kab kbb x y : ℝ} (hkaa : kaa ≠ 0) :
    coupledHessianQuadratic kaa kab kbb x y =
      kaa * (x + kab / kaa * y) ^ 2 +
        (kbb - kab ^ 2 / kaa) * y ^ 2 := by
  unfold coupledHessianQuadratic
  field_simp [hkaa]
  ring

/--
Se o bloco torsional e seu complemento de Schur são positivos, a forma
quadrática acoplada é estritamente positiva fora da origem.
-/
theorem coupledHessianQuadratic_pos
    {kaa kab kbb x y : ℝ}
    (hkaa : 0 < kaa)
    (hschur : 0 < kbb - kab ^ 2 / kaa)
    (hxy : x ≠ 0 ∨ y ≠ 0) :
    0 < coupledHessianQuadratic kaa kab kbb x y := by
  rw [coupledHessianQuadratic_schur hkaa.ne']
  by_cases hy : y = 0
  · have hx : x ≠ 0 := hxy.resolve_right (fun h ↦ h hy)
    subst y
    simpa using mul_pos hkaa (sq_pos_of_ne_zero hx)
  · have hsecond :
        0 < (kbb - kab ^ 2 / kaa) * y ^ 2 :=
      mul_pos hschur (sq_pos_of_ne_zero hy)
    have hfirst :
        0 ≤ kaa * (x + kab / kaa * y) ^ 2 :=
      mul_nonneg hkaa.le (sq_nonneg _)
    linarith

/--
No bloco reduzido, a condição física restante para um modo `y` é
precisamente:

`kbb - kab² / kaa > 0`.

O teorema não atribui valores a `kab` ou `kbb`.
-/
theorem torsionCoupledMode_stable_of_schur
    {q u kab kbb x y : ℝ}
    (hq : 0 < q) (huU : u ≤ 5 / 42)
    (hschur :
      0 <
        kbb - kab ^ 2 / normalizedTorsionHessianU q u)
    (hxy : x ≠ 0 ∨ y ≠ 0) :
    0 <
      coupledHessianQuadratic
        (normalizedTorsionHessianU q u) kab kbb x y := by
  exact coupledHessianQuadratic_pos
    (normalizedTorsionHessianU_pos hq huU) hschur hxy

end GDQ
