---
title: Questão 30 — confinamento, Wilson loops e mass gap
status: closed-structurally-effective
source: manuscrito/18_confinement_signal_problem/index.md
updated: 2026-07-21
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

9. O coeficiente do cap Ricci--Bohm foi derivado:

$$
C_{\rm GDQ}
=
\frac14
\int_{\rm cap}R_2dA
=
\pi.
$$

10. O raio canônico de superfície fornece
$r_p=0{,}840778765450\,\mathrm{fm}$ e
$\sigma=0{,}876946044304\,\mathrm{GeV/fm}$. O raio comprimido de sonda
$0{,}8354\,\mathrm{fm}$ fornece
$\sigma=0{,}888274921594\,\mathrm{GeV/fm}$.

11. A Hessiana torsional vinculada tem
$K_R=5{,}32888850629080>0$ no modo homogêneo.

## Cálculos preservados do manuscrito

O manuscrito contém:

- proposta analítica de $\alpha_s^{\rm eff}=3/(8\pi)$ via Fredholm;
- previsão fenomenológica $P_\Lambda\approx0{,}85\%$ para polarização global de
  híperons.

Esses cálculos são relevantes, mas não substituem a prova integral de
confinamento/mass gap no sentido externo de Yang--Mills.

## Pendências

Permanecem posteriores:

- calcular explicitamente $g_s$ por norma interna completa;
- formalizar completamente a medida funcional infinita do setor $A_C$;
- provar coercividade global no espaço funcional especificado;
- calcular a Hessiana completa acoplada se for desejado espectro/glueballs;
- comparar com glueballs/espectro hadrônico se desejado.

## Ponteiros

- Resultado: `brain/conditional-results/q30-confinement-effective-su3/index.md`
- Pendência: `brain/open-problems/q30-explicit-confinement-numerics/index.md`
- Manuscrito: `manuscrito/18_confinement_signal_problem/`
