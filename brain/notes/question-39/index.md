---
title: Questão 39 — massas leptônicas
status: resolved-intrinsic-reduced-and-8d-product
source: questoes/q39/questao_39.md
updated: 2026-07-16
---

# Questão 39 — massas leptônicas

## Estado vigente

A Q39 está fechada pela rota GDQ intrínseca reduzida de tensão/topologia e
pela elevação por Schur ao background 8D estacionário produto/bloco.

A antiga rota Rosen--Morse/Reg-Reg permanece preservada como benchmark
histórico numericamente coerente, mas não é mais a ontologia da hierarquia
leptônica porque promovia o índice radial \(n_\tau=17\) a índice físico de
geração.

## Cadeia vigente

O modelo reduzido intrínseco usa três setores físicos:

- \(e\): torção primária;
- \(\mu\): torção transversal/biespacial;
- \(\tau\): saturação tridimensional.

O múon é:

$$
R_\mu
=
\frac{3}{2\alpha}
+\frac65
+2\alpha
\simeq
206{,}768593470628673.
$$

O tau é determinado por:

$$
\frac{1+R_\mu+R_\tau}
{(1+\sqrt{R_\mu}+\sqrt{R_\tau})^2}
=
\frac23,
$$

dando:

$$
R_\tau
\simeq
3477{,}446405098381092.
$$

## Elevação 8D

No background leptônico 8D estacionário produto:

$$
g_8=g_B\oplus g_K,
\qquad
A(k)=\mathrm{const},
\qquad
f_K(k)=\mathrm{const},
\qquad
H_{BK}=0,
\qquad
\mathcal C_{BK}=0.
$$

Logo:

$$
a_W=a_f=a_H=\varepsilon=0.
$$

O gap físico conservador usado no critério de Schur é:

$$
\lambda_B^{\rm gap}=\Delta_0=\frac12.
$$

Com \(C_\gamma=\tau=R_{\max}=1\), temos:

$$
m_\perp^2=1,
\qquad
j_{\rm mix}=0,
\qquad
\Delta_{\rm Schur}=0.
$$

Portanto:

$$
R_\ell^{(8)}=R_\ell^{(0)}.
$$

## Benchmark histórico

O operador radial de Rosen--Morse é:

$$
-\phi''(\chi)
+
\left(
\frac{C_{\csc}}{\sin^2\chi}
-V_{\rm cot}\cot\chi
\right)\phi(\chi)
=
\lambda\phi(\chi).
$$

No limite global:

$$
\lambda_n=(s+n)^2-\frac{b^2}{(s+n)^2}.
$$

Com $n=0,1,17$:

$$
r_2=\sqrt{\frac{\lambda_1}{\lambda_0}}\approx206{,}7679,
\qquad
r_3=\sqrt{\frac{\lambda_{17}}{\lambda_0}}\approx3477{,}1465.
$$

## Contorno físico histórico

Comparação de domínios:

- Reg-Reg: espectro global/topológico;
- Robin-Reg: um estômato finito;
- Robin-Robin: duplo estômato/espelho.

A massa de repouso física é global Reg-Reg; contornos Robin medem resposta
local de cirurgia.

## Estabilidade

Três gerações carregadas estáveis são ancoradas pelo suporte tridimensional
de tensão, pela exclusão de quarto projetor ortogonal em \(\mathbb R^3\) e
pela preservação do índice crítico no Schur 8D produto.

Backgrounds warped/mistos reais permanecem como setores condicionais: devem
ser avaliados calculando \(a_W,a_f,a_H,\varepsilon\) no próprio background e
aplicando o critério

$$
\frac{j_{\rm mix}^2}{m_\perp^2}<\lambda_B^{\rm gap}.
$$

## Ponteiro

- Resultado vigente: `questoes/q39/questao_39.md`
- Avaliação 8D: `questoes/q39/associados/saida_background_8d_estacionario_q39.md`
- Benchmark histórico: `brain/conditional-results/q39-leptonic-mass-spectrum/index.md`
