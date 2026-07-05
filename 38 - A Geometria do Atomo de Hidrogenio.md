# Capítulo 38 - A Geometria do Átomo de Hidrogênio: Espectro, Lamb Shift e a Anomalia Muônica

## 38.1 Limite de Campo Fraco e Correspondência Clássica (O Limite de Sommerfeld-Dirac)

### 38.1.1 Ontologia do Sistema e Simplificação de Campo Fraco

Na formulação clássica do eletromagnetismo, a órbita circular acelerada do elétron implicaria a irradiação contínua de energia, sugerindo a instabilidade dinâmica do sistema orbital. Para descrever a estabilidade atômica, a mecânica quântica convencional postula a existência de estados estacionários não-irradiantes por meio da equação de Schrödinger.

No escopo da [[02 - A Geometrização da Matéria|Geometrodinâmica Quântica (GDQ)]], o átomo de hidrogênio é tratado de forma local, mecânica e reológica. O sistema consiste no acoplamento mútuo entre dois defeitos topológicos estáveis (nós geométricos estáveis) na malha elástica:

-   **O [[26 - Próton - O Solíton de Ricci Composto|Próton]]:** Um [[26 - Próton - O Solíton de Ricci Composto|solíton composto]], caracterizado por um número de nós ou gênero topológico $n=3$, que atua como uma garganta de curvatura massiva hiperbólica fixa. Fixamos este defeito na origem do sistema de coordenadas esféricas relativísticas ($r=0$).
-   **O Elétron:** Um [[08 - Singularidade do Buraco Negro|solíton elementar]] com nó singular de gênero $n=1$, imerso na deformação métrica induzida pelo próton. Ele possui uma função de densidade volumétrica de métrica localizada, denotada por $\rho_{\text{elétron}}(r) = R^2(r)$, com massa de repouso $m_e$ decorrente da auto-energia elástica do confinamento.

A interação coulombiana clássica é descrita nesse formalismo como decorrente do perfil de deformação assintótica da métrica do [[17 - Monotonicidade sob Torção de Cartan|vácuo elástico]] gerado pela assimetria do acoplamento de [[12 -  O Tempo de Tunelamento Quântico (Efeito Hartman)|Kähler]]. A deformação métrica gerada pelo nó estável do próton ($n=3$) altera as componentes da métrica temporal e radial. Em coordenadas esféricas relativísticas $(ct, r, \theta, \phi)$, a métrica se aproxima de uma geometria do tipo *Reissner-Nordström* modificada pela rigidez quântica, onde o elemento de linha $ds^2$ é dado por:

$$ds^2 = -f(r) c^2 dt^2 + \frac{1}{f(r)} dr^2 + r^2 d\Omega^2$$

No limite de **campo fraco** (distâncias distais onde $r \gg r_s$), a função de relaxação elástica do vácuo radial $f(r)$ é aproximada linearmente por:

$$f(r) \approx 1 - \frac{2r_s}{r}$$

Onde $r_s$ é o raio de deformação característico do próton.

---

### 38.1.2 A Equação de Onda Radial sob Torção Basal de Cartan

A densidade métrica $\rho = R^2$ do elétron obedece à conservação do fluxo relativístico na variedade trançada. A amplitude escalar do sóliton $\Phi(x^\mu)$ responde à geometria de fundo através do operador de Laplace-Beltrami modificado pela [[09 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|torção de Cartan]] $\mathcal{T}^\lambda_{\mu\nu}$:

$$\left[ \frac{1}{\sqrt{-g}}\partial_\mu \left( \sqrt{-g} g^{\mu\nu} \partial_\nu \right) + \mathcal{T}^\mu_{\mu\lambda}g^{\lambda\nu}\partial_\nu - \frac{m_e^2 c^2}{\hbar^2} \right] \Phi = 0$$

Onde o termo de contração da torção $\mathcal{T}^\mu_{\mu\lambda}$ representa o arraste cinemático do fluido quântico induzido pela [[09 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|vorticidade]] intrínseca do espaço-tempo ao redor do próton.

#### Dedução Formal da Torção Radial ($\mathcal{T}^r$)

Em uma geometria de Cartan esfericamente simétrica, as equações de estrutura de Maurer-Cartan na fibração de Hopf impõem que o tensor de torção de fundo deve ser invariante sob rotações espaciais. A contração do tensor de torção que representa o fluxo radial de vorticidade deve respeitar a conservação da torção topológica no vácuo (condição de divergência nula):

