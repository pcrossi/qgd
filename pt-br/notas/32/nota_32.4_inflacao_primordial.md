### Adendo Teórico: 13. A Inflação Cósmica e o Campo do Inflaton

A descrição da fase inflacionária na cosmologia convencional frequentemente recorre à introdução de campos escalares fundamentais (como o inflaton), os quais requerem condições específicas de ajuste fino e estabilização frente a correções radiativas.

Na GDQ, a expansão acelerada primordial e a homogeneidade espacial podem ser descritas a partir da dinâmica de relaxação elástica da métrica durante o desdobramento de uma singularidade de pescoço (*neck-pinch*) sob o fluxo de Ricci. No limite em que o raio da singularidade se aproxima da escala microscópica de corte, a aplicação da cirurgia topológica de Perelman introduz uma variação conformal transiente que atua expandindo a métrica de forma exponencial. Isso oferece uma descrição geométrica para o horizonte de causalidade macroscópica sem a necessidade de introduzir novos campos escalares livres.

### Formalismo Matemático e Teorema de Expansão Primordial

Seja o Universo modelado inicialmente como uma variedade compacta de Bismut-Kähler $\mathcal{M}$ evoluindo sob o fluxo de Ricci modificado pelo potencial dilatônico $f$:

$$\frac{\partial g_{ij}}{\partial \tau} = -2(R_{ij} + \nabla_i \nabla_j f)$$

1. **A Dinâmica da Singularidade de Pescoço (*Neck-Pinch*):** Nos estágios iniciais ($\tau \to 0$), o fluxo geométrico pode induzir o colapso localizado de subvariedades cilíndricas do tipo $S^n \times \mathbb{R}$. A curvatura de fundo eleva-se na garganta conforme o raio coordenado do pescoço, $r_{\text{neck}}(\tau)$, aproxima-se do limite de corte da rede definido pela escala de Cartan:

    $$\lim_{\tau \to \tau_c} r_{\text{neck}}(\tau) = \delta_{\text{Cartan}} \equiv \frac{\hbar c}{\Lambda_C}$$

2. **O Processo Conformal e a Cirurgia de Perelman:** No limiar em que a continuidade diferenciável clássica seria interrompida ($\tau = \tau_c$), adota-se o formalismo de cirurgia topológica de Perelman para regularizar a variedade, conectando calotas estáveis. O potencial geométrico associado a essa transição topológica induz uma variação local do fator de escala conformal $\phi(\tau)$ da métrica ($g_{ij} = \phi^2 \hat{g}_{ij}$), governada pela relaxação da energia elástica acumulada:

    $$\frac{\partial \ln \phi}{\partial \tau} = \frac{1}{d} \left( \Delta_{\text{Kähler}} f - R_{\text{local}} \right)$$

    Como a curvatura local $R_{\text{local}}$ assume valores negativos expressivos na sela da garganta antes da cirurgia, o termo de restituição elástica torna-se positivo e dominante no intervalo de transição:

    $$\frac{\partial \ln \phi}{\partial \tau} \approx \sqrt{\frac{\Lambda_{\text{cosmo}}}{3}} \implies \phi(\tau) = \phi_0 \exp\left(\sqrt{\frac{\Lambda_{\text{cosmo}}}{3}} \tau\right)$$

3. **Homogeneidade e Causalidade:** Devido ao acoplamento global no espaço de Kähler associado ao propagador no plano complexo, o horizonte de causalidade geométrica engloba a variedade antes do desdobramento exponencial. Esse mecanismo proporciona uma explicação geométrica para a homogeneidade e planicidade assintótica observadas na radiação cósmica de fundo (CMB).

### A Emergência da Inflação Primordial por Cirurgia de Perelman

O modelo inflacionário padrão introduz o campo do inflaton para explicar a isotropia e homogeneidade do fundo cósmico de micro-ondas. Na Geometrodinâmica Quântica, propõe-se uma interpretação na qual a fase inflacionária decorre de uma transição topológica do vácuo.

O Big Bang é modelado como o desdobramento cirúrgico de um colapso do tipo *neck-pinch* hiperbólico na variedade. Quando o fluxo de Ricci atinge o limite elástico microscópico ($r_{\text{neck}} \to \delta_{\text{Cartan}}$), a variedade passa por uma cirurgia de estabilização topológica. A transição induz uma reconfiguração do fator de escala conformal $\phi(\tau)$, cuja dinâmica sob estresse elástico é expressa por:

$$\frac{d^2 \phi}{d\tau^2} - \kappa_{\text{vac}} \left( \nabla_i f \nabla^i f \right) \phi = 0$$

À medida que o gradiente do potencial $f$ acumula a impedância da rede no limiar da cirurgia, a solução para o fator de escala transita por um regime de acoplamento hiperbólico da forma $\phi(\tau) \propto \cosh(\omega \tau) \sim \exp(\omega \tau)$. Esta expansão exponencial estica as flutuações locais, distribuindo a curvatura ao longo da variedade e conduzindo a curvatura espacial global para zero ($k \equiv 0$). Uma vez concluída a transição topológica, o gradiente do potencial dissipa-se em direção ao ponto de equilíbrio estável do funcional de Perelman ($\partial \mathcal{W} / \partial \tau \to 0$), encerrando o período de expansão acelerada primordial. Q.E.D.
