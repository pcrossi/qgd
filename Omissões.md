# Relatório de Faltas e Omissões do Manuscrito Reestruturado em Relação ao Legado

> [!warning] Auditoria canônica posterior
> Este arquivo preserva o diagnóstico histórico de perdas editoriais, mas não
> pode ser lido como lista de pendências científicas. Depois da conferência das
> questões consolidadas, vários itens abaixo foram recuperados no manuscrito
> por suas demonstrações vigentes, e não pelas fórmulas antigas:
>
> - a difusão variável de Nelson, incluindo todos os termos de Itô, foi
>   reinserida em `01.8` e em nota própria a partir da Questão 16;
> - NESS foi recuperado como redução macroscópica efetiva, sem identificar
>   $\tau$ com uma quinta dimensão física, conforme a Questão 21;
> - o problema dos fantasmas foi reinserido como construção do quociente
>   físico, jacobiano geométrico e auditoria BRST, conforme as Questões 4 e 34;
> - Ward e Slavnov--Taylor foram recuperadas pela covariância espectral;
> - o polo de Landau foi recuperado pelo cálculo $U(1)$ com heat kernel e
>   saturação ultravioleta, conforme a Questão 35.
>
> Não foram restauradas como provas a antiga função beta, a identidade de
> cancelamento de determinantes sem derivação, a seleção dinâmica de $n=4$ por
> Bohm/Atiyah--Singer, nem a identificação automática de $\tau$ com tempo
> físico. Esses elementos permanecem registro histórico ou programa futuro.

## Quadro canônico após a recuperação

| Item deste relatório | Situação vigente | Destino editorial |
|---|---|---|
| NESS e reologia | recuperado como redução efetiva; $\tau\neq t$ | `01.9` e nota de NESS |
| derivada total após continuação | já estava demonstrada | `01.5` e nota de bordo |
| Nelson multidimensional | recuperado com termos de Itô | `01.8` e nota de difusão variável |
| $m_0$ como massa do nêutron | não demonstrado por Q16 | não reinserido como teorema |
| $T^4$ como espaço de fase interno | interpretação possível, não consequência topológica | capítulo próprio após construção do mapa físico |
| seleção de $n=4$ por Bohm | não demonstrada | registro histórico em `02.2` |
| seleção de $n=4$ por Atiyah--Singer | programa futuro | `02.2` e `possibilidades.md` |
| ângulo dinâmico de Wick | não derivado da ação oficial | não usado como fundamento |
| fórmula histórica para tempo complexo | substituída pela variável causal auditada | Capítulo 3 e suas notas |
| autoenergia fermiônica legada | comparação efetiva, não loop fundamental | substituída pela Hessiana oficial |
| diluição holográfica de $\rho_\Lambda$ | não demonstrada pela ação local | não reinserida como resultado |
| anomalia conforme como motor | analogia externa, não identidade fundamental | não reinserida como equação GDQ |
| fantasmas | fechado no setor declarado | `04.7` e nota do quociente físico |
| polo de Landau | fechado condicionalmente em $U(1)$ | `04.7` e nota da polarização |
| função beta histórica | refutada e superada | preservada apenas como histórico |

Este relatório identifica de forma detalhada as ideias, intuições físicas, passagens matemáticas (equações, coeficientes e normalizações) e resultados que constavam na versão legada (`pt-br/`, capítulos 00 a 05) e foram simplificados, omitidos ou esquecidos na nova estrutura (`manuscrito/`, capítulos 1 a 5).

---

## 1. Capítulo 1: O Problema Inicial (Wiener vs. Feynman)
**Fontes comparadas:** `pt-br/00 - Introdução Terminológica.md` e `pt-br/01 - O Problema Inicial.md` contra `manuscrito/01_initial_problem/`

