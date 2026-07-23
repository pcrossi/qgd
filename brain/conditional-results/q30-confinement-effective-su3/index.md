---
title: Q30 effective SU3 confinement structure
status: closed-structurally-effective
source: manuscrito/18_confinement_signal_problem/index.md
updated: 2026-07-21
---

# Q30 effective SU3 confinement structure

## Enunciado

No setor efetivo de cor da GDQ, a cadeia estrutural de confinamento é:

$$
E_C\simeq\mathbb C^3
\Longrightarrow
SU(3)_C
\Longrightarrow
A_C
\Longrightarrow
F_C
\Longrightarrow
W_R(C)
\Longrightarrow
\sigma>0
\Longrightarrow
\langle W(C)\rangle\sim e^{-\sigma A_{\min}}
\Longrightarrow
V(r)=\sigma r
\Longrightarrow
\Delta>0.
$$

## Lei de área

A constância de tensão não é assumida. Para o tubo minimizador,

$$
\partial_z\mathcal L_\perp=0
\Longrightarrow
\mathcal L_\perp(q_0,0)=\sigma=\text{constante}.
$$

Então:

$$
\langle W(C)\rangle
\sim
\exp[-\sigma A_{\min}(C)].
$$

## Gap

Depois de remover modos de gauge puro e modos nulos geométricos, a Hessiana
efetiva tem forma

$$
\mathcal H_{\rm conf}
=
-\Delta_{A_C}+V_{\rm geom}.
$$

Sob a condição suficiente

$$
\operatorname{Ric}^{B}_f\ge \Lambda_0 g,
\qquad
\Lambda_0>0,
\qquad
\sigma>0,
$$

obtém-se

$$
\lambda_1\ge c_D\Lambda_0+c_\sigma\sigma>0.
$$

## Status lógico

Fechado estruturalmente no setor efetivo GDQ--$SU(3)_C$. Não declarar como
solução completa do problema Clay de Yang--Mills puro.

## Correção GDQ vigente

A rota física fundamental da Q30 não é uma ação de Yang--Mills importada. O
background transversal vigente é o pescoço Ricci--Bohm do sóliton GDQ:

$$
\mathcal A_0=\pi r_\perp^2,
\qquad
\Delta_{\rm GDQ}=\frac{\hbar c}{r_\perp},
\qquad
\sigma_{\rm GDQ}
=\mathcal S_\perp[q_*]-\mathcal S_\perp[q_{\rm vac}]>0.
$$

A integração direta reduzida preservada no manuscrito calcula:

$$
\sigma_{\rm GDQ}
=\int_0^{r_\perp}2\pi s\,ds\,
\frac{\hbar c}{r_\perp^4}
=\pi\frac{\hbar c}{r_\perp^2}.
$$

Ela fornece:

$$
r_\perp=0{,}86\,\mathrm{fm},
\qquad
\Delta_{\rm GDQ}=0{,}229449977209\,\mathrm{GeV},
\qquad
\sigma_{\rm GDQ}=0{,}838184142752\,\mathrm{GeV/fm}.
$$

Classificação: integração direta reduzida e comparação fenomenológica
posterior. A integração 8D completa de $\mathcal S_\perp[q_*]$ permanece como
refinamento metrológico, não como reabertura do confinamento estrutural. O
funcional homogêneo $\mathcal W_Q(R)$ não deve substituir a tensão tubular:
ele produziria $0{,}435314347824\,\mathrm{GeV/fm}$.

O coeficiente reduzido foi derivado no cap Ricci--Bohm:

$$
C_{\rm GDQ}
=\frac14\int_{\rm cap}R_2\,dA
=\pi.
$$

Logo, $\pi$ é carga geométrica reduzida do cap com bordo geodésico, não
calibração pelo dado hadrônico.

Correção de status: o cap primitivo não bate metrologicamente. Para
$r_\perp=0{,}86\,\mathrm{fm}$, falta
$F_{\rm shape}=1{,}061819181018$ para atingir
$\sigma_{\rm had}\simeq0{,}89\,\mathrm{GeV/fm}$. Com
$F_{\rm shape}=1$, o raio efetivo seria
$r_{\rm eff}=0{,}834589983421\,\mathrm{fm}$.

Reavaliação com raio efetivo legado: usando
$r_{\rm eff}=0{,}8354\,\mathrm{fm}$ já presente no corpus, obtém-se
$F_{\rm shape}=1{,}059761067152$ e
$\sigma_{\rm GDQ}^{\rm eff}=0{,}888274921594\,\mathrm{GeV/fm}$, com desvio
$-0{,}193829\%$ frente à escala $0{,}89\,\mathrm{GeV/fm}$. Esse fechamento é
condicionado ao raio efetivo legado.

Derivação canônica Q39/Q40: o raio de superfície é
$r_p=0{,}840778765450\,\mathrm{fm}$, dando
$F_{\rm shape}=1{,}046245090518$ e
$\sigma_{\rm GDQ}=0{,}876946044304\,\mathrm{GeV/fm}$. Esse é o valor derivado
sem usar a tensão como alvo; o $0{,}8354\,\mathrm{fm}$ deve permanecer como
cenário adicional de compressão de sonda.

Status consolidado: Q30 fechada estruturalmente e com escala de tensão
fechada condicionalmente ao raio efetivo. A diferença entre raio canônico e
raio comprimido é questão de contorno/sonda, não falha da lei linear nem do
gap.

Atualização de autocontenção do manuscrito: as deduções foram migradas para
`manuscrito/18_confinement_signal_problem/notes/confinement/`, incluindo
`coeficiente_cap_ricci_bohm.md`, `raio_fator_forma_tensao.md`,
`hessiana_torcional_vinculada.md`, `medida_selas_tubulares_lei_area.md` e
`equivalencia_operacional_heaviside_yang_mills.md`. Scripts autocontidos
correspondentes foram adicionados e executados no diretório
`manuscrito/18_confinement_signal_problem/scripts/`.
