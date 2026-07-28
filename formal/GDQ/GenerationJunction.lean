import GDQ.C3ConcreteHessian
import GDQ.APSHopfBismut
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.Tactic

namespace GDQ

open scoped BigOperators

/-!
# Seleção do junction e aditividade geracional

Este módulo formaliza o elo lógico que faltava entre:

1. o vínculo horizontal de Noether;
2. a dimensão do kernel de sua linearização;
3. a seleção de três centros por isolamento módulo rotação comum;
4. a aditividade do índice APS local;
5. a contagem de componentes quirais.

O teorema não afirma que todo background da ação oficial satisfaz as
hipóteses de posto e isolamento. Ele prova que, quando a linearização do
vínculo horizontal tem posto dois e o único modo nulo é a rotação comum, o
número de centros é necessariamente três.
-/

/--
Certificado linearizado de um junction horizontal com `N` centros.

`fullHorizontalRank` codifica que as duas componentes horizontais do vínculo
de Noether são independentes. `isolatedModuloCommonRotation` codifica que o
kernel possui somente a rotação global.
-/
structure HorizontalJunctionCertificate (N : ℕ) where
  closureDifferential :
    (Fin N → ℝ) →ₗ[ℝ] (Fin 2 → ℝ)
  fullHorizontalRank :
    Module.finrank ℝ (LinearMap.range closureDifferential) = 2
  isolatedModuloCommonRotation :
    Module.finrank ℝ (LinearMap.ker closureDifferential) = 1

/--
Posto dois mais isolamento módulo uma rotação comum selecionam `N=3`.

Esta é a aplicação direta de posto--nulidade:
`2 + 1 = dim (ℝ^N) = N`.
-/
theorem isolated_horizontal_junction_has_three_centers
    {N : ℕ}
    (J : HorizontalJunctionCertificate N) :
    N = 3 := by
  have hdim :=
    LinearMap.finrank_range_add_finrank_ker J.closureDifferential
  rw [J.fullHorizontalRank, J.isolatedModuloCommonRotation] at hdim
  simpa using hdim.symm

/--
Se a linearização tem posto dois, a dimensão total do kernel é `N-2`.
-/
theorem horizontal_junction_kernel_dimension
    {N : ℕ}
    (D : (Fin N → ℝ) →ₗ[ℝ] (Fin 2 → ℝ))
    (hRank : Module.finrank ℝ (LinearMap.range D) = 2) :
    Module.finrank ℝ (LinearMap.ker D) = N - 2 := by
  have hdim := LinearMap.finrank_range_add_finrank_ker D
  rw [hRank] at hdim
  have hN : 2 ≤ N := by
    have : 2 ≤ Module.finrank ℝ (Fin N → ℝ) := by omega
    simpa using this
  have htotal : Module.finrank ℝ (Fin N → ℝ) = N := by simp
  rw [htotal] at hdim
  omega

/--
Depois de remover a rotação comum, sob `N≥3`, restam `N-3` modos nulos
internos.
-/
theorem horizontal_junction_internal_zero_modes
    {N : ℕ}
    (hN : 3 ≤ N)
    (D : (Fin N → ℝ) →ₗ[ℝ] (Fin 2 → ℝ))
    (hRank : Module.finrank ℝ (LinearMap.range D) = 2) :
    Module.finrank ℝ (LinearMap.ker D) - 1 = N - 3 := by
  rw [horizontal_junction_kernel_dimension D hRank]
  omega

/-- Tensões cartesianas do equilíbrio equilátero `C₃`. -/
noncomputable def c3EquilibriumTension
    (T : ℝ) : Fin 3 → Fin 2 → ℝ :=
  ![
    ![T, 0],
    ![-T / 2, Real.sqrt 3 * T / 2],
    ![-T / 2, -Real.sqrt 3 * T / 2]
  ]

/-- O equilíbrio equilátero satisfaz exatamente o fechamento de Noether. -/
theorem c3EquilibriumTension_sum_zero
    (T : ℝ) :
    ∑ a, c3EquilibriumTension T a = (fun _ => 0) := by
  funext i
  fin_cases i <;>
    (simp [c3EquilibriumTension, Fin.sum_univ_succ] <;> ring)

/-- Soma dos índices APS locais de um conjunto finito de estômatos. -/
def totalLocalAPSIndex
    {N : ℕ}
    (localIndex : Fin N → ℤ) : ℤ :=
  ∑ a, localIndex a

/-- `N` estômatos primitivos coorientados possuem índice total `N`. -/
theorem totalLocalAPSIndex_primitive
    (N : ℕ) :
    totalLocalAPSIndex (fun _ : Fin N => (1 : ℤ)) = N := by
  simp [totalLocalAPSIndex]

/-- Uma unidade local de índice acompanha quinze componentes de Weyl. -/
def oneGenerationWeylCount : ℕ :=
  3 * 2 + 3 * 1 + 3 * 1 + 1 * 2 + 1 * 1

theorem oneGenerationWeylCount_eq_fifteen :
    oneGenerationWeylCount = 15 := by
  norm_num [oneGenerationWeylCount]

/-- Contagem quiral para `N` unidades locais de índice. -/
def totalWeylCount (N : ℕ) : ℕ :=
  N * oneGenerationWeylCount

/--
O junction isolado e primitivo possui três unidades de índice e 45
componentes de Weyl.
-/
theorem isolated_primitive_junction_generation_count
    {N : ℕ}
    (J : HorizontalJunctionCertificate N) :
    totalLocalAPSIndex (fun _ : Fin N => (1 : ℤ)) = 3 ∧
      totalWeylCount N = 45 := by
  have hN := isolated_horizontal_junction_has_three_centers J
  subst N
  constructor
  · norm_num [totalLocalAPSIndex]
  · norm_num [totalWeylCount, oneGenerationWeylCount]

end GDQ
