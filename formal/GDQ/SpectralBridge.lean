import GDQ.GlobalLocalTransport
import GDQ.VariationalHessian

namespace GDQ

/-!
# Herança espectral global--local

Este módulo formaliza os Lemas 3--6 no nível lógico adequado.

* A convergência de Mosco é definida por `liminf` fraco e sequência forte de
  recuperação.
* Localização, gap, resolventes e projetores possuem certificados separados.
* A conclusão composta não transforma esses certificados em axiomas globais:
  eles devem ser construídos para cada background.
-/

variable
  {E : Type*}
  [NormedAddCommGroup E]
  [InnerProductSpace ℝ E]

/-- Convergência fraca expressa por todos os funcionais do produto interno. -/
def WeaklyTendsto (u : Nat → E) (u₀ : E) : Prop :=
  ∀ v : E,
    Filter.Tendsto (fun k => inner ℝ (u k) v)
      Filter.atTop (nhds (inner ℝ u₀ v))

/-- Forma quadrática real finita no espaço físico identificado. -/
abbrev RealQuadraticForm (E : Type*) := E → ℝ

/--
Certificado de convergência de Mosco das formas físicas.

No problema geométrico, `familyForm k` já inclui o transporte unitário da
medida e o projetor físico.
-/
structure MoscoConvergenceData (E : Type*)
    [NormedAddCommGroup E] [InnerProductSpace ℝ E] where
  familyForm : Nat → RealQuadraticForm E
  localForm : RealQuadraticForm E
  liminf :
    ∀ (u : Nat → E) (u₀ : E),
      WeaklyTendsto u u₀ →
      localForm u₀ ≤ Filter.liminf (fun k => familyForm k (u k)) Filter.atTop
  recovery :
    ∀ u₀ : E,
      ∃ u : Nat → E,
        Filter.Tendsto u Filter.atTop (nhds u₀) ∧
        Filter.Tendsto (fun k => familyForm k (u k))
          Filter.atTop (nhds (localForm u₀))

/-- Dados de um cluster físico local separado do restante do espectro. -/
structure LocalSpectralGap where
  gap : ℝ
  gap_pos : 0 < gap

/--
Certificado do Lema 4. `familyGap` é o gap depois do transporte; a estimativa
de Agmon é registrada separadamente para não confundir positividade espectral
com localização.
-/
structure UniformLocalizationGap (E : Type*)
    [NormedAddCommGroup E] where
  localGap : LocalSpectralGap
  delta : ℝ
  delta_nonneg : 0 ≤ delta
  three_delta_lt_gap : 3 * delta < localGap.gap
  familyGap : Nat → ℝ
  familyGap_lower :
    ∀ᶠ k in Filter.atTop,
      localGap.gap - 2 * delta ≤ familyGap k
  agmonWeight : E → ℝ
  agmonBound : ℝ
  agmonBound_nonneg : 0 ≤ agmonBound
  localizedModes : Nat → Set E
  agmon_estimate :
    ∀ k u, u ∈ localizedModes k →
      agmonWeight u ≤ agmonBound

/-- A margem `Δ₀ - 2δ` do Lema 4 é estritamente positiva. -/
theorem UniformLocalizationGap.transferred_margin_pos
    {F : Type*} [NormedAddCommGroup F]
    (G : UniformLocalizationGap F) :
    0 < G.localGap.gap - 2 * G.delta := by
  linarith [G.localGap.gap_pos, G.three_delta_lt_gap]

/-- Eventualmente, todo gap transportado é positivo. -/
theorem UniformLocalizationGap.eventually_family_gap_pos
    {F : Type*} [NormedAddCommGroup F]
    (G : UniformLocalizationGap F) :
    ∀ᶠ k in Filter.atTop, 0 < G.familyGap k := by
  filter_upwards [G.familyGap_lower] with k hk
  exact lt_of_lt_of_le G.transferred_margin_pos hk

/--
Certificado da convergência forte dos resolventes no espaço já identificado.

O parâmetro `z` deve permanecer fora do espectro; essa condição pertence à
construção concreta do certificado.
-/
structure StrongResolventConvergence (E : Type*)
    [NormedAddCommGroup E] where
  familyResolvent : Nat → ℂ → E → E
  localResolvent : ℂ → E → E
  admissibleParameter : ℂ → Prop
  converges :
    ∀ z, admissibleParameter z →
      ∀ u,
        Filter.Tendsto (fun k => familyResolvent k z u)
          Filter.atTop (nhds (localResolvent z u))

