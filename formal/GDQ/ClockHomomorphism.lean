import GDQ.CausalContour
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Topology.Instances.RealVectorSpace

namespace GDQ

/-!
# Homomorfismo causal do relógio

O resultado deste arquivo é condicional à hipótese de compatibilidade entre:

* o grupo aditivo das translações do parâmetro local `t`;
* o grupo multiplicativo das dilatações positivas do parâmetro de fluxo.

Ele não identifica todo contorno causal complexo com esta família.
-/

/-- Escala positiva exponencial associada ao relógio local. -/
noncomputable def exponentialFlowScale
    (τ₀ κ t : ℝ) : ℝ :=
  τ₀ * Real.exp (κ * t)

/-- Uma escala inicial positiva permanece positiva. -/
theorem exponentialFlowScale_pos
    {τ₀ : ℝ} (hτ₀ : 0 < τ₀) (κ t : ℝ) :
    0 < exponentialFlowScale τ₀ κ t := by
  exact mul_pos hτ₀ (Real.exp_pos (κ * t))

/-- Lei de composição relativa que realiza o homomorfismo aditivo--multiplicativo. -/
theorem exponentialFlowScale_add
    {τ₀ : ℝ} (hτ₀ : τ₀ ≠ 0) (κ t₁ t₂ : ℝ) :
    exponentialFlowScale τ₀ κ (t₁ + t₂) / τ₀ =
      (exponentialFlowScale τ₀ κ t₁ / τ₀) *
        (exponentialFlowScale τ₀ κ t₂ / τ₀) := by
  simp [exponentialFlowScale, hτ₀, mul_add, Real.exp_add]

/--
Fator relativo de um relógio homogêneo.

`factor t` representa `τγ(t)/τ₀`. As hipóteses registram exatamente
normalização, positividade, composição temporal e regularidade.
-/
structure PositiveClockHomomorphism where
  factor : ℝ → ℝ
  map_zero : factor 0 = 1
  map_add_mul : ∀ t₁ t₂, factor (t₁ + t₂) = factor t₁ * factor t₂
  positive : ∀ t, 0 < factor t
  continuous : Continuous factor

/-- O logaritmo de um relógio positivo transforma composição em adição. -/
noncomputable def PositiveClockHomomorphism.logAddHom
    (h : PositiveClockHomomorphism) : ℝ →+ ℝ where
  toFun := fun t ↦ Real.log (h.factor t)
  map_zero' := by
    rw [h.map_zero, Real.log_one]
  map_add' := by
    intro t₁ t₂
    rw [h.map_add_mul]
    exact Real.log_mul
      (ne_of_gt (h.positive t₁))
      (ne_of_gt (h.positive t₂))

/-- O logaritmo do fator relativo é contínuo. -/
theorem PositiveClockHomomorphism.continuous_log
    (h : PositiveClockHomomorphism) :
    Continuous (fun t ↦ Real.log (h.factor t)) := by
  rw [continuous_iff_continuousAt]
  intro t
  exact
    (Real.continuousAt_log (ne_of_gt (h.positive t))).comp
      h.continuous.continuousAt

/-- A forma exponencial é determinada pelo valor do relógio em uma unidade. -/
theorem PositiveClockHomomorphism.eq_exp_log_one
    (h : PositiveClockHomomorphism) (t : ℝ) :
    h.factor t = Real.exp (Real.log (h.factor 1) * t) := by
  have hlinear :
      h.logAddHom t = t * h.logAddHom 1 := by
    have hsmul :=
      map_real_smul h.logAddHom h.continuous_log t (1 : ℝ)
    simpa using hsmul
  have hlog :
      Real.log (h.factor t) = Real.log (h.factor 1) * t := by
    simpa [PositiveClockHomomorphism.logAddHom, mul_comm] using hlinear
  rw [← hlog, Real.exp_log (h.positive t)]

/--
Existência: todo relógio positivo, contínuo e compatível com a composição
tem fator relativo exponencial.

Interpretação física:

* este resultado não afirma que toda curva do tipo geral `CausalContour` seja
  exponencial;