$$\nabla_\mu \mathcal{T}^\mu = 0 \implies \frac{1}{r^2}\partial_r \left( r^2 \mathcal{T}^r \right) = 0 \implies \mathcal{T}^r = \frac{2\tau_0}{r^2}$$

Onde $\tau_0$ é a constante de acoplamento da vorticidade fundamental do vácuo.

Para uma órbita estacionária estável com frequência de holonomia $\omega = E/\hbar$, adota-se a separação temporal $\Phi = \psi(\mathbf{r})e^{-iEt/\hbar}$. Substituindo as componentes inversas do tensor métrico $g^{00} = -1/f(r)$, $g^{rr} = f(r)$, e o determinante $\sqrt{-g} = r^2 \sin\theta$, a equação espacial sob a aproximação linear de $f(r)$ se reduz à **Equação Diferencial Radial de GDQ**:

$$\frac{d^2 \mathcal{R}}{dr^2} + \frac{2}{r}\frac{d\mathcal{R}}{dr} + \left[ \frac{E^2 - m_e^2 c^4}{\hbar^2 c^2} + \frac{2E\alpha}{\hbar c r} - \frac{\ell(\ell+1) - 4\alpha^2}{r^2} \right]\mathcal{R}(r) = 0$$

#### Identificação da Carga via Impedância de Escoamento

A [[29 -  A constante de estrutura fina|constante de estrutura fina]] $\alpha$ surge de primeiros princípios como a razão geométrica entre o raio de deformação topológica $r_s$ do próton e o comprimento de onda Compton reduzido do elétron $\lambda_c = \frac{\hbar}{m_e c}$:

$$\alpha \equiv \frac{r_s}{\lambda_c} = \frac{m_e c^2 r_s}{\hbar c} = \frac{e^2}{4\pi\varepsilon_0 \hbar c}$$

Eso estabelece que o termo de acoplamento coulombiano $\frac{e^2}{4\pi\varepsilon_0}$ é a tradução física macroscópica da impedância elástica da métrica elástica deformada ($m_e c^2 r_s$). O termo $-4\alpha^2/r^2$ é gerado pelo acoplamento da torção basal de Cartan com a vorticidade de spin do elétron, surgindo de forma geométrica.

---

### 38.1.3 Resolução de Frobenius e Espectro de Sommerfeld-Dirac

Para resolver a equação radial de campo fraco, definimos o fator de escala de decaimento do vácuo $\gamma$ e a coordenada adimensional $\rho$:

$$\gamma = \frac{\sqrt{m_e^2 c^4 - E^2}}{\hbar c} \quad (E < m_e c^2), \quad \rho = 2\gamma r$$

Substituindo na equação diferencial radial, obtemos a forma canônica de Whittaker:

$$\frac{d^2 \mathcal{R}}{d\rho^2} + \frac{2}{\rho}\frac{d\mathcal{R}}{d\rho} + \left[ \frac{\rho_0}{\rho} - \frac{1}{4} - \frac{\ell(\ell+1) - 4\alpha^2}{\rho^2} \right]\mathcal{R}(\rho) = 0$$

Onde $\rho_0 = \frac{E\alpha}{\hbar c \gamma}$.

#### Análise dos Limites Críticos:

1.  **Para $\rho \to \infty$**: A equação se aproxima de $\mathcal{R}'' - \frac{1}{4}\mathcal{R} = 0 \implies \mathcal{R} \sim e^{-\rho/2}$.
2.  **Para $\rho \to 0$**: A barreira centrífuga e torsional impõe a equação indicial para a regularidade do nó topológico:
    $$s(s+1) - [\ell(\ell+1) - 4\alpha^2] = 0 \implies s = -\frac{1}{2} + \sqrt{\left(\ell+\frac{1}{2}\right)^2 - 4\alpha^2}$$

Efetuamos a substituição regular $\mathcal{R}(\rho) = \rho^s e^{-\rho/2} L(\rho)$, obtendo para $L(\rho)$ a equação confluente de Laguerre:

$$\rho \frac{d^2 L}{d\rho^2} + \left[ 2(s + 1) - \rho \right] \frac{dL}{d\rho} + \left[ \rho_0 - (s + 1) \right] L(\rho) = 0$$

