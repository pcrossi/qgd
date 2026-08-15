---
title: "Delayed choice as boundary"
---

# Delayed choice as boundary

## Statement

Delayed choice is a temporal change of the apparatus boundary, not sending a physical signal to the past.

## Formulation

The apparatus realizes an impedance:

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

The final registration depends on the causal history via:

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

The kernel $w(t_f,t)$ must have causal support:

$$
w(t_f,t)=0
\quad
\text{if }t>t_f.
$$

## Interpretation

What changes is the effective boundary value problem:

$$
(\Omega,\partial\Omega_{\rm old})
\to
(\Omega,\partial\Omega_{\rm new}).
$$

This alters the final registration without requiring physical retrocausality.
