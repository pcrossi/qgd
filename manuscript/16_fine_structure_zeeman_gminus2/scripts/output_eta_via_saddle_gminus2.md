# Chapter 16 — density amplitude calculated by the saddle

## Classification

Direct evaluation of a normalized reduced Galerkin saddle and convergence test. It is not the complete physical leptonic saddle in eight dimensions. The experimental target of `g-2` does not participate in the calculation.

## 1. Variational problem

With fixed unit circulation, one varies:

$$
y=(a_1,a_2,\eta,\sigma).
$$

The phase with monodromy is differentiated by:

$$
P'=\frac{1}{2\pi}+a_1\cos\theta+2a_2\cos2\theta.
$$

The measure is constrained by:

$$
\frac1{2\pi}\int_0^{2\pi}\rho\sqrt g\,d\theta=1.
$$

The constant mode of $\operatorname{Re}f$ is then determined by:

$$
F_0=\log I_0(2\sigma-\eta).
$$

The saddle solves $\nabla_y S_{\rm red}=0$.

## 2. Convergence

| N | roots | a1 | a2 | eta | sigma | U norm | ||grad S|| | min eig |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024 | 1 | 5.478823037e-10 | -2.054013509e-12 | 3.472867244e-09 | 1.720979579e-09 | 1.000000000000e+00 | 0.000e+00 | -6.247154919e-02 |
| 2048 | 1 | 3.243608548e-10 | 2.271665450e-12 | 2.026916669e-09 | 1.016777962e-09 | 1.000000000000e+00 | 5.921e-11 | -6.247203793e-02 |
| 4096 | 1 | -7.249600845e-11 | -1.032349560e-13 | -4.699924510e-10 | -2.482808855e-10 | 1.000000000000e+00 | 5.921e-11 | -6.247150832e-02 |
| 8192 | 1 | -2.103530131e-10 | -6.996303574e-13 | -1.339190334e-09 | -6.640015440e-10 | 1.000000000000e+00 | 0.000e+00 | -6.247246698e-02 |

## 3. Result

Within the search box $[-5,5]^4$, initiated from nine points, the only normalized stationary root is the homogeneous saddle:

$$
a_1=a_2=\eta_\ell=\sigma=0
$$

with final numerical value `eta_l = -1.339190333605100e-09`.

The reduced Hessian still possesses a negative eigenvalue. Therefore, the root is a saddle of the reduced functional, not a stable minimum nor the already projected 8D physical leptonic background.

## 4. Consequence for the upper channel

Since $\eta_\ell=0$ in this saddle,

$$
\Delta H_{12}=\eta_\ell T_{123}=0.
$$

The unnormalized solution with $|\eta|\simeq 1.064$ is excluded: it alters the total norm of $\mathcal U\sqrt g$ and does not belong to the normalized variational domain of QGD.

The calculation demonstrates a useful negative result: the homogeneous angular saddle does not generate the upper metrological correction. A non-zero value of $\eta_\ell$ can only come from the non-homogeneous, warped, or mixed 8D background, with specified domain, boundaries, and physical projector.
