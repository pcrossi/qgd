import GDQ.LogicalStatus
import GDQ.NumericalProtocol

namespace GDQ

/-!
# FAQ técnica

O módulo certifica distinções lógicas usadas no Capítulo 28. Ele não introduz
uma nova dinâmica física nem transforma respostas editoriais em teoremas da
ação oficial.
-/

/-- Um resultado condicional é uma implicação, não uma afirmação sem hipótese. -/
def ConditionalResult (hypothesis result : Prop) : Prop :=
  hypothesis → result

theorem conditionalResult_apply
    {hypothesis result : Prop}
    (h : ConditionalResult hypothesis result)
    (hhypothesis : hypothesis) :
    result :=
  h hhypothesis

/--
Mesmo que exista concordância numérica, a falta de background admissível
continua impedindo a cadeia forte.
-/
theorem numericalAgreement_does_not_close_missing_background
    (agreement : Prop)
    {chain : ClosureChain}
    (hmissing : ¬chain.admissibleBackground) :
    agreement → ¬StrongPredictionReady chain := by
  intro _
  exact not_strongPredictionReady_of_missing_background hmissing

/-- Estado conjunto fatorável em relação a um mapa de composição declarado. -/
def StateFactorizes
    {α β γ : Type*}
    (compose : α → β → γ)
    (joint : γ)
    (localA : α)
    (localB : β) : Prop :=
  joint = compose localA localB

/-- Emaranhamento, nesta camada, é não fatoração do estado preparado. -/
def EntangledState
    {α β γ : Type*}
    (compose : α → β → γ)
    (joint : γ)
    (localA : α)
    (localB : β) : Prop :=
  ¬StateFactorizes compose joint localA localB

theorem entangledState_is_state_nonfactorization
    {α β γ : Type*}
    (compose : α → β → γ)
    (joint : γ)
    (localA : α)
    (localB : β) :
    EntangledState compose joint localA localB ↔
      joint ≠ compose localA localB :=
  Iff.rfl

/-- Born operacional e dinâmica do evento são requisitos diferentes. -/
structure MeasurementStatus where
  operationalProbabilities : Prop
  individualEventDynamics : Prop

def OperationalBornClosed (s : MeasurementStatus) : Prop :=
  s.operationalProbabilities

def FullMeasurementDynamics (s : MeasurementStatus) : Prop :=
  s.operationalProbabilities ∧ s.individualEventDynamics

theorem fullMeasurementDynamics_implies_operationalBorn
    {s : MeasurementStatus}
    (h : FullMeasurementDynamics s) :
    OperationalBornClosed s :=
  h.1

theorem not_fullMeasurementDynamics_of_missing_event_dynamics
    {s : MeasurementStatus}
    (h : ¬s.individualEventDynamics) :
    ¬FullMeasurementDynamics s := by
  intro hfull
  exact h hfull.2

/-- Hipóteses mínimas para a leitura setorial produto de Perelman. -/
structure ProductSectorConditions where
  flatFactorRicciZero : Prop
  dilatonConstantAlongFlatFactor : Prop
  noMixedTorsion : Prop
  productMetric : Prop

def ProductSectorReductionAdmissible
    (c : ProductSectorConditions) : Prop :=
  c.flatFactorRicciZero
    ∧ c.dilatonConstantAlongFlatFactor
    ∧ c.noMixedTorsion
    ∧ c.productMetric

theorem not_productSectorReduction_of_mixed_torsion
    {c : ProductSectorConditions}
    (h : ¬c.noMixedTorsion) :
    ¬ProductSectorReductionAdmissible c := by
  intro hc
  exact h hc.2.2.1

theorem not_productSectorReduction_of_nonproduct_metric
    {c : ProductSectorConditions}
    (h : ¬c.productMetric) :
    ¬ProductSectorReductionAdmissible c := by
  intro hc
  exact h hc.2.2.2

/-- Dados de aparelho e alvo de comparação têm papéis distintos. -/
theorem apparatusData_not_comparisonTarget :
    ExperimentalDataRole.boundaryOrApparatus
      ≠ ExperimentalDataRole.comparisonTarget :=
  boundaryData_ne_comparisonTarget

end GDQ
