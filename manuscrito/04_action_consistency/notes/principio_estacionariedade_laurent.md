---
title: "Princípio de estacionariedade dos coeficientes de Laurent"
---

# Princípio de estacionariedade dos coeficientes de Laurent

Esta nota separa duas afirmações que não devem ser confundidas.

A primeira é uma identidade de contorno. A segunda é um princípio técnico de
reconstrução local usado quando se deseja obter equações diferenciais modo a
modo a partir da ação de contorno da GDQ.

## 1. O que a integral de contorno impõe sozinha

Considere uma variação já integrada no bulk espacial, escrita
esquematicamente como

$$
\delta S
=
\oint_\gamma
E(z_\tau)
\frac{dz_\tau}{z_\tau}.
$$

Suponha que, no anel onde o contorno $\gamma$ é tomado, o integrando admita
expansão de Laurent:

$$
E(z_\tau)
=
\sum_{k=-\infty}^{\infty}
E_kz_\tau^k.
$$

Então

$$
E(z_\tau)\frac{dz_\tau}{z_\tau}
=
\sum_{k=-\infty}^{\infty}
E_kz_\tau^{k-1}dz_\tau.
$$

Pelo teorema dos resíduos,

$$
\oint_\gamma
E(z_\tau)
\frac{dz_\tau}{z_\tau}
=
2\pi i\,E_0.
$$

Logo, a estacionariedade da integral de contorno implica apenas

$$
E_0=0.
$$

Ela não implica automaticamente

$$
E_k=0
\qquad
\forall k.
$$

## 2. Por que isso não basta para equações locais

Se somente $E_0=0$ fosse imposto, diferentes modos de Laurent poderiam
cancelar-se no contorno sem que cada coeficiente local fosse estacionário. Em
termos físicos, isso deixaria a ação estacionária apenas como média/resíduo
global ao longo de $\gamma$, mas não produziria equações locais independentes
para cada setor de escala causal.

Para obter uma dinâmica local, a GDQ adota o princípio suplementar:

$$
\boxed{
E_k=0
\quad
\forall k.
}
$$

Chamaremos isso de **princípio de estacionariedade dos coeficientes de
Laurent**.

## 3. Status lógico

Esse princípio é condicional e técnico. Ele não altera a ação oficial. Ele
declara qual classe de variações e soluções será aceita quando a teoria for
lida localmente a partir do contorno causal.

A hierarquia correta é:

$$
\mathcal S_{\rm GDQ}
\to
\delta S=0
\to
E_0=0
\quad
\text{pela integral de contorno},
$$

e, para reconstrução local,

$$
E_k=0
\quad
\forall k.
$$

Portanto, o princípio de Laurent não é novo termo dinâmico. Ele é uma condição
de resolução local do problema variacional de contorno.

