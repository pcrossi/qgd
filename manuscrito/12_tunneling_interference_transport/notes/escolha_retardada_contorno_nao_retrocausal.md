---
title: "Escolha retardada como contorno"
---

# Escolha retardada como contorno

## Enunciado

Escolha retardada é mudança temporal do contorno do aparelho, não envio de
sinal físico para o passado.

## Formulação

O aparelho realiza uma impedância:

$$
\mathsf R_{\rm app}(t)
=
\mathsf R_{\rm off}
+
s(t-t_c)
\left(
\mathsf R_{\rm on}
-
\mathsf R_{\rm off}
\right).
$$

O registro final depende do histórico causal por:

$$
\Gamma_{\rm det}(t_f)
=
\frac12
\int
\langle
\Delta\Phi_\partial(t),
\mathsf R_{\rm app}(t)
\Delta\Phi_\partial(t)
\rangle
w(t_f,t)\,dt.
$$

O kernel $w(t_f,t)$ deve ter suporte causal:

$$
w(t_f,t)=0
\quad
\text{se }t>t_f.
$$

## Interpretação

O que muda é o problema de contorno efetivo:

$$
(\Omega,\partial\Omega_{\rm old})
\to
(\Omega,\partial\Omega_{\rm new}).
$$

Isso altera o registro final sem exigir retrocausalidade física.
