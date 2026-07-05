# Capítulo 37 - A Resolução Mecânico-Geométrica do Experimento da Dupla Fenda de Young

## 37.1 Ontologia do Sistema e a Descrição Geometrodinâmica

Na interpretação ortodoxa da mecânica quântica (Escola de Copenhague), o experimento da fenda dupla de Young é comumente associado à dualidade onda-partícula, onde se descreve a superposição de estados até que ocorra o processo de medição.

No âmbito da [[2 - A Geometrização da Matéria|Geometrodinâmica Quântica (GDQ)]], busca-se descrever esse fenômeno por meio de um mecanismo físico local e determinístico. A matéria não é um ponto matemático abstrato flutuando em um espaço rígido de Minkowski; ela é descrita pela representação polar de um fluxo elástico do vácuo $f = -\frac{1}{\hbar}(S_I - iS_R)$, onde a densidade e a inércia geométrica estão indissociáveis no [[12 -  O Tempo de Tunelamento Quântico (Efeito Hartman)|vácuo de Kähler]].

A estrutura de uma partícula elementar na GDQ divide-se em duas componentes integradas:

1.  **O nó de torção local (A Partícula):** Um nó topológico altamente localizado, modelado como um *Colapso Geométrico Localizado* estável, que concentra a maior parte da energia de curvatura, comportando-se como um [[8 - Singularidade do Buraco Negro|sóliton]].
    
2.  **O fluxo contínuo (A Onda):** Um escoamento real e compressível de densidade de probabilidade estatística, espalhado tridimensionalmente ao redor do estômato e acoplado à malha elástica.
    

Quando o sistema é lançado em direção à barreira, o nó de torção local localizado (a partícula) desloca-se por uma das fendas. No entanto, o fluido real de Madelung, que carrega o volume conjugado de densidade $\rho = e^{S_I/\hbar} = R^2$, estende-se por todo o espaço acessível da variedade, dividindo o seu volume entre as duas aberturas.

---

## 37.2 Divisão de Volume Métrico e Escoamento de Calibre

Considere a barreira localizada no plano $y = 0$, contendo duas fendas idênticas $A_1$ e $A_2$ separadas por uma distância $d$. A conservação da densidade do fluido do vácuo ao cruzar as aberturas é governada pela Equação de Continuidade, deduzida de primeiros princípios via simetria de fase de Noether na GDQ:

$$\frac{\partial \rho}{\partial \tau} + \tau t_0 \nabla_\mu \left( \rho \cdot \mathbf{v}^\mu \right) = 0$$

Onde $\mathbf{v}^\mu = \frac{1}{m} g^{\mu\bar{\nu}} \partial_{\bar{\nu}} S_R$ representa o campo vetorial de velocidades de corrente balística que deforma difeomorficamente a métrica local.

Ao interceptar o plano de restrição, a integral da medida invariante de fluxo $d\mu = e^{-f}\sqrt{g}d^4x$ sobre as superfícies de fronteira das fendas exige a partição exata da corrente líquida:

$$\int_{A_1} \rho \mathbf{v} \cdot d\mathbf{A} = \int_{A_2} \rho \mathbf{v} \cdot d\mathbf{A} = \frac{1}{2} \mathcal{J}_{\text{total}}$$

As duas fendas atuam, portanto, como duas fontes secundárias idênticas de escoamento hidrodinâmico na variedade complexa. As frentes de fase mecânica $S_R^{(1)}(\mathbf{x}, t)$ e $S_R^{(2)}(\mathbf{x}, t)$ emanadas de cada abertura propagam-se na região pós-fenda e começam a sobrepor-se, esculpindo de forma determinística o perfil global de densidade de probabilidade do fluido:

$$\rho_{\text{total}}(\mathbf{x}, t) = \left| R_1 e^{iS_R^{(1)}/\hbar} + R_2 e^{iS_R^{(2)}/\hbar} \right|^2 = R_1^2 + R_2^2 + 2R_1 R_2 \cos\left( \frac{\Delta S_R}{\hbar} \right)$$

Onde $\Delta S_R = S_R^{(1)} - S_R^{(2)}$ dita a diferença de caminhamento geométrico das linhas de fluxo na métrica de Kähler.

---

