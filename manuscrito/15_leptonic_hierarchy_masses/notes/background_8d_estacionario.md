---
title: "Background 8D estacionário da hierarquia"
---

# Background 8D estacionário da hierarquia

O background leptônico usado na elevação 8D do Capítulo 15 é o background
produto estacionário:

$$
g_8=g_B\oplus g_K,
\qquad
K_5=T^5.
$$

As hipóteses físicas são:

$$
\nabla_K f=0,
\qquad
H_{BK}=0,
\qquad
\mathcal C_{BK}=0.
$$

Aqui $\mathcal C_{BK}$ denota o bloco misto da conexão/métrica que mediria a
falha de produto. Portanto:

$$
a_W=\|\nabla_KA\|_\infty=0,
$$

$$
a_f=\|\nabla_Kf_K\|_\infty=0,
$$

$$
a_H=\|H_{BK}\|_\infty=0,
$$

$$
\varepsilon=\|\mathcal C_{BK}\|=0.
$$

O gap transversal físico é tomado como o menor gap conservador disponível no
setor reduzido:

$$
\lambda_B^{\rm gap}=\frac12.
$$

Com esses valores:

$$
m_\perp^2
=
C_\gamma\tau R_{\max}^{-2}
-
\left(c_Wa_W^2+c_fa_f^2+c_Ha_H^2+c_C\varepsilon^2\right)
>
0,
$$

e:

$$
j_{\rm mix}=b_Wa_W+b_fa_f+b_Ha_H+b_C\varepsilon=0.
$$

Logo:

$$
\Delta_{\rm Schur}
=
\frac{j_{\rm mix}^2}{m_\perp^2}
=
0.
$$

Isso prova que, no background produto estacionário, a elevação 8D não desloca
as razões leptônicas:

$$
R_\ell^{(8)}=R_\ell^{(0)}.
$$

O script correspondente é:

[[../scripts/background_8d_estacionario|background_8d_estacionario.py]]

e sua saída é:

[[../scripts/saida_background_8d_estacionario|Saída — background leptônico 8D estacionário]].
