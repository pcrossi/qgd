---
title: "Nelson derivatives and continuity equation"
type: derivation
status: stochastic-reduction
---

# Nelson derivatives and continuity equation

## 1. Forward process

Consider, in flat space and with a constant coefficient $\nu>0$,

$$
dX_t=b_+(X_t,t)dt+\sqrt{2\nu}\,dW_t.
$$

For a smooth test function $F$, Itô's formula provides the generator

$$
D_+F
=\partial_tF+b_+\cdot\nabla F+\nu\Delta F.
$$

The density $\rho$ satisfies the forward Fokker--Planck equation

$$
\partial_t\rho
=-\nabla\cdot(b_+\rho)+\nu\Delta\rho.
$$

## 2. Backward process

The future-conditioned description has a backward drift $b_-$ and generator

$$
D_-F
=\partial_tF+b_-\cdot\nabla F-\nu\Delta F.
$$

The same density satisfies

$$
\partial_t\rho
=-\nabla\cdot(b_-\rho)-\nu\Delta\rho.
$$

The opposite signs of the Laplacian encode the two conditional orientations; they do not represent two independent physical processes.

## 3. Current and osmotic velocities

Define

$$
v=\frac{b_++b_-}{2}
$$

and

$$
u=\frac{b_+-b_-}{2}.
$$

Adding the two Fokker--Planck equations and dividing by two,

$$
\boxed{
\partial_t\rho+\nabla\cdot(\rho v)=0.
}
$$

Subtracting them,

$$
0
=-\nabla\cdot[(b_+-b_-)\rho]+2\nu\Delta\rho.
$$

Thus,

$$
\nabla\cdot(\rho u-\nu\nabla\rho)=0.
$$

Under adequate decay at infinity, or with zero normal flux at the boundary and no additional solenoidal component, it follows that

$$
\rho u=\nu\nabla\rho,
$$

that is,

$$
\boxed{
u=\nu\nabla\ln\rho.
}
$$

The last equality requires the declared global conditions. The divergence equation, and not the pointwise equality, is the general result without additional hypotheses.

## 4. Symmetric acceleration

A reversible choice of mean acceleration is

$$
a
=\frac12(D_+D_-+D_-D_+)X_t.
$$

Using $b_\pm=v\pm u$, one obtains

$$
a
=\partial_tv+(v\cdot\nabla)v
-(u\cdot\nabla)u
-\nu\Delta u.
$$

If $v=\nabla S/m$, $u=\nu\nabla\ln\rho$, and the mean force is conservative, $ma=-\nabla V$, the spatial integration of this equation leads to the Hamilton--Jacobi equation with the quantum term, up to a function of time only that can be absorbed in $S$.

## 5. Status in GDQ

These identities belong to Nelson's stochastic reduction. In GDQ, they serve as a test of the hydrodynamic limit. To constitute a fundamental derivation, $b_\pm$, $\nu$, and the symmetric acceleration must emerge from the official action and the causal prescription, rather than being postulated separately.
