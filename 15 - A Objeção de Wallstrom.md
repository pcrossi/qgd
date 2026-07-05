# Capítulo 15 - A Objeção de Wallstrom

A formulação da mecânica estocástica proposta por Edward Nelson em 1966 permitiu a derivação da equação de Schrödinger linear a partir de flutuações brownianas de uma partícula imersa em um vácuo estocástico. Contudo, em 1989 e 1994, Timothy Wallstrom^[11] apontou uma limitação conceitual significativa no âmbito da mecânica estocástica e da hidrodinâmica clássica: a equação de [[01 - O Problema Inicial - A Divergência entre a Integral de Feynman e a de Wiener|Madelung]] (e o formalismo de Nelson) admite soluções onde a circulação do campo de velocidades $\mathbf{v}$ ao longo de um contorno fechado assuma valores arbitrários e contínuos:
$$\oint_\gamma m \mathbf{v} \cdot d\mathbf{x} = \kappa \cdot h, \quad \kappa \in \mathbb{R}$$

Para recuperar a mecânica quântica, na qual a circulação é obrigatoriamente restrita a valores discretos inteiros ($\kappa \in \mathbb{Z}$), a mecânica de Nelson precisa postular a condição de univocidade da função de onda complexa de forma axiomática e *ad-hoc*. Esta exigência axiomática limita o caráter puramente emergente da mecânica estocástica como uma descrição independente da teoria quântica convencional.

No âmbito do formalismo da GDQ, a objeção de Wallstrom é contornada de maneira geométrica. A quantização da circulação deixa de figurar como um postulado externo e emerge como uma **consequência geométrica e dinâmica rigorosa do fluxo** sobre a variedade de Kähler.

---

## 15.1 A Estrutura Geométrica e a Descontinuidade de Fase

Na teoria GDQ, o vácuo físico e os [[02 - A Geometrização da Matéria|solítons]] (partículas) são descritos pelo campo escalar complexo $f$ sobre a variedade de Kähler. O potencial $f$ é decomposto em termos das ações mecânica real ($S_R$) e osmótica de Nelson ($S_I$):
$$f = -\frac{S_I - i S_R}{\hbar}$$

O campo de velocidades de corrente do fluido quântico é governado pelo gradiente da fase real da ação:
$$\mathbf{v} = \frac{\nabla S_R}{m}$$

Consideremos um contorno fechado simplesmente conexo $\gamma$ que envolve um defeito topológico linear (um vórtice ou estômato de curvatura). A circulação genérica da fase acumula um erro de quantização $\epsilon$:
$$\oint_\gamma \nabla_\mu S_R \, dx^\mu = \kappa \cdot h = (n + \frac{\epsilon}{2\pi}) h$$
onde $n \in \mathbb{Z}$ representa a classe de homotopia do enrolamento e $\epsilon \in [0, 2\pi)$ é o desvio contínuo (não-quantizado) da circulação.

Quando $\epsilon \neq 0$, o campo de fase $S_R$ exibe multivaloração não-trivial no contorno, o que introduz uma descontinuidade na [[09 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|conexão afim]] e uma deformação por cisalhamento métrico transversal.

---

## 15.2 A Soma de Poisson e o Pente de Dirac no Espaço de Estados

Para descrever a estabilidade topológica sob a perspectiva de caminhos integrados, recorremos ao [[03 - Causalidade Complexa e o Fim do Paradoxo de Wick|propagador simétrico]]. A amplitude total de probabilidade topológica $\Psi_{\text{total}}(\epsilon)$ é construída somando as contribuições de todas as classes de homotopia (winding numbers) sobre o grupo fundamental da circunferência $\pi_1(S^1) \cong \mathbb{Z}$:
$$\Psi_{\text{total}}(\epsilon) = \sum_{m=-\infty}^{\infty} e^{im\epsilon}$$

A regularidade física exige que o espaço de estados admissíveis seja o espaço de funções de teste suaves de decaimento rápido (espaço de Schwartz $\mathcal{S}(S^1)$), sobre o qual a fase e seus momentos são definidos. No espaço de distribuições temperadas $\mathcal{S}'(S^1)$, a soma infinita acima é a definição exata do **Pente de Dirac** (Dirac Comb). Pela fórmula de Soma de Poisson, temos:
$$\sum_{m=-\infty}^{\infty} e^{im\epsilon} = 2\pi \sum_{n=-\infty}^{\infty} \delta(\epsilon - 2\pi n)$$
onde $\delta$ é a distribuição delta de Dirac.

