import GDQ.Admissibility
import GDQ.CausalContour

namespace GDQ

/-!
# Assinatura da ação oficial

Este arquivo não substitui a ação por outro funcional. Ele registra somente
o seu tipo lógico:

* uma configuração admissível de campos;
* um contorno causal;
* um escalar de saída;
* uma função que associa a ação à configuração e ao contorno.

A integral oficial completa será formalizada após a introdução de variedades,
medidas, regularidade, integrabilidade e diferenciação sob o sinal de
integração.
-/

/--
Dados mínimos de uma ação GDQ.

`Scalar` permanece paramétrico. Posteriormente será especializado ao corpo
adequado, depois que realidade e orientação do contorno forem formalizadas.
-/
structure OfficialActionData (Scalar : Type) where
  action : AdmissibleConfiguration → CausalContour → Scalar

/-- Uma configuração é estacionária quando sua primeira variação se anula. -/
def IsStationary
    {Scalar Variation : Type}
    [OfNat Scalar 0]
    (firstVariation :
      AdmissibleConfiguration → CausalContour → Variation → Scalar)
    (Φ : AdmissibleConfiguration)
    (γ : CausalContour) : Prop :=
  ∀ h, firstVariation Φ γ h = 0

/--
Teste lógico elementar: se a primeira variação se anula para toda variação,
ela se anula para uma variação particular.
-/
theorem stationary_implies_zero_variation
    {Scalar Variation : Type}
    [OfNat Scalar 0]
    (firstVariation :
      AdmissibleConfiguration → CausalContour → Variation → Scalar)
    (Φ : AdmissibleConfiguration)
    (γ : CausalContour)
    (hStationary : IsStationary firstVariation Φ γ)
    (h : Variation) :
    firstVariation Φ γ h = 0 := by
  exact hStationary h

end GDQ
