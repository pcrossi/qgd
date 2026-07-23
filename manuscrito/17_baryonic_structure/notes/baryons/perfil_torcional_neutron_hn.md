---
title: "Perfil torsional variacional do nêutron"
---

# Perfil torsional variacional do nêutron

## 1. Objetivo

O nêutron tem carga total nula:

$$
G_E^n(0)=0.
$$

Mas isso não implica densidade elétrica interna nula. Na GDQ, o nêutron é uma
configuração bariônica com estômato invertido e cisalhamento torsional
antiparalelo. O perfil elétrico de baixa energia deve, portanto, ser obtido
como resposta de superfície.

## 2. Coordenada local de superfície

Usa-se a coordenada normal ao estômato:

$$
\xi=r-r_p.
$$

A distância física é a projeção de superfície:

$$
r=r_p+\xi.
$$

## 3. Fonte torsional estacionária

A separação torsional líder é:

$$
\xi_+
=
-\frac12r_p\alpha_{\rm tor}^{(2)},
\qquad
\xi_-
=
\frac12r_p\alpha_{\rm tor}^{(2)}.
$$

com:

$$
\alpha_{\rm tor}^{(2)}
=
2\alpha\ln(2\pi^2).
$$

A amplitude é fixada pelo momento magnético do nêutron:

$$
A_n=|\mu_n|.
$$

## 4. Problema variacional

O perfil suave é a solução do fluxo de calor de Perelman na camada de
superfície:

$$
\left(
\partial_\tau-\partial_\xi^2
\right)
H_n(\xi,\tau)
=
0.
$$

Com condição inicial dipolar:

$$
H_n(\xi,0)
=
|\mu_n|
\left[
\delta(\xi-\xi_+)
-
\delta(\xi-\xi_-)
\right].
$$

Logo:

$$
H_n(\xi,\tau_n)
=
|\mu_n|
\left[
K_{\tau_n}(\xi,\xi_+)
-
K_{\tau_n}(\xi,\xi_-)
\right],
$$

onde:

$$
K_\tau(\xi,\xi_0)
=
\frac1{\sqrt{4\pi\tau}}
\exp
\left[
-\frac{(\xi-\xi_0)^2}{4\tau}
\right].
$$

A largura natural escolhida pela separação torsional é:

$$
\sigma_r
=
\sqrt{2\tau_n}
=
\frac12r_p\alpha_{\rm tor}^{(2)}.
$$

## 5. Fator de forma

O fator elétrico do nêutron no nível líder é:

$$
G_E^n(q^2)
=
\int
H_n(\xi,\tau_n)
j_0(q(r_p+\xi))
d\xi.
$$

Como os dois núcleos têm mesma massa total e sinais opostos:

$$
\int H_n d\xi=0,
$$

então:

$$
G_E^n(0)=0.
$$

O raio quadrático segue da expansão de $j_0$:

$$
j_0(qr)
=
1-\frac{q^2r^2}{6}+O(q^4).
$$

Assim:

$$
-6
\left.
\frac{dG_E^n}{dq^2}
\right|_0
=
\int H_n(\xi,\tau_n)(r_p+\xi)^2d\xi.
$$

No limite líder:

$$
\langle r_n^2\rangle
=
-2|\mu_n|\alpha_{\rm tor}^{(2)}r_p^2.
$$

## 6. Significado físico

O perfil $H_n$ fecha carga nula e inclinação de baixa energia. Ele não deve ser
confundido com o fator de forma completo medido por espalhamento: a sonda
eletromagnética também possui impedância de superfície.

Script:

[[../../scripts/perfil_torcional_neutron|perfil_torcional_neutron.py]]

Saída:

[[../../scripts/saida_perfil_torcional_neutron|Saída — perfil torsional do nêutron]].
