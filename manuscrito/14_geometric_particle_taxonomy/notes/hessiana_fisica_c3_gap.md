---
title: "Hessiana física C3 e gap reduzido"
---

# Hessiana física C3 e gap reduzido

Esta nota explicita o bloco de estabilidade usado na seleção de três
estômatos. O cálculo é reduzido, mas deriva do procedimento variacional
correto da GDQ: ação oficial, vínculo de Noether, Hessiana, projeção física e
complemento de Schur.

## 1. Variáveis coletivas

No junction $C_3$, escreva as tensões horizontais como:

$$
\mathbf T_a
=
T(\cos\theta_a,\sin\theta_a),
\qquad
a=1,2,3.
$$

O vínculo de fluxo é:

$$
\mathcal C(\theta)
=
\sum_{a=1}^{3}\mathbf T_a.
$$

O equilíbrio simétrico é:

$$
\theta_a=\theta_0+\frac{2\pi(a-1)}{3}.
$$

## 2. Hessiana vinculada

O funcional aumentado é:

$$
\widetilde{\mathcal S}
=
\mathcal S_{\rm GDQ}
+\boldsymbol\lambda\cdot\mathcal C.
$$

Linearizando o vínculo:

$$
D\mathcal C
=
T
\begin{pmatrix}
-\sin\theta_1&-\sin\theta_2&-\sin\theta_3\\
\cos\theta_1&\cos\theta_2&\cos\theta_3
\end{pmatrix}.
$$

A segunda variação vinculada no setor angular é:

$$
H_\theta
=
\kappa_{\rm rel}
(D\mathcal C)^\dagger D\mathcal C.
$$

No ponto $C_3$:

$$
\operatorname{spec}H_\theta
=
\kappa_{\rm rel}T^2
\left\{
0,\frac32,\frac32
\right\}.
$$

O autovalor zero é a rotação global simultânea. O projetor físico remove esse
modo:

$$
P_{\rm phys}
=
I
-
\frac13
\mathbf 1\mathbf 1^\top.
$$

Logo:

$$
P_{\rm phys}^\top H_\theta P_{\rm phys}
=
\frac32\kappa_{\rm rel}T^2 I_2.
$$

## 3. Modo radial homogêneo e Schur

O modo radial homogêneo preservando a classe primitiva tem rigidez:

$$
K_\perp^{(r,0)}
=
\frac{3}{2\tau}I_3.
$$

A conservação da classe de fluxo elimina o acoplamento angular--radial no
setor físico:

$$
J_{\theta r}=0.
$$

Assim, o complemento de Schur é:

$$
H_{\rm eff}
=
H_{\rm rel}
-
J_{\theta r}
\left(K_\perp^{(r,0)}\right)^{-1}
J_{\theta r}^{\dagger}
=
H_{\rm rel}.
$$

## 4. Modos não homogêneos

No preenchimento gaussiano reduzido, os modos não homogêneos do operador de
Hessiana métrico-dilatônico entram pelo operador de Ornstein--Uhlenbeck:

$$
L_f=-\Delta_f.
$$

Seu espectro normalizado é:

$$
\operatorname{spec}L_f
=
\left\{
\frac{m}{2\tau}
:
m=0,1,2,\ldots
\right\}.
$$

Depois de remover os modos de simetria e normalização, o primeiro modo físico
não homogêneo é:

$$
\lambda_{\rm nh}
=
\frac{1}{2\tau}.
$$

Portanto, na normalização $T=1$, $\kappa_{\rm rel}=1$:

$$
\lambda_{\rm gap}^{C_3}
=
\min
\left\{
\frac32,
\frac{1}{2\tau}
\right\}.
$$

Para $\tau=1$:

$$
\lambda_{\rm gap}^{C_3}=\frac12.
$$

## 5. Status

O resultado fecha a estabilidade no setor reduzido horizontal e no
preenchimento gaussiano físico projetado. Ele não afirma que todo background
cosmológico misto foi diagonalizado; afirma que a contagem local por três
estômatos não possui instabilidade no bloco que a seleciona.

## 6. Verificação computacional

O script:

$$
{\tt scripts/hessiana_fisica_c3_gap.py}
$$

calcula explicitamente o espectro angular, o projetor físico, o bloco radial,
o complemento de Schur e o gap reduzido.
