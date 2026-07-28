import GDQ.NoetherPhaseCurrent
import GDQ.BoundaryPhaseQuantization

namespace GDQ

/-!
# Stokes, balanço de carga e quantização relativa

`PhaseStokesData` registra a instanciação do teorema de Stokes numa região
concreta com duas folhas e uma parede lateral. Assim a hipótese geométrica
permanece visível.
-/

/-- Dados orientados de Stokes entre duas folhas. -/
structure PhaseStokesData where
  initialCharge : ℝ
  finalCharge : ℝ
  lateralFlux : ℝ
  bulkDivergenceIntegral : ℝ
  stokesIdentity :
    bulkDivergenceIntegral =
      finalCharge - initialCharge + lateralFlux

/-- Corrente conservada no bulk: integral da divergência nula. -/
def PhaseStokesData.IsBulkConserved (D : PhaseStokesData) : Prop :=
  D.bulkDivergenceIntegral = 0

/-- Stokes e conservação local fornecem o balanço orientado. -/
theorem PhaseStokesData.oriented_charge_balance
    (D : PhaseStokesData) (hconserved : D.IsBulkConserved) :
    D.finalCharge - D.initialCharge + D.lateralFlux = 0 := by
  rw [← D.stokesIdentity]
  exact hconserved

/-- Sem fluxo lateral, a carga nas folhas coincide. -/
theorem PhaseStokesData.charge_conserved_of_zero_lateral_flux
    (D : PhaseStokesData)
    (hconserved : D.IsBulkConserved)
    (hlateral : D.lateralFlux = 0) :
    D.finalCharge = D.initialCharge := by
  exact boundaryCharge_conserved_of_zero_lateral_flux
    D.initialCharge D.finalCharge D.lateralFlux
    (D.oriented_charge_balance hconserved) hlateral

/-- Fluxos opostos conservam a carga do sistema objeto--aparelho. -/
theorem composite_charge_conserved_from_opposite_lateral_flux
    (Qobj₁ Qobj₂ Qapp₁ Qapp₂ : ℝ)
    (hobject : Qobj₂ - Qobj₁ + (Qapp₂ - Qapp₁) = 0) :
    Qobj₂ + Qapp₂ = Qobj₁ + Qapp₁ := by
  linarith

/-- Cadeia: Stokes, termo de extremidade e ação exponenciada. -/
theorem relative_phase_quantized_from_stokes
    (D : PhaseStokesData)
    (hconserved : D.IsBulkConserved)
    (hlateral : D.lateralFlux = 0)
    (ℏ phaseIncrement physicalShift : ℝ)
    (hℏ : ℏ ≠ 0)
    (hshift : physicalShift = D.finalCharge * phaseIncrement)
    (hexp :
      boundaryExponentiatedActionShift ℏ physicalShift = 1) :
    D.finalCharge = D.initialCharge ∧
      ∃ n : ℤ,
        D.finalCharge * phaseIncrement =
          n * (2 * Real.pi * ℏ) := by
  refine ⟨D.charge_conserved_of_zero_lateral_flux hconserved hlateral, ?_⟩
  let Q : BoundaryPhaseQuantizationData :=
    { ℏ := ℏ
      charge := D.finalCharge
      phaseIncrement := phaseIncrement
      physicalShift := physicalShift
      planck_ne_zero := hℏ
      physicalShift_is_boundaryTerm := hshift
      exponentiatedInvariant := hexp }
  exact Q.product_quantized

end GDQ
