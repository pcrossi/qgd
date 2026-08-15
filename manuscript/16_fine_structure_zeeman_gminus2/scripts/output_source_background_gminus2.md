# Chapter 16 — reduced leptonic background and magnetic map

## Classification

Reduced construction and stability test. The stable block below is a minimal effective background compatible with Q39 and with the leading response; it is not yet the complete 8D background of QGD.

## 1. Direct search on the official Galerkin truncation

- best objective: `3.489115534716972e+04`
- background found: `[1.0, 0.0, 0.05, 0.0, 0.0]`
- norm of the transverse gradient: `4.036685330345434e+01`
- candidates evaluated: `11`

| sector | eigenvalues |
|---|---|
| complete Galerkin Hessian | `[-63.794201508927706, -18.113164129568492, 6.268744065544268, 24.872950882301176, 140.8807437387756]` |
| transverse Galerkin Hessian | `[-57.67293342747282, 6.268111375276628, 23.848628031801464, 36.50224547557788]` |

Reading: the simple official Galerkin truncation continues to present negative modes. Therefore, it does not by itself provide the physical leptonic saddle. This is a useful negative result: the physical background requires a physical projector/complete bulk or a richer truncation.

## 2. Physical magnetic map of external source

For a weak magnetic field, treated as apparatus/boundary datum:

$$
M[\Phi;B]
=
B\left(\gamma_0\mathcal C[\Phi]+M_\perp[\Phi]\right).
$$

The minimal part is protected by Noether:

$$
M_{\rm min}[\Phi;B]=B\gamma_0\mathcal C[\Phi].
$$

The leading transverse part is the harmonic projection on the phase cycle:

$$
M_\perp^{(1)}[\Phi;B]=B\,A_h[\Phi],
\qquad
\langle h,h\rangle=\frac{1}{2\pi}.
$$

In the stable matrix representation, the stiffness of the harmonic channel is `K1=2*pi/alpha` and the normalized source is `m_perp=(0,1,0)`, producing `alpha/(2*pi)` by contraction with `H^{-1}`, not by post-fitting to the target.

## 3. Reduced stable leptonic background

| lepton | current Q39 role | M_l/M_e | stable K2 | leading a | file |
|---|---|---:|---:|---:|---|
| e | primary torsion | 1.000000000000000e+00 | 8.610225765836003e+02 | 1.161409732097665e-03 | `leptonic_stable_background_e_gminus2.npz` |
| mu | transverse/bispatial torsion | 2.067685934706287e+02 | 1.780324271066477e+05 | 1.161409732097665e-03 | `leptonic_stable_background_mu_gminus2.npz` |
| tau | three-dimensional saturation | 3.477446405098381e+03 | 2.994159863649186e+06 | 1.161409732097665e-03 | `leptonic_stable_background_tau_gminus2.npz` |

## 4. Verdict

The physical map `M[Phi;B]` is derived in the linear apparatus regime: minimal term by Noether plus harmonic transverse term. The minimal stable leptonic background was constructed as a positive effective block compatible with Q39 and the leading response.

What is not yet closed is the complete 8D saddle nor the metrological upper channels. The direct search showed that the simple Galerkin truncation still has negative modes, so it should not be used as a blind prediction of `g_e` or `g_mu-2`.