## 37.3 Resolução Analítica Explícita do Campo de Perelman

Para descrever a distribuição do padrão de interferência na GDQ, modelam-se os fluxos contínuos que emergem de cada fenda de largura $\sigma_0$ (centradas em $x_1 = -d/2$ e $x_2 = d/2$) como dois pacotes Gaussianos densos propagando-se na aproximação paraxial ao longo do eixo $y$ (onde a velocidade longitudinal constante do sóliton é $v_0$), sob a evolução do [[17 - Monotonicidade sob Torção de Cartan|campo de Perelman]]:

$$\psi_1(x, y) = \frac{1}{(2\pi \sigma_0^2)^{1/4}} \frac{1}{\sqrt{1 + i \frac{y}{y_R}}} \exp\left[ -\frac{(x + d/2)^2}{4\sigma_0^2 \left(1 + i \frac{y}{y_R}\right)} \right] e^{i (k_0 y - \omega_0 t)}$$

$$\psi_2(x, y) = \frac{1}{(2\pi \sigma_0^2)^{1/4}} \frac{1}{\sqrt{1 + i \frac{y}{y_R}}} \exp\left[ -\frac{(x - d/2)^2}{4\sigma_0^2 \left(1 + i \frac{y}{y_R}\right)} \right] e^{i (k_0 y - \omega_0 t)}$$

Onde $y_R = \frac{2 m v_0 \sigma_0^2}{\hbar}$ é o comprimento de *Rayleigh* do vácuo quântico e $\sigma_t^2 = \sigma_0^2 \left(1 + \frac{y^2}{y_R^2}\right)$ é a dispersão espacial dependente da distância $y$.

Decompondo as frações complexas nos expoentes em partes reais e imaginárias:

$$\psi_{1,2}(x, y) = \frac{1}{(2\pi \sigma_t^2)^{1/4}} \exp\left[ -\frac{(x \pm d/2)^2}{4\sigma_t^2} \right] \exp\left[ i \left( k_0 y - \omega_0 t - \frac{1}{2}\arctan\left(\frac{y}{y_R}\right) + \frac{y (x \pm d/2)^2}{4\sigma_t^2 y_R} \right) \right]$$

Somando os dois pacotes $\psi_{\text{total}} = \psi_1 + \psi_2$ e calculando o quadrado do módulo do campo ($\rho = |\psi_{\text{total}}|^2$), obtemos a **função analítica explícita da densidade**:

$$\rho_{\text{total}}(x, y) = \frac{2}{\sqrt{2\pi \sigma_t^2}} \exp\left[ -\frac{x^2 + d^2/4}{2\sigma_t^2} \right] \left[ \cosh\left( \frac{x d}{2\sigma_t^2} \right) + \cos\left( \frac{y d x}{2\sigma_t^2 y_R} \right) \right]$$

Esta função descreve as franjas de densidade observadas no anteparo. O termo de cosseno gera a oscilação das franjas de interferência, enquanto o termo $\cosh$ modula a modulação de envelope dada pelas intensidades individuais de difração das duas fendas.

### 37.3.1 A Natureza Realista dos Mínimos Não Nulos

É digno de nota que o perfil analítico exato $\rho_{\text{total}}(x, y)$ mostra que a interferência destrutiva nos mínimos laterais ($x \neq 0$) não atinge exatamente zero. Isso ocorre porque o termo hiperbólico é estritamente maior que a unidade fora do eixo de simetria:

$$\cosh\left( \frac{x d}{2\sigma_t^2} \right) > 1 \quad \forall x \neq 0$$

Como o valor mínimo do cosseno é $-1$, a soma dos dois fatores no colchete é estritamente positiva para qualquer ponto fora da origem:

$$\cosh\left( \frac{x d}{2\sigma_t^2} \right) + \cos\left( \frac{y d x}{2\sigma_t^2 y_R} \right) > 0$$

Fisicamente, este comportamento reflete o fato de que os dois pacotes Gaussianos (que modelam fendas com largura finita real) estão centrados em posições espaciais distintas ($x = \pm d/2$). Portanto, suas amplitudes locais diferem em qualquer coordenada transversal fora do eixo central $x=0$, impedindo o cancelamento destrutivo completo das fases opostas.

