import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

namespace GDQ

/-!
# Regra de Born por traço em dimensão finita

Este módulo estende o setor puro de `FiniteBorn.lean` ao setor misto
finito-dimensional. A matriz densidade e os projetores são reais neste núcleo
algébrico; a mesma prova vale sobre matrizes Hermitianas complexas depois de
tomar a parte real do traço.

A positividade de `Tr (ρ P)` é uma hipótese espectral explícita. Ela não é
deduzida apenas da normalização: fisicamente corresponde a `ρ ≥ 0` e `P ≥ 0`.
-/

variable {n outcome : Type*} [Fintype n] [DecidableEq n]
  [Fintype outcome]

/-- Matriz densidade finita normalizada. -/
structure FiniteDensityMatrix where
  matrix : Matrix n n ℝ
  trace_one : Matrix.trace matrix = 1

/--
Medição projetiva finita resolvendo a identidade. A positividade dos pesos
relativos à matriz densidade é registrada sem esconder a hipótese espectral.
-/
structure FiniteProjectiveMeasurement (ρ : FiniteDensityMatrix (n := n)) where
  projector : outcome → Matrix n n ℝ
  complete : ∑ i, projector i = 1
  trace_nonneg : ∀ i, 0 ≤ Matrix.trace (ρ.matrix * projector i)

/-- Peso operacional de Born de um resultado projetivo. -/
noncomputable def mixedBornTraceWeight
    (ρ : FiniteDensityMatrix (n := n))
    (P : FiniteProjectiveMeasurement (outcome := outcome) ρ)
    (i : outcome) : ℝ :=
  Matrix.trace (ρ.matrix * P.projector i)

/-- Os pesos de Born por traço são não negativos. -/
theorem mixedBornTraceWeight_nonneg
    (ρ : FiniteDensityMatrix (n := n))
    (P : FiniteProjectiveMeasurement (outcome := outcome) ρ)
    (i : outcome) :
    0 ≤ mixedBornTraceWeight ρ P i :=
  P.trace_nonneg i

/-- Uma resolução projetiva da identidade normaliza os pesos por traço. -/
theorem mixedBornTraceWeights_sum_one
    (ρ : FiniteDensityMatrix (n := n))
    (P : FiniteProjectiveMeasurement (outcome := outcome) ρ) :
    ∑ i, mixedBornTraceWeight ρ P i = 1 := by
  unfold mixedBornTraceWeight
  rw [← Matrix.trace_sum]
  have hmul :
      (∑ i, ρ.matrix * P.projector i) =
        ρ.matrix * (∑ i, P.projector i) := by
    rw [Matrix.mul_sum]
  rw [hmul, P.complete, mul_one, ρ.trace_one]

/-- Cada peso normalizado pertence ao intervalo `[0,1]`. -/
theorem mixedBornTraceWeight_le_one
    [DecidableEq outcome]
    (ρ : FiniteDensityMatrix (n := n))
    (P : FiniteProjectiveMeasurement (outcome := outcome) ρ)
    (i : outcome) :
    mixedBornTraceWeight ρ P i ≤ 1 := by
  have hsum := mixedBornTraceWeights_sum_one ρ P
  calc
    mixedBornTraceWeight ρ P i
        ≤ ∑ j ∈ Finset.univ, mixedBornTraceWeight ρ P j := by
          exact Finset.single_le_sum
            (fun j _ => mixedBornTraceWeight_nonneg ρ P j)
            (Finset.mem_univ i)
    _ = 1 := hsum

end GDQ
