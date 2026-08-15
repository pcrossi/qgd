---
title: "Multiparametric calibration by invariant embedding"
---

# Multiparametric calibration by invariant embedding

## 1. Statement and status

We aim to construct the calibratable response of an apparatus without altering the fundamental action of the theory describing the object. In GDQ, the official action provides the bulk dynamics; the source, material, geometry, and boundary of the apparatus are external data of the problem.

The result of this note is exact in the quadratic sector around an admissible and stable background. Nonlinear applications require updating the background or retaining higher orders.

## 2. Quadratic and Gaussian expansion

If $\Phi_*(\boldsymbol\lambda)$ is a joint background and $\eta$ a physical fluctuation, then:

$$
\mathcal S[\Phi_*+\eta;J]
=
\mathcal S[\Phi_*]
+\frac{1}{2}\langle\eta,K_{\rm phys}\eta\rangle
-\langle J,\eta\rangle
+O(\eta^3),
$$

with:

$$
K_{\rm phys}
=
P_{\rm phys}^{\dagger}
\operatorname{Hess}_{\Phi_*}\mathcal S
P_{\rm phys}.
$$

In a finite discretization:

$$
S^{(2)}
=
\frac{1}{2}\eta^{\mathsf T}K\eta-J^{\mathsf T}\eta.
$$

Completing the square:

$$
S^{(2)}
=
\frac{1}{2}
(\eta-K^{-1}J)^{\mathsf T}
K
(\eta-K^{-1}J)
-\frac{1}{2}J^{\mathsf T}K^{-1}J.
$$

If $K>0$ in the physical subspace:

$$
\int_{\mathbb R^N}
\exp\!\left[-\frac{S^{(2)}}{\hbar}\right]d^N\eta
=
\frac{(2\pi\hbar)^{N/2}}{\sqrt{\det K}}
\exp\!\left[
\frac{1}{2\hbar}J^{\mathsf T}K^{-1}J
\right].
$$

In the continuum, the determinant only exists after the definition of the domain and a spectral regularization. The finite identity does not authorize a formal determinant without these choices.

## 3. Elimination of the interior

Separate interface data $q$ and internal modes $y$:

$$
S^{(2)}
=
\frac{1}{2}q^{\mathsf T}K_{qq}q
+q^{\mathsf T}K_{qy}y
+\frac{1}{2}y^{\mathsf T}K_{yy}y
-J_q^{\mathsf T}q
-J_y^{\mathsf T}y.
$$

The internal equation provides:

$$
y_*
=
K_{yy}^{-1}(J_y-K_{yq}q).
$$

Substituting it back into the action, the quadratic interface form is governed by:

$$
\boxed{
\text{R}
=
K_{qq}
-
K_{qy}K_{yy}^{-1}K_{yq}
}.
$$

This is the Schur complement and, in the corresponding boundary value problem, the Dirichlet-to-Neumann operator. If $K$ is positive and $K_{yy}$ is invertible, then $\text{R}$ is also positive.

## 4. Riccati as differential Schur

Consider:

$$
u'
=
A_{11}u+A_{12}p,
$$

$$
p'
=
A_{21}u+A_{22}p.
$$

Define $p=\text{R}u$. Then:

$$
p'
=
\text{R}'u+\text{R}u'.
$$

Substituting the system and eliminating $u$:

$$
\boxed{
\text{R}'
=
A_{21}
+A_{22}\text{R}
-\text{R} A_{11}
-\text{R} A_{12}\text{R}
}.
$$

The Riccati equation is, therefore, the differential version of successive Schur condensation.

## 5. Verifiable scalar example

For:

