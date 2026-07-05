# Capítulo 21 - Estados Estacionários de Não-Equilíbrio (NESS) e a Emergência da Irreversibilidade

O formalismo da [[2 - A Geometrização da Matéria|Geometrodinâmica Quântica (GDQ)]] descreve o vácuo físico e suas excitações solitônicas elementares como sistemas dinâmicos abertos acoplados à [[12 -  O Tempo de Tunelamento Quântico (Efeito Hartman)|rede de Kähler]]. Um dos maiores desafios conceituais da teoria reside na aparente contradição entre a estabilidade unitária e reversível dos sólitons individuais e a irreversibilidade termodinâmica macroscópica. 

Neste capítulo, essa tensão é equacionada demonstrando-se como os Estados Estacionários de Não-Equilíbrio (NESS) microscópicos no [[17 - Monotonicidade sob Torção de Cartan|vácuo de Perelman]] dão origem à Segunda Lei da Termodinâmica no limite macroscópico através de processos de coarse-graining e espalhamento de fase.

---

## 21.1 O Ponto Fixo do NESS e o Micro-Balanço Detalhado

Na escala elementar do sóliton ($\sim 10^{-15}\text{ m}$), a evolução métrica sob o fluxo de Ricci modificado pelo vetor de DeTurck é balanceada pelo termo de força do [[3 - Causalidade Complexa e o Fim do Paradoxo de Wick|potencial avançado de Sudarshan]]. Define-se a densidade local de produção de entropia geométrica de Perelman $\sigma_{\mathcal{W}}$ como:
$$\sigma_{\mathcal{W}} = 2 |R_{ij} + \nabla_i \nabla_j f|_{g}^2 e^{-f}$$

No regime de ponto fixo (sóliton isolado), as restrições do potencial de Sudarshan atuam como um contratermo ao [[1 - O Problema Inicial - A Divergência entre a Integral de Feynman e a de Wiener|fluxo parabólico dissipativo de Ricci]]. A integral global do funcional de entropia $\mathcal{W}$ resulta em:
$$\frac{d\mathcal{W}}{d\tau}\Big|_{\text{sóliton}} = \int_{\mathcal{M}} \sigma_{\mathcal{W}} dV - \Phi_{\text{Sudarshan}} = 0$$

Nesta escala fundamental, a unitaridade é preservada e não há seta de tempo macroscópica; o sóliton é uma estrutura estável e eterna imersa no vácuo quântico, caracterizando um Estado Estacionário de Não-Equilíbrio (NESS) com produção líquida de entropia nula.

---

## 21.2 O Mecanismo de Espalhamento de Fano de Vácuo

A quebra de simetria temporal e a consequente emergência da irreversibilidade iniciam-se quando o sóliton interage com as flutuações contínuas da rede de Kähler. A interação do estado solitônico discreto $|\phi_D\rangle$ (energia $E_D$) com o contínuo de modos de onda do vácuo $|\psi_E\rangle$ (energia $E$) é descrita através do Hamiltoniano de acoplamento:
$$H = E_D |\phi_D\rangle\langle \phi_D| + \int dE \, E |\psi_E\rangle\langle \psi_E| + \int dE \left( V_E |\phi_D\rangle\langle \psi_E| + V_E^* |\psi_E\rangle\langle \phi_D| \right)$$

Onde $V_E$ representa o elemento de matriz de transição induzido pelas perturbações da métrica local $\delta g_{ij}$. Quando perturbações de fase que não obedecem à condição de quantização estrita ($\oint \omega \neq n h$) incidem sobre o sóliton, elas sofrem espalhamento.

A matriz de espalhamento de fase $S(E)$ exibe um perfil de ressonância de Fano assimétrico para a transmissão de flutuações de curvatura:
$$\sigma(E) = \frac{(q + \epsilon)^2}{1 + \epsilon^2}$$

Onde $\epsilon = \frac{E - E_D - \Delta E}{\Gamma_{\text{Fano}}/2}$ é a energia normalizada e $q$ é o parâmetro de assimetria de Fano. A largura de decaimento $\Gamma_{\text{Fano}}$, que mede a taxa de acoplamento e dissipação de fase para o vácuo de Kähler, é dada por:
$$\Gamma_{\text{Fano}} = 2\pi |V_{E_D}|^2$$

Qualquer perturbação de fase desalinhada é ejetada de forma radial do sóliton em direção à fronteira assintótica como radiação transiente de calibre, representando uma perda irreversível de fase holomorfa para o contínuo infinito de Kähler.

---

## 21.3 O Coarse-Graining de Zwanzig-Mori sobre o Vácuo