### 1.1 Ontologia do Tempo Real ($\tau$) como Reologia e o NESS
* **Omissão:** Na versão legada (`pt-br/00`), o espaço-tempo quadridimensional ($x, y, z, t$) é concebido estritamente como um **Estado Estacionário de Não-Equilíbrio (NESS - Non-Equilibrium Steady State)**. A dinâmica quântica e a medição ocorrem ao longo de uma quinta dimensão real (o parâmetro de fluxo de Perelman $\tau$). A propagação causal e a medição não são evoluções cronológicas em $t$, mas sim um relaxamento geométrico profundo de todo o universo-bloco 4D ao longo de $\tau$.
* **Status no Manuscrito:** Essa visão ontológica do NESS e o relaxamento do universo-bloco foram bastante atenuados, restando no manuscrito atual apenas menções discretas a $\tau$ como fluxo matemático de renormalização ou difusão abstrata, enfraquecendo a intuição de reologia cósmica da teoria.

### 1.2 Destruição Euclidiana da Simetria de Calibre por Wick
* **Simplificação:** O texto legado em "A Quebra de Invariância na Derivada Total" detalhava fisicamente que uma transformação de calibre trivial em Minkowski ($L' = L + dF/dt$) altera apenas a fase global sem afetar as probabilidades, mas sob a rotação de Wick ela se torna um fator exponencial real ($e^{-[F(t_1)-F(t_0)]}$) que afeta diretamente o peso de Boltzmann e destrói a convergência estatística na integral de Wiener.
* **Status no Manuscrito:** No arquivo `01.5`, a discussão foi consideravelmente simplificada e abstratizada ("alterar a normalização aparente do kernel..."), diluindo a explicação mecânica direta de como o calibre interfere na convergência da medida estocástica de Wiener.

### 1.3 Equações Estocásticas Multidimensionais de Nelson
* **Omissão Matemática:** O texto legado apresentava a generalização do cálculo estocástico de Nelson para o vácuo de Kähler com o fator de escalonamento métrico $\Omega(x,t) = m(x,t)/m_0$. As seguintes equações explícitas foram omitidas na versão nova:
  * O processo estocástico cinemático modificado:
    $$dx^i(t) = b_\pm^i(x(t), t)dt + \sqrt{2\nu_0 \cdot \Omega^{-1}} \, dW^i(t)$$
  * A velocidade osmótica/difusiva resultante:
    $$u^i = \nu_0 \Omega^{-1} \nabla^i \ln \rho$$
  * A equação de forças estocásticas generalizada:
    $$m_0 \Omega \left( \frac{\partial v^i}{\partial t} + v^j \nabla_j v^i \right) = -\nabla^i \left( V_{\text{clássico}} + Q_{\text{Bohm}} \right)$$
* **Status no Manuscrito:** Em `01.8` e na nota associada, essas equações multidimensionais explícitas foram removidas, substituídas por um alerta geral de que a variação espacial de $\Omega$ gera termos adicionais (como $\nabla \Omega \cdot \nabla \rho$ e $\rho \Delta \Omega$) na Fokker-Planck.

### 1.4 A Massa do Nêutron como Atrator Dinâmico
* **Omissão:** O texto legado afirmava que a massa de corte $m_0$ do vácuo de Kähler ($\nu_0 = \hbar / 2m_0$) é deduzida no Grafo Acíclico Direcionado (DAG) da GDQ como um **atrator dinâmico (output de baixa energia) decorrente do horizonte de confinamento conformal**, representando a escala em que o fluxo de Perelman-Madelung estabiliza o solíton bariônico fundamental (o nêutron) contra o colapso.
* **Status no Manuscrito:** Essa conexão entre a escala $m_0$, o confinamento conformal e a estabilidade do nêutron foi retirada, restando em `01.8` apenas a menção de que $m_0$ é um parâmetro a ser deduzido sem calibrações ad-hoc.

---

## 2. Capítulo 2: A Geometrização da Matéria
**Fontes comparadas:** `pt-br/02 - A Geometrização da Matéria.md` contra `manuscrito/02_geometrization/`

### 2.1 Significado Físico das 4 Dimensões Complexas Extra
* **Omissão:** O texto legado explicava que as 4 dimensões reais complementares (o setor ortogonal $T^\perp \mathcal{M}_{\mathbb{R}}$ da subvariedade Lagrangiana maximal) não são dimensões espaciais compactificadas (como em teorias tipo Kaluza-Klein), mas constituem o **espaço de fase interno do vácuo quântico**, onde residem a velocidade de Madelung $v^\mu$, as flutuações de Nelson e a torção de Cartan $B_{\mu\nu\lambda}$.
* **Status no Manuscrito:** Essa conceituação física das dimensões extras foi omitida no manuscrito atual (p. ex., em `02.2`), restando apenas uma discussão matemática formal de que a dimensão complexa $n=4$ é consequência da escolha axiomática do bulk local $M = \mathbb{R}^4 \times T^4$.

### 2.2 Estabilização Dimensional pelo Potencial de Bohm
* **Omissão:** O texto original apresentava uma análise de estabilidade para justificar por que a dimensão holomorfa da variedade de Kähler deve ser precisamente $n=4$:
  * Se $n \leq 3$, a força repulsiva de Bohm $\mathcal{V}_{\text{Bohm}}(r) \propto r^{-(2n-3)}$ decai muito lentamente no UV em relação à curvatura de Einstein-Bismut, colapsando a geometria em uma singularidade de densidade infinita.
  * Se $n \geq 5$, a singularidade repulsiva no UV é severa e provoca uma *pinçada de pescoço espacial (neckpinch)*, quebrando a variedade em domínios desconexos.
  * Se $n=4$, a força de Bohm escala criticamente como $r^{-5}$, equilibrando a contração do fluxo de Perelman de quarta ordem na conexão de Bismut, travando a métrica em um atrator UV estável.
* **Status no Manuscrito:** Toda essa análise dinâmica e dimensional de estabilidade foi removida e omitida na reestruturação do capítulo 2.

### 2.3 Travamento Conformal via Anomalias e Atiyah-Singer
* **Omissão:** O texto legado demonstrava que o acoplamento entre as correntes de folheação do Toro $T^5$ e a estrutura quiral da representação adjunta força a anulação estrita do polinômio de anomalia gauge-gravidade $\text{Tr}(\mathcal{R}^4) - \frac{1}{4}(\text{Tr}\mathcal{R}^2)^2$ no teorema do índice de Atiyah-Singer se, e somente se, a dimensão holomorfa for exatamente $n=4$.
* **Status no Manuscrito:** Essa derivação foi completamente retirada e classificada no `preservation_map.md` do capítulo 2 como "programa futuro/possibilidades", sob a justificativa de que faltavam cálculos detalhados do fibrado na versão original.

---

## 3. Capítulo 3: Causalidade Complexa e o Fim do Paradoxo de Wick
**Fontes comparadas:** `pt-br/03 - Causalidade Complexa e o Fim do Paradoxo de Wick.md` contra `manuscrito/03_complex_causality/`

### 3.1 Equação de Escoamento do Ângulo de Wick ($\theta$)
* **Omissão Matemática:** A seção legada `3.3` definia a complexificação do tempo como $dt_{\mathbb{C}} = e^{-i\theta(\tau)} d\tau$ e propunha uma equação dinâmica orientada pela entropia de Perelman $\mathcal{W}$ para a evolução de $\theta$:
  $$\frac{d\theta}{d\tau} = -\kappa \frac{\partial \mathcal{W}}{\partial \theta}$$
  Deduzia-se que:
  * No limite UV ($\tau \to 0$), a densidade oscila e o potencial de Bohm domina ($\langle Q_{\text{Bohm}} \rangle \gg \langle R_g \rangle$), forçando $\theta \to 0$ (regime Lorentziano/Minkowskian de **Feynman**).
  * No ponto de sela ($\tau \to \infty$), o torque se anula e $\theta \to \pi/2$ (regime Euclidiano de **Wiener**, onde $dt_{\mathbb{C}} = -i d\tau$).
* **Status no Manuscrito:** Esta interpolação dinâmica baseada no gradiente de entropia de Perelman foi **completamente omitida** do corpo principal (rebaixada a "programa futuro/possibilidades" no mapa de preservação de `03.8`, devido a não ser derivada diretamente da ação oficial).

### 3.2 Forma Analítica do Tempo Complexificado e a Regularização
* **Omissão:** O texto legado propunha uma forma explícita para a coordenada de tempo quântica holomorfa:
  $$dt_{\mathbb{C}} = dt_{\text{real}} + i \left( \frac{\hbar}{M_p c^2} \right) \frac{d\tau_{\text{fluxo}}}{r_p^2}$$
  e a integral de trajetória transmutada:
  $$\Psi[\gamma] = \int \mathcal{D}[\gamma] \exp\left( \frac{i}{\hbar} S_R \right) \cdot \exp\left( - \mathcal{W}(g, f, \tau) \right)$$
  mostrando que o crescimento de $\mathcal{W}$ sob o fluxo de Ricci atua como um form factor amortecedor ultravioleta.
* **Status no Manuscrito:** Ambas as equações e o papel explícito da entropia de Perelman como amortecedor foram removidos. O capítulo reestruturado agora nega a igualdade genérica $S_I = \hbar \mathcal{W}$ e restringe o tema à comparação histórica.

---

## 4. Capítulo 4: A Ação Funcional e Consistência Quântica (Loops)
**Fontes comparadas:** `pt-br/04 - A Ação Funcional e Consistência Quântica (Loops).md` contra `manuscrito/04_action_consistency/`

### 4.1 Cálculo Explicito de Autoenergia a 1-Loop e Propagador Modificado
* **Omissão Matemática:** Na seção `4.3` da versão legada, apresentava-se o propagador fermiônico modificado pela torção de Cartan:
  $$S_F(p) = \frac{1}{\gamma^\mu p_\mu - m_0 - i \Pi_{\text{torsão}}(p^2)}$$
  onde $\Pi_{\text{torsão}}(p^2) \propto \exp(p^2/\Lambda_C^2)$. A partir disso, calculava-se explicitamente o loop de autoenergia do elétron de primeira ordem:
  $$\Sigma(p) = e^2 \int_0^{\Lambda_C} \frac{k^3 \, dk}{8\pi^2} \frac{2m_0 - \slashed{k}}{k^2 + m_0^2} \cdot \exp\left( -\frac{k^2}{\Lambda_C^2} \right)$$
  destilando o resultado analítico exato:
  $$\Sigma(p) = \frac{e^2 m_0}{4\pi^2} \left[ \ln\left( \frac{\Lambda_C^2}{m_0^2} \right) - \gamma_E + \mathcal{O}\left(\frac{m_0^2}{\Lambda_C^2}\right) \right]$$
* **Status no Manuscrito:** Esse cálculo detalhado e suas equações foram **completamente omitidos** do arquivo `04.7`, que agora trata a consistência em loops de forma estritamente abstrata e geral.

### 4.2 Diluição Holográfica da Constante Cosmológica
* **Omissão:** O texto legado apresentava a relação que conecta o cutoff UV de Cartan ($\Lambda_C$) à constante cosmológica observada no infravermelho ($\rho_\Lambda$) por diluição holográfica unidimensional ao longo do raio de Hubble $R_H$:
  $$\rho_\Lambda = \rho_{\text{rede}} \left( \frac{r_p}{R_H} \right) \propto \frac{\Lambda_C^4}{R_H}$$
* **Status no Manuscrito:** Esta fórmula física foi excluída do novo Capítulo 4, restando apenas discussões abstratas de independência de escalas e adiando o cálculo cosmológico.

---

## 5. Capítulo 5: Renormalização e Anomalia Conforme
**Fontes comparadas:** `pt-br/05 - Renormalização e Anomalia Conforme.md` contra `manuscrito/05_equations_conservation/` (e verificação em `06_global_local_bridge/`)

### 5.1 Omissão Quase Total do Conteúdo Físico Original
O novo Capítulo 5 (`05_equations_conservation`) foi focado exclusivamente em deduzir as variações de primeira ordem da ação oficial (Noether, correntes de fase, densidade e métrica). Com isso, **quase a totalidade do Capítulo 5 legado foi omitida e não foi transferida para nenhum outro capítulo (incluindo o Capítulo 6)**. As perdas específicas são descritas abaixo:

### 5.2 Anomalia Conforme como o "Motor" do Fluxo de Ricci
* **Omissão:** O acoplamento conceitual que identifica a equação clássica do grupo de renormalização com a evolução métrica do fluxo de Ricci:
  $$\frac{\partial g_{ij}}{\partial \ln \mu} = \beta_{ij} \quad \longleftrightarrow \quad \frac{\partial g_{ij}}{\partial \tau} = -2(R_{ij} + \nabla_i \nabla_j f)$$
  em que o traço do tensor de energia-momento ($T^\mu_\mu$) atua como a tensão topológica que força a deformação do espaço-tempo até a estabilização do solíton, foi **completamente apagado**.

### 5.3 Cancelamento Algébrico dos Fantasmas de Faddeev-Popov
* **Omissão Matemática:** O argumento detalhado demonstrando que a rigidez de Kähler e a 2-forma fechada $\omega$ cancelam os modos não-físicos longitudinais e eliminam a necessidade de fantasmas artificiais via a identidade de Bianchi complexa e a equação:
  $$\det\left( \frac{\partial (d\omega)}{\partial \epsilon} \right) \cdot \Delta_{\text{longitudinal}}(g) = 1$$
  foi **completamente omitido**. O novo manuscrito trata fantasmas apenas como "linguagem auxiliar de auditoria" em `04.7`.

### 5.4 Eliminação Física do Polo de Landau via Potencial de Bohm
* **Omissão:** O mecanismo físico detalhado mostrando que a atração clássica entre cargas no limite $r \to 0$ é vencida pela barreira repulsiva do potencial quântico de Bohm $\mathcal{V}_{\text{Bohm}} \to +\infty$ (que deforma a métrica de Kähler localmente via tensor de Ricci, dilatando a "régua" de distâncias e tornando o ponto $r=0$ inacessível), foi **totalmente omitido**.

### 5.5 Função Beta Geométrica Modificada e Ponto Fixo UV Estável ($\alpha_{\text{UV}}$)
* **Omissão Matemática:** O modelo exato da função-$\beta$ geométrica modificada pelo vácuo de Kähler com a escala de corte de Cartan $\Lambda_C$:
  $$\beta(\alpha) \equiv \frac{d\alpha}{dt} = -b_0 \alpha^2 + \gamma_C \alpha^3 \exp\left( -\frac{\Lambda_C^2}{Q^2} \right)$$
  e a elegante dedução do ponto fixo ultravioleta não-trivial e estável:
  $$\alpha_{\text{UV}} = \frac{1}{3\pi \gamma_C}$$
  que resolve em definitivo o problema da trivialidade quântica no vácuo de Kähler, foram **completamente deletados** e não aparecem em nenhuma seção da nova estrutura.

---

## Recomendações e Próximos Passos Editoriais

1. **Reinserir a Ontologia Reológica do NESS:** É fundamental readicionar a explicação conceitual de $\tau$ como coordenada reológica onde o universo 4D relaxa de forma estacionária no Capítulo 1 e no acordo terminológico (`01.2`).
2. **Reassentar a Derivação Dimensional $n=4$ (Potencial de Bohm):** A análise de estabilidade e o equilíbrio entre a atração do fluxo de Perelman e a repulsão da pressão de Bohm no Capítulo 2 constitui um dos pontos altos de intuição e elegância do manuscrito legado. Ela deve ser readicionada como um "Teorema de Redução Efetiva" ou "Hipótese de Confinamento".
3. **Mapear a Função Beta e o Polo de Landau:** A exclusão completa do mecanismo que elimina o Polo de Landau e a anomalia conforme desprotege a consistência perturbativa da teoria. Estes tópicos devem ser reinseridos, seja no Capítulo 4 (loops e renormalização) ou sob a forma de uma seção de "Consistência e Limites de Altas Energias".
4. **Recuperar Nelson Multidimensional:** As equações estocásticas explícitas e a velocidade osmótica no vácuo de Kähler com variação espacial de massa ($\Omega(x,t)$) devem ser reintroduzidas para que a conexão com a mecânica quântica usual no Capítulo 7 não pareça desconectada de sua fundamentação mecânica original.
