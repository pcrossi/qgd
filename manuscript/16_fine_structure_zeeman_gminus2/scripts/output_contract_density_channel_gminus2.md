# Chapter 16 — contraction of the density-mediated upper channel

## Classification

Conditional evaluation of a channel derived from the reduced action. Does not use experimental values of `g-2`.

## 1. Input

- `eta_density = 0.000000000000000e+00`
- `T123 = -6.283174869281538e+00`
- `alpha/(2*pi) = 1.161409732097664e-03`

The applied channel is:

$$
\Delta H_{12}
=
\eta_\ell T_{123}.
$$

Here $\eta_\ell$ must come from an admissible saddle. The normalized reduced angular saddle was calculated separately and yields $\eta_\ell=0$. A non-zero value would require the non-homogeneous, warped, or mixed 8D background.

## 2. Results

| block | Q39 role | M_l/M_e | eig_min | a0 | a_eff | delta_a |
|---|---|---:|---:|---:|---:|---:|
| `leptonic_stable_background_e_gminus2.npz` | primary torsion | 1.000000000000000e+00 | 9.988372413989819e-01 | 1.161409732097665e-03 | 1.161409732097665e-03 | 0.000000000000000e+00 |
| `leptonic_stable_background_mu_gminus2.npz` | transverse/bispatial torsion | 2.067685934706287e+02 | 9.988372413989819e-01 | 1.161409732097665e-03 | 1.161409732097665e-03 | 0.000000000000000e+00 |
| `leptonic_stable_background_tau_gminus2.npz` | three-dimensional saturation | 3.477446405098381e+03 | 9.988372413989819e-01 | 1.161409732097665e-03 | 1.161409732097665e-03 | 0.000000000000000e+00 |

## 3. Reading

For the value reported above, the table directly shows the response of the density-mediated channel. The canonical execution uses $\eta_\ell=0$, the value of the normalized reduced angular saddle; in this case, the contraction does not alter the leading response.

Therefore, the next physical datum necessary for metrology is not `mu2_required`; it is $\eta_\ell$ or, more generally, the complete stationary profile of $\operatorname{Re}f$ on the 8D leptonic saddle. Once this background is provided, this same operator calculates the correction without experimental post-fitting.
