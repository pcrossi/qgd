import GDQ.PhaseFirstVariation

namespace GDQ

open scoped BigOperators

/-!
# Corrente de Noether da fase

Identifica-se o coeficiente de `∂η` na primeira variação oficial. A
invariância por deslocamento constante é separada da conservação on shell.
-/

variable {ι Test : Type*} [Fintype ι]

/-- Corrente densitizada extraída da primeira variação. -/
noncomputable def officialPhaseCurrentDensity
    (ℏ ΛC τ kernel volumeDensity : ℝ)
    (metricInv : ι → ι → ℝ) (phaseGradient : ι → ℝ) (i : ι) : ℝ :=
  2 * (ℏ / ΛC ^ 2) * (τ / ℏ ^ 2) * kernel * volumeDensity *
    ∑ j, metricInv i j * phaseGradient j

/-- Corrente vetorial sem o elemento de volume. -/
noncomputable def officialPhaseCurrent
    (ℏ ΛC τ kernel : ℝ)
    (metricInv : ι → ι → ℝ) (phaseGradient : ι → ℝ) (i : ι) : ℝ :=
  2 * (ℏ / ΛC ^ 2) * (τ / ℏ ^ 2) * kernel *
    ∑ j, metricInv i j * phaseGradient j

/-- Forma normalizada usual, válida para `ℏ ≠ 0`. -/
theorem officialPhaseCurrent_eq_normalized
    (ℏ ΛC τ kernel : ℝ)
    (hℏ : ℏ ≠ 0)
    (metricInv : ι → ι → ℝ) (phaseGradient : ι → ℝ) (i : ι) :
    officialPhaseCurrent ℏ ΛC τ kernel metricInv phaseGradient i =
      (2 * τ / (ℏ * ΛC ^ 2)) * kernel *
        ∑ j, metricInv i j * phaseGradient j := by
  unfold officialPhaseCurrent
  field_simp [hℏ]

/-- A primeira variação é o emparelhamento corrente--gradiente teste. -/
theorem officialPhaseFirstVariation_eq_currentPairing
    (ℏ ΛC τ kernel volumeDensity : ℝ)
    (metricInv : ι → ι → ℝ)
    (hmetric : ∀ i j, metricInv i j = metricInv j i)
    (phaseGradient testGradient : ι → ℝ) :
    officialPhaseFirstVariation ℏ ΛC τ kernel volumeDensity metricInv
        phaseGradient testGradient =
      ∑ i,
        officialPhaseCurrentDensity ℏ ΛC τ kernel volumeDensity metricInv
          phaseGradient i * testGradient i := by
  rw [officialPhaseFirstVariation_eq_twice _ _ _ _ _ metricInv hmetric]
  unfold officialPhaseCurrentDensity phaseGradientContraction
  simp_rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i _
  rw [Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro j _
  ring

/-- Gradiente de uma translação global constante. -/
def constantPhaseShiftGradient (ι : Type*) [Fintype ι] : ι → ℝ :=
  0

/-- Deslocamentos globais constantes não alteram a densidade de fase. -/
theorem officialPhaseSectorDensity_constantShift
    (ℏ ΛC τ kernel volumeDensity c : ℝ)
    (metricInv : ι → ι → ℝ) (phaseGradient : ι → ℝ) :
    officialPhaseSectorDensity ℏ ΛC τ kernel volumeDensity metricInv
        (phaseGradient + c • constantPhaseShiftGradient ι) =
      officialPhaseSectorDensity ℏ ΛC τ kernel volumeDensity metricInv
        phaseGradient := by
  simp [constantPhaseShiftGradient]

/-- Estacionariedade fraca para uma classe de funções teste. -/
def PhaseWeakStationary
    (ℏ ΛC τ kernel volumeDensity : ℝ)
    (metricInv : ι → ι → ℝ)
    (phaseGradient : ι → ℝ)
    (testGradient : Test → ι → ℝ) : Prop :=
  ∀ η,
    officialPhaseFirstVariation ℏ ΛC τ kernel volumeDensity metricInv
      phaseGradient (testGradient η) = 0

/-- Conservação fraca da corrente na mesma classe de testes. -/
def PhaseCurrentWeaklyConserved
    (ℏ ΛC τ kernel volumeDensity : ℝ)
    (metricInv : ι → ι → ℝ)
    (phaseGradient : ι → ℝ)
    (testGradient : Test → ι → ℝ) : Prop :=
  ∀ η,
    ∑ i,
      officialPhaseCurrentDensity ℏ ΛC τ kernel volumeDensity metricInv
        phaseGradient i * testGradient η i = 0

/-- A equação variacional fraca equivale à conservação fraca da corrente. -/
theorem phaseWeakStationary_iff_currentWeaklyConserved
    (ℏ ΛC τ kernel volumeDensity : ℝ)
    (metricInv : ι → ι → ℝ)
    (hmetric : ∀ i j, metricInv i j = metricInv j i)
    (phaseGradient : ι → ℝ)
    (testGradient : Test → ι → ℝ) :
    PhaseWeakStationary ℏ ΛC τ kernel volumeDensity metricInv
        phaseGradient testGradient ↔
      PhaseCurrentWeaklyConserved ℏ ΛC τ kernel volumeDensity metricInv
        phaseGradient testGradient := by
  constructor <;> intro h η
  · rw [← officialPhaseFirstVariation_eq_currentPairing
      ℏ ΛC τ kernel volumeDensity metricInv hmetric]
    exact h η
  · rw [officialPhaseFirstVariation_eq_currentPairing
      ℏ ΛC τ kernel volumeDensity metricInv hmetric]
    exact h η

end GDQ
