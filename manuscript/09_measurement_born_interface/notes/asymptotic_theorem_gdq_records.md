---
title: "Asymptotic theorem of GDQ records"
---

# Asymptotic theorem of GDQ records

This note consolidates the technical part of measurement in GDQ. It does not introduce a new action. The apparatus enters as a source, boundary, and interface impedance applied to the official action.

## 1. Data of the measurement problem

A measurement involves:

$$
S+A+E,
$$

where $S$ is the system, $A$ is the apparatus, and $E$ is the environment. The apparatus defines external classical data:

$$
J_{\rm app},
\qquad
\text{R}_{\rm app},
\qquad
\Omega_{\rm app},
\qquad
\partial\Omega_{\rm app}.
$$

These data select the domain and boundary. They do not modify the official action.

During the measurement window, assume an admissible background:

$$
\Phi_\ast=(g_\ast,f_\ast,\bar f_\ast),
\qquad
\mathcal U_\ast
=
\frac{\rho_\ast}{(4\pi z_\tau)^n}.
$$

## 2. GDQ measurement operator

The effective measurement operator is the projected physical Hessian:

$$
\mathcal H_{\rm meas}
=
P^{\rm phys}
\operatorname{Hess}_{\Phi_\ast}
\mathcal S_{\rm GDQ}^{S+A+E}
P^{\rm phys}.
$$

Here $P^{\rm phys}$ removes diffeomorphisms, gauge redundancies, and variations that violate physical constraints. The notation $S+A+E$ means that the same official action is evaluated with the sources and boundaries of the system, apparatus, and environment.

The typical domain is:

$$
\mathcal D(\mathcal H_{\rm meas})
=
\left\{
\delta\Phi\in H^2_{\rm loc}(\Omega):
(\nabla_n+\text{R}_{\rm app})\delta\Phi|_{\partial\Omega}
=
J_{\rm app}^{(1)}
\right\}
\cap
\operatorname{Im}P^{\rm phys}.
$$

In the linearized homogeneous sector, $J_{\rm app}^{(1)}=0$ and the condition reduces to:

$$
(\nabla_n+\text{R}_{\rm app})\delta\Phi=0.
$$

## 3. Density reduction

Since

$$
\rho=e^{-(f+\bar f)/2},
$$

a real density variation is:

$$
\delta\rho
=
-
\frac12\rho(\delta f+\delta\bar f).
$$

In the reduced dissipative sector of the measurement, the projected Hessian induces:

$$
\partial_\tau\delta\rho
=
-
\mathcal H_\rho\delta\rho,
$$

with:

$$
\mathcal H_\rho
=
\Pi_\rho\mathcal H_{\rm meas}\Pi_\rho^\ast.
$$

In the limit where only the effective density is observed:

$$
\mathcal H_\rho
\simeq
-
\Delta_K+R_{\rm eff}.
$$

The sign is chosen such that positive eigenvalues generate decay:

$$
\rho(\tau)=e^{-\tau\mathcal H_\rho}\rho(0).
$$

## 4. Inner product, boundary and self-adjointness

The reduced inner product uses the stationary measure of GDQ:

$$
\langle u,v\rangle_{\mathcal U}
=
\int_\Omega
\bar u\,v\,
\mathcal U_\ast\sqrt{\det g_\ast}\,d^{2n}z.
$$

With $\text{R}_{\rm app}$ Hermitian on the boundary and $P^{\rm phys}$ orthogonal in this product, integration by parts gives:

$$
\langle u,\mathcal H_\rho v\rangle_{\mathcal U}
=
\langle\mathcal H_\rho u,v\rangle_{\mathcal U}.
$$

The boundary term is proportional to:

$$
\int_{\partial\Omega}
\bar u
\left(
\nabla_n v+\text{R}_{\rm app}v
\right)
d\Sigma_{\mathcal U}.
$$

It vanishes for functions in the Robin/DtN domain. A stable apparatus requires the quadratic form:

$$
Q_\rho[u]
=
\langle u,\mathcal H_\rho u\rangle_{\mathcal U}
\ge0
$$

in the physical record sector.

## 5. Records as spectral sectors

A macroscopic record $R_i$ is represented by a sector:

$$
R_i
\leftrightarrow
\Omega_i
\leftrightarrow
\Pi_i.
$$

The sectorial projectors satisfy:

$$
\Pi_i\Pi_j=\delta_{ij}\Pi_i,
\qquad
\sum_i\Pi_i=I_{\rm reg}.
$$

When the sector is defined by a separated spectral cluster:

