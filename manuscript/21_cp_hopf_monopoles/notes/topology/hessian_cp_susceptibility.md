---
title: "CP Hessian and topological susceptibility"
---

# CP Hessian and topological susceptibility

The parameter that measures the rigidity of the vacuum against CP shifts is the topological susceptibility. In the effective formulation:

$$
\chi_{\rm top}^{\rm GDQ}
=
\left.
\frac{\partial^2E_{\rm vac}(\theta)}
{\partial\theta^2}
\right|_{\theta=0}.
$$

Since the energy depends on the topological charge:

$$
Q_C
=
\int_N q_C,
$$

the same quantity can be written as a correlation function:

$$
\chi_{\rm top}^{\rm GDQ}
=
\int d^4x\,
\langle q_C(x)q_C(0)\rangle_{\rm GDQ}.
$$

In the language of the official action, this is the curvature of the effective functional after projecting the second variation onto the torsional angular mode. If $\Phi_\ast=(g_\ast,J_\ast,H_\ast,f_\ast,\mathcal U_\ast)$ is the admissible background, the relevant physical operator is:

$$
K_{\rm CP}^{\rm phys}
=
P_{\rm phys}
\delta^2\mathcal S_{\rm GDQ}[\Phi_\ast]
P_{\rm phys}.
$$

The normalized angular mode is represented by a direction $\eta_B$ in the space of torsional fluctuations:

$$
\delta H
=
\eta_B\,\delta\vartheta_B.
$$

The direct susceptibility of GDQ is then the quadratic form:

$$
\chi_{\rm top}^{\rm GDQ}
=
\langle
\eta_B,
K_{\rm CP}^{\rm phys}
\eta_B
\rangle_{\mathcal U_\ast}.
$$

This statement separates three levels:

1. the periodicity, which is topological;
2. the relaxation, which depends on $\chi_{\rm top}^{\rm GDQ}>0$;
3. the metrology, which requires evaluating $K_{\rm CP}^{\rm phys}$ on the strong background.

For the periodic potential:

$$
V(\theta)
=
\chi_{\rm top}^{\rm GDQ}
(1-\cos\theta),
$$

the reduced angular Hessian is:

$$
\frac{d^2V}{d\theta^2}
=
\chi_{\rm top}^{\rm GDQ}\cos\theta.
$$

At the CP minimum:

$$
\left.
\frac{d^2V}{d\theta^2}
\right|_{\theta=0}
=
\chi_{\rm top}^{\rm GDQ}
>
0.
$$

At the unstable maximum:

$$
\left.
\frac{d^2V}{d\theta^2}
\right|_{\theta=\pi}
=
-
\chi_{\rm top}^{\rm GDQ}
<
0.
$$

Therefore, the positivity of the physical Hessian in the torsional channel is exactly the mathematical condition that makes $\theta=0\pmod{2\pi}$ a stable attractor.