Expandindo $L(\rho) = \sum_{k=0}^{\infty} a_k \rho^k$, a relação de recorrência dos coeficientes estruturais do sóliton é:

$$a_{k+1} = \frac{k + s + 1 - \rho_0}{(k + 1)(k + 2s + 2)} a_k$$

#### Truncamento Topológico

Para manter a estabilidade mecânico-geométrica da variedade e garantir a integrabilidade do fluxo (impedindo que a densidade divirja no infinito), a série deve truncar em um número inteiro de nós radial $k = n_r$. A condição de truncamento impõe:

$$\rho_0 = n_r + s + 1$$

Substituindo $s$ e definindo o número quântico principal $n = n_r + \ell + 1$ ($n \in \mathbb{Z}^+$):

$$\rho_0 = n - \left(\ell + \frac{1}{2}\right) + \sqrt{\left(\ell+\frac{1}{2}\right)^2 - 4\alpha^2}$$

Substituindo $\rho_0$ de volta em sua definição cinemática e isolando a constante de holonomia temporal $E$, obtemos o espectro de energia do limite de campo fraco da GDQ:

$$E_{n,\ell} = m_e c^2 \left[ 1 + \left( \frac{\alpha}{n - (\ell + 1/2) + \sqrt{(\ell + 1/2)^2 - 4\alpha^2}} \right)^2 \right]^{-1/2}$$

Esta fórmula reproduz o espectro de *Sommerfeld-Dirac* de forma geométrica, com a modificação $-4\alpha^2$ decorrente do acoplamento dinâmico da torção de Cartan.

> [!NOTE]
> **Representação Geral por Funções Hipergeométricas Confluentes**
> 
> A solução geral para a amplitude radial da densidade do sóliton elétron no limite de campo fraco pode ser expressa de forma fechada em termos da função hipergeométrica confluente de Kummer (ou primeira função hipergeométrica confluente) $_1F_1(a; c; \rho)$:
> 
> $$\mathcal{R}(\rho) = C \cdot \rho^s e^{-\rho/2} \, _1F_1(s + 1 - \rho_0; 2s + 2; \rho)$$
> 
> Onde:
> - $C$ é a constante de normalização geométrica determinada pela [[17 - Monotonicidade sob Torção de Cartan|integral de Perelman]].
> - $_1F_1(a; c; z) = \sum_{k=0}^{\infty} \frac{(a)_k}{(c)_k} \frac{z^k}{k!}$ (sendo $(x)_k$ o símbolo de Pochhammer).
> 
> Em termos da função confluente de Whittaker $M_{\kappa, \mu}(z)$, a solução geral escreve-se como:
> 
> $$\mathcal{R}(\rho) = \frac{C}{\rho} M_{\rho_0, s + 1/2}(\rho)$$
> 
> Esta formulação hipergeométrica é a representação analítica mais geral do escoamento sob simetria central. O confinamento físico do nó topológico e a integrabilidade do funcional métrico exigem que a função $_1F_1(a; c; \rho)$ se comporte como um polinômio finito (truncamento). Isso ocorre se, e somente se, o primeiro argumento $a = s + 1 - \rho_0$ for um inteiro não positivo ($-n_r$), o que restringe os autovalores da holonomia $E$ exatamente aos níveis quantizados de *Sommerfeld-Dirac* derivados acima.

---

## 38.2 Campo Próximo e a Emergência de Termos de Ordem Superior

### 38.2.1 A Expansão Exata de Taylor da Métrica Elástica

Quando o sóliton elétron sonde regiões mais profundas e próximas do núcleo ($r \to r_s$), a aproximação de campo fraco linear falha. Devemos reter a métrica exata de relaxação do próton $f(r) = 1 - \frac{2r_s}{r}$ e expandi-la em série geométrica infinita:

$$\frac{1}{f(r)} = \sum_{k=0}^{\infty} \left(\frac{2r_s}{r}\right)^k = 1 + \frac{2r_s}{r} + \frac{4r_s^2}{r^2} + \frac{8r_s^3}{r^3} + \dots$$

$$\frac{1}{f^2(r)} = \sum_{k=0}^{\infty} (k+1)\left(\frac{2r_s}{r}\right)^k = 1 + \frac{4r_s}{r} + \frac{12r_s^2}{r^2} + \frac{32r_s^3}{r^3} + \dots$$

