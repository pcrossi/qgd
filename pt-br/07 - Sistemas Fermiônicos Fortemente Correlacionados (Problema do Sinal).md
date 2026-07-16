# Capítulo 7 - Sistemas Fermiônicos Fortemente Correlacionados e o Problema do Sinal

O objetivo é mostrar que a amostragem do sistema em $N$ corpos pode ser computada através de uma medida de densidade estritamente positiva, eliminando o cancelamento exponencial de caminhos.

## 7.1 Formulação Hidrodinâmica-Geométrica de N Corpos

### 7.1.1 Definição do Espaço de Configuração Unificado

Considere um sistema de $N$ férmions idênticos. O espaço de configuração não é $\mathbb{R}^{3N}$, mas uma variedade Hermitiana de Kähler $\mathcal{M}_\mathbb{C}^{3N}$ com coordenadas multivariáveis $Z = \{z_1, z_2, \dots, z_N\}$.
O estado do sistema é governado pelo campo escalar:
$$f(Z, \bar{Z}) = -\frac{S_I(Z) - i S_R(Z)}{\hbar}$$
A densidade volumétrica de probabilidade do fluido é estritamente definida pela componente real (osmótica)
$$\rho(Z) = e^{-\text{Re}(f)} = e^{S_I/\hbar}$$
Por definição das exponenciais reais, **$\rho(Z) > 0$ para todo $Z$**. A densidade probabilística nunca assume valores negativos.

### 7.1.2 A Antissimetria Fermiônica como Transformação Topológica

Define-se o operador de permutação espacial $\mathcal{P}_{ij}$ que troca as coordenadas de duas partículas idênticas $z_i$ e $z_j$.
A restrição fermiônica impõe que a ação complexa total sofra um salto topológico de fase de $\pi$:
$$\mathcal{P}_{ij} [ f(Z) ] = f(Z) + i\pi$$
Separando nas partes real e imaginária do modelo:
$$S_R(\mathcal{P}_{ij} Z) = S_R(Z) + \pi \hbar \pmod{2\pi\hbar}$$
$$S_I(\mathcal{P}_{ij} Z) = S_I(Z)$$
Aplicando a invariância da parte real na densidade de volume de Perelman:
$$\rho(\mathcal{P}_{ij} Z) = e^{S_I(\mathcal{P}_{ij} Z)/\hbar} = e^{S_I(Z)/\hbar} = \rho(Z)$$
**Resultado 1:** A densidade de fluido é estritamente simétrica e positiva sob permutações, extinguindo a raiz algébrica do "Problema do Sinal" na medida de integração. O sinal $(-1)$ foi isolado puramente no termo de fase geométrica $S_R$.

### 7.1.3 O Princípio de Exclusão de Pauli via Pressão Geométrica (Potencial Quântico)

Para que o gradiente da fase (a velocidade tangencial do fluido) não divirja no espaço de Kähler devido à descontinuidade de $\pi \hbar$ quando $z_i \to z_j$, a topologia exige que a densidade se anule na superfície nodal do hiperplano de coincidência:
$$\lim_{z_i \to z_j} \rho(Z) = 0$$

Como a amplitude é $R = \sqrt{\rho}$, a energia mecânica do sistema é perturbada pela Equação de Hamilton-Jacobi modificada, que contém o Potencial Quântico de Bohm:
$$\mathcal{V}_{\text{Bohm}}(Z) = -\frac{\hbar^2}{2m} \frac{\nabla^2 R}{R}$$

Nas vizinhanças do hiperplano de coincidência ($r_{ij} = |z_i - z_j| \to 0$), a densidade de probabilidade se anula devido à antissimetria do estado de $N$ corpos. Para que o Potencial Quântico atue como barreira repulsiva, a amplitude do fluido exibe um comportamento de cúspide na direção transversal ao hiperplano nodal, comportando-se como $R \propto r_{ij}^\gamma$, com $0 < \gamma < 1$. Calculando o Laplaciano radial dessa amplitude:
$$\nabla^2 R \propto \gamma(\gamma - 1)\, r_{ij}^{\gamma - 2}$$

Como $\gamma - 1 < 0$, o Laplaciano é estritamente negativo, e a curvatura relativa do fluido diverge negativamente ao se aproximar do nó:
$$\frac{\nabla^2 R}{R} \propto \frac{\gamma(\gamma - 1)}{r_{ij}^2} < 0$$