$$
\Pi_i
=
\frac1{2\pi i}
\oint_{\Gamma_i}
(z-\mathcal H_\rho)^{-1}\,dz.
$$

## 6. Measurement gap

In each sector:

$$
\mathcal H_i
=
\Pi_i\mathcal H_\rho\Pi_i.
$$

Assume:

$$
0\le\lambda_{i,0}<\lambda_{i,1}\le\lambda_{i,2}\le\cdots.
$$

Define:

$$
\Delta_i=\lambda_{i,1}-\lambda_{i,0}>0,
$$

and, for distinct sectors:

$$
\Delta_{ij}
=
\operatorname{dist}(\sigma_i,\sigma_j)>0.
$$

The measurement gap is:

$$
\Delta_{\rm meas}
=
\min
\left\{
\min_i\Delta_i,
\min_{i\ne j}\Delta_{ij}
\right\}
>0.
$$

## 7. Asymptotic suppression of coherences

After the ideal interaction:

$$
|\Psi_{SAE}\rangle
=
\sum_i c_i|s_i\rangle|A_i\rangle|E_i\rangle.
$$

The off-diagonal terms receive:

$$
\Gamma_{ij}(\tau)
=
\langle A_j(\tau),E_j(\tau)|A_i(\tau),E_i(\tau)\rangle.
$$

Since distinct records belong to separate spectral sectors:

$$
|\Gamma_{ij}(\tau)|
\le
C_{ij}e^{-\Delta_{ij}\tau}
+
O(e^{-S_{\rm sep}/\hbar}),
\qquad
i\ne j.
$$

Hence:

$$
\rho_{SA}(\tau)
\to
\sum_i
\operatorname{Tr}(\rho_SP_i)
|s_i,A_i\rangle\langle s_i,A_i|.
$$

## 8. Repeatability

After observing record $i$, the conditioned state is:

$$
\rho_{S|i}
=
\frac{P_i\rho_SP_i}{\operatorname{Tr}(\rho_SP_i)}.
$$

Then:

$$
\operatorname{Tr}(\rho_{S|i}P_i)=1.
$$

This proves ideal repeatability.

## 9. Unique outcome by real basins

Decoherence and gap prove asymptotic diagonalization. One individual event requires a real dynamics of basins in the apparatus and environment.

Define:

$$
\mathcal C_{A+E}
=
\{(g,f,\bar f;\xi_{\rm app})
\text{ compatible with the apparatus boundary}\}/\mathcal G.
$$

The open effective functional is:

$$
\mathfrak F_{\rm meas}[\Phi]
=
\operatorname{Re}
\mathcal S_{\rm GDQ}^{S+A+E}[\Phi].
$$

Sufficient hypotheses:

1. $\mathcal C_{A+E}$ is regular in the projected physical sector;
2. $\mathfrak F_{\rm meas}$ is $C^2$;
3. there exists dissipative dynamics with a Lyapunov function:

$$
\frac{d}{d\tau}\mathfrak F_{\rm meas}[\Phi(\tau)]\le0;
$$

4. each record $R_i$ is a hyperbolic minimum:

$$
\nabla\mathfrak F_{\rm meas}(R_i)=0,
\qquad
\operatorname{Hess}_{R_i}^{\rm phys}\mathfrak F_{\rm meas}>0;
$$

5. boundaries between basins are stable manifolds of saddles;
6. the initial measure is absolutely continuous with respect to the measure induced by $\mathcal U_\ast$.

The basin is:

$$
\mathcal B_i
=
\left\{
\Phi_0\in\mathcal C_{A+E}:
\lim_{\tau\to\infty}\Phi(\tau;\Phi_0)=R_i
\right\}.
$$

By the stable manifold theorem, basin boundaries have measure zero. Therefore, for almost every real initial condition, there exists a unique $i$ such that:

$$
\Phi_0\in\mathcal B_i,
\qquad
\Phi(\tau;\Phi_0)\to R_i.
$$

Born compatibility is:

$$
\mu_{\rm init}(\mathcal B_i)
=
\operatorname{Tr}(\rho_SP_i).
$$

## 10. Logical status

The asymptotic records theorem is conditional:

$$
\boxed{
\mathcal H_{\rm meas}\text{ self-adjoint}
+
\Delta_{\rm meas}>0
\Longrightarrow
\text{exponential decoherence, stable records, and repeatability}.
}
$$

The ontological unique outcome is conditionally dependent additionally on the existence of real Morse basins in the microgeometric space of the apparatus and environment. This condition does not alter the official action; it specifies when a concrete apparatus performs a complete measurement.
