---
title: "Hartman como comprimento próprio saturado"
---

# Hartman como comprimento próprio saturado

Status: teorema reduzido condicional.

## Hipóteses

1. barreira unidimensional estacionária;
2. modo evanescente dominante;
3. transversais congeladas;
4. fluxo propagante real suprimido dentro da barreira;
5. calibre longitudinal fixado pela densidade;
6. normalização na interface.

## Prova

O modo evanescente tem:

$$
\rho(x)=\rho_0e^{-2\kappa x}.
$$

No setor reduzido:

$$
g_{xx}(x)=g_0\rho(x)/\rho_0.
$$

Portanto:

$$
ds=\sqrt{g_0}e^{-\kappa x}dx.
$$

Integrando:

$$
D_{\rm prop}(L)
=
\int_0^Lds
=
\frac{\sqrt{g_0}}{\kappa}
\left(1-e^{-\kappa L}\right).
$$

Logo:

$$
\lim_{L\to\infty}D_{\rm prop}(L)
=
\frac{\sqrt{g_0}}{\kappa}.
$$

Se a velocidade própria reduzida é limitada por $v_0\le c$:

$$
\tau_{\rm GDQ}(L)
=
\frac{D_{\rm prop}(L)}{v_0}
$$

também satura.

## Alcance

Isso explica a saturação geométrica. Não prova que uma frente causal atravessa
a barreira mais rápido que a luz. A comparação experimental depende do
observável temporal escolhido.
