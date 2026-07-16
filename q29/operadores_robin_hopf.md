# Q29 — Operadores Robin derivados do modo de Hopf

## 1. Dado geométrico

O modo de ordem já construído é

$$
\Phi_{\rm EW}=\frac{\beta}{\sqrt2}u,
\qquad
u\in S^3\subset\mathbb C^2,
\qquad
u_0=\begin{pmatrix}0\\1\end{pmatrix}.
$$

Use os geradores

$$
T_i=\frac{\sigma_i}{2},
\qquad
Y=\frac{I_2}{2}.
$$

A Hessiana de interface restrita às direções de calibre é o Gram real dos
vetores $T_iu_0,Yu_0$:

$$
\mathsf B_{ab}
=\operatorname{Re}\langle T_au_0,T_bu_0\rangle.
$$

## 2. Matriz calculada

Na base $(W_1,W_2,W_3,B)$ sem absorver os acoplamentos,

$$
\boxed{
\mathsf B
=\frac14
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&1&-1\\
0&0&-1&1
\end{pmatrix}.
}
$$

Seu espectro é

$$
\operatorname{spec}\mathsf B
=\left\{0,\frac14,\frac14,\frac12\right\}.
$$

Logo, a Hessiana seleciona exatamente:

1. dois canais carregados degenerados;
2. um canal neutro rígido;
3. um canal neutro nulo.

## 3. Acoplamentos e fóton

Na base física $(W_3,B)$, os vetores entram como $(gW_3,g'B)$. O bloco
neutro é

$$
\mathsf B_0(g,g')
=\frac14
\begin{pmatrix}
g^2&-gg'\\
-gg'&g'^2
\end{pmatrix}.
$$

Portanto,

$$
\det\mathsf B_0=0.
$$

O kernel é a direção eletromagnética

$$
\begin{pmatrix}W_3\\B\end{pmatrix}_{\gamma}
\propto
\begin{pmatrix}g'\\g\end{pmatrix},
$$

enquanto a direção ortogonal é o canal $Z$. Isso deriva o fóton sem massa e
a matriz de massas sem importar um potencial de Higgs fundamental.

## 4. Condição Robin

Se $\kappa_\partial>0$ é a rigidez radial obtida pela projeção da Hessiana
oficial, o operador de contorno é

$$
\boxed{
\left(\nabla_n I_4+\kappa_\partial\mathsf B(g,g')\right)\Psi
\big|_{\chi=\epsilon}=0.
}
$$

Nos canais diagonalizados,

$$
\mathsf M_{\partial,\gamma}=0,
\qquad
\mathsf M_{\partial,W}=\frac{\kappa_\partial g^2}{4},
\qquad
\mathsf M_{\partial,Z}=\frac{\kappa_\partial(g^2+g'^2)}{4}.
$$

Aqui essas expressões devem ser entendidas como a matriz quadrática de
interface $\mathsf M_\partial$. Na condição Robin radial, a quantidade que
multiplica o campo é

$$
\mathsf R_a^{\rm Robin}
=p(\epsilon)^{-1}\mathsf M_{\partial,a},
$$

onde $p$ é a rigidez radial do bulk. Essa distinção dimensional é detalhada em
`q29/problema_sturm_liouville_wz.md`.

## 5. O que esse cálculo determina — e o que não determina

O pullback determina de forma intrínseca:

$$
m_\gamma=0,
\qquad
m_W^2\propto g^2,
\qquad
m_Z^2\propto g^2+g'^2,
$$

e, portanto, a estrutura da quebra. Contudo, ele não determina sozinho a
razão cinética $g'/g$: os símbolos $g,g'$ multiplicam os geradores antes do
pullback. Confundir essa matriz de massa com a matriz de rigidez cinética seria
circular.

O transporte deve vir da normalização dos perfis radiais solucionados com
esses contornos:

$$
\frac1{g_{a,4}^2}
=C_{\rm GDQ}\int_\epsilon^\pi
e^{-F+3A}\sin^2\chi\,|\Psi_a(\chi)|^2d\chi.
$$

O coeficiente comum foi posteriormente identificado pela normalização cinética
do próprio modo de Hopf:

$$
\kappa_\partial=Z_\beta\beta_*^2=v^2.
$$

Não se deve identificá-lo com $V''(\beta_*)$, que é a curvatura do modo radial.
A derivação está em `q29/separacao_rigidez_radial_robin.md`. Resta resolver o
Sturm--Liouville acoplado no background warped.
