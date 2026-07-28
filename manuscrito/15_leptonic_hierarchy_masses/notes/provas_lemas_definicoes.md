---
title: "Provas, lemas e definições — Capítulo 15"
---

# Provas, lemas e definições — Capítulo 15

## 1. Construção GDQ da hierarquia

Status: cadeia estrutural completa.

Nota:

[[construcao_gdq_hierarquia_leptonica|Construção GDQ da hierarquia leptônica]]

## 2. Escala dimensional

Status: regra metrológica fechada.

Nota:

[[escala_dimensional_calibracao|Escala dimensional e calibração]]

Conteúdo preservado:

1. operadores físicos têm autovalores com dimensão $L^{-2}$;
2. operadores normalizados têm autovalores adimensionais;
3. a conversão exige $E_0=\hbar c/\ell_0$;
4. razões $M_i/M_j$ independem de $E_0$;
5. $M_e$ pode ser usado como padrão metrológico, sem virar derivação absoluta;
6. a ponte beta usa $\delta_B$ como número geométrico e $Q_\beta$ como
   contorno metrológico.

## 3. Rosen--Morse

Status: benchmark auxiliar.

Nota:

[[rosen_morse_benchmark_auxiliar|Rosen-Morse como benchmark auxiliar]]

## 4. Múon

Status: teorema condicional no modelo reduzido intrínseco.

Nota:

[[muon_tensao_intrinseca|Razão do múon por tensão intrínseca]]

Certificação Lean:
[LeptonicHierarchy.lean](../../../formal/GDQ/LeptonicHierarchy.lean). O módulo
prova a composição exata

$$
\frac{1}{(2/3)\alpha}+\frac65+2\alpha
=
\frac{3}{2\alpha}+\frac65+2\alpha
$$

e sua positividade para $\alpha>0$. Os coeficientes $2/3$, $6/5$ e $2\alpha$
são dados geometricamente especificados no modelo reduzido; o módulo não os
deriva da ação completa nem os promove a identidades universais de todo
background da ação oficial.

## 5. Tau/Koide

Status: teorema geométrico reduzido.

Nota:

[[koide_saturacao_geometrica|Koide como saturação geométrica]]

Certificação Lean:
[KoideGeometry.lean](../../../formal/GDQ/KoideGeometry.lean). O módulo prova a
equivalência exata entre igualdade das normas paralela e perpendicular e

$$
3\sum_i A_i^2
=
2\left(\sum_i A_i\right)^2,
$$

deduz $Q=2/3$ no setor não degenerado e verifica simbolicamente o ramo pesado
explícito. A seleção física desse ramo continua pertencendo à Hessiana do
background leptônico.

O módulo
[LeptonicHierarchy.lean](../../../formal/GDQ/LeptonicHierarchy.lean)
acrescenta a ordenação entre os ramos, a impossibilidade de quatro direções
linearmente independentes em $\mathbb R^3$, a preservação exata das razões
quando o bloco misto de Schur se anula e o critério escalar subcrítico para
uma correção mista.

## 6. Hessiana 8D

Status: fechada no background produto; warped/misto condicional.

Nota:

[[hessiana_8d_schur_hierarquia|Hessiana 8D e Schur]]

## 7. Redução Perelman 3D/8D

Status: teorema condicional fechado sob fatoração topológica.

Nota:

[[reducao_perelman_3d_bulk8|Redução Perelman 3D no bulk 8D]]

Certificação Lean:
[PerelmanProductReduction.lean](../../../formal/GDQ/PerelmanProductReduction.lean).
Sob fatoração, ausência de termos físicos mistos e planicidade de Ricci do
fator interno, o módulo prova

$$
\partial_\tau g_K=0,
\qquad
\mathcal R_8=\mathcal R_B,
$$

e a equivalência entre não limitação da curvatura total e do fator base. Isso
não afirma o resultado para backgrounds warped ou mistos.

## 8. Background 8D estacionário

Status: fechado no background produto leptônico.

Nota:

[[background_8d_estacionario|Background 8D estacionário da hierarquia]]

## 9. Scripts

Status: versões finais/reduzidas migradas.

Nota:

[[scripts_preservados_hierarquia|Scripts migrados da hierarquia leptônica]]
