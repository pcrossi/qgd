## Calculation of the real Boltzmann weight
### 1. The Wave Function and Density in the Madelung Formalism

In traditional quantum mechanics and quantum hydrodynamics, the wave function is expressed in its polar form:
$$\psi = R e^{\frac{i S_R}{\hbar}}$$
Where $R$ is the real amplitude and $S_R$ is the real phase (Hamilton's Principal Function). The physical probability density $\rho$ is given by:
$$\rho = |\psi|^2 = R^2$$
To map the amplitude $R$ into the exponential domain of statistical mechanics and geometric entropy, the osmotic component of the action ($S_I$) is defined such that:
$$R = e^{\frac{S_I}{2\hbar}} \implies \rho = R^2 = e^{\frac{S_I}{\hbar}}$$
Substituting this representation into the original wave function, we have:
$$\psi = e^{\frac{S_I}{2\hbar}} e^{\frac{i S_R}{\hbar}} = e^{\frac{i S_R + \frac{1}{2}S_I}{\hbar}}$$
### 2. Correct Definition of Perelman's Complex Field ($f$)

In the formalism, for Perelman's conjugate volume measure ($u \propto e^{-f}$) to geometrically correspond to the quantum probability density ($\rho$), the field $f(z, \bar{z})$ must be structurally defined from the Madelung potentials as follows:
$$f(z, \bar{z}) = -\frac{S_I - i S_R}{\hbar}$$
Expanding the expression into its real and imaginary parts explicitly:
$$f = -\frac{S_I}{\hbar} + i \frac{S_R}{\hbar}$$
From this definition, the complex conjugate $\bar{f}$ (obtained by strictly inverting the sign of the imaginary unit $i$) is:
$$\bar{f} = -\frac{S_I}{\hbar} - i \frac{S_R}{\hbar}$$
### 3. Sum $f + \bar{f}$
The density calculation in Perelman's solitonic theory is based on the purely real component of the field, obtained via symmetric projection ($f + \bar{f}$). Performing the term-by-term sum:
$$f + \bar{f} = \left( -\frac{S_I}{\hbar} + i \frac{S_R}{\hbar} \right) + \left( -\frac{S_I}{\hbar} - i \frac{S_R}{\hbar} \right)$$
Grouping similar terms:
$$f + \bar{f} = \left( -\frac{S_I}{\hbar} - \frac{S_I}{\hbar} \right) + i \left( \frac{S_R}{\hbar} - \frac{S_R}{\hbar} \right)$$
Here emerges the analytical annihilation of the phase:
$$f + \bar{f} = -\frac{2 S_I}{\hbar} + i \cdot (0)$$
Therefore:
$$f + \bar{f} = -\frac{2 S_I}{\hbar}$$
### 4. Final Obtainment of $\rho(z, \bar{z})$
By definition of the invariant statistical weight in the Action, the density is given by the inverse of the exponential of half the sum:
$$\rho(z, \bar{z}) = e^{-\frac{f + \bar{f}}{2}}$$
Substituting the exact result obtained for $f + \bar{f}$:
$$\rho(z, \bar{z}) = e^{-\frac{1}{2} \left( -\frac{2 S_I}{\hbar} \right)}$$
The linear factors $\frac{1}{2}$ and $2$ cancel each other reciprocally, and the product of the negative signs results in a positive:
$$\rho(z, \bar{z}) = e^{\frac{S_I}{\hbar}}$$
Since we initially defined that $e^{\frac{S_I}{\hbar}} = R^2$ to maintain isomorphism with the fluid:
$$\rho(z, \bar{z}) = e^{\frac{S_I}{\hbar}} = R^2$$
This demonstrates that the physical probability density $\rho$ depends **exclusively** on the osmotic potential $S_I$ (which dictates the wave amplitude). The mechanical Hamilton-Jacobi phase ($S_R$) was naturally eliminated by the Hermitian conjugation operation in the complex Kähler plane, remaining strictly as the carrier of the velocity field and the current ($\mathbf{v} = \frac{\nabla S_R}{m}$), without interfering with the probabilistic scalar modulus.
