import Mathlib.Algebra.Star.Basic
import Mathlib.Tactic

namespace GDQ

/-!
# Isomorfismo operacional setorial GDQ--Yang--Mills

O módulo trabalha apenas com as álgebras reduzidas de observáveis. Ele não
identifica as ações fundamentais nem os espaços brutos de campos.
-/

variable {YM GDQObs : Type*}
  [Monoid YM] [Star YM]
  [Monoid GDQObs] [Star GDQObs]

/-- Isomorfismo unital, multiplicativo e compatível com a involução. -/
structure SectorStarIsomorphism where
  toGDQ : YM → GDQObs
  toYM : GDQObs → YM
  left_inv : Function.LeftInverse toYM toGDQ
  right_inv : Function.RightInverse toYM toGDQ
  map_one : toGDQ 1 = 1
  map_mul : ∀ x y, toGDQ (x * y) = toGDQ x * toGDQ y
  map_star : ∀ x, toGDQ (star x) = star (toGDQ x)

/-- A equivalência setorial é bijetiva. -/
theorem sectorStarIsomorphism_bijective
    (H : SectorStarIsomorphism (YM := YM) (GDQObs := GDQObs)) :
    Function.Bijective H.toGDQ :=
  ⟨H.left_inv.injective, H.right_inv.surjective⟩

/-- Estado YM transportado do estado GDQ pela equivalência reduzida. -/
def transportedYMState
    (H : SectorStarIsomorphism (YM := YM) (GDQObs := GDQObs))
    (omegaGDQ : GDQObs → ℝ) : YM → ℝ :=
  fun x => omegaGDQ (H.toGDQ x)

/-- A normalização do estado é preservada. -/
theorem transportedYMState_normalized
    (H : SectorStarIsomorphism (YM := YM) (GDQObs := GDQObs))
    (omegaGDQ : GDQObs → ℝ)
    (hnorm : omegaGDQ 1 = 1) :
    transportedYMState H omegaGDQ 1 = 1 := by
  simp [transportedYMState, H.map_one, hnorm]

/-- A positividade sobre elementos `x* x` é preservada pelo transporte. -/
theorem transportedYMState_positive
    (H : SectorStarIsomorphism (YM := YM) (GDQObs := GDQObs))
    (omegaGDQ : GDQObs → ℝ)
    (hpos : ∀ y, 0 ≤ omegaGDQ (star y * y))
    (x : YM) :
    0 ≤ transportedYMState H omegaGDQ (star x * x) := by
  unfold transportedYMState
  rw [H.map_mul, H.map_star]
  exact hpos (H.toGDQ x)

/-- Produtos finitos de observáveis são transportados multiplicativamente. -/
theorem sectorStarIsomorphism_map_three
    (H : SectorStarIsomorphism (YM := YM) (GDQObs := GDQObs))
    (x y z : YM) :
    H.toGDQ (x * y * z) = H.toGDQ x * H.toGDQ y * H.toGDQ z := by
  rw [H.map_mul, H.map_mul]

end GDQ
