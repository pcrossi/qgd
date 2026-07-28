---
title: "Provas, lemas e definições — Capítulo 10"
---

# Provas, lemas e definições — Capítulo 10

## 0. Construção GDQ do problema

Status: cadeia estrutural do defeito até CAR/Pauli.

Nota:

[[construcao_gdq_spin_estatistica|Construção GDQ do spin, estatística e Pauli]]

## 1. Estrutura spin

Status: demonstrado para o bulk local oficial.

Nota:

[[estrutura_spin_em_R4_T4|Estrutura spin em $\mathbb R^4\times T^4$]]

## 2. Recobrimento duplo e rotação

Status: teorema estrutural.

Nota:

[[rotacao_2pi_4pi_su2|Rotação de $2\pi$ e $4\pi$ em $SU(2)$]]

## 3. Hopf, resíduo e meia-monodromia

Status: leitura geométrica compatível.

Nota:

[[spin_hopf_residuo_cauchy|Spin, Hopf e resíduo de Cauchy]]

## 4. Troca fermiônica

Status: interpretação geométrica da antissimetria.

Nota:

[[holonomia_troca_fermionica|Holonomia de troca fermiônica]]

## 5. Pauli

Status: teorema algébrico no setor CAR.

Nota:

[[pauli_car_barreira_bohm|Pauli, CAR e barreira de Bohm]]

Certificação Lean complementar:
[CARPauli.lean](../../../formal/GDQ/CARPauli.lean). O módulo prova
abstratamente, em um espaço de operadores linear de característica zero, que

$$
a_i^\dagger a_i^\dagger
+
a_i^\dagger a_i^\dagger
=0
$$

implica

$$
(a_i^\dagger)^2=0.
$$

Ele também prova que uma função de onda antissimétrica satisfaz
$\Psi(x,x)=0$. O módulo assume as CAR; não afirma que elas já foram derivadas
fora das hipóteses do teorema spin--estatística abaixo.

## 6. Spin--estatística

Status: teorema condicional no setor efetivo físico.

Hipóteses:

1. espaço-tempo Lorentziano físico $(N,h)$;
2. estrutura spin;
3. produto interno positivo;
4. energia positiva;
5. cone causal comum;
6. localidade graduada.

Conclusão:

$$
\text{spin semi-inteiro}
\Longrightarrow
\text{estatística fermiônica}.
$$

Nota completa:

[[teorema_spin_estatistica_condicional|Teorema spin-estatística condicional na GDQ]]

Certificação Lean da interface lógica:
[SpinStatisticsConditional.lean](../../../formal/GDQ/SpinStatisticsConditional.lean).
O módulo tipa separadamente setor Lorentziano, estrutura spin, spin
semi-inteiro, cone causal comum, positividade do produto interno e da energia,
localidade dos observáveis pares e localidade graduada. Uma realização da
ponte relativística produz CAR e, pelo módulo `CARPauli`, exclusão de Pauli.

Limite: Lean certifica a composição condicional e sua consequência algébrica;
a demonstração analítica completa do teorema spin--estatística relativístico
continua sendo o resultado externo aplicado sob essas hipóteses.
