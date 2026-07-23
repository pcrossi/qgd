---
title: "No-go do produto local e do colar Berger"
---

# No-go do produto local e do colar Berger

Esta nota registra resultados negativos que não devem ser perdidos. Eles
impedem repetir ansätze que já foram excluídos.

## 1. Produto local não transporta $3/8$

Considere:

1. junction $C_3$ com classe de fluxo primitiva conservada;
2. background produto $T^5\times S^3$;
3. perfis constantes no toro;
4. interface radial $r=R(1+\varepsilon Y)$ com $Y=x_4$;
5. geradores normalizados de $SU(2)_L$ e $U(1)_Y$.

No junction:

$$
J_{\theta r}=0.
$$

Então:

$$
H_{\rm eff}
=
H_{\rm rel}
-
J_{\theta r}K_r^{-1}J_{\theta r}^{\dagger}
=
H_{\rm rel}.
$$

Na interface $\ell=1$, o peso depende apenas de $x_4$. Pela isotropia
residual:

$$
I_{W_1}=I_{W_2}=I_{W_3}=I_Y.
$$

No toro com perfis constantes, a medida normalizada fornece um fator comum.
Logo:

$$
Z_W=Z_Y.
$$

Portanto:

$$
\sin^2\theta_W=\frac38.
$$

O ansatz produto/local não gera o transporte até $2/9$.

## 2. Berger homogêneo é instável

Na métrica de Berger:

$$
ds^2=R^2(\sigma_1^2+\sigma_2^2+q^2\sigma_3^2),
$$

o extremo homogêneo fica em:

$$
q=1.
$$

Mas a Hessiana reduzida do modo de squashing possui:

$$
H_q^{\rm eff}
=
-2{,}67090856<0.
$$

Portanto, o modo Berger homogêneo é uma instabilidade real. A quártica positiva
do modo eletrofraco $\ell=1$ estabiliza $\beta$, mas não estabiliza
automaticamente o squashing métrico comum $q$.

## 3. Colar dinâmico com interface disponível

Na redução cohomogeneidade um:

$$
ds^2
=
N(r)^2dr^2
+a(r)^2(\sigma_1^2+\sigma_2^2)
+c(r)^2\sigma_3^2,
\qquad
q(r)=\frac{c(r)}{a(r)}.
$$

Com torção fechada:

$$
B=h(r)\sigma_1\wedge\sigma_2\wedge\sigma_3,
\qquad
dB=0,
$$

temos:

$$
h'(r)=0.
$$

As condições naturais de bordo atualmente derivadas são:

$$
\Pi_a=\Pi_c=\Pi_f=0.
$$

Elas implicam:

$$
a'=c'=f'=0.
$$

Assim, sem um pullback métrico--dilatônico adicional de interface, o colar
seleciona o cilindro homogêneo. Nesse cilindro:

$$
H_q^{\rm total}=-2{,}67090856<0.
$$

Além disso, o modo fotônico radial é constante. Em colar infinito:

$$
\|\Psi_\gamma\|^2=\infty,
$$

e o modo não fica localizado.

## 4. Elemento ausente

O objeto matemático ausente é:

$$
I_{\rm int}^{(a,c,f)}.
$$

Isto é, o pullback métrico--dilatônico da colagem global do estômato. Ele
deve fornecer condições Robin para $(a,c,f)$ derivadas da ação oficial e do
contorno global. Escolher seus coeficientes numericamente seria nova hipótese
constitutiva.

## 5. Status

Esse no-go não reabre a quebra eletrofraca. Ele delimita a metrologia fina:
para prever $\alpha_{\rm EW}$, localização fotônica e transporte $2/9$ em
sentido forte, é necessário um background global não produto com Hessiana de
contorno derivada.

## 6. Verificação computacional

O script:

$$
{\tt scripts/no_go_berger_colar.py}
$$

reproduz os valores de diagnóstico: $Z_W/Z_Y=1$, $\sin^2\theta_W=3/8$ no
produto local, $H_q^{\rm eff}<0$ e a divergência linear da norma fotônica no
colar infinito.
