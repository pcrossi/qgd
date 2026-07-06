# Capítulo 10 - Resolução Mecânico-Geométrica do Experimento de Stern-Gerlach

A demonstração da separação discreta do feixe em duas trajetórias não exige projetores de von Neumann ou operadores hermitianos, emergindo como uma **bifurcação hidrodinâmica forçada pela holonomia da métrica**.

No formalismo convencional da mecânica quântica, a deflexão discreta de um feixe de átomos de prata em um campo magnético inomogêneo é descrita operacionalmente por meio do postulado da medição, no qual a interação com o aparelho projeta o estado nos autovalores do operador de spin $\hat{S}_z$. Sob a perspectiva geometrodinâmica, esse mesmo comportamento pode ser interpretado como o resultado dinâmico direto da força de arrasto convectiva exercida por um gradiente de curvatura de gauge sobre um [[02 - A Geometrização da Matéria|solíton]] dotado de [[09 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|torção quiral quantizada]].

---

## 10.1 A Equação de Estado Hidrodinâmica com Torção

O ponto de partida é a equação de evolução do Campo de Escoamento Complexo, $f = -\frac{S_I - i S_R}{\hbar}$, sob o regime de Estado Estacionário de Não-Equilíbrio (NESS), onde a entropia geométrica está travada ($\partial_\tau \mathcal{W}_T = 0$). Projetando a dinâmica na subvariedade real através da densidade geométrica ($\rho = e^{-\text{Re}(f)} = e^{S_I/\hbar}$), a Função Principal de Hamilton ($S_R$) obedece à **Equação de Hamilton-Jacobi** modificada pela torção de Cartan:
$$\frac{\partial S_R}{\partial t} + \frac{1}{2m} g^{ij} (\partial_i S_R)(\partial_j S_R) + \mathcal{V}_{\text{Bohm}} + V_{\text{ext}} = 0$$

Onde $\mathcal{V}_{\text{Bohm}}$ é o Potencial Quântico expandido pela identidade jacobi-logarítmica do tensor antissimétrico $B_{\mu\nu\lambda}$:
$$\mathcal{V}_{\text{Bohm}} = -\frac{\hbar^2}{2m} \frac{\Delta_K R_M}{R_M} + \frac{1}{4} B_{\mu\nu\lambda}B^{\mu\nu\lambda}$$

> **Justificativa da Passagem:** A inclusão do termo $\frac{1}{4}B^2$ decorre diretamente da métrica hermitiana estendida $\tilde{g}_{\mu\nu} = g_{\mu\nu} + iB_{\mu\nu}$. O estresse de cisalhamento gerado pela contrarrotação do fluido ao redor do estômato central cria uma barreira de pressão centrífuga que impede o colapso da densidade ($\rho = R_M^2$), estabilizando o raio crítico do solíton.

> [!note]- Justificativa do Termo Torsional: Por que o termo 1/4 B² no potencial quântico?
> 
> ![[notas/10/nota 10.1.md]]

---

## 10.2 Acoplamento com a Curvatura Inomogênea de Gauge

Introduzimos um campo magnético externo macroscópico direcionado ao longo do eixo $Z$, apresentando um gradiente espacial linear $\frac{\partial B_z}{\partial z}$. Na teoria de Kähler-Cartan, este campo não é um vetor abstrato, mas uma perturbação elástica da 2-forma de curvatura de gauge $\mathcal{F}_{\mu\bar{\nu}} = \partial_\mu \mathcal{A}_{\bar{\nu}} - \partial_{\bar{\nu}}\mathcal{A}_\mu$.

O acoplamento mecânico entre a perturbação externa e o solíton ocorre pela integração do arrasto de Cartan ao redor da fronteira elíptica do estômato $\partial\mathcal{M}$. O termo de energia potencial de interface $V_{\text{ext}}$ assume a forma de uma contração helicoidal:
$$V_{\text{ext}} = -\gamma \int_{\partial\mathcal{M}} B_{\mu\nu\lambda} \mathcal{F}^{\mu\nu} dx^\lambda = -\kappa \cdot \mu_B \cdot B_z(z)$$

Onde $\mu_B$ é o magneton de Bohr geométrico e $\kappa$ é o **índice quiral de vorticidade intrínseca** do estômato.

> **Justificativa da Passagem:** Como provado anteriormente via **Índice de Maslov** ($\mu_M = 2$) e **Soma de Poisson**, a estabilidade topológica contra a dissipação do Fluxo de Ricci força a integral circulatória a assumir valores estritamente discretos. O parâmetro quiral $\kappa$ fica cinematicamente confinado aos autovalores isolados:
> $$\kappa = \pm 1 \implies S_z = \kappa \cdot \frac{1}{2}\hbar = \pm\frac{1}{2}\hbar$$

---

## 10.3 Dedução Analítica da Força de Deflexão Torsional

Para encontrar a trajetória espacial do centro de massa do solíton, aplicamos o operador gradiente espacial $\partial_z$ sobre a equação de Hamilton-Jacobi-Bohm. Sabendo que a velocidade de deriva do pacote fluídico é dada por $v_i = \frac{1}{m} \partial_i S_R$, a derivada total temporal do momentum linear do solíton resulta na equação de força hidrodinâmica:
$$m \frac{d v_z}{dt} = -\frac{\partial}{\partial z} \left( \mathcal{V}_{\text{Bohm}} + V_{\text{ext}} \right)$$

