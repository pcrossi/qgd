import GDQ.OSReconstruction
import Mathlib.Analysis.Complex.Trigonometric

namespace GDQ

/-!
# Semigrupo euclidiano e evolução unitária reconstruída

O teorema OS funcional completo associa a um semigrupo euclidiano positivo um
gerador autoadjunto não negativo. Este módulo não oculta essa etapa analítica.
Ele:

1. tipa os dados que o setor reconstruído deve fornecer;
2. prova as propriedades modo a modo dos pesos espectrais
   `exp (-a E / ℏ)` e `exp (-i t E / ℏ)`;
3. separa contração euclidiana de preservação da norma em tempo físico.

A existência do gerador autoadjunto de um background concreto continua sendo
uma obrigação espectral do setor.
-/

variable
  {H : Type*}
  [NormedAddCommGroup H]
  [InnerProductSpace ℂ H]

/-- Dados de um semigrupo euclidiano contrativo no Hilbert reconstruído. -/
structure PositiveEuclideanSemigroup (H : Type*)
    [NormedAddCommGroup H]
    [InnerProductSpace ℂ H] where
  T : NNReal → H →L[ℂ] H
  map_zero : T 0 = ContinuousLinearMap.id ℂ H
  map_add : ∀ a b, T (a + b) = (T a).comp (T b)
  contractive : ∀ a ψ, ‖T a ψ‖ ≤ ‖ψ‖

/-- O semigrupo euclidiano não aumenta a norma. -/
theorem PositiveEuclideanSemigroup.norm_le
    (S : PositiveEuclideanSemigroup H) (a : NNReal) (ψ : H) :
    ‖S.T a ψ‖ ≤ ‖ψ‖ :=
  S.contractive a ψ

/--
Dados de um grupo unitário no tempo físico. Usamos equivalências lineares
isométricas para que inversibilidade e preservação da norma sejam estruturais.
-/
structure ReconstructedUnitaryGroup (H : Type*)
    [NormedAddCommGroup H]
    [InnerProductSpace ℂ H] where
  U : ℝ → H ≃ₗᵢ[ℂ] H
  map_zero : U 0 = LinearIsometryEquiv.refl ℂ H
  map_add : ∀ t s, U (t + s) = (U t).trans (U s)

/-- A evolução física reconstruída preserva exatamente a norma. -/
theorem ReconstructedUnitaryGroup.norm_eq
    (U : ReconstructedUnitaryGroup H) (t : ℝ) (ψ : H) :
    ‖U.U t ψ‖ = ‖ψ‖ :=
  (U.U t).norm_map ψ

/-- Peso de um modo de energia `E` no parâmetro euclidiano positivo. -/
noncomputable def euclideanSpectralWeight
    (ℏ E a : ℝ) : ℝ :=
  Real.exp (-(a * E / ℏ))

/-- O peso espectral euclidiano é estritamente positivo. -/
theorem euclideanSpectralWeight_pos
    (ℏ E a : ℝ) :
    0 < euclideanSpectralWeight ℏ E a := by
  exact Real.exp_pos _

/--
Para `ℏ>0`, `E≥0` e `a≥0`, o peso euclidiano é contrativo.
-/
theorem euclideanSpectralWeight_le_one
    {ℏ E a : ℝ}
    (hℏ : 0 < ℏ) (hE : 0 ≤ E) (ha : 0 ≤ a) :
    euclideanSpectralWeight ℏ E a ≤ 1 := by
  rw [euclideanSpectralWeight, ← Real.exp_zero]
  apply Real.exp_le_exp.mpr
  have hprod : 0 ≤ a * E := mul_nonneg ha hE
  exact neg_nonpos.mpr (div_nonneg hprod hℏ.le)

/-- Os pesos euclidianos satisfazem a lei de semigrupo. -/
theorem euclideanSpectralWeight_add
    {ℏ E a b : ℝ} :
    euclideanSpectralWeight ℏ E (a + b) =
      euclideanSpectralWeight ℏ E a *
        euclideanSpectralWeight ℏ E b := by
  rw [euclideanSpectralWeight, euclideanSpectralWeight,
    euclideanSpectralWeight, ← Real.exp_add]
  congr 1
  ring

/-- Peso do mesmo modo depois da continuação ao tempo físico. -/
noncomputable def lorentzianSpectralWeight
    (ℏ E t : ℝ) : ℂ :=
  Complex.exp (((-(t * E / ℏ) : ℝ) : ℂ) * Complex.I)

/-- Todo peso lorentziano espectral possui módulo unitário. -/
theorem lorentzianSpectralWeight_norm
    (ℏ E t : ℝ) :
    ‖lorentzianSpectralWeight ℏ E t‖ = 1 := by
  exact Complex.norm_exp_ofReal_mul_I _

/-- Os pesos lorentzianos satisfazem a lei de grupo aditivo. -/
theorem lorentzianSpectralWeight_add
    {ℏ E t s : ℝ} :
    lorentzianSpectralWeight ℏ E (t + s) =
      lorentzianSpectralWeight ℏ E t *
        lorentzianSpectralWeight ℏ E s := by
  rw [lorentzianSpectralWeight, lorentzianSpectralWeight,
    lorentzianSpectralWeight, ← Complex.exp_add]
  congr 1
  push_cast
  ring

/--
Um modo euclidiano pode contrair, enquanto o modo físico correspondente
preserva a norma. As duas afirmações coexistem sem perda de probabilidade.
-/
theorem euclidean_contraction_and_lorentzian_unitarity
    {ℏ E a t : ℝ}
    (hℏ : 0 < ℏ) (hE : 0 ≤ E) (ha : 0 ≤ a) :
    euclideanSpectralWeight ℏ E a ≤ 1 ∧
      ‖lorentzianSpectralWeight ℏ E t‖ = 1 :=
  ⟨euclideanSpectralWeight_le_one hℏ hE ha,
    lorentzianSpectralWeight_norm ℏ E t⟩

end GDQ
