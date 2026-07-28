import Mathlib.Analysis.Complex.Exponential
import GDQ.PhaseReconstruction

namespace GDQ

/-!
# Quantização relativa de fase por carga e termo de extremidade

Este módulo formaliza a camada algébrica final do teorema condicional:

`identificação global + carga conservada + ação exponenciada`

implica

`Q * ΔS = 2πℏ n`.

Ele também registra o no-go local indispensável: deslocar o levantamento por
uma constante durante toda a história tem mudança de ação nula para qualquer
incremento real. Portanto a simetria contínua da densidade bulk não seleciona
sozinha um reticulado inteiro.

A existência das folhas físicas, o teorema de Stokes no background concreto,
a reconstrução lorentziana real e a seleção do setor primitivo permanecem
hipóteses geométricas explícitas, e não axiomas escondidos neste arquivo.
-/

/-- Fase associada a uma mudança real da ação física. -/
noncomputable def boundaryExponentiatedActionShift
    (ℏ ΔI : ℝ) : ℂ :=
  Complex.exp ((((ΔI / ℏ : ℝ) : ℂ)) * Complex.I)

/-- Resíduo escalar do balanço entre duas folhas e o bordo lateral. -/
def boundaryChargeBalanceResidual
    (Q₁ Q₂ lateralFlux : ℝ) : ℝ :=
  Q₂ - Q₁ + lateralFlux

/--
Se Stokes fornece balanço nulo e não há fuga lateral, a carga coincide nas
duas folhas.
-/
theorem boundaryCharge_conserved_of_zero_lateral_flux
    (Q₁ Q₂ lateralFlux : ℝ)
    (hbalance :
      boundaryChargeBalanceResidual Q₁ Q₂ lateralFlux = 0)
    (hflux : lateralFlux = 0) :
    Q₂ = Q₁ := by
  simp [boundaryChargeBalanceResidual, hflux] at hbalance
  linarith

/--
Se o fluxo que sai do objeto entra no aparelho, conserva-se a carga do
sistema composto.
-/
theorem boundaryCompositeCharge_conserved
    (Qobj₁ Qobj₂ Qapp₁ Qapp₂ : ℝ)
    (htransfer : Qobj₂ - Qobj₁ = -(Qapp₂ - Qapp₁)) :
    Qobj₂ + Qapp₂ = Qobj₁ + Qapp₁ := by
  linarith

/--
Termo de extremidade produzido por uma interpolação
`S ↦ S + a(t) ΔS` com carga conservada `Q`.
-/
def interpolatingLiftBoundaryShift
    (Q ΔS a₁ a₂ : ℝ) : ℝ :=
  Q * ΔS * (a₂ - a₁)

/--
Um deslocamento constante da história inteira possui mudança de ação nula.
-/
theorem constantLift_has_zero_boundaryShift
    (Q ΔS a : ℝ) :
    interpolatingLiftBoundaryShift Q ΔS a a = 0 := by
  simp [interpolatingLiftBoundaryShift]

/--
A invariância exponenciada do deslocamento constante vale para todo
incremento real. Logo ela não seleciona inteiros.
-/
theorem constantLift_exponential_invariant
    (ℏ Q ΔS a : ℝ) :
    boundaryExponentiatedActionShift ℏ
      (interpolatingLiftBoundaryShift Q ΔS a a) = 1 := by
  simp [boundaryExponentiatedActionShift,
    interpolatingLiftBoundaryShift]

/--
Uma interpolação de `a=0` para `a=1` produz o produto `Q ΔS`.

Isso avalia o termo de extremidade; não afirma que os pontos intermediários
sejam representantes do mesmo estado físico.
-/
theorem endpointInterpolation_gives_chargePhaseProduct
    (Q ΔS : ℝ) :
    interpolatingLiftBoundaryShift Q ΔS 0 1 = Q * ΔS := by
  simp [interpolatingLiftBoundaryShift]

