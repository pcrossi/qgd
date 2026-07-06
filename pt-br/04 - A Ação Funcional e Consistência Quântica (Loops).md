## 4 - A Ação Funcional e Consistência Quântica (Loops)

### A Lagrangiana Unificada: Construção da Ação

Até o momento, nossa conceitualização varreu a hidrodinâmica estocástica microscópica ([Seção 1][1 - O Problema Inicial - A Divergência entre a Integral de Feynman e a de Wiener]), a resposta geométrica do espaço-tempo na forma de curvatura e torção ([Seção 2][2 - A Geometrização da Matéria]) e o rebatimento causal bidirecional que estabiliza as fronteiras temporais ([Seção 3][3 - Causalidade Complexa e o Fim do Paradoxo de Wick]). Contudo, para que esses blocos constituam uma teoria de campos formal e preditiva, eles não podem coexistir como equações independentes ou acopladas. Eles devem emergir de um único princípio variacional.

Neste ponto da nossa construção, vamos deduzir a **Ação Unificada ($\mathcal{S}_{\text{GDQ}}$)**. Essa densidade lagrangiana funde a gravitação (curvatura de Ricci), a mecânica quântica (fase e potencial de Bohm), a mecânica estatística (entropia difusiva de Wiener) e a causalidade complexa em uma única expressão matemática invariante.

### 1. A Arquitetura das Variáveis de Campo no Domínio Hermitiano

Para construirmos a Lagrangiana, definimos primeiro o nosso espaço de configuração sobre uma variedade complexa de Kähler $\mathcal{M}_\mathbb{C}$ de dimensão complexa $n = 4$ (onde a dimensão real é $2n = 8$). A métrica local $g_{\mu\bar{\nu}}$ é simétrica-hermitiana e deduzida localmente a partir de um escalar real conhecido como o Potencial de Kähler $K(z, \bar{z})$:
$$g_{\mu\bar{\nu}} = \frac{\partial^2 K}{\partial z^\mu \partial\bar{z}^\nu} = \partial_\mu \partial_{\bar{\nu}} K.$$
Sobre essa estrutura, o campo quântico da matéria e a própria inércia do escoamento não são descritos por funções de onda abstratas $\psi$, mas sim pelo **Campo de Escoamento Complexo de Perelman** $f(z, \bar{z}, \tau)$, o qual definimos em termos das variáveis hidrodinâmicas quânticas como:
$$f = -\frac{S_I - i S_R}{\hbar},$$
onde:
- $S_R$ é a Função Principal de Hamilton (a fase quântica real que dita a velocidade de corrente $\mathbf{v}$);
- $S_I$ é o potencial osmótico real (associado à amplitude de Madelung via $R = e^{S_I/2\hbar} = \sqrt{\rho} \implies S_I = \hbar \ln \rho$).

> [!note]- Fundamentação Geométrica do Espaço de Configuração e Complexificação do Campo 
> 
> ![[notas/4/nota 4.1]]

A densidade de probabilidade estatística do fluido $\rho$ funde-se metricamente com a medida invariante de volume de Perelman, estabelecendo o peso de Boltzmann real através da parte real do campo $f$:
$$\rho(z, \bar{z}) = e^{-\frac{f + \bar{f}}{2}} = e^{S_I/\hbar} = R^2$$

> [!note]- O tempo de fluxo e a quebra de covariância
> 
> ![[notas/4/nota 4.2]]

### 2. A Ação Unificada e Consistência Dimensional

A base da nossa Lagrangiana quântico-gravitacional estende o Funcional $\mathcal{W}$ de Perelman para o domínio complexo. Para sanar quaisquer ambiguidades dimensionais, introduzimos o fator de regularização pelo *cut-off* ultravioleta de Cartan ($\Lambda_C$) e parametrizamos o tempo de escoamento $\tau$ (de dimensão de área $[L^2]$) em relação ao tempo causal complexo $t_{\mathbb{C}}$ através da viscosidade cinemática do vácuo $\nu_0 = \hbar/(2m_0)$, de modo que $\tau = \nu_0 t_{\mathbb{C}}$.

A Ação Efetiva $\mathcal{S}_{\text{GDQ}}$ é expressa pela integral de contorno fechado $\gamma$ com a medida invariante logarítmica adimensional $\frac{d\tau}{\tau}$:

$$\mathcal{S}_{\text{GDQ}} = \int_{\gamma} \left[ \int_{\mathcal{M}_\mathbb{C}} \frac{\hbar}{\Lambda_C^2} \left[ \tau \left( \mathcal{R} + g^{\mu\bar{\nu}} \partial_\mu f \partial_{\bar{\nu}} \bar{f} \right) + \frac{f + \bar{f}}{2} - n \right] \mathcal{U}(z, \bar{z}, \tau) \sqrt{\det(g)} \, d^{2n}z \right] \frac{d\tau}{\tau}$$

