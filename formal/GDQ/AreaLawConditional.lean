import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Topology.Instances.ENNReal.Lemmas
import Mathlib.Tactic

namespace GDQ

/-!
# Lei de área condicional

Uma thimble tubular estável fornece uma resposta positiva exponencial. Este
módulo prova a identidade de energia livre e o limite de tensão quando os
termos de perímetro e resto são subextensivos.
-/

/-- Módulo reduzido da resposta de holonomia tubular. -/
noncomputable def tubularHolonomyResponse
    (sigma mu area perimeter remainder : ℝ) : ℝ :=
  Real.exp (-(sigma * area + mu * perimeter + remainder))

/-- Energia livre exata associada à resposta tubular positiva. -/
theorem tubular_free_energy_exact
    (sigma mu area perimeter remainder : ℝ) :
    -Real.log (tubularHolonomyResponse sigma mu area perimeter remainder) =
      sigma * area + mu * perimeter + remainder := by
  simp [tubularHolonomyResponse]

/-- Energia livre por área, antes do limite termodinâmico. -/
theorem tubular_free_energy_per_area
    {sigma mu area perimeter remainder : ℝ}
    (harea : area ≠ 0) :
    -Real.log (tubularHolonomyResponse sigma mu area perimeter remainder) / area =
      sigma + mu * (perimeter / area) + remainder / area := by
  rw [tubular_free_energy_exact]
  field_simp

/--
Se perímetro/área e resto/área desaparecem, a energia livre por área converge
à tensão efetiva.
-/
theorem tubular_area_law_limit
    {area perimeter remainder : ℕ → ℝ}
    {sigma mu : ℝ}
    (harea : ∀ n, area n ≠ 0)
    (hper :
      Filter.Tendsto (fun n => perimeter n / area n)
        Filter.atTop (nhds 0))
    (hrem :
      Filter.Tendsto (fun n => remainder n / area n)
        Filter.atTop (nhds 0)) :
    Filter.Tendsto
      (fun n =>
        -Real.log
          (tubularHolonomyResponse sigma mu (area n) (perimeter n)
            (remainder n)) / area n)
      Filter.atTop (nhds sigma) := by
  have hconst :
      Filter.Tendsto (fun _ : ℕ => sigma) Filter.atTop (nhds sigma) :=
    tendsto_const_nhds
  have hmu :
      Filter.Tendsto (fun n => mu * (perimeter n / area n))
        Filter.atTop (nhds 0) := by
    simpa using (tendsto_const_nhds.mul hper)
  have hsum := (hconst.add hmu).add hrem
  convert hsum using 1
  funext n
  rw [tubular_free_energy_per_area (harea n)]
  ring_nf

end GDQ