$$
S^{(2)}
=
\frac{1}{2}\int_0^L
\left[
a(u')^2+Vu^2
\right]ds
+\frac{1}{2}R_0u(0)^2,
$$

we have:

$$
-au''+Vu=0.
$$

Defining:

$$
R
=
a\frac{u'}{u},
$$

it follows:

$$
R'
=
V-\frac{R^2}{a}.
$$

With $m=\sqrt{V/a}$:

$$
\boxed{
R(L)
=
am
\frac{R_0+am\tanh(mL)}
{am+R_0\tanh(mL)}
}.
$$

This solution allows testing, without experimental data, the equivalence between the analytical solution, Riccati integration, and discrete Schur condensation.

## 6. Multiparametric extension

Consider:

$$
\frac{\partial\text{R}}{\partial\lambda_i}
=
\mathcal F_i(\text{R},\boldsymbol\lambda).
$$

The correct compatibility condition is not just commuting explicit derivatives. Since $\mathcal F_i$ depends on $\text{R}$, the curvature of the flows is:

$$
\Omega_{ij}
=
\partial_i\mathcal F_j
-\partial_j\mathcal F_i
+D_{\text{R}}\mathcal F_j[\mathcal F_i]
-D_{\text{R}}\mathcal F_i[\mathcal F_j].
$$

If:

$$
\Omega_{ij}=0,
$$

the transport is locally independent of the path in the parameter space. If $\Omega_{ij}\neq0$, the order of the preparation produces a different response. This can represent hysteresis, memory, or physically non-commuting controls; it must not be eliminated by tuning.

## 7. Identifiability

Given $D_a$ and covariances $\Sigma_a$, define:

$$
\chi^2(\boldsymbol\lambda)
=
\sum_a
r_a^{\mathsf T}\Sigma_a^{-1}r_a,
\qquad
r_a
=
D_a-\mathcal O_a(\boldsymbol\lambda).
$$

The estimator is:

$$
\widehat{\boldsymbol\lambda}
=
\operatorname*{arg\,min}_{\boldsymbol\lambda}
\chi^2(\boldsymbol\lambda).
$$

The observational Jacobian is:

$$
J_{ai}
=
\frac{\partial\mathcal O_a}{\partial\lambda_i}.
$$

In the local approximation, the information matrix is:

$$
\mathcal I
=
J^{\mathsf T}\Sigma^{-1}J.
$$

If $\mathcal I$ has full rank, the parameters can be separated locally. A deficient rank implies a degenerate family of indistinguishable apparatuses by the available data. More decimal places or a different optimizer will not resolve this degeneracy; a new observable is required.

## 8. Inference protocol

1. define theory, background, domain, source, and boundary;
2. derive $P_{\rm phys}$ and $K_{\rm phys}$;
3. calculate $\text{R}_{\rm app}(\boldsymbol\lambda)$;
4. verify stability and compatibility of the flows;
5. define $D_{\rm cal}$ and $D_{\rm test}$ beforehand;
6. estimate $\widehat{\boldsymbol\lambda}$ only on $D_{\rm cal}$;
7. freeze parameters;
8. calculate observables on $D_{\rm test}$;
9. report sensitivity, convergence, and residuals;
10. classify the outcome as calibration, comparison, or prediction.

## 9. Application outside GDQ

The method uses general mathematical structures:

$$
\text{linearized operator}
\to
\text{Schur/DtN}
\to
\text{embedding}
\to
\text{identifiability}
\to
\text{testing}.
$$

Therefore, it can be used with elasticity, Maxwell in media, acoustics, optics, transport, linearized gravity, or any other variational theory. The physical content still belongs to the starting theory. The common structure does not authorize importing operators from one theory to another.

The Schur complement, the DtN response, the Riccati flow, the invariant embedding, and the information analysis are not individual inventions of GDQ. The content proposed here is the protocol that chains them, preserving the variational origin of the operator and separating calibration from validation. Its comparative novelty should be evaluated against the literature before any historical claim.

## 10. Benchmark with cesium

In the experiment of Fein et al., the current $I$ is the physical coordinate of the apparatus in the linear regime. The integrated coil response is:

$$
C(I)
=
(10.3\ {\rm G\,m/A})I+L^2G_0,
\qquad
L=0.98\ {\rm m}.
$$

For $^{133}{\rm Cs}$:

$$
\phi_{m_F}(v,I)
=
\frac{2\pi}{d}
\frac{m_Fg_F\mu_B}{m_{\rm Cs}v^2}
C(I),
$$

$$
\frac{V(I)}{V_0}
=
\frac{
\left|
\int_0^\infty
\rho(v)
\sum_{F,m_F}
\cos[\phi_{m_F}(v,I)]\,dv
\right|
}{16}.
$$

The published skew-normal distributions were used:

| nominal series | location | scale | shape |
|---:|---:|---:|---:|
| $270\ {\rm m/s}$ | $228\ {\rm m/s}$ | $118\ {\rm m/s}$ | 4.4 |
| $380\ {\rm m/s}$ | $290\ {\rm m/s}$ | $171\ {\rm m/s}$ | 2.1 |

The centers of the markers were extracted from the vector PDF. As they are not the raw data nor do they include the original covariance table, the comparison is not given a metrological chi-squared interpretation.

The background gradient was calibrated on the even indices of the fast series:

$$
G_0^{\rm cal}
=
0.35035948\ {\rm G/m}.
$$

The article reports $0.4\ {\rm G/m}$ in the fit of the complete set. With the frozen parameter:

| set | RMSE | bias |
|---|---:|---:|
| fast calibration | 0.022693 | -0.010751 |
| retained fast test | 0.022753 | -0.003857 |
| independent slow series | 0.023745 | -0.000433 |

The validation error remains at the level of the calibration error. This constitutes initial evidence of the generalization of the instrumental method, not an exclusive validation of the GDQ ontology.

Reproducible verifications:

- [[../scripts/output_verify_immersion_calibration|Consistency between analytical solution, Riccati, and Schur]];
- [[../scripts/output_benchmark_cs_fein2022|Calibration and validation with cesium]].

## 11. Limitations

- The Hessian must be evaluated on a physical background, not a fixture.
- Null modes must be projected out before inverting $K_{yy}$.
- Losses require retarded/causal response, not just Euclidean Hessian.
- Nonlinear terms require continuation of the background.
- A single record does not identify multiple degenerate parameters.
- The cesium benchmark uses the published operational magnetic channel.
- The individual event, Born, and irreversibility are not derived by calibration alone.

## 12. Conclusion

The method separates four objects:

$$
\boxed{
\text{constants of the theory}
\neq
\text{apparatus parameters}
\neq
\text{numerical parameters}
\neq
\text{validation data}
}.
$$

Its central result is to transform calibration into a geometric problem of response, composition, and identifiable intersection, preserving the starting physical theory.