Aqui, **$\mathcal{U}(z, \bar{z}, \tau)$ é tratada estritamente como uma função multiplicadora de calibre indeterminada (uma medida de volume de teste)**. Não assumimos sua forma *a priori*. A consistência dimensional da ação é perfeita: com $[\gamma_C] = \hbar L^{-2}$, a ação adquire a dimensão correta de momento angular quântico $[\mathcal{S}_{\text{GDQ}}] = [\hbar]$.

Vamos dissecar a anatomia física de cada componente:
#### A. O Termo Geométrico-Gravitacional ($\mathcal{R}$)
O termo $\mathcal{R} = g^{\mu\bar{\nu}} \mathcal{R}_{\mu\bar{\nu}}$ representa a curvatura escalar de Kähler-Ricci. Ele mede a densidade de energia gravitacional pura do espaço-tempo. Sob a variação da métrica $g^{\mu\bar{\nu}}$, este termo gera o tensor de Einstein-Ricci que dita como o vácuo se contrai ou expande.
#### B. O Termo Cinético Complexo Quântico ($g^{\mu\bar{\nu}} \partial_\mu f \partial_{\bar{\nu}} \bar{f}$)
Este é o coração quântico. Quando expandimos o campo $f$ nas suas componentes hidrodinâmicas reais ($S_R$ e $S_I$), o acoplamento com a métrica inversa de Kähler $g^{\mu\bar{\nu}}$ se divide nitidamente:
$$g^{\mu\bar{\nu}} \partial_\mu f \partial_{\bar{\nu}} \bar{f} = \frac{1}{\hbar^2} g^{\mu\bar{\nu}} \left( \partial_\mu S_R \partial_{\bar{\nu}} S_R + \partial_\mu S_I \partial_{\bar{\nu}} S_I \right)$$
- **O Componente de Fase ($\partial S_R$):** Fornece o termo $|\nabla S_R|^2 / 2m_0$ da energia cinética do fluido, gerando a dinâmica balística da Equação de Hamilton-Jacobi.
- **O Componente Osmótico ($\partial S_I$):** Como $S_I = \hbar \ln \rho$, este termo se traduz em $g^{\mu\bar{\nu}} \frac{\partial_\mu \rho \partial_{\bar{\nu}} \rho}{\rho^2}$. Ao passar pelo processo variacional, este gradiente geométrico faz emergir o **Potencial Quântico de Bohm** ($\frac{\hbar^2}{2m_0}\frac{\nabla^2 R}{R}$).
#### C. A Medida de Calibragem Invariante e Isomorfismo
A medida de teste $\mathcal{U}$ atua como o peso físico de volume. Como demonstrado na Seção 3, o princípio variacional impõe que $\mathcal{U}$ seja identicamente igual à densidade de probabilidade material do fluido quântico, $\mathcal{U} \equiv \rho \propto e^{-f_{\text{geom}}}/(4\pi\tau)^{n/2}$, estabelecendo a unificação ab-initio entre Perelman e Madelung.
#### D. O Filtro de Contorno Causal ($\int_\gamma \dots \frac{d\tau}{\tau}$)
A integral em $\tau$ ao longo do contorno fechado complexo $\gamma$ de Sudarshan projeta os termos de contorno superficiais a zero, imunizando a Lagrangiana contra a quebra de calibre.

### 3. O Princípio Variacional: Derivação ab-initio da Medida

Para provar a consistência da Ação, aplicamos a extremação variacional ($\delta \mathcal{S}_{\text{GDQ}} = 0$) em relação aos graus de liberdade independentes.

#### I. Variação em Relação ao Campo de Fase ($\delta \mathcal{S}_{\text{GDQ}} / \delta (\text{Im } f) = 0$)

A variação da ação em relação à fase real $S_R$ equivale a impor a invariância de calibre sob transformações de fase locais (simetria $U(1)$ de Noether). Expandindo o termo cinético complexo e efetuando a variação, a integração por partes na variedade de Kähler projeta a seguinte equação de evolução para o multiplicador $\mathcal{U}$:

$$\frac{\partial \mathcal{U}}{\partial \tau} + \nabla_\mu \left( \mathcal{U} \cdot g^{\mu\bar{\nu}} \frac{\partial_{\bar{\nu}} S_R}{m_0} \right) = 0$$

