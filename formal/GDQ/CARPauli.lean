import Mathlib.Algebra.Module.Defs
import Mathlib.Tactic

namespace GDQ

/-!
# Relações CAR e exclusão de Pauli

Este módulo formaliza somente a consequência algébrica das relações de
anticomutação canônicas. Ele não deriva CAR da ação oficial: essa passagem
continua pertencendo ao teorema spin--estatística condicional no setor
Lorentziano, positivo e graduadamente local.
-/

variable {A Mode X : Type*}

/--
Dados mínimos do setor de criação fermiônico. O espaço de operadores é
suposto linear sobre `ℚ`, hipótese suficiente para excluir torção de ordem
dois e dividir a relação `2x = 0`.
-/
structure CreationCAR
    (A Mode : Type*)
    [AddCommGroup A] [Module ℚ A] [Mul A] where
  create : Mode → A
  creation_anticomm :
    ∀ i j, create i * create j + create j * create i = 0

/--
Se um elemento satisfaz sua relação CAR consigo mesmo, seu quadrado é nulo.
-/
theorem square_zero_of_self_anticomm
    [AddCommGroup A] [Module ℚ A] [Mul A]
    (a : A)
    (hcar : a * a + a * a = 0) :
    a * a = 0 := by
  have hhalf :=
    congrArg (fun z : A => (1 / 2 : ℚ) • z) hcar
  simpa [smul_add, ← add_smul] using hhalf

/-- As CAR de criação implicam a exclusão de ocupação dupla no mesmo modo. -/
theorem CreationCAR.pauli
    [AddCommGroup A] [Module ℚ A] [Mul A]
    (car : CreationCAR A Mode) (i : Mode) :
    car.create i * car.create i = 0 := by
  apply square_zero_of_self_anticomm
  exact car.creation_anticomm i i

/--
Versão em funções de onda: antissimetria de troca implica anulação na
diagonal, desde que os valores formem um espaço linear de característica
zero.
-/
theorem antisymmetric_wavefunction_vanishes_on_diagonal
    [AddCommGroup A] [Module ℚ A]
    (ψ : X → X → A)
    (hswap : ∀ x y, ψ x y = -ψ y x)
    (x : X) :
    ψ x x = 0 := by
  have hself : ψ x x + ψ x x = 0 := by
    calc
      ψ x x + ψ x x = -ψ x x + ψ x x := by
        exact congrArg (fun z : A => z + ψ x x) (hswap x x)
      _ = 0 := neg_add_cancel (ψ x x)
  have hhalf :=
    congrArg (fun z : A => (1 / 2 : ℚ) • z) hself
  simpa [smul_add, ← add_smul] using hhalf

end GDQ