Esse comportamento decorre do tratamento via pacotes de ondas de extensão finita em vez de aproximações de ondas planas infinitas. No campo distante ($y \gg y_R$), conforme os pacotes se expandem lateralmente e sua largura domina sobre a separação ($\sigma_t \gg d$), o termo de $\cosh$ decai assintoticamente para $1$, e os vales aproximam-se de zero, recuperando o limite clássico das aproximações de livros-texto.

---

## 37.4 Frentes de Pressão Bohmiana e Guiagem Topológica

A amplitude real do campo $R(x, y) = \sqrt{\rho_{\text{total}}(x, y)}$ é expressa por:

$$R(x, y) = F(x, y) \cdot [H(x, y)]^{1/2}$$

Onde:
-   $F(x, y) = \left(\frac{2}{\sqrt{2\pi \sigma_t^2}}\right)^{1/2} \exp\left[ -\frac{x^2 + d^2/4}{4\sigma_t^2} \right]$ é o envelope difrativo.
-   $H(x, y) = \cosh\left(\beta x\right) + \cos\left(k_x x\right)$ é o fator de interferência quântica pura.
-   $\beta = \frac{d}{2\sigma_t^2}$ e $k_x = \frac{y d}{2\sigma_t^2 y_R}$.

Na aproximação paraxial, a guiagem do sóliton no plano transversal é governada pela pressão geométrica de fluxo decorrente da derivada de segunda ordem de $R(x, y)$ em relação à coordenada transversal $x$. A pressão geométrica (ou [[10 - Resolução Mecânico-Geométrica do Experimento de Stern-Gerlach|potencial quântico de Bohm]]) $\mathcal{V}_{\text{Bohm}}(x, y) = -\frac{\hbar^2}{2m} \frac{1}{R} \frac{\partial^2 R}{\partial x^2}$ é obtida calculando as derivadas parciais:

$$\frac{1}{F} \frac{\partial^2 F}{\partial x^2} = \frac{x^2}{4\sigma_t^4} - \frac{1}{2\sigma_t^2}$$

$$\frac{\partial H}{\partial x} = \beta \sinh(\beta x) - k_x \sin(k_x x)$$

$$\frac{\partial^2 H}{\partial x^2} = \beta^2 \cosh(\beta x) - k_x^2 \cos(k_x x)$$

Substituindo os termos pela regra da cadeia, deduzimos a **expressão analítica explícita para a pressão geométrica**:

$$\mathcal{V}_{\text{Bohm}}(x, y) = -\frac{\hbar^2}{2m} \left[ \frac{x^2}{4\sigma_t^4} - \frac{1}{2\sigma_t^2} - \frac{x \left[ \beta \sinh(\beta x) - k_x \sin(k_x x) \right]}{2 \sigma_t^2 H(x, y)} - \frac{\left[ \beta \sinh(\beta x) - k_x \sin(k_x x) \right]^2}{4 H(x, y)^2} + \frac{\beta^2 \cosh(\beta x) - k_x^2 \cos(k_x x)}{2 H(x, y)} \right]$$

### 37.4.1 Análise Matemática das Barreiras de Pressão

A análise matemática dessa equação revela o mecanismo de guiagem:

1.  **Franjas Construtivas (Máximos de Intensidade):** Onde $\cos(k_x x) \approx 1$, o denominador $H(x, y)$ é máximo. O potencial $\mathcal{V}_{\text{Bohm}}$ é regular, suave e apresenta vales locais de energia que canalizam o nó de torção local ao longo de trajetórias estáveis.
2.  **Franjas Destrutivas (Mínimos de Intensidade/Nodos):** À medida que nos aproximamos de um ponto de interferência destrutiva ideal, $\cos(k_x x) \to -1$. Próximo ao centro do feixe ($x \approx 0$), temos $\cosh(\beta x) \to 1$. Consequentemente, o denominador de interferência colapsa para zero:
    $$\lim_{H(x,y) \to 0} H(x, y) = 0$$
    O penúltimo termo dentro dos colchetes, sendo um termo quadrático negativo dividido por $H(x,y)^2$, diverge para $-\infty$:
    $$\lim_{H(x,y) \to 0} \left( - \frac{\left[ \beta \sinh(\beta x) - k_x \sin(k_x x) \right]^2}{4 H(x, y)^2} \right) = -\infty$$
    Multiplicado pelo coeficiente global $-\frac{\hbar^2}{2m}$, a energia potencial diverge positivamente:
    $$\lim_{H(x,y) \to 0} \mathcal{V}_{\text{Bohm}}(x, y) = +\infty$$

