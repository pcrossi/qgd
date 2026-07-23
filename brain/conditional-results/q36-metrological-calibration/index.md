---
title: Q36 metrological calibration of dimensional scale
status: closed-metrologically
source: manuscrito/15_leptonic_hierarchy_masses/notes/escala_dimensional_calibracao.md
updated: 2026-07-21
---

# Q36 metrological calibration of dimensional scale

## Enunciado

Autovalores adimensionais da GDQ tornam-se massas físicas somente após fixar
uma escala metrológica.

## Fórmula

$$
M_n c^2
=
\frac{\hbar c}{\ell_0}\sqrt{\hat\lambda_n}.
$$

Com calibração eletrônica:

$$
M_n=M_e\sqrt{\frac{\hat\lambda_n}{\hat\lambda_0}}.
$$

## Status

Fechado por calibração. A exigência física é prever razões, não criar a unidade
"MeV" a partir do nada.

## Verificação preservada

Script autocontido:

- `manuscrito/15_leptonic_hierarchy_masses/scripts/verificar_calibracao_metrologica_q36.py`.

Resultados:

$$
\frac{M_\mu}{M_e}=206{,}768593470629
$$

independente da escolha de $E_0$.

Com $M_e=0{,}51099895000\,{\rm MeV}$:

$$
M_\mu=105{,}658534156\,{\rm MeV}.
$$

A ponte beta usa:

$$
\delta_B=\ln(2\pi^2)\frac{3\sqrt2}{5}=2{,}530825921868.
$$
