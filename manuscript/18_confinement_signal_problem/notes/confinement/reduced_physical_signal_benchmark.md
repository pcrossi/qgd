---
title: "Reduced physical benchmark of the signal problem"
---

# Reduced physical benchmark of the signal problem

This note records the self-contained version of the reduced physical benchmark used to test the GDQ reading for the fermionic signal problem. The objective is not to prove that every strongly correlated fermionic problem becomes polynomial. The objective is more restricted and verifiable:

1. construct a positive ensemble coherent with GDQ;
2. maintain fermionic antisymmetry as phase holonomy;
3. obtain a unitary interface from a reduced Hermitian impedance;
4. calculate a spin/circulation correlation without negative weights;
5. compare the sign and order of magnitude with cold data from lattice atoms.

## 1. Data of the Reduced Problem

The experimental apparatus is represented by a finite square lattice $L\times L$. In the minimum benchmark, $L=4$ was used, hence $N=L^2=16$. The local variable $\sigma_i=\pm1$ represents the observed signal in the spin/circulation sector. To separate the antiferromagnetic alternation from the positivity of the measure, we define the staggered variable

$$
x_i=\eta_i\sigma_i,
\qquad
\eta_i=(-1)^{x(i)+y(i)}.
$$

The bipartite lattice transfers the alternating sign to the observable, not to the measure. Thus, the reduced energy used for sampling is the positive quadratic form

$$
E_{\rm GDQ}(x)
=
\frac{1}{2}x^T K_{\rm red}x,
$$

with

$$
K_{\rm red}
=
m_{\rm gap}I+\kappa_H\Delta_{\rm lat}.
$$

Here, $\Delta_{\rm lat}$ is the graph Laplacian of the periodic lattice, $m_{\rm gap}>0$ is the reduced gap of the transverse sector, and $\kappa_H>0$ is the reduced stiffness inherited from the physical Hessian. In the preserved test, we used

$$
L=4,
\qquad
\beta_{\rm eff}=0.45,
\qquad
\kappa_H=0.35,
\qquad
m_{\rm gap}=0.18.
$$

These numbers belong to the reduced benchmark. They are not declared as fundamental constants of GDQ.

## 2. Positive Measure and Signal as Holonomy

The Monte Carlo measure is

$$
\rho_{\rm MC}(x)
=
\frac{1}{Z}\exp\left(-\beta_{\rm eff}E_{\rm GDQ}(x)\right),
\qquad
Z=\sum_x \exp\left(-\beta_{\rm eff}E_{\rm GDQ}(x)\right).
$$

Since $E_{\rm GDQ}(x)$ is real, the measure is strictly positive:

$$
\rho_{\rm MC}(x)>0.
$$

Fermionic antisymmetry does not enter as a negative weight. It enters as exchange holonomy,

$$
\operatorname{Hol}(P_{ij})=-1.
$$

This is the essential distinction of GDQ in this sector: the fermionic signal is kept in the phase/circulation, while the density used for sampling remains positive.

## 3. Interface by the Reduced Hessian

For each edge $(i,j)$, we extract the local block of the reduced Hessian:

$$
K_{ij}
=
K_{\rm red}\big|_{\{i,j\}}.
$$

Normalizing by its spectral norm, we obtain the Hermitian impedance

$$
\mathsf R_{ij}
=
\frac{K_{ij}}{\|K_{ij}\|_2}.
$$

The interface matrix is then the Cayley transform

$$
\mathsf S_{ij}
=
\left(I+i\mathsf R_{ij}\right)^{-1}
\left(I-i\mathsf R_{ij}\right),
$$

with the fermionic holonomy applied to the exchange channel. Since $\mathsf R_{ij}=\mathsf R_{ij}^\dagger$, it directly follows that

$$
\mathsf S_{ij}^\dagger\mathsf S_{ij}=I.
$$

In the self-contained numerical test, the maximum unitarity error was of the order of $10^{-16}$, that is, machine error.

## 4. Correlation Observable

The first-neighbor observable is

$$
C_s(1)
=
\left\langle
\sigma_i\sigma_{i+\hat e}
\right\rangle.
$$

Since $\sigma_i=\eta_i x_i$, the antiferromagnetic signal appears in the observable:

$$
\sigma_i\sigma_j
=
\eta_i\eta_j x_i x_j.
$$

For first neighbors in a bipartite lattice,

$$
\eta_i\eta_j=-1.
$$

Therefore, a positive and smooth correlation of $x_i x_j$ generates $C_s(1)<0$ without introducing a negative weight in the measure.

## 5. Internal Results of the Benchmark

For $L=4$, there are $2^{16}=65536$ configurations, allowing exact enumeration. The test was also repeated by Metropolis Monte Carlo with a positive measure.

| Quantity | Value |
|---|---:|
| exact configurations | $65536$ |
| exact $C_s(1)$ | $-0.1698717343244$ |
| Monte Carlo $C_s(1)$ | $-0.16836$ |
| MC standard error | $6.2963\times10^{-4}$ |
| exact $C_s(2)$ | $0.05714802778502$ |
| Monte Carlo $C_s(2)$ | $0.05517$ |
| MC acceptance | $0.75515$ |
| observed fit | $\tau_{\rm corr}\sim N^{0.934}$ |

