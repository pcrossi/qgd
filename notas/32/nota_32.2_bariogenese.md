### Adendo Teórico: 1. Assimetria Matéria-Antimatéria (Bariogênese Geométrica)

A origem da assimetria matéria-antimatéria no Universo é um dos temas de intensa investigação na cosmologia. No âmbito do Modelo Padrão, as condições de Sakharov estabelecem os requisitos necessários para a bariogênese, abrangendo a violação de número bariônico ($B$), a violação das simetrias de carga ($C$) e paridade-carga ($CP$), e o desequilíbrio térmico. Contudo, a magnitude da violação de CP descrita pela matriz CKM é considerada insuficiente para dar conta da assimetria observada na densidade bariônica ($\eta \sim 10^{-10}$).

No formalismo da GDQ, propõe-se que a assimetria possa ser descrita a partir de uma instabilidade topológica dinâmica associada ao fluxo geométrico sob condições de alta curvatura no Universo primordial. Nesse modelo, os estados associados à matéria e à antimatéria são relacionados a orientações quirais distintas sob os tensores de torção antissimétrica de Cartan ($\mathcal{T}^\mu_{\nu\rho}$).

Abaixo, apresenta-se a formulação para o fluxo de gradiente e a evolução topológica correspondente da quiralidade sob este formalismo.

### 1. Formalismo Matemático: O Funcional de Perelman Modificado por Torção Quiral

Para descrever a evolução do vácuo no regime inicial, estende-se o funcional de entropia de Perelman $\mathcal{W}$ incluindo o termo topológico associado ao invariante de Nieh-Yan. A correspondente ação geométrica sob o parâmetro de escala $\tau$ é expressa por:

$$\mathcal{W}_{\text{total}}(g, \mathcal{T}, f, \tau) = \int_M \left[ R + |\nabla f|^2 - \frac{1}{12}\mathcal{T}_{ijk}\mathcal{T}^{ijk} + \gamma \epsilon^{\mu\nu\rho\sigma} \mathcal{T}_{\mu\nu}^{\lambda} \mathcal{T}_{\rho\sigma\lambda} \right] e^{-f} dV$$

Onde:
- $R$ é a curvatura escalar.
- $f$ é o potencial dilatônico de Perelman.
- $\mathcal{T}_{ijk}$ é o tensor de torção de Cartan.
- O último termo representa a densidade de Nieh-Yan, acoplada pela constante topológica $\gamma$, atuando como o termo de quebra de paridade geométrica.

O parâmetro de ordem quiral $\theta_C(\tau)$ é definido pela assimetria de volume integrada entre as configurações de fluxo dextrogira ($\mathcal{H}^+$) e levogira ($\mathcal{H}^-$):

$$\theta_C(\tau) \equiv \frac{\text{Vol}(\mathcal{H}^+) - \text{Vol}(\mathcal{H}^-)}{\text{Vol}(\mathcal{H}^+) + \text{Vol}(\mathcal{H}^-)}$$

### 2. Equação de Transporte e Evolução Temporal

A evolução temporal do fluxo geométrico sob o parâmetro $\tau$ é descrita pelas equações acopladas do fluxo de Ricci modificado:

$$\frac{\partial g_{ij}}{\partial \tau} = -2(R_{ij} + \nabla_i \nabla_j f) + \frac{1}{2} \mathcal{T}_{ikl}\mathcal{T}_j^{\ kl}$$

$$\frac{\partial \mathcal{T}^\mu_{\nu\rho}}{\partial \tau} = -\kappa \frac{\partial \mathcal{W}_{\text{total}}}{\partial \mathcal{T}^\mu_{\nu\rho}} = \nabla^\alpha \nabla_\alpha \mathcal{T}^\mu_{\nu\rho} + \gamma \lambda_C \epsilon_{\nu\rho\alpha\beta} \mathcal{R}^{\mu \alpha\beta}_{\ \ \ \lambda} v^\lambda$$

Onde $v^\lambda$ representa o vetor de escoamento conformal e $\mathcal{R}$ é o tensor de curvatura de Riemann com torção.

A variação do parâmetro de ordem quiral $\theta_C$ em relação ao funcional de entropia $\mathcal{W}$ sob condições de alta densidade resulta na seguinte equação de transporte:

$$\frac{d\theta_C}{d\tau} = -\Gamma_{\text{elástica}} \frac{\partial \mathcal{W}_{\text{total}}}{\partial \theta_C} = \alpha_G \cdot \mathcal{H}^4(\tau) \cdot \theta_C \left(1 - \theta_C^2\right) + \delta_{\text{flutuação}}$$

Onde $\alpha_G$ é um coeficiente geométrico determinado pelas propriedades da variedade e $\mathcal{H}(\tau)$ representa a escala de variação do fluxo.

### 3. Análise de Estabilidade do Fluxo

O comportamento dinâmico deste sistema de equações sugere as seguintes propriedades:

1. **Instabilidade da Configuração Simétrica ($\theta_C = 0$):** Em regimes de alta curvatura ($\mathcal{H} \to \Lambda_{\text{Planck}}$), a configuração de simetria quiral exata ($\theta_C = 0$) comporta-se como um ponto de sela instável sob a influência da flutuação induzida pelo acoplamento de Nieh-Yan $\delta_{\text{flutuação}}$.
2. **Evolução em Direção ao Atrator Estável ($\theta_C \to 1$):** Sob a ação do fluxo de Perelman, o sistema evolui em direção a um dos estados de mínima energia livre. A configuração do vácuo tende a se estabilizar no atrator:

$$\lim_{\tau \to \infty} \theta_C(\tau) = +1$$

Este modelo sugere que a assimetria quiral inicial pode ser conduzida pelo fluxo em direção a configurações energeticamente favoráveis de fechamento geométrico, fornecendo um mecanismo alternativo para descrever a assimetria cósmica observada por meio do acoplamento entre torção e curvatura de vácuo.
