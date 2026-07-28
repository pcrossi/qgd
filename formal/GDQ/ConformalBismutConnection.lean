import GDQ.ConformalBismutTorsion
import GDQ.CoordinateGeometry
import Mathlib.Tactic

namespace GDQ

open scoped BigOperators Matrix

/-!
# Conexão coordenada do background Hermitiano conformal

Este módulo eleva o ansatz torsional de `ConformalBismutTorsion` ao nível da
conexão. Em coordenadas reais, usamos

`gᵢⱼ = exp(2φ) δᵢⱼ`, `φ(x)=a x⁰`

e a conexão métrica com torção totalmente antissimétrica

`Γᴮᵏᵢⱼ = Γᴸᶜᵏᵢⱼ + 1/2 gᵏˡ Hᵢⱼₗ`.

As identidades de compatibilidade métrica e de torção são verificadas
componente a componente. Nenhuma ação auxiliar é introduzida.
-/

/-- Delta de Kronecker real em oito dimensões. -/
def delta8 (i j : Index8) : ℝ :=
  if i = j then 1 else 0

@[simp] theorem delta8_self (i : Index8) :
    delta8 i i = 1 := by
  simp [delta8]

theorem delta8_symmetric (i j : Index8) :
    delta8 i j = delta8 j i := by
  simp [delta8, eq_comm]

theorem sum_delta8_left (j : Index8) (F : Index8 → ℝ) :
    ∑ m, delta8 m j * F m = F j := by
  classical
  simp [delta8]

theorem sum_delta8_right (i : Index8) (F : Index8 → ℝ) :
    ∑ m, F m * delta8 i m = F i := by
  classical
  simp [delta8]

/-- Gradiente constante de `φ(x)=a x⁰`. -/
def conformalPhiGradient (a : ℝ) (i : Index8) : ℝ :=
  if i = 0 then a else 0

/-- Métrica real conformal `gᵢⱼ=e^{2φ}δᵢⱼ`. -/
noncomputable def conformalRealMetric
    (a : ℝ) (x : LocalPoint) (i j : Index8) : ℝ :=
  conformalScale a x * delta8 i j

/-- Inversa `gⁱʲ=e^{-2φ}δⁱʲ`. -/
noncomputable def conformalRealInverseMetric
    (a : ℝ) (x : LocalPoint) (i j : Index8) : ℝ :=
  (conformalScale a x)⁻¹ * delta8 i j

/-- Derivada coordenada declarada de `gᵢⱼ`. -/
noncomputable def conformalRealMetricDerivative
    (a : ℝ) (x : LocalPoint) (p i j : Index8) : ℝ :=
  conformalScaleDerivative a x p * delta8 i j

/-- Coeficientes reais da estrutura complexa padrão. -/
def standardComplexCoeff (i j : Index8) : ℝ :=
  if j = standardJPartner i then -standardJSign i else 0

/-- Contração de uma função com o primeiro índice de `J`. -/
theorem sum_mul_standardComplexCoeff_first
    (F : Index8 → ℝ) (j : Index8) :
    ∑ m, F m * standardComplexCoeff m j =
      F (standardJPartner j) * standardJSign j := by
  fin_cases j <;>
    simp only [Fin.sum_univ_succ] <;>
    norm_num [standardComplexCoeff, standardJPartner, standardJSign,
      Fin.ext_iff]
  all_goals congr 1

/-- Contração de uma função com o segundo índice de `J`. -/
theorem sum_mul_standardComplexCoeff_second
    (F : Index8 → ℝ) (i : Index8) :
    ∑ m, F m * standardComplexCoeff i m =
      F (standardJPartner i) * (-standardJSign i) := by
  fin_cases i <;>
    simp only [Fin.sum_univ_succ] <;>
    norm_num [standardComplexCoeff, standardJPartner, standardJSign,
      Fin.ext_iff]
  all_goals congr 1

/-- O sinal da estrutura complexa padrão tem módulo um. -/
theorem standardJSign_sq (i : Index8) :
    standardJSign i ^ 2 = 1 := by
  fin_cases i <;>
    norm_num [standardJSign]

