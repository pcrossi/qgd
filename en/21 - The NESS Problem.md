# Chapter 21 - Non-Equilibrium Steady States (NESS) and the Emergence of Irreversibility

The formalism of [[02 - The Geometrization of Matter|Quantum Geometrodynamics (QGD)]] describes the physical vacuum and its elementary solitonic excitations as open dynamic systems coupled to the [[12 -  The Quantum Tunneling Time (Hartman Effect)|Kähler lattice]]. One of the major conceptual challenges of the theory lies in the apparent contradiction between the unitary and reversible stability of individual solitons and macroscopic thermodynamic irreversibility.

In this chapter, this tension is resolved by demonstrating how the microscopic Non-Equilibrium Steady States (NESS) in the [[17 - Monotonicity under Cartan Torsion|Perelman vacuum]] give rise to the Second Law of Thermodynamics in the macroscopic limit through processes of coarse-graining and phase scattering.

---

## 21.1 The NESS Fixed Point and Detailed Micro-Balance

At the elementary scale of the soliton ($\sim 10^{-15}\text{ m}$), the metric evolution under the Ricci flow modified by the DeTurck vector is balanced by the force term of the [[03 - Complex Causality and the End of the Wick Paradox|Sudarshan advanced potential]]. We define the local density of Perelman geometric entropy production $\sigma_{\mathcal{W}}$ as:
$$\sigma_{\mathcal{W}} = 2 |R_{ij} + \nabla_i \nabla_j f|_{g}^2 e^{-f}$$

In the fixed point regime (isolated soliton), the restrictions of the Sudarshan potential act as a counterterm to the [[01 - The Initial Problem - The Divergence between the Feynman and Wiener Integrals|parabolic dissipative Ricci flow]]. The global integral of the entropy functional $\mathcal{W}$ yields:
$$\frac{d\mathcal{W}}{d\tau}\Big|_{\text{soliton}} = \int_{\mathcal{M}} \sigma_{\mathcal{W}} dV - \Phi_{\text{Sudarshan}} = 0$$

At this fundamental scale, unitarity is preserved and there is no macroscopic arrow of time; the soliton is a stable and eternal structure immersed in the quantum vacuum, characterizing a Non-Equilibrium Steady State (NESS) with zero net entropy production.

---

## 21.2 The Vacuum Fano Scattering Mechanism

The breaking of time symmetry and the consequent emergence of irreversibility begin when the soliton interacts with the continuous fluctuations of the Kähler lattice. The interaction of the discrete solitonic state $|\phi_D\rangle$ (energy $E_D$) with the continuum of vacuum wave modes $|\psi_E\rangle$ (energy $E$) is described through the coupling Hamiltonian:
$$H = E_D |\phi_D\rangle\langle \phi_D| + \int dE \, E |\psi_E\rangle\langle \psi_E| + \int dE \left( V_E |\phi_D\rangle\langle \psi_E| + V_E^* |\psi_E\rangle\langle \phi_D| \right)$$

Where $V_E$ represents the transition matrix element induced by perturbations of the local metric $\delta g_{ij}$. When phase perturbations that do not obey the strict quantization condition ($\oint \omega \neq n h$) fall upon the soliton, they undergo scattering.

The phase scattering matrix $S(E)$ exhibits an asymmetric Fano resonance profile for the transmission of curvature fluctuations:
$$\sigma(E) = \frac{(q + \epsilon)^2}{1 + \epsilon^2}$$

Where $\epsilon = \frac{E - E_D - \Delta E}{\Gamma_{\text{Fano}}/2}$ is the normalized energy and $q$ is the Fano asymmetry parameter. The decay width $\Gamma_{\text{Fano}}$, which measures the coupling and phase dissipation rate to the Kähler vacuum, is given by:
$$\Gamma_{\text{Fano}} = 2\pi |V_{E_D}|^2$$

Any misaligned phase perturbation is ejected radially from the soliton towards the asymptotic boundary as transient gauge radiation, representing an irreversible loss of holomorphic phase to the infinite Kähler continuum.

---

## 21.3 The Zwanzig-Mori Coarse-Graining over the Vacuum

