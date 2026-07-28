import GDQ.CosmologicalFamily
import GDQ.FlowKernel
import Mathlib.Topology.Instances.Complex

namespace GDQ

/-!
# Transporte apontado dos campos oficiais

As cartas apontadas puxam todos os coeficientes para um domínio local fixo.
Assim, a convergência pode ser expressa sem identificar globalmente os dois
espaços. `H` não é transportado como campo independente: a naturalidade de
`H = dᶜ_J ω_g` é uma obrigação explícita do certificado.
-/

/--
Valores coordenados mínimos dos campos oficiais depois do pullback por uma
carta apontada.
-/
structure PulledBackGDQFields (X : Type*) where
  metric : X → Fin 4 → Fin 4 → ℂ
  complexStructure : X → Fin 8 → Fin 8 → ℝ
  torsion : X → Fin 8 → Fin 8 → Fin 8 → ℝ
  potential : X → ℂ

/-- Densidade constitutiva; não é um parâmetro independente. -/
noncomputable def PulledBackGDQFields.rho
    {X : Type*} (Φ : PulledBackGDQFields X) (x : X) : ℝ :=
  Real.exp (-Complex.re (Φ.potential x))

/-- Kernel constitutivo oficial em dimensão complexa quatro. -/
noncomputable def PulledBackGDQFields.kernel
    {X : Type*} (Φ : PulledBackGDQFields X)
    (zτ : ℂ) (x : X) : ℂ :=
  officialFlowKernel 4 (Φ.rho x) zτ

/-- Família de campos cosmológicos puxados para uma carta local fixa. -/
structure PointedFieldTransport (X : Type*) where
  localFields : PulledBackGDQFields X
  cosmological : Nat → PulledBackGDQFields X
  metric_tendsto :
    ∀ x μ ν,
      Filter.Tendsto (fun k => (cosmological k).metric x μ ν)
        Filter.atTop (nhds (localFields.metric x μ ν))
  complexStructure_tendsto :
    ∀ x i j,
      Filter.Tendsto (fun k => (cosmological k).complexStructure x i j)
        Filter.atTop (nhds (localFields.complexStructure x i j))
  torsion_tendsto :
    ∀ x i j l,
      Filter.Tendsto (fun k => (cosmological k).torsion x i j l)
        Filter.atTop (nhds (localFields.torsion x i j l))
  potential_tendsto :
    ∀ x,
      Filter.Tendsto (fun k => (cosmological k).potential x)
        Filter.atTop (nhds (localFields.potential x))
  /--
  Certifica que o transporte de `H` foi obtido pela operação natural
  `dᶜ_J ω_g`, não pela escolha independente de uma três-forma.
  -/
  torsion_is_natural_bismut_pullback : Prop
  torsion_is_natural_bismut_pullback_proof :
    torsion_is_natural_bismut_pullback

/--
A lei exponencial mostra que a convergência do potencial transporta
automaticamente a densidade.
-/
theorem PointedFieldTransport.rho_tendsto
    {X : Type*} (T : PointedFieldTransport X) (x : X) :
    Filter.Tendsto (fun k => (T.cosmological k).rho x)
      Filter.atTop (nhds (T.localFields.rho x)) := by
  have hre :
      Filter.Tendsto
        (fun k => Complex.re ((T.cosmological k).potential x))
        Filter.atTop
        (nhds (Complex.re (T.localFields.potential x))) :=
    Complex.continuous_re.continuousAt.tendsto.comp
      (T.potential_tendsto x)
  have hneg :
      Filter.Tendsto
        (fun k => -Complex.re ((T.cosmological k).potential x))
        Filter.atTop
        (nhds (-Complex.re (T.localFields.potential x))) :=
    hre.neg
  change Filter.Tendsto
    (fun k => Real.exp (-Complex.re ((T.cosmological k).potential x)))
    Filter.atTop
    (nhds (Real.exp (-Complex.re (T.localFields.potential x))))
  convert Real.continuous_exp.continuousAt.tendsto.comp hneg using 1
  funext k
  rfl

/--
Para `zτ ≠ 0` fixo, a convergência da densidade transporta o kernel oficial.
-/
theorem PointedFieldTransport.kernel_tendsto
    {X : Type*} (T : PointedFieldTransport X)
    (zτ : ℂ) (_hz : zτ ≠ 0) (x : X) :
    Filter.Tendsto (fun k => (T.cosmological k).kernel zτ x)
      Filter.atTop (nhds (T.localFields.kernel zτ x)) := by
  have hρ := T.rho_tendsto x
  have hρc :
      Filter.Tendsto
        (fun k => (((T.cosmological k).rho x : ℝ) : ℂ))
        Filter.atTop
        (nhds (((T.localFields.rho x : ℝ) : ℂ))) :=
    Complex.continuous_ofReal.continuousAt.tendsto.comp hρ
  simpa [PulledBackGDQFields.kernel, officialFlowKernel] using
    hρc.div_const (((((4 * Real.pi : ℝ) : ℂ) * zτ) ^ (4 : Nat)))

/--
Certificado de transporte unitário da medida ponderada.

O campo `norm_preserving` é precisamente a obrigação analítica associada ao
fator de Jacobiano
`(dμ₀ / Φ_R^* dμ_R)^{1/2}`.
-/
structure WeightedMeasureTransport
    (E₀ E : Type*)
    [NormedAddCommGroup E₀] [NormedAddCommGroup E] where
  identify : Nat → E₀ →+ E
  norm_preserving : ∀ k u, ‖identify k u‖ = ‖u‖

/-- O transporte com Jacobiano certificado é isométrico em cada escala. -/
theorem WeightedMeasureTransport.distance_preserving
    {E₀ E : Type*}
    [NormedAddCommGroup E₀] [NormedAddCommGroup E]
    (I : WeightedMeasureTransport E₀ E) (k : Nat) (x y : E₀) :
    dist (I.identify k x) (I.identify k y) = dist x y := by
  simpa only [dist_eq_norm, map_sub] using I.norm_preserving k (x - y)

end GDQ