/-- Símbolos de Christoffel da métrica conformal. -/
def conformalLeviCivitaConnection
    (a : ℝ) (k i j : Index8) : ℝ :=
  delta8 k j * conformalPhiGradient a i +
  delta8 k i * conformalPhiGradient a j -
  delta8 i j * conformalPhiGradient a k

/--
Conexão de Bismut do ansatz conformal.

O termo torsional usa literalmente a 3-forma `H=d_J^cω` já construída.
-/
noncomputable def conformalBismutConnectionCoeff
    (a : ℝ) (x : LocalPoint) (k i j : Index8) : ℝ :=
  conformalLeviCivitaConnection a k i j +
  (conformalBismutTorsion a).value x i j k /
    (2 * conformalScale a x)

/-- Derivada de escala fatorada pela própria escala. -/
theorem conformalScaleDerivative_factor
    (a : ℝ) (x : LocalPoint) (i : Index8) :
    conformalScaleDerivative a x i =
      conformalScale a x *
        (if i = 0 then 2 * a else 0) := by
  by_cases hi : i = 0
  · simp [conformalScaleDerivative, hi]
    ring
  · simp [conformalScaleDerivative, hi]

/-- Parte de `dω` depois de retirar o fator conformal positivo. -/
def conformalDOmegaNormalized
    (a : ℝ) (i j k : Index8) : ℝ :=
  (if i = 0 then 2 * a else 0) * standardFundamentalForm j k +
  (if j = 0 then 2 * a else 0) * standardFundamentalForm k i +
  (if k = 0 then 2 * a else 0) * standardFundamentalForm i j

/-- Parte de `H=d_J^cω` independente da posição após elevar um índice. -/
def conformalTorsionNormalized
    (a : ℝ) (i j k : Index8) : ℝ :=
  -(standardJSign i * standardJSign j * standardJSign k) *
    conformalDOmegaNormalized a
      (standardJPartner i)
      (standardJPartner j)
      (standardJPartner k)

/-- A 3-forma torsional contém exatamente um fator `e^{2φ}`. -/
theorem conformalBismutTorsion_factor
    (a : ℝ) (x : LocalPoint) (i j k : Index8) :
    (conformalBismutTorsion a).value x i j k =
      conformalScale a x * conformalTorsionNormalized a i j k := by
  change conformalDJcOmega a x i j k =
    conformalScale a x * conformalTorsionNormalized a i j k
  unfold conformalDJcOmega conformalDOmega
    conformalTorsionNormalized conformalDOmegaNormalized
  rw [conformalScaleDerivative_factor,
    conformalScaleDerivative_factor,
    conformalScaleDerivative_factor]
  ring

/-- Forma constante dos coeficientes de Bismut no ansatz linear. -/
noncomputable def conformalBismutConnectionConstant
    (a : ℝ) (k i j : Index8) : ℝ :=
  conformalLeviCivitaConnection a k i j +
    conformalTorsionNormalized a i j k / 2

/--
Os coeficientes da conexão são independentes da posição porque o fator
`e^{2φ}` de `H` cancela exatamente contra `g⁻¹`.
-/
theorem conformalBismutConnection_eq_constant
    (a : ℝ) (x : LocalPoint) (k i j : Index8) :
    conformalBismutConnectionCoeff a x k i j =
      conformalBismutConnectionConstant a k i j := by
  rw [conformalBismutConnectionCoeff,
    conformalBismutConnectionConstant,
    conformalBismutTorsion_factor]
  have hs : conformalScale a x ≠ 0 :=
    ne_of_gt (conformalScale_pos a x)
  field_simp

/-- A métrica real conformal é simétrica. -/
theorem conformalRealMetric_symmetric
    (a : ℝ) (x : LocalPoint) (i j : Index8) :
    conformalRealMetric a x i j =
      conformalRealMetric a x j i := by
  simp [conformalRealMetric, delta8_symmetric]