/--
Certificado da convergência em norma dos projetores de Riesz de um cluster
finito localizado.
-/
structure RieszProjectorConvergence (E : Type*)
    [NormedAddCommGroup E] [InnerProductSpace ℝ E] where
  familyProjector : Nat → E →L[ℝ] E
  localProjector : E →L[ℝ] E
  family_idempotent :
    ∀ k u, familyProjector k (familyProjector k u) = familyProjector k u
  local_idempotent :
    ∀ u, localProjector (localProjector u) = localProjector u
  operatorNormConverges :
    Filter.Tendsto
      (fun k => ‖familyProjector k - localProjector‖)
      Filter.atTop (nhds 0)

/--
Pacote completo dos seis lemas para um background local admissível.

Não há uma interface global--local: `measureTransport` identifica os espaços
em cartas apontadas; DtN pertence apenas ao bordo físico do estômato.
-/
structure SixLemmaBridgeData
    (X E : Type*)
    [NormedAddCommGroup E] [InnerProductSpace ℝ E] where
  geometry : PointedConvergenceCertificate
  fields : PointedFieldTransport X
  measureTransport : WeightedMeasureTransport E E
  mosco : MoscoConvergenceData E
  localizationGap : UniformLocalizationGap E
  resolvents : StrongResolventConvergence E
  riesz : RieszProjectorConvergence E
  localBackgroundAdmissible : Prop
  localBackgroundAdmissible_proof : localBackgroundAdmissible
  hessianIsOfficialProjectedSecondVariation : Prop
  hessianIsOfficialProjectedSecondVariation_proof :
    hessianIsOfficialProjectedSecondVariation

/-- Conclusão lógica transportada pelos seis lemas. -/
def SixLemmaBridgeConclusion
    {X : Type*} (B : SixLemmaBridgeData X E) : Prop :=
  B.localBackgroundAdmissible ∧
  B.hessianIsOfficialProjectedSecondVariation ∧
  (∀ᶠ k in Filter.atTop, 0 < B.localizationGap.familyGap k) ∧
  (∀ z, B.resolvents.admissibleParameter z →
    ∀ u,
      Filter.Tendsto (fun k => B.resolvents.familyResolvent k z u)
        Filter.atTop (nhds (B.resolvents.localResolvent z u))) ∧
  Filter.Tendsto
    (fun k => ‖B.riesz.familyProjector k - B.riesz.localProjector‖)
    Filter.atTop (nhds 0)

/--
Composição formal dos seis lemas: todas as conclusões mantêm visíveis as
obrigações analíticas usadas.
-/
theorem six_lemma_bridge
    {X : Type*} (B : SixLemmaBridgeData X E) :
    SixLemmaBridgeConclusion B := by
  exact ⟨B.localBackgroundAdmissible_proof,
    B.hessianIsOfficialProjectedSecondVariation_proof,
    B.localizationGap.eventually_family_gap_pos,
    B.resolvents.converges,
    B.riesz.operatorNormConverges⟩

/-- Classes de quantidades que aparecem na ponte. -/
inductive BridgeQuantity
  | index
  | relativeCharge
  | chernClass
  | boundMultiplicity
  | boundDimensionlessRatio
  | absoluteMass
  | couplingNormalization
  | detectorResponse
  | decayRate
  deriving DecidableEq, Repr

/--
Classificação formal do Lema 6. `true` significa herança pela ponte; não
significa que a quantidade exista em todo background.
-/
def BridgeQuantity.isInherited : BridgeQuantity → Bool
  | .index => true
  | .relativeCharge => true
  | .chernClass => true
  | .boundMultiplicity => true
  | .boundDimensionlessRatio => true
  | .absoluteMass => false
  | .couplingNormalization => false
  | .detectorResponse => false
  | .decayRate => false

theorem topological_quantities_are_inherited :
    BridgeQuantity.index.isInherited = true ∧
    BridgeQuantity.relativeCharge.isInherited = true ∧
    BridgeQuantity.chernClass.isInherited = true := by
  decide

theorem continuous_normalizations_are_not_automatic :
    BridgeQuantity.absoluteMass.isInherited = false ∧
    BridgeQuantity.couplingNormalization.isInherited = false ∧
    BridgeQuantity.detectorResponse.isInherited = false ∧
    BridgeQuantity.decayRate.isInherited = false := by
  decide

end GDQ