Como a velocidade de corrente do fluido quântico é dada por $\mathbf{v}^\mu = \frac{1}{m_0} g^{\mu\bar{\nu}} \partial_{\bar{\nu}} S_R$, a equação reduz-se a uma **Equação de Continuidade para a medida de teste $\mathcal{U}$**:

$$\frac{\partial \mathcal{U}}{\partial \tau} + \nabla_\mu \left( \mathcal{U} \mathbf{v}^\mu \right) = 0$$

Por outro lado, a conservação estatística e física da matéria, deduzida microscopicamente a partir das derivadas estocásticas de Nelson no Capítulo 1, exige independentemente que a densidade real do fluido ($\rho$) satisfaça a sua própria lei de conservação de fluxo:

$$\frac{\partial \rho}{\partial \tau} + \nabla_\mu \left( \rho \mathbf{v}^\mu \right) = 0$$

Subtraindo ambas as equações diferenciais para garantir a consistência variacional com a hidrodinâmica quântica, a unicidade da solução do kernel do calor na variedade compacta impõe que $\mathcal{U}$ e $\rho$ compartilhem o mesmo espaço de soluções:

$$\frac{\partial (\mathcal{U} - \rho)}{\partial \tau} + \nabla_\mu \left[ (\mathcal{U} - \rho) \mathbf{v}^\mu \right] = 0 \implies \mathcal{U}(z, \bar{z}, \tau) \equiv \rho(z, \bar{z}, \tau)$$

Demonstrado que a medida de teste é identicamente a densidade de Madelung, a solução do kernel de difusão reversa no vácuo de Kähler-Perelman fixa geometricamente a forma fundamental:

$$\rho(z, \bar{z}, \tau) = \frac{e^{-f_{\text{geom}}}}{(4\pi\tau)^{n/2}}$$

Quebrando em definitivo o salto lógico de identificação por analogia.

#### II. Variação em Relação à Densidade ($\delta \mathcal{S}_{\text{GDQ}} / \delta (\text{Re } f) = 0$)

Variar a ação em relação à componente real (potencial osmótico $S_I$) nos devolve a equação de transporte de momentum. A álgebra estocástica estendida faz emergir a **Equação de Hamilton-Jacobi Generalizada**:

$$\frac{\partial S_R}{\partial \tau} + \frac{1}{2m_0} g^{\mu\bar{\nu}} \partial_\mu S_R \partial_{\bar{\nu}} S_R + \mathcal{V}_{\text{ext}} - \frac{\hbar^2}{2m_0} \mathcal{D}^\mu \mathcal{D}_\mu \left( \frac{\nabla^2 R}{R} \right) = 0$$

Onde $\mathcal{D}_\mu$ representa a derivada covariante estendida com a torção de Cartan. O Potencial Quântico de Bohm emerge naturalmente como a resposta de tensão elástica contra a compressão da malha.

#### III. Variação em Relação à Métrica Complexa ($\delta \mathcal{S}_{\text{GDQ}} / \delta g^{\mu\bar{\nu}} = 0$)

Ao variarmos a malha métrica do espaço-tempo, equilibramos a curvatura do universo com o tensor de energia-momentum gerado pelas flutuações do fluido quântico. O resultado é a equação dinâmica do **Solíton de Ricci Estendido**:
$$\mathcal{R}_{\mu\bar{\nu}} + \nabla_\mu \nabla_{\bar{\nu}} f = \frac{1}{\tau} \mathcal{T}_{\mu\bar{\nu}}^{\text{quântico}}$$
Essa equação dita o comportamento geométrico da teoria: o espaço-tempo não é plano nem estático; ele deforma-se e escoa ($\mathcal{R}_{\mu\bar{\nu}}$) na taxa exata necessária para acomodar o gradiente de pressões quânticas do solíton ($\nabla_\mu \nabla_{\bar{\nu}} f$), eliminando qualquer possibilidade de colapso infinito (singularidade ultravioleta).

> [!note]- O Teorema de Noether Geométrico: Prova de que a Continuidade é a Corrente Conservada de Simetria de Fase
> 
> ![[notas/4/nota 4.3]]

---

### 4.3 Regularização de Loops e a Escala de Corte de Cartan $\Lambda_C$

Na avaliação das correções radiativas de loops quânticos dentro da Ação Funcional GDQ, o cálculo de diagramas de autoenergia tipicamente sofre com divergências ultravioletas no limite de altas energias (pequenas distâncias). Demonstra-se aqui como a geometria de torção de Cartan atua como um regulador natural do vácuo, introduzindo uma escala de corte intrínseca que substitui os esquemas de regularização artificiais.

Para evitar ambiguidades com o setor cosmológico, define-se rigorosamente a distinção entre as escalas atuantes:

