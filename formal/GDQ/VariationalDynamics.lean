import GDQ.PhysicalProjector

namespace GDQ

/-!
# Dinâmica variacional, linearização e redução física

Este módulo liga três níveis que devem permanecer conceitualmente distintos:

1. a equação variacional da ação oficial, antes de qualquer projeção;
2. a linearização dessa equação num background estacionário;
3. a compressão da linearização ao espaço tangente físico.

A Hessiana e o projetor não são novas leis fundamentais. A Hessiana é a
derivada da equação de Euler--Lagrange representada pelo gradiente, enquanto
o projetor apenas restringe essa linearização às variações admissíveis e
ortogonais ao gauge.
-/

variable
  {E : Type*}
  [NormedAddCommGroup E]
  [InnerProductSpace ℝ E]

/-- A equação variacional não projetada é representada pelo gradiente da ação. -/
noncomputable def PhysicalHessianData.eulerLagrangeMap
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) : E → E :=
  H.gradient

/-- A primeira variação é o pareamento com a equação de Euler--Lagrange. -/
theorem PhysicalHessianData.firstVariation_eq_eulerLagrange_pairing
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) (u v : E) :
    fderiv ℝ F.action u v =
      inner ℝ (H.eulerLagrangeMap u) v := by
  exact H.gradient_represents_first_variation u v

/--
Estacionariedade sem vínculos: a primeira variação se anula para toda
direção do espaço de configurações.
-/
def PhysicalHessianData.IsUnconstrainedStationary
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) : Prop :=
  ∀ v, fderiv ℝ F.action H.background v = 0

/--
No espaço de Hilbert real, a equação variacional não projetada equivale ao
anulamento do gradiente da ação.
-/
theorem PhysicalHessianData.unconstrainedStationary_iff_eulerLagrange_zero
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) :
    H.IsUnconstrainedStationary ↔
      H.eulerLagrangeMap H.background = 0 := by
  constructor
  · intro hstationary
    apply (inner_self_eq_zero (𝕜 := ℝ)).mp
    rw [← H.firstVariation_eq_eulerLagrange_pairing
      H.background (H.eulerLagrangeMap H.background)]
    exact hstationary (H.eulerLagrangeMap H.background)
  · intro hzero v
    rw [H.firstVariation_eq_eulerLagrange_pairing, hzero]
    simp

/--
Estacionariedade física: a primeira variação se anula em toda direção fixada
pelo projetor físico. Esta é a forma tangente dos vínculos e do quociente de
gauge; ela não altera o funcional variado.
-/
def PhysicalHessianData.IsPhysicallyStationary
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) : Prop :=
  ∀ v, H.projector v = v →
    fderiv ℝ F.action H.background v = 0

/--
A equação variacional restrita ao setor físico equivale ao anulamento da
componente física do gradiente.
-/
theorem PhysicalHessianData.physicallyStationary_iff_projectedGradient_zero
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) :
    H.IsPhysicallyStationary ↔
      H.projector (H.eulerLagrangeMap H.background) = 0 := by
  constructor
  · intro hstationary
    let w := H.projector (H.eulerLagrangeMap H.background)
    have hw : H.projector w = w := by
      exact H.projector_idempotent _
    have hpair :
        inner ℝ (H.eulerLagrangeMap H.background) w = 0 := by
      rw [← H.firstVariation_eq_eulerLagrange_pairing H.background w]
      exact hstationary w hw
    apply (inner_self_eq_zero (𝕜 := ℝ)).mp
    calc
      inner ℝ w w =
          inner ℝ (H.eulerLagrangeMap H.background) (H.projector w) := by
            change
              inner ℝ
                  (H.projector (H.eulerLagrangeMap H.background)) w =
                inner ℝ
                  (H.eulerLagrangeMap H.background) (H.projector w)
            exact H.projector_selfAdjoint
              (H.eulerLagrangeMap H.background) w
      _ = inner ℝ (H.eulerLagrangeMap H.background) w := by rw [hw]
      _ = 0 := hpair
  · intro hzero v hv
    rw [H.firstVariation_eq_eulerLagrange_pairing, ← hv]
    rw [← H.projector_selfAdjoint, hzero]
    simp

/--
A Hessiana é literalmente a derivada de Fréchet da equação variacional no
background. Portanto a dinâmica linearizada não é um postulado adicional.
-/
theorem PhysicalHessianData.eulerLagrange_linearizes_to_hessian
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) :
    HasFDerivAt H.eulerLagrangeMap H.hessian H.background := by
  exact H.hessian_is_gradient_derivative

/--
Operador linearizado restrito: primeiro restringe a entrada à direção física,
aplica a Hessiana derivada da ação e então retém a componente física da
resposta.
-/
noncomputable def PhysicalHessianData.restrictedLinearization
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) : E →L[ℝ] E :=
  H.projector.comp (H.hessian.comp H.projector)

/--
A linearização restrita coincide por definição demonstrável com a Hessiana
física já usada nos cálculos espectrais.
-/
theorem PhysicalHessianData.restrictedLinearization_eq_physicalHessian
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) :
    H.restrictedLinearization = H.physicalHessian := by
  rfl

/--
Numa direção física, o projetor de entrada é a identidade: a projeção não
cria a dinâmica, apenas remove da resposta a componente não física.
-/
theorem PhysicalHessianData.physicalHessian_apply_of_physical
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) (v : E)
    (hv : H.projector v = v) :
    H.physicalHessian v = H.projector (H.hessian v) := by
  simp [PhysicalHessianData.physicalHessian, hv]

/--
Se a Hessiana bruta preserva o setor físico, sua compressão não modifica a
dinâmica nesse vetor.
-/
theorem PhysicalHessianData.physicalHessian_eq_raw_of_invariant
    {F : OfficialActionVariationFamily E}
    (H : PhysicalHessianData F) (v : E)
    (hv : H.projector v = v)
    (hinvariant : H.projector (H.hessian v) = H.hessian v) :
    H.physicalHessian v = H.hessian v := by
  rw [H.physicalHessian_apply_of_physical v hv, hinvariant]

end GDQ
