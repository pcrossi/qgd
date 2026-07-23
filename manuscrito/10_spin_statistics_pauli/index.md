---
title: "10. Spin, circulação, estatística e Pauli"
---

# 10. Spin, circulação, estatística e Pauli

Na GDQ, spin não é tratado como uma partícula pontual girando sobre si mesma.
A imagem física correta é a de circulação, holonomia e torção de um defeito
geométrico estendido. Porém, essa imagem não substitui a estrutura matemática
necessária para spin semi-inteiro.

O ponto central deste capítulo é:

$$
\text{a circulação manifesta o spin;}
\qquad
\text{a estrutura spinorial realiza o spin.}
$$

Por isso, o capítulo segue duas camadas. Primeiro, apresenta a leitura GDQ:
vorticidade, estômato, Hopf, resíduos e torção. Depois, mostra o fechamento
matemático no setor efetivo: estrutura spin, álgebra de Clifford, operador
espinorial, transformação $2\pi\mapsto -1$, estatística fermiônica e exclusão
de Pauli.

## Roteiro

- [[10.1 - O que significa spin na GDQ]]
- [[10.2 - Circulação, defeitos e torção]]
- [[10.3 - Por que circulação escalar não basta]]
- [[10.4 - Estrutura spin e recobrimento duplo]]
- [[10.5 - Álgebra de Clifford e operador espinorial efetivo]]
- [[10.6 - Rotação de 2pi e 4pi]]
- [[10.7 - Troca, holonomia e sinal fermiônico]]
- [[10.8 - CAR, localidade graduada e energia positiva]]
- [[10.9 - Exclusão de Pauli como nó e barreira geométrica]]
- [[10.10 - Alcance e limitações do capítulo]]

## Resultado central

A cadeia lógica do capítulo é:

$$
\text{defeito geométrico}
\to
\text{circulação/Hopf/torção}
\to
\text{estrutura spin}
\to
\text{Clifford}
\to
\text{representação de }\mathrm{Spin}(3,1)
\to
\text{CAR}
\to
\text{Pauli}.
$$

O setor espinorial efetivo usa:

$$
\psi\in\Gamma(S\otimes E),
$$

com:

$$
\{\gamma^a,\gamma^b\}=2\eta^{ab}I.
$$

Uma rotação espacial de $2\pi$ atua no levantamento spinorial como:

$$
U(2\pi)=-I,
$$

e uma rotação de $4\pi$ retorna:

$$
U(4\pi)=I.
$$

Para campos de spin semi-inteiro no setor local Lorentziano, positivo e
graduadamente local, a estatística correta é fermiônica:

$$
\{\widehat\psi_\alpha(t,\mathbf x),
\widehat\psi_\beta^\dagger(t,\mathbf y)\}
=
\delta_{\alpha\beta}\delta^{(3)}(\mathbf x-\mathbf y).
$$

Da CAR segue imediatamente:

$$
(a_i^\dagger)^2=0.
$$

Esse é o princípio de exclusão de Pauli.

## Estatuto do resultado

| Bloco | Status | Observação |
|---|---|---|
| Spin como circulação/torção | Interpretação GDQ preservada | Não substitui fibrado spin. |
| Spin $1/2$ | Fechado estruturalmente | Via estrutura spin e recobrimento duplo. |
| Resíduo/Hopf | Leitura geométrica compatível | Explica meia-monodromia. |
| Operador espinorial | Efetivo/reconstruído | Não é nova ação fundamental. |
| Estatística fermiônica | Fechada condicionalmente | Setor Lorentziano, spinorial, energia positiva e localidade graduada. |
| Pauli | Fechado no setor CAR | Barreira de Bohm é manifestação geométrica. |
| Seleção dinâmica de setor spin | Programa futuro | Não reabre a estrutura efetiva. |

## Controle editorial

- [[checklist_operacional|Checklist operacional do capítulo]]
- [[notes/provas_lemas_definicoes|Provas, lemas e definições associados]]
- [[notes/construcao_gdq_spin_estatistica|Construção GDQ do spin, estatística e Pauli]]
- [[notes/estrutura_spin_em_R4_T4|Estrutura spin em $\mathbb R^4\times T^4$]]
- [[notes/rotacao_2pi_4pi_su2|Rotação de $2\pi$ e $4\pi$ em $SU(2)$]]
- [[notes/spin_hopf_residuo_cauchy|Spin, Hopf e resíduo de Cauchy]]
- [[notes/holonomia_troca_fermionica|Holonomia de troca fermiônica]]
- [[notes/teorema_spin_estatistica_condicional|Teorema spin-estatística condicional na GDQ]]
- [[notes/pauli_car_barreira_bohm|Pauli, CAR e barreira de Bohm]]

[[../index|← Home]] | [[10.1 - O que significa spin na GDQ|Next →]]
