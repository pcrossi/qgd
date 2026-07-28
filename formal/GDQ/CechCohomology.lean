import GDQ.CechChern
import Mathlib.GroupTheory.QuotientGroup.Basic

namespace GDQ

/-!
# Complexo de Čech inteiro em graus 1 e 2

Este arquivo constrói a infraestrutura algébrica mínima necessária para
transformar os inteiros locais `nABC` numa classe global:

* cochains inteiras em graus 1, 2 e 3;
* operadores de cobordo `δ₁` e `δ₂`;
* a identidade `δ₂ ∘ δ₁ = 0`;
* cociclos de grau 2;
* cobordos de grau 2;
* o quociente `H² = Z² / B²`;
* invariância da classe ao somar um cobordo.

O tipo de índices representa o nervo de uma cobertura. Condições geométricas
sobre interseções vazias ou uma boa cobertura devem ser acrescentadas na
aplicação a uma variedade concreta.
-/

/-- 1-cochains inteiras no índice de uma cobertura. -/
abbrev CechCochain1 (ι : Type*) :=
  ι → ι → ℤ

/-- 2-cochains inteiras no índice de uma cobertura. -/
abbrev CechCochain2 (ι : Type*) :=
  ι → ι → ι → ℤ

/-- 3-cochains inteiras no índice de uma cobertura. -/
abbrev CechCochain3 (ι : Type*) :=
  ι → ι → ι → ι → ℤ

/-- Cobordo de uma 1-cochain, com a convenção orientada padrão. -/
def cechD1 (ι : Type*) :
    CechCochain1 ι →+ CechCochain2 ι where
  toFun k := fun a b c ↦ k b c - k a c + k a b
  map_zero' := by
    funext a b c
    simp
  map_add' k l := by
    funext a b c
    simp
    ring

/-- Cobordo de uma 2-cochain. -/
def cechD2 (ι : Type*) :
    CechCochain2 ι →+ CechCochain3 ι where
  toFun n := fun a b c d ↦
    n b c d - n a c d + n a b d - n a b c
  map_zero' := by
    funext a b c d
    simp
  map_add' n m := by
    funext a b c d
    simp
    ring

/-- Identidade fundamental do complexo: `δ₂(δ₁k)=0`. -/
theorem cechD2_cechD1_zero
    (ι : Type*) (k : CechCochain1 ι) :
    cechD2 ι (cechD1 ι k) = 0 := by
  funext a b c d
  simp [cechD1, cechD2]
  ring

/-- Subgrupo das 2-cochains fechadas. -/
def CechTwoCocycles (ι : Type*) :
    AddSubgroup (CechCochain2 ι) :=
  (cechD2 ι).ker

/-- O cobordo de toda 1-cochain é um 2-cociclo. -/
def cechD1ToCocycles (ι : Type*) :
    CechCochain1 ι →+ CechTwoCocycles ι where
  toFun k := ⟨cechD1 ι k, cechD2_cechD1_zero ι k⟩
  map_zero' := by
    ext a b c
    simp [cechD1]
  map_add' k l := by
    ext a b c
    simp [cechD1]
    ring

/-- Subgrupo dos 2-cobordos dentro dos 2-cociclos. -/
def CechTwoCoboundaries (ι : Type*) :
    AddSubgroup (CechTwoCocycles ι) :=
  (cechD1ToCocycles ι).range

/--
Segundo grupo de cohomologia de Čech do complexo inteiro associado ao índice.
-/
abbrev CechH2 (ι : Type*) :=
  (CechTwoCocycles ι) ⧸ (CechTwoCoboundaries ι)

/-- Classe de cohomologia de um 2-cociclo. -/
def cechH2Class (ι : Type*) :
    CechTwoCocycles ι →+ CechH2 ι :=
  QuotientAddGroup.mk' (CechTwoCoboundaries ι)

/-- Todo cobordo representa a classe zero. -/
theorem cechH2Class_coboundary_zero
    (ι : Type*) (k : CechCochain1 ι) :
    cechH2Class ι (cechD1ToCocycles ι k) = 0 := by
  change
    ((cechD1ToCocycles ι k : CechTwoCocycles ι) : CechH2 ι) = 0
  rw [QuotientAddGroup.eq_zero_iff]
  exact ⟨k, rfl⟩