The physical reading is limited but clear: in the size interval tested, there is no sign of exponential explosion of autocorrelation, and the antiferromagnetic correlation arises with the correct sign using a positive weight.

## 6. External Phenomenological Comparison

The external data below are local values preserved for comparison with experimental cold atoms in a lattice. The complete bibliographic reference must be inserted in the reference folder of the manuscript; here we record only the values used in the verification.

### 6.1 Direct Cold Comparison

| Local Source | $k_BT/t$ | Observable | Experimental | Reduced GDQ | Deviation |
|---|---:|---|---:|---:|---:|
| central cold data | $0.45$ | $C_s(1)$ | $-0.190\pm0.008$ | $-0.1698717$ | $2.516\sigma$ |
| digitized point | $0.45$ | $C_s(1)$ | $-0.210\pm0.020$ | $-0.1698717$ | $2.006\sigma$ |

The benchmark reproduces the sign and order of magnitude, but it is not a metrological agreement with all experimental points.

### 6.2 Reduced Thermal Map

Inverting the positive curve of the reduced ensemble for the digitized points, we obtain the phenomenological family

$$
\beta_{\rm eff}
\simeq
\frac{0.291786}{k_BT/t+0.050000}.
$$

This inversion shows that the shape of the curve can be represented by a positive thermal family of the reduced GDQ, but it still does not prove that this thermal map was directly derived from the full Hessian of the apparatus.

### 6.3 Schur Complement of the Apparatus

The observed mode was taken as the circulation difference on the first constraint of the lattice. The orthogonal complement acts as a reduced bath/apparatus. The decomposition gives

$$
K_H=1.93,
\qquad
\chi_A=J K_A^{-1}J^T=0.2229537798681,
$$

and, therefore,

$$
K_{\rm Schur}
=
K_H-JK_A^{-1}J^T
=
1.707046220132.
$$

The reduced second-moment response is

$$
\chi_2
=
J K_A^{-2}J^T
=
0.1593233959409.
$$

The best unadjusted Schur map used in the comparison was

$$
\beta_{\rm Schur}(\Theta)
=
\frac{\mu_A}{\Theta+\Theta_A},
\qquad
\mu_A=0.554521554,
\qquad
\Theta_A=0.616921719,
$$

with $\Theta=k_BT/t$.

| $k_BT/t$ | Experimental $C_s(1)$ | GDQ--Schur $C_s(1)$ | Deviation |
|---|---:|---:|---:|
| $0.00$ | $-0.350\pm0.020$ | $-0.450850$ | $-5.042\sigma$ |
| $0.45$ | $-0.210\pm0.020$ | $-0.210714$ | $-0.036\sigma$ |
| $0.55$ | $-0.240\pm0.020$ | $-0.180111$ | $2.994\sigma$ |
| $0.90$ | $-0.110\pm0.020$ | $-0.129634$ | $-0.982\sigma$ |
| $1.50$ | $-0.050\pm0.020$ | $-0.093611$ | $-2.181\sigma$ |

The point $k_BT/t=0.45$ is reproduced very well. The complete curve still shows residuals, especially in the cold limit and at high temperature. The point $k_BT/t=0.55$ must be treated with caution because the preserved digitization is not monotonic with respect to the neighboring points.

## 7. Thermal Width Correction

The reduced Schur width was

$$
\Theta_A^{\rm Schur}
\simeq
0.616921719.
$$

The effective map fitted to the curve required

$$
\Theta_A^{\rm fit}
\simeq
0.721527850.
$$

Hence the width residue was

$$
\Delta\Theta_A
\simeq
0.104606131.
$$

Spectral corrections of the bath generated positive contributions of the correct order, for example

$$
\Delta\Theta_A
\simeq
0.0690713
$$

for the candidate $\sum J_k^2/(\lambda_k(\lambda_k+K_{\rm Schur}))$. This indicates that the physical direction is plausible, but that the reduced model still omits dissipative channels, causal mobility, or real thermal weights of the apparatus.

## 8. Verdict

The reduced physical benchmark closes the structural statement of GDQ:

$$
\boxed{
\text{it is possible to sample the tested fermionic sector with a positive measure,}
\quad
\text{maintaining the sign as holonomy.}
}
$$

It also provides a useful phenomenological comparison:

$$
C_s(1)_{\rm GDQ}
=
-0.1698717
$$

against experimental/digitized cold values of the order of $-0.19$ to $-0.21$.

What is not proven by this benchmark is a universal algorithmic solution to the signal problem. For that strong statement, the following would still be necessary:

1. a complete GDQ Hessian, not just a reduced one;
2. a thermal map of the apparatus derived from $\mathsf R_{\rm app}$ and causal mobility;
3. asymptotic bounds on variance and autocorrelation;
4. benchmarks in larger families of Hamiltonians/contours, with parameters frozen before comparison.

Thus, the correct status is: signal problem structurally closed in GDQ and validated in a reduced benchmark; general computational solution remains a future program.
