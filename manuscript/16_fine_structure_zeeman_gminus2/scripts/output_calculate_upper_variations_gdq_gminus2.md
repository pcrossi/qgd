# Chapter 16 — upper variations of the reduced QGD action

## Classification

Local derivative of a reduced Galerkin truncation of the official action. It is not a metrological prediction of `g-2`.

## 1. Expansion point

The same point from the Galerkin audit was used:

$$
x_*=(1,0,0,0,0),
$$

with coordinates:

| index | mode |
|---:|---|
| 0 | circulation/linear phase |
| 1 | leading harmonic sin(theta) |
| 2 | upper harmonic sin(2theta) |
| 3 | density Re(f) cos(theta) |
| 4 | conformal metric cos(theta) |

## 2. Local Hessian

- central difference step: `2.0e-03`

| eigenvalue | value |
|---:|---:|
| 0 | -1.932949747140319e+02 |
| 1 | -4.769504872323265e+01 |
| 2 | 6.280031355700243e+00 |
| 3 | 2.510719663015614e+01 |
| 4 | 1.155477545652323e+03 |

The presence of negative eigenvalues confirms the previous diagnostic: this simple truncation is not the physical leptonic saddle.

## 3. Selected cubic coefficients

Notation:

$$
T_{ijk}=\frac{\partial^3 S_{\rm red}}{\partial x_i\partial x_j\partial x_k}(x_*).
$$

| term | indices | value | reading |
|---|---|---:|---|
| `T112` | `(1, 1, 2)` | -2.664535259100376e-06 | leading² → direct upper; here it comes out compatible with zero |
| `T113` | `(1, 1, 3)` | 8.881784197001252e-07 | upper coupling allowed/forbidden by the truncation |
| `T114` | `(1, 1, 4)` | -2.664535259100376e-06 | upper coupling allowed/forbidden by the truncation |
| `T122` | `(1, 2, 2)` | -2.664535259100376e-06 | upper coupling allowed/forbidden by the truncation |
| `T123` | `(1, 2, 3)` | -6.283174869281538e+00 | leading-upper mediated by density; robust channel |
| `T124` | `(1, 2, 4)` | -1.776356839400250e-06 | upper coupling allowed/forbidden by the truncation |
| `T011` | `(0, 1, 1)` | 4.440892098500626e-06 | coupling involving protected circulation |
| `T012` | `(0, 1, 2)` | 2.664535259100376e-06 | coupling involving protected circulation |

## 4. Selected quartic coefficients

Notation:

$$
Q_{ijkl}=\frac{\partial^4 S_{\rm red}}{\partial x_i\partial x_j\partial x_k\partial x_l}(x_*).
$$

| term | indices | value |
|---|---|---:|
| `Q1111` | `(1, 1, 1, 1)` | 4.662936703425657e-03 |
| `Q1122` | `(1, 1, 2, 2)` | 3.108624468950438e-03 |
| `Q1133` | `(1, 1, 3, 3)` | 4.714229007163340e+00 |
| `Q1144` | `(1, 1, 4, 4)` | 2.220446049250313e-03 |
| `Q0011` | `(0, 0, 1, 1)` | 2.220446049250313e-03 |
| `Q0022` | `(0, 0, 2, 2)` | 1.554312234475219e-03 |
| `Q0112` | `(0, 1, 1, 2)` | -4.440892098500626e-04 |

## 5. Comparison with harmonic selection

The reduced harmonic selection calculated previously yields:

$$
\beta_{12}=\langle u_2,u_1^2-\langle u_1^2\rangle\rangle
=
\frac{1}{2\sqrt\pi}.
$$

Numerically, `1/(2 sqrt(pi)) = 2.820947917738781e-01`.

In the tested reduced action, `T112` comes out at the level of numerical noise. Thus, the purely harmonic selection `beta12` does not automatically convert into a direct variational source leading² → upper.

The robust cubic coupling is `T123`, numerically close to `-2*pi`. The correct reading is that the leading mode and the upper mode communicate through the density `Re(f)`, not through a universal direct source in a uniform field.

## 6. Consequence for Chapter 16

This calculation does not yet provide metrological `mu_2`. The reason is structural:

1. at the symmetric point `x_*`, the linear magnetic response uses only the quadratic Hessian;
2. cubic/quartic terms generate non-linear response in `B`, unless the physical background already has non-zero stationary internal amplitudes;
3. the tested truncation possesses negative modes and, therefore, cannot be used as the final leptonic background.

The correct route for the metrological prediction then becomes precise:

1. construct a stable 8D leptonic saddle `Phi_l`;
2. evaluate `T` and `Q` on this saddle, not at the unstable symmetric point;
3. contract these tensors with the boundary magnetic map `M[Phi;B]`;
4. set up physical `H_C(alpha)` and re-run the extractor.

Thus, Chapter 16 gains an additional conclusion: the reduced action allows a density-mediated upper channel, but not a universal direct source. Metrology depends on the stable 8D saddle and the complete tensorial contraction. There is no justification for using `mu_2_required` as a prediction.
