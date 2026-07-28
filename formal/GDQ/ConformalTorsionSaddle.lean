import GDQ.ConformalOfficialDensity
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Calculus.Deriv.MeanValue
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.DerivativeTest
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Tactic

namespace GDQ

/-!
# Sela torsional conformal normalizada

Este módulo trata somente a família conformal já construída:

`g(a) = exp (2 a x⁰) δ`, `H(a) = dᶜ_J ω(a)`.

O cálculo é feito numa folha euclidiana positiva, sobre
`ℝ⁴ × T⁴`, com Haar do toro normalizada. A largura gaussiana é `τ > 0`
e o parâmetro positivo do contorno é escrito `z = q τ`.

O vínculo `∫ 𝒰 dV_g = 1` é imposto antes da variação. Portanto a constante
de normalização de `Re f` varia com `a`; mantê-la fixa produziria uma
variação fora do espaço físico normalizado.

Depois das integrais gaussianas, a dependência não constante da ação oficial
é a função abaixo, com `u = τ a²`. O termo `fBase` é independente de `a` e
não afeta a equação de sela.
-/

/-- Ação oficial reduzida na subvariedade normalizada, salvo um prefator
positivo independente de `a`. -/
noncomputable def normalizedTorsionReducedAction
    (q fBase u : ℝ) : ℝ :=
  q * Real.exp (-28 * u) * (2 - 24 * u) +
    fBase - 2 + 128 * u

/-- Derivada da ação reduzida em relação a `u = τ a²`. -/
noncomputable def normalizedTorsionSlope
    (q u : ℝ) : ℝ :=
  q * Real.exp (-28 * u) * (672 * u - 80) + 128

/-- Derivada da inclinação em relação a `u`. -/
noncomputable def normalizedTorsionSlopeDerivative
    (q u : ℝ) : ℝ :=
  q * Real.exp (-28 * u) * (2912 - 18816 * u)

theorem normalizedTorsionReducedAction_hasDerivAt
    (q fBase u : ℝ) :
    HasDerivAt (normalizedTorsionReducedAction q fBase)
      (normalizedTorsionSlope q u) u := by
  unfold normalizedTorsionReducedAction normalizedTorsionSlope
  have hexp :
      HasDerivAt (fun x : ℝ ↦ Real.exp (-28 * x))
        (-28 * Real.exp (-28 * u)) u := by
    simpa [Function.comp_def, mul_comm] using
      (Real.hasDerivAt_exp (-28 * u)).comp u
        ((hasDerivAt_id u).const_mul (-28))
  have h :=
    ((hexp.const_mul q).mul
      (hasDerivAt_const u 2 |>.sub
        ((hasDerivAt_id u).const_mul 24))).add
      (hasDerivAt_const u (fBase - 2) |>.add
        ((hasDerivAt_id u).const_mul 128))
  apply (h.congr_of_eventuallyEq ?_).congr_deriv
  · simp only [Pi.sub_apply, id_eq, mul_one, zero_sub, zero_add]
    ring
  · exact Filter.Eventually.of_forall (fun x ↦ by
      change
        q * Real.exp (-28 * x) * (2 - 24 * x) +
            fBase - 2 + 128 * x =
          q * Real.exp (-28 * x) * (2 - 24 * x) +
            (fBase - 2 + 128 * x)
      ring)

theorem normalizedTorsionSlope_hasDerivAt
    (q u : ℝ) :
    HasDerivAt (normalizedTorsionSlope q)
      (normalizedTorsionSlopeDerivative q u) u := by
  unfold normalizedTorsionSlope normalizedTorsionSlopeDerivative
  have hexp :
      HasDerivAt (fun x : ℝ ↦ Real.exp (-28 * x))
        (-28 * Real.exp (-28 * u)) u := by
    simpa [Function.comp_def, mul_comm] using
      (Real.hasDerivAt_exp (-28 * u)).comp u
        ((hasDerivAt_id u).const_mul (-28))
  have h :=
    ((hexp.const_mul q).mul
      ((hasDerivAt_id u).const_mul 672 |>.sub_const 80)).add_const 128
  apply (h.congr_of_eventuallyEq ?_).congr_deriv
  · simp only [id_eq, mul_one]
    ring
  · exact Filter.Eventually.of_forall (fun x ↦ by
      change
        q * Real.exp (-28 * x) * (672 * x - 80) + 128 =
          q * Real.exp (-28 * x) * (672 * x - 80) + 128
      rfl)

