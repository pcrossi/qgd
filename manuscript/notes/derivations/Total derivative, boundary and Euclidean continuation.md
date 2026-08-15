---
title: "Total derivative, boundary and Euclidean continuation"
type: derivation
status: exact-identity-with-analytical-caution
---

# Total derivative, boundary and Euclidean continuation

## 1. Real action

Consider

$$
L'=L+\frac{dF(x,t)}{dt}.
$$

For a path with endpoints $(x_0,t_0)$ and $(x_1,t_1)$,

$$
S'[x]
=\int_{t_0}^{t_1}L'\,dt
=S[x]+F(x_1,t_1)-F(x_0,t_0).
$$

Thus,

$$
e^{iS'[x]/\hbar}
=e^{i(F_1-F_0)/\hbar}e^{iS[x]/\hbar}.
$$

The factor is independent of the path's interior but depends on the endpoints. For physical equivalence, boundary states and observables must receive the compatible transformation.

## 2. Continuation

Suppose $F(x,t)$ admits analytic continuation to $t=-i\tau$. Define the Euclidean action by the convention

$$
e^{iS/\hbar}\longrightarrow e^{-S_E/\hbar}.
$$

If the continued term $F_E$ is real, then

$$
S_E'=S_E+F_{E,1}-F_{E,0}
$$

and

$$
e^{-S_E'/\hbar}
=e^{-(F_{E,1}-F_{E,0})/\hbar}e^{-S_E/\hbar}.
```
The factor is real and can alter the apparent normalization of the kernel. If $F_E$ is not real, the separation between phase and damping will be different. Therefore, the nature of the term cannot be decided before specifying the continuation.

## 3. What remains invariant

The total derivative does not alter the Euler--Lagrange equations in the interior when variations of the endpoints are fixed. It can alter:

1. the generating functional on the boundary;
2. the natural conditions when the boundary varies;
3. the phase or normalization of the states;
4. the realization of the operator in the Euclidean domain.

Therefore, the correct conclusion is not that Wick "breaks the gauge". The conclusion is that the gauge equivalence must be continued jointly in the bulk, in the states, and on the boundary.