Como o Solíton de Ricci viaja de forma coerente e rígida ao longo do aparelho, o seu perfil interno de densidade de Perelman deforma-se simetricamente em relação ao seu próprio baricentro móvel. Consequentemente, o gradiente do potencial interno de Bohm-Cartan na coordenada do centro de massa anula-se identicamente ($\partial_z \mathcal{V}_{\text{Bohm}} = 0$). Substituindo o potencial de acoplamento $V_{\text{ext}}$:
$$m \frac{d^2 z}{dt^2} = -\frac{\partial}{\partial z} \left( -\kappa \cdot \mu_B \cdot B_z(z) \right)$$
$$m \frac{d^2 z}{dt^2} = \kappa \cdot \mu_B \cdot \left( \frac{\partial B_z}{\partial z} \right)$$

> **Justificativa da Passagem:** A aceleração do solíton na direção $Z$ deixa de depender de probabilidades de transição. Ela passa a ser uma resposta mecânica determinística clássica do tipo Newtoniana, onde o sentido da força aceleradora é governado unicamente pelo sinal do nó topológico ($\kappa = +1$ ou $\kappa = -1$) que foi capturado na preparação da fronteira.

---

## 10.4 Resolução das Equações de Trajetória e Bifurcação do Feixe

Assumindo que o feixe de sólitons é injetado ao longo do eixo $Y$ com velocidade uniforme $v_y$, e penetra em uma região magnética de comprimento $L$, o tempo de trânsito mecânico dentro do gradiente de curvatura é rigorosamente:
$$t = \frac{L}{v_y}$$

Integrando a equação diferencial de segunda ordem obtida no passo anterior em relação ao tempo real de Minkowski $t$, sob as condições de contorno iniciais $z(0) = 0$ e $v_z(0) = 0$, obtemos a equação de deflexão espacial:
$$v_z(t) = \int_{0}^{t} \frac{\kappa \cdot \mu_B}{m} \left( \frac{\partial B_z}{\partial z} \right) dt' = \frac{\kappa \cdot \mu_B}{m} \left( \frac{\partial B_z}{\partial z} \right) t$$
$$z(t) = \int_{0}^{t} v_z(t') dt' = \frac{\kappa \cdot \mu_B}{2m} \left( \frac{\partial B_z}{\partial z} \right) t^2$$

Substituindo o tempo de trânsito estrutural $t = \frac{L}{v_y}$ na equação de posição final, isolamos o vetor de deflexão observado na chapa fotográfica:
$$\Delta z = \kappa \cdot \left[ \frac{\mu_B L^2}{2m v_y^2} \left( \frac{\partial B_z}{\partial z} \right) \right]$$

Como a distribuição delta de Dirac da Soma de Poisson bloqueou deterministicamente os únicos valores estáveis do sistema em $\kappa = \pm 1$, a equação projeta duas, e apenas duas, coordenadas de impacto discretas:
$$\Delta z_{\text{up}} = + \frac{\mu_B L^2}{2m v_y^2} \left( \frac{\partial B_z}{\partial z} \right) \quad (\text{para } \kappa = +1)$$
$$\Delta z_{\text{down}} = - \frac{\mu_B L^2}{2m v_y^2} \left( \frac{\partial B_z}{\partial z} \right) \quad (\text{para } \kappa = -1)$$

---

## 10.5 Conclusão e Blindagem de Causalidade

A resolução prova que o feixe original se divide de forma limpa em duas linhas simétricas com exclusão absoluta de impactos na zona central ($\Delta z = 0$). Se um pacote de fluido tentasse assumir uma trajetória intermediária contínua (o que equivaleria a uma rotação fracionária não-inteira do spin no espaço observável), o desvio de fase residual $\epsilon$ geraria uma grande força de fricção interna sob o fluxo.

O circuito de retrocausalidade destruiria o casamento de fase holomorfa da 1-forma de Kähler, induzindo uma interferência puramente destrutiva que aniquilaria a densidade do solíton em tempo finito ($\rho \to 0$). Portanto, a descontinuidade observada no experimento de Stern-Gerlach não é uma quebra da causalidade quântica: ela é a assinatura macroscópica de que **apenas geometrias quantizadas com períodos meio-inteiros possuem estabilidade mecânica para sobreviver ao tecido do espaço-tempo**. 

No formalismo GDQ, a transição para o regime relativístico fermiônico dispensa o uso operacional das matrizes $\gamma^\mu$ de Dirac, mapeando a densidade de corrente espinorial diretamente sobre a sua [[09 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|tradução hidrodinâmica exata de Takabayasi]]^[10].

A Equação de Hamilton-Jacobi-Takabayasi Estendida: A evolução da Função Principal de Hamilton ($S_R$) sob o tempo de fluxo geométrico $\tau$ incorpora o transporte balístico, a barreira repulsiva do potencial de Bohm-Cartan e o acoplamento magnético torsional, estacionando rigorosamente na equação de estado:
$$\frac{\partial S_R}{\partial \tau} + \frac{(\nabla S_R)^2}{2m} + \mathcal{V}_{\text{Bohm}} + \frac{e}{m}(\mathbf{S} \cdot \mathbf{B}) = 0$$
