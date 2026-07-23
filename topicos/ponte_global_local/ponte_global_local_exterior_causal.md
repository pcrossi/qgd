# Ponte global--local — exterior Berger com relógio distinguido

## 1. Escolha causal e escopo

A Questão 2 seleciona a forma-relógio em um círculo de $T^4$. Para não
confundir a coordenada radial $s$ com o tempo físico, decompõe-se

$$
T^4=S^1_{\theta_0}\times T^3.
$$

Na seção cosmológica $s=s_H$, a imersão causal local é

$$
\iota_t(t,\mathbf x)
=\left(
\theta_0=\Omega t,
\theta_i=k_ix^i,
s=s_H,
p_{S^3}=p_0
\right).
$$

Com a forma-relógio $d\theta_0$, a normalização por tempo próprio dá

$$
\Omega=A_0(s_H)^{-1},
\qquad
\xi=A_0(s_H)^{-1}\partial_{\theta_0}.
$$

Essa construção é local. Sua extensão global requer o recobrimento universal
do círculo-relógio ou a reconstrução OS. Esse ponto não é ocultado na redução.

## 2. Ansatz causal mínimo

O ansatz anterior usava um único warp para $T^4$ e não permitia variar o
comprimento temporal mantendo o volume espacial fixo. O ansatz mínimo é

$$
g_+
=N^2ds^2
+A_0^2d\theta_0^2
+A_s^2g_{T^3}
+a^2(\sigma_1^2+\sigma_2^2)
+c^2\sigma_3^2.
$$

Defina

$$
x_0=\log A_0,
\quad
x_s=\log A_s,
\quad
y=\log a,
\quad
z=\log c,
$$

e a derivada própria $\dot X=N^{-1}X'$. A medida radial é

$$
\mathscr V=e^{x_0+3x_s+2y+z-u}.
$$

## 3. Torção derivada

Com

$$
\omega=e^{12}+e^{34}+e^{58}+e^{67},
$$

onde $e^1=A_0d\theta_0$ e $e^{2,3,4}=A_sd\theta_{2,3,4}$, resulta

$$
\boxed{
H
=-(\dot x_0+\dot x_s)e^8\wedge e^{12}
-2\dot x_s e^8\wedge e^{34}
+2(\dot y-e^{z-2y})e^{678}.
}
$$

Na convenção tensorial vigente,

$$
\boxed{
|H|^2
=6\left[(\dot x_0+\dot x_s)^2
+4\dot x_s^2
+4(\dot y-e^{z-2y})^2\right].
}
$$

Para $x_0=x_s=x$, recupera-se exatamente
$48\dot x^2+24(\dot y-e^{z-2y})^2$.

## 4. Curvatura

O escalar de Levi--Civita é

$$
\begin{aligned}
R_{\rm LC}={}&
-2\ddot x_0-6\ddot x_s-4\ddot y-2\ddot z\\
&-2\dot x_0^2-12\dot x_s^2-6\dot y^2-2\dot z^2\\
&-6\dot x_0\dot x_s-4\dot x_0\dot y-2\dot x_0\dot z\\
&-12\dot x_s\dot y-6\dot x_s\dot z-4\dot y\dot z\\
&+8e^{-2y}-2e^{2z-4y}.
\end{aligned}
$$

## 5. Ação oficial reduzida

Após a integração por partes completa,

$$
I_+=\int ds\,N\mathscr V
\left[\tau\mathcal K_C+u-4-\lambda_N\right],
$$

com

$$
\mathcal K_C=\mathcal K_{C,2}
+4E\dot y+8e^{-2y}-4E^2,
\qquad E=e^{z-2y},
$$

e

$$
\begin{aligned}
\mathcal K_{C,2}={}&
-\frac12\dot x_0^2+\frac72\dot x_s^2
+5\dot x_0\dot x_s\\
&+4\dot x_0\dot y+2\dot x_0\dot z
+12\dot x_s\dot y+6\dot x_s\dot z
+4\dot y\dot z\\
&-2\dot u\dot x_0-6\dot u\dot x_s
-4\dot u\dot y-2\dot u\dot z
+\dot u^2+\dot v^2.
\end{aligned}
$$

Substituir $x_0=x_s=x$ recupera exatamente o funcional Berger anterior.

## 6. Restrição e momentos

A restrição do lapse é

$$
\boxed{
\mathcal C_N
=\tau\left(8e^{-2y}-4E^2-\mathcal K_{C,2}\right)
+u-4-\lambda_N=0.
}
$$

Os momentos são obtidos diretamente de $\mathcal K_C$. Em particular,

$$
\boxed{
p_0
=\tau\mathscr V
(-\dot x_0+5\dot x_s+4\dot y+2\dot z-2\dot u).
}
$$

Esse momento inclui a contribuição torsional porque foi calculado depois de
substituir $H=d_J^c\omega$ na ação oficial. Portanto ele não importa uma
energia de Einstein--Hilbert.

Definindo

$$
r_0=\frac{p_0}{\tau\mathscr V},
\quad
r_s=\frac{p_s}{\tau\mathscr V},
\quad
r_y=\frac{p_y}{\tau\mathscr V}-4E,
\quad
r_z=\frac{p_z}{\tau\mathscr V},
\quad
r_u=\frac{p_u}{\tau\mathscr V},
$$

a inversão exata é

$$
\dot x_0=-\frac{11}{32}r_0+\frac1{32}r_s-\frac14r_u,
$$

$$
\dot x_s=\frac1{32}r_0-\frac3{32}r_s-\frac14r_u,
$$

$$
\dot y=-\frac18r_y-\frac14r_u,
\qquad
\dot z=-\frac12r_z-\frac12r_u,
$$

$$
\dot u=-\frac14r_0-\frac14r_s-\frac14r_y
-\frac12r_z-\frac32r_u.
$$

## 7. Energia como resposta ao período causal

Se a coordenada $\theta_0$ possui período coordenado $\ell_0$, seu
comprimento próprio na fronteira é

$$
\beta_E=\ell_0A_0(s_H).
$$

Mantendo os demais dados induzidos fixos, a variação on shell satisfaz

$$
\delta I_{\rm on}
=p_0^{\rm full}\,\delta x_0
=\frac{p_0^{\rm full}}{\beta_E}\,\delta\beta_E.
$$

Logo a energia euclidiana relativa do setor reduzido é

$$
\boxed{
\mathcal H_\xi^{\rm red}
=\frac{p_0^{\rm full}-p_{0,\rm ref}^{\rm full}}{\beta_E}.
}
$$

A referência deve possuir a mesma métrica induzida, topologia e polarização
de fronteira. O sinal lorentziano é fixado pela continuação causal e pela
convenção de energia positiva. Essa fórmula coincide com a derivada térmica
$\partial I_{\rm on}/\partial\beta_E$ e inclui o setor torsional reduzido.

O vínculo energético no modelo causal reduzido passa a ser

$$
\boxed{
\mathcal C_E^{\rm red}
=\frac{p_0^{\rm full}-p_{0,\rm ref}^{\rm full}}{\beta_E}-E_H=0.
}
$$

## 8. Limite da derivação

Essa construção fecha $\mathcal C_E$ no ansatz estacionário com $J$ fixo e
relógio toroidal distinguido. Ela ainda é condicional a:

1. levantamento global do círculo-relógio ou equivalência OS;
2. estacionariedade do peso depois da integração em $\gamma$;
3. escolha da referência com os mesmos dados de bordo;
4. inclusão dos modos $\delta J$ e não homogêneos na Hessiana física final.

Ela não autoriza identificar o Hamiltoniano radial com energia física.
