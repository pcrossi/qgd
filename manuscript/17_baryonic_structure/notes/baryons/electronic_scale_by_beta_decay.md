---
title: "Electronic scale by beta decay"
---

# Electronic scale by beta decay

This note records an important metrological consequence of the reduced baryonic construction.

In the baryonic sector, masses are obtained in electronic units:

$$
\frac{M_p}{M_e},
\qquad
\frac{M_n}{M_e}.
$$

The neutron–proton difference is:

$$
\frac{M_n-M_p}{M_e}
=
\delta_B.
$$

Since free beta decay has endpoint:

$$
Q_\beta
=
M_n-M_p-M_e,
$$

it follows that:

$$
Q_\beta
=
(\delta_B-1)M_ec^2.
$$

Thus:

$$
M_ec^2
=
\frac{Q_\beta}{\delta_B-1}.
$$

With:

$$
\delta_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5}
\Delta \simeq
2.530825921868,
$$

and using the experimental free beta endpoint as a metrological boundary condition:

$$
Q_\beta
\simeq
0.78233356\,{\rm MeV},
$$

we obtain:

$$
M_ec^2
\simeq
0.51105325\,{\rm MeV}.
$$

Compared to the reference value:

$$
M_ec^2_{\rm ref}
=
0.51099895\,{\rm MeV},
$$

the relative error is:

$$
\frac{0.51105325-0.51099895}{0.51099895}
\simeq
1.06\times10^{-4}.
$$

## Physical Reading

This is not an absolute prediction of a unit from nothing. The endpoint $Q_\beta$ is a physical boundary/metrological datum. What GDQ provides is the geometric bridge:

$$
\delta_B-1,
$$

which converts the beta endpoint into the electronic scale.

Therefore, the correct status is:

$$
\boxed{
\text{metrological determination of the electronic scale by beta endpoint.}
}
$$

It is stronger than simply choosing $M_e$ as a unit, but remains dependent on the experimental datum $Q_\beta$.

Self-contained verification:
[[../../scripts/output_electronic_scale_beta|Output — electronic scale by beta]].
