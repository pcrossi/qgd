import Mathlib.Analysis.Fourier.PoissonSummation
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Topology.Homotopy.Lifting

namespace GDQ

open scoped FourierTransform
open unitInterval

/-!
# Quantização da fase circular e papel do pente de Dirac

Este arquivo separa duas afirmações que não devem ser confundidas.

1. A integralidade nasce do fechamento global da fase em `U(1)`.
2. A fórmula de Poisson é uma identidade harmônica posterior. Ela não cria
   os índices inteiros.

A igualdade informal

`∑ n : ℤ, exp (I * n * θ) = 2π ∑ k : ℤ, δ (θ - 2πk)`

é distribucional, não pontual. Em Lean usamos o teorema rigoroso de Poisson
para funções de Schwartz; não postulamos uma soma divergente como função.
-/

/-- Levantamento local de fase real para a fase física complexa. -/
noncomputable def circularPhase (α θ : ℝ) : ℂ :=
  Complex.exp (((α * θ : ℝ) : ℂ) * Complex.I)

/-- Valor físico circular associado a um levantamento real geral `χ`. -/
noncomputable def liftedCircularPhase (χ : ℝ → ℝ) (θ : ℝ) : ℂ :=
  Complex.exp ((χ θ : ℂ) * Complex.I)

/-- A fase no ponto inicial é a unidade de `U(1)`. -/
@[simp] theorem circularPhase_zero (α : ℝ) :
    circularPhase α 0 = 1 := by
  simp [circularPhase]

/--
Critério exato de fechamento de uma fase linear ao completar uma volta.

O lado direito não é assumido: ele é obtido da periodicidade do exponencial
complexo e mostra que o coeficiente local precisa ser um inteiro.
-/
theorem circularPhase_two_pi_eq_one_iff_integer (α : ℝ) :
    circularPhase α (2 * Real.pi) = 1 ↔
      ∃ n : ℤ, α = n := by
  rw [circularPhase, Complex.exp_eq_one_iff]
  constructor
  · rintro ⟨n, hn⟩
    refine ⟨n, ?_⟩
    have hn' : (α : ℂ) = (n : ℂ) := by
      apply mul_right_cancel₀ Complex.two_pi_I_ne_zero
      calc
        (α : ℂ) * (2 * Real.pi * Complex.I) =
            (((α * (2 * Real.pi) : ℝ) : ℂ) * Complex.I) := by
              push_cast
              ring
        _ = (n : ℂ) * (2 * Real.pi * Complex.I) := hn
    exact_mod_cast hn'
  · rintro ⟨n, rfl⟩
    refine ⟨n, ?_⟩
    push_cast
    ring

/-- Fechamento entre os extremos `0` e `2π` equivale a integralidade. -/
theorem circularPhase_closes_iff_integer (α : ℝ) :
    circularPhase α (2 * Real.pi) = circularPhase α 0 ↔
      ∃ n : ℤ, α = n := by
  simpa using circularPhase_two_pi_eq_one_iff_integer α

/--
Teorema global para um levantamento arbitrário ao longo de uma volta.

Se os valores físicos da fase nos extremos coincidem, o incremento do
levantamento real é necessariamente um múltiplo inteiro de `2π`.

A continuidade de `χ` é necessária na aplicação geométrica para que ele seja
um levantamento de caminho. A conclusão algébrica abaixo usa apenas o
fechamento dos extremos.
-/
theorem closed_lift_increment_is_integer
    (χ : ℝ → ℝ)
    (hclose :
      liftedCircularPhase χ (2 * Real.pi) =
        liftedCircularPhase χ 0) :
    ∃ n : ℤ,
      χ (2 * Real.pi) - χ 0 = 2 * Real.pi * n := by
  rw [liftedCircularPhase, liftedCircularPhase,
    Complex.exp_eq_exp_iff_exists_int] at hclose
  obtain ⟨n, hn⟩ := hclose
  refine ⟨n, ?_⟩
  have hc :
      (χ (2 * Real.pi) : ℂ) =
        (χ 0 : ℂ) + (n : ℂ) * (2 * Real.pi) := by
    apply mul_right_cancel₀ Complex.I_ne_zero
    calc
      (χ (2 * Real.pi) : ℂ) * Complex.I =
          (χ 0 : ℂ) * Complex.I +
            (n : ℂ) * (2 * Real.pi * Complex.I) := hn
      _ = ((χ 0 : ℂ) + (n : ℂ) * (2 * Real.pi)) * Complex.I := by
        ring
  have hr :
      χ (2 * Real.pi) =
        χ 0 + (n : ℝ) * (2 * Real.pi) := by
    exact_mod_cast hc
  rw [hr]
  ring

