import Mathlib

/-!
# GDQ.BaryonicReduction

Certificados algébricos do modelo bariônico reduzido usado no Capítulo 17.

Este módulo não afirma que a ação oficial seleciona o background de três
estômatos, nem deriva os coeficientes de superfície. Ele prova apenas as
consequências exatas das hipóteses geométricas declaradas no modelo reduzido:

* aditividade das três câmaras;
* equilíbrio da orientação torsional `(1, 1, -2)`;
* invariante quadrático de cisalhamento;
* relações algébricas entre as massas reduzidas;
* identidade de Cauchy--Schwarz usada na norma beta;
* eliminação de Schur de um modo transversal quártico.
-/

namespace GDQ

noncomputable section

def baryonicBulk : ℝ :=
  6 * Real.pi ^ 5

def protonSurface (α : ℝ) : ℝ :=
  α * (3 * Real.pi / 2 + 3 / (4 * Real.pi ^ 3))

def reducedProtonRatio (α : ℝ) : ℝ :=
  baryonicBulk + protonSurface α

def reducedNeutronExcess : ℝ :=
  Real.log (2 * Real.pi ^ 2) * (3 * Real.sqrt 2 / 5)

def reducedNeutronRatio (α : ℝ) : ℝ :=
  reducedProtonRatio α + reducedNeutronExcess

/-- Três câmaras de volume `2 π⁵` somam o volume reduzido `6 π⁵`. -/
theorem three_chambers_volume :
    3 * (2 * Real.pi ^ 5) = baryonicBulk := by
  unfold baryonicBulk
  ring

/-- A orientação reduzida do nêutron conserva a soma torsional. -/
theorem neutron_torsional_balance :
    (1 : ℝ) + 1 - 2 = 0 := by
  norm_num

/-- O cisalhamento par a par de `(1,1,-2)` tem quadrado igual a `18`. -/
theorem neutron_pairwise_shear_sq :
    ((1 : ℝ) - 1) ^ 2 + (1 - (-2)) ^ 2 + (1 - (-2)) ^ 2 = 18 := by
  norm_num

/-- O triângulo dimensional usado na projeção reduzida é exatamente 3--4--5. -/
theorem three_four_five_identity :
    (3 : ℝ) ^ 2 + 4 ^ 2 = 5 ^ 2 := by
  norm_num

/-- A diferença reduzida nêutron--próton é, por definição do modelo, `δ_B`. -/
theorem reduced_neutron_minus_proton (α : ℝ) :
    reducedNeutronRatio α - reducedProtonRatio α = reducedNeutronExcess := by
  unfold reducedNeutronRatio
  ring

/-- Forma equivalente do termo de superfície protônico. -/
theorem protonSurface_expanded (α : ℝ) :
    protonSurface α =
      α * (3 * Real.pi / 2) + α * (3 / (4 * Real.pi ^ 3)) := by
  unfold protonSurface
  ring

/-- A norma não polarizada é não negativa. -/
theorem betaContractedNorm_nonneg (cS cT : ℂ) :
    0 ≤ 2 * ‖cS‖ ^ 2 + 6 * ‖cT‖ ^ 2 := by
  positivity

/--
Eliminação algébrica de um modo transversal:

`(K/2) ξ² + (G/2) ξ q² + (V₄/24) q⁴`

avaliado em `ξ = -G q²/(2K)` produz o coeficiente quártico efetivo
`V₄ - 3G²/K`.
-/
theorem quarticSchurElimination
    (K G V₄ q : ℝ) (hK : K ≠ 0) :
    K / 2 * (-G * q ^ 2 / (2 * K)) ^ 2
        + G / 2 * (-G * q ^ 2 / (2 * K)) * q ^ 2
        + V₄ / 24 * q ^ 4
      =
    (V₄ - 3 * G ^ 2 / K) / 24 * q ^ 4 := by
  field_simp [hK]
  ring

/--
A fórmula de vida média abaixo é uma identidade algébrica somente depois de
assumida a lei reduzida `τ = (32/15) αinv¹¹ ℏ / m`.
-/
theorem reducedLifetime_inverse
    (αinv ℏ m : ℝ) (hα : αinv ≠ 0) (hℏ : ℏ ≠ 0) (hm : m ≠ 0) :
    ((32 / 15 : ℝ) * αinv ^ 11 * ℏ / m) *
        ((15 / 32 : ℝ) * m / (αinv ^ 11 * ℏ)) = 1 := by
  field_simp [hα, hℏ, hm]

end

end GDQ
