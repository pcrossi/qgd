---
title: "Nota — Formalização Lean da FAQ técnica"
---

# Nota — Formalização Lean da FAQ técnica

O módulo [`TechnicalFAQ.lean`](../../../formal/GDQ/TechnicalFAQ.lean)
certifica distinções lógicas usadas neste capítulo. Ele importa a taxonomia do
estado lógico e o protocolo numérico, mas não cria dinâmica física nova.

## 1. Resultado condicional

`ConditionalResult H R` é definido como $H\Rightarrow R$. O teorema
`conditionalResult_apply` somente entrega $R$ depois de receber uma prova de
$H$. Assim, uma hipótese declarada não desaparece quando o resultado é
reutilizado.

## 2. Concordância numérica

O teorema
`numericalAgreement_does_not_close_missing_background` mostra que uma
concordância numérica, mesmo aceita como proposição, não completa a cadeia
forte se falta um background admissível.

## 3. Emaranhamento

Para um mapa de composição declarado, o predicado `EntangledState` é a
negação da fatoração do estado:

$$
\Psi_{AB}\ne\Psi_A\otimes\Psi_B.
$$

Lean certifica essa equivalência sem afirmar que o espaço de Hilbert composto
deixe de admitir produto tensorial.

## 4. Born e evento

`MeasurementStatus` separa:

- probabilidades operacionais;
- dinâmica do evento individual.

O fechamento da dinâmica completa implica Born operacional, mas a ausência de
dinâmica do evento impede declarar a teoria integral da medida fechada.

## 5. Perelman setorial

`ProductSectorConditions` exige simultaneamente:

1. fator plano Ricci-nulo;
2. dilatão constante nesse fator;
3. ausência de torção mista;
4. métrica produto.

Os teoremas de no-go mostram que torção mista ou métrica não produto impedem
usar automaticamente a redução setorial.

## 6. Alcance

O módulo certifica coerência da classificação. As provas físicas permanecem
nos módulos dos capítulos correspondentes: ação, projetor, Perelman produto,
Born, aparelhos, Yang--Mills efetivo e protocolo numérico.