Essa formulação matemática descreve variações no potencial quântico que atuam no direcionamento da singularidade, conduzindo o nó de torção (a partícula) para as regiões de mínimos locais de energia (franjas construtivas) e afastando-o das regiões nodais ($H = 0$).

---

## 37.5 Limite de Correspondência: Redução à Mecânica Quântica Convencional

Para analisar a consistência do formalismo da GDQ frente à formulação tradicional, apresenta-se a seguir o limite onde a solução geometrodinâmica se reduz à formulação padrão da Mecânica Quântica (MQ) de Schrödinger e às trajetórias de De Broglie-Bohm em espaço plano.

### 37.5.1 O Campo de Fase $S_R(x, y)$

A fase real do campo total é obtida tomando-se a fase da superposição $\psi_{\text{total}} = A_1 e^{i \phi_1} + A_2 e^{i \phi_2}$:

$$S_R(x, y) = \hbar (k_0 y - \omega_0 t) - \frac{\hbar}{2}\arctan\left(\frac{y}{y_R}\right) + \frac{m v_0 y (x^2 + d^2/4)}{2(y^2 + y_R^2)} - \hbar \arctan\left[ \tanh\left( \frac{x d}{4\sigma_t^2} \right) \tan\left( \frac{y d x}{4\sigma_t^2 y_R} \right) \right]$$

Esta função de fase governa o campo de velocidades balísticas da partícula por meio do gradiente espacial.

### 37.5.2 O Limite de Campo Distante (Fraunhofer)

Consideramos o limite físico onde o anteparo é posicionado muito além da zona de espalhamento proximal das fendas, isto é, na região de campo distante ($y \gg y_R$).

Nesse limite, a dispersão espacial simplifica-se assintoticamente para:

$$\sigma_t^2 = \sigma_0^2 \left(1 + \frac{y^2}{y_R^2}\right) \approx \sigma_0^2 \frac{y^2}{y_R^2} = \frac{\hbar^2 y^2}{m^2 v_0^2 \sigma_0^2}$$

Substituindo esta aproximação nas parcelas da densidade $\rho_{\text{total}}(x, y)$:

1.  **O envelope hiperbólico:** Próximo ao eixo óptico (região central de interferência onde $x \ll y$), o termo de $\cosh$ aproxima-se da unidade:
    $$\frac{x d}{2\sigma_t^2} \approx \frac{x d m^2 v_0^2 \sigma_0^2}{2 \hbar^2 y^2} \ll 1 \implies \cosh\left(\frac{x d}{2\sigma_t^2}\right) \approx 1$$
2.  **O termo oscilatório de fase:** Substituindo a definição de $y_R$ na fase do cosseno:
    $$\frac{y d x}{2\sigma_t^2 y_R} \approx \frac{y d x}{2 \left( \sigma_0^2 \frac{y^2}{y_R^2} \right) y_R} = \frac{d x y_R}{2 \sigma_0^2 y} = \frac{m v_0 d x}{2 \hbar y}$$
    
    Utilizando a relação fundamental de de Broglie para o comprimento de onda associado à partícula, $\lambda = \frac{h}{p} = \frac{2\pi \hbar}{m v_0}$, o argumento do cosseno torna-se:
    $$\frac{m v_0 d x}{2 \hbar y} = \frac{\pi d x}{\lambda y}$$

Substituindo de volta na densidade de probabilidade total $\rho_{\text{total}}(x, y)$:

$$\rho_{\text{total}}(x, y) \propto \exp\left[ -\frac{x^2}{2\sigma_t^2} \right] \left[ 1 + \cos\left( \frac{2\pi d x}{2 \lambda y} \right) \right] = 2 \exp\left[ -\frac{x^2}{2\sigma_t^2} \right] \cos^2\left( \frac{\pi d x}{2 \lambda y} \right)$$