/-- A métrica e sua inversa satisfazem a lei matricial pontual. -/
theorem conformalRealInverse_law
    (a : ℝ) (x : LocalPoint) (i j : Index8) :
    ∑ k,
      conformalRealInverseMetric a x i k *
        conformalRealMetric a x k j =
      if i = j then 1 else 0 := by
  have hs : conformalScale a x ≠ 0 :=
    ne_of_gt (conformalScale_pos a x)
  classical
  simp [conformalRealInverseMetric, conformalRealMetric, delta8, hs]

/-- A métrica real conformal é definida positiva. -/
theorem conformalRealMetric_positive
    (a : ℝ) (x : LocalPoint) (v : Index8 → ℝ) (hv : v ≠ 0) :
    0 <
      ∑ i, ∑ j,
        v i * conformalRealMetric a x i j * v j := by
  have hs : 0 < conformalScale a x := conformalScale_pos a x
  have hvsum : 0 < ∑ i, (v i) ^ 2 := by
    rw [Finset.sum_pos_iff_of_nonneg]
    · rcases Function.ne_iff.mp hv with ⟨i, hi⟩
      exact ⟨i, Finset.mem_univ i, sq_pos_of_ne_zero hi⟩
    · intro i hi
      exact sq_nonneg (v i)
  have hform :
      (∑ i, ∑ j,
        v i * conformalRealMetric a x i j * v j) =
        conformalScale a x * ∑ i, (v i) ^ 2 := by
    simp only [conformalRealMetric, delta8]
    simp
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro i hi
    ring
  rw [hform]
  exact mul_pos hs hvsum

/-- A matriz métrica é a matriz diagonal com entrada `e^{2φ}`. -/
theorem conformalRealMetric_eq_diagonal
    (a : ℝ) (x : LocalPoint) :
    (fun i j ↦ conformalRealMetric a x i j) =
      Matrix.diagonal (fun _ : Index8 ↦ conformalScale a x) := by
  ext i j
  by_cases h : i = j
  · subst j
    simp [conformalRealMetric, delta8]
  · simp [conformalRealMetric, delta8, h]

/-- Determinante explícito da métrica conformal em dimensão real oito. -/
theorem conformalRealMetric_det
    (a : ℝ) (x : LocalPoint) :
    Matrix.det (fun i j ↦ conformalRealMetric a x i j) =
      (conformalScale a x) ^ 8 := by
  rw [conformalRealMetric_eq_diagonal, Matrix.det_diagonal]
  simp

/-- O determinante da métrica conformal é positivo. -/
theorem conformalRealMetric_det_pos
    (a : ℝ) (x : LocalPoint) :
    0 < Matrix.det (fun i j ↦ conformalRealMetric a x i j) := by
  rw [conformalRealMetric_det]
  exact pow_pos (conformalScale_pos a x) 8

/-- A estrutura complexa padrão satisfaz `J²=-1` em componentes. -/
theorem standardComplexCoeff_square_neg
    (i j : Index8) :
    ∑ k, standardComplexCoeff i k * standardComplexCoeff k j =
      if i = j then -1 else 0 := by
  rw [sum_mul_standardComplexCoeff_first
    (fun k ↦ standardComplexCoeff i k) j]
  by_cases hij : i = j
  · subst j
    rw [show
        standardComplexCoeff i (standardJPartner i) =
          -standardJSign i by
        simp [standardComplexCoeff]]
    rw [if_pos rfl]
    calc
      -standardJSign i * standardJSign i =
          -(standardJSign i ^ 2) := by ring
      _ = -1 := by rw [standardJSign_sq]
  · have hpartner :
        standardJPartner j ≠ standardJPartner i := by
      intro h
      have hp := congrArg standardJPartner h
      have : j = i := by
        simpa [standardJPartner_involution] using hp
      exact hij this.symm
    simp [standardComplexCoeff, hpartner, hij]

/--
A conexão construída tem exatamente a torção prescrita `H`.