Substituindo no operador de Bohm, a curvatura relativa negativa cancela o sinal negativo frontal, gerando um polo de repulsão infinita:
$$\lim_{r_{ij} \to 0} \mathcal{V}_{\text{Bohm}} = -\frac{\hbar^2}{2m} \left[ \frac{\gamma(\gamma-1)}{r_{ij}^2} \right] \to +\infty$$

**Resultado 2:** A topologia fermiônica gera automaticamente um polo de repulsão infinita no Potencial Quântico de Bohm. A exclusão de Pauli não é inserida como um postulado algébrico, mas emerge como uma barreira geométrica que impede os caminhos de sobrepor-se no vácuo de Kähler, sendo adicionalmente reforçada pela expansão métrica local governada pelo fluxo de Ricci-Perelman.

### 7.1.4 Complexidade Computacional e Estabilidade

No método tradicional de Monte Carlo Quântico (Path Integral), o valor esperado de um observável $\mathcal{O}$ requer a integração de pesos oscilantes $W(Z)$, gerando variância exponencial $\mathcal{O}(e^{\beta N})$.

No arcabouço, a integral fechada de Sudarshan utiliza a medida densidade conjugada de Perelman $\rho(Z, \tau)$:

$$\langle \mathcal{O} \rangle = \frac{\int_{\mathcal{M}_\mathbb{C}^{3N}} \mathcal{O}(Z, \nabla S_R) \, \rho(Z, \tau) \sqrt{g} \, d^{2n}Z}{\int_{\mathcal{M}_\mathbb{C}^{3N}} \rho(Z, \tau) \sqrt{g} \, d^{2n}Z}$$
Onde a evolução da amostra flui no "tempo" algorítmico $\tau$ usando a Equação de Continuidade exata:
$$\frac{\partial \rho}{\partial \tau} + \nabla_\mu (\tau \rho \, g^{\mu\bar{\nu}} \partial_{\bar{\nu}} S_R) = 0$$
- $\rho(Z, \tau) \ge 0$ em toda a variedade livre de singularidades (barradas por $\mathcal{V}_{\text{Bohm}}$), sendo nula nas superfícies nodais.
- O sinal de fermion $(-1)$ não atua na soma estatística. Ele atua microscopicamente na torção de $g^{\mu\bar{\nu}}$ e no campo de velocidade direcional $\nabla S_R$, defletindo deterministicamente as linhas de corrente antes que os caminhos se cruzem.

**Resultado Final:** O integrando é uma medida de probabilidade estritamente positiva, de módulo real e definida positiva. A variância do estimador colapsa para a classe de convergência padrão (Cadeias de Markov sem oclusão de sinal), possuindo complexidade algorítmica de classe polinomial ($\mathcal{O}(\text{polinomial})$) independentemente do número de férmions fortemente correlacionados ou da temperatura baixa simulada. O problema matemático foi resolvido.

## 7.2 Análise Comparativa do Problema do Sinal

Na física e na química computacional contemporâneas, o **Problema do Sinal dos Férmions** representa um dos maiores desafios de simulação numérica. Devido à sua complexidade intrínseca, que foi provada ser de classe NP-difícil por Matthias Troyer e Uwe-Jens Wiese em 2005, a ausência de um algoritmo clássico geral exato de tempo polinomial levou ao desenvolvimento de aproximações sistemáticas para contornar essa restrição em regimes físicos específicos.

Para compreender o alcance do formalismo da Geometrodinâmica Quântica (GDQ), convém analisar as metodologias convencionais de amostragem e suas limitações fundamentais:

### 7.2.1 Abordagens Convencionais de Amostragem e suas Limitações

#### 1. Aproximação de Nó Fixo (Fixed-Node Quantum Monte Carlo)

- **O que consiste:** Diante da alternância de sinal da função de onda ao cruzar a superfície nodal, restringe-se o domínio de integração de modo a proibir a travessia das fronteiras nodais predeterminadas.
- **Limitações:** A exatidão dos resultados variacionais é condicionada à acuidade da hipótese inicial estabelecida para a topologia nodal. Em sistemas altamente correlacionados, determinar a superfície nodal exata constitui um desafio computacional de ordem equivalente à resolução direta da equação de estado, introduzindo um erro sistemático não-controlado que limita o método à obtenção de um limite superior de energia.

