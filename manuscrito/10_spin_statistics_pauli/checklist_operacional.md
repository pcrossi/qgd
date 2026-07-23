---
title: "Checklist operacional — Capítulo 10"
---

# Checklist operacional — Capítulo 10

## 1. Enunciado

Mostrar como a GDQ interpreta spin como circulação/torção e, ao mesmo tempo,
recupera matematicamente spin $1/2$, estatística fermiônica e exclusão de
Pauli no setor efetivo correto.

## 2. Status lógico

| Bloco | Status | Observação |
|---|---|---|
| Circulação/torção | Interpretação GDQ | Não substitui estrutura spinorial. |
| Estrutura spin de $\mathbb R^4\times T^4$ | Demonstrada | $w_2=0$. |
| Spin $1/2$ | Fechado estruturalmente | Recobrimento $SU(2)\to SO(3)$. |
| Resíduo/Hopf | Fechado como leitura geométrica | Meia-monodromia por raiz quadrada. |
| Clifford/Dirac--Bismut | Efetivo | Operador reconstruído, não ação fundamental. |
| Estatística fermiônica | Fechada condicionalmente | Setor Lorentziano, positivo e local. |
| Pauli | Fechado no setor CAR | Barreira de Bohm é manifestação. |
| Seleção dinâmica do setor spin | Programa futuro | não reabre a construção de spin-estatística. |

## 3. Cadeia dedutiva

$$
M=\mathbb R^4\times T^4
\to
w_2=0
\to
\Phi_\ast^{\rm estômato}
\to
K_{\rm phys}^{\rm spin}
\to
P_{\rm Spin}
\to
\mathrm{Spin}(3,1)
\to
\mathrm{Clifford}
\to
U(2\pi)=-I
\to
\text{CAR}
\to
\text{Pauli}.
$$

Construção técnica chamada:

- [[notes/construcao_gdq_spin_estatistica|Construção GDQ do spin, estatística e Pauli]]

## 4. Scripts opcionais

| Script | Classificação |
|---|---|
| `verificar_rotacao_su2.py` | Teste simbólico de $2\pi$ e $4\pi$. |
| `verificar_residuo_hopf_cauchy.py` | Teste simbólico-numérico do resíduo $1/2$. |
| `verificar_holonomia_troca.py` | Teste simbólico/topológico de holonomia $-1$. |
| `verificar_car_pauli.py` | Teste algébrico de CAR e exclusão. |

## 5. Pontos que não podem ser esquecidos

- Não reduzir spin $1/2$ a circulação escalar.
- Não tratar Dirac--Bismut como ação fundamental.
- Não usar Pauli como postulado independente.
- Não confundir sinal fermiônico com peso negativo da medida.
- Não importar Modelo Padrão como ontologia.