Este é o primeiro elo diferencial que exclui o controle `H=0` do setor
material.
-/
theorem conformalBismutConnection_torsion
    (a : ℝ) (x : LocalPoint) (i j k : Index8) :
    (∑ m,
      conformalRealMetric a x k m *
        (conformalBismutConnectionCoeff a x m i j -
          conformalBismutConnectionCoeff a x m j i)) =
      (conformalBismutTorsion a).value x i j k := by
  have hs : conformalScale a x ≠ 0 :=
    ne_of_gt (conformalScale_pos a x)
  classical
  simp only [conformalRealMetric]
  simp only [delta8]
  simp
  rw [conformalBismutConnectionCoeff,
    conformalBismutConnectionCoeff]
  have hLC :
      conformalLeviCivitaConnection a k i j =
        conformalLeviCivitaConnection a k j i := by
    simp [conformalLeviCivitaConnection, delta8_symmetric]
    ring
  have hH :
      (conformalBismutTorsion a).value x j i k =
        -(conformalBismutTorsion a).value x i j k :=
    (conformalBismutTorsion a).swap₁₂ x j i k
  rw [hLC, hH]
  field_simp
  ring

/-- A conexão de Bismut é compatível com a métrica conformal. -/
theorem conformalBismutConnection_metricCompatible
    (a : ℝ) (x : LocalPoint) (p i j : Index8) :
    conformalRealMetricDerivative a x p i j -
      (∑ m,
        conformalBismutConnectionCoeff a x m p i *
          conformalRealMetric a x m j) -
      (∑ m,
        conformalBismutConnectionCoeff a x m p j *
          conformalRealMetric a x i m) = 0 := by
  have hs : conformalScale a x ≠ 0 :=
    ne_of_gt (conformalScale_pos a x)
  classical
  simp only [conformalRealMetric]
  simp only [delta8]
  simp
  rw [conformalBismutConnectionCoeff,
    conformalBismutConnectionCoeff]
  have hH :
      (conformalBismutTorsion a).value x p j i =
        -(conformalBismutTorsion a).value x p i j :=
    (conformalBismutTorsion a).swap₂₃ x p j i
  rw [hH]
  have hder :
      conformalScaleDerivative a x p =
        2 * conformalScale a x * conformalPhiGradient a p := by
    fin_cases p <;>
      simp [conformalScaleDerivative, conformalPhiGradient] <;>
      ring
  rw [conformalRealMetricDerivative, hder]
  simp only [conformalLeviCivitaConnection]
  rw [delta8_symmetric j i, delta8_symmetric j p,
    delta8_symmetric i p]
  field_simp
  ring

set_option maxHeartbeats 1000000

/--
A estrutura complexa é paralela para a conexão torsional construída.

Como `J` é constante nas coordenadas escolhidas, a parcela de derivada é zero.
-/
theorem conformalBismutConnection_complexCompatible
    (a : ℝ) (x : LocalPoint) (p i j : Index8) :
    (∑ m,
        conformalBismutConnectionCoeff a x i p m *
          standardComplexCoeff m j) -
      (∑ m,
        conformalBismutConnectionCoeff a x m p j *
          standardComplexCoeff i m) = 0 := by
  have hs : conformalScale a x ≠ 0 :=
    ne_of_gt (conformalScale_pos a x)
  rw [sum_mul_standardComplexCoeff_first
    (fun m ↦ conformalBismutConnectionCoeff a x i p m) j]
  rw [sum_mul_standardComplexCoeff_second
    (fun m ↦ conformalBismutConnectionCoeff a x m p j) i]
  fin_cases p <;> fin_cases i <;> fin_cases j <;>
    norm_num [conformalBismutConnectionCoeff,
      conformalLeviCivitaConnection, conformalPhiGradient, delta8,
      conformalBismutTorsion, conformalDJcOmega, conformalDOmega,
      conformalScaleDerivative, standardFundamentalForm, standardJPartner,
      standardJSign, Fin.ext_iff, hs] <;>
    field_simp <;>
    ring

set_option maxHeartbeats 200000

end GDQ