Obtém-se, assim, a expressão convencional para a interferência de dupla fenda de Young, onde o perfil oscilatório $\cos^2$ é modulado pelo envelope difrativo Gaussiano decorrente da largura finita das fendas.

### 37.5.3 Recuperação das Trajetórias Bohmianas Clássicas

No limite em que desprezamos a [[9 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|torção de Cartan]] e consideramos uma métrica espacial perfeitamente plana ($g_{\mu\bar{\nu}} \to \delta_{\mu\bar{\nu}}$), o acoplamento gravitacional-geométrico é desativado. O fluxo elástico $f$ reduz-se à função de onda de Schrödinger standard por meio de $\psi = e^{-f/2}$.

Nesse limite, a equação de movimento para o centro de massa do sóliton reduz-se à clássica **Equação de Guiagem de de Broglie-Bohm**:

$$\mathbf{v}(x, y) = \frac{1}{m} \nabla S_R(x, y)$$

Substituindo a expressão analítica do gradiente de $S_R(x, y)$ em relação a $x$:

$$v_x(x, y) = \frac{v_0 y x}{y^2 + y_R^2} - \frac{\hbar}{m} \frac{\partial}{\partial x} \arctan\left[ \tanh\left( \frac{x d}{4\sigma_t^2} \right) \tan\left( \frac{y d x}{4\sigma_t^2 y_R} \right) \right]$$

Esta velocidade transversal reproduz as trajetórias bohmianas parabólicas que divergem suavemente a partir das fendas, dobrando-se ao redor dos planos nodais de interferência destrutiva para se agruparem nas zonas de franja brilhante, estabelecendo o princípio de correspondência da GDQ.

### 37.5.4 Verificação Numérica e Visualização da Convergência

Para visualizar a transição entre o regime geometrodinâmico exato e o limite convencional, o script Python `plot_dupla_fenda.py` calcula e compara as duas densidades em duas regiões distintas (campo próximo e campo distante):

```python
# Parâmetros Físicos (unidades normalizadas)
m = 1.0       # Massa da partícula
v0 = 10.0     # Velocidade longitudinal
hbar = 1.0    # Constante de Planck reduzida
d = 1.5       # Distância entre as fendas
sigma_0 = 0.25 # Largura inicial das fendas

# Comprimento de de Broglie
lambd = (2 * np.pi * hbar) / (m * v0)

# Comprimento de Rayleigh do vácuo
y_R = (2.0 * m * v0 * sigma_0**2) / hbar
```

Ao executar o script, os resultados são salvos em `figs/dupla_fenda_comparacao.png`:
-   No **Campo Próximo** ($y = 2.0\,y_R$), a curva azul da GDQ mostra uma modulação de envelope e assimetrias sutis induzidas pelo termo de fase completo e pelo fator de pressão elástica $\cosh$, afastando-se da aproximação simplificada de Fraunhofer (curva vermelha tracejada).
-   No **Campo Distante** ($y = 15.0\,y_R$), a solução da GDQ aproxima-se da curva de probabilidade da mecânica quântica convencional, ilustrando numericamente o princípio de correspondência.

---

*(Nota: A discussão detalhada sobre a [[3 - Causalidade Complexa e o Fim do Paradoxo de Wick|retrocausalidade]] aparente, o Experimento da Escolha Retardada de Wheeler e a atuação do Propagador Simétrico de [[3 - Causalidade Complexa e o Fim do Paradoxo de Wick|Sudarshan]] no colapso do padrão de interferência encontra-se formalizada no **Apêndice 9** desta obra.)*

---

## 37.6 Acoplamento com o Substrato Detector e a Decoerência Geométrica

### 37.6.1 A Modificação da Densidade Total do Sistema

Quando o fluido real de Madelung ($\rho = R^2$) interage com a região ocupada pelo substrato detector, a densidade de probabilidade estatística do vácuo sofre uma penalização proporcional à densidade de aprisionamento ou blindagem quântica do material:

$$\rho_{\text{total}}(x, y) = \rho_{\text{fluido}}(x, y) \cdot e^{-\sigma_{\text{det}} \rho_{\text{det}} L}$$

