---
title: "Checklist operacional — Capítulo 22"
---

# Checklist operacional — Capítulo 22

## 1. Construções incluídas

| Construção | Status |
|---|---|
| $\mathcal D_{p,e}^{B}$ | redução espinorial efetiva |
| domínio e contorno $\mathsf R_p$ | formulados |
| Schur/DtN $\mathsf R_p=K_{YY}-K_{YI}K_{II}^{-1}K_{IY}$ | incluído |
| Sommerfeld--Dirac | calculado |
| estrutura fina | calculada |
| hiperfina | calculada em camadas |
| Zemach | calculado por casca e por fator magnético Schur |
| Lamb near | escala diagnosticada |
| hidrogênio muônico | amplificação calculada |

## 2. Scripts incorporados

Os scripts finais estão em [[scripts/README]].

## 3. Omissões deliberadas

Não foram incorporadas tentativas históricas nem scripts que usavam o valor
metrológico como ajuste. O capítulo preserva apenas a cadeia final reduzida e
as escalas diagnósticas.

## 4. Certificação formal

| Módulo | Alcance |
|---|---|
| `formal/GDQ/HydrogenSpectrum.lean` | Massa reduzida; simetria $\kappa\leftrightarrow-\kappa$; degenerescência Coulombiana; desdobramento fino $m\alpha^4/32$; álgebra singlete--triplete; sinal de Zemach; critério de Schur protônico. |

A fórmula Sommerfeld--Dirac é registrada como espectro do operador efetivo no
domínio declarado. A formalização certifica suas consequências algébricas;
ela não substitui a análise espectral contínua do operador radial.

## 5. Pendência real

Falta a avaliação direta dos blocos superiores da Hessiana protônica:

$$
K_{YY},
\qquad
K_{YI},
\qquad
K_{II}.
$$

Essa pendência é metrológica, não estrutural.
