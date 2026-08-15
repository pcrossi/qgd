---
title: "Local Perelman--Madelung map and limits"
type: conditional-theorem
status: locally-demonstrated
---

# Local Perelman--Madelung map and limits

This note records the precise correspondence between the complex field used in GDQ and the Madelung variables. It does not transform Perelman's functional into a physical action. The term "Perelman" here identifies the weighted geometric grammar of the measure; the physical action remains $\mathcal S_{\rm GDQ}$.

## 1. Regular domain

Let $\Omega\subset M$ be an open set in which:

$$
\rho(x)>0,
\qquad
f\in C^2(\Omega),
\qquad
g\in C^2(\Omega),
$$

and where the phase $S_R$ can be chosen as a local single-valued function. We call this open set the regular Madelung domain:

$$
\mathcal D_{\rm reg}
=
\left\{
(g,f):
\rho=e^{-(f+\bar f)/2}>0,
\quad
S_R=\frac{\hbar}{2i}(f-\bar f)
\text{ locally defined}
\right__.
$$

## 2. Direct map

In the regular domain, the complex field determines density and phase by

$$
\rho=e^{-(f+\bar f)/2},
$$

and

$$
S_R=\frac{\hbar}{2i}(f-\bar f).
$$

We can also write the amplitude and the projective function:

$$
R=\sqrt\rho,
\qquad
\Psi=R\,e^{iS_R/\hbar}.
$$

Thus, the direct map is

$$
(g,f)
\longmapsto
(g,\rho,S_R,\Psi).
$$

If the action measure is also considered, then

$$
\mathcal U
=\frac{\rho}{(4\pi z_\tau)^n}.
$$

## 3. Local inverse map

Given a regular pair $(\rho,S_R)$, with $\rho>0$, we define

$$
f=-\ln\rho+i\frac{S_R}{\hbar}.
$$

Then

$$
\bar f=-\ln\rho-i\frac{S_R}{\hbar}.
$$

Adding them,

$$
f+\bar f=-2\ln\rho,
$$

therefore

$$
e^{-(f+\bar f)/2}
=e^{\ln\rho}
=\rho.
$$

Subtracting them,

$$
f-\bar f=2i\frac{S_R}{\hbar},
$$

and therefore,

$$
\frac{\hbar}{2i}(f-\bar f)=S_R.
$$

Thus, once the local branch of the phase is fixed, the map is locally invertible.

## 4. Preservation of equations in the reduced sector

In the sector where the physical bridge has reduced the action to the canonical Madelung form,

$$
I_{\rm Mad}
=
\int dt\int_\Sigma
\left[
\rho
\left(
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
\right)
+\frac{\hbar^2}{8m}
\frac{|\nabla\rho|^2}{\rho}
\right]d^dx,
$$

the variation in $S_R$ yields

$$
\partial_t\rho+\nabla\cdot(\rho v)=0,
\qquad
v=\frac{\nabla S_R}{m},
$$

and the variation in $\rho$ yields

$$
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=0.
$$

These two equations are the Madelung representation. The preservation of the equations holds in this reduced sector; it does not assert that every off-shell solution of the official action is already in this canonical polarization.

## 5. Injectivity and surjectivity

Locally, with fixed $g$, chosen phase branch, and normalized $\rho$, the map $f\mapsto(\rho,S_R)$ is injective. Indeed,

$$
\operatorname{Re}f=-\ln\rho,
\qquad
\operatorname{Im}f=\frac{S_R}{\hbar}.
$$

Globally, there is phase ambiguity:

$$
S_R\sim S_R+2\pi\hbar k,
\qquad
k\in\mathbb Z.
$$

Therefore, if the phase is taken modulo $2\pi\hbar$, one must choose a branch, chart, or topological class to recover $f$ globally.

The map is also not surjective over all abstract quantum states. States with nodes, multivalued phases, spinorial sectors, gauge sectors, or non-trivial bundles require additional data.

## 6. Nodes

At a node,

$$
\rho=0.
$$

Then $\ln\rho$ diverges and

$$
f=-\ln\rho+i\frac{S_R}{\hbar}
$$

is not regular. Furthermore, the term

$$
\frac{\Delta\sqrt\rho}{\sqrt\rho}
$$

can diverge. The correct treatment is to remove the nodal set:

$$
\Omega^\ast=\Omega\setminus\{\rho=0\},
$$

work with charts on each connected component, and impose topological compatibility around the nodes. In GDQ, these sets can be read as defects, effective boundaries, or stomata, depending on the problem.

## 7. Multivalued phase

If

$$
\oint_\Gamma\nabla S_R\cdot dx
=2\pi\hbar N,
\qquad
N\in\mathbb Z,
$$

then $S_R$ is not a global single-valued function, but $e^{iS_R/\hbar}$ remains single-valued. In local charts $U_a$,

$$
S_R^{(a)}-S_R^{(b)}
=2\pi\hbar k_{ab},
$$

and therefore,

$$
f^{(a)}-f^{(b)}
=i\,2\pi k_{ab}.
$$

Thus, the multivalued phase does not invalidate the local map; it requires atlases and topological data.

## 8. Superposition

The Madelung transformation is non-linear. If

$$
\Psi=\Psi_1+\Psi_2,
$$

it does not follow that

$$
\rho=\rho_1+\rho_2,
\qquad
S_R=S_{R,1}+S_{R,2}.
$$

In fact,

$$
\rho
=|\Psi_1+\Psi_2|^2
=\rho_1+\rho_2
+2\sqrt{\rho_1\rho_2}
\cos\left(\frac{S_1-S_2}{\hbar}\right),
$$

and

$$
S_R=\hbar\,\arg(\Psi_1+\Psi_2).
$$

Therefore, superposition must be performed in $\Psi$ and only then translated to $(\rho,S_R)$. Destructive interference can create nodes, at which the regular chart must be replaced.

## 9. Final status

The Perelman--Madelung map of GDQ is:

- local;
- regular;
- sectorial;
- invertible only after choice of branch and geometric data;
- preserving the equations only in the reduced Madelung sector.

It is not a global bijection of the entire theory.
