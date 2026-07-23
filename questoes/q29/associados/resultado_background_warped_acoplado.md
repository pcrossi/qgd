# Q29 — Resultado do background warped acoplado

## Problema resolvido

Foram resolvidas simultaneamente as equações de Euler--Lagrange de $A$ e
$F=f-5A$ derivadas da ação oficial reduzida, acrescentando a variável de
normalização

$$
N'(\chi)=e^{-F}\sin^2\chi.
$$

As condições usadas foram

$$
F'(\epsilon)=0,
\qquad
A'(\pi)=0,
\qquad
F'(\pi)=0,
$$

$$
N(\epsilon)=0,
\qquad
N(\pi)=1.
$$

A condição de fluxo de $A$ no estômato não foi imposta adicionalmente: ela
foi verificada como consequência integrada da equação.

## Resultado numérico

Com

$$
R=1{,}998411184770,
\qquad
\tau=1,
\qquad
\epsilon=0{,}011591040463,
$$

o solver convergiu em $11943$ nós com resíduo RMS máximo
$1{,}87\times10^{-5}$. Obteve-se

$$
A(\epsilon)=-1{,}2731698873,
\qquad
F(\epsilon)=-5{,}2718635830,
$$

$$
A'(\epsilon)=76{,}3085234374,
\qquad
F'(\epsilon)=0.
$$

A retroação dilatônica reduz fortemente o gradiente encontrado na aproximação
$F=$ constante. O balanço integrado é

$$
e^{-F(\epsilon)}\sin^2\epsilon A'(\epsilon)
=1{,}9968236317
=\frac{R^2}{2\tau}N(\pi),
$$

dentro da tolerância numérica.

## Rigidez radial no bordo

A solução fornece

$$
\boxed{
\frac{p(\epsilon)}{C_{\rm GDQ}}
=1{,}43749050425\times10^{-4}.
}
$$

Com

$$
\frac{\kappa_\partial}{C_{\rm GDQ}}
=3{,}94950542527\times10^{-5},
$$

o fator Robin comum é

$$
\boxed{
\eta_0
=\frac{\kappa_\partial}{p(\epsilon)}
=0{,}274750018425.
}
$$

Logo,

$$
\eta_W=\eta_0\frac{g^2}{4},
\qquad
\eta_Z=\eta_0\frac{g^2+g'^2}{4},
\qquad
\eta_\gamma=0.
$$

No ponto geométrico comum da Q28,

$$
\eta_W=0{,}0167966110,
\qquad
\eta_Z=0{,}0268745776.
$$

Esses valores não usam massas experimentais. Eles são as entradas do solver
de Sturm--Liouville radial.

## Alcance

A normalização $N(\pi)=1$ absorve o volume toroidal no prefator comum. O
resultado é adequado para razões e para o problema radial reduzido. Uma
normalização dimensional cosmológica absoluta ainda deve restaurar o volume
de $T^5$, mas não altera $\kappa_\partial/p$ se bulk e interface forem
normalizados pela mesma ação.
