import Mathlib.Analysis.InnerProductSpace.Completion
import Mathlib.Analysis.Normed.Group.NullSubmodule

namespace GDQ

/-!
# Reconstrução Osterwalder--Schrader setorial

Este módulo formaliza o núcleo funcional da reconstrução depois que um setor
euclidiano concreto da GDQ forneceu uma forma de Osterwalder--Schrader.

A hipótese analítica central é visível no tipo: o pareamento refletido já deve
definir uma estrutura de produto interno possivelmente semidefinida no domínio
positivo. Lean então certifica:

* positividade por reflexão;
* remoção dos vetores de seminorma nula;
* remoção simultânea de gauge quando o gauge é nulo para a forma OS;
* produto interno bem definido no quociente;
* completamento em um espaço de Hilbert complexo.

O módulo não afirma que todo background GDQ satisfaz positividade por
reflexão. Essa verificação continua sendo uma obrigação do setor concreto.
-/

variable
  {D : Type*}
  [SeminormedAddCommGroup D]
  [InnerProductSpace ℂ D]

/--
Dados de um setor euclidiano positivo.

`D` já carrega a seminorma e o produto interno induzidos pela forma OS.
O campo `reflectionPairing_eq_inner` registra que essa estrutura é exatamente
o pareamento euclidiano refletido, e não um produto interno independente.
-/
structure ReflectionPositiveSector (D : Type*)
    [SeminormedAddCommGroup D]
    [InnerProductSpace ℂ D] where
  reflection : D → D
  euclideanPairing : D → D → ℂ
  reflectionPairing_eq_inner :
    ∀ F G, euclideanPairing (reflection F) G = inner ℂ F G
  gauge : Submodule ℂ D
  gauge_is_null : gauge ≤ nullSubmodule ℂ D

/-- Subespaço de vetores de norma OS nula. -/
noncomputable def ReflectionPositiveSector.nullSpace
    (_S : ReflectionPositiveSector D) : Submodule ℂ D :=
  nullSubmodule ℂ D

/--
Quando todas as redundâncias de gauge são nulas para a forma OS,
`N + G = N`; não é necessário impor um segundo quociente incompatível.
-/
theorem ReflectionPositiveSector.nullSpace_sup_gauge
    (S : ReflectionPositiveSector D) :
    S.nullSpace ⊔ S.gauge = S.nullSpace := by
  exact sup_eq_left.mpr S.gauge_is_null

/-- A hipótese de representação pela forma interna implica reflexão positiva. -/
theorem ReflectionPositiveSector.reflectionPositive
    (S : ReflectionPositiveSector D) (F : D) :
    0 ≤ (S.euclideanPairing (S.reflection F) F).re := by
  rw [S.reflectionPairing_eq_inner]
  exact inner_self_nonneg (𝕜 := ℂ)

/-- Pré-Hilbert separado, obtido pelo quociente dos vetores nulos. -/
abbrev ReflectionPositiveSector.Separated
    (_S : ReflectionPositiveSector D) :=
  SeparationQuotient D

/-- Hilbert físico: completamento do quociente separado. -/
abbrev ReflectionPositiveSector.Hilbert
    (S : ReflectionPositiveSector D) :=
  UniformSpace.Completion S.Separated

/-- Classe de um funcional positivo no quociente separado. -/
noncomputable def ReflectionPositiveSector.separatedState
    (S : ReflectionPositiveSector D) (F : D) : S.Separated :=
  SeparationQuotient.mk F

/-- Imersão canônica de um funcional positivo no Hilbert reconstruído. -/
noncomputable def ReflectionPositiveSector.physicalState
    (S : ReflectionPositiveSector D) (F : D) : S.Hilbert :=
  (S.separatedState F : S.Hilbert)

/-- O produto interno reconstruído coincide com o pareamento refletido. -/
theorem ReflectionPositiveSector.inner_physicalState
    (S : ReflectionPositiveSector D) (F G : D) :
    inner ℂ (S.physicalState F) (S.physicalState G) =
      S.euclideanPairing (S.reflection F) G := by
  rw [S.reflectionPairing_eq_inner]
  simp [ReflectionPositiveSector.physicalState,
    ReflectionPositiveSector.separatedState]

/-- A norma do estado reconstruído é exatamente a seminorma OS original. -/
theorem ReflectionPositiveSector.norm_physicalState
    (S : ReflectionPositiveSector D) (F : D) :
    ‖S.physicalState F‖ = ‖F‖ := by
  simp [ReflectionPositiveSector.physicalState,
    ReflectionPositiveSector.separatedState]

/-- Um funcional nulo representa o vetor zero no Hilbert reconstruído. -/
theorem ReflectionPositiveSector.physicalState_eq_zero_of_null
    (S : ReflectionPositiveSector D) (F : D)
    (hF : F ∈ S.nullSpace) :
    S.physicalState F = 0 := by
  rw [← norm_eq_zero]
  rw [S.norm_physicalState]
  exact hF

/--
Redundâncias de gauge nulas para o pareamento OS desaparecem no mesmo
quociente físico.
-/
theorem ReflectionPositiveSector.physicalState_eq_zero_of_gauge
    (S : ReflectionPositiveSector D) (F : D)
    (hF : F ∈ S.gauge) :
    S.physicalState F = 0 :=
  S.physicalState_eq_zero_of_null F (S.gauge_is_null hF)

/--
Dois representantes que diferem por uma direção nula fornecem o mesmo estado
físico.
-/
theorem ReflectionPositiveSector.physicalState_eq_of_sub_null
    (S : ReflectionPositiveSector D) (F G : D)
    (hFG : F - G ∈ S.nullSpace) :
    S.physicalState F = S.physicalState G := by
  have hinsep : Inseparable F G := by
    rw [Metric.inseparable_iff, dist_eq_norm]
    exact hFG
  have hquot :
      (SeparationQuotient.mk F : S.Separated) =
        SeparationQuotient.mk G :=
    SeparationQuotient.mk_eq_mk.mpr hinsep
  exact congrArg
    (fun x : S.Separated => (x : S.Hilbert)) hquot

/-- Os estados provenientes do domínio positivo são densos no completamento. -/
theorem ReflectionPositiveSector.physicalState_denseRange
    (S : ReflectionPositiveSector D) :
    DenseRange S.physicalState := by
  have hmk :
      Function.Surjective
        (fun F : D => (SeparationQuotient.mk F : S.Separated)) :=
    SeparationQuotient.surjective_mk
  change DenseRange
    ((fun x : S.Separated => (x : S.Hilbert)) ∘
      (fun F : D => SeparationQuotient.mk F))
  simpa using
    (UniformSpace.Completion.denseRange_coe.comp
      hmk.denseRange
      (UniformSpace.Completion.continuous_coe S.Separated))

/-- O completamento reconstruído possui a estrutura complexa de Hilbert. -/
noncomputable example (S : ReflectionPositiveSector D) :
    InnerProductSpace ℂ S.Hilbert := by infer_instance

/-- O completamento reconstruído é completo. -/
example (S : ReflectionPositiveSector D) :
    CompleteSpace S.Hilbert := by infer_instance

end GDQ
