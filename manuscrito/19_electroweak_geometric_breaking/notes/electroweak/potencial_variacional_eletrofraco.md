---
title: "Potencial variacional da a quebra eletrofraca geométrica"
---

# Potencial variacional da a quebra eletrofraca geométrica

Seja $\Phi_\ast$ um background simétrico admissível e $\Phi_{\rm EW}$ uma
direção física da Hessiana. A família de teste é:

$$
\mathfrak G(\varphi)
=
\Phi_\ast+\varphi\Phi_{\rm EW}.
$$

O potencial efetivo é apenas a ação restrita:

$$
S_{\rm eff}(\varphi)
=
\mathcal S_{\rm GDQ}[\mathfrak G(\varphi)].
$$

Expandindo:

$$
S_{\rm eff}
=
S_0
+
\frac12a_2|\varphi|^2
+
\frac14a_4|\varphi|^4
+
O(|\varphi|^6).
$$

O termo quadrático é:

$$
a_2
=
\langle\Phi_{\rm EW},K_{\rm phys}\Phi_{\rm EW}\rangle.
$$

Com:

$$
K_{\rm phys}
=
P_{\rm phys}\delta^2\mathcal S_{\rm GDQ}[\Phi_\ast]P_{\rm phys}.
$$

O termo quartico é a quarta variação física na mesma direção, depois de
respeitar vínculos de volume, fluxo e interface:

$$
a_4
=
\delta^4\mathcal S_{\rm GDQ}
[
\Phi_{\rm EW},
\Phi_{\rm EW},
\bar\Phi_{\rm EW},
\bar\Phi_{\rm EW}
]_{\rm phys}.
$$

O mínimo existe se:

$$
a_2<0,
\qquad
a_4>0.
$$

Na normalização adotada:

$$
|\varphi_\ast|^2
=
-\frac{a_2}{a_4}.
$$

Quando a variável é escrita como dupleto efetivo:

$$
\langle\Phi\rangle
=
\frac1{\sqrt2}
\begin{pmatrix}
0\\
v
\end{pmatrix},
$$

temos:

$$
v^2
=
-\frac{2a_2}{a_4}
$$

após fixar a normalização cinética correspondente.

## Certificação Lean

O módulo
[ElectroweakStability.lean](../../../../formal/GDQ/ElectroweakStability.lean)
formaliza a completação do quadrado:

$$
V(\beta)
=
\frac{a_4}{4}
\left(
\beta^2+\frac{a_2}{a_4}
\right)^2
-
\frac{a_2^2}{4a_4}.
$$

Para $a_4>0$, o último termo é a cota inferior global. Se
$a_2<0<a_4$, existe $\beta_\ast>0$ com:

$$
\beta_\ast^2=-\frac{a_2}{a_4},
$$

que satura a cota e possui energia estritamente menor que $\beta=0$. O
enunciado Lean recebe $a_2$ e $a_4$ como coeficientes da Hessiana e da quarta
variação já calculadas; ele não os escolhe por um alvo experimental.
