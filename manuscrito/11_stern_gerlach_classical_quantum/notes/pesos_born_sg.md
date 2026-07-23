---
title: "Pesos Born no Stern-Gerlach"
---

# Pesos Born no Stern-Gerlach

## Enunciado

Para preparação $\mathbf a$ e aparelho em eixo $\mathbf n$:

$$
p_\pm(\mathbf n|\mathbf a)
=
\frac{1\pm\mathbf a\cdot\mathbf n}{2}.
$$

## Prova

Escreva:

$$
\varrho_{\mathbf a}
=
\frac12(I+\mathbf a\cdot\sigma),
$$

e:

$$
P_{\mathbf n}^{\pm}
=
\frac12(I\pm\mathbf n\cdot\sigma).
$$

Pela regra operacional:

$$
p_\pm
=
\operatorname{Tr}(\varrho_{\mathbf a}P_{\mathbf n}^{\pm}).
$$

Multiplicando:

$$
\varrho_{\mathbf a}P_{\mathbf n}^{\pm}
=
\frac14
\left(
I
\mathbf a\cdot\sigma
\pm\mathbf n\cdot\sigma
\pm(\mathbf a\cdot\sigma)(\mathbf n\cdot\sigma)
\right).
$$

Usando:

$$
\operatorname{Tr}I=2,
\qquad
\operatorname{Tr}\sigma_i=0,
\qquad
\operatorname{Tr}(\sigma_i\sigma_j)=2\delta_{ij},
$$

resulta:

$$
p_\pm
=
\frac14(2\pm2\mathbf a\cdot\mathbf n)
=
\frac{1\pm\mathbf a\cdot\mathbf n}{2}.
$$

Se $\mathbf a\cdot\mathbf n=\cos\theta$:

$$
p_+=\cos^2\frac\theta2,
\qquad
p_-=\sin^2\frac\theta2.
$$

## Alcance

Os pesos vêm da regra operacional de Born no setor físico. A GDQ fornece a
estrutura geométrica dos projetores e a interação de contorno do aparelho.