/--
Núcleo algébrico da ação exponenciada: uma mudança fisicamente invisível é
múltiplo inteiro de `2πℏ`.
-/
theorem boundaryExponentiatedActionShift_eq_one_iff
    (ℏ ΔI : ℝ) (hℏ : ℏ ≠ 0) :
    boundaryExponentiatedActionShift ℏ ΔI = 1 ↔
      ∃ n : ℤ, ΔI = n * (2 * Real.pi * ℏ) := by
  rw [boundaryExponentiatedActionShift,
    GDQ.real_phase_eq_one_iff_integer_multiple]
  constructor
  · rintro ⟨n, hn⟩
    refine ⟨n, ?_⟩
    have h := congrArg (fun x : ℝ ↦ x * ℏ) hn
    field_simp [hℏ] at h ⊢
    nlinarith
  · rintro ⟨n, hn⟩
    refine ⟨n, ?_⟩
    rw [hn]
    field_simp [hℏ]

/--
Dados explícitos do teorema condicional de bordo.

* `physicalShift_is_boundaryTerm` deve vir da redução variacional;
* `exponentiatedInvariant` expressa a identificação física dos extremos no
  setor lorentziano reconstruído.
-/
structure BoundaryPhaseQuantizationData where
  ℏ : ℝ
  charge : ℝ
  phaseIncrement : ℝ
  physicalShift : ℝ
  planck_ne_zero : ℏ ≠ 0
  physicalShift_is_boundaryTerm :
    physicalShift = charge * phaseIncrement
  exponentiatedInvariant :
    boundaryExponentiatedActionShift ℏ physicalShift = 1

/--
Teorema de quantização relativa: o produto carga-incremento é múltiplo
inteiro de `2πℏ`.
-/
theorem BoundaryPhaseQuantizationData.product_quantized
    (D : BoundaryPhaseQuantizationData) :
    ∃ n : ℤ,
      D.charge * D.phaseIncrement =
        n * (2 * Real.pi * D.ℏ) := by
  have hshift :
      ∃ n : ℤ,
        D.physicalShift = n * (2 * Real.pi * D.ℏ) :=
    (boundaryExponentiatedActionShift_eq_one_iff
      D.ℏ D.physicalShift D.planck_ne_zero).mp
        D.exponentiatedInvariant
  obtain ⟨n, hn⟩ := hshift
  exact ⟨n, by simpa [D.physicalShift_is_boundaryTerm] using hn⟩

/--
No setor cuja carga primitiva foi selecionada independentemente como um, o
incremento é múltiplo inteiro de `2πℏ`.
-/
theorem BoundaryPhaseQuantizationData.primitive_increment_quantized
    (D : BoundaryPhaseQuantizationData)
    (hprimitive : D.charge = 1) :
    ∃ n : ℤ,
      D.phaseIncrement = n * (2 * Real.pi * D.ℏ) := by
  obtain ⟨n, hn⟩ := D.product_quantized
  exact ⟨n, by simpa [hprimitive] using hn⟩

/-! ## Classificação conservadora dos backgrounds -/

inductive QuantizationBackgroundClass where
  | topologicalCircular
  | relativeBoundary
  | trivial
  | spinorialHopf
  | openFlux
  | obstructed
  deriving DecidableEq, Repr

inductive QuantizationConclusion where
  | phaseIntegral
  | chargePhaseProductIntegral
  | zeroIncrement
  | halfMonodromy
  | noGlobalCharge
  | routeNotApplicable
  deriving DecidableEq, Repr

/-- Conclusão máxima autorizada em cada classe. -/
def quantizationConclusionFor :
    QuantizationBackgroundClass → QuantizationConclusion
  | .topologicalCircular => .phaseIntegral
  | .relativeBoundary => .chargePhaseProductIntegral
  | .trivial => .zeroIncrement
  | .spinorialHopf => .halfMonodromy
  | .openFlux => .noGlobalCharge
  | .obstructed => .routeNotApplicable

theorem relativeBoundary_quantizes_only_product :
    quantizationConclusionFor .relativeBoundary =
      .chargePhaseProductIntegral := rfl

theorem openFlux_has_no_isolated_globalCharge :
    quantizationConclusionFor .openFlux = .noGlobalCharge := rfl

theorem spinorialHopf_is_separate_class :
    quantizationConclusionFor .spinorialHopf = .halfMonodromy := rfl

end GDQ
