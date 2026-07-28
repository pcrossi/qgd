import GDQ.PhaseQuantization

namespace GDQ

/-!
# Cociclo de Čech e precursor formal da primeira classe de Chern

Este módulo formaliza a etapa local que transforma funções de transição
`U(1)` em um cociclo inteiro.

Numa interseção tripla, escolhemos levantamentos reais
`lamAB`, `lamBC`, `lamCA`. A condição multiplicativa

`gAB * gBC * gCA = 1`

implica

`lamAB + lamBC + lamCA = 2π nABC`.

Mudanças dos levantamentos por múltiplos inteiros de `2π` alteram `nABC`
por um cobordo inteiro. Assim, o representante depende da escolha de
levantamentos, mas sua classe de cohomologia não depende.

O quociente cohomológico global sobre uma cobertura inteira ainda não é
construído neste arquivo.
-/

/-- Dados levantados de um cociclo `U(1)` numa interseção tripla. -/
structure U1TripleLift where
  lamAB : ℝ
  lamBC : ℝ
  lamCA : ℝ
  cocycle :
    Complex.exp ((lamAB : ℂ) * Complex.I) *
        Complex.exp ((lamBC : ℂ) * Complex.I) *
        Complex.exp ((lamCA : ℂ) * Complex.I) = 1

/-- Existência do representante inteiro associado à interseção tripla. -/
theorem U1TripleLift.exists_cechInteger
    (c : U1TripleLift) :
    ∃ n : ℤ,
      c.lamAB + c.lamBC + c.lamCA = 2 * Real.pi * n := by
  exact u1_triple_overlap_integer
    c.lamAB c.lamBC c.lamCA c.cocycle

/-- O inteiro de Čech escolhido para o cociclo levantado. -/
noncomputable def U1TripleLift.cechInteger
    (c : U1TripleLift) : ℤ :=
  Classical.choose c.exists_cechInteger

/-- O inteiro escolhido satisfaz a equação de cociclo levantada. -/
theorem U1TripleLift.cechInteger_spec
    (c : U1TripleLift) :
    c.lamAB + c.lamBC + c.lamCA =
      2 * Real.pi * c.cechInteger := by
  exact Classical.choose_spec c.exists_cechInteger

/-- Múltiplos inteiros de `2π` têm coeficiente único. -/
theorem two_pi_int_multiple_injective
    {m n : ℤ}
    (h : 2 * Real.pi * m = 2 * Real.pi * n) :
    m = n := by
  have hπ : (2 * Real.pi : ℝ) ≠ 0 := by positivity
  have hcast : (m : ℝ) = (n : ℝ) := by
    exact mul_left_cancel₀ hπ h
  exact_mod_cast hcast

/--
Mudança dos três levantamentos por múltiplos de `2π`.

As funções de transição em `U(1)` não mudam, pois o exponencial dos
múltiplos inteiros de `2π` é a unidade.
-/
noncomputable def U1TripleLift.shift
    (c : U1TripleLift)
    (kAB kBC kCA : ℤ) :
    U1TripleLift where
  lamAB := c.lamAB + 2 * Real.pi * kAB
  lamBC := c.lamBC + 2 * Real.pi * kBC
  lamCA := c.lamCA + 2 * Real.pi * kCA
  cocycle := by
    have hab :
        Complex.exp
            (((c.lamAB + 2 * Real.pi * kAB : ℝ) : ℂ) * Complex.I) =
          Complex.exp ((c.lamAB : ℂ) * Complex.I) := by
      rw [show
        (((c.lamAB + 2 * Real.pi * kAB : ℝ) : ℂ) * Complex.I) =
          (c.lamAB : ℂ) * Complex.I +
            (kAB : ℂ) * (2 * Real.pi * Complex.I) by
              push_cast
              ring]
      rw [Complex.exp_add]
      simp
    have hbc :
        Complex.exp
            (((c.lamBC + 2 * Real.pi * kBC : ℝ) : ℂ) * Complex.I) =
          Complex.exp ((c.lamBC : ℂ) * Complex.I) := by
      rw [show
        (((c.lamBC + 2 * Real.pi * kBC : ℝ) : ℂ) * Complex.I) =
          (c.lamBC : ℂ) * Complex.I +
            (kBC : ℂ) * (2 * Real.pi * Complex.I) by
              push_cast
              ring]
      rw [Complex.exp_add]
      simp
    have hca :
        Complex.exp
            (((c.lamCA + 2 * Real.pi * kCA : ℝ) : ℂ) * Complex.I) =
          Complex.exp ((c.lamCA : ℂ) * Complex.I) := by
      rw [show
        (((c.lamCA + 2 * Real.pi * kCA : ℝ) : ℂ) * Complex.I) =
          (c.lamCA : ℂ) * Complex.I +
            (kCA : ℂ) * (2 * Real.pi * Complex.I) by
              push_cast
              ring]
      rw [Complex.exp_add]
      simp
    rw [hab, hbc, hca]
    exact c.cocycle

/--
Lei de transformação do representante inteiro de Čech.

O termo `kAB + kBC + kCA` é o cobordo inteiro da mudança de levantamentos
na interseção tripla.
-/
theorem U1TripleLift.cechInteger_shift
    (c : U1TripleLift)
    (kAB kBC kCA : ℤ) :
    (c.shift kAB kBC kCA).cechInteger =
      c.cechInteger + kAB + kBC + kCA := by
  apply two_pi_int_multiple_injective
  calc
    2 * Real.pi * (c.shift kAB kBC kCA).cechInteger =
        (c.shift kAB kBC kCA).lamAB +
          (c.shift kAB kBC kCA).lamBC +
          (c.shift kAB kBC kCA).lamCA := by
            rw [(c.shift kAB kBC kCA).cechInteger_spec]
    _ = 2 * Real.pi *
          ((c.cechInteger + kAB + kBC + kCA : ℤ) : ℝ) := by
            simp only [U1TripleLift.shift]
            push_cast
            calc
              c.lamAB + 2 * Real.pi * (kAB : ℝ) +
                    (c.lamBC + 2 * Real.pi * (kBC : ℝ)) +
                    (c.lamCA + 2 * Real.pi * (kCA : ℝ)) =
                  (c.lamAB + c.lamBC + c.lamCA) +
                    2 * Real.pi *
                      ((kAB : ℝ) + (kBC : ℝ) + (kCA : ℝ)) := by
                        ring
              _ = 2 * Real.pi * (c.cechInteger : ℝ) +
                    2 * Real.pi *
                      ((kAB : ℝ) + (kBC : ℝ) + (kCA : ℝ)) := by
                        rw [c.cechInteger_spec]
              _ = 2 * Real.pi *
                    ((c.cechInteger : ℝ) + (kAB : ℝ) +
                      (kBC : ℝ) + (kCA : ℝ)) := by
                        ring

/--
O representante muda exatamente por um cobordo; portanto sua classe módulo
cobordos é invariante.
-/
theorem U1TripleLift.cechInteger_shift_sub
    (c : U1TripleLift)
    (kAB kBC kCA : ℤ) :
    (c.shift kAB kBC kCA).cechInteger - c.cechInteger =
      kAB + kBC + kCA := by
  rw [c.cechInteger_shift]
  ring

end GDQ
