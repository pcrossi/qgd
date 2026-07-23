---
title: "Hessiana torsional vinculada da garganta"
---

# Hessiana torsional vinculada da garganta

Esta nota mostra como a conservação de carga torsional produz rigidez. O ponto
central é que puxar o estômato não permite variar volume e módulo de torção de
forma independente.

## 1. Conservação de carga

Seja $\Sigma_s$ um ciclo tridimensional envolvendo a garganta. Suponha:

$$
dH_s=0,
\qquad
Q_T:=\int_{\Sigma_s}H_s={\rm constante}.
$$

Na classe fixa:

$$
H_s
=
Q_T\eta_s+d\beta_s,
\qquad
\int_{\Sigma_s}\eta_s=1.
$$

O representante de menor norma é o harmônico:

$$
H_s=Q_T\eta_s.
$$

Então:

$$
\mathcal E_T(s)
=
\frac{\kappa_T}{2}Q_T^2
\int_{\Sigma_s}
|\eta_s|_{g_s}^2\,d\mu_{g_s}.
$$

## 2. Caso homogêneo

Se:

$$
\eta_s
=
\frac{{\rm vol}_{\Sigma_s}}{V(s)},
\qquad
V(s)={\rm Vol}(\Sigma_s),
$$

então:

$$
H_s
=
\frac{Q_T}{V(s)}
{\rm vol}_{\Sigma_s},
$$

e:

$$
\mathcal E_T(s)
=
\frac{\kappa_TQ_T^2}{2V(s)}.
$$

Assim, uma deformação que altera $V$ altera necessariamente $|H|$.

## 3. Funcional radial homogêneo

No setor homogêneo $S^3$ da garganta:

$$
\mathcal W_Q(R)
=
\tau
\left(
\frac6{R^2}
-
\frac{Q_T^2}{2\pi^2R^6}
\right)
+3\log R.
$$

A primeira variação é:

$$
\mathcal W_Q'(R)
=
\frac{3}{\pi^2R^7}
\left[
Q_T^2\tau
+\pi^2R^6
-4\pi^2\tau R^4
\right].
$$

Logo, a sela satisfaz:

$$
R^6-4\tau R^4+\frac{\tau Q_T^2}{\pi^2}=0.
$$

## 4. Segunda variação

Antes de impor a sela:

$$
\mathcal W_Q''(R)
=
-\frac{3}{\pi^2R^8}
\left[
7Q_T^2\tau
+\pi^2R^6
-12\pi^2\tau R^4
\right].
$$

Eliminando $Q_T$ pela equação estacionária:

$$
K_R
:=
\left.
\mathcal W_Q''(R)
\right|_{\rm sela}
=
\frac{6(3R^2-8\tau)}{R^4}.
$$

Portanto:

$$
K_R>0
\quad
\Longleftrightarrow
\quad
R^2>\frac83\tau.
$$

## 5. Avaliação reduzida

Com:

$$
R=1{,}03707435228632,
\qquad
\tau=0{,}274900522513626,
\qquad
Q_T=1,
$$

obtemos:

$$
\frac{R^2}{\tau}
=
3{,}91240875912406
>
\frac83,
$$

e:

$$
K_R
=
5{,}32888850629080>0.
$$

Assim, a conservação torsional estabiliza o modo radial homogêneo.

## 6. Resposta estática

Para uma fonte clássica $J_R$:

$$
\delta^2\mathcal W_J
=
\frac12K_R(\delta R)^2
-J_R\delta R.
$$

Logo:

$$
\delta R
=
K_R^{-1}J_R,
\qquad
K_R^{-1}
=
0{,}187656393790\ldots.
$$

Como $V_{S^3}\propto R^3$ e $Q_T$ é conservada:

$$
\frac{\delta |H|}{|H|}
=
-3\frac{\delta R}{R}.
$$

## 7. Limite

Esse é um teorema setorial para o modo homogêneo vinculado. A coercividade
total ainda exige controlar modos anisotrópicos, blocos de curvatura/dilatão e
mobilidade causal.

