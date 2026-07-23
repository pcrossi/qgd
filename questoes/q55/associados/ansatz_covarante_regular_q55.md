# Q55 — Ansatz covariante regular para buracos negros GDQ

## Objetivo

Registrar o modelo covariante mínimo que substitui o balanço newtoniano legado
por uma construção compatível com a emergência macroscópica de Einstein da
Q54.

## Métrica efetiva

No setor esfericamente simétrico estático, use

$$
ds^2
=
-e^{2\Phi(r)}A(r)c^2dt^2
+A(r)^{-1}dr^2
+r^2d\Omega^2,
$$

com

$$
A(r)
=
1-\frac{2Gm(r)}{c^2r}.
$$

A função de massa é definida por

$$
m'(r)
=
\frac{4\pi r^2}{c^2}\epsilon_{\rm GDQ}(r),
$$

onde $\epsilon_{\rm GDQ}$ é a energia efetiva média da densidade, fase,
torção e pressão geométrica derivadas da equação métrica ponderada.

## Condições de regularidade no centro

Para evitar singularidade em $r=0$, exige-se

$$
\epsilon_{\rm GDQ}(r)
=
\epsilon_0+O(r^2),
$$

logo

$$
m(r)
=
\frac{4\pi\epsilon_0}{3c^2}r^3+O(r^5).
$$

Assim,

$$
A(r)
=
1-\frac{\Lambda_{\rm core}}{3}r^2+O(r^4),
$$

com

$$
\Lambda_{\rm core}
=
\frac{8\pi G}{c^4}\epsilon_0.
$$

O centro é de Sitter/anti-colapso efetivo, não Schwarzschild singular.

## Invariantes de curvatura no core

No limite regular:

$$
R(0)=4\Lambda_{\rm core},
$$

$$
R_{\mu\nu}R^{\mu\nu}(0)
=
4\Lambda_{\rm core}^2,
$$

$$
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}(0)
=
\frac83\Lambda_{\rm core}^2.
$$

Todos são finitos se $\epsilon_0$ é finito.

## Horizonte

Horizontes são raízes de

$$
A(r_H)=0.
$$

Equivalente a

$$
r_H
=
\frac{2Gm(r_H)}{c^2}.
$$

Se $m(r)\to M$ para $r$ grande, o horizonte externo tende a

$$
r_+
\simeq
\frac{2GM}{c^2}.
$$

Dependendo do core, pode haver horizonte interno $r_-$ e um limite extremal
onde

$$
A(r_*)=0,
\qquad
A'(r_*)=0.
$$

## Temperatura efetiva

Para horizonte não degenerado:

$$
T_H
=
\frac{\hbar c}{4\pi k_B}
e^{\Phi(r_H)}
\left|A'(r_H)+2A(r_H)\Phi'(r_H)\right|.
$$

Como $A(r_H)=0$:

$$
T_H
=
\frac{\hbar c}{4\pi k_B}
e^{\Phi(r_H)}
\left|A'(r_H)\right|.
$$

No limite extremal $A'(r_*)=0$:

$$
T_H\to0.
$$

## Classificação

Este ansatz é uma redução efetiva covariante. Ele não é a solução final da
ação oficial. A solução final exige derivar $\epsilon_{\rm GDQ}(r)$,
$p_r(r)$, $p_t(r)$ e $\Phi(r)$ diretamente da equação métrica ponderada e da
Hessiana física do background de colapso.

