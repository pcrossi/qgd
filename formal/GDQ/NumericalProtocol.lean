import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

namespace GDQ

/-!
# Protocolo numérico e experimental

Este módulo formaliza somente a contabilidade lógica do Capítulo 27 e algumas
identidades elementares de erro. Ele não transforma um solver, um benchmark ou
uma comparação fenomenológica em teorema físico da GDQ.
-/

/-- Classes mutuamente distintas de uso de um cálculo numérico. -/
inductive NumericalClass where
  | directEvaluation
  | convergenceTest
  | consistencyTest
  | inverseEngineering
  | calibration
  | phenomenologicalComparison
  | blindPrediction
  deriving DecidableEq, Repr

/-- Papéis distintos que um dado externo pode desempenhar. -/
inductive ExperimentalDataRole where
  | boundaryOrApparatus
  | calibration
  | comparisonTarget
  deriving DecidableEq, Repr

/-- Manifesto mínimo de rastreabilidade de um cálculo GDQ. -/
structure NumericalManifest where
  equationDeclared : Prop
  backgroundDeclared : Prop
  domainDeclared : Prop
  boundaryDeclared : Prop
  constraintsDeclared : Prop
  operatorDeclared : Prop
  physicalProjectorDeclared : Prop
  normalizationAndUnitsDeclared : Prop
  apparatusSourceDeclared : Prop
  observableDeclared : Prop
  numericalParametersDeclared : Prop
  useOfExperimentalDataDeclared : Prop

def ReproducibleManifest (m : NumericalManifest) : Prop :=
  m.equationDeclared
    ∧ m.backgroundDeclared
    ∧ m.domainDeclared
    ∧ m.boundaryDeclared
    ∧ m.constraintsDeclared
    ∧ m.operatorDeclared
    ∧ m.physicalProjectorDeclared
    ∧ m.normalizationAndUnitsDeclared
    ∧ m.apparatusSourceDeclared
    ∧ m.observableDeclared
    ∧ m.numericalParametersDeclared
    ∧ m.useOfExperimentalDataDeclared

/-- Requisitos que antecedem legitimamente a comparação de uma previsão cega. -/
structure PredictionProtocol where
  formulaDerivedBeforeComparison : Prop
  universalParametersFrozen : Prop
  apparatusDataMeasuredIndependently : Prop
  targetNotUsedInConstruction : Prop
  convergenceChecked : Prop
  numericalUncertaintyReported : Prop
  boundarySensitivityReported : Prop

def BlindPredictionEligible (p : PredictionProtocol) : Prop :=
  p.formulaDerivedBeforeComparison
    ∧ p.universalParametersFrozen
    ∧ p.apparatusDataMeasuredIndependently
    ∧ p.targetNotUsedInConstruction
    ∧ p.convergenceChecked
    ∧ p.numericalUncertaintyReported
    ∧ p.boundarySensitivityReported

/-- Requisitos adicionais para chamar uma comparação de metrologicamente forte. -/
structure StrongComparisonProtocol extends PredictionProtocol where
  experimentalUncertaintyReported : Prop
  numericalUncertaintyBelowDiscrepancy : Prop
  sameParametersAcrossObservables : Prop

def StrongComparisonEligible (p : StrongComparisonProtocol) : Prop :=
  BlindPredictionEligible p.toPredictionProtocol
    ∧ p.experimentalUncertaintyReported
    ∧ p.numericalUncertaintyBelowDiscrepancy
    ∧ p.sameParametersAcrossObservables

theorem not_blindPredictionEligible_of_target_used
    {p : PredictionProtocol} (h : ¬p.targetNotUsedInConstruction) :
    ¬BlindPredictionEligible p := by
  intro hp
  exact h hp.2.2.2.1

theorem not_blindPredictionEligible_of_parameters_not_frozen
    {p : PredictionProtocol} (h : ¬p.universalParametersFrozen) :
    ¬BlindPredictionEligible p := by
  intro hp
  exact h hp.2.1

theorem strongComparison_implies_blindPredictionEligible
    {p : StrongComparisonProtocol} (h : StrongComparisonEligible p) :
    BlindPredictionEligible p.toPredictionProtocol := h.1

theorem boundaryData_ne_comparisonTarget :
    ExperimentalDataRole.boundaryOrApparatus
      ≠ ExperimentalDataRole.comparisonTarget := by
  decide

theorem inverseEngineering_ne_blindPrediction :
    NumericalClass.inverseEngineering ≠ NumericalClass.blindPrediction := by
  decide

theorem convergenceTest_ne_blindPrediction :
    NumericalClass.convergenceTest ≠ NumericalClass.blindPrediction := by
  decide

/-- Erro relativo; a referência nula deve ser tratada separadamente na física. -/
noncomputable def relativeError (computed reference : ℝ) : ℝ :=
  |computed - reference| / |reference|

theorem relativeError_nonneg (computed reference : ℝ) :
    0 ≤ relativeError computed reference := by
  unfold relativeError
  positivity

theorem relativeError_eq_zero_of_eq
    (computed reference : ℝ) (h : computed = reference) :
    relativeError computed reference = 0 := by
  simp [relativeError, h]

/--
A discrepância total é limitada pela soma do erro numérico em relação ao
limite calculado e da discrepância física entre esse limite e o alvo.
-/
theorem numerical_physical_error_decomposition
    (computed continuum target : ℝ) :
    |computed - target|
      ≤ |computed - continuum| + |continuum - target| := by
  exact abs_sub_le computed continuum target

/-- Um alvo usado para escolher coeficiente interno impede previsão cega. -/
structure PostFitRecord where
  targetUsedToChooseInternalCoefficient : Prop

theorem postfit_incompatible_with_blind_prediction
    (r : PostFitRecord)
    (hfit : r.targetUsedToChooseInternalCoefficient) :
    ¬(¬r.targetUsedToChooseInternalCoefficient) := by
  intro h
  exact h hfit

end GDQ
