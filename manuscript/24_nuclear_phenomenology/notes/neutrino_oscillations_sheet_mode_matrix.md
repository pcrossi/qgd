---
title: "Note — Neutral oscillations, masses, and sheet--mode matrix"
---

# Note — Neutral oscillations, masses, and sheet--mode matrix

This note preserves the reduced construction of neutrino oscillations in the native language of GDQ. The goal is not to insert the PMNS matrix as a fundamental input. The goal is to show how the observed matrix appears when the neutral torsional sector is projected from the leptonic sheet basis to the inertial eigenmode basis.

## 1. Local neutral channel

The local neutral channel already appears in beta decay as a torsional mode without a charged stoma. We write:

$$
\psi_{\bar\nu}
\in
\ker D_{0,-3/2}^{(0)}.
$$

This mode is neutral because it is in the kernel of the electric charge:

$$
Q\psi_{\bar\nu}=0.
$$

It is propagating because it is not bound to a charged stomatal boundary. Instead of a localized defect, the neutrino is a torsion/phase wave in the neutral sector of the physical Hessian.

## 2. Transport between leptonic sheets

The three leptonic sheets are obtained by transporting the same neutral channel along geometric paths in the neutral bundle:

$$
\Psi_\alpha^{\rm sheet}
=
\mathcal P_{\alpha e}\psi_{\bar\nu},
\qquad
\alpha=e,\mu,\tau.
$$

The transport is induced by the projected Bismut connection:

$$
\mathcal P_{\alpha e}
=
\operatorname{Pexp}
\left(
-\int_{\mathcal C_{\alpha e}}
\nabla^B_{\rm neutral}
\right).
$$

Thus, the reduced oscillation space is:

$$
\mathcal H_\nu^{\rm sheet}
=
\operatorname{span}
\left\{
\Psi_e^{\rm sheet},
\Psi_\mu^{\rm sheet},
\Psi_\tau^{\rm sheet}
\right\}.
$$

## 3. Gram matrix, Hessian, and generalized problem

The physical inner product is not the arbitrary flat product. It is weighted by the GDQ measure:

$$
\langle A,B\rangle_{\mathcal U}
=
\int_M
\overline A B\,\mathcal U\,dV_g.
$$

With this, the Gram matrix of the sheet channels is:

$$
G^\nu_{\alpha\beta}
=
\left\langle
\Psi_\alpha^{\rm sheet},
\Psi_\beta^{\rm sheet}
\right\rangle_{\mathcal U}.
$$

The dynamical block comes from the official physical Hessian projected onto the neutral sector:

$$
K^\nu_{\alpha\beta}
=
\left\langle
\Psi_\alpha^{\rm sheet},
K_{\rm neutral}^{\rm phys}
\Psi_\beta^{\rm sheet}
\right\rangle_{\mathcal U}.
$$

The correct problem is generalized:

$$
K^\nu c_i
=
\lambda_i G^\nu c_i.
$$

The states observed as mass states are the eigenmodes of this problem. The mixing matrix is the projection matrix between sheets and modes:

$$
\mathsf U_{\alpha i}^{\rm GDQ}
=
\frac{
\left\langle
\Psi_\alpha^{\rm sheet},
\Psi_i^{\rm neutral}
\right\rangle_{\mathcal U}
}{
\|\Psi_\alpha^{\rm sheet}\|_{\mathcal U}
\|\Psi_i^{\rm neutral}\|_{\mathcal U}
}.
$$

In operational laboratory language:

$$
U_{\rm PMNS}
=
\mathsf U^{\rm GDQ}.
$$

## 4. Reduced scale of squared masses

In the preserveable reduced construction, the neutral scale is:

$$
S_\nu
=
\alpha^7 Q_\beta^2.
$$

Here $Q_\beta$ is the available energy in the free beta channel. The power $\alpha^7$ represents seven neutral leakage filters:

1. three real spatial directions of the tension support;
2. three leptonic sheets;
3. one causal boundary selection of the neutral channel.

This reading is reduced. To become a final metrological prediction, the same power must emerge as a matrix element of the neutral symplectic current of the official action.

The preserved candidate spectrum is:

$$
\lambda
=
\left(
0,
\frac{\chi_\nu^2}{2},
\frac{6\pi}{5}
\right),
$$

with:

$$
\chi_\nu
=
\frac{12}{25}e^{-\alpha/4}.
$$

The factor $12/25$ is the $3$--$4$--$5$ dual-channel projection:

$$
\frac{12}{25}
=
\frac{3}{5}\frac{4}{5}.
$$

The factor $1/2$ comes from the normalization of the relative subspace of two sheets. The factor $6\pi/5$ is the reduced upper neutral circulation:

$$
\frac{6\pi}{5}
=
3\frac{2\pi}{5}.
$$

This last step uses the global transport of five cycles in Einstein's cosmological space and should be read as a reduced global--local bridge.

## 5. Squared mass differences

With:

