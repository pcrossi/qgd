---
title: "Nota — Escala eletrofraca e raio do próton"
---

# Nota — Escala eletrofraca e raio do próton

A escala eletrofraca geométrica candidata é:

$$
v_{\rm GDQ}
=
M_p\frac{6\pi^5}{7}.
$$

Ela é a normalização dimensional global do modo eletrofraco. O modo
adimensional vem do potencial:

$$
\mathcal V(\beta)
=
\frac12a_2\beta^2
+
\frac14a_4\beta^4,
$$

com:

$$
\beta_\ast^2
=
-\frac{a_2}{a_4}.
$$

Para:

$$
a_2=-0.253196676,
\qquad
a_4=2133.554507,
$$

obtém-se:

$$
\beta_\ast=0.0108937431.
$$

A conexão dimensional é:

$$
v=\sqrt{Z_\beta}\,\beta_\ast.
$$

Ela deve ser distinguida da fórmula auxiliar:

$$
v_K
=
\frac{M_e}{\alpha}
\left(
1-\frac{3}{4\pi^2}
\right)^{-1/2},
$$

que produz apenas uma escala de dezenas de MeV.

No nível reduzido atual:

$$
v_{\rm GDQ}
=
246.111195996\,{\rm GeV},
$$

com erro de $-0.044048\%$ contra a escala operacional extraída de $G_F$.

O raio estrutural do próton é:

$$
r_p^{\rm surf}
=
\frac18
\left(
1+\frac{\alpha}{4}
\right)
\epsilon_{\rm eff}
\frac{3\Lambda_C}{2}.
$$

Essa expressão vem da decomposição:

$$
r_p^{\rm surf}
=
C_r\epsilon_{\rm eff}R_B,
$$

com:

$$
C_r
=
\frac18
\left(
1+\frac{\alpha}{4}
\right),
\qquad
R_B
=
\frac32\Lambda_C.
$$

Para:

$$
\alpha^{-1}=137.035999084,
\qquad
\epsilon_{\rm eff}=0.011591040463,
\qquad
\Lambda_C=386.159268\,{\rm fm},
$$

temos:

$$
C_r=0.125228042267790,
\qquad
R_B=579.238902\,{\rm fm},
$$

e:

$$
\boxed{
r_p^{\rm surf}
=
0.840778765432\,{\rm fm}.
}
$$

## Fórmula de contração descartada

A fórmula multiplicativa auxiliar:

$$
0.8778\times0.07479\times10^{-3}\times3.7915
$$

fornece:

$$
0.000248914485\,{\rm fm},
$$

e não $0.0369\,{\rm fm}$. O fator de erro é:

$$
\frac{0.0369}{0.000248914485}
=
148.243683.
$$

Logo essa rota não deve ser usada como derivação quantitativa do puzzle do
raio do próton.

## Fator de forma e raio observado

O raio de carga observado por espalhamento é definido pela inclinação do fator
de forma:

$$
F_p(q^2)
=
1-\frac{q^2r_p^2}{6}
+O(q^4).
$$

O tamanho finito em estados $ns$ entra por:

$$
\Delta E_{\rm fs}(ns)
=
\frac{2\pi}{3}
Z\alpha\hbar c\,
r_p^2
|\psi_{ns}(0)|^2.
$$

Como:

$$
|\psi_{ns}(0)|^2
=
\frac{(Z\alpha\mu c/\hbar)^3}{\pi n^3},
$$

segue:

$$
\Delta E_{\rm fs}(ns)
\propto
\mu^3r_p^2.
$$

Essa é a razão estrutural pela qual o hidrogênio muônico é muito mais sensível
ao raio do próton que o hidrogênio eletrônico.

O raio medido por uma sonda é:

$$
r_p^{\rm eff}[\ell]
=
r_p^{\rm surf}
+
\delta r_p[\ell],
$$

com:

$$
\delta r_p[\ell]
=
-
\left(H_p^{\rm surf}\right)^{-1}J_{p,\ell}.
$$

Assim, diferenças entre hidrogênio eletrônico e muônico pertencem ao problema
de interface sonda--próton.

No limite de contato dos estados $s$:

$$
\frac{\delta r_p[e]}{\delta r_p[\mu]}
=
\left(
\frac{\mu_{ep}}{\mu_{\mu p}}
\right)^3
=
1.555489846615637\times10^{-7}.
$$

O fechamento metrológico fino exige calcular diretamente
$H_p^{\rm surf}$, $J_{p,e}$ e $J_{p,\mu}$ da ação oficial, sem ajustar esses
blocos por um raio experimental.
