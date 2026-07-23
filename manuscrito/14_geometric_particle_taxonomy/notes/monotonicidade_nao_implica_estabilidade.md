---
title: "Monotonicidade não implica estabilidade sem Hessiana"
---

# Monotonicidade não implica estabilidade sem Hessiana

Esta nota fixa uma distinção necessária na GDQ: funcionais monotônicos de
Perelman--Bismut controlam o fluxo geométrico, mas não bastam para declarar uma
partícula estável. Estabilidade de uma configuração material exige o espectro
da segunda variação no setor físico.

## 1. Funcionas auxiliares

No setor torsional/Bismut, o funcional de energia geométrica de escala fixa é

$$
\mathcal F_T(g,H,\phi)
=
\int_M
\left(
R
-\frac1{12}|H|^2
+|\nabla\phi|^2
\right)
e^{-\phi}dV_g.
$$

O funcional de escala variável é

$$
\mathcal W_T(g,H,\phi,\sigma)
=
\int_M
\left[
\sigma
\left(
R
-\frac1{12}|H|^2
+|\nabla\phi|^2
\right)
+\phi-d
\right]
(4\pi\sigma)^{-d/2}e^{-\phi}dV_g.
$$

Esses funcionais são auxiliares de estabilidade geométrica. Eles não substituem
a ação oficial da GDQ.

## 2. Hipóteses da monotonicidade

A identidade de monotonicidade exige:

1. bulk Riemanniano/Hermitiano positivo;
2. regularidade suficiente da solução;
3. $H$ real e antissimétrico;
4. condição de Bianchi torsional, por exemplo $dH=0$ no setor simples;
5. medida normalizada;
6. termos de bordo nulos ou compensados;
7. gauge adequado;
8. topologia do setor preservada.

A medida usada é

$$
d\mu
=
(4\pi\sigma)^{-d/2}e^{-\phi}dV_g,
$$

ou, na ação complexa,

$$
\rho=e^{-(f+\bar f)/2}.
$$

## 3. Derivada como soma de quadrados

Na convenção em que o funcional cresce com $\tau$:

$$
\frac{d\mathcal F_T}{d\tau}
=
2\int_M
\left|
R_{ij}
-\frac14H_{ik\ell}H_j{}^{k\ell}
+\nabla_i\nabla_j\phi
\right|^2
e^{-\phi}dV_g
+
\frac16
\int_M
\left|
d_\phi^\dagger H
\right|^2
e^{-\phi}dV_g
\ge0.
$$

Para $\mathcal W_T$:

$$
\frac{d\mathcal W_T}{d\tau}
=
2\sigma
\int_M
\left|
R_{ij}
-\frac14H_{ik\ell}H_j{}^{k\ell}
+\nabla_i\nabla_j\phi
-\frac1{2\sigma}g_{ij}
\right|^2
d\mu
+
\frac{\sigma}{6}
\int_M
\left|
d_\phi^\dagger H
\right|^2
d\mu
\ge0.
$$

Se a orientação do fluxo for invertida, os mesmos enunciados aparecem com
sinal oposto. O conteúdo invariável é: a derivada é soma de quadrados e zera
em solítons.

## 4. O que a monotonicidade prova

Ela prova que o funcional atua como Lyapunov para o fluxo no setor em que as
hipóteses valem.

Ela também caracteriza pontos críticos. Para $\mathcal W_T$, a igualdade
ocorre quando

$$
R_{ij}
-\frac14H_{ik\ell}H_j{}^{k\ell}
+\nabla_i\nabla_j\phi
=
\frac1{2\sigma}g_{ij},
$$

e

$$
d_\phi^\dagger H=0.
$$

Isso identifica candidatos a sóliton Ricci--Bismut/Perelman.

## 5. O que a monotonicidade não prova

Monotonicidade não determina sozinha se o ponto crítico é mínimo, máximo ou
sela no espaço físico de perturbações.

Para isso, deve-se calcular a segunda variação:

$$
\delta^2\mathcal I_T[U,U]
=
\langle U,\mathcal J_{\mathfrak S}U\rangle_{\rho_\ast},
$$

onde

$$
U=(h,\beta,\eta)
$$

representa perturbações de métrica, torção e dilaton/fase real, e

$$
\mathcal J_{\mathfrak S}
=
D^2\mathcal I_T|_{\mathfrak S}.
$$

Esquematicamente:

$$
\mathcal J_{\mathfrak S}
=
\begin{pmatrix}
\Delta_L^\phi+\mathcal R_{HH}+\mathcal R_{\phi\phi}
&
\mathcal C_{gH}
&
\mathcal C_{g\phi}
\\
\mathcal C_{Hg}
&
\Delta_{H,\phi}+\mathcal M_H
&
\mathcal C_{H\phi}
\\
\mathcal C_{\phi g}
&
\mathcal C_{\phi H}
&
-\Delta_\phi+\mathcal V_\phi
\end{pmatrix}.
$$

Aqui $\Delta_L^\phi$ é Lichnerowicz ponderado, $\Delta_{H,\phi}$ é
Hodge ponderado e os blocos $\mathcal C$ registram acoplamentos de menor
ordem.

## 6. Espaço físico

O espectro deve ser avaliado depois de remover modos que não representam
instabilidade física:

$$
\mathcal H_{\rm phys}
=
\left(
\ker_{\rm diff}
\oplus
\ker_{\rm gauge}
\oplus
\ker_{\rm trans}
\oplus
\ker_{\rm rot}
\oplus
\ker_{\rm scale}
\oplus
\ker_{\rm moduli}
\right)^\perp.
$$

No sinal em que $\mathcal I_T$ é energia livre minimizada, a condição de
estabilidade linear é

$$
\operatorname{spec}
\left(
\mathcal J_{\mathfrak S}\big|_{\mathcal H_{\rm phys}}
\right)
\subseteq[0,\infty).
$$

Autovalor negativo físico significa instabilidade. Autovalor zero não
explicado significa modo marginal ou modulus não controlado.

## 7. Caso gaussiano

Para o solíton gaussiano neutro:

$$
g=\delta,
\qquad
H=0,
\qquad
\phi=\frac{|x|^2}{4\sigma},
$$

o operador escalar reduzido é do tipo Ornstein--Uhlenbeck:

$$
\mathcal L_{\rm OU}
=
-\Delta
+\frac{x}{2\sigma}\cdot\nabla.
$$

Seu espectro em $L^2(\rho_NdV)$ é

$$
\lambda_k=\frac{k}{2\sigma}.
$$

Depois de remover o modo constante e os modos de simetria/moduli do setor, o
gap reduzido é positivo.

## 8. Critério final

A implicação correta é:

$$
\text{monotonicidade}
+
\text{ponto crítico real}
+
\text{bordos compatíveis}
+
\text{topologia preservada}
+
\text{Hessiana física sem autovalores negativos}
\Rightarrow
\text{estabilidade local/orbital}.
$$

Sem o último termo, não há prova de estabilidade de partícula.

