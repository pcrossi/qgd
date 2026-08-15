---
title: "Audit of the canonical term rho d_t S_R"
---

# Audit of the canonical term $\rho\,\partial_tS_R$

## Statement

We want to verify whether the temporal pullback of the official action directly implies:

$$
\Theta_{\Sigma}=\int_{\Sigma}\rho\,\delta S_R\,d\Sigma
$$

and, consequently, a reduced action containing:

$$
\int dt\int_{\Sigma_t}\rho\,\partial_tS_R\,d\Sigma_t.
$$

The direct answer is negative: the official action produces a momentum proportional to the normal derivative of the phase. Equality with $\rho$ requires a dynamic condition or an additional polarization, which must be derived.

## Current obtained from the official action

With

$$
f=-\ln\rho+\frac{i}{\hbar}S_R,
$$

the measure $\mathcal U$ does not depend on $S_R$. The variation of the phase yields:

$$
\widehat J_S^\mu
= \frac{2\tau}{\hbar\Lambda_C^2}
\mathcal U\,g^{\mu\bar\nu}\partial_{\bar\nu}S_R.
$$

If $n$ is the unit normal vector selected by the synchronized clock-form, the pre-symplectic potential of the phase on a sheet $\Sigma$ is:

$$
\Theta_{\Sigma,S}
=\int_\Sigma\Pi_{S_R}\,\delta S_R\,d\Sigma,
$$

where

$$
\Pi_{S_R}
=n_\mu\widehat J_S^\mu
=\frac{2\tau}{\hbar\Lambda_C^2}
\mathcal U\,n_\mu g^{\mu\bar\nu}\partial_{\bar\nu}S_R.
$$

Using

$$
\mathcal U=\frac{\rho}{(4\pi z_\tau)^n},
$$

we obtain

$$
\Pi_{S_R}
=\rho\,
\frac{2\tau}{\hbar\Lambda_C^2(4\pi z_\tau)^n}
n_\mu g^{\mu\bar\nu}\partial_{\bar\nu}S_R.
$$

Therefore,

$$
\boxed{\Pi_{S_R}\neq\rho\quad\text{in general}.}
$$

## Why internal normalization is not enough

If $K$ represents the internal directions, the charge density transported to the laboratory is the pushforward:

$$
\varrho_{\rm lab}(x)=\int_K\Pi_{S_R}(x,y)\,dV_K,
$$

while the geometric marginal is obtained from the pushforward of $\mathcal U$. The normalization of the internal conditional distribution does not eliminate the factor $n\cdot dS_R$. A constant phase yields $\Pi_{S_R}=0$ even when $\rho>0$ and the internal measure is normalized. Therefore,

$$
\boxed{
\int_K\mathcal U\,dV_K=1
\quad\not\Rightarrow\quad
\varrho_{\rm lab}=\rho_{\rm lab}.
}
$$

## Exact closure condition

The canonical identity requires, after the causal and internal pushforward:

$$
\boxed{\Pi_{S_R}^{\rm lab}=\rho_{\rm lab}.}
$$

In the factored case, this is equivalent to the weighted condition:

$$
\frac{2\tau}{\hbar\Lambda_C^2(4\pi z_\tau)^n}
\left\langle
n_\mu g^{\mu\bar\nu}\partial_{\bar\nu}S_R
\right\rangle_K=1.
$$

It is also necessary to choose a physical polarization that eliminates or relates the conjugate momentum of the amplitude $u=-\ln\rho$. This condition must follow from an internal structure of GDQ, such as a causal boundary flux constraint, a Routh reduction under fixed Noether charge, a derived boundary polarization, or an identity of the complete stationary solution.

## First-order form

The second-order action can be rewritten in Hamiltonian form by Legendre transformation, without adding a new fundamental action:

$$
I_{\rm red}
=\int dt\int_{\Sigma_t}
\left(
\Pi_{S_R}^{\rm lab}\,\partial_tS_R
-\mathcal H_{\rm red}
\right)d\Sigma_t.
$$

