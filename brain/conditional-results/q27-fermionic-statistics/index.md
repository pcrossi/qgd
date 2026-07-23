---
title: Q27 fermionic statistics from effective spinorial sector
status: closed-structurally
source: manuscrito/10_spin_statistics_pauli/notes/teorema_spin_estatistica_condicional.md
updated: 2026-07-21
---

# Q27 fermionic statistics from effective spinorial sector

## Enunciado

No setor efetivo local, Lorentziano, spinorial, de energia positiva e produto
interno positivo, a GDQ recupera estatística fermiônica.

## Resultado

Os campos de spin semi-inteiro devem ser quantizados por anticomutadores:

$$
\{a(f),a^\dagger(g)\}=\langle f,g\rangle_{\mathcal H_1},
\qquad
\{a(f),a(g)\}=0.
$$

O espaço de muitos corpos é a álgebra exterior:

$$
\mathcal F_-(\mathcal H_1)
=
\bigoplus_{n=0}^{\infty}\wedge^n\mathcal H_1.
$$

## Leitura geométrica GDQ

A antissimetria é interpretada como holonomia torsional/spinorial:

$$
\operatorname{Hol}_\gamma=-1,
\qquad
\Psi(r_2,r_1)=-\Psi(r_1,r_2).
$$

## Limite do resultado

A holonomia explica o sinal, mas o teorema spin--estatística requer o conjunto
completo de hipóteses efetivas: localidade graduada, energia positiva,
Lorentzianidade e positividade de norma.

## Preservação no manuscrito

O resultado está autocontido no Capítulo 10:

1. `manuscrito/10_spin_statistics_pauli/10.8 - CAR, localidade graduada e energia positiva.md`;
2. `manuscrito/10_spin_statistics_pauli/10.9 - Exclusão de Pauli como nó e barreira geométrica.md`;
3. `manuscrito/10_spin_statistics_pauli/notes/teorema_spin_estatistica_condicional.md`;
4. `manuscrito/10_spin_statistics_pauli/notes/holonomia_troca_fermionica.md`;
5. `manuscrito/10_spin_statistics_pauli/notes/pauli_car_barreira_bohm.md`;
6. scripts `verificar_holonomia_troca.py` e `verificar_car_pauli.py`.

Scripts preservados confirmam holonomia `-1`, exclusão
`(a_i^dagger)^2=0` e anticomutação em álgebra exterior finita.
