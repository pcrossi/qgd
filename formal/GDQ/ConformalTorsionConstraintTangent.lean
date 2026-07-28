import GDQ.ConformalTorsionProjectedHessian
import Mathlib.Tactic

namespace GDQ

/-!
# Tangente do vínculo de normalização no background torsional

O parâmetro `fBase` da ação reduzida não é uma flutuação material livre. Ele
é determinado pelos dados globais de normalização. Este módulo prova:

* variar `fBase` independentemente produz derivada unitária, não uma sela;
* o valor normalizado `f₀(a)=fBase+64 τ a²` tem tangente
  `δf₀=128 τ a δa`;
* portanto, dentro da família conformal normalizada, a direção física é
  unidimensional e já está parametrizada por `a`.

Nenhum bloco 8D misto é declarado ou inferido.
-/

/-- Constante do potencial gaussiano depois de impor a normalização. -/
noncomputable def torsionNormalizedF0
    (fBase τ a : ℝ) : ℝ :=
  fBase + 64 * (τ * a ^ 2)

/-- A dependência da ação reduzida em `fBase` é exatamente afim. -/
theorem normalizedTorsionReducedAction_fBase_shift
    (q fBase u s : ℝ) :
    normalizedTorsionReducedAction q (fBase + s) u =
      normalizedTorsionReducedAction q fBase u + s := by
  unfold normalizedTorsionReducedAction
  ring

/-- Se `fBase` fosse variado livremente, sua derivada seria exatamente um. -/
theorem normalizedTorsionReducedAction_fBase_hasDerivAt
    (q fBase u : ℝ) :
    HasDerivAt
      (fun b : ℝ ↦ normalizedTorsionReducedAction q b u)
      1 fBase := by
  have h :=
    (hasDerivAt_const fBase
      (q * Real.exp (-28 * u) * (2 - 24 * u) - 2 + 128 * u)).add
      (hasDerivAt_id fBase)
  apply (h.congr_of_eventuallyEq ?_).congr_deriv
  · simp
  · exact Filter.Eventually.of_forall (fun b ↦ by
      unfold normalizedTorsionReducedAction
      simp only [Pi.add_apply, id_eq]
      ring)

/--
Logo não existe ponto crítico da ação reduzida no espaço artificial em que
`fBase` seja promovido a variável dinâmica independente.
-/
theorem normalizedTorsionReducedAction_not_stationary_in_fBase
    (q fBase u : ℝ) :
    deriv
      (fun b : ℝ ↦ normalizedTorsionReducedAction q b u)
      fBase ≠ 0 := by
  rw [(normalizedTorsionReducedAction_fBase_hasDerivAt
    q fBase u).deriv]
  norm_num

/-- A derivada em `u` não depende de `fBase`; o bloco misto artificial é nulo. -/
theorem normalizedTorsionReducedAction_uDerivative_independent_fBase
    (q fBase u : ℝ) :
    deriv (normalizedTorsionReducedAction q fBase) u =
      normalizedTorsionSlope q u :=
  (normalizedTorsionReducedAction_hasDerivAt q fBase u).deriv

/-- A segunda derivada na direção artificial `fBase` é nula. -/
theorem normalizedTorsionReducedAction_fBase_secondDerivative_zero
    (q fBase u : ℝ) :
    deriv
      (fun b : ℝ ↦
        deriv
          (fun c : ℝ ↦ normalizedTorsionReducedAction q c u)
          b)
      fBase = 0 := by
  have hfun :
      (fun b : ℝ ↦
        deriv
          (fun c : ℝ ↦ normalizedTorsionReducedAction q c u)
          b) =
        fun _ : ℝ ↦ 1 := by
    funext b
    exact
      (normalizedTorsionReducedAction_fBase_hasDerivAt q b u).deriv
  rw [hfun]
  simp

/-- A derivada mista `∂fBase ∂u` também é nula. -/
theorem normalizedTorsionReducedAction_mixed_fBase_u_zero
    (q fBase u : ℝ) :
    deriv
      (fun b : ℝ ↦
        deriv (normalizedTorsionReducedAction q b) u)
      fBase = 0 := by
  have hfun :
      (fun b : ℝ ↦
        deriv (normalizedTorsionReducedAction q b) u) =
        fun _ : ℝ ↦ normalizedTorsionSlope q u := by
    funext b
    exact normalizedTorsionReducedAction_uDerivative_independent_fBase
      q b u
  rw [hfun]
  simp

/-- A derivada de `f₀(a)` é a linearização exata do vínculo. -/
theorem torsionNormalizedF0_hasDerivAt
    (fBase τ a : ℝ) :
    HasDerivAt (torsionNormalizedF0 fBase τ)
      (128 * τ * a) a := by
  unfold torsionNormalizedF0
  have h :=
    (hasDerivAt_const a fBase).add
      (((hasDerivAt_pow 2 a).const_mul τ).const_mul 64)
  apply (h.congr_of_eventuallyEq ?_).congr_deriv
  · simp only [zero_add]
    norm_num
    ring
  · exact Filter.Eventually.of_forall (fun x ↦ by
      simp only [Pi.add_apply])

/-- Relação linearizada que define os vetores tangentes normalizados. -/
def IsNormalizedTorsionTangent
    (τ a δa δf₀ : ℝ) : Prop :=
  δf₀ = 128 * τ * a * δa

/-- A componente dilatônica de qualquer tangente normalizado é única. -/
theorem normalizedTorsionTangent_f0_unique
    {τ a δa δf₀ δf₀' : ℝ}
    (h : IsNormalizedTorsionTangent τ a δa δf₀)
    (h' : IsNormalizedTorsionTangent τ a δa δf₀') :
    δf₀ = δf₀' := by
  exact h.trans h'.symm

/-- Todo valor de `δa` determina um único tangente normalizado. -/
theorem existsUnique_normalizedTorsionTangent_f0
    (τ a δa : ℝ) :
    ∃! δf₀ : ℝ, IsNormalizedTorsionTangent τ a δa δf₀ := by
  refine ⟨128 * τ * a * δa, rfl, ?_⟩
  intro y hy
  exact hy

/--
Consequência lógica: no ansatz conformal normalizado não existe um segundo
coeficiente físico independente `K_aX` ou `K_XX`. Eles só podem surgir ao
ampliar a família para modos 8D genuinamente independentes.
-/
theorem conformalNormalizedTangent_has_one_free_coordinate
    (τ a δa : ℝ) :
    IsNormalizedTorsionTangent τ a δa
      (128 * τ * a * δa) :=
  rfl

end GDQ
