import Mathlib.Analysis.Normed.Module.Basic
import Mathlib.Tactic

namespace GDQ

/-!
# Fonte clássica, Hessiana física e resposta de interface

Este módulo formaliza a cadeia linear:

`J_app → δΦ = K_phys⁻¹ J_app → R_app`.

Os mapas são dados derivados da segunda variação de um background com
contorno de aparelho. O módulo não adiciona uma fonte à ação fundamental e
não afirma que qualquer operador arbitrário seja uma Hessiana GDQ.
-/

variable
  {E B I : Type*}
  [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedAddCommGroup B] [NormedSpace ℝ B]
  [NormedAddCommGroup I] [NormedSpace ℝ I]

/-- Problema de resposta linear de um aparelho clássico. -/
structure LinearApparatusProblem (E : Type*)
    [NormedAddCommGroup E] [NormedSpace ℝ E] where
  physicalHessian : E →L[ℝ] E
  physicalGreen : E →L[ℝ] E
  hessian_green : physicalHessian.comp physicalGreen =
    ContinuousLinearMap.id ℝ E
  classicalSource : E

/-- Perturbação induzida pela fonte clássica. -/
noncomputable def LinearApparatusProblem.perturbation
    (A : LinearApparatusProblem E) : E :=
  A.physicalGreen A.classicalSource

/-- A resposta construída resolve exatamente a equação linearizada. -/
theorem LinearApparatusProblem.perturbation_solves
    (A : LinearApparatusProblem E) :
    A.physicalHessian A.perturbation = A.classicalSource := by
  change
    (A.physicalHessian.comp A.physicalGreen) A.classicalSource =
      A.classicalSource
  rw [A.hessian_green]
  rfl

/--
Blocos da Hessiana física depois da separação entre traços de fronteira `B`
e graus internos `I`.
-/
structure InterfaceBlockProblem (B I : Type*)
    [NormedAddCommGroup B] [NormedSpace ℝ B]
    [NormedAddCommGroup I] [NormedSpace ℝ I] where
  Kbb : B →L[ℝ] B
  Kbi : I →L[ℝ] B
  Kib : B →L[ℝ] I
  Kii : I →L[ℝ] I
  KiiInv : I →L[ℝ] I
  Kii_rightInverse :
    Kii.comp KiiInv = ContinuousLinearMap.id ℝ I

/-- Resposta interna estacionária a um traço de fronteira prescrito. -/
noncomputable def InterfaceBlockProblem.interiorResponse
    (K : InterfaceBlockProblem B I) (b : B) : I :=
  -(K.KiiInv (K.Kib b))

/--
A resposta interna satisfaz a equação de Euler--Lagrange do bloco eliminado.
-/
theorem InterfaceBlockProblem.interior_stationary
    (K : InterfaceBlockProblem B I) (b : B) :
    K.Kib b + K.Kii (K.interiorResponse b) = 0 := by
  rw [InterfaceBlockProblem.interiorResponse]
  rw [map_neg]
  have hinverse := congrArg
    (fun T : I →L[ℝ] I => T (K.Kib b))
    K.Kii_rightInverse
  change K.Kii (K.KiiInv (K.Kib b)) = K.Kib b at hinverse
  rw [hinverse]
  exact add_neg_cancel _

/-- Operador efetivo de Schur/Dirichlet--to--Neumann na interface. -/
noncomputable def InterfaceBlockProblem.schurResponse
    (K : InterfaceBlockProblem B I) : B →L[ℝ] B :=
  K.Kbb - K.Kbi.comp (K.KiiInv.comp K.Kib)

/-- Resíduo de fronteira depois de resolver o interior on shell. -/
noncomputable def InterfaceBlockProblem.boundaryResidual
    (K : InterfaceBlockProblem B I) (b : B) : B :=
  K.Kbb b + K.Kbi (K.interiorResponse b)

/--
Eliminar o interior produz exatamente o complemento de Schur, sem parâmetro
adicional de interface.
-/
theorem InterfaceBlockProblem.boundaryResidual_eq_schur
    (K : InterfaceBlockProblem B I) (b : B) :
    K.boundaryResidual b = K.schurResponse b := by
  simp [InterfaceBlockProblem.boundaryResidual,
    InterfaceBlockProblem.interiorResponse,
    InterfaceBlockProblem.schurResponse, sub_eq_add_neg]

/-- Problema reduzido de resposta somente no espaço de fronteira. -/
structure ReducedBoundaryResponse (B : Type*)
    [NormedAddCommGroup B] [NormedSpace ℝ B] where
  response : B →L[ℝ] B
  responseInv : B →L[ℝ] B
  response_inverse :
    response.comp responseInv = ContinuousLinearMap.id ℝ B
  boundarySource : B

/-- Traço de fronteira induzido pela fonte do aparelho. -/
noncomputable def ReducedBoundaryResponse.boundaryField
    (R : ReducedBoundaryResponse B) : B :=
  R.responseInv R.boundarySource

/-- O traço construído resolve a equação efetiva de interface. -/
theorem ReducedBoundaryResponse.boundaryField_solves
    (R : ReducedBoundaryResponse B) :
    R.response R.boundaryField = R.boundarySource := by
  change (R.response.comp R.responseInv) R.boundarySource =
    R.boundarySource
  rw [R.response_inverse]
  rfl

end GDQ
