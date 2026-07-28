import GDQ.ClassicalApparatusResponse
import GDQ.FiniteBorn

namespace GDQ

/-!
# Canais espectrais do aparelho e pesos de Born

Este módulo conecta uma resposta linear já derivada da Hessiana física a uma
medição projetiva finita. A base de canais deve diagonalizar a Hessiana do
aparelho e o estado-resposta deve estar normalizado.

A álgebra então força pesos de Born positivos e normalizados. A estrutura
geral `BasinRealization` abaixo mantém a realização dinâmica como hipótese.
O módulo `GDQ.QNDBornBasins` descarrega essa hipótese para a classe QND
gaussiana finita, sem afirmar o mesmo para todo aparelho.
-/

variable
  {ι H : Type*}
  [Fintype ι]
  [NormedAddCommGroup H]
  [InnerProductSpace ℂ H]

/--
Readout espectral finito produzido por uma Hessiana física complexificada.
-/
structure FiniteApparatusReadout (ι H : Type*)
    [Fintype ι]
    [NormedAddCommGroup H]
    [InnerProductSpace ℂ H] where
  physicalHessian : H →L[ℂ] H
  physicalGreen : H →L[ℂ] H
  hessian_green :
    physicalHessian.comp physicalGreen =
      ContinuousLinearMap.id ℂ H
  classicalSource : H
  channels : OrthonormalBasis ι ℂ H
  channelEnergy : ι → ℝ
  channels_diagonalize :
    ∀ i, physicalHessian (channels i) =
      (channelEnergy i : ℂ) • channels i
  normalized_response :
    ‖physicalGreen classicalSource‖ = 1

/-- Estado operacional produzido pela resposta linear do aparelho. -/
noncomputable def FiniteApparatusReadout.responseState
    (A : FiniteApparatusReadout ι H) : H :=
  A.physicalGreen A.classicalSource

/-- O estado-resposta resolve a equação linearizada com fonte. -/
theorem FiniteApparatusReadout.responseState_solves
    (A : FiniteApparatusReadout ι H) :
    A.physicalHessian A.responseState = A.classicalSource := by
  change
    (A.physicalHessian.comp A.physicalGreen) A.classicalSource =
      A.classicalSource
  rw [A.hessian_green]
  rfl

/-- Peso do registro associado ao canal espectral `i`. -/
noncomputable def FiniteApparatusReadout.recordWeight
    (A : FiniteApparatusReadout ι H) (i : ι) : ℝ :=
  pureBornWeight (A.channels i) A.responseState

/-- Todo registro possui peso não negativo. -/
theorem FiniteApparatusReadout.recordWeight_nonneg
    (A : FiniteApparatusReadout ι H) (i : ι) :
    0 ≤ A.recordWeight i :=
  pureBornWeight_nonneg _ _

/--
Os pesos de todos os canais espectrais do aparelho somam exatamente um.
-/
theorem FiniteApparatusReadout.recordWeights_sum_one
    (A : FiniteApparatusReadout ι H) :
    ∑ i, A.recordWeight i = 1 := by
  exact pureBornWeights_sum_one A.channels A.responseState
    A.normalized_response

/-- Cada peso individual está no intervalo `[0,1]`. -/
theorem FiniteApparatusReadout.recordWeight_le_one
    (A : FiniteApparatusReadout ι H) (i : ι) :
    A.recordWeight i ≤ 1 := by
  exact pureBornWeight_le_one (A.channels i) A.responseState
    (A.channels.norm_eq_one i) A.normalized_response

/--
Hipótese dinâmica de bacias: a medida microscópica da bacia de cada registro
coincide com o peso espectral. Ela é mantida como dado verificável, não como
consequência da diagonalização.
-/
structure BasinRealization
    (A : FiniteApparatusReadout ι H) where
  basinWeight : ι → ℝ
  basin_matches_spectral :
    ∀ i, basinWeight i = A.recordWeight i

/-- Se as bacias realizam os pesos espectrais, suas medidas somam um. -/
theorem BasinRealization.basinWeights_sum_one
    {A : FiniteApparatusReadout ι H}
    (B : BasinRealization A) :
    ∑ i, B.basinWeight i = 1 := by
  simp_rw [B.basin_matches_spectral]
  exact A.recordWeights_sum_one

end GDQ
