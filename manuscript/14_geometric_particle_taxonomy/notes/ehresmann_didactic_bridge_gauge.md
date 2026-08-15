---
title: "Ehresmann connection as a didactic bridge for effective gauge"
---

# Ehresmann connection as a didactic bridge for effective gauge

This note preserves an intuitive way of reading gauge fields as internal gluing geometry. It is a didactic bridge, not a new fundamental action.

Consider locally a toroidal fiber with angular coordinates $\theta^a$. Without coupling, the vertical 1-forms are simply

$$
d\theta^a.
$$

An Ehresmann connection separates horizontal and vertical directions by means of modified forms

$$
\boxed{
\Theta^a=d\theta^a+g_aA^a.
}
$$

Here $A^a=A_\mu^adx^\mu$ is the local component of the effective connection seen in the projected space, and $g_a$ is the normalization of the respective channel. Under a local change of trivialization of the fiber,

$$
\theta^a\mapsto\theta^a-\lambda^a(x),
$$

we have

$$
d\theta^a\mapsto d\theta^a-d\lambda^a.
$$

For $\Theta^a$ to remain geometrically well-defined, the connection must transform as

$$
A^a\mapsto A^a+\frac{1}{g_a}d\lambda^a.
$$

This is the usual gauge transformation in the reduced abelian sector. In the non-abelian case, the same idea is replaced by a connection on an internal vector bundle:

$$
A_\mu
=
G_\mu^aT_a
+
W_\mu^it_i
+
B_\mu Y.
$$

The physical point is that gauge appears as the freedom to choose internal frames and horizontals without altering the geometric observables. This fits the definition used in the chapter:

$$
G_{\rm eff}
=
\operatorname{Aut}_{\rm GDQ}(E_{\rm int}).
$$

Therefore, the language of Ehresmann can help visualize the geometric origin of $A_\mu$, but the foundation remains:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast
\to
K_{\rm phys}
\to
\text{reconstructed effective connections}.
$$
