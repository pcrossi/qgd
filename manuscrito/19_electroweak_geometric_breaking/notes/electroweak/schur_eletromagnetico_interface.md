---
title: "Schur eletromagnético de interface"
---

# Schur eletromagnético de interface

O dado externo eletromagnético $A$ e o traço interno $x$ da interface podem
ser escritos pela energia quadrática:

$$
S_{\rm col}^{(2)}
=
\frac12K_0x^2
+
\frac12K_\partial(A-x)^2.
$$

Na base $(x,A)$:

$$
\mathbb H_{\rm EM}
=
\begin{pmatrix}
K_0+K_\partial & -K_\partial\\
-K_\partial & K_\partial
\end{pmatrix}.
$$

Eliminando $x$ por complemento de Schur:

$$
K_{\rm EM}^{\rm eff}
=
K_\partial
-
K_\partial(K_0+K_\partial)^{-1}K_\partial.
$$

Logo:

$$
\boxed{
K_{\rm EM}^{\rm eff}
=
\frac{K_0K_\partial}{K_0+K_\partial}.
}
$$

Definindo a admitância de superfície:

$$
\mathcal S_\partial
=
\frac{K_0}{K_\partial},
$$

temos:

$$
K_{\rm EM}^{\rm eff}
=
\frac{K_0}{1+\mathcal S_\partial}.
$$

Com:

$$
\mathcal S_\partial
=
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right),
$$

obtém-se:

$$
\frac{K_{\rm EM}^{\rm eff}}{K_0}
=
0{,}966590303209.
$$

Esse bloco é teorema condicional: a álgebra de Schur está fechada; a
identificação constitutiva completa de $\mathcal S_\partial$ com a segunda
variação direta da ação oficial permanece refinamento metrológico.
