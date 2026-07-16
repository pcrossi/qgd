---
title: Questão 30 — confinamento, Wilson loops e mass gap
status: closed-structurally-effective
source: questão_30_yang_mills.md; questão_30.md
updated: 2026-07-16
---

# Questão 30 — confinamento, Wilson loops e mass gap

## Estado vigente

A Q30 está fechada estruturalmente no setor efetivo GDQ--$SU(3)_C$.

Isso não é uma solução completa do problema Clay de Yang--Mills puro. O que
fica estabelecido é: na GDQ, o setor de cor efetivo admite conexão $SU(3)$,
Wilson loops, lei de área e gap positivo sob hipóteses funcionais explícitas.

## Cadeia registrada

1. Pela Q28, $E_C\simeq\mathbb C^3$.
2. Automorfismos unitários preservando volume complexo geram $SU(3)_C$.
3. A conexão efetiva é

$$
A_C=G_\mu^aT_a\,dx^\mu
\in
\Omega^1(N,\mathfrak{su}(3)).
$$

4. A curvatura é

$$
F_C=dA_C+A_C\wedge A_C.
$$

5. Wilson loop é holonomia geométrica:

$$
W_R(C)=\operatorname{Tr}_R\mathcal P\exp\left(i\oint_C A_C\right).
$$

6. A tensão/constante de área $\sigma$ é obtida variacionalmente, não
   postulada.
7. Para loops retangulares:

$$
V(r)=-\lim_{T\to\infty}\frac1T\log\langle W(C_{r,T})\rangle
=\sigma r+O(1).
$$

8. O gap geométrico efetivo segue de Hessiana positiva após remoção de gauge e
   modos nulos, sob coercividade/hipóteses funcionais explicitadas.

## Cálculos preservados do manuscrito

O manuscrito contém:

- proposta analítica de $\alpha_s^{\rm eff}=3/(8\pi)$ via Fredholm;
- previsão fenomenológica $P_\Lambda\approx0{,}85\%$ para polarização global de
  híperons.

Esses cálculos são relevantes, mas não substituem a prova integral de
confinamento/mass gap no sentido externo de Yang--Mills.

## Pendências

Permanecem posteriores:

- calcular explicitamente $g_s$ por norma interna;
- formalizar completamente a medida funcional do setor $A_C$;
- provar coercividade no espaço funcional especificado;
- calcular numericamente $\sigma$ e $\lambda_1$;
- comparar com glueballs/espectro hadrônico se desejado.

## Ponteiros

- Resultado: `brain/conditional-results/q30-confinement-effective-su3/index.md`
- Pendência: `brain/open-problems/q30-explicit-confinement-numerics/index.md`