* afirma que todo contorno que represente um relógio físico homogêneo,
  positivo, contínuo, normalizado e compatível com a composição temporal é
  necessariamente exponencial;
* nessa classe física, a forma exponencial não é um ansatz nem uma escolha de
  coordenadas: ela é a única solução possível;
* curvas complexas mais gerais continuam matematicamente admissíveis, mas não
  representam esse relógio homogêneo sem uma demonstração adicional.
-/
theorem PositiveClockHomomorphism.eq_exp
    (h : PositiveClockHomomorphism) :
    ∃ κ : ℝ, ∀ t : ℝ, h.factor t = Real.exp (κ * t) := by
  exact
    ⟨Real.log (h.factor 1), h.eq_exp_log_one⟩

/-- O gerador exponencial de um relógio homogêneo é único. -/
theorem PositiveClockHomomorphism.generator_unique
    (h : PositiveClockHomomorphism)
    {κ₁ κ₂ : ℝ}
    (h₁ : ∀ t : ℝ, h.factor t = Real.exp (κ₁ * t))
    (h₂ : ∀ t : ℝ, h.factor t = Real.exp (κ₂ * t)) :
    κ₁ = κ₂ := by
  have he : Real.exp κ₁ = Real.exp κ₂ := by
    simpa using (h₁ 1).symm.trans (h₂ 1)
  exact Real.exp_injective he

/-- Contorno causal exponencial contido no eixo real positivo. -/
noncomputable def exponentialCausalContour
    (τ₀ κ : ℝ) (hτ₀ : 0 < τ₀) : CausalContour where
  z := fun t ↦ (exponentialFlowScale τ₀ κ t : ℂ)
  dz := fun t ↦
    (τ₀ * (Real.exp (κ * t) * κ) : ℂ)
  nonzero := by
    intro t
    exact_mod_cast
      ne_of_gt (exponentialFlowScale_pos hτ₀ κ t)
  hasDeriv := by
    intro t
    have hr :
        HasDerivAt
          (fun s : ℝ ↦ exponentialFlowScale τ₀ κ s)
          (τ₀ * (Real.exp (κ * t) * κ)) t := by
      have hlin : HasDerivAt (fun s : ℝ ↦ κ * s) κ t := by
        simpa using (hasDerivAt_id t).const_mul κ
      have hexp :
          HasDerivAt
            (fun s : ℝ ↦ Real.exp (κ * s))
            (Real.exp (κ * t) * κ) t :=
        (Real.hasDerivAt_exp (κ * t)).comp t hlin
      simpa [exponentialFlowScale] using hexp.const_mul τ₀
    have hc :=
      (Complex.ofRealCLM.hasFDerivAt.comp t hr.hasFDerivAt).hasDerivAt
    simpa [Function.comp_def] using hc

/-- O contorno exponencial fornece uma seção real positiva explícita. -/
theorem exponentialCausalContour_z
    (τ₀ κ : ℝ) (hτ₀ : 0 < τ₀) (t : ℝ) :
    (exponentialCausalContour τ₀ κ hτ₀).z t =
      (exponentialFlowScale τ₀ κ t : ℂ) := by
  rfl

/--
O coeficiente do pullback logarítmico é o gerador constante `κ`.

Esta é a forma formal de `γ*(dτ/τ) = κ dt`.
-/
theorem exponentialCausalContour_dlog
    (τ₀ κ : ℝ) (hτ₀ : 0 < τ₀) (t : ℝ) :
    (exponentialCausalContour τ₀ κ hτ₀).dlog t = (κ : ℂ) := by
  change
    (τ₀ * (Real.exp (κ * t) * κ) : ℂ) /
      (exponentialFlowScale τ₀ κ t : ℂ) = (κ : ℂ)
  have hs :
      exponentialFlowScale τ₀ κ t ≠ 0 :=
    ne_of_gt (exponentialFlowScale_pos hτ₀ κ t)
  rw [div_eq_iff]
  · norm_num [exponentialFlowScale]
    ring
  · exact_mod_cast hs

end GDQ
