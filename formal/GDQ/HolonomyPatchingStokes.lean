import GDQ.AharonovBohmHolonomy
import GDQ.SagnacHolonomy
import GDQ.CechChern
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic

namespace GDQ

/-!
# Colagem, Stokes celular e normalização de Sagnac

Este módulo certifica o núcleo finito e algébrico comum aos efeitos
Aharonov--Bohm e Sagnac.

* `discrete_stokes` é a identidade exata entre a soma da curvatura nas faces
  e a circulação na cadeia de bordo. Ela é a realização celular finita de
  Stokes; não pretende substituir o teorema suave sobre variedades.
* `u1Holonomy_add_integer_period` mostra que mudanças de levantamento por
  múltiplos inteiros de `2π` não alteram a colagem física.
* `sagnacTimeDelay_of_rotationCirculation` deriva o fator quatro depois que
  a circulação cinemática vale `2 Ω·A`.

Os dados geométricos do domínio perfurado e do interferômetro real continuam
entrando como hipóteses explícitas.
-/

section CellularStokes

variable {Edge Face : Type*} [Fintype Edge] [Fintype Face]

/-- Cobordo discreto de um potencial de aresta, avaliado numa face. -/
def discreteCurvature
    (incidence : Face → Edge → ℝ)
    (potential : Edge → ℝ)
    (face : Face) : ℝ :=
  ∑ edge, incidence face edge * potential edge

/-- Coeficiente de cada aresta no bordo da cadeia ponderada de faces. -/
def discreteBoundaryCoefficient
    (faceWeight : Face → ℝ)
    (incidence : Face → Edge → ℝ)
    (edge : Edge) : ℝ :=
  ∑ face, faceWeight face * incidence face edge

/-- Circulação do potencial no bordo discreto. -/
def discreteBoundaryCirculation
    (faceWeight : Face → ℝ)
    (incidence : Face → Edge → ℝ)
    (potential : Edge → ℝ) : ℝ :=
  ∑ edge,
    discreteBoundaryCoefficient faceWeight incidence edge * potential edge

/-- Fluxo da curvatura discreta através da cadeia de faces. -/
def discreteFlux
    (faceWeight : Face → ℝ)
    (incidence : Face → Edge → ℝ)
    (potential : Edge → ℝ) : ℝ :=
  ∑ face, faceWeight face * discreteCurvature incidence potential face

/--
Teorema de Stokes celular finito.

As contribuições de arestas internas cancelam na soma orientada codificada
pela matriz de incidência; resta exatamente a circulação do bordo.
-/
theorem discrete_stokes
    (faceWeight : Face → ℝ)
    (incidence : Face → Edge → ℝ)
    (potential : Edge → ℝ) :
    discreteBoundaryCirculation faceWeight incidence potential =
      discreteFlux faceWeight incidence potential := by
  simp only [discreteBoundaryCirculation, discreteBoundaryCoefficient,
    discreteFlux, discreteCurvature]
  calc
    (∑ edge, (∑ face, faceWeight face * incidence face edge) *
        potential edge) =
        ∑ edge, ∑ face,
          (faceWeight face * incidence face edge) * potential edge := by
            apply Finset.sum_congr rfl
            intro edge _
            rw [Finset.sum_mul]
    _ = ∑ face, ∑ edge,
          (faceWeight face * incidence face edge) * potential edge := by
            rw [Finset.sum_comm]
    _ = ∑ face,
          faceWeight face *
            ∑ edge, incidence face edge * potential edge := by
            apply Finset.sum_congr rfl
            intro face _
            rw [Finset.mul_sum]
            apply Finset.sum_congr rfl
            intro edge _
            ring

/--
O representante harmônico `A = Φ dθ/(2π)` possui circulação total `Φ`
quando os incrementos angulares somam `2π`.
-/
theorem harmonicRepresentative_circulation
    (dtheta : Edge → ℝ)
    (flux : ℝ)
    (hAngle : ∑ edge, dtheta edge = 2 * Real.pi) :
    ∑ edge, (flux / (2 * Real.pi)) * dtheta edge = flux := by
  rw [← Finset.mul_sum, hAngle]
  field_simp [Real.pi_ne_zero]

