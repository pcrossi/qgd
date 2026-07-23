---
title: "Saída — background leptônico 8D estacionário"
---

# Saída — background leptônico 8D estacionário

## Classificação

Avaliação direta de quantidade já derivada no background estacionário
produto/bloco da GDQ. Não é engenharia inversa e não usa alvo
experimental.

## Background avaliado

$$
g_8=g_B\oplus g_K,
\qquad
K=T^5\text{ plano}.
$$

$$
A(k)=\text{constante},
\qquad
f_K(k)=\text{constante},
\qquad
H_{BK}=0,
\qquad
\mathcal C_{BK}=0.
$$

## Valores físicos extraídos

| quantidade | valor | origem |
|---|---:|---|
| $a_W=\|\nabla_K A\|_\infty$ | `0` | $A(k)$ constante |
| $a_f=\|\nabla_K f_K\|_\infty$ | `0` | $f_K(k)$ constante |
| $a_H=\|H_{BK}\|_\infty$ | `0` | torção sem bloco misto |
| $\varepsilon=\|\mathcal C_{BK}\|$ | `0` | métrica produto |
| $\lambda_B^{\rm gap}$ | `0.5` | menor gap físico conservador |

## Critério de Schur

$$
m_\perp^2
=
C_\gamma\tau R_{\max}^{-2}
-
\left(c_Wa_W^2+c_fa_f^2+c_Ha_H^2+c_C\varepsilon^2\right).
$$

$$
j_{\rm mix}=b_Wa_W+b_fa_f+b_Ha_H+b_C\varepsilon.
$$

- $m_\perp^2=1$;
- $j_{\rm mix}=0$;
- $\Delta_{\rm Schur}=0$.

$$
\frac{j_{\rm mix}^2}{m_\perp^2}
=
0
<
\frac12.
$$

## Massas relativas resultantes

| lépton | razão 8D |
|---|---:|
| $e$ | `1.000000000000000` |
| $\mu$ | `206.768593470628673` |
| $\tau$ | `3477.446405098381092` |

Como o complemento de Schur é nulo:

$$
R_\ell^{(8)}=R_\ell^{(0)}.
$$
