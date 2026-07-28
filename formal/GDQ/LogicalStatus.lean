import Mathlib.Data.List.Basic
import Mathlib.Tactic

namespace GDQ

/-!
# Estado lógico da GDQ

Este módulo não acrescenta física. Ele torna verificável a taxonomia usada no
Capítulo 26 e a cadeia mínima exigida para uma afirmação preditiva forte.
-/

/-- Classes editoriais e científicas mutuamente distintas. -/
inductive ClaimClass where
  | axiom
  | definition
  | derivation
  | conditionalTheorem
  | effectiveReduction
  | numericalEvidence
  | inverseEngineering
  | phenomenologicalComparison
  | futureProgram
  deriving DecidableEq, Repr

/-- Status de fechamento usado nos documentos canônicos. -/
inductive ClosureStatus where
  | closed
  | structurallyClosed
  | conditionallyClosed
  | partiallyResolved
  | open
  | futureProgram
  deriving DecidableEq, Repr

/--
Os dois axiomas centrais são separados dos dados que especificam um problema
concreto.
-/
structure CoreAxioms where
  officialAction : Prop
  hermitianBismutClass : Prop

/-- Contorno, topologia e calibração pertencem ao problema, não à ação. -/
structure ProblemData where
  causalContour : Prop
  admissibleTopology : Prop
  boundaryConditions : Prop
  metrologicalCalibration : Prop

/-- Cadeia completa exigida para uma previsão forte sem pós-ajuste. -/
structure ClosureChain where
  officialAction : Prop
  admissibleBackground : Prop
  physicalHessian : Prop
  operatorAndDomain : Prop
  boundaryConditions : Prop
  stableSpectrum : Prop
  observableWithoutPostFit : Prop

def StrongPredictionReady (chain : ClosureChain) : Prop :=
  chain.officialAction
    ∧ chain.admissibleBackground
    ∧ chain.physicalHessian
    ∧ chain.operatorAndDomain
    ∧ chain.boundaryConditions
    ∧ chain.stableSpectrum
    ∧ chain.observableWithoutPostFit

theorem strongPredictionReady_officialAction
    {chain : ClosureChain} (h : StrongPredictionReady chain) :
    chain.officialAction := h.1

theorem strongPredictionReady_all_links
    {chain : ClosureChain} (h : StrongPredictionReady chain) :
    chain.admissibleBackground
      ∧ chain.physicalHessian
      ∧ chain.operatorAndDomain
      ∧ chain.boundaryConditions
      ∧ chain.stableSpectrum
      ∧ chain.observableWithoutPostFit := h.2

theorem not_strongPredictionReady_of_missing_background
    {chain : ClosureChain} (hmissing : ¬chain.admissibleBackground) :
    ¬StrongPredictionReady chain := by
  intro h
  exact hmissing h.2.1

theorem not_strongPredictionReady_of_postfit
    {chain : ClosureChain} (hpostfit : ¬chain.observableWithoutPostFit) :
    ¬StrongPredictionReady chain := by
  intro h
  exact hpostfit h.2.2.2.2.2.2

/-- Condições mínimas para chamar uma projeção de redução controlada. -/
structure ReductionData where
  preservesOfficialAction : Prop
  declaresDomain : Prop
  declaresBoundary : Prop
  usesPhysicalProjector : Prop

def ControlledReduction (reduction : ReductionData) : Prop :=
  reduction.preservesOfficialAction
    ∧ reduction.declaresDomain
    ∧ reduction.declaresBoundary
    ∧ reduction.usesPhysicalProjector

theorem controlledReduction_preserves_action
    {reduction : ReductionData} (h : ControlledReduction reduction) :
    reduction.preservesOfficialAction := h.1

theorem not_controlledReduction_of_changed_action
    {reduction : ReductionData}
    (hchanged : ¬reduction.preservesOfficialAction) :
    ¬ControlledReduction reduction := by
  intro h
  exact hchanged h.1

/--
Trocar os dados externos não altera, por construção, o registro dos axiomas
centrais. O teorema é estrutural: a ação e o contorno vivem em tipos distintos.
-/
def attachProblemData
    (core : CoreAxioms) (data : ProblemData) :
    CoreAxioms × ProblemData :=
  (core, data)

theorem attachProblemData_core
    (core : CoreAxioms) (data : ProblemData) :
    (attachProblemData core data).1 = core := rfl

/-- Um bom número, isoladamente, permanece evidência numérica. -/
theorem numericalEvidence_ne_axiom :
    ClaimClass.numericalEvidence ≠ ClaimClass.axiom := by decide

theorem effectiveReduction_ne_axiom :
    ClaimClass.effectiveReduction ≠ ClaimClass.axiom := by decide

theorem conditionalTheorem_ne_openStatus :
    ClosureStatus.conditionallyClosed ≠ ClosureStatus.open := by decide

end GDQ
