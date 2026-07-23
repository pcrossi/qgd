---
title: "20. Gravitação, vácuo e contorno cosmológico"
---

# 20. Gravitação, vácuo e contorno cosmológico

Este capítulo organiza a parte gravitacional e cosmológica da GDQ.

A ideia central é separar três níveis que não podem ser misturados:

1. o bulk local oficial;
2. o espaço cosmológico de Einstein;
3. a projeção macroscópica que o observador lê como gravitação.

O bulk local oficial continua sendo

$$
M_{\rm loc}
=
\mathbb R^4\times T^4.
$$

O espaço cosmológico/espectral usado para normalizações globais é

$$
M_E
=
T^5\times S^3.
$$

O valor de $G$, a densidade de energia escura e a escala de aceleração
galáctica não são extraídos de uma fibra local infinitesimal. Eles pertencem
ao problema global de contorno. A geometria local deve transportar esse dado
e ser compatível com ele, mas não substitui o contorno cosmológico.

## Cadeia do capítulo

O capítulo usa a cadeia:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast^{\rm cos}
\to
K_{\rm cos}^{\rm phys}
\to
\text{contorno global}
\to
G,\rho_\Lambda,a_0.
$$

Quando a Hessiana cosmológica completa não foi diagonalizada, o resultado é
classificado como estrutural ou condicional. Quando uma fórmula reduzida já foi
derivada, ela é avaliada numericamente e comparada com valores aceitos.

## Seções

- [[20.1 - Gravidade como resposta global da GDQ]]
- [[20.2 - O grupo adimensional de Newton]]
- [[20.3 - Regularidade térmica e colagem axial]]
- [[20.4 - Energia do vácuo e tensão UV protonica]]
- [[20.5 - Diluição linear, 28 canais e projeção alpha2]]
- [[20.6 - Equação de estado e perturbações cosmológicas]]
- [[20.7 - Aceleração crítica e limite galáctico]]
- [[20.8 - Hessiana cosmológica e status metrológico]]

## Notas chamadas

- [[notes/gravity/prova_grupo_pi_newton|Grupo adimensional de Newton]]
- [[notes/gravity/cadeia_termico_axial_newton|Cadeia térmico-axial do cálculo reduzido de Newton]]
- [[notes/gravity/auditoria_prefator_buckingham|Auditoria do prefator de Buckingham]]
- [[notes/gravity/auditoria_rotas_descartadas_G|Rotas descartadas na derivação de G]]
- [[notes/gravity/derivacao_rho_lambda|Derivação da densidade de energia escura]]
- [[notes/gravity/perturbacoes_hessiana_cosmologica|Perturbações e Hessiana cosmológica]]
- [[notes/gravity/aceleracao_critica|Aceleração crítica]]
- [[notes/gravity/torcao_homogenea_fluido_rigido|Torção homogênea como fluido rígido]]

## Scripts e verificações

- [[scripts/README|Scripts do Capítulo 20]]
- [[checklist_operacional|Checklist operacional]]

## Status

| Bloco | Status | Observação |
|---|---|---|
| $G$ como grupo adimensional | fechado estruturalmente | $\Pi_G=G M_p^2/(\hbar c)$ |
| $G$ como resposta de contorno | fechado condicionalmente | exige $R_H$ e $E_H$ do problema cosmológico |
| expoente $e^{-1/(2\alpha)}$ | condicional | depende da colagem global $R=\pi^2\sqrt\alpha R_H$ |
| prefator Buckingham | fenomenologia forte | perto de $G$, mas não ab initio completo |
| energia escura a energia do vácuo | fechada estruturalmente | erro numérico atual de cerca de $5\%$ |
| $w=-1$ | fechado no background homogêneo | perturbações exigem Hessiana cosmológica |
| $a_0$ | fechado estruturalmente | $a_0=cH_0/(2\pi)$, não MOND fundamental |
| metrologia CMB/BAO/SNe | programa posterior | requer $\Phi_\ast^{\rm cos}$ completo |

[[../19_electroweak_geometric_breaking/index|← Previous chapter]] | [[../index|Manuscrito]] | [[../21_cp_hopf_monopoles/index|Next chapter →]]