> [!IMPORTANT] Importante
> **Veredito Topológico:** Para qualquer desvio de quantização $\epsilon \neq 0 \pmod{2\pi}$, a amplitude de probabilidade topológica $\Psi_{\text{total}}(\epsilon)$ anula-se de forma exata sob a ação de qualquer funcional ou observável suave. Isso significa que estados com circulação não-quantizada possuem **medida de suporte físico estritamente nula** no espaço de Hilbert topológico do [[12 -  O Tempo de Tunelamento Quântico (Efeito Hartman)|vácuo de Kähler]].

Para visualizar o efeito físico da dissipação sob a métrica flutuante, introduzimos o parâmetro de viscosidade cinemática $\eta > 0$ associado ao fluxo, definindo a soma regularizada de Abel:
$$\Psi_{\text{reg}}(\epsilon) = \lim_{\check{\eta} \to 0^+} \left[ \sum_{m=0}^{\infty} e^{-\check{\eta} m} e^{im\epsilon} + \sum_{m=1}^{\infty} e^{-\check{\eta} m} e^{-im\epsilon} \right]$$

Somando as séries geométricas e aplicando o limite:
$$\Psi_{\text{reg}}(\epsilon) = \lim_{\check{\eta} \to 0^+} \frac{1 - e^{-2\check{\eta}}}{1 - 2e^{-\check{\eta}}\cos(\epsilon) + e^{-2\check{\eta}}} = \begin{cases} \infty & \text{se } \epsilon = 0 \pmod{2\pi} \\ 0 & \text{se } \epsilon \neq 0 \pmod{2\pi} \end{cases}$$

O limite recupera o Pente de Dirac. Qualquer estado intermediário ($\epsilon \neq 0$) sofre uma interferência destrutiva infinitamente continuada no circuito fechado, aniquilando a probabilidade de transição local.

---

## 15.3 Divergência Energética no Funcional $\mathcal{W}$

A presença de um desvio de circulação $\epsilon \neq 0$ afeta diretamente a densidade de energia interna do fluido. O integrando do funcional entrópico de Perelman $\mathcal{W}$ contém o termo de energia cinética de gradiente $|\nabla f|^2$. Ao aproximarmos a vizinhança imediata do núcleo do vórtice radial (raio $r \to 0$), a densidade de energia escala como:
$$|\nabla f|^2 \propto \frac{(nh + \epsilon)^2}{r^2}$$

A integração do funcional $\mathcal{W}$ sobre uma região que envolve o vórtice resulta em:
$$\mathcal{W}(g, f, \tau) \propto \int_{\text{vórtice}} \frac{(nh + \epsilon)^2}{r^2} \, r \, dr \, d\theta \sim (nh + \epsilon)^2 \ln\left(\frac{R_{\text{ext}}}{r_{\text{core}}}\right)$$

Para qualquer desvio $\epsilon \neq 0$, a perturbação introduz uma barreira de energia potencial infinita no limite ultravioleta ($r_{\text{core}} \to 0$). O ponto de sela estável que minimiza a ação entrópica e garante a finitude do funcional exige estritamente:
$$\frac{\partial \mathcal{W}}{\partial \epsilon} = 0 \implies \epsilon = 0 \implies \kappa = n \in \mathbb{Z}$$

Os únicos mínimos locais estáveis da ação do vácuo de Kähler são os estados puramente quantizados.

---

## 15.4 Dissipação Dinâmica pelo Fluxo de Ricci em Tempo Finito

Se um estado físico for artificialmente preparado em um regime de circulação fracionária ou irracional ($\epsilon \neq 0$), a assimetria na rotação do espaço métrico gera uma tensão de cisalhamento não-nula que excita os graus de liberdade da curvatura transversal. A evolução da métrica de Kähler $g_{ij}$ sob o fluxo de é expressa por:
$$\frac{\partial g_{ij}}{\partial \tau} = -2\left( R_{ij} + \nabla_i \nabla_j f \right)$$
onde $\tau$ é o parâmetro de escala adimensional do fluxo.

Usando coordenadas harmônicas locais (via o mapa de DeTurck), a dinâmica evolutiva da curvatura média sob a flutuação estocástica de Itô satisfaz a desigualdade diferencial quase-linear:
$$\frac{\partial}{\partial \tau} \mathbb{E}[|R_{ij}|^2] \le \Delta_K \mathbb{E}[|R_{ij}|^2] - C_1 \left( \mathbb{E}[|R_{ij}|^2] \right)^{3/2} + \sigma^2_\epsilon$$
onde $\sigma^2_\epsilon$ representa a densidade de variância e deformação gerada pelo desalinhamento de fase $\epsilon$.

