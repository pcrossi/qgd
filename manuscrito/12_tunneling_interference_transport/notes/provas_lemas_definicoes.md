---
title: "Provas, lemas e definições — Capítulo 12"
---

# Provas, lemas e definições — Capítulo 12

## 0. Construção GDQ do problema

Status: cadeia fonte--background--Hessiana--impedância--transporte.

Nota:

[[construcao_gdq_transporte_interferencia|Construção GDQ do transporte e da interferência]]

## 1. Hartman reduzido

Status: ansatz conformal unidimensional.

Nota:

[[hartman_ansatz_conformal_unidimensional|Hartman como ansatz conformal unidimensional]]

Certificação Lean:
[TransportInterference.lean](../../../formal/GDQ/TransportInterference.lean).
O módulo prova a atenuação evanescente, a identidade exata do erro
exponencial para a assíntota e:

$$
\lim_{L\to\infty}
D_{\rm prop}(L)
=
\frac{\sqrt{g_0}}{\kappa}.
$$

A certificação é condicional ao ansatz reduzido declarado na nota.

## 2. Dupla fenda em Madelung

Status: redução efetiva em fundo fixo.

Nota:

[[dupla_fenda_madelung_fundo_fixo|Dupla fenda em Madelung no fundo fixo]]

O mesmo módulo Lean prova:

$$
|\psi_1+\psi_2|^2
=
|\psi_1|^2+|\psi_2|^2
+2\operatorname{Re}(\psi_1\bar\psi_2),
$$

e os limites construtivo e destrutivo do padrão para amplitudes não
negativas.

## 3. Nós e pressão de Bohm

Status: consequência da redução Madelung.

Nota:

[[pressao_bohm_nos_interferencia|Pressão de Bohm nos nós de interferência]]

## 4. Detector por DtN/Schur

Status: fechado estruturalmente em canal reduzido.

Nota:

[[detector_DtN_Schur_visibilidade|Detector DtN/Schur e visibilidade]]

Certificação Lean:
[DetectorDtNSchur.lean](../../../formal/GDQ/DetectorDtNSchur.lean). A partir do
perfil hiperbólico com Dirichlet nas duas extremidades, o módulo deriva

$$
-\partial_s\varphi(0)
=
\lambda\coth(\lambda L)\varphi_0,
$$

prova a positividade da impedância para $\lambda,L>0$, a não negatividade do
expoente de Schur e

$$
0<
e^{-\Gamma_{\rm det}}
\le1.
$$

Os valores de $\lambda$, $L$ e do acoplamento continuam pertencendo ao
aparelho concreto, não à ação fundamental.

## 5. Escolha retardada

Status: fechado estruturalmente como contorno/transporte.

Nota:

[[escolha_retardada_contorno_nao_retrocausal|Escolha retardada como contorno]]

A versão finita do kernel causal também é certificada em
[TransportInterference.lean](../../../formal/GDQ/TransportInterference.lean):
se o peso do kernel desaparece depois do registro, alterar somente os dados
futuros não modifica o registro calculado.