Onde:
-   $\rho_{\text{det}}$ é a **densidade de nós topológicos por unidade de volume** do substrato detector (ex: densidade eletrônica ou atômica do material).
-   $\sigma_{\text{det}}$ é a seção de choque geométrica de acoplamento da malha elástica com o detector.
-   $L$ é a profundidade de penetração do sinal no substrato.

### 37.6.2 O Impacto Analítico na Pressão Geométrica

Se o detector estiver posicionado logo após as fendas para medir por qual abertura a partícula passou, a amplitude local de densidade $R_{\text{total}} = \sqrt{\rho_{\text{total}}}$ decai exponencialmente devido à impedância do meio:

$$R_{\text{total}}(x, y) = \mathcal{A}(y) |\cos(k_x x)| \cdot e^{-\frac{1}{2} \sigma_{\text{det}} \rho_{\text{det}} y}$$

Ao recalcular-se a pressão geométrica ($\mathcal{V}_{\text{Bohm}} = -\frac{\hbar^2}{2m} \frac{\nabla^2 R_{\text{total}}}{R_{\text{total}}}$) introduzindo a derivada parcial em relação a $y$ (direção do escoamento no detector), o termo de densidade do substrato gera um termo de pressão dissipativo:

$$\frac{\partial R_{\text{total}}}{\partial y} = \left[ \frac{\partial \mathcal{A}}{\partial y} |\cos(k_x x)| - \frac{1}{2}\sigma_{\text{det}}\rho_{\text{det}} \mathcal{A}|\cos(k_x x)| \right] e^{-\frac{1}{2}\sigma_{\text{det}}\rho_{\text{det}}y}$$

Este acoplamento introduz uma componente complexa na ação (uma contribuição dissipativa) que atua diretamente nas frentes de pressão.

### 37.6.3 Destruição do Padrão: O Limite de Alta Densidade ($\rho_{\text{det}} \to \infty$)

No limite em que a densidade do substrato detector é suficientemente alta para realizar uma medição localizável, a impedância métrica domina sobre a rigidez elástica do vácuo.

A força de reação retrocausal do propagador avançado de Sudarshan ($G_{\text{adv}}$) injeta as restrições de contorno de $\rho_{\text{det}}$ diretamente no plano das fendas. O balanço de fases é cancelado assintoticamente pelo ruído térmico e geométrico do substrato, o que transforma a distribuição transversal coerente:

$$\rho_{\text{total}}(x, y) \approx \rho_1(x,y) + \rho_2(x,y)$$

A densidade do substrato detector $\rho_{\text{det}}$ atua como um parâmetro de descoordenação elástica (decoerência geométrica). Quanto maior for $\rho_{\text{det}}$, maior é a dispersão local da fase mecânica $S_R$ e mais rápido os trilhos de contra-pressão do potencial de Bohm se desfazem, conduzindo a partícula a comportar-se como um projétil clássico.

### 37.6.4 Interpretação Física e Ontológica da Decoerência em GDQ

No âmbito da interpretação física da GDQ, a destruição das franjas de interferência pelo detector oferece leituras sobre a mecânica quântica:

1.  **A Dinâmica de Redução:** No formalismo da GDQ, a dinâmica associada à redução do pacote de onda é descrita como um processo de atenuação e cisalhamento mecânico local decorrente da interação com o meio material do detector (representado por $\rho_{\text{det}}$). Essa interação dispersa a fase local $S_R$, modificando as barreiras de potencial quântico.
2.  **A Resolução da Escolha Retardada de Wheeler:** O circuito retrocausal síncrono proporcionado pelo propagador simétrico de Sudarshan ($G_{\text{sym}}$) assegura que o sistema resolva a equação de Hamilton-Jacobi Modificada considerando simultaneamente as condições de contorno de entrada e saída. Nessa abordagem, a presença do detector constitui um vínculo de contorno estacionário que afeta a geometria global das trajetórias admissíveis a partir do início do fluxo de Madelung.

---

## 37.7 Conclusão Ontológica

Desse modo, o experimento da fenda dupla é descrito sob uma perspectiva realista. A dualidade onda-partícula é interpretada em termos geométricos, onde a onda corresponde à repartição do fluxo contínuo pelas fendas e a partícula é representada pelo nó de torção localizado, cujo movimento é condicionado pelas frentes de potencial quântico do espaço-tempo.

