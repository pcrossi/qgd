---
title: "Exact derivatives, endpoint states and causal continuation"
---

# Exact derivatives, endpoint states and causal continuation

If

$$
L'=L+\frac{dF(q,t)}{dt},
$$

then

$$
S'[q]=S[q]+F(q_1,t_1)-F(q_0,t_0).
$$

The Lorentzian kernel transforms as

$$
K'(q_1,t_1;q_0,t_0)
=e^{iF(q_1,t_1)/\hbar}
K(q_1,t_1;q_0,t_0)
e^{-iF(q_0,t_0)/\hbar}.
$$

Therefore, equivalence does not consist in ignoring the term: the boundary vectors must undergo the conjugate transformation. In operator notation,

$$
U'(t_1,t_0)
=V(t_1)U(t_1,t_0)V(t_0)^{-1},
$$

with

$$
V(t)=e^{iF(t)/\hbar}.
$$

After continuation to a Euclidean parameter, the factors may cease to be unitary. This makes it indispensable to also transport the domain, the states, and the reflection condition. Concluding only that "the factor became real" is not enough to prove gauge breaking.