/-- Circulação definida pelo incremento de um levantamento geral. -/
noncomputable def liftedPhaseCirculation
    (ℏ : ℝ) (χ : ℝ → ℝ) : ℝ :=
  ℏ * (χ (2 * Real.pi) - χ 0)

/--
Todo levantamento fechado possui circulação quantizada, sem exigir que o
perfil local da fase seja linear.
-/
theorem liftedPhaseCirculation_quantized
    (ℏ : ℝ) (χ : ℝ → ℝ)
    (hclose :
      liftedCircularPhase χ (2 * Real.pi) =
        liftedCircularPhase χ 0) :
    ∃ n : ℤ,
      liftedPhaseCirculation ℏ χ = n * (2 * Real.pi * ℏ) := by
  obtain ⟨n, hn⟩ := closed_lift_increment_is_integer χ hclose
  refine ⟨n, ?_⟩
  simp [liftedPhaseCirculation, hn]
  ring

/--
Existência de levantamento e quantização para uma volta contínua arbitrária
no círculo.

Este teorema internaliza a propriedade de levantamento da cobertura
`Circle.exp : ℝ → Circle`. Portanto, diferentemente do lema anterior, o
levantamento real não é fornecido como hipótese: ele é construído a partir
do laço contínuo.
-/
theorem circleLoop_has_quantized_lift
    (γ : C(I, Circle))
    (hloop : γ 1 = γ 0) :
    ∃ Γ : C(I, ℝ),
      (∀ t : I, Circle.exp (Γ t) = γ t) ∧
        ∃ n : ℤ, Γ 1 - Γ 0 = 2 * Real.pi * n := by
  have hstart :
      γ 0 = Circle.exp (Complex.arg (γ 0)) := by
    exact (Circle.exp_arg (γ 0)).symm
  obtain ⟨Γ, hlift, -⟩ :=
    Circle.isCoveringMap_exp.exists_path_lifts
      γ (Complex.arg (γ 0)) hstart
  refine ⟨Γ, ?_, ?_⟩
  · intro t
    exact congrFun hlift t
  · have hend :
        Circle.exp (Γ 1) = Circle.exp (Γ 0) := by
      calc
        Circle.exp (Γ 1) = γ 1 := congrFun hlift 1
        _ = γ 0 := hloop
        _ = Circle.exp (Γ 0) := (congrFun hlift 0).symm
    have hmod :
        Γ 1 ≡ Γ 0 [PMOD (2 * Real.pi)] :=
      Circle.exp_inj.mp hend
    rw [AddCommGroup.modEq_iff_zsmul'] at hmod
    obtain ⟨m, hm⟩ := hmod
    refine ⟨-m, ?_⟩
    have hm' :
        Γ 0 - Γ 1 = (m : ℝ) * (2 * Real.pi) := by
      simpa using hm
    rw [← neg_sub (Γ 0) (Γ 1), hm']
    push_cast
    ring

/--
Uma fase real cujo exponencial é a unidade é um múltiplo inteiro de `2π`.
-/
theorem real_phase_eq_one_iff_integer_multiple (x : ℝ) :
    Complex.exp ((x : ℂ) * Complex.I) = 1 ↔
      ∃ n : ℤ, x = 2 * Real.pi * n := by
  rw [Complex.exp_eq_one_iff]
  constructor
  · rintro ⟨n, hn⟩
    refine ⟨n, ?_⟩
    have hc : (x : ℂ) = (n : ℂ) * (2 * Real.pi) := by
      apply mul_right_cancel₀ Complex.I_ne_zero
      calc
        (x : ℂ) * Complex.I =
            (n : ℂ) * (2 * Real.pi * Complex.I) := hn
        _ = ((n : ℂ) * (2 * Real.pi)) * Complex.I := by ring
    have hr : x = (n : ℝ) * (2 * Real.pi) := by
      exact_mod_cast hc
    rw [hr]
    ring
  · rintro ⟨n, rfl⟩
    refine ⟨n, ?_⟩
    push_cast
    ring

/-- Somar `2πk` a um levantamento real não altera sua fase `U(1)`. -/
theorem complex_exp_phase_add_two_pi_int
    (x : ℝ) (k : ℤ) :
    Complex.exp
        (((x + 2 * Real.pi * k : ℝ) : ℂ) * Complex.I) =
      Complex.exp ((x : ℂ) * Complex.I) := by
  rw [show
    (((x + 2 * Real.pi * k : ℝ) : ℂ) * Complex.I) =
      (x : ℂ) * Complex.I +
        (k : ℂ) * (2 * Real.pi * Complex.I) by
          push_cast
          ring]
  rw [Complex.exp_add]
  simp

/--
Integralidade do cociclo de transição em uma interseção tripla.

Se as três funções de transição `U(1)` multiplicam para a identidade, a soma
de quaisquer levantamentos reais locais é `2π n`. Esse inteiro é o dado de
Čech que antecede a construção da primeira classe de Chern.
-/
theorem u1_triple_overlap_integer
    (lamAB lamBC lamCA : ℝ)
    (hcocycle :
      Complex.exp ((lamAB : ℂ) * Complex.I) *
          Complex.exp ((lamBC : ℂ) * Complex.I) *
          Complex.exp ((lamCA : ℂ) * Complex.I) = 1) :
    ∃ n : ℤ, lamAB + lamBC + lamCA = 2 * Real.pi * n := by
  apply (real_phase_eq_one_iff_integer_multiple
    (lamAB + lamBC + lamCA)).mp
  calc
    Complex.exp (((lamAB + lamBC + lamCA : ℝ) : ℂ) * Complex.I) =
        Complex.exp ((lamAB : ℂ) * Complex.I) *
          Complex.exp ((lamBC : ℂ) * Complex.I) *
          Complex.exp ((lamCA : ℂ) * Complex.I) := by
            rw [← Complex.exp_add, ← Complex.exp_add]
            congr 1
            push_cast
            ring
    _ = 1 := hcocycle

/-- Circulação do levantamento linear `χ(θ)=αθ`. -/
noncomputable def phaseCirculation (ℏ α : ℝ) : ℝ :=
  2 * Real.pi * ℏ * α

/--
Uma fase globalmente fechada tem circulação inteira em unidades
`h = 2πℏ`.
-/
theorem phaseCirculation_quantized
    (ℏ α : ℝ)
    (hclose : circularPhase α (2 * Real.pi) = circularPhase α 0) :
    ∃ n : ℤ, phaseCirculation ℏ α = n * (2 * Real.pi * ℏ) := by
  obtain ⟨n, rfl⟩ := (circularPhase_closes_iff_integer α).mp hclose
  refine ⟨n, ?_⟩
  simp [phaseCirculation]
  ring

/--
Forma rigorosa de Poisson disponível no formalismo: a igualdade vale para
funções de Schwartz, com somas convergentes.

Esta proposição certifica a etapa harmônica posterior à seleção topológica
dos caracteres inteiros. O limite para o pente de deltas pertence à teoria
de distribuições temperadas e não é usado para derivar a integralidade.
-/
theorem poisson_summation_for_schwartz
    (f : SchwartzMap ℝ ℂ) (x : ℝ) :
    ∑' n : ℤ, f (x + n) =
      ∑' n : ℤ, 𝓕 f n * fourier n (x : UnitAddCircle) := by
  exact SchwartzMap.tsum_eq_tsum_fourier f x

end GDQ
