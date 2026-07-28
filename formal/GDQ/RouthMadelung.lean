import Mathlib.Algebra.BigOperators.Field
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace GDQ

/-!
# Núcleo finito da redução de Routh--Madelung

O manuscrito não afirma `Π = ρ` como identidade universal *off shell*. A
igualdade caracteriza o mínimo do setor hidrodinâmico depois de fixadas a
carga e a normalização. Este módulo certifica o núcleo algébrico finito dessa
afirmação.

Não são formalizados aqui o limite contínuo, o funcional de influência do
aparelho nem a convergência dinâmica ao mínimo. Esses elos continuam
hipóteses explícitas do teorema físico condicional.
-/

open scoped BigOperators

variable {ι : Type*}

/-- Energia quadrática ponderada do momento de fase. -/
noncomputable def weightedPhaseEnergy
    (s : Finset ι) (ρ piField : ι → ℝ) : ℝ :=
  s.sum (fun i => (piField i) ^ 2 / ρ i)

/-- Excesso quadrático em relação à polarização `Π = c ρ`. -/
noncomputable def routhExcess
    (s : Finset ι) (ρ piField : ι → ℝ) (c : ℝ) : ℝ :=
  s.sum (fun i => (piField i - c * ρ i) ^ 2 / ρ i)

/-- O excesso de Routh é não negativo para densidade estritamente positiva. -/
theorem routhExcess_nonneg
    (s : Finset ι) (ρ piField : ι → ℝ) (c : ℝ)
    (hρ : ∀ i ∈ s, 0 < ρ i) :
    0 ≤ routhExcess s ρ piField c := by
  unfold routhExcess
  apply Finset.sum_nonneg
  intro i hi
  exact div_nonneg (sq_nonneg _) (le_of_lt (hρ i hi))

/--
Completação exata do quadrado. A energia é o valor no setor de carga mais o
excesso de Routh.
-/
theorem weightedPhaseEnergy_decomposition
    (s : Finset ι) (ρ piField : ι → ℝ) (c : ℝ)
    (hρ : ∀ i ∈ s, ρ i ≠ 0) :
    weightedPhaseEnergy s ρ piField
      =
      routhExcess s ρ piField c
        + 2 * c * s.sum piField
        - c ^ 2 * s.sum ρ := by
  unfold weightedPhaseEnergy routhExcess
  calc
    s.sum (fun i => (piField i) ^ 2 / ρ i)
        =
        s.sum (fun i =>
          (piField i - c * ρ i) ^ 2 / ρ i
            + 2 * c * piField i - c ^ 2 * ρ i) := by
          apply Finset.sum_congr rfl
          intro i hi
          field_simp [hρ i hi]
          ring
    _ =
        s.sum (fun i => (piField i - c * ρ i) ^ 2 / ρ i)
          + 2 * c * s.sum piField
          - c ^ 2 * s.sum ρ := by
          rw [Finset.sum_sub_distrib, Finset.sum_add_distrib]
          rw [Finset.mul_sum, Finset.mul_sum]

/--
Se a densidade e a carga são normalizadas e `c = 1`, a energia é `1` mais
um excesso não negativo.
-/
theorem normalizedPhaseEnergy_eq_one_add_excess
    (s : Finset ι) (ρ piField : ι → ℝ)
    (hρne : ∀ i ∈ s, ρ i ≠ 0)
    (hρnorm : s.sum ρ = 1)
    (hPiNorm : s.sum piField = 1) :
    weightedPhaseEnergy s ρ piField
      = 1 + routhExcess s ρ piField 1 := by
  rw [weightedPhaseEnergy_decomposition s ρ piField 1 hρne]
  rw [hρnorm, hPiNorm]
  ring

/-- A polarização `Π = ρ` anula exatamente o excesso normalizado. -/
theorem routhExcess_eq_zero_of_polarized
    (s : Finset ι) (ρ piField : ι → ℝ)
    (hPiRho : ∀ i ∈ s, piField i = ρ i) :
    routhExcess s ρ piField 1 = 0 := by
  unfold routhExcess
  apply Finset.sum_eq_zero
  intro i hi
  rw [hPiRho i hi]
  ring

/--
Reciprocamente, excesso nulo e densidade positiva forçam `Π = ρ` em cada
ponto da discretização.
-/
theorem polarized_of_routhExcess_eq_zero
    (s : Finset ι) (ρ piField : ι → ℝ)
    (hρ : ∀ i ∈ s, 0 < ρ i)
    (hzero : routhExcess s ρ piField 1 = 0) :
    ∀ i ∈ s, piField i = ρ i := by
  intro i hi
  have hterm_nonneg :
      ∀ j ∈ s, 0 ≤ (piField j - 1 * ρ j) ^ 2 / ρ j := by
    intro j hj
    exact div_nonneg (sq_nonneg _) (le_of_lt (hρ j hj))
  have hterm_zero :
      (piField i - 1 * ρ i) ^ 2 / ρ i = 0 := by
    apply (Finset.sum_eq_zero_iff_of_nonneg hterm_nonneg).mp
    simpa [routhExcess] using hzero
    exact hi
  have hsquare : (piField i - ρ i) ^ 2 = 0 := by
    have hρne : ρ i ≠ 0 := ne_of_gt (hρ i hi)
    simpa [hρne] using hterm_zero
  nlinarith [sq_nonneg (piField i - ρ i)]

end GDQ