end CellularStokes

section U1Patching

/-- Holonomia `U(1)` de uma fase real. -/
noncomputable def u1Holonomy (phase : ℝ) : ℂ :=
  Complex.exp ((phase : ℂ) * Complex.I)

/-- A concatenação de caminhos soma fases e multiplica holonomias. -/
theorem u1Holonomy_add
    (phase₁ phase₂ : ℝ) :
    u1Holonomy (phase₁ + phase₂) =
      u1Holonomy phase₁ * u1Holonomy phase₂ := by
  unfold u1Holonomy
  rw [show
    (((phase₁ + phase₂ : ℝ) : ℂ) * Complex.I) =
      (phase₁ : ℂ) * Complex.I + (phase₂ : ℂ) * Complex.I by
        push_cast
        ring]
  exact Complex.exp_add _ _

/-- Mudar um levantamento por `2π n` não altera a holonomia física. -/
theorem u1Holonomy_add_integer_period
    (phase : ℝ)
    (n : ℤ) :
    u1Holonomy (phase + 2 * Real.pi * n) = u1Holonomy phase := by
  unfold u1Holonomy
  rw [show
    (((phase + 2 * Real.pi * n : ℝ) : ℂ) * Complex.I) =
      (phase : ℂ) * Complex.I +
        (n : ℂ) * (2 * Real.pi * Complex.I) by
          push_cast
          ring]
  rw [Complex.exp_add]
  simp

/-- A meia-volta possui holonomia `-1`. -/
theorem u1Holonomy_half_turn :
    u1Holonomy Real.pi = -1 := by
  change Complex.exp ((Real.pi : ℂ) * Complex.I) = -1
  exact Complex.exp_pi_mul_I

/-- Dados mínimos da colagem de dois patches por um levantamento real. -/
structure TwoPatchU1Gluing where
  transitionLift : ℝ

/-- Holonomia da função de transição no recobrimento de dois patches. -/
noncomputable def TwoPatchU1Gluing.holonomy
    (g : TwoPatchU1Gluing) : ℂ :=
  u1Holonomy g.transitionLift

/-- Mudança do levantamento local por um enrolamento inteiro. -/
noncomputable def TwoPatchU1Gluing.shift
    (g : TwoPatchU1Gluing)
    (n : ℤ) : TwoPatchU1Gluing where
  transitionLift := g.transitionLift + 2 * Real.pi * n

/-- A colagem física independe do levantamento escolhido. -/
theorem TwoPatchU1Gluing.holonomy_shift
    (g : TwoPatchU1Gluing)
    (n : ℤ) :
    (g.shift n).holonomy = g.holonomy := by
  exact u1Holonomy_add_integer_period g.transitionLift n

/-- A fase de Aharonov--Bohm é a holonomia `U(1)` da circulação pesada. -/
theorem aharonovBohmHolonomy_eq_u1
    (charge hbar circulation : ℝ) :
    aharonovBohmHolonomy charge hbar circulation =
      u1Holonomy (charge * circulation / hbar) := by
  rfl

end U1Patching

section SagnacNormalization

/-- Atraso temporal obtido de uma circulação cinemática orientada. -/
noncomputable def sagnacTimeDelay
    (c circulation : ℝ) : ℝ :=
  (2 / c ^ 2) * circulation

/--
Se a circulação do campo de rotação vale `2 Ω·A`, os dois sentidos de
propagação produzem o atraso `4 Ω·A/c²`.
-/
theorem sagnacTimeDelay_of_rotationCirculation
    (c circulation omegaArea : ℝ)
    (hCirculation : circulation = 2 * omegaArea) :
    sagnacTimeDelay c circulation = 4 * omegaArea / c ^ 2 := by
  rw [hCirculation]
  unfold sagnacTimeDelay
  ring

/-- A inversão da rotação inverte o atraso temporal. -/
theorem sagnacTimeDelay_rotation_reversal
    (c omegaArea : ℝ) :
    4 * (-omegaArea) / c ^ 2 = -(4 * omegaArea / c ^ 2) := by
  ring

end SagnacNormalization

end GDQ