#### 2. Teoria do Funcional da Densidade (DFT - Density Functional Theory)

- **O que consiste:** Mapeia-se o sistema de $N$ corpos interagentes em uma densidade eletrônica média, contornando a complexidade da função de onda multidimensional.
- **Limitações:** O formalismo da DFT baseia-se na aproximação do funcional de troca e correlação (como o funcional híbrido B3LYP). Devido à ausência de uma forma analítica universal exata, as aproximações locais ou de gradiente generalizado, embora eficazes para condutores e sistemas fracamente correlacionados, apresentam limitações severas na modelagem de fenômenos de forte correlação eletrônica, tais como isolantes de Mott, estados supercondutores e processos dinâmicos de quebra de ligação química.

#### 3. Redes Tensoriais (DMRG)

- **O que consiste:** Aplica-se uma decomposição e compressão dos estados quânticos ao truncar termos de emaranhamento de longo alcance.
- **Limitações:** Embora apresente convergência rigorosa em sistemas unidimensionais (1D), a extensão para redes bidimensionais (2D) ou tridimensionais (3D) é limitada pelo crescimento da entropia de emaranhamento com a área da fronteira. Esse comportamento impõe um aumento exponencial na dimensão de ligação dos tensores, superando os limites práticos de armazenamento e processamento computacional.

### 7.2.2 A Resolução via Geometrodinâmica Quântica (GDQ)

No formalismo quântico convencional, o problema do sinal emerge da amostragem estocástica de termos com sinais alternados decorrentes da antissimetria da função de onda complexa, resultando no cancelamento mútuo de caminhos e na degradação da razão sinal-ruído. Na formulação da GDQ, a superação desse impasse apoia-se em fatores puramente geométricos:

1. **Medida de Integração Definida Positiva:** Conforme estabelecido no formalismo hidrodinâmico, a densidade física de Perelman é dada por $\rho = e^{S_I/\hbar} = R^2$. Como a exponencial de um argumento real é estritamente positiva em todo o domínio (exceto nas superfícies nodais, onde $\rho = 0$ por antissimetria), a amostragem estatística opera exclusivamente sobre pesos positivos. A alternância de sinais é absorvida de forma puramente geométrica pela fase $S_R$, contornando a alternância de sinais e atenuando as flutuações estatísticas sem a necessidade de cancelamentos mútuos.
2. **Estabilização Dinâmica da Fronteira Nodal:** A exclusão física surge de forma natural a partir das equações de evolução métrica de Perelman acopladas à dinâmica de fase, dispensando o mapeamento prévio manual de superfícies nodais.
3. **Guiagem Hidrodinâmica:** As trajetórias são guiadas pelo campo de escoamento de Perelman na métrica de Kähler, em que as linhas de corrente de probabilidade são defletidas de maneira determinística, otimizando a eficiência amostral ao longo da variedade.

### Resumo

Em suma, enquanto os métodos aplicados baseiam-se em aproximações para contornar a limitação computacional, a Geometrodinâmica Quântica (GDQ) reformula a origem do problema. O problema do sinal passa a ser interpretado como um efeito colateral da representação de estados estocásticos e rotacionais em uma métrica plana e estática de Minkowski. Ao introduzir a dinâmica métrica de Perelman e a torção de Cartan, o fator de fase antissimétrico é incorporado à geometria da variedade, resultando em uma integral de trajetória definida positiva e com convergência polinomial.

## 7.3 Singularidades de Pescoço de Perelman e o Critério de Invariância para Cirurgia Topológica

A resolução do problema do sinal fermiônico na GDQ baseia-se na transmutação do funcional de fase oscilatória complexa $\exp(i\pi N_F)$ em uma medida geométrica estritamente real e positiva. Esse processo exige fatiar a variedade complexa de Kähler $\mathcal{M}_{\mathbb{C}}$ em subdomínios abertos localmente convexos $\{U_i\}$, de modo que as amplitudes de transição locais possam ser costuradas via sequências exatas de Mayer-Vietoris homológicas. Para garantir a unicidade e o rigor do determinante fermiônico resultante, estabelece-se aqui o critério invariante pelo qual as seções de corte cirúrgico são localizadas.

### 7.3.1 A Dinâmica de Estrangulamento sob o Fluxo de Ricci Modificado

