# Ponte global--local — exterior cosmológico Berger completo

## 1. Necessidade

O DtN interno possui quatro traços

$$
(a,c,u,v).
$$

Um exterior com $S^3$ redondo imporia $a=c$ na interface e removeria por
hipótese o modo anisotrópico de Berger. Para testar sua estabilidade, o
exterior deve preservar os dois raios.

## 2. Métrica e variáveis

Use

$$
g_+
=N^2ds^2+A^2g_{T^4}
+a^2(\sigma_1^2+\sigma_2^2)
+c^2\sigma_3^2.
$$

Defina

$$
x=\log A,
\qquad
y=\log a,
\qquad
z=\log c,
$$

e

$$
\dot X=N^{-1}X'.
$$

A densidade radial é

$$
\mathscr V=e^{4x+2y+z-u}.
$$

## 3. Estrutura Hermitiana e torção

Com

$$
\omega=e^{12}+e^{34}+e^{58}+e^{67},
$$

a torção dependente é

$$
\boxed{
H
=-2\dot x\,e^8\wedge(e^{12}+e^{34})
+2\left(\dot y-e^{z-2y}\right)e^{678}.
}
$$

Logo,

$$
\boxed{
|H|^2
=48\dot x^2
+24\left(\dot y-e^{z-2y}\right)^2.
}
$$

Para $x=$ constante, essa expressão reduz exatamente à torção do colar
Berger já derivada.

## 4. Curvatura

O escalar de Levi--Civita é

$$
\boxed{
\begin{aligned}
R_{\rm LC}
=\;&-8\ddot x-4\ddot y-2\ddot z
-20\dot x^2-6\dot y^2-2\dot z^2\\
&-16\dot x\dot y-8\dot x\dot z-4\dot y\dot z\\
&+8e^{-2y}-2e^{2z-4y}.
\end{aligned}
}
$$

No limite $x=$ constante, coincide com o escalar do colar Berger.

## 5. Funcional de primeira ordem

Depois da integração por partes variacionalmente completa,

$$
I_+
=\int ds\,N\mathscr V
\left[
\tau\mathcal K_B+u-4-\lambda_N
\right],
$$

onde

$$
\mathcal K_B
=\mathcal K_{B,2}
+4e^{z-2y}\dot y
+8e^{-2y}-4e^{2z-4y},
$$

e

$$
\boxed{
\begin{aligned}
\mathcal K_{B,2}
=\;&8\dot x^2
+16\dot x\dot y
+8\dot x\dot z
+4\dot y\dot z\\
&-8\dot u\dot x
-4\dot u\dot y
-2\dot u\dot z
+\dot u^2+\dot v^2.
\end{aligned}
}
$$

Impondo $z=y$, recupera-se exatamente o funcional isotrópico anterior.

## 6. Restrição do lapse

Defina

$$
V_B=8e^{-2y}-4e^{2z-4y}.
$$

A variação de $N$ fornece

$$
\boxed{
\mathcal C_N
=\tau\left(V_B-\mathcal K_{B,2}\right)
+u-4-\lambda_N=0.
}
$$

## 7. Momentos

Os momentos canônicos são

$$
p_x
=\tau\mathscr V
(16\dot x+16\dot y+8\dot z-8\dot u),
$$

$$
p_y
=\tau\mathscr V
(16\dot x+4\dot z-4\dot u+4e^{z-2y}),
$$

$$
p_z
=\tau\mathscr V
(8\dot x+4\dot y-2\dot u),
$$

$$
p_u
=\tau\mathscr V
(-8\dot x-4\dot y-2\dot z+2\dot u),
$$

$$
p_v=2\tau\mathscr V\dot v.
$$

## 8. Inversão exata

Defina

$$
r_x=\frac{p_x}{\tau\mathscr V},
\qquad
r_y=\frac{p_y}{\tau\mathscr V}-4e^{z-2y},
$$

$$
r_z=\frac{p_z}{\tau\mathscr V},
\qquad
r_u=\frac{p_u}{\tau\mathscr V}.
$$

A matriz possui determinante $-512$. Sua inversa fornece

$$
\boxed{
\dot x=-\frac1{16}r_x-\frac14r_u,
}
$$

$$
\boxed{
\dot y=-\frac18r_y-\frac14r_u,
}
$$

$$
\boxed{
\dot z=-\frac12r_z-\frac12r_u,
}
$$

$$
\boxed{
\dot u=-\frac14r_x-\frac14r_y-\frac12r_z-\frac32r_u,
}
$$

$$
\boxed{
\dot v=\frac{p_v}{2\tau\mathscr V}.
}
$$

## 9. Equações dos momentos

Com

$$
E=e^{z-2y},
\qquad
F=\tau\mathcal K_B+u-4-\lambda_N,
$$

obtém-se

$$
\boxed{
\dot p_x=4\mathscr V F,
}
$$

$$
\boxed{
\dot p_y
=\mathscr V
\left[
2F+\tau\left(
-8E\dot y-16e^{-2y}+16E^2
\right)
\right],
}
$$

$$
\boxed{
\dot p_z
=\mathscr V
\left[
F+\tau\left(4E\dot y-8E^2\right)
\right],
}
$$

$$
\boxed{
\dot p_u=\mathscr V(1-F),
\qquad
\dot p_v=0.
}
$$

## 10. Correspondência de traços com o DtN interno

Na interface, os traços comuns são

$$
(a,c,u,v)=(e^y,e^z,u,v).
$$

O warp toroidal $x$ é um traço exterior adicional. Sua condição conjugada
vem da conservação da tensão global no $T^4$, não do DtN normal de quatro
dimensões.

Os momentos devem ser convertidos pela regra de cadeia:

$$
\Pi_a^+=\frac{p_y}{a},
\qquad
\Pi_c^+=\frac{p_z}{c},
$$

$$
\Pi_u^+=p_u,
\qquad
\Pi_v^+=p_v.
$$

A colagem livre exige

$$
\boxed{
\Pi_A^-+\Pi_A^+=0,
\qquad A\in\{a,c,u,v\}.
}
$$

## 11. Status

$$
\boxed{
\text{exterior Berger completo derivado e compatível com os quatro traços
do DtN interno.}
}
$$

O próximo passo é implementar este sistema, validar a restrição e construir o
resíduo de colagem de duas interfaces.