@[simp] theorem normalizedTorsionSlope_zero (q : ℝ) :
    normalizedTorsionSlope q 0 = 128 - 80 * q := by
  simp [normalizedTorsionSlope]
  ring

@[simp] theorem normalizedTorsionSlope_upper (q : ℝ) :
    normalizedTorsionSlope q (5 / 42 : ℝ) = 128 := by
  rw [normalizedTorsionSlope]
  norm_num

/--
Acima do limiar `q > 8/5`, a inclinação é negativa em `u=0` e positiva em
`u=5/42`. Portanto existe uma raiz estritamente interna.
-/
theorem exists_normalized_nonzero_torsion_root
    {q : ℝ} (hq : 8 / 5 < q) :
    ∃ u : ℝ, 0 < u ∧ u < 5 / 42 ∧
      normalizedTorsionSlope q u = 0 := by
  have hzero : normalizedTorsionSlope q 0 < 0 := by
    rw [normalizedTorsionSlope_zero]
    linarith
  have hupper : 0 < normalizedTorsionSlope q (5 / 42 : ℝ) := by
    rw [normalizedTorsionSlope_upper]
    norm_num
  have hcont : Continuous (normalizedTorsionSlope q) := by
    unfold normalizedTorsionSlope
    fun_prop
  have hle : (0 : ℝ) ≤ 5 / 42 := by norm_num
  have hmem :
      (0 : ℝ) ∈
        Set.Icc (normalizedTorsionSlope q 0)
          (normalizedTorsionSlope q (5 / 42 : ℝ)) := by
    exact ⟨hzero.le, hupper.le⟩
  obtain ⟨u, huIcc, hu⟩ :=
    (intermediate_value_Icc hle hcont.continuousOn) hmem
  refine ⟨u, ?_, ?_, hu⟩
  · rcases huIcc with ⟨hu0, _⟩
    exact lt_of_le_of_ne hu0 (fun h ↦ by
      subst u
      exact hzero.ne hu)
  · rcases huIcc with ⟨_, huU⟩
    exact lt_of_le_of_ne huU (fun h ↦ by
      subst u
      exact hupper.ne' hu)

/-- Em todo o intervalo onde nasce a raiz não nula, a inclinação é
estritamente crescente quando `q>0`. -/
theorem normalizedTorsionSlopeDerivative_pos
    {q u : ℝ} (hq : 0 < q) (huU : u ≤ 5 / 42) :
    0 < normalizedTorsionSlopeDerivative q u := by
  unfold normalizedTorsionSlopeDerivative
  have hexp : 0 < Real.exp (-28 * u) := Real.exp_pos _
  have hlin : 0 < 2912 - 18816 * u := by
    linarith
  positivity

/-- A inclinação é estritamente crescente no intervalo que contém o ramo
torsional. -/
theorem normalizedTorsionSlope_strictMonoOn
    {q : ℝ} (hq : 0 < q) :
    StrictMonoOn (normalizedTorsionSlope q)
      (Set.Icc (0 : ℝ) (5 / 42)) := by
  apply strictMonoOn_of_deriv_pos (convex_Icc (0 : ℝ) (5 / 42))
  · exact
      (continuous_iff_continuousAt.mpr
        (fun u ↦
          (normalizedTorsionSlope_hasDerivAt q u).continuousAt)).continuousOn
  · intro u hu
    have huIoo : u ∈ Set.Ioo (0 : ℝ) (5 / 42) := by
      simpa only [interior_Icc, show (0 : ℝ) < 5 / 42 by norm_num]
        using hu
    rw [(normalizedTorsionSlope_hasDerivAt q u).deriv]
    exact normalizedTorsionSlopeDerivative_pos hq huIoo.2.le

/-- A raiz física no intervalo `0<u<5/42` é única. -/
theorem normalized_nonzero_torsion_root_unique
    {q u v : ℝ} (hq : 0 < q)
    (hu0 : 0 < u) (huU : u < 5 / 42)
    (hv0 : 0 < v) (hvU : v < 5 / 42)
    (hu : normalizedTorsionSlope q u = 0)
    (hv : normalizedTorsionSlope q v = 0) :
    u = v := by
  exact
    (normalizedTorsionSlope_strictMonoOn hq).injOn
      ⟨hu0.le, huU.le⟩ ⟨hv0.le, hvU.le⟩
      (hu.trans hv.symm)

/--
Uma raiz interna da inclinação fornece duas amplitudes torsionais
`a = ±sqrt(u/τ)`. O coeficiente da segunda variação na direção `a` é positivo.
-/
theorem normalizedTorsionSaddle_secondCoefficient_pos
    {q τ u : ℝ} (hq : 0 < q) (hτ : 0 < τ)
    (hu0 : 0 < u) (huU : u < 5 / 42) :
    0 <
      4 * τ * u * normalizedTorsionSlopeDerivative q u := by
  have hslope :
      0 < normalizedTorsionSlopeDerivative q u :=
    normalizedTorsionSlopeDerivative_pos hq huU.le
  have hfront : 0 < 4 * τ * u := by positivity
  exact mul_pos hfront hslope

/-- Primeira variação da ação reduzida quando se retorna de `u` para a
amplitude geométrica `a`, com `u=τa²`. -/
noncomputable def normalizedTorsionFirstVariationInA
    (q τ a : ℝ) : ℝ :=
  2 * τ * a * normalizedTorsionSlope q (τ * a ^ 2)

/-- Uma raiz interna é um mínimo local da ação reduzida como função de
`u=τa²`. -/
theorem normalizedTorsion_root_isLocalMin
    {q fBase u : ℝ} (hq : 0 < q)
    (huU : u < 5 / 42)
    (hroot : normalizedTorsionSlope q u = 0) :
    IsLocalMin (normalizedTorsionReducedAction q fBase) u := by
  apply isLocalMin_of_deriv_deriv_pos
  · have hderiv :
        deriv (normalizedTorsionReducedAction q fBase) =
          normalizedTorsionSlope q := by
      funext x
      exact
        (normalizedTorsionReducedAction_hasDerivAt
          q fBase x).deriv
    rw [hderiv, (normalizedTorsionSlope_hasDerivAt q u).deriv]
    exact normalizedTorsionSlopeDerivative_pos hq huU.le
  · exact
      (normalizedTorsionReducedAction_hasDerivAt
        q fBase u).deriv.trans hroot
  · exact
      (normalizedTorsionReducedAction_hasDerivAt
        q fBase u).continuousAt

/-- Para cada `τ>0` e cada contorno acima do limiar existe um ramo positivo
`a_*>0`; o ramo negativo segue da paridade da ação. -/
theorem exists_positive_normalized_torsion_saddle
    {q τ : ℝ} (hq : 8 / 5 < q) (hτ : 0 < τ) :
    ∃ a : ℝ,
      0 < a ∧
      normalizedTorsionFirstVariationInA q τ a = 0 ∧
      0 <
        4 * τ * (τ * a ^ 2) *
          normalizedTorsionSlopeDerivative q (τ * a ^ 2) := by
  obtain ⟨u, hu0, huU, hroot⟩ :=
    exists_normalized_nonzero_torsion_root hq
  let a : ℝ := Real.sqrt (u / τ)
  have ha : 0 < a := by
    exact Real.sqrt_pos.2 (div_pos hu0 hτ)
  have huEq : τ * a ^ 2 = u := by
    dsimp [a]
    rw [Real.sq_sqrt (div_nonneg hu0.le hτ.le)]
    field_simp
  have hqpos : 0 < q := by linarith
  refine ⟨a, ha, ?_, ?_⟩
  · unfold normalizedTorsionFirstVariationInA
    rw [huEq, hroot]
    ring
  · rw [huEq]
    exact
      normalizedTorsionSaddle_secondCoefficient_pos
        hqpos hτ hu0 huU

/-- O limiar `q=8/5` é exatamente o ponto em que a rigidez quadrática do
ramo sem torção muda de sinal. -/
theorem normalizedTorsion_zeroMode_threshold :
    normalizedTorsionSlope (8 / 5 : ℝ) 0 = 0 := by
  rw [normalizedTorsionSlope_zero]
  norm_num

end GDQ
