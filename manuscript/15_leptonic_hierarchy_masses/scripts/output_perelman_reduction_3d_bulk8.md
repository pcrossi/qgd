---
title: "Output — Perelman 3D reduction in the 8D bulk"
---

# Output — Perelman 3D reduction in the 8D bulk

## Input

| quantity | value |
|---|---:|
| dimension of the curved factor $B_3$ | `3` |
| dimension of the spectator factor $K_5$ | `5` |
| $\|\operatorname{Ric}(g_K)\|$ | `0.0` |
| $\|\nabla_K f\|$ | `0.0` |
| $\|H_{BK}\|$ | `0.0` |

## Verified Identity

For $g_8=g_B\oplus g_K$, it holds:

$$
\operatorname{Ric}(g_8)
=
\operatorname{Ric}(g_B)\oplus\operatorname{Ric}(g_K).
$$

With $\operatorname{Ric}(g_K)=0$, the flow on the spectator factor freezes:

$$
\partial_\tau g_K=0.
$$

The admissible singularity has a product form:

$$
\Sigma_{\rm sing}^{(8)}
=
\Sigma_{\rm sing}^{(3)}\times K_5.
$$

## Verdict

- valid product sector: `True`;
- Perelman is used only on the curved three-dimensional factor;
- the torus classifies holonomy/charge/phase, but does not generate the surgery.
