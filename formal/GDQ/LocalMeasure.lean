import GDQ.Spaces
import Mathlib.MeasureTheory.Measure.Haar.Basic
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.Topology.Instances.AddCircle.Real

namespace GDQ

open MeasureTheory

/-!
# Estrutura Borel e medida do bulk local

O setor `ℝ⁴` recebe a medida de Lebesgue. O toro `T⁴` recebe uma medida de
Haar aditiva. A medida de referência do bulk é o produto dessas duas medidas.
Ela é uma medida de referência coordenada; o fator geométrico `sqrt(det g)`
continua pertencendo à densidade oficial.
-/

/-- O período angular `2π` é estritamente positivo. -/
instance anglePeriodPositive : Fact (0 < 2 * Real.pi) :=
  ⟨mul_pos (by norm_num) Real.pi_pos⟩

/-- O círculo angular é compacto como quociente `ℝ/(2πℤ)`. -/
noncomputable instance angleCompactSpace : CompactSpace Real.Angle := by
  change CompactSpace (AddCircle (2 * Real.pi))
  infer_instance

/-- Estrutura mensurável Borel explícita no toro. -/
noncomputable instance torusMeasurableSpace (n : Nat) :
    MeasurableSpace (Torus n) :=
  borel (Torus n)

/-- A estrutura mensurável escolhida no toro é precisamente a Boreliana. -/
instance torusBorelSpace (n : Nat) : BorelSpace (Torus n) where
  measurable_eq := rfl

/-- Estrutura produto mensurável explícita no bulk local. -/
noncomputable instance localPointMeasurableSpace :
    MeasurableSpace LocalBulkModel :=
  MeasurableSpace.prod
    (inferInstance : MeasurableSpace Euclidean4)
    (torusMeasurableSpace 4)

/-- Medida de Haar de referência no toro de dimensão `n`. -/
noncomputable def torusHaarMeasure (n : Nat) : Measure (Torus n) :=
  Measure.addHaar

/--
Medida de referência no bulk local `ℝ⁴ × T⁴`.

O volume métrico físico ainda é obtido multiplicando por `sqrt(det g)` na
densidade da ação.
-/
noncomputable def localBulkReferenceMeasure : Measure LocalBulkModel :=
  (MeasureTheory.volume : Measure Euclidean4).prod (torusHaarMeasure 4)

end GDQ