The Madelung term appears exactly if the dynamics or the physical constraint selects:

$$
\Pi_{S_R}^{\rm lab}=\rho_{\rm lab;.
$$

The Legendre transformation explains how a temporal linear term can arise from an originally quadratic action, but it does not prove by itself the identification of the momentum with the density.

## Routh reduction and variational inequality

There is a stronger route that does not need to assume a monoenergetic phase beforehand. Suppose that the synchronized pullback and the internal integration reduce the temporal Hamiltonian to:

$$
H_t[\Pi,\rho]
=\int_\Sigma\frac{\Pi^2}{2A\rho}\,d\Sigma,
\qquad A>0
$$

with constant $A$. Define:

$$
Q_S=\int_\Sigma\Pi\,d\Sigma,
\qquad
N_\rho=\int_\Sigma\rho\,d\Sigma.
$$

By Cauchy--Schwarz,

$$
Q_S^2
\leq
\left(\int_\Sigma\frac{\Pi^2}{\rho}\,d\Sigma\right)
\left(\int_\Sigma\rho\,d\Sigma\right),
$$

and, therefore,

$$
H_t\geq\frac{Q_S^2}{2A N_\rho}.
$$

Equality occurs if, and only if,

$$
\Pi=\frac{Q_S}{N_\rho}\rho
$$

almost everywhere. Thus, if the primitive phase charge and the density normalization are derived independently as:

$$
Q_S=N_\rho=1,
$$

the minimizer will satisfy:

$$
\Pi=\rho.
$$

This is a legitimate conditional variational proof. To apply it to GDQ, it is still necessary to demonstrate directly in the pullback that:

1. $A$ is constant on the physical support;
2. lapse, shift, and internal modes do not produce cross terms;
3. there is no boundary flux leakage;
4. $\rho>0$ on the connected support;
5. $Q_S=1$ is fixed independently as a primitive sector, and not chosen afterward to obtain the equality;
6. the background is the minimizer of the convex sector.

If $A=A(x)$, the minimizer is proportional to $A(x)\rho(x)$, not to $\rho(x)$. If $Q_S=1$ is only a renormalization chosen after $N_\rho=1$, the argument will be circular.

## Why the stationary ansatz is not enough

The ansatz $S_R=-Et+\sigma$ yields $\Pi=Z_E\rho$ only when the frequency, the lapse, and the pushforward are uniform. Equating $Q_S=N_\rho=1$ afterward fixes $Z_E=1$, but does not prove that the phase charge is primitively unitary. Furthermore, the temporal translation and phase shifting charges are distinct Noether charges. Therefore, this route defines a possible on-shell sector, but does not constitute the sought-after general proof.

## ADM calculation and preservation test

Suppose provisionally that the causal pushforward is local in $t$. With

$$
ds^2=-N^2dt^2+h_{ij}(dx^i+N^idt)(dx^j+N^jdt)
$$

and $D_tS_R=\partial_tS_R-N^i\partial_iS_R$, the phase sector assumes the form:

$$
L_S=\frac A2N\sqrt h\,\rho
\left[-(D_tS_R/N)^2+h^{ij}\partial_iS_R\partial_jS_R\right].
$$

Therefore,

$$
\Pi_{S_R}=-A\sqrt h\,\rho\frac{D_tS_R}{N}.
$$

The desired densitized equality is equivalent to:

$$
\Pi_{S_R}=\sqrt h\rho
\quad\Longleftrightarrow\quad
-A\frac{D_tS_R}{N}=1.
$$

The amplitude sector also has regular temporal kinetics:

$$
L_\rho=\frac{A\hbar^2}{2}N\sqrt h
\left[-\frac{(D_t\rho/N)^2}{\rho}+\frac{|D\rho|^2}{\rho}\right],
$$

with independent momentum

$$
p_\rho=-A\hbar^2\sqrt h\frac{D_t\rho/N}{\rho}.
$$

Thus, the temporal Hessian in $(\partial_tS_R,\partial_t\rho)$ is regular for $A\rho\neq0$. The condition

$$
C:=\Pi_{S_R}-\sqrt h\rho=0
$$

is not a primary constraint of the official action. Its Hamiltonian equations show that $\dot C=0$ imposes an additional condition involving $p_\rho$, sheet expansion, shift, and spatial flux of the phase; it does not vanish identically on $C=0$.

In the comoving stationary sector,

$$
N^i=0,
\quad D_iS_R=0,
\quad\dot\rho=\dot h=0,
\quad p_\rho=0,
$$

$C=0$, once selected initially, is preserved. The Routh inequality shows that this sheet is the minimizer in the uniform sector of fixed charge, but does not derive its initial normalization.

## Causal obstruction to the calculation of $A$

The corpus defines $z_\tau=\tau+i\nu_0t$, but does not provide a complete map:

$$
\gamma:t\longmapsto\tau_\gamma(t)
$$

nor an identity that determines

$$
\gamma^*\left(\frac{d\tau}{\tau}\right)
$$

as a function of $dt$. Synchronization fixes the direction, the unit, and the orientation of the local clock, but not this causal Jacobian. The historical Laurent projector normalizes an already constant coefficient; it does not demonstrate the factorization of the phase momentum. Therefore, $A$ cannot yet be evaluated without completing the causal pullback.

## Final verdict

$$
\boxed{
\text{The phase current and pre-symplectic potential are derived.}
}
$$

$$
\boxed{
\text{Stationary } C_3\text{: }\Pi_{S_R}=\rho
\text{ can be selected and is conditionally preserved.}
}
$$

$$
\boxed{
\text{General dynamics: }\Pi_{S_R}=\rho
\text{ is neither constraint nor identity of the official action.}
}
$$

A general derivation would require the causal pullback to produce a degenerate reduction or a physical polarization that eliminates half of the canonical data. This structure is not demonstrated in the current formulation.

## Audit of the Killing--Perelman attempt

A subsequent proposal tried to close the two remaining conditions by Killing isometry and Perelman monotonicity. It preserves a useful idea, but does not constitute a proof.

First, from $\mathcal L_Kg=0$ it does not follow that:

$$
\Delta\kappa=0.
$$

The Killing equation controls the metric along $K$; it does not provide an elliptic equation for the independent Jacobian $\kappa=d\tau_\gamma/dt$. Furthermore, even if $\tau_\gamma(t)=at+b$, we would have:

$$
\gamma^*\left(\frac{d\tau}{\tau}\right)
=\frac{a}{at+b}\,dt,
$$

which is not constant. A constant coefficient in $d\tau/\tau$ would require an exponential law for $\tau_\gamma$, not an affine law. This law must come from the causal dynamics, not from the isolated flat isometry.

Second, the monotonicity of an auxiliary Perelman functional in $\tau$ does not imply that the physical momentum $p_\rho$ decays in $t$. It also does not demonstrate:

1. convergence of all initial data to a single soliton;
2. identification of the soliton with the minimum of the Routh Hamiltonian;
3. saturation of the Cauchy--Schwarz inequality;
4. physical relaxation of an apparatus;
5. equivalence between the geometric flow in $\tau$ and temporal dissipation in $t$.

The valid part of the proposal remains the Routh inequality. It proves the form of the minimizer if the system is already in the declared convex sector; it does not prove that Perelman dynamically selects this sector.

## Audit of the scale--adiabatic elimination route

A second proposal replaced Killing--Perelman with a clock homomorphism and adiabatic elimination. It improves the separation between $\tau$ and $t$, but still does not close the proof.

If it is demonstrated or adopted that the causal map is a continuous homomorphism:

$$
\gamma:(\mathbb R,+)\longrightarrow(\mathbb R_+,\times),
$$

then

$$
\gamma(t+s)=\gamma(t)\gamma(s)/\gamma(0)
$$

implies rigorously:

$$
\tau_\gamma(t)=\tau_0e^{\kappa t}
$$

and

$$
\gamma^*\left(\frac{d\tau}{\tau}\right)=\kappa\,dt.
$$

The mathematical result is correct. However, the invariance of $d\tau/\tau$ and the homogeneity of the ticks do not demonstrate, by themselves, that the physical map must preserve the group law. This composition compatibility must be derived from the causal construction or declared as a clock condition. It also does not fix the value of $\kappa$, nor, by itself, all factors of $A$.

The effective equation

$$
\dot p_\rho=-\Gamma p_\rho-\frac{\delta H_t}{\delta\rho}
$$

does not yet follow from the official action. To obtain it by elimination of the apparatus, it is necessary to calculate its influence functional and demonstrate the positivity of the dissipative kernel, noise compatible with fluctuation--dissipation, separation of scales, Markovian approximation, and the gap of the fast sector. Furthermore, $p_\rho\to0$ and $N^i\to0$ do not imply by themselves that the distribution $\Pi_{S_R}$ minimizes $H_t$ at fixed charge. It is necessary to derive a closed equation for this mode or a Lyapunov functional whose equality selects Routh.

Thus, the causal part is a simple conditional theorem; the dissipative part is a calculable program of measurement theory, not an already completed proof.

## Exact theorem in Kähler state space

There is an intrinsic and exact origin for the pair $(\rho,S_R)$ in the state space. Define:

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
$$

Then

$$
\delta\Psi
=e^{iS_R/\hbar}
\left(
\frac{\delta\rho}{2\sqrt\rho}
+\frac{i\sqrt\rho}{\hbar}\delta S_R
\right),
$$

and, therefore,

$$
\hbar\operatorname{Im}(\bar\Psi\,\delta\Psi)
=\rho\,\delta S_R.
$$

Integrating on the physical sheet,

$$
\boxed{
\Theta_{\rm state}
=\hbar\operatorname{Im}\langle\Psi,\delta\Psi\rangle
= \int_\Sigma\rho\,\delta S_R\,d\Sigma.
}
$$

Hence,

$$
\boxed{
\Omega_{\rm state}
=\delta\Theta_{\rm state}
=\int_\Sigma\delta\rho\wedge\delta S_R\,d\Sigma.
}
$$

The same result appears directly in the weighted geometry of the target. With $u=-\ln\rho$ and $v=S_R/\hbar$, the metric

$$
G=\rho(du^2+dv^2)
$$

has compatible form:

$$
\omega_T=\rho\,du\wedge dv
=-\frac1\hbar d\rho\wedge dS_R.
$$

Thus, $(\rho,S_R)$ are natural Darboux coordinates in the space of normalized states, after removing the constant phase.

## Non-automatic identification theorem

The previous result does not automatically coincide with the covariant form of the official action. The latter is:

$$
\Omega_{\rm GDQ}
= \int_\Sigma
\left(
\delta\Pi_{S_R}\wedge\delta S_R
+\delta p_\rho\wedge\delta\rho
+\text{metric sector}
\right).
$$

$\Omega_{\rm state}$ lives on the space of normalized configurations; $\Omega_{\rm GDQ}$ lives on the cotangent bundle of the Cauchy data. Furthermore, the Hessian of the official action in the velocities is non-degenerate, while a first-order action $\rho\dot S_R-H$ has a degenerate temporal Hessian. A total derivative or a boundary term does not change this rank.

Therefore, under the current axioms, one cannot conclude:

$$
\Omega_{\rm GDQ}^{\rm phys}=\Omega_{\rm state}
$$

without deriving an invariant dynamic submanifold that eliminates the amplitude pair and relates $\Pi_{S_R}$ to $\rho$. Kähler geometry demonstrates exactly the candidate canonical pair; the official action does not yet demonstrate that its entire Cauchy space reduces to this pair.
