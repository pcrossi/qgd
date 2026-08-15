---
title: "Spectral transport of the Weinberg angle"
---

# Spectral transport of the Weinberg angle

This note separates the common geometric point from the operational value after transport. It also records the numerical comparison used only as a diagnostic.

## 1. Common point

At the common geometric point inherited from the internal taxonomy:

$$
I_2=2,
\qquad
I_Y=\frac{10}{3}.
$$

Thus:

$$
\frac{g'^2}{g^2}
=
\frac35,
$$

and:

$$
\sin^2\theta_W
=
\frac{g'^2}{g^2+g'^2}
=
\frac38.
$$

This value is the local correspondence. It should not be forced to be the operational value measured at another scale.

## 2. Differential transport

If the stiffnesses are transported by factors $Z_W$ and $Z_Y$:

$$
\frac1{g_{\rm EW}^2}
=
Z_W\frac1{g_{\rm match}^2},
$$

$$
\frac1{g_{\rm EW}'{}^2}
=
Z_Y\frac1{g_{\rm match}'{}^2},
$$

then:

$$
\frac{g_{\rm EW}'{}^2}{g_{\rm EW}^2}
=
\frac35\frac{Z_W}{Z_Y}.
$$

The operational value:

$$
\sin^2\theta_W=\frac29
$$

is equivalent to:

$$
\frac{g'^2}{g^2}=\frac27.
$$

Thus the necessary and sufficient condition is:

$$
\boxed{
\frac{Z_W}{Z_Y}
=
\frac{10}{21}.
}
$$

This is a transport condition. It does not alter the official action and must not be imposed as a target.

## 3. Reduced spectral transport

In the reduced model, the stiffnesses are read as heat traces of the Hessian:

$$
K_a(s)
=
C_{\rm GDQ}{\rm Tr}
\left(
T_a^2e^{-s\mathcal O_a}
\right).
$$

The reduced spectral calculation shows the transition:

$$
\frac38
\longrightarrow
\frac29
$$

at:

$$
s_\ast=5{,}9090386\times10^6.
$$

The parameter $s$ is dimensionless. The associated resolution scale is:

$$
\frac{Q_\ast}{\Lambda_0}
=
\frac1{\sqrt{s_\ast}}
=
4{,}113784964\times10^{-4}.
$$

With the internal operator calibration:

$$
\Lambda_0=126354{,}3162\,{\rm GeV},
$$

it follows:

$$
Q_\ast=51{,}97944877\,{\rm GeV}.
$$

This number is a semigroup resolution scale, not automatically a particle mass.

## 4. W/Z comparison

With:

$$
v=246{,}111195996\,{\rm GeV},
$$

and the conditional identity:

$$
\alpha_{\rm EW}^{-1}=132{,}457669,
\qquad
\sin^2\theta_W=\frac29,
$$

we obtain:

$$
m_W=80{,}403325\,{\rm GeV},
$$

$$
m_Z=91{,}168801\,{\rm GeV}.
$$

Comparing with the reference values used in the diagnostic:

$$
m_W^{\rm ref}=80{,}379\,{\rm GeV},
\qquad
m_Z^{\rm ref}=91{,}1876\,{\rm GeV},
$$

the errors are approximately:

$$
\delta_W=+0{,}0303\%,
\qquad
\delta_Z=-0{,}0206\%.
$$

## 5. Status

Spectral transport is a quantitatively strong path. The final metrological closure requires deriving $Z_W/Z_Y$ and $\alpha_{\rm EW}$ directly from the global boundary Hessian, without using $m_W$ or $m_Z$ as targets.

## 6. Computational verification

The script:

$$
{\tt scripts/conditional\_weinberg\_transport.py}
$$

calculates the condition $Z_W/Z_Y=10/21$, the scale $Q_\ast$, the W/Z values, and the relative errors.
