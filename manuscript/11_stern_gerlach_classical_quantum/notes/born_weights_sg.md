---
title: "Born weights in Stern-Gerlach"
---

# Born weights in Stern-Gerlach

## Statement

For preparation $\mathbf a$ and apparatus along axis $\mathbf n$:

$$
p_\pm(\mathbf n|\mathbf a)
=
\frac{1\pm\mathbf a\cdot\mathbf n}{2}.
$$

## Proof

Write:

$$
\varrho_{\mathbf a}
=
\frac12(I+\mathbf a\cdot\sigma),
$$

and:

$$
P_{\mathbf n}^{\pm}
=
\frac12(I\pm\mathbf n\cdot\sigma).
$$

By the operational rule:

$$
p_\pm
=
\operatorname{Tr}(\varrho_{\mathbf a}P_{\mathbf n}^{\pm}).
$$

Multiplying:

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

Using:

$$
\operatorname{Tr}I=2,
\qquad
\operatorname{Tr}\sigma_i=0,
\qquad
\operatorname{Tr}(\sigma_i\sigma_j)=2\delta_{ij},
$$

it results:

$$
p_\pm
=
\frac14(2\pm2\mathbf a\cdot\mathbf n)
=
\frac{1\pm\mathbf a\cdot\mathbf n}{2}.
$$

If $\mathbf a\cdot\mathbf n=\cos\theta$:

$$
p_+=\cos^2\frac\theta2,
\qquad
p_-=\sin^2\frac\theta2.
$$

## Scope

The weights come from the operational Born rule in the physical sector. GDQ provides the geometric structure of the projectors and the boundary interaction of the apparatus.
