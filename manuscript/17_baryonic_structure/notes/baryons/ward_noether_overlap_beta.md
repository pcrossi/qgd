---
title: "Ward–Noether, outgoing modes and beta overlap"
---

# Ward–Noether, outgoing modes and beta overlap

## 1. Statement

This note preserves the correct construction of the beta sector: conservation laws determine selection, kinematics, and angular basis of beta decay, but do not determine the magnitude of the reduced coefficients on their own.

The process is:

$$
n\to p+e^-+\bar\nu_e.
$$

The official action does not receive a new fundamental vertex. The effective vertex is the projected fourth variation of the GDQ action on the surgery background:

$$
\mathcal V_{\rm eff}^{(4)}
=
\mathcal S_{\rm GDQ}^{(4)}
-
\mathcal S_{\rm GDQ}^{(3)}
K_\perp^{-1}
\mathcal S_{\rm GDQ}^{(3)}
+
\text{permutations}.
$$

## 2. Dirac–Bismut Outgoing Modes

At the boundary $S^3_r$, the reduced tangential operator used in the outgoing sector is:

$$
D_{m,-3/2}^{(j)}
=
\frac1r
\left(
2\boldsymbol\sigma\cdot\mathbf L
-
m\sigma_3
\right).
$$

For the electronic channel, $m=-1$ and $j=1/2$. The spectrum in units of $r^{-1}$ is:

$$
\{-1-\sqrt5,\ 0,\ \sqrt5-1,\ 2\}.
$$

The kernel of the block is one-dimensional; with the Peter–Weyl spectator multiplicity, the physical sector before APS projection has dimension $2$.

For the neutral torsional mode, $m=0$ and $j=0$:

$$
D_{0,-3/2}^{(0)}=0_{2\times2}.
$$

Thus the neutral kernel has dimension $2$. This is the reduced sector of the torsional antineutrino. The APS orientation and the outgoing current select the physical propagating subspace; the isolated tangential equation does not choose a unique basis.

## 3. Partial Zero Does Not Annul Decay

The overlap between only the electronic mode and the neutral mode with a scalar orbital operator can be zero. This does not imply that the complete process has a null amplitude, because the physical vertex also contains the baryonic legs $n$ and $p$.

The complete unpolarized amplitude is reduced by isotropy to two invariants:

$$
\mathcal M_0=C_SS+C_TT.
$$

A convenient basis is:

$$
S=(p^\dagger n)(e^\dagger\nu),
$$

$$
T=\sum_i(p^\dagger\sigma_i n)(e^\dagger\sigma_i\nu).
$$

Pauli algebra provides the Fierz identity:

$$
\sum_i
(\sigma_i)_{ab}
(\sigma_i)_{cd}
=
2\delta_{ad}\delta_{cb}
-
\delta_{ab}\delta_{cd}.
$$

Summing over final spins and averaging over the initial neutron spin:

$$
\frac12\langle S,S\rangle=2,
\qquad
\frac12\langle T,T\rangle=6,
\qquad
\frac12\langle S,T\rangle=0.
$$

Thus,

$$
\frac12\sum_{\rm spins}|\mathcal M_0|^2
=
2|C_S|^2+6|C_T|^2.
$$

## 4. What Ward–Noether Fixes

Temporal and spatial homogeneity provide the conservation delta:

$$
\mathcal M_{fi}
=
(2\pi)^4
\delta^{(4)}(P_f-P_i)
\widehat{\mathcal M}_{fi}.
$$

Noether charges impose:

$$
\sum_r\epsilon_r Q_{{\rm EM},r}=0,
\qquad
\sum_r\epsilon_r Q_{T,r}=0.
$$

In terms of the amputated vertex, the Ward identity has the schematic form:

$$
q_\mu\Gamma_A^\mu
=
\sum_{r\in{\rm ext}}
\epsilon_r Q_{A,r}K_r.
$$

On-shell, $K_r\psi_r=0$, so:

$$
q_\mu\Gamma_A^\mu=0.
$$

This fixes the longitudinal part and excludes channels that violate conservation. It does not fix the physical transverse part of the vertex.

In fact, for any $\lambda\in\mathbb C$,

$$
C_S\mapsto\lambda C_S,
\qquad
C_T\mapsto\lambda C_T
$$

preserves the charges, isotropy, and homogeneous identities on-shell, but changes the rate by $|\lambda|^2$:

$$
\Gamma_n\mapsto|\lambda|^2\Gamma_n.
$$

Therefore,

$$
\boxed{
\text{Noether alone does not determine }C_S,C_T.
}
$$

Closure requires the projected action:

$$
C_A
=
\frac{\hbar}{\Lambda_C^2}
\frac{2\pi i}{(4\pi)^4}
[z^3]F_A,
\qquad
A\in\{S,T\}.
$$

## 5. Causal Jets and Contracted Combination

If the causal weight and the vertex have expansions:

$$
P(z)=P_0+P_1z+\frac12P_2z^2+\frac16P_3z^3,
$$

$$
N(z)=N_0+N_1z+\frac12N_2z^2+\frac16N_3z^3,
$$

then the cubic coefficient of the product is:

$$
[z^3](PN)
=
\frac16P_0N_3
+
\frac12P_1N_2
+
\frac12P_2N_1
+
\frac16P_3N_0.
$$

For a torsional energy written as $E_T=E_0e^{-X(z)}$, with:

$$
X(z)=x_1z+\frac12x_2z^2+\frac16x_3z^3,
$$

we have:

$$
E_T'''(0)
=
E_0
\left(
-x_1^3+3x_1x_2-x_3
\right).
$$

These identities do not assign values to the physical jets; they define what must be calculated from the causal background.

## 6. Flux Projector and Quartic Schur

If $C(v)=c\cdot v$ is a linear flux constraint, the Euclidean projector onto the physical subspace is:

$$
P_Q
=
I
-
c^T(cc^T)^{-1}c.
$$

It satisfies:

$$
P_Q^2=P_Q,
\qquad
cP_Q=0.
$$

When eliminating a transverse mode $\xi$ from:

$$
\frac12K\xi^2+\frac12G\xi q^2+\frac1{24}V_4q^4,
$$

the stationary solution is:

$$
\xi_*=-\frac{G}{2K}q^2.
$$

Substituting back, the effective fourth variation is:

$$
V_{4,\rm eff}
=
V_4-\frac{3G^2}{K}.
$$

This is the elementary Schur complement that appears in the projected fourth variation.

## 7. Status

Demonstrated:

1. the reduced outgoing modes of the declared operator;
2. the existence of two angular invariants $S,T$;
3. the unpolarized norm $2|C_S|^2+6|C_T|^2$;
4. that Ward–Noether does not fix the transverse magnitude;
5. the symbolic identities of the causal jets;
6. the flux projector and the elementary quartic Schur.

Conditional:

1. the separated values of $C_S$ and $C_T$;
2. angular correlations and polarized observables;
3. direct evaluation of the jets $[z^3]F_S$ and $[z^3]F_T$ by the complete Hessian.

Self-contained verifications:

- `scripts/solve_bismut_dirac_modes_beta.py`;
- `scripts/verify_four_mode_overlap_beta.py`;
- `scripts/verify_noether_freedom_beta.py`;
- `scripts/verify_causal_jets_beta.py`;
- `scripts/verify_quartic_flux_projection_beta.py`.
