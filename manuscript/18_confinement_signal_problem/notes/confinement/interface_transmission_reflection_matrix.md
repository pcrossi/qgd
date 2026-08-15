---
title: "Interface matrix by Hessian"
---

# Interface matrix by Hessian

With Hermitian impedance $\mathsf Z=\mathsf Z^\dagger$, the Cayley transform:

$$
\mathsf S
=
(I-i\mathsf Z)(I+i\mathsf Z)^{-1}
$$

is unitary:

$$
\mathsf S^\dagger\mathsf S=I.
$$

If there is apparatus dissipation or an open channel, $\mathsf Z$ is replaced by a maximal dissipative operator, obtaining:

$$
\mathsf S^\dagger\mathsf S\le I.
$$

In GDQ, $\mathsf Z$ is the impedance extracted from the reduced physical Hessian at the interface. The minimal construction is:

$$
K_{\rm GDQ}
=
\delta^2\mathcal S_{\rm GDQ}[\Phi_\ast].
$$

The physical projector separates observable fluctuations from gauge redundancies, boundary null modes, and variations that violate conserved constraints:

$$
K_{\rm phys}
=
P_{\rm phys}K_{\rm GDQ}P_{\rm phys}.
$$

In the interface domain, the elliptic solution with Dirichlet data $\varphi$ defines the Dirichlet-to-Neumann operator:

$$
\Lambda_{\rm DtN}\varphi
=
\nabla_n\delta\Phi_\varphi\big|_{\Sigma}.
$$

The reduced impedance is then:

$$
\mathsf Z_\Sigma
=
Z_0^{-1}\Lambda_{\rm DtN}^{\rm phys},
$$

with $Z_0$ merely normalizing internal units of the reduced channel. On a closed interface without loss, $\mathsf Z_\Sigma$ is Hermitian; therefore, the Cayley transform generates a unitary $\mathsf S$. If the macroscopic apparatus or bath opens channels, the dissipative part makes $\mathsf S$ contractive.