$$\frac{f'(r)}{f(r)} = \frac{2r_s}{r^2}\left(1 + \frac{2r_s}{r} + \frac{4r_s^2}{r^2} + \dots\right) = \frac{2r_s}{r^2} + \frac{4r_s^2}{r^3} + \frac{8r_s^3}{r^4} + \dots$$

Substituindo estas expansões sem truncamento artificial no operador de Laplace-Beltrami radial e coletando os termos em potências de $1/r$, a equação diferencial radial exata da GDQ assume a forma:

$$\frac{d^2 \mathcal{R}}{dr^2} + \left( \frac{2}{r} + \frac{2r_s + 2\tau_0}{r^2} + \frac{4r_s^2 + 4r_s\tau_0}{r^3} + \frac{8r_s^3 + 8r_s^2\tau_0}{r^4} + \dots \right)\frac{d\mathcal{R}}{dr} + \left[ \beta_0^2 + \frac{\beta_1}{r} - \frac{\ell(\ell+1) - \mu_0^2}{r^2} + \frac{\chi_3}{r^3} + \frac{\chi_4}{r^4} + \dots \right]\mathcal{R}(r) = 0$$

Onde as constantes estruturais do vácuo elástico são dadas por:
-   $\beta_0^2 = \frac{E^2 - m_e^2 c^4}{\hbar^2 c^2}$
-   $\beta_1 = \frac{2r_s(2E^2 - m_e^2 c^4)}{\hbar^2 c^2}$
-   $\mu_0^2 = 12r_s^2 k_E^2 - 4r_s^2 k_C^2 + 2r_s\ell(\ell+1) \quad (\text{com } k_E = E/\hbar c, k_C = m_e c/\hbar)$
-   $\chi_3 = 8r_s^3 (4k_E^2 - k_C^2) - 4r_s^2\ell(\ell+1)$

---

### 38.2.2 Os Efeitos Físicos das Altas Potências de Campo Próximo

A presença de termos de ordem superior na equação radial fornece descrições para fenômenos associados, na formulação convencional, a correções radiativas de *loops* em QED:

#### A. O Termo de Viscosidade de Alta Ordem e a Fricção Métrica

O termo de primeira derivada $\left( \frac{4r_s^2 + 4r_s\tau_0}{r^3} \right)\frac{d\mathcal{R}}{dr}$ e potências superiores atuam como uma viscosidade não-linear induzida pela curvatura. Conforme o elétron penetra as camadas mais densas do vácuo deformado próximo ao núcleo, o escoamento sofre um amortecimento reológico intrínseco.

#### B. Polarização de Vácuo Geométrica e o Lamb Shift

Na formulação de Dirac, os estados $2s_{1/2}$ e $2p_{1/2}$ apresentam degenerescência. A quebra dessa degenerescência, conhecida como Lamb Shift, é descrita na QED convencional por meio do potencial de Uehling associado a correções radiativas. Na GDQ, essa separação é descrita a partir do termo em $\mathcal{O}(1/r^3)$:

$$\mathcal{V}_{\text{pol}}(r) \propto \frac{\chi_3}{r^3} = \frac{8r_s^3 (4k_E^2 - k_C^2) - 4r_s^2\ell(\ell+1)}{r^3}$$

-   **Estados $s$ ($\ell = 0$):** A amplitude radial do sóliton $\mathcal{R}(r)$ é não-nula na origem ($r \to 0$), fazendo com que o elétron experimente a máxima intensidade desta barreira compressiva de campo próximo.
-   **Estados $p, d$ ($\ell > 0$):** Possuem um nó radial na origem ($\mathcal{R}(0) = 0$), tornando-os imunes a esta barreira geométrica de curto alcance.

Esta diferença de interação elástica quebra a degenerescência e gera o Lamb Shift como efeito da própria geometria de campo próximo.

#### C. Quebra da Simetria de Runge-Lenz

O potencial coulombiano puro $1/r$ possui a simetria oculta $SO(4)$ descrita pela conservação do vetor de Laplace-Runge-Lenz. A série elástica infinita de campo próximo da GDQ, especificamente os termos em $1/r^3$ e além, quebra essa simetria, forçando uma precessão geodésica quântica da órbita do sóliton elétron.

---

### 38.2.3 Relação de Recorrência Multi-Termo e Determinantes de Hill

Devido à presença dos termos $\mathcal{O}(1/r^3)$, $\mathcal{O}(1/r^4)$ e potências superiores, o método de Frobenius não se fecha em uma relação de dois termos. Ao postularmos a série regular $\mathcal{R}(r) = e^{-\gamma r} \sum_{k=0}^{\infty} a_k r^{k+s}$, as potências superiores no coeficiente de arraste acoplam coeficientes distantes, gerando uma **relação de recorrência de múltiplos termos**:

$$A_k a_{k+1} + B_k a_k + C_k a_{k-1} + D_k a_{k-2} = 0$$

Onde os acoplamentos $C_k$ e $D_k$ são governados diretamente pelas potências de deformação de campo próximo $\chi_3$ e $\chi_4$.

Para garantir a integrabilidade do fluxo no infinito, a condição de truncamento da série infinita generaliza-se: ela exige que o **determinante da matriz infinita de Jacobi (ou determinante de Hill)** seja identicamente nulo:

$$\det \begin{pmatrix} 
B_0 & A_0 & 0 & 0 & \dots \\ 
C_1 & B_1 & A_1 & 0 & \dots \\ 
D_2 & C_2 & B_2 & A_2 & \dots \\ 
0 & D_3 & C_3 & B_3 & \dots \\ 
\vdots & \vdots & \vdots & \vdots & \ddots 
\end{pmatrix} = 0$$

As raízes desse determinante transcendente fornecem as frequências de holonomia (autovalores de energia) exatas do sistema, mesclando os números quânticos discretos com as deformações elásticas não-lineares de campo próximo.

> [!NOTE]
> **A Solução Geral de Campo Próximo via Funções Confluentes de Heun**
> 
> No regime exato de campo próximo (Parte II), a presença de termos polinomiais de ordem superior ($\mathcal{O}(1/r^3)$ e além) e de múltiplas singularidades físicas na variedade complexa altera a natureza da equação diferencial radial.
> 
> A equação possui duas singularidades regulares (em $r = 0$, que é a origem física do nó topológico, e em $r = 2r_s$, correspondente ao raio de deformação crítica conformal do próton onde $f(r)=0$) e uma singularidade irregular no infinito ($r = \infty$). Equações lineares de segunda ordem com esta estrutura de singularidades pertencem à classe da **Equação Confluente de Heun**:
> 
> $$\frac{d^2 y}{dz^2} + \left[ \alpha_0 + \frac{\beta + 1}{z} + \frac{\gamma + 1}{z - 1} \right] \frac{dy}{dz} + \left[ \frac{\mu}{z} + \frac{\nu}{z - 1} \right] y = 0$$
> 
> Onde $z = \frac{r}{2r_s}$ é a coordenada radial normalizada.
> 
> A solução exata mais geral para a amplitude radial $\mathcal{R}(z)$ da densidade do sóliton elétron é expressa pela combinação linear das funções confluentes de Heun $H_C(p, \beta, \gamma, \delta, \eta; z)$:
> 
> $$\mathcal{R}(z) = C_1 \cdot z^s (z - 1)^u e^{-\gamma_0 z} H_C(p, \beta, \gamma, \delta, \eta; z) + C_2 \cdot z^{-s} (z - 1)^u e^{-\gamma_0 z} H_C(p, -\beta, \gamma, \delta, \eta; z)$$
> 
> Onde as constantes e parâmetros ($\beta, \gamma, \delta, \eta, p$) são mapeados unicamente pelas constantes físicas do vácuo ($\hbar, m_e, E, \ell, \alpha, \tau_0$).
> 
> Assim como no caso confluente de Kummer, a integrabilidade do fluxo e a condição de contorno de confinamento no vácuo exigem que a função confluente de Heun se degenere em um polinômio finito (Heun Polynomial). Isto ocorre sob duas condições simultâneas:
> 1. O parâmetro de crescimento assintótico satisfaz uma restrição linear inteira (condição de truncamento na relação multi-termo).
> 2. O determinante de Hill (Jacobi) de tamanho correspondente colapsa a zero ($\det \mathbf{M} = 0$).
> 
> Essa formulação Heuniana descreve o Lamb Shift e o comportamento de campo próximo sob uma perspectiva geométrica, relacionando a física atômica fina com a modelagem do vácuo.

---

## 38.3 Acoplamento Solitônico Bidirecional e Hidrogênio Muônico

### 38.3.1 O Múon como Sonda de Campo Próximo

No **hidrogênio muônico**, o elétron de gênero $n=1$ é substituído por um múon (também um sóliton elementar de gênero $n=1$, mas com massa $m_\mu \approx 207\,m_e$).

A maior massa do múon faz com que sua frequência estrutural de onda de compactação volumétrica ($\gamma_\mu$) seja maior:

$$\gamma_\mu = \frac{\sqrt{m_\mu^2 c^4 - E^2}}{\hbar c} \gg \gamma_e$$

Como a coordenada de escoamento do vácuo quântico é dada por $\rho = 2\gamma r$, o raio físico orbital de Bohr correspondente encolhe por um fator de 207:

$$a_{0,\mu} \approx 2.56 \times 10^{-13} \text{ m}$$

Diferente do elétron, que orbita na periferia de campo fraco, o sóliton múon é forçado a escoar na vizinhança proximal do nó do próton ($n=3$), ativando os termos de ordem superior ($\frac{\chi_3}{r^3}$, $\frac{\chi_4}{r^4}$ e o arraste viscoso de curto alcance).

---

### 38.3.2 O Fluxo de Ricci Reativo e a Deformação Mútua dos Sólitons

Na GDQ, os nós elásticos não se comportam como corpos rígidos. O acoplamento entre o múon e o próton é **bidirecional**. O estresse reológico e a torção gerados pelo fluxo do múon de alta energia injetam um termo de fonte reativa diretamente na equação de evolução da métrica do próprio próton, governada pelo [[17 - Monotonicidade sob Torção de Cartan|fluxo de Ricci]] modificado:

$$\frac{\partial g_{ij}}{\partial \tau} = -2\left( R_{ij} + \nabla_i\nabla_j f \right) + \kappa_{\text{vac}} \left( \mathcal{T}_{\text{próton}} \cdot \mathcal{T}_{\text{múon}} \right)$$

Onde a fonte $(\mathcal{T}_{\text{próton}} \cdot \mathcal{T}_{\text{múon}})$ representa a contração local das densidades de torção antissimétrica de Cartan dos dois sólitons em proximidade extrema.

#### O Sinal da Contração Torsional

Como o múon e o próton possuem orientações topológicas opostas na malha elástica (representando cargas opostas), as suas vorticidades intrínsecas de Cartan estão orientadas de forma antiparalela. A contração tensorial do produto de suas torções é negativa:

$$\kappa_{\text{vac}} \left( \mathcal{T}_{\text{próton}} \cdot \mathcal{T}_{\text{múon}} \right) < 0$$

Este termo atua como um sumidouro de volume conformal na vizinhança da origem. Ele induz uma contração conformal elástica na garganta hiperbólica do próton, encolhendo o perfil topológico do seu nó de gênero $n=3$.

---

### 38.3.3 A Resolução da Anomalia do Raio do Próton

Experimentalmente, a medição do raio de carga do próton usando hidrogênio muônico fornece um valor significativamente menor ($\Delta r_p \approx -0.042 \text{ fm}$) do que as medições tradicionais com hidrogênio eletrônico ou espalhamento de elétrons.

Na GDQ, essa discrepância é analisada desvinculando-se a caracterização do próton de um raio estático invariante:
-   Quando o próton é acoplado ao elétron leve, a impedância elástica gerada pelo elétron na periferia é insignificante, e o próton mantém seu raio de relaxação de vácuo livre ($r_p \approx 0.88 \text{ fm}$).
-   Quando o próton é acoplado ao múon pesado em órbita ultra-próxima, o estresse de cisalhamento da torção mútua contrai conformalmente a métrica da garganta hiperbólica. A garganta hiperbólica associada ao próton experimenta uma contração elástica durante o acoplamento muônico, apresentando um raio efetivo menor ($r_{p,\mu} \approx 0.84 \text{ fm}$).

Dessa forma, a variação observada no raio de carga do próton é descrita como decorrente do estresse reológico associado ao acoplamento solitônico bidirecional em campo próximo, no qual o raio efetivo do defeito topológico comporta-se como uma propriedade dinâmica determinada pelo estresse do acoplamento solitônico bidirecional.


