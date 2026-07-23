---
title: "Normalização cinética do modo de Hopf"
---

# Normalização cinética do modo de Hopf

Esta nota registra a normalização interna do modo eletrofraco. Ela separa o
que é integral interna fechada do que depende da conversão dimensional global.

## 1. Flutuação torsional carregada

No elo $S^3$, tome um harmônico $\ell=1$:

$$
-\Delta_{S^3}Y=\lambda_1Y,
\qquad
\lambda_1=\frac3{R^2}.
$$

A normalização usada é:

$$
\langle Y^2\rangle=\frac14.
$$

A flutuação torsional eletrofraca é:

$$
\delta B_{\rm EW}
=
\beta(x)Y\,{\rm vol}_{S^3}.
$$

Como $Y$ tem média zero, a 3-forma é exata no setor ortogonal ao fluxo
homogêneo. Um potencial de 2-forma é:

$$
\mathcal A_{\rm EW}
=
-\frac1{\lambda_1}*_{3}dY.
$$

Então:

$$
d\mathcal A_{\rm EW}
=
Y\,{\rm vol}_{S^3}
$$

na convenção de sinal adotada.

## 2. Norma interna

Pela identidade espectral:

$$
\langle|dY|^2\rangle
=
\lambda_1\langle Y^2\rangle.
$$

Logo:

$$
\left\langle
|\mathcal A_{\rm EW}|^2
\right\rangle
=
\frac{\langle Y^2\rangle}{\lambda_1}
=
\frac{R^2}{12}.
$$

Para:

$$
R=1{,}998411184770,
$$

obtemos:

$$
\left\langle
|\mathcal A_{\rm EW}|^2
\right\rangle
=
0{,}332804.
$$

## 3. Termo cinético efetivo

Quando $\beta$ varia no espaço-tempo físico:

$$
B
=
d[\beta(x)\mathcal A_{\rm EW}]
=
d_4\beta\wedge\mathcal A_{\rm EW}
+\beta Y\,{\rm vol}_{S^3}.
$$

Integrando o espaço interno com a medida oficial normalizada:

$$
Z_\beta
=
C_{\rm GDQ}\tau\frac{R^2}{12},
$$

onde:

$$
C_{\rm GDQ}
=
\frac{\hbar}{\Lambda_C^2}\mathfrak C_\gamma.
$$

O campo canônico reduzido é:

$$
\Phi_c=\sqrt{Z_\beta}\,\beta.
$$

Portanto:

$$
v=\sqrt{Z_\beta}\,\beta_\ast.
$$

## 4. Limite do resultado

A integral interna está fechada:

$$
\frac{Z_\beta}{C_{\rm GDQ}}
=
\tau\frac{R^2}{12}.
$$

Mas a conversão para GeV exige a normalização dimensional e causal global. O
capítulo usa a escala reduzida já registrada:

$$
v
=
m_p\frac{6\pi^5}{7}
=
246{,}111195996\,{\rm GeV}.
$$

Essa separação evita usar $G_F$ ou $m_W$ como entrada para definir $v$.

## 5. Verificação computacional

O script:

$$
{\tt scripts/normalizacao\_cinetica\_hopf.py}
$$

calcula $\lambda_1$, $\langle|\mathcal A_{\rm EW}|^2\rangle$ e
$Z_\beta/C_{\rm GDQ}$.
