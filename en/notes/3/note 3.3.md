### Momentum Complexification and the Kähler 1-Form

In the adopted geometric formalism, we define spacetime as a Kähler manifold equipped with a complex Hermitian metric $\tilde{g}_{\mu\nu} = g_{\mu\nu} + iB_{\mu\nu}$ and a Cartan affine connection containing an irreducible topological torsion $T^\lambda_{\mu\nu}$. Under this structure, the matter field (hydrodynamic soliton) is no longer modeled by abstract amplitudes in a Hilbert space, and is instead described in its classical polar representation by the fluid:
$$\Psi(z) = \sqrt{\rho(z)} e^{\frac{i}{\hbar} S_R(z)},$$
where $\rho(z)$ represents the vacuum fluid's volumetric probability density and $S_R(z)$ denotes the Real Action, physically identified as Hamilton's Principal Function.

To unify the diffusive statistical dynamics and the directional inertia of the field into a single continuous geometric object, we isomorphically map this wave function onto the Unified Complex Action $S_C$ through a pure exponential relation:
$$\Psi(z) = e^{\frac{i}{\hbar} S_C(z)}.$$
Equating both representations with the objective of isolating the complexified action functional, the constraint is established:
$$e^{\frac{i}{\hbar} S_C} = \sqrt{\rho} e^{\frac{i}{\hbar} S_R}.$$
Applying the analytic continuation of the complex logarithm to both sides of the equation, we obtain the separation of components:
$$\frac{i}{\hbar} S_C = \ln\left(\rho^{1/2}\right) + \frac{i}{\hbar} S_R.$$
Multiplying the entire expression by $-i\hbar$ to purify the linear translation term, the algebra performs the direct extraction of $S_C$:
$$S_C = S_R - i\hbar \ln\left(\rho^{1/2}\right) = S_R - i \frac{\hbar}{2} \ln\rho.$$
By defining the imaginary component of the action — directly associated with the osmotic potential and the stochastic diffusion terms of the vacuum — as $S_I = -\frac{\hbar}{2} \ln\rho$, the structure cleanly consolidates into the canonical linear decomposition:
$$S_C = S_R + i S_I.$$
The extension of the momentum variables to the complex 1-form $\omega$ naturally emerges when we apply the covariant exterior derivative operator $\nabla_\mu$ to the unified action $S_C$. This operator acts compulsorily coupled to the asymmetric affine connection with Cartan torsion, shielding the integrability of the field along the complex geodesics of the manifold:
$$\omega = p_\mu dx^\mu = \nabla_\mu S_C \, dx^\mu = \nabla_\mu \left( S_R - i \frac{\hbar}{2} \ln\rho \right) dx^\mu.$$
Distributing the linear differentiation operator over the real and imaginary parts of the functional, we have:
$$\omega = \left( \nabla_\mu S_R \right) dx^\mu - i \frac{\hbar}{2} \left( \nabla_\mu \ln\rho \right) dx^\mu.$$
Applying the chain rule to the logarithmic gradient that dictates the density's kinetic profile ($\nabla_\mu \ln\rho = \frac{1}{\rho} \nabla_\mu \rho$), the final expanded form of the 1-form is rigorously established by:
$$\omega = \nabla_\mu S_R \, dx^\mu - i \frac{\hbar}{2\rho} \nabla_\mu \rho \, dx^\mu.$$
Substituting the fundamental dynamic variables of the fluid — where we identify the classical mechanical current momentum (responsible for regular ballistic transport) as $p_\mu^{\text{c}} = \nabla_\mu S_R$ and the osmotic fluctuation momentum towards equilibrium as $u_\mu = -\frac{\hbar}{2\rho} \nabla_\mu \rho$ —, the 1-form assumes its unified complex canonical signature:
$$\omega = (p^{\text{c}}_\mu + i u_\mu) dx^\mu.$$
The osmotic term $i u_\mu$ does not constitute an externally added portion to the 1-form, but rather the intrinsic imaginary component of the complexified momentum vector itself $p_\mu = p_\mu^{\text{c}} + i u_\mu$. This deduction demonstrates that quantum oscillation and statistical density do not operate disjointly; the fluid's momentum is intrinsically coupled to the geometric torsion of the local spacetime, proving that the abstract "spin" of the quantum phase maps as a continuous structural micro-twisting of the metric fabric itself along the soliton's path.
