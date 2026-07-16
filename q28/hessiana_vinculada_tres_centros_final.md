# Q28 — Hessiana vinculada do background simétrico de três centros

## 1. Interfaces, não bordas externas

Os três estômatos são interfaces internas produzidas pela cirurgia. Portanto,
não se introduzem três impedâncias Robin livres. Os campos são colados com
continuidade e o vínculo de Noether correlaciona os fluxos normais.

No setor primitivo,

$$
\mathcal C=\sum_{a=1}^{3}\mathbf T_a=0,
\qquad
|\mathbf T_a|=T.
$$

O funcional aumentado é

$$
\widetilde{\mathcal S}
=\mathcal S_{\rm GDQ}
+\boldsymbol\lambda\cdot\mathcal C.
$$

## 2. Bloco relativo

Para

$$
\mathbf T_a=T(\cos\theta_a,\sin\theta_a),
$$

o Jacobiano do vínculo é

$$
D\mathcal C
=T
\begin{pmatrix}
-\sin\theta_1&-\sin\theta_2&-\sin\theta_3\\
\cos\theta_1&\cos\theta_2&\cos\theta_3
\end{pmatrix}.
$$

No equilíbrio $C_3$,

$$
(\theta_1,\theta_2,\theta_3)
=(0,2\pi/3,4\pi/3).
$$

A Hessiana vinculada angular é

$$
H_\theta
=\kappa_{\rm rel}(D\mathcal C)^\dagger D\mathcal C.
$$

Seu espectro é

$$
\operatorname{spec}H_\theta
=\kappa_{\rm rel}T^2\{0,3/2,3/2\}.
$$

Removendo a rotação comum,

$$
\boxed{
H_{\rm rel}
=\frac32\kappa_{\rm rel}T^2I_2.
}
$$

O produto $\kappa_{\rm rel}T^2$ é a unidade física de rigidez do fluxo
primitivo. Na normalização topológica $T=1$ e na normalização da forma
quadrática de Noether, $\kappa_{\rm rel}=1$.

## 3. Bloco transversal disponível

O modo homogêneo do raio, calculado diretamente da ação oficial, possui

$$
\lambda_{r,0}=\frac{3}{2\tau}.
$$

Para os três centros idênticos,

$$
\boxed{
K_\perp^{(r,0)}
=\frac{3}{2\tau}I_3>0.
}
$$

## 4. Bloco misto

O fluxo primitivo é uma classe topológica preservada pelas flutuações físicas.
Consequentemente,

$$
\delta_rT_a=0.
$$

Além disso, o background equilátero satisfaz $\mathcal C=0$. A derivada mista
do termo quadrático de fechamento é, portanto,

$$
\boxed{J_{\theta r}=0.}
$$

Isso não é uma escolha numérica: decorre da conservação da classe de fluxo e
da avaliação no ponto fechado.

## 5. Complemento de Schur

No setor multicítrico simétrico calculável,

$$
H_{\rm eff}
=H_{\rm rel}
-J_{\theta r}(K_\perp^{(r,0)})^{-1}J_{\theta r}^\dagger
=H_{\rm rel}.
$$

Logo,

$$
\boxed{
\operatorname{spec}H_{\rm eff}
=\kappa_{\rm rel}T^2\{3/2,3/2\}>0.
}
$$

O modo radial homogêneo também é positivo. Assim, o background de três
centros é estável contra as duas deformações relativas e contra as três
flutuações radiais homogêneas.

## 6. Alcance exato

Este cálculo fecha a Hessiana vinculada do **background simétrico de três
centros nos setores que definem e podem desestabilizar a contagem**:

1. modos angulares relativos;
2. rotação comum removida;
3. modos radiais homogêneos;
4. mistura angular--radial.

Modos métricos não homogêneos de comprimento de onda arbitrário continuam
pertencendo ao problema espectral geral da ação, mas não alteram a contagem
$N=3$ enquanto o operador transversal gauge-fixado permanecer não negativo.
Eles não devem ser confundidos com os modos coletivos do junction calculados
aqui.
