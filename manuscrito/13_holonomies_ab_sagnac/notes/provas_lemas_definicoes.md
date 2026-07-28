---
title: "Provas, lemas e definições — Capítulo 13"
---

# Provas, lemas e definições — Capítulo 13

## 1. Holonomia AB

Status: fechado estruturalmente.

Nota:

[[holonomia_ab_patches_mayer_vietoris|Holonomia AB por patches e Mayer-Vietoris]]

## 2. Invariância de calibre

Status: demonstrada em laço fechado.

Nota:

[[invariancia_calibre_AB|Invariância de calibre no AB]]

Certificação complementar:
[AharonovBohmHolonomy.lean](../../../formal/GDQ/AharonovBohmHolonomy.lean).
O módulo prova que $A\mapsto A+d\lambda$ não altera a circulação quando os
extremos do levantamento coincidem e que circulação e fluxo produzem a mesma
holonomia quando a identidade de Stokes vale no domínio perfurado. A hipótese
de Stokes permanece geométrica e explícita.

O núcleo de colagem e Stokes celular é certificado adicionalmente em
[HolonomyPatchingStokes.lean](../../../formal/GDQ/HolonomyPatchingStokes.lean).
Nesse módulo:

1. a soma da curvatura discreta nas faces é provada igual à circulação na
   cadeia de bordo;
2. o representante $A_{\rm harm}=\Phi\,d\theta/(2\pi)$ tem circulação
   exatamente $\Phi$ quando a soma angular é $2\pi$;
3. mudanças do levantamento da função de transição por $2\pi n$ deixam a
   holonomia `U(1)` inalterada;
4. a meia-volta possui holonomia $-1$.

O primeiro item é a realização celular finita de Stokes. O teorema suave
sobre variedades continua sendo aplicado com suas hipóteses usuais de
regularidade, orientação e domínio; não foi substituído por uma identidade
combinatória.

## 3. Potencial como conexão GDQ

Status: interpretação estrutural.

Nota:

[[potencial_como_conexao_na_GDQ|Potencial como conexão na GDQ]]

## 4. Solenoide real

Status: programa metrológico.

Nota:

[[solenoide_real_schur_DtN|Solenoide real por Schur/DtN]]

Construção variacional:

[[hessiana_projetores_resposta_interface|Hessiana, projetores e resposta de interface]]

## 5. Sagnac

Status: fechado estruturalmente.

Nota:

[[sagnac_forma_relogio|Sagnac como forma-relógio]]

Certificação complementar:
[SagnacHolonomy.lean](../../../formal/GDQ/SagnacHolonomy.lean). O módulo prova
que a fase comum cancela, o termo ímpar sob orientação é duplicado e a
reversão da rotação troca o sinal da diferença. A conversão desse termo em
uma frequência ou atraso exige a métrica e a geometria do interferômetro.

O mesmo módulo
[HolonomyPatchingStokes.lean](../../../formal/GDQ/HolonomyPatchingStokes.lean)
prova que, se a circulação cinemática vale
$2\boldsymbol\Omega\cdot\mathbf A$, então o prefator dos dois sentidos
produz exatamente
$4\boldsymbol\Omega\cdot\mathbf A/c^2$. Assim, o fator quatro não é um
parâmetro ajustado: ele é a composição do fator dois da circulação rotacional
com o fator dois da comparação dos dois sentidos.

## 6. COW

Status: extensão reduzida.

Nota:

[[cow_interferometria_gravitacional|COW como extensão interferométrica]]
