### Theoretical Addendum: 1. Matter-Antimatter Asymmetry (Geometric Baryogenesis)

The origin of the matter-antimatter asymmetry in the Universe is one of the themes of intense investigation in cosmology. Within the Standard Model, the Sakharov conditions establish the necessary requirements for baryogenesis, encompassing baryon number violation ($B$), charge ($C$) and charge-parity ($CP$) symmetry violations, and thermal disequilibrium. However, the magnitude of the CP violation described by the CKM matrix is considered insufficient to account for the asymmetry observed in the baryonic density ($\eta \sim 10^{-10}$).

In the QGD formalism, it is proposed that the asymmetry can be described from a dynamic topological instability associated with the geometric flow under high curvature conditions in the early Universe. In this model, the states associated with matter and antimatter are related to distinct chiral orientations under the antisymmetric Cartan torsion tensors ($\mathcal{T}^\mu_{\nu\rho}$).

Below, we present the formulation for the gradient flow and the corresponding topological evolution of chirality under this formalism.

### 1. Mathematical Formalism: The Perelman Functional Modified by Chiral Torsion

To describe the vacuum evolution in the initial regime, the Perelman entropy functional $\mathcal{W}$ is extended by including the topological term associated with the Nieh-Yan invariant. The corresponding geometric action under the scale parameter $\tau$ is expressed by:

$$\mathcal{W}_{\text{total}}(g, \mathcal{T}, f, \tau) = \int_M \left[ R + |\nabla f|^2 - \frac{1}{12}\mathcal{T}_{ijk}\mathcal{T}^{ijk} + \gamma \epsilon^{\mu\nu\rho\sigma} \mathcal{T}_{\mu\nu}^{\lambda} \mathcal{T}_{\rho\sigma\lambda} \right] e^{-f} dV$$

Where:
- $R$ is the scalar curvature.
- $f$ is the Perelman dilatonic potential.
- $\mathcal{T}_{ijk}$ is the Cartan torsion tensor.
- The last term represents the Nieh-Yan density, coupled by the topological constant $\gamma$, acting as the geometric parity-breaking term.

The chiral order parameter $\theta_C(\tau)$ is defined by the integrated volume asymmetry between the dextrorotatory ($\mathcal{H}^+$) and levorotatory ($\mathcal{H}^-$) flow configurations:

$$\theta_C(\tau) \equiv \frac{\text{Vol}(\mathcal{H}^+) - \text{Vol}(\mathcal{H}^-)}{\text{Vol}(\mathcal{H}^+) + \text{Vol}(\mathcal{H}^-)}$$

### 2. Transport Equation and Temporal Evolution

The temporal evolution of the geometric flow under the parameter $\tau$ is described by the coupled equations of the modified Ricci flow:

$$\frac{\partial g_{ij}}{\partial \tau} = -2(R_{ij} + \nabla_i \nabla_j f) + \frac{1}{2} \mathcal{T}_{ikl}\mathcal{T}_j^{\ kl}$$

$$\frac{\partial \mathcal{T}^\mu_{\nu\rho}}{\partial \tau} = -\kappa \frac{\partial \mathcal{W}_{\text{total}}}{\partial \mathcal{T}^\mu_{\nu\rho}} = \nabla^\alpha \nabla_\alpha \mathcal{T}^\mu_{\nu\rho} + \gamma \lambda_C \epsilon_{\nu\rho\alpha\beta} \mathcal{R}^{\mu \alpha\beta}_{\ \ \ \lambda} v^\lambda$$

Where $v^\lambda$ represents the conformal flow vector and $\mathcal{R}$ is the Riemann curvature tensor with torsion.

The variation of the chiral order parameter $\theta_C$ with respect to the entropy functional $\mathcal{W}$ under high-density conditions results in the following transport equation:

$$\frac{d\theta_C}{d\tau} = -\Gamma_{\text{elástica}} \frac{\partial \mathcal{W}_{\text{total}}}{\partial \theta_C} = \alpha_G \cdot \mathcal{H}^4(\tau) \cdot \theta_C \left(1 - \theta_C^2\right) + \delta_{\text{flutuação}}$$

Where $\alpha_G$ is a geometric coefficient determined by the properties of the manifold and $\mathcal{H}(\tau)$ represents the scale of flow variation.

### 3. Flow Stability Analysis

The dynamical behavior of this system of equations suggests the following properties:

1. **Instability of the Symmetric Configuration ($\theta_C = 0$):** In high-curvature regimes ($\mathcal{H} \to \Lambda_{\text{Planck}}$), the exact chiral symmetry configuration ($\theta_C = 0$) behaves as an unstable saddle point under the influence of the fluctuation induced by the Nieh-Yan coupling $\delta_{\text{fluctuation}}$.
2. **Evolution Towards the Stable Attractor ($\theta_C \to 1$):** Under the action of the Perelman flow, the system evolves towards one of the minimum free energy states. The vacuum configuration tends to stabilize at the attractor:

$$\lim_{\tau \to \infty} \theta_C(\tau) = +1$$

This model suggests that the initial chiral asymmetry can be driven by the flow towards energetically favorable configurations of geometric closure, providing an alternative mechanism to describe the observed cosmic asymmetry through the coupling between vacuum torsion and curvature.
