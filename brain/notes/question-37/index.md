---
title: Questão 37 — constante de estrutura fina
status: structurally-resolved-numerically-open
source: questoes/q37/questao_37.md
updated: 2026-07-16
---

# Questão 37 — constante de estrutura fina

## Estado vigente

A Q37 está estruturalmente resolvida e numericamente aberta.

A GDQ fornece a cadeia correta para $\alpha$ como normalização do canal
eletromagnético $U(1)_Q$, mas o valor absoluto exige calcular $Z_Q^E$ pela
Hessiana oficial global e pelo complemento de Schur, sem inserir o alvo.

## Cadeia vigente

O setor elétrico é deformação horizontal gerada pela direção primitiva
$U(1)_Q$. O coeficiente físico é:

$$
K_Q^{\rm eff}
=
K_{QQ}-K_{Q\perp}K_{\perp\perp}^{-1}K_{\perp Q}.
$$

Se a ponte preserva corrente simplética, normalização primitiva e forma-relógio:

$$
Z_Q^{\rm lab}=Z_Q^E,
\qquad
\alpha_{\rm lab}=\alpha_E.
$$

## Resultado diagnóstico

A aproximação DtN pela 4-bola redonda deu:

$$
\alpha_{\rm DtN}^{-1}=137{,}604601779\ldots
$$

sem usar $\alpha$ como entrada, com erro de $0{,}414868\%$ em $Z_Q$. Isso
indica a rota correta, mas ainda não é prova final.

## Fórmula cosmológica histórica

A fórmula histórica pode ser lida como média cosmológica de Einstein e fica
condicional à isotropia do ensemble e à seleção do autovetor Hopf axial
coerente. Ainda falta derivar a igualdade numérica pela Hessiana global.

## Ponteiros

- Resultado: `brain/conditional-results/q37-alpha-structural-normalization/index.md`
- Pendência: `brain/open-problems/q37-alpha-dtn-warped-bismut/index.md`

