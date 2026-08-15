---
title: "Galactic critical acceleration"
---

# Galactic critical acceleration

This note derives the critical acceleration scale used in the galactic limit of GDQ. The objective is not to postulate MOND, but to show how a MOND-like scale appears when the global cosmological boundary is projected onto the local circulation channel.

## 1. Geometric data

The global datum is the Hubble radius:

$$
R_H
=
\frac{c}{H_0}.
$$

This radius is not a local constant of the soliton. It is a boundary condition of the cosmological problem.

The horizon scale is:

$$
a_H
=
cH_0
=
\frac{c^2}{R_H}.
$$

The relevant local channel for a stationary radial response is circular. The complete circulation has angular length $2\pi$. Therefore, the acceleration per projected cycle is:

The circular response per cycle is:

$$
a_0^{\rm GDQ}
=
\frac{a_H}{2\pi}
=
\frac{cH_0}{2\pi}.
$$

This is the adopted formula. The factor $2\pi$ is not chosen to fit the phenomenological scale: it is the circulation normalization of the radial channel when a global horizon scale is transported to a local response.

## 2. Distinction between Hubble and de Sitter horizons

There is an auxiliary scale:

$$
a_{\rm dS}^{(2\pi)}
=
\frac{cH_0\sqrt{\Omega_\Lambda}}{2\pi}.
$$

It belongs to the effective de Sitter horizon. This scale is useful in cosmology, but it is not the main definition of the galactic critical acceleration. The confusion between the two scales was the source of a historical arithmetic inconsistency: if the numerator is approximately $5.46\times10^{-10}$, then:

$$
\frac{5.46\times10^{-10}}{2\pi}
\approx
8.69\times10^{-11},
$$

and not $1.21\times10^{-10}$.

## 3. Comparison with typical MOND scale

The usual phenomenological value is of the order of:

$$
a_0^{\rm MOND}
\sim
1.20\times10^{-10}\,{\rm m/s^2}.
$$

For $H_0=67.4\,{\rm km\,s^{-1}\,Mpc^{-1}}$:

$$
a_0^{\rm GDQ}
=
1.0422\times10^{-10}\,{\rm m/s^2}.
$$

For $H_0=73\,{\rm km\,s^{-1}\,Mpc^{-1}}$:

$$
a_0^{\rm local}
=
1.1288\times10^{-10}\,{\rm m/s^2}.
$$

Thus:

| Boundary | $a_0$ in ${\rm m/s^2}$ | relative error against $1.20\times10^{-10}$ |
|---|---:|---:|
| $H_0=67.4$ | $1.042197881145\times10^{-10}$ | $-13.150177\%$ |
| $H_0=73$ | $1.128789989964\times10^{-10}$ | $-5.934168\%$ |
| $H_0=67.4$ with $\sqrt{\Omega_\Lambda}$ | $8.623833237863\times10^{-11}$ | $-28.134723\%$ |

## 4. Galactic limit

GDQ is not fundamental MOND. It contains a galactic low-acceleration limit. In this reduction, the observed radial response has the form:

$$
g_{\rm obs}
\simeq
\sqrt{g_Na_0^{\rm GDQ}},
$$

with:

$$
g_N
=
\frac{GM_b(r)}{r^2}.
$$

Since $g_{\rm obs}=v^2/r$, it follows:

$$
v^4
\simeq
GM_ba_0^{\rm GDQ}.
$$

This is the structure of the baryonic Tully-Fisher relation. In GDQ, it arises from the bridge:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast^{\rm cos}
\to
K_{\rm grav}^{\rm phys}
\to
R_H
\to
\frac{1}{2\pi}
\to
a_0^{\rm GDQ}.
$$

## 5. Lensing, clusters, and CMB

A scalar acceleration law is not sufficient for lensing and perturbative cosmology. GDQ treats these effects through the effective metric reconstructed from the physical Hessian:

$$
K_{\rm grav}^{\rm phys}\delta\Phi
=
J_{\rm bar}
+
J_{\rm tor}.
$$

Here $J_{\rm bar}$ is the baryonic source and $J_{\rm tor}$ represents the residual geometric/torsional tension of the Hermitian-Bismut background. The deflection of light must be calculated by optical geometry:

$$
\hat\alpha
=
\int_{\gamma_{\rm luz}}
\nabla_\perp(\Phi+\Psi)
\frac{2\,dl}{c^2}.
$$

In clusters, the residual geometric component can be represented effectively by:

$$
\Theta_{\mu\nu}^{(H)}
\sim
H_{\mu\alpha\beta}H_\nu{}^{\alpha\beta}
-
\frac{1}{2} g_{\mu\nu}|H|^2.
$$

This separates:

1. dissipative baryonic gas;
2. quasi-ballistic galaxies;
3. residual geometric tension contributing to lensing.

In the CMB, the residual geometric sector must sustain gravitational potentials with low effective pressure. The expected reduced form in the linear regime is:

$$
\ddot\delta_{\rm geo}
+
\mathcal H\dot\delta_{\rm geo}
-
4\pi G\rho_{\rm eff}\delta_{\rm geo}
=
O(c_s^2k^2)+O(\sigma_H).
$$

When $c_s^2\approx0$ and the electromagnetic coupling is zero, this sector behaves as an effective cold dark component.

## 6. Status

The numerical result is a direct evaluation of a reduced formula already derived, followed by phenomenological comparison. It does not use $1.20\times 10^{-10}\,{\rm m/s^2}$ as input.

The structural conclusion is:

$$
\boxed{
a_0^{\rm GDQ}
=
\frac{cH_0}{2\pi}
}
$$

What remains for the metrological extension is to explicitly solve $K_{\rm grav}^{\rm phys}$ in backgrounds of galaxies, clusters, and perturbative cosmology, comparing with SPARC/RAR, lensing, and $C_\ell$ spectra.
