# Q29 — Normalização cinética do modo de Hopf

## 1. Reconstrução do potencial

A flutuação torsional interna é

$$
\delta B_{\rm EW}
=\beta(x)Y\operatorname{vol}_{S^3},
$$

com

$$
-\Delta Y=\lambda_1Y,
\qquad
\lambda_1=\frac3{R^2},
\qquad
\langle Y^2\rangle=\frac14.
$$

Como $Y$ tem média zero, a 3-forma é exata. Um potencial global no setor
ortogonal ao fluxo homogêneo é

$$
\boxed{
\mathcal A_{\rm EW}
=-\frac1{\lambda_1}*_{3}dY,
}
$$

de modo que

$$
d\mathcal A_{\rm EW}=Y\operatorname{vol}_{S^3}
$$

na convenção de sinal adotada.

## 2. Norma

Pela identidade espectral,

$$
\langle|dY|^2\rangle
=\lambda_1\langle Y^2\rangle.
$$

Portanto,

$$
\left\langle
|\mathcal A_{\rm EW}|^2
\right\rangle
=\frac{\langle Y^2\rangle}{\lambda_1}
=\frac{R^2}{12}.
$$

Para

$$
R=1{,}998411184770,
$$

isso fornece

$$
\boxed{
\left\langle|\mathcal A_{\rm EW}|^2\right\rangle
=0{,}332804.
}
$$

## 3. Termo cinético 4D

Quando $\beta$ depende das coordenadas físicas,

$$
B=d[\beta(x)\mathcal A_{\rm EW}]
=d_4\beta\wedge\mathcal A_{\rm EW}
+\beta Y\operatorname{vol}_{S^3}.
$$

Após integrar o espaço interno com a medida oficial normalizada, o coeficiente
cinético é

$$
\boxed{
Z_\beta
=C_{\rm GDQ}\,\tau\frac{R^2}{12},
\qquad
C_{\rm GDQ}=\frac{\hbar}{\Lambda_C^2}
\mathfrak C_\gamma,
}
$$

onde $\mathfrak C_\gamma$ representa a normalização real do contorno temporal
oficial. Os volumes de $T^5$ e $S^3$ não aparecem novamente porque
$\int\mathcal U_*dV=1$.

O campo canônico é

$$
\Phi_c=\sqrt{Z_\beta}\,\beta.
$$

Logo,

$$
\boxed{v=\sqrt{Z_\beta}\,\beta_*.}
$$

## 4. Resultado e dependência restante

A parte interna da normalização cinética está calculada exatamente. Para
$\tau=1$,

$$
\boxed{
\frac{Z_\beta}{C_{\rm GDQ}}
=0{,}332804.
}
$$

O valor em GeV ainda depende do prefator dimensional
$C_{\rm GDQ}=\hbar\mathfrak C_\gamma/\Lambda_C^2$. Portanto, confirmar
$v=246{,}111196\,\mathrm{GeV}$ exige usar a escala $\Lambda_C$ e a
normalização causal determinadas nas Q33/Q36/Q38. Essa dependência não pode
ser substituída pelo valor experimental de $G_F$.