/--
Somar um cobordo a um cociclo não altera sua classe de cohomologia.
-/
theorem cechH2Class_add_coboundary
    (ι : Type*)
    (n : CechTwoCocycles ι)
    (k : CechCochain1 ι) :
    cechH2Class ι (n + cechD1ToCocycles ι k) =
      cechH2Class ι n := by
  rw [map_add, cechH2Class_coboundary_zero, add_zero]

/--
Versão subtrativa: dois cociclos que diferem por um cobordo têm a mesma
classe.
-/
theorem cechH2Class_eq_of_sub_eq_coboundary
    (ι : Type*)
    (n n' : CechTwoCocycles ι)
    (k : CechCochain1 ι)
    (h : n' - n = cechD1ToCocycles ι k) :
    cechH2Class ι n' = cechH2Class ι n := by
  have hn : n' = n + cechD1ToCocycles ι k := by
    rw [← h]
    abel
  rw [hn, cechH2Class_add_coboundary]

/-! ## Ligação com funções de transição `U(1)` -/

/--
Levantamentos reais das funções de transição de uma cobertura.

`antisymm` fixa a convenção orientada `lam j i = -lam i j`.
`cocycle` é a condição multiplicativa em toda interseção tripla.
-/
structure U1CechLiftData (ι : Type*) where
  lam : ι → ι → ℝ
  antisymm : ∀ i j, lam j i = -lam i j
  cocycle : ∀ i j k,
    Complex.exp ((lam i j : ℂ) * Complex.I) *
        Complex.exp ((lam j k : ℂ) * Complex.I) *
        Complex.exp ((lam k i : ℂ) * Complex.I) = 1

/-- Restrição dos dados globais a uma interseção tripla. -/
noncomputable def U1CechLiftData.triple
    {ι : Type*} (u : U1CechLiftData ι)
    (i j k : ι) :
    U1TripleLift where
  lamAB := u.lam i j
  lamBC := u.lam j k
  lamCA := u.lam k i
  cocycle := u.cocycle i j k

/-- 2-cochain inteira produzida pelos cociclos levantados. -/
noncomputable def U1CechLiftData.integerCochain
    {ι : Type*} (u : U1CechLiftData ι) :
    CechCochain2 ι :=
  fun i j k ↦ (u.triple i j k).cechInteger

/-- Equação local satisfeita pela 2-cochain inteira. -/
theorem U1CechLiftData.integerCochain_spec
    {ι : Type*} (u : U1CechLiftData ι)
    (i j k : ι) :
    u.lam i j + u.lam j k + u.lam k i =
      2 * Real.pi * u.integerCochain i j k := by
  exact (u.triple i j k).cechInteger_spec

/--
A 2-cochain inteira construída das transições `U(1)` é fechada.

Esta é a passagem algébrica de `n_ijk` para um elemento de `Z²`.
-/
theorem U1CechLiftData.integerCochain_closed
    {ι : Type*} (u : U1CechLiftData ι) :
    cechD2 ι u.integerCochain = 0 := by
  funext i j k l
  have h_jkl := u.integerCochain_spec j k l
  have h_ikl := u.integerCochain_spec i k l
  have h_ijl := u.integerCochain_spec i j l
  have h_ijk := u.integerCochain_spec i j k
  have hreal :
      2 * Real.pi *
          ((cechD2 ι u.integerCochain i j k l : ℤ) : ℝ) = 0 := by
    simp only [cechD2, AddMonoidHom.coe_mk, ZeroHom.coe_mk]
    push_cast
    calc
      2 * Real.pi *
          ((u.integerCochain j k l : ℝ) -
            (u.integerCochain i k l : ℝ) +
            (u.integerCochain i j l : ℝ) -
            (u.integerCochain i j k : ℝ)) =
          2 * Real.pi * (u.integerCochain j k l : ℝ) -
            2 * Real.pi * (u.integerCochain i k l : ℝ) +
            2 * Real.pi * (u.integerCochain i j l : ℝ) -
            2 * Real.pi * (u.integerCochain i j k : ℝ) := by
              ring
      _ =
          (u.lam j k + u.lam k l + u.lam l j) -
            (u.lam i k + u.lam k l + u.lam l i) +
            (u.lam i j + u.lam j l + u.lam l i) -
            (u.lam i j + u.lam j k + u.lam k i) := by
              rw [← h_jkl, ← h_ikl, ← h_ijl, ← h_ijk]
      _ = 0 := by
        rw [u.antisymm l j, u.antisymm j l,
          u.antisymm k i, u.antisymm i k]
        ring
  have hπ : (2 * Real.pi : ℝ) ≠ 0 := by positivity
  have hz :
      ((cechD2 ι u.integerCochain i j k l : ℤ) : ℝ) = 0 :=
    (mul_eq_zero.mp hreal).resolve_left hπ
  exact_mod_cast hz

/-- O cociclo inteiro global associado às transições `U(1)`. -/
noncomputable def U1CechLiftData.integerCocycle
    {ι : Type*} (u : U1CechLiftData ι) :
    CechTwoCocycles ι :=
  ⟨u.integerCochain, u.integerCochain_closed⟩

/--
Primeira classe de Chern definida como a classe do cociclo inteiro obtido das
funções de transição levantadas.
-/
noncomputable def U1CechLiftData.firstChernClass
    {ι : Type*} (u : U1CechLiftData ι) :
    CechH2 ι :=
  cechH2Class ι u.integerCocycle

/-! ## Independência global dos levantamentos -/

/-- Mudança inteira e orientada dos levantamentos locais. -/
structure CechLiftGauge (ι : Type*) where
  k : CechCochain1 ι
  antisymm : ∀ i j, k j i = -k i j

/--
Mudança global dos levantamentos por `2π k_ij`.

Ela preserva as funções de transição e a condição de cociclo em `U(1)`.
-/
noncomputable def U1CechLiftData.shift
    {ι : Type*} (u : U1CechLiftData ι)
    (q : CechLiftGauge ι) :
    U1CechLiftData ι where
  lam i j := u.lam i j + 2 * Real.pi * q.k i j
  antisymm i j := by
    rw [u.antisymm i j, q.antisymm i j]
    push_cast
    ring
  cocycle i j k := by
    rw [complex_exp_phase_add_two_pi_int,
      complex_exp_phase_add_two_pi_int,
      complex_exp_phase_add_two_pi_int]
    exact u.cocycle i j k

/--
A 2-cochain inteira muda pelo cobordo da 1-cochain inteira que muda os
levantamentos.
-/
theorem U1CechLiftData.integerCochain_shift
    {ι : Type*} (u : U1CechLiftData ι)
    (q : CechLiftGauge ι) :
    (u.shift q).integerCochain =
      u.integerCochain + cechD1 ι q.k := by
  funext i j k
  apply two_pi_int_multiple_injective
  calc
    2 * Real.pi * (u.shift q).integerCochain i j k =
        (u.shift q).lam i j +
          (u.shift q).lam j k +
          (u.shift q).lam k i := by
            rw [(u.shift q).integerCochain_spec]
    _ = (u.lam i j + u.lam j k + u.lam k i) +
          2 * Real.pi *
            ((q.k i j : ℝ) + (q.k j k : ℝ) + (q.k k i : ℝ)) := by
            simp only [U1CechLiftData.shift]
            ring
    _ = 2 * Real.pi * (u.integerCochain i j k : ℝ) +
          2 * Real.pi *
            ((q.k i j : ℝ) + (q.k j k : ℝ) + (q.k k i : ℝ)) := by
            rw [u.integerCochain_spec i j k]
    _ = 2 * Real.pi *
          ((u.integerCochain i j k : ℝ) +
            (cechD1 ι q.k i j k : ℝ)) := by
            simp only [cechD1, AddMonoidHom.coe_mk,
              ZeroHom.coe_mk]
            rw [q.antisymm i k]
            push_cast
            ring
    _ = 2 * Real.pi *
          (((u.integerCochain + cechD1 ι q.k) i j k : ℤ) : ℝ) := by
            simp

/-- A mudança dos levantamentos altera o cociclo inteiro por um cobordo. -/
theorem U1CechLiftData.integerCocycle_shift
    {ι : Type*} (u : U1CechLiftData ι)
    (q : CechLiftGauge ι) :
    (u.shift q).integerCocycle =
      u.integerCocycle + cechD1ToCocycles ι q.k := by
  ext i j k
  exact congrFun (congrFun (congrFun (u.integerCochain_shift q) i) j) k

/--
A primeira classe de Chern é independente da escolha dos levantamentos
reais das funções de transição.
-/
theorem U1CechLiftData.firstChernClass_shift
    {ι : Type*} (u : U1CechLiftData ι)
    (q : CechLiftGauge ι) :
    (u.shift q).firstChernClass = u.firstChernClass := by
  rw [U1CechLiftData.firstChernClass,
    U1CechLiftData.firstChernClass,
    u.integerCocycle_shift q,
    cechH2Class_add_coboundary]

end GDQ
