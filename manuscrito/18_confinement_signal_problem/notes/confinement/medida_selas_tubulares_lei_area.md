---
title: "Medida de selas tubulares e lei de área"
---

# Medida de selas tubulares e lei de área

Esta nota formaliza a passagem entre sela tubular GDQ e lei de área.

## 1. Setores funcionais

Para um contorno fechado $C$, considere:

1. $\mathfrak C_0$: setor do vácuo;
2. $\mathfrak C_C$: setor com holonomia exigida por $C$;
3. $q_C^\ast$: sela tubular Ricci--Bohm de menor parte real da ação em
   $\mathfrak C_C$.

A diferença clássica tem forma extensiva:

$$
{\rm Re}\,\mathcal S[q_C^\ast]
-
{\rm Re}\,\mathcal S[q_0]
=
\sigma_{\rm cl}A_{\min}(C)
+\mu_{\rm cl}P(C)
+O(1).
$$

Aqui $\sigma_{\rm cl}>0$ é o custo por área da superfície de mundo do tubo.

## 2. Thimble física

O contorno causal da GDQ é complexo. Portanto, a medida positiva global não é
presumida. No regime semiclassicamente estável, usa-se a thimble de descida
íngreme $\mathcal J_C$ que passa por $q_C^\ast$.

Nessa thimble:

1. ${\rm Im}\,\mathcal S$ é constante;
2. ${\rm Re}\,\mathcal S$ cresce para longe da sela;
3. a Hessiana física não possui direções negativas após remover modos
   coletivos.

Com corte espectral $N$:

$$
Z_C^{(N)}
=
\int_{\mathcal J_C^{(N)}}
d\mu_N(q)
\exp
\left[
-\frac{{\rm Re}\,\mathcal S_N[q]}{\hbar}
\right].
$$

## 3. Resposta de holonomia

A resposta normalizada é:

$$
\langle\mathcal H(C)\rangle_N
=
e^{i\Theta_C}
\frac{Z_C^{(N)}}{Z_0^{(N)}}.
$$

No limite de Laplace:

$$
-\hbar\log
\left|
\langle\mathcal H(C)\rangle_N
\right|
=
\Delta S_{\rm cl}(C)
+\frac\hbar2
\log
\frac{\det{}'\mathcal H_C^{(N)}}
{\det{}'\mathcal H_0^{(N)}}
+O(\hbar^2).
$$

## 4. Tensão efetiva

Por localidade ao longo do tubo e gap transversal:

$$
\frac\hbar2
\log
\frac{\det{}'\mathcal H_C}
{\det{}'\mathcal H_0}
=
\delta\sigma\,A_{\min}(C)
+\delta\mu\,P(C)
+o(A).
$$

Defina:

$$
\sigma_{\rm eff}
=
\sigma_{\rm cl}
+\delta\sigma
+O(\hbar^2).
$$

## 5. Existência do limite de área

Se duas superfícies grandes são coladas ao longo de bordo de comprimento
$L_\partial$, a localidade dá:

$$
F(A_1+A_2)
\le
F(A_1)+F(A_2)+cL_\partial,
$$

onde:

$$
F(A)
:=
-\hbar\log|Z_C/Z_0|.
$$

Para retângulos com razão de aspecto limitada, o termo de bordo dividido pela
área tende a zero. O argumento subaditivo garante:

$$
\sigma_{\rm eff}
=
\lim_{A\to\infty}
\frac{F(A)}{A}.
$$

Se $\sigma_{\rm eff}>0$, então:

$$
\left|
\langle\mathcal H(C)\rangle
\right|
=
\exp
\left[
-\frac{\sigma_{\rm eff}}{\hbar}A_{\min}(C)
-\frac{\mu_{\rm eff}}{\hbar}P(C)
+o(A)
\right].
$$

Para $C_{R,T}$ retangular:

$$
V(R)
=
-\lim_{T\to\infty}
\frac\hbar T
\log
\left|
\langle\mathcal H(C_{R,T})\rangle
\right|
=
\sigma_{\rm eff}R+O(1).
$$

## 6. Status

A lei de área é teorema condicional da GDQ sob:

1. existência da thimble tubular;
2. sela isolada com $\sigma_{\rm cl}>0$;
3. Hessiana física com gap transversal;
4. limite espectral preservando localidade e subaditividade.

Isso é suficiente para o fechamento estrutural deste setor. Não é uma construção
matemática completa do problema Clay de Yang--Mills puro.