$$
\Delta m_{ij}^2
=
S_\nu(\lambda_i-\lambda_j),
$$

we obtain:

$$
\Delta m_{21}^2
=
7.741214557111\times10^{-5}\,{\rm eV}^2,
$$

$$
\Delta m_{31}^2
=
2.542566638608\times10^{-3}\,{\rm eV}^2.
$$

Comparison with the reference values used in the script:

| quantity | Reduced GDQ | reference | relative error |
|---|---:|---:|---:|
| $\Delta m_{21}^2$ | $7.741214557111\times10^{-5}\,{\rm eV}^2$ | $7.49\times10^{-5}\,{\rm eV}^2$ | $+3.353999\%$ |
| $\Delta m_{31}^2$ | $2.542566638608\times10^{-3}\,{\rm eV}^2$ | $2.534\times10^{-3}\,{\rm eV}^2$ | $+0.338068\%$ |

The minimum masses in the normal hierarchy, taking $m_1=0$ as the reduced spectral origin, are:

$$
m_1=0,
\qquad
m_2=8.798417219655\times10^{-3}\,{\rm eV},
\qquad
m_3=5.042386973059\times10^{-2}\,{\rm eV}.
$$

Therefore:

$$
\sum_i m_i
=
5.922228695025\times10^{-2}\,{\rm eV}.
$$

## 6. Reduced angles and mixing matrix

The preserveable reduced angles are:

$$
\theta_{12}
=
\operatorname{arctan}\left(\frac{1}{\sqrt{2}}\right),
$$

$$
\theta_{23}
=
\frac{\pi}{4},
$$

$$
\theta_{13}
=
\operatorname{arcsin}\left(\frac{\chi_\nu}{\pi}\right).
$$

Numerically:

| parameter | Reduced GDQ | reference used | difference |
|---|---:|---:|---:|
| $\theta_{12}$ | $35.264389683^\circ$ | $33.680000000^\circ$ | $+1.584389683^\circ$ |
| $\theta_{23}$ | $45.000000000^\circ$ | $48.500000000^\circ$ | $-3.500000000^\circ$ |
| $\theta_{13}$ | $8.772427998^\circ$ | $8.520000000^\circ$ | $+0.252427998^\circ$ |

The phase:

$$
\delta_{\rm CP}
=
\arg
\operatorname{Hol}_{\Gamma_{\rm sheets}}
(\nabla^B_{\rm neutral})
$$

must still be calculated as the neutral oriented holonomy. The historical value $3.84$ radians can be used only as a comparative marker, not as a final prediction.

## 7. Oscillation probability in the laboratory reduction

Once $\mathsf U^{\rm GDQ}$ and $\Delta m^2$ are obtained, the operational translation for the laboratory is:

$$
P_{\alpha\to\beta}(L,E)
=
\left|
\sum_i
\mathsf U_{\beta i}^{\rm GDQ}
\exp\left(
-i\frac{m_i^2L}{2E}
\right)
\overline{\mathsf U_{\alpha i}^{\rm GDQ}}
\right|^2.
$$

In standard oscillation units:

$$
\phi_{ij}
=
1.267\,
\Delta m_{ij}^2
\frac{L/{\rm km}}{E/{\rm GeV}}.
$$

This formula is not a new axiom. It is the operational expression obtained after GDQ provides the inertial scale differences and the sheet--mode matrix.

## 8. Sensitivity of the coefficients

With the scale fixed:

$$
S_\nu
=
6.744367477916\times10^{-4}\,{\rm eV}^2,
$$

the coefficients required by references would be:

| coefficient | required | Reduced GDQ | relative error |
|---|---:|---:|---:|
| $\lambda_2$ | $1.110556330824\times10^{-1}$ | $1.147804383800\times10^{-1}$ | $+3.353999\%$ |
| $\lambda_3$ | $3.757209268768$ | $3.769911184308$ | $+0.338068\%$ |
| $\chi_\nu$ | $4.712868194260\times10^{-1}$ | $4.791251159771\times10^{-1}$ | $+1.663169\%$ |
| $\lambda_3/(2\pi)$ | $5.979784273551\times10^{-1}$ | $6.000000000000\times10^{-1}$ | $+0.338068\%$ |

The main metrological bottleneck is the dual-channel block that determines $\lambda_2$. The upper mode is already very close to the global circulation of $3/5$.

## 9. Status

The preserved result is:

$$
\boxed{
\text{neutrinos = neutral torsional modes; oscillations = sheet--mode projection.}
}
$$

The sector is structurally closed and has a reduced quantitative candidate. The final metrological closure requires:

1. constructing the neutral background $\Phi_*^\nu$;
2. calculating $G^\nu$ and $K^\nu$ directly from the official Hessian;
3. obtaining $Z_\nu$ via the global--local bridge;
4. calculating $\delta_{\rm CP}$ as the neutral oriented holonomy;
5. calculating the medium potential $V_{\rm GDQ}(n_e)$ as the torsional refraction by a classical matter source.