Para formalizar a transição para a escala macroscópica de múltiplos corpos, recorremos ao formalismo de projeção de Zwanzig-Mori. Seja $\rho(\Gamma)$ a densidade de probabilidade no espaço de fases estendido da métrica complexa. Define-se o operador de projeção $\mathcal{P}$ que projeta a dinâmica sobre o conjunto de macro-variáveis observáveis (posições e momentos dos centros dos sólitons, $A_i$):
$$\mathcal{P} \rho = \sum_{ij} \langle \rho, A_i \rangle (g^{-1})_{ij} A_j$$

O operador complementar $\mathcal{Q} = 1 - \mathcal{P}$ isola os infinitos graus de liberdade ocultos e flutuações microscópicas do vácuo ($\mathcal{Q}\Gamma$). O operador de Liouville geométrico $\mathcal{L}$ governa a evolução temporal de $\rho$:
$$\frac{\partial \rho}{\partial \tau} = -i\mathcal{L} \rho$$

Aplicando a identidade de projeção à equação de Liouville, obtemos a equação de movimento generalizada de Zwanzig-Mori para a densidade projetada $\mathcal{P}\rho(\tau)$:
$$\frac{\partial \mathcal{P}\rho(\tau)}{\partial \tau} = -i\mathcal{P}\mathcal{L}\mathcal{P}\rho(\tau) - \int_{0}^{\tau} \mathcal{K}(\tau') \mathcal{P}\rho(\tau - \tau') d\tau' + \mathcal{F}(\tau)$$

Onde o termo de memória $\mathcal{K}(\tau')$ e a força estocástica de flutuação $\mathcal{F}(\tau)$ são dados por:
$$\mathcal{K}(\tau') = \mathcal{P}\mathcal{L} e^{-i\mathcal{Q}\mathcal{L}\tau'} \mathcal{Q}\mathcal{L}\mathcal{P}$$
$$\mathcal{F}(\tau) = -i\mathcal{P}\mathcal{L} e^{-i\mathcal{Q}\mathcal{L}\tau} \mathcal{Q}\rho(0)$$

O núcleo de memória $\mathcal{K}(\tau')$ codifica a viscosidade cinemática intrínseca do vácuo ($\nu_0 = \hbar / 2m_0$) e a dissipação acumulada pelas perdas por [[9 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|cisalhamento de Cartan]]. A densidade projetada no espaço macroscópico atua como um [[13 - Regra de Born|fluido de Madelung]] efetivo.

---

## 21.4 A Emergência Assintótica da Segunda Lei (Teorema-$\mathcal{H}$ Geométrico)

Define-se a macro-entropia observável $\mathcal{S}_{\text{macro}}$ integrando a densidade de probabilidade sob o coarse-graining:
$$\mathcal{S}_{\text{macro}} = -k_B \int \bar{\rho} \ln \bar{\rho} \, d\Gamma_{\text{macro}}$$

Onde $\bar{\rho} = \mathcal{P}\rho$. A evolução de $\mathcal{S}_{\text{macro}}$, sob a ação do núcleo de Zwanzig-Mori com memória dissipativa $\mathcal{K}(\tau)$, incorpora a perda contínua de informação das fases ejetadas pelo espalhamento de Fano. A taxa de variação temporal de $\mathcal{S}_{\text{macro}}$ para qualquer macro-processo de não-equilíbrio satisfaz a desigualdade:
$$\frac{d\mathcal{S}_{\text{macro}}}{d\tau} = \int \left( \frac{\mathcal{F}(\tau)^2}{\nu_0 \bar{\rho}} \right) d\Gamma_{\text{macro}} \ge 0$$

---

## 21.5 Conclusão

A seta do tempo e a irreversibilidade termodinâmica não são propriedades primitivas das leis fundamentais do espaço-tempo. Elas emergem de maneira estrita na transição de escala:

1. **Escala Micro (Sóliton):** A estabilidade é unitária e reversível ($\dot{\mathcal{W}} = 0$) devido ao balanço exato de Ricci-Sudarshan.
2. **Mecanismo de Fano (Acoplamento):** Perturbações não-quantizadas são dispersas e ejetadas para as bandas contínuas do vácuo de Kähler.
3. **Escala Macro (Zwanzig-Mori):** A projeção macroscópica sobre as variáveis de centro de massa, ignorando a radiação microscópica dispersa no vácuo, introduz o termo de atrito de memória e resulta na produção positiva de entropia $\dot{\mathcal{S}}_{\text{macro}} \ge 0$, gerando a seta do tempo.
