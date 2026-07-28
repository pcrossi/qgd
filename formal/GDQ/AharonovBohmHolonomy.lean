import Mathlib.Analysis.Complex.Exponential
import Mathlib.Tactic

namespace GDQ

/-!
# Holonomia de Aharonov--Bohm

O núcleo topológico do efeito é uma holonomia exponencial dependente da
circulação da conexão. O potencial local pode mudar por um gradiente, mas a
circulação em um laço fechado não muda. A identificação da circulação com o
fluxo confinado usa Stokes no domínio físico perfurado e entra aqui como
hipótese geométrica explícita.
-/

/-- Fase de Aharonov--Bohm associada à circulação da conexão. -/
noncomputable def aharonovBohmHolonomy
    (charge hbar circulation : ℝ) : ℂ :=
  Complex.exp (((charge * circulation / hbar : ℝ) : ℂ) * Complex.I)

/-- Mudança da circulação de um caminho aberto sob `A ↦ A + dλ`. -/
def gaugeShiftedCirculation
    (circulation lambdaStart lambdaEnd : ℝ) : ℝ :=
  circulation + (lambdaEnd - lambdaStart)

/-- Em um laço fechado, o termo de calibre possui extremos iguais. -/
theorem gaugeShiftedCirculation_closed
    (circulation lambdaStart lambdaEnd : ℝ)
    (hClosed : lambdaEnd = lambdaStart) :
    gaugeShiftedCirculation circulation lambdaStart lambdaEnd = circulation := by
  simp [gaugeShiftedCirculation, hClosed]

/-- A holonomia de Aharonov--Bohm é invariante sob calibre em laços fechados. -/
theorem aharonovBohmHolonomy_gauge_invariant
    (charge hbar circulation lambdaStart lambdaEnd : ℝ)
    (hClosed : lambdaEnd = lambdaStart) :
    aharonovBohmHolonomy charge hbar
        (gaugeShiftedCirculation circulation lambdaStart lambdaEnd)
      = aharonovBohmHolonomy charge hbar circulation := by
  rw [gaugeShiftedCirculation_closed circulation lambdaStart lambdaEnd hClosed]

/--
Se Stokes identifica a circulação externa com o fluxo confinado, as duas
descrições fornecem a mesma fase observável.
-/
theorem aharonovBohm_circulation_eq_flux
    (charge hbar circulation flux : ℝ)
    (hStokes : circulation = flux) :
    aharonovBohmHolonomy charge hbar circulation
      = aharonovBohmHolonomy charge hbar flux := by
  rw [hStokes]

end GDQ