A taxa de entropia ao longo do escoamento geométrico dissipa a perturbação de cisalhamento através do tensor de viscosidade:
$$\frac{d\mathcal{W}}{d\tau} = 2 \int_{\mathcal{M}} |R_{ij} + \nabla_i \nabla_j f|^2 e^{-f} dV \ge \lambda_\epsilon > 0$$
onde $\lambda_\epsilon$ é uma constante de taxa de decaimento proporcional a $|\epsilon|^2$.

O amortecimento parabólico do fluxo força a contração e o estrangulamento da métrica transversal ao redor do filamento de circulação não-quantizada. A [[13 - Regra de Born|densidade de Madelung]] associada a essa configuração decai exponencialmente para zero:
$$\rho(\tau) = \rho_0 \exp\left( - \int_0^\tau \lambda_\epsilon(\tau') d\tau' \right)$$

Como o loop de retroação causal não se fecha para valores não-inteiros, a taxa de perda viscosa consome a energia do estado, extinguindo a configuração em um tempo de fluxo finito $\tau_{\text{fim}}$:
$$\tau_{\text{fim}} \le \frac{\mathcal{W}_{\text{inicial}}}{\lambda_\epsilon} < \infty$$

A perturbação fracionária é amortecida e convertida em flutuações de calor do vácuo (fônons métricos de alta frequência), restaurando a quantização inteira estável ($\epsilon = 0$).

---

## 15.5 Conclusão

A objeção de Wallstrom é completamente resolvida porque, na GDQ, a geometria de Kähler-Perelman não é um plano passivo, mas um meio dinâmico auto-regularizador. Estados com circulação não-quantizada são matematicamente aniquilados por interferência distribucional no Pente de Dirac e dinamicamente dissipados em tempo finito pelo Fluxo de Ricci. A quantização $nh$ da circulação atua como condição de regularidade elíptica e estabilidade topológica para a métrica da variedade.

---

## 15.6 O Fluxo de DeTurck e a Unicidade da Folheação

A evolução do espaço-tempo quântico e da densidade de probabilidade neste modelo é mapeada pelo fluxo de Ricci modificado por um difeomorfismo gerado pelo campo de velocidades quântico (método ou difeomorfismo de DeTurck). A equação de evolução da métrica de Kähler de fundo sob o fluxo de Ricci-DeTurck assume a forma de uma equação parabólica estritamente elíptica:
$$\frac{\partial g_{\mu\nu}}{\partial t} = -2R_{\mu\nu} + \mathcal{L}_v g_{\mu\nu}$$
onde $\mathcal{L}_v$ é a derivada de Lie ao longo do campo gradiente determinado pela fase $S$ ($v_ \mu = \nabla_\mu S$).

Pelo teorema de estabilidade geométrica de Hamilton-DeTurck, dada uma condição inicial na variedade, o fluxo converge de forma única para uma estrutura geométrica regularizada. As superfícies de fase constante ($S = \text{constante}$) formam uma **folheação de codimensão-1** do espaço de configuração. A elipticidade estrita do fluxo de DeTurck impede analiticamente o cruzamento ou a bifurcação dessas folhas geométricas, trancando a topologia local.

### 15.6.1 Resolução da Objeção via Mapeamento Suave de $S^1$

Dado que o fluxo de Ricci estabiliza a subvariedade e força as linhas de fluxo a contornar os nós de densidade zero através de caminhos topologicamente fechados na variedade complexa, a fase $S$ deixa de ser um funcional livre e passa a ser rigidamente acoplada à holonomia da conexão de Cartan local.

Para que a folheação de codimensão-1 seja globalmente regular e contínua ($C^\infty$), o mapa que leva o espaço de configuração à fase ao longo de qualquer curva fechada não-trivial $\gamma$ deve ser um recobrimento liso do círculo unidade:
$$S: \gamma \to S^1$$

Se houvesse ambiguidades na circulação (gaps não-inteiros), a estabilidade de DeTurck seria violada, introduzindo singularidades de estrangulamento (_pinching singularities_) na métrica de Kähler, o que é inconsistente com o comportamento assintótico do funcional de Perelman no vácuo. Portanto, a unicidade e a suavidade da folheação eliminam o grau de liberdade fisicamente inconsistente apontado por Wallstrom.