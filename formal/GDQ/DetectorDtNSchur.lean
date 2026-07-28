import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp
import Mathlib.Tactic

namespace GDQ

/-!
# Impedância DtN, energia de Schur e visibilidade

O detector reduzido ocupa `s ∈ [0,L]` e obedece
`(-∂ₛ² + λ²)φ = 0`, com `φ(0)=φ₀` e `φ(L)=0`.
O perfil explícito permite calcular o mapa Dirichlet--to--Neumann.
-/

/-- Cotangente hiperbólica escrita sem introduzir uma nova função primitiva. -/
noncomputable def coth (x : ℝ) : ℝ :=
  Real.cosh x / Real.sinh x

/-- Perfil estacionário do detector com dados de Dirichlet nas extremidades. -/
noncomputable def detectorProfile (lam L φ₀ s : ℝ) : ℝ :=
  φ₀ * Real.sinh (lam * (L - s)) / Real.sinh (lam * L)

/-- Impedância Dirichlet--to--Neumann do canal linear. -/
noncomputable def detectorDtN (lam L : ℝ) : ℝ :=
  lam * coth (lam * L)

/-- O perfil assume o valor prescrito na interface esquerda. -/
theorem detectorProfile_at_zero
    {lam L φ₀ : ℝ} (hlamL : Real.sinh (lam * L) ≠ 0) :
    detectorProfile lam L φ₀ 0 = φ₀ := by
  simp [detectorProfile, hlamL]

/-- O perfil se anula na extremidade direita. -/
theorem detectorProfile_at_length (lam L φ₀ : ℝ) :
    detectorProfile lam L φ₀ L = 0 := by
  simp [detectorProfile]

/--
O fluxo normal de saída na interface é a impedância DtN multiplicada pelo
dado de Dirichlet.
-/
theorem detectorProfile_outwardDerivative_at_zero
    {lam L φ₀ : ℝ} (hlamL : Real.sinh (lam * L) ≠ 0) :
    HasDerivAt (fun s => -detectorProfile lam L φ₀ s)
      (detectorDtN lam L * φ₀) 0 := by
  have hinner :
      HasDerivAt (fun s : ℝ => lam * (L - s)) (-lam) 0 := by
    simpa [id_eq] using
      ((hasDerivAt_const (x := (0 : ℝ)) L).sub
        (hasDerivAt_id (𝕜 := ℝ) 0)).const_mul lam
  have hsinh :
      HasDerivAt (fun s : ℝ => Real.sinh (lam * (L - s)))
        (Real.cosh (lam * L) * (-lam)) 0 := by
    change HasDerivAt
      (Real.sinh ∘ fun s : ℝ => lam * (L - s))
      (Real.cosh (lam * L) * (-lam)) 0
    simpa only [sub_zero] using
      (Real.hasDerivAt_sinh (lam * (L - 0))).comp 0 hinner
  have hprofile :
      HasDerivAt (detectorProfile lam L φ₀)
        (φ₀ * (Real.cosh (lam * L) * (-lam)) / Real.sinh (lam * L)) 0 := by
    unfold detectorProfile
    exact (hsinh.const_mul φ₀).div_const (Real.sinh (lam * L))
  have hcoeff :
      -(φ₀ * (Real.cosh (lam * L) * (-lam)) / Real.sinh (lam * L)) =
        detectorDtN lam L * φ₀ := by
    unfold detectorDtN coth
    field_simp
  rw [← hcoeff]
  exact hprofile.neg

/-- Para `λ,L>0`, a impedância do detector é estritamente positiva. -/
theorem detectorDtN_pos {lam L : ℝ} (hlam : 0 < lam) (hL : 0 < L) :
    0 < detectorDtN lam L := by
  unfold detectorDtN coth
  have hs : 0 < Real.sinh (lam * L) :=
    (Real.sinh_pos_iff).2 (mul_pos hlam hL)
  positivity

/-- Expoente de decoerência quadrático induzido pela interface. -/
noncomputable def detectorDecoherence
    (lam L ζ Cpath : ℝ) : ℝ :=
  (1 / 2 : ℝ) * ζ ^ 2 * Cpath * detectorDtN lam L

/-- O expoente de decoerência é não negativo nos dados físicos. -/
theorem detectorDecoherence_nonneg
    {lam L ζ Cpath : ℝ}
    (hlam : 0 < lam) (hL : 0 < L) (hC : 0 ≤ Cpath) :
    0 ≤ detectorDecoherence lam L ζ Cpath := by
  unfold detectorDecoherence
  have hR : 0 ≤ detectorDtN lam L := (detectorDtN_pos hlam hL).le
  positivity

/-- A visibilidade/coerência reduzida pertence a `(0,1]`. -/
theorem detectorVisibility_mem
    {lam L ζ Cpath : ℝ}
    (hlam : 0 < lam) (hL : 0 < L) (hC : 0 ≤ Cpath) :
    0 < Real.exp (-detectorDecoherence lam L ζ Cpath) ∧
      Real.exp (-detectorDecoherence lam L ζ Cpath) ≤ 1 := by
  constructor
  · exact Real.exp_pos _
  · rw [Real.exp_le_one_iff]
    exact neg_nonpos.mpr (detectorDecoherence_nonneg hlam hL hC)

end GDQ