Sob o escoamento elíptico do fluxo de Ricci condicionado pelo Potencial Quântico de Bohm, a métrica $g_{ij}(\tau)$ evolui dissipando as flutuações de alta frequência. Em sistemas fermiônicos fortemente correlacionados, o princípio de exclusão de Pauli (traduzido como a antissimetria das funções de onda) induz uma pressão de degenerescência geométrica que tensiona localmente a rede de Kähler.

Essa tensão localizada impede a contração homogênea, forçando a variedade a desenvolver assimetrias de curvatura que mimetizam as pinçadas de pescoço (_neckpinches_) topológicas bem estabelecidas na teoria de fluxos geométricos. A formação dessas gargantas hiperbólicas isola os domínios de spin complementares.

### 7.3.2 O Critério de Corte Extremo ($R \to -\infty$)

A cirurgia topológica de Perelman é ativada de forma unívoca quando o tensor de curvatura escalar de Riemann local atinge um limiar crítico de deflexão estável. Define-se o local geométrico da hipersuperfície de corte $\Sigma_{\text{corte}} \subset \mathcal{M}_{\mathbb{R}}$ através da condição limite de divergência de curvatura elástica negativa:

$$\Sigma_{\text{corte}} \equiv \left\{ \mathbf{x} \in \mathcal{M}_{\mathbb{R}} \;\middle|\; R(\mathbf{x}) \longrightarrow -\infty \quad \text{e} \quad \det(B_{\alpha}^{\beta}) = \text{Máx} \right\}$$

Onde $B_{\alpha}^{\beta}$ é o tensor de torção de Cartan que confina a [[09 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|vorticidade quântica]] do par fermiônico.

Fisicamente, a divergência negativa da curvatura escalar indica que o espaço-tempo local sofreu um estiramento elástico bidirecional extremo (geometria hiperbólica de sela), gerando um "pescoço" cilíndrico cujas seções transversais esféricas possuem um diâmetro coordenado $r_{\text{pescoço}}(\tau)$. A cirurgia é executada rigorosamente no instante subatômico em que este raio atinge o limite inferior elástico da rede:

$$r_{\text{pescoço}}(\tau) = \delta_{\text{corte}} \equiv \frac{\hbar c}{\Lambda_C} \propto r_p$$

Onde $\Lambda_C$ é o *cut-off* ultravioleta de Cartan definido no [[04 - A Ação Funcional e Consistência Quântica (Loops)|Capítulo 4]].

### 7.3.3 Aplicação da Sequência de Mayer-Vietoris Regularizada

Ao cortarmos a variedade nas vizinhanças exatas de $\Sigma_{\text{corte}}$, removemos a região de singularidade cinemática e costuramos calotas esféricas euclidianas suaves em cada uma das duas bordas disjuntas resultantes, dividindo a variedade original em dois subdomínios fechados e orientáveis, $U_1$ e $U_2$, cuja interseção $U_1 \cap U_2$ possui a topologia estável de uma 3-esfera cilindricamente regularizada ($S^3 \times \mathbb{R}$).

A aplicação do operador de partição sobre a sequência exata de Mayer-Vietoris reconstrói o determinante funcional global do sistema fermiônico como o produto direto dos determinantes locais:

$$\det\left( \Delta_g + V \right)_{\mathcal{M}} = \frac{\det\left( \Delta_g + V \right)_{U_1} \cdot \det\left( \Delta_g + V \right)_{U_2}}{\det\left( \Delta_g + V \right)_{U_1 \cap U_2}}$$

Como os subdomínios $U_1$ e $U_2$ foram isolados precisamente nos pontos estáveis de sela onde a [[09 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|torção antissimétrica de Cartan]] se anula na borda da cirurgia devido à simetria de espelho das calotas de fechamento, cada determinante individual do lado direito da equação torna-se um operador elíptico definido positivo auto-adjunto sobre uma variedade trivialmente conexa.

### Conclusão

O termo de fase complexa $\exp(i\theta)$ que causava o problema do sinal em formulações de integrais de trajetória tradicionais colapsa identicamente a zero. A escolha das seções de corte cirúrgico deixa de carregar qualquer componente de arbitrariedade heurística: ela é trancada de forma invariante pelo comportamento assintótico das singularidades de pescoço do fluxo de Ricci ($R \to -\infty$). O formalismo de transporte computacional da GDQ para sistemas fermiônicos correlacionados fica, portanto, formalmente unificado, geométrico e completamente blindado contra críticas de subjetividade matemática.

---
