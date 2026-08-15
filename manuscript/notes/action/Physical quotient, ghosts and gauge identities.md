---
title: "Physical quotient, ghosts and gauge identities"
---

# Physical quotient, ghosts and gauge identities

## 1. The geometric problem

If $\eta$ is a fluctuation and $R\epsilon$ is an infinitesimal gauge direction,

$$
\eta\sim\eta+R\epsilon.
$$

The raw Hessian has null modes along the orbit. The physical space is the quotient

$$
\mathcal V_{\rm phys}
=\ker C\cap\mathcal D_{\rm boundary}\big/\operatorname{Im}R,
$$

where $C$ gathers the linear constraints. Once the weighted inner product of the action is chosen, one can represent this quotient by an orthogonal projector $P_{\rm phys}$ and define

$$
\mathbb H_{\rm phys}
=P_{\rm phys}\mathbb HP_{\rm phys}.
$$

This is the intrinsic operator. No ghost fields have been introduced.

## 2. Gauge coordinates and Jacobian

A condition $F[A]=0$ locally chooses a section of the orbit. Inserting this section into the functional integral yields:

$$
1
=\Delta_{\rm FP}[A]
\int\mathcal Dg\,\delta(F[A^g]),
$$

with

$$
\Delta_{\rm FP}[A]
=\det M_A,
\qquad
M_A
=\left.\frac{\delta F[A^g]}{\delta\epsilon}\right|_{\epsilon=0}.
$$

The determinant is the Jacobian of the coordinate change between the total space and the local product "section times orbit". The identity

$$
\det M_A
=\int\mathcal D\bar c\,\mathcal Dc\,
e^{-\langle\bar c,M_Ac\rangle}
$$

is an algebraic representation of this Jacobian. It does not transform $c$ and $\bar c$ into material excitations.

In the $U(1)$ sector, with $F[A]=\partial^\mu A_\mu$,

$$
M_A=-\partial^2,
$$

independent of $A$. Its determinant is a common constant across configurations and does not contribute to the polarization.

## 3. Ward identity without dynamic ghosts

If

$$
L_{A^g}=g^{-1}L_Ag,
$$

then, by functional calculus,

$$
F_\tau(L_{A^g})
=g^{-1}F_\tau(L_A)g.
$$

The cyclicity of the trace yields:

$$
\Gamma_\tau[A^g]
=\operatorname{Tr}F_\tau(L_{A^g})
=\operatorname{Tr}F_\tau(L_A)
=\Gamma_\tau[A].
$$

For $U(1)$, $\delta A_\mu=\partial_\mu\varepsilon$. Therefore,

$$
0=\delta_\varepsilon\Gamma_\tau
=\int d^dx\,
\frac{\delta\Gamma_t}{\delta A_\mu}
\partial_\mu\varepsilon.
$$

Integrating by parts and using arbitrary $\varepsilon$,

$$
\partial_\mu
\frac{\delta\Gamma_\tau}{\delta A_\mu}=0.
$$

A new functional derivative with respect to $A_\nu$ and the Fourier transform give

$$
q^\mu\Pi_{\mu\nu}^{(\tau)}(q)=0.
$$

## 4. Non-abelian extension

In the non-abelian case, the orbit, the gauge condition, and the Jacobian are covariant with respect to the background. The invariance of the effective functional is encoded by the identity

$$
\mathcal S(\Gamma_\tau)=0.
$$

Its expanded form is the Slavnov--Taylor identity. BRST provides a convenient cohomological notation to demonstrate it; the GDQ construction can equally maintain it as a geometric identity of the quotient and the covariant operator.

## 5. Logical conclusion

The demonstrated result is not that "a determinant magically cancels all modes". It is more precise:

1. the gauge modes are removed by quotient or physical projector;
2. a gauge section introduces a geometric Jacobian;
3. ghosts are an optional representation of this Jacobian;
4. spectral covariance produces Ward and Slavnov--Taylor;
5. therefore, ghosts are not fundamental ontology of GDQ.

The closure holds in the sectors and domains where the covariant operator and the physical quotient have been constructed. It is not an indiscriminate statement about any singular background.