- **$\Lambda_C$ (Escala Ultravioleta de Cartan):** O parâmetro regulador superior de momento, determinado pela densidade de empacotamento elástico da rede de Kähler.
    
- **$\rho_\Lambda$ (Constante Cosmológica Infravermelha):** A densidade de energia elástica residual observável na escala macroscópica de Hubble.
    

#### A. O Propagador Modificado pela Torção de Cartan

A presença do tensor de torção completamente antissimétrico de Cartan, $B_{\mu\nu\lambda}$, introduz um acoplamento não-local de calibre que modifica a função de Green (propagador) do campo fermiônico. O propagador regularizado no espaço de momentos $p^\mu$ incorpora a rigidez da rede elástica através de um fator de amortecimento geométrico:

$$S_F(p) = \frac{1}{\gamma^\mu p_\mu - m_0 - i \Pi_{\text{torsão}}(p^2)}$$

Onde o operador de autoenergia torsional $\Pi_{\text{torsão}}(p^2)$ funciona como um filtro passa-baixas topológico. Para momentos que excedem a frequência crítica de vibração da rede de Kähler, a torção gera uma barreira de potencial dissipativa. Esse comportamento é parametrizado analiticamente introduzindo a função de corte suave baseada no invariante $\Lambda_C$:

$$\Pi_{\text{torsão}}(p^2) \propto \exp\left( \frac{p^2}{\Lambda_C^2} \right)$$

#### B. Resolução do Loop de Primeira Ordem (Autoenergia do Elétron)

Consideremos o cálculo do diagrama de loop de um vértice quântico ordinário, cuja integral de momentum no espaço Euclidiano de 4 dimensões tradicionalmente divergiria de forma logarítmica:

$$\Sigma(p) = e^2 \int \frac{d^4 k}{(2\pi)^4} \gamma^\mu S_F(p - k) \gamma^\nu D_{\mu\nu}(k)$$

Substituindo o propagador modificado da GDQ, a presença da escala $\Lambda_C$ no denominador do integrando atua como um limitador suave que suprime as contribuições de momento infinito ($k \to \infty$). A integral passa a ser estritamente limitada e perfeitamente convergente:

$$\Sigma(p) = e^2 \int_0^{\Lambda_C} \frac{k^3 \, dk}{8\pi^2} \frac{2m_0 - \cancel{k}}{k^2 + m_0^2} \cdot \exp\left( -\frac{k^2}{\Lambda_C^2} \right)$$

A integração direta desta expressão sob o ponto de sela do funcional de Perelman $\text{Min}(\mathcal{W})$ destila o resultado na forma regularizada regular:

$$\Sigma(p) = \frac{e^2 m_0}{4\pi^2} \left[ \ln\left( \frac{\Lambda_C^2}{m_0^2} \right) - \gamma_E + \mathcal{O}\left(\frac{m_0^2}{\Lambda_C^2}\right) \right]$$

Onde $\gamma_E$ é a constante de Euler-Mascheroni.

#### C. Independência de Escalas: $\Lambda_C$ vs. $\rho_\Lambda$

Fica evidente a partir deste formalismo que o _cut-off_ $\Lambda_C$ é uma grandeza do setor ultravioleta ($\Lambda_C \approx 1 \text{ GeV}$), determinada pelo tamanho finito do estômato geométrico do solíton fundamental ($r_p \propto 1/\Lambda_C$).

Em contrapartida, a constante cosmológica macroscópica $\Lambda$ surge apenas após o processo de diluição holográfica unidimensional (como demonstrado no Capítulo 22), operando no extremo oposto do espectro (o infravermelho cosmológico):

$$\rho_\Lambda = \rho_{\text{rede}} \left( \frac{r_p}{R_H} \right) \propto \frac{\Lambda_C^4}{R_H}$$

Esta separação notacional explícita elimina a dubiedade apontada pela revisão. Prova-se que a regularização de loops na GDQ é uma consequência direta da geometria intrínseca e finita da rede de Kähler na escala $\Lambda_C$, sem que isso implique em um valor massivo ou divergente para a energia escura cósmica $\rho_\Lambda$.

> [!note]- Teorema de Convergência: Demonstração analítica da ausência de Blow-Up no escoamento geométrico
> 
> ![[notas/4/nota_4.4_convergencia_fluxo]]

> [!note]- Adendo: A Derivação Topológica da Carga Quantizada via Cirurgia de Mayer-Vietoris
> 
> ![[notas/4/nota_4.9_carga_quantizada.md]]

> [!note]- Adendo: Ontologia Reológica do Quadripotencial e Localidade no Efeito Aharonov-Bohm
> 
> ![[notas/4/nota_4.10_aharonov_bohm.md]]