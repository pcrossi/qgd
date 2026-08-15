---
title: "Neutron lifetime and alpha minus 11"
---

# Neutron lifetime and $\alpha^{-11}$

This note records the reduced derivation of the total neutron lifetime in the unpolarized sector. The result is conditional because it uses the contracted norm of the beta channel, not the complete differential separation of the coefficients.

## 1. Phase Space

The reduced phase space is:

$$
I_\beta
=
\int_{m_e}^{\Delta M}
p_eE_e(\Delta M-E_e)^2\,dE_e,
\qquad
p_e=\sqrt{E_e^2-m_e^2}.
$$

With:

$$
m_e=0.51099895069\,{\rm MeV},
\qquad
\Delta M=1.29333251\,{\rm MeV},
$$

we obtain:

$$
I_\beta
=
5.700456936530352\times10^{-17}\,{\rm GeV}^5.
$$

The preserved script calculates this value using both an analytical formula and Simpson's rule. At refinement $N=80000$, the relative error against the analytical formula is:

$$
1.377\times10^{-8}.
$$

## 2. Total Rate

The total rate is:

$$
\Gamma_n
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}I_\beta.
$$

With:

$$
\mathcal J_3^2
=
\frac{15\pi^3}{16}
\frac{\alpha^{11}m_ec^2}{I_\beta}.
$$

It follows that:

$$
\Gamma_n
=
\frac{15}{32}
\alpha^{11}
\frac{m_ec^2}{\hbar}.
$$

Therefore:

$$
\tau_n
=
\frac{32}{15}
\alpha^{-11}
\frac{\hbar}{m_ec^2}.
$$

Using:

$$
\alpha^{-1}=137.035999177,
$$

results in:

$$
\Gamma_n
=
1.137140542406870\times10^{-3}\,{\rm s}^{-1},
$$

$$
\tau_n
=
879.398775004012\,{\rm s},
$$

and:

$$
T_{1/2}
=
609.552781481901\,{\rm s}.
$$

## 3. Comparison

With the reference:

$$
\tau_n^{\rm ref}
=
878.3\pm0.4\,{\rm s},
$$

the deviation is:

$$
\Delta\tau
=
1.098775004\,{\rm s},
$$

that is:

$$
\frac{\Delta\tau}{\tau_n^{\rm ref}}
\simeq
1.25\times10^{-3}.
$$

In units of the error $0.4\,{\rm s}$:

$$
\frac{\Delta\tau}{0.4\,{\rm s}}
\simeq
2.75.
$$

With the alternative reference $878.4\pm0.5\,{\rm s}$, the deviation is close to $2.0\sigma$.

## 4. Physical Reading

This closure is for the total reduced rate. It does not replace the complete differential calculation of angular correlations, recoil, and surface terms.

The distinction is:

$$
\boxed{
\text{total rate depends on }\mathcal J_3^2;
\qquad
\text{differential observables depend on }C_S,C_T.
}
$$

Self-contained verification:
[[../../scripts/output_validate_free_beta_complete|Output — beta decay validation GDQ]].