To formalize the transition to the macroscopic many-body scale, we resort to the Zwanzig-Mori projection formalism. Let $\rho(\Gamma)$ be the probability density in the extended phase space of the complex metric. We define the projection operator $\mathcal{P}$ that projects the dynamics onto the set of observable macro-variables (positions and momenta of the soliton centers, $A_i$):
$$\mathcal{P} \rho = \sum_{ij} \langle \rho, A_i \rangle (g^{-1})_{ij} A_j$$

The complementary operator $\mathcal{Q} = 1 - \mathcal{P}$ isolates the infinite hidden degrees of freedom and microscopic fluctuations of the vacuum ($\mathcal{Q}\Gamma$). The geometric Liouville operator $\mathcal{L}$ governs the temporal evolution of $\rho$:
$$\frac{\partial \rho}{\partial \tau} = -i\mathcal{L} \rho$$

Applying the projection identity to the Liouville equation, we obtain the generalized Zwanzig-Mori equation of motion for the projected density $\mathcal{P}\rho(\tau)$:
$$\frac{\partial \mathcal{P}\rho(\tau)}{\partial \tau} = -i\mathcal{P}\mathcal{L}\mathcal{P}\rho(\tau) - \int_{0}^{\tau} \mathcal{K}(\tau') \mathcal{P}\rho(\tau - \tau') d\tau' + \mathcal{F}(\tau)$$

Where the memory term $\mathcal{K}(\tau')$ and the stochastic fluctuation force $\mathcal{F}(\tau)$ are given by:
$$\mathcal{K}(\tau') = \mathcal{P}\mathcal{L} e^{-i\mathcal{Q}\mathcal{L}\tau'} \mathcal{Q}\mathcal{L}\mathcal{P}$$
$$\mathcal{F}(\tau) = -i\mathcal{P}\mathcal{L} e^{-i\mathcal{Q}\mathcal{L}\tau} \mathcal{Q}\rho(0)$$

The memory kernel $\mathcal{K}(\tau')$ encodes the intrinsic kinematic viscosity of the vacuum ($\nu_0 = \hbar / 2m_0$) and the dissipation accumulated by losses through [[09 - Spin and Cartan Geometry - The Vorticity of Spacetime|Cartan shear]]. The density projected in macroscopic space acts as an effective [[13 - Born Rule|Madelung fluid]].

---

## 21.4 The Asymptotic Emergence of the Second Law (Geometric $\mathcal{H}$-Theorem)

We define the observable macro-entropy $\mathcal{S}_{\text{macro}}$ by integrating the probability density under coarse-graining:
$$\mathcal{S}_{\text{macro}} = -k_B \int \bar{\rho} \ln \bar{\rho} \, d\Gamma_{\text{macro}}$$

Where $\bar{\rho} = \mathcal{P}\rho$. The evolution of $\mathcal{S}_{\text{macro}}$, under the action of the Zwanzig-Mori kernel with dissipative memory $\mathcal{K}(\tau)$, incorporates the continuous loss of information of the phases ejected by the Fano scattering. The temporal rate of change of $\mathcal{S}_{\text{macro}}$ for any non-equilibrium macro-process satisfies the inequality:
$$\frac{d\mathcal{S}_{\text{macro}}}{d\tau} = \int \left( \frac{\mathcal{F}(\tau)^2}{\nu_0 \bar{\rho}} \right) d\Gamma_{\text{macro}} \ge 0$$

---

## 21.5 Conclusion

The arrow of time and thermodynamic irreversibility are not primitive properties of the fundamental laws of spacetime. They emerge strictly in the scale transition:

1. **Micro Scale (Soliton):** Stability is unitary and reversible ($\dot{\mathcal{W}} = 0$) due to the exact Ricci-Sudarshan balance.
2. **Fano Mechanism (Coupling):** Non-quantized perturbations are dispersed and ejected into the continuous bands of the Kähler vacuum.
3. **Macro Scale (Zwanzig-Mori):** The macroscopic projection onto the center of mass variables, ignoring the microscopic radiation dispersed in the vacuum, introduces the memory friction term and results in the positive production of entropy $\dot{\mathcal{S}}_{\text{macro}} \ge 0$, generating the arrow of time.
