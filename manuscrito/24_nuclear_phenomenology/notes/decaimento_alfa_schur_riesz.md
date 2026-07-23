---
title: "Nota — Decaimento alfa por Schur e Riesz"
---

# Nota — Decaimento alfa por Schur e Riesz

Considere a segunda variação física da ação oficial no background nuclear:

$$
\delta^2\mathcal S_{\rm GDQ}
=
\frac12
\left\langle
\begin{pmatrix}
\delta\Phi_I\\
\delta\Phi_\partial
\end{pmatrix},
\begin{pmatrix}
K_{II} & K_{I\partial}\\
K_{\partial I} & K_{\partial\partial}
\end{pmatrix}
\begin{pmatrix}
\delta\Phi_I\\
\delta\Phi_\partial
\end{pmatrix}
\right\rangle.
$$

No cálculo de canal, os modos internos são eliminados variacionalmente:

$$
\frac{\delta}{\delta\Phi_I}
\delta^2\mathcal S_{\rm GDQ}
=
0.
$$

Logo:

$$
K_{II}\delta\Phi_I
+
K_{I\partial}\delta\Phi_\partial
=
0,
$$

e:

$$
\delta\Phi_I
=
-
K_{II}^{-1}
K_{I\partial}\delta\Phi_\partial.
$$

Substituindo na forma quadrática:

$$
\delta^2\mathcal S_{\partial}
=
\frac12
\left\langle
\delta\Phi_\partial,
K_{\partial}^{\rm phys}
\delta\Phi_\partial
\right\rangle,
$$

com:

$$
K_{\partial}^{\rm phys}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

O projetor de canal é:

$$
P_\alpha
=
\frac{1}{2\pi i}
\oint_{\mathcal C_\alpha}
\left(z-K_{\partial}^{\rm phys}\right)^{-1}
\,dz.
$$

A energia de superfície é:

$$
E_{\partial}^{\rm GDQ}
=
\langle
P_\alpha(1-P_{\rm filho})\Phi_\alpha,
K_{\partial}^{\rm phys}
P_\alpha(1-P_{\rm filho})\Phi_\alpha
\rangle_\partial.
$$

Essa é a construção preservada. O cálculo reduzido usa matrizes pequenas para
avaliar esse esquema; o cálculo metrológico futuro deve substituir esses blocos
por operadores obtidos diretamente da Hessiana nuclear completa.

## Construção reduzida executada

Para evitar que a comparação alfa pareça apenas uma tabela ajustada, a versão
reduzida preservada constrói os blocos a partir de dados do canal:

$$
A,\quad Z,\quad Q_\alpha,
$$

e das grandezas geométricas:

$$
R_{\rm touch}
=
r_0\left((A-4)^{1/3}+4^{1/3}\right),
$$

$$
x_{\rm barrier}
=
\frac{2(Z-2)\alpha\hbar c}{R_{\rm touch}Q_\alpha}
-1,
$$

$$
\delta_{\rm touch}
=
\frac{R_{\rm touch}-r_0A^{1/3}}{r_0A^{1/3}},
$$

e:

$$
\chi_{\rm curv}
=
\frac{\delta_{\rm touch}^2}{x_{\rm barrier}}.
$$

A base positiva de impedância de superfície é:

$$
\mathcal I_\Sigma(x)
=
j_0^2\frac{x^2}{1+x}
+j_1^2\frac{x^2}{(1+x)^2}
+j_2^2\frac{x^3}{(1+x)^2}.
$$

Na normalização reduzida:

$$
K_{\partial\partial}
=
\operatorname{diag}
\left(
\frac{4\mathcal I_\Sigma(\chi_{\rm curv})}{\alpha},
1+s_{\rm shell},
1+x_{\rm barrier}
\right).
$$

O bloco interno é tomado positivo:

$$
K_{II}
=
\operatorname{diag}
\left(
1+x_{\rm barrier},
1+\frac{4\chi_{\rm curv}}{\alpha},
1+s_{\rm shell}
\right).
$$

O bloco cruzado $K_{I\partial}$ usa as mesmas correntes reduzidas
$j_0,j_1,j_2$ que entram em $\mathcal I_\Sigma$. Assim a retroação de Schur
não é um fator livre, mas a contração matricial:

$$
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

A rigidez de camada reduzida é:

$$
s_{\rm shell}
=
\frac{(A-4)^{2/3}}{D_{\rm shell}+(A-4)^{2/3}},
$$

onde:

$$
D_{\rm shell}
=
d_Z^2+d_N^2,
$$

e $d_Z,d_N$ são distâncias aos fechamentos gerados pelo operador angular
spin--torção, não por uma lista manual.

Depois de formar $K_\partial^{\rm phys}$, seleciona-se a banda com maior
overlap com o vetor primitivo alfa após remover o subespaço do filho:

$$
P_\perp
=
P_\alpha(1-P_{\rm filho}).
$$

A frequência de tentativa reduzida é:

$$
\nu_{\rm bounce}
=
\frac{c}{2R_{\rm touch}}
\sqrt{\frac{2Q_\alpha}{\mu}}.
$$

Com mobilidade de determinante:

$$
\nu_{\rm GDQ}
=
\nu_{\rm bounce}
\left(1+\lambda_\alpha\right)^{n_{\rm cl}/2},
$$

onde $n_{\rm cl}$ é o número de fechamentos exatos do núcleo filho em
prótons e nêutrons. Para $\mathrm{Po}$-$212\to\mathrm{Pb}$-$208+\alpha$,
$n_{\rm cl}=2$.

Por fim:

$$
\Gamma_{\rm GDQ}
=
\nu_{\rm GDQ}
\exp(-E_\partial^{\rm GDQ})
\exp(-W_{\rm rad}^{\rm GDQ}).
$$

Verificação autocontida:
[[../scripts/saida_alfa_pipeline_schur_riesz_reduzido|Saída — pipeline alfa Schur--Riesz reduzido]].
