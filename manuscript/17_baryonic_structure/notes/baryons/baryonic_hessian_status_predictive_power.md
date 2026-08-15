---
title: "Derivational Status, Hessian, and Predictive Power of the Baryonic Sector"
---

# Derivational Status, Hessian, and Predictive Power of the Baryonic Sector

## 1. Statement and Domain

The baryonic problem considered in this chapter is:

$$
\text{construct a trimodal background }
\Phi_B=(g_B,f_B,H_B,\mathcal A_B)
$$

on the local bulk $\mathbb R^4\times T^4$, with three stoma interfaces, and extract its observables in the reconstructed physical section.

The cycle

$$
\mathcal C_B\simeq T^5_{\rm braided}\times S^3_{\rm hol}
$$

is used to calculate global invariants. It is not identified with the local bulk.

## 2. Chain that a Complete Prediction Must Satisfy

$$
\mathcal S_{\rm GDQ}
\longrightarrow
\Phi_B
\longrightarrow
K_B^{\rm phys}
\longrightarrow
\text{stable spectrum}
\longrightarrow
\text{observable}.
$$

With constraints $\mathcal C_i[\Phi_B]=c_i$, the correct physical Hessian is the second variation of the augmented functional:

$$
K_B^{\rm phys}
=
P_{\rm phys}^{\dagger}
\left.
\delta^2
\left(
\mathcal S_{\rm GDQ}
-
\sum_i\lambda_i\mathcal C_i
\right)
\right|_{\Phi_B}
P_{\rm phys}.
$$

The projector $P_{\rm phys}$ removes diffeomorphisms, gauge zero modes, and variations incompatible with normalization, charge, flux, trimodal class, and interface conditions. It cannot remove a physical mode just because that mode makes the Hessian indefinite.

The chapter features a reduced glued construction and surface Hessian blocks. It does not yet have a general smooth solution of the coupled 8D system throughout the throat. Therefore, observables depending on the full profiles are conditional results of the reduced model.

## 3. What is Exact

Once the three-chamber decomposition is fixed:

$$
3(2\pi^5)=6\pi^5.
$$

Once the neutral orientation is fixed:

$$
1+1-2=0,
$$

and:

$$
(1-1)^2+(1+2)^2+(1+2)^2=18.
$$

Also exact:

1. the integrability of the Cauchy residue under the assumptions of the argument principle;
2. the continuous kinematics of free beta decay;
3. the Fierz identity and the norm $2|C_S|^2+6|C_T|^2$;
4. the Schur elimination $V_{4,\rm eff}=V_4-3G^2/K$;
5. the normalizations $G_E^p(0)=1$ and $G_E^n(0)=0$ for already normalized densities.

These identities have been formalized in [[../../../../formal/GDQ/BaryonicReduction.lean|GDQ/BaryonicReduction.lean]].

## 4. What is Conditional

The formulas:

$$
\frac{M_p}{M_e}
=
6\pi^5
+
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right),
$$

$$
\delta_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5},
$$

$$
r_p
=
\frac18
\left(
1+\frac{\alpha}{4}
\right)
\epsilon_{\rm eff}
\left(
\frac32\Lambda_C
\right),
$$

and the reduced formulas for $\mu_p$ and $\mu_n$ depend, respectively, on:

1. normalization of the baryonic integrand by an electronic unit;
2. identification of $\pi/2$ per stoma and the minimum impedance per volume;
3. Fredholm-Fano $3$--$4$--$5$ projection;
4. octant projection and boundary dressing;
5. reduction of the full current to the surface current.

These assumptions are geometric and do not use the experimental proton/neutron values as algebraic arguments. However, they have not all been obtained by direct evaluation of the 8D saddle point and its full Hessian. Thus, the excellent numerical errors are conditional phenomenological comparisons, not a closed blind prediction.

## 5. What is a Fit

The script `collective_surface_modes.py` determines three coefficients by least squares against the Galster parameterization. This block is:

$$
\boxed{\text{fit/benchmark of shape at intermediate }q.}
$$

It demonstrates that a Schur impedance with three modes can reproduce the reference shape. It does not demonstrate that the official Hessian has those three coefficients.

## 6. Neutron Lifetime

The formula:

$$
\tau_n
=
\frac{32}{15}
\alpha^{-11}
\frac{\hbar}{m_ec^2}
$$

is a historical reduced law. The exponent $11$ was associated in the legacy work with the number of deformation modes and $32/15$ with a volumetric projection, but these two numbers have not yet been calculated from the determinant of the baryonic Hessian and the causal jets $[z^3]F_S,[z^3]F_T$.

Thus, its status is:

$$
\boxed{
\text{conditional phenomenological ansatz, evaluated without continuous post-fitting.}
}
$$

Once the ansatz is assumed, the rate, the half-life, the phase space, and the conversion to the contracted norm $\mathcal J_3$ follow exactly. The agreement at the $10^{-3}$ level is interesting numerical evidence, but it does not close the variational derivation of the coupling.

## 7. Status Table

| Result | Status |
|---|---|
| arithmetic $6\pi^5$ | exact identity under three-chamber decomposition |
| selection of three chambers | trimodal background hypothesis |
| integer charge | theorem under meromorphy and closed boundary |
| equilibrium $(1,1,-2)$ | conservation identity of the neutral ansatz |
| proton/neutron mass | conditional geometric reduction |
| radius and moments | conditional surface reduction |
| Sachs normalizations | exact identities |
| Galster curve | fit/benchmark, not prediction |
| continuous beta kinematics | closed |
| $S,T$ base and contracted norm | structurally closed |
| physical $C_S,C_T$ | open to the full fourth variation |
| $\alpha^{-11}$ and $32/15$ | historical phenomenological ansatz |
| lifetime obtained from ansatz | direct evaluation and comparison |

## 8. Criterion for Future Promotion

The sector will be promoted from conditional reduction to complete baryonic prediction when the following are calculated, without using the targets:

$$
\Phi_B^{8D},
\qquad
K_B^{\rm phys},
\qquad
[z^3]F_S,
\qquad
[z^3]F_T,
\qquad
\mathsf R_{\rm EM}(q).
$$

These calculations must reproduce or correct the current reduced coefficients, with convergence study and sensitivity to boundary conditions.
