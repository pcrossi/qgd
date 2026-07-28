import GDQ.FlowKernel

namespace GDQ

/-!
# Admissibilidade geométrica

Este arquivo separa os campos brutos das configurações que podem entrar na
ação. Os quatro campos proposicionais de `BismutWitness` são obrigações de
prova. Eles não são declarados automaticamente verdadeiros.
-/

/-- Conexão real abstrata no modelo local. -/
abbrev ConnectionData :=
  LocalPoint → LocalTangent → LocalTangent → LocalTangent

/--
Testemunho das propriedades geométricas exigidas da conexão de Bismut.

As proposições serão refinadas para equações tensoriais quando a estrutura
suave completa for introduzida.
-/
structure BismutWitness (Φ : GDQFieldConfiguration) where
  connection : ConnectionData
  complexIntegrable : Prop
  metricCompatible : Prop
  complexCompatible : Prop
  torsionMatchesH : Prop
  complexIntegrable_proof : complexIntegrable
  metricCompatible_proof : metricCompatible
  complexCompatible_proof : complexCompatible
  torsionMatchesH_proof : torsionMatchesH

/--
Configuração admissível no estágio atual.

Além do testemunho de Bismut, o kernel deve coincidir exatamente com a
definição constitutiva oficial em dimensão complexa quatro.
-/
structure AdmissibleConfiguration extends GDQFieldConfiguration where
  bismut : BismutWitness toGDQFieldConfiguration
  kernel_law :
    ∀ q x,
      kernel q x =
        officialFlowKernel 4 (toGDQFieldConfiguration.rho x) q.zτ

/-- A configuração possui torção material não trivial em algum ponto. -/
def AdmissibleConfiguration.HasNonzeroTorsion
    (Φ : AdmissibleConfiguration) : Prop :=
  ∃ x i j k, Φ.torsion.value x i j k ≠ 0

/--
Configuração admissível do setor material da GDQ.

A não anulação da torção é uma obrigação de prova e impede que um background
Kähler plano seja usado silenciosamente como background de matéria. A
identidade diferencial completa `H=d_J^cω` continua sendo verificada pela
camada coordenada/suave de Bismut.
-/
structure MaterialAdmissibleConfiguration
    extends AdmissibleConfiguration where
  torsion_nonzero : toAdmissibleConfiguration.HasNonzeroTorsion

/-- Regularidade pontual de uma configuração admissível. -/
def AdmissibleConfiguration.RegularAt
    (Φ : AdmissibleConfiguration) (x : LocalPoint) : Prop :=
  Φ.toGDQFieldConfiguration.RegularAt x

/-- No locus regular, o numerador complexo não se anula. -/
theorem AdmissibleConfiguration.rho_cast_ne_zero_of_regular
    (Φ : AdmissibleConfiguration) (x : LocalPoint)
    (hx : Φ.RegularAt x) :
    ((Φ.toGDQFieldConfiguration.rho x : ℝ) : ℂ) ≠ 0 := by
  exact_mod_cast ne_of_gt hx

/-- O kernel não se anula no locus regular. -/
theorem AdmissibleConfiguration.kernel_ne_zero_of_regular
    (Φ : AdmissibleConfiguration) (q : FlowPoint) (x : LocalPoint)
    (hx : Φ.RegularAt x) :
    Φ.kernel q x ≠ 0 := by
  rw [Φ.kernel_law q x]
  apply div_ne_zero
  · exact Φ.rho_cast_ne_zero_of_regular x hx
  · exact officialFlowKernel_denominator_ne_zero 4 q.zτ q.zτ_ne_zero

/-- Em um nó `ρ = 0`, a lei constitutiva força o kernel a se anular. -/
theorem AdmissibleConfiguration.kernel_eq_zero_of_not_regular
    (Φ : AdmissibleConfiguration) (q : FlowPoint) (x : LocalPoint)
    (hx : ¬ Φ.RegularAt x) :
    Φ.kernel q x = 0 := by
  rw [Φ.kernel_law q x]
  have hρ :
      Φ.toGDQFieldConfiguration.rho x = 0 :=
    Φ.toGDQFieldConfiguration.rho_eq_zero_of_not_regular x hx
  rw [hρ]
  norm_num [officialFlowKernel]

end GDQ
