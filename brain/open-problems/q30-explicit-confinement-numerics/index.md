---
title: Q30 explicit confinement numerics and functional closure
status: metrological-refinement
source: manuscrito/18_confinement_signal_problem/index.md
updated: 2026-07-21
---

# Q30 explicit confinement numerics and functional closure

## Problema

A Q30 sai do bloco de faltas estruturais, mas ainda exige cálculo explícito e
numérico para transformar o fechamento estrutural em avaliação quantitativa.

## O que falta

1. substituir a integração direta reduzida do disco por uma integração 8D
   completa de $\mathcal S_\perp[q_*]-\mathcal S_\perp[q_{\rm vac}]$ no
   perfil estacionário completo;
2. calcular o primeiro autovalor físico da Hessiana completa acoplada do
   pescoço Ricci--Bohm, não apenas a escala transversal
   $\Delta_{\rm GDQ}=\hbar c/r_\perp$;
3. comparar com espectro hadrônico/glueballs apenas depois de congelar o
   background, o operador, o domínio e os contornos.

## Já realizado

O manuscrito executa a integração direta reduzida do disco Ricci--Bohm:

$$
r_\perp=0{,}86\,\mathrm{fm},
\qquad
\mathcal A_0=2{,}323521926595\,\mathrm{fm}^2,
$$

$$
\Delta_{\rm GDQ}=0{,}229449977209\,\mathrm{GeV},
\qquad
\sigma_{\rm GDQ}=0{,}838184142752\,\mathrm{GeV/fm}.
$$

Comparado posteriormente com
$\sigma_{\rm had}\simeq0{,}89\,\mathrm{GeV/fm}$, o desvio reduzido é
$-5{,}822006\%$.

A quadratura direta reproduziu a integral analítica com erro relativo
$-1{,}325\times10^{-16}$. A auditoria do funcional homogêneo
$\mathcal W_Q(R)$ deu apenas
$0{,}435314347824\,\mathrm{GeV/fm}$; portanto esse funcional não é a tensão
tubular completa.

O Capítulo 18 derivou o
coeficiente:

$$
C_{\rm GDQ}=\frac14\int_{\rm cap}R_2dA=\pi.
$$

O aberto agora é calcular o fator de forma $F_{\rm shape}$ da solução 8D
completa. No cap primitivo reduzido, $F_{\rm shape}=1$, mas a comparação
metrológica exige $F_{\rm shape}=1{,}061819181018$ se
$r_\perp=0{,}86\,\mathrm{fm}$ for mantido.

Usando o raio efetivo legado
$r_{\rm eff}=0{,}8354\,\mathrm{fm}$, o fator de forma calculado é
$F_{\rm shape}=1{,}059761067152$, suficiente para
$\sigma_{\rm GDQ}^{\rm eff}=0{,}888274921594\,\mathrm{GeV/fm}$. O aberto
remanescente é rederivar esse mesmo raio efetivo no background transversal
oficial da Q30.

A derivação canônica Q39/Q40 já fornece
$r_p=0{,}840778765450\,\mathrm{fm}$ e
$F_{\rm shape}=1{,}046245090518$, resultando em
$\sigma_{\rm GDQ}=0{,}876946044304\,\mathrm{GeV/fm}$. O aberto real é explicar
se a Q30 deve usar o raio canônico de superfície ou o raio comprimido de
sonda, e derivar essa escolha pela condição de contorno do tubo.

Reclassificação: esse aberto é refinamento de contorno/sonda, não pendência
estrutural de confinamento.

## Status

Aberto apenas como refinamento metrológico completo. A avaliação reduzida
existe no manuscrito e não reabre o fechamento estrutural de Q30.
