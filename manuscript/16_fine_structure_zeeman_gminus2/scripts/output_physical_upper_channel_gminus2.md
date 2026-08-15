# Chapter 16 — derivation of the physical upper channel

## Classification

Direct evaluation of the selection rule of the linear magnetic map. Does not use experimental value of `g_e` or `g_mu-2`.

## 1. Linear magnetic map

For a uniform magnetic field on the Noether cycle, the linear coupling selects only the harmonic Hodge component:

$$
M[\Phi;B]
=
B\left(\gamma_0\mathcal C[\Phi]+M_\perp[\Phi]\right).
$$

The direct upper channel would be a projection of $M_\perp$ onto upper exact modes $d\sin(k\vartheta)$.

## 2. Selection rule

$$
h=\frac{d\vartheta}{2\pi},
\qquad
e_k\propto d\sin(k\vartheta).
$$

Since the uniform field is constant on the cycle,

$$
\langle h,e_k\rangle=0
\qquad
(k\ge1).
$$

Numerically:

- `||h||^2 = 1.591549430918953e-01`
- `<h,e_1> = -4.359835622510790e-17`
- `<h,e_2> = -2.724897264069244e-17`
- `<e_1,e_2> = -6.539753433766185e-17`

Therefore:

$$
\boxed{\mu_{2,\ell}^{\rm direct}=0.}
$$

## 3. Stable blocks with selection rule

| lepton | Q39 role | M_l/M_e | K2 | direct mu2 | a obtained | file |
|---|---|---:|---:|---:|---:|---|
| e | primary torsion | 1.000000000000000e+00 | 8.610225765836003e+02 | 0.0 | 1.161409732097665e-03 | `leptonic_selection_background_e_gminus2.npz` |
| mu | transverse/bispatial torsion | 2.067685934706287e+02 | 1.780324271066477e+05 | 0.0 | 1.161409732097665e-03 | `leptonic_selection_background_mu_gminus2.npz` |
| tau | three-dimensional saturation | 3.477446405098381e+03 | 2.994159863649186e+06 | 0.0 | 1.161409732097665e-03 | `leptonic_selection_background_tau_gminus2.npz` |

## 4. Consequence

The first upper channel is not a new direct linear source for a uniform magnetic field. Thus, replacing the `required` blocks with a derived direct source gives `mu2=0`, not the observed metrological value.

Therefore, the upper residuals of `g-2` must come from another internal link:

1. correction of the physical Hessian `H_C=H_0+alpha H_1+...`;
2. Hessian mixture between the leading channel and upper modes;
3. non-uniform internal electrogeometric map, if derived from the bulk;
4. or non-uniform apparatus source, which is not universal.

For the universal anomaly in a uniform field, the correct route is the Hessian correction, not a new direct `mu2`.
