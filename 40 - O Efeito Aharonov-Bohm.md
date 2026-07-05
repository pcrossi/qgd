# Capítulo 40 - O Efeito Aharonov-Bohm e a Ontologia Mecânico-Geométrica dos Potenciais de Calibre

## 40.1 Comparação entre a Formulação Convencional e a Abordagem da GDQ

Na mecânica quântica e na eletrodinâmica clássica, o Efeito Aharonov-Bohm descreve uma situação em que uma partícula carregada, ao se deslocar por uma região com campo magnético nulo ($\mathbf{B} = \nabla \times \mathbf{A} = 0$), experimenta um deslocamento de fase em seu padrão de interferência devido à presença do potencial vetor $\mathbf{A}$ no exterior do solenoide. Na interpretação convencional, esse efeito evidencia a relevância física dos potenciais de calibre no regime quântico.

No âmbito da [[2 - A Geometrização da Matéria|Geometrodinâmica Quântica (GDQ)]], os potenciais de calibre são interpretados como representações de escoamentos e [[8 - Singularidade do Buraco Negro|deformações elásticas]] na malha do vácuo. Sob essa perspectiva, o potencial de calibre $\mathbf{A}$ é relacionado à velocidade de cisalhamento local do fluxo contínuo da rede.

O campo magnético $\mathbf{B}$ descreve a [[9 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|vorticidade]] macroscópica (ou [[9 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|torção antissimétrica métrica]]) concentrada no interior do solenoide. Assim, ao circular o solenoide, o comportamento da partícula é descrito pela interação com o fluxo local, irrotacional porém sob tensão elástica, do vácuo circundante.

---

## 40.2 Formulação Hidrodinâmica-Geométrica do Deslocamento de Fase

A matéria na GDQ é descrita pela representação polar da função de densidade do fluxo, cuja densidade $\rho = R^2$ mapeia o volume invariante e o gradiente da fase $S$ determina a cinemática local. No espaço tridimensional fora do solenoide, a região ocupada pelo fluxo do elétron é multiplamente conexa (topologia de um cilindro perfurado, $M \approx \mathbb{R}^3 \setminus D^2$, onde $D^2$ representa a seção reta do solenoide).

A 1-forma de momentum complexo $\omega$ que dita o escoamento do fluxo contínuo da malha incorpora o acoplamento mínimo como uma distorção métrica primária:

$$\omega = p_\mu dx^\mu = \left( \hbar \partial_\mu S - \frac{e}{c} A_\mu \right) dx^\mu$$

Fora do solenoide, a condição de que o campo de torção macroscópica (eletromagnetismo clássico) se anule impõe que a curvatura da conexão de calibre seja zero, implicando que a 1-forma $A = A_\mu dx^\mu$ é localmente fechada ($dA = 0$). Contudo, devido à topologia não-trivial da variedade ($\pi_1(M) = \mathbb{Z}$), a forma não é exata.

A [[10 - Resolução Mecânico-Geométrica do Experimento de Stern-Gerlach|velocidade do fluxo contínuo]] $\mathbf{u}$ é dada pelo balanço de momento local de primeiros princípios da GDQ:

$$\mathbf{u} = \frac{\hbar}{m} \nabla S - \frac{e}{mc} \mathbf{A}$$

Como o fluido é incompressível e estacionário na região de trânsito estável, a circulação do campo de velocidades ao longo de uma curva fechada $\gamma$ que envolve o solenoide quantifica a memória topológica fixada pelo aprisionamento do fluxo geométrico relaxante.

---

## 40.3 A Integral de Holonomia e o Teorema de Mayer-Vietoris

Ao dividirmos o escoamento do fluxo contínuo pelas duas rotas possíveis ao redor do solenoide (Caminho 1, superior, e Caminho 2, inferior), o espaço de configurações é decomposto via cirurgia topológica de Mayer-Vietoris nos subdomínios abertos $U_1$ e $U_2$, cuja interseção envolve as regiões de fenda e de detecção.

O deslocamento de fase total acumulado $\Delta \phi$ na franja de interferência surge da diferença de ação geométrica entre os dois fluxos de escoamento ao longo da fronteira de colagem:

$$\Delta \phi = \oint_{\gamma} \nabla S \cdot d\mathbf{r} = \int_{\gamma_1} \nabla S \cdot d\mathbf{r} - \int_{\gamma_2} \nabla S \cdot d\mathbf{r}$$

Substituindo a definição da velocidade do fluxo contínuo $\mathbf{u}$, extraímos o acoplamento elástico intrínseco:

$$\Delta \phi = \frac{m}{\hbar} \oint_{\gamma} \mathbf{u} \cdot d\mathbf{r} + \frac{e}{\hbar c} \oint_{\gamma} \mathbf{A} \cdot d\mathbf{r}$$

Na GDQ, a condição de quantização de fase de [[34 - Monopolos e a Fibração de Hopf|Wallstrom-Bohm]] é garantida nativamente pela rigidez holomorfa da malha elástica de fundo, que tranca a circulação mecânica do fluxo elástico puro ($\oint \mathbf{u} \cdot d\mathbf{r} = 0$) fora das regiões de estoma (vorticidade nula na vizinhança). Consequentemente:

$$\Delta \phi = \frac{e}{\hbar c} \oint_{\gamma} \mathbf{A} \cdot d\mathbf{r}$$

Utilizando o Teorema de Stokes generalizado sobre a subvariedade compacta da seção do solenoide $\Sigma$ (onde a borda $\partial\Sigma = \gamma$), a integral do potencial vetor (cisalhamento de vácuo) converte-se identicamente no fluxo da 3-forma de [[9 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|torção de Cartan]] $\mathcal{T}$ (O fluxo magnético encastelado $\Phi$):

$$\oint_{\gamma} \mathbf{A} \cdot d\mathbf{r} = \iint_{\Sigma} (\nabla \times \mathbf{A}) \cdot d\mathbf{\Sigma} = \iint_{\Sigma} \mathbf{B} \cdot d\mathbf{\Sigma} = \Phi$$

Portanto, o deslocamento de fase geométrico é rigidamente travado pelo invariante topológico da barreira:

$$\Delta \phi = \frac{e \Phi}{\hbar c}$$

---

## 40.4 O Mecanismo Local: Cisalhamento e Impedância do Vácuo

A descrição da GDQ para o Efeito Aharonov-Bohm baseia-se em dois aspectos principais:

1.  **A Natureza Reológica de $\mathbf{A}$**: Na GDQ, a fixação de calibre relaciona-se à reologia do vácuo, de modo que $\mathbf{A}$ descreve o arrasto convectivo e a deformação de cisalhamento da [[12 -  O Tempo de Tunelamento Quântico (Efeito Hartman)|métrica de Kähler]] no exterior do solenoide, o qual altera a métrica e a conexão locais.
    
2.  **Evolução pelo [[17 - Monotonicidade sob Torção de Cartan|fluxo de Perelman]]**: Embora o núcleo da singularidade não penetre na região com vorticidade interna do solenoide, o sóliton apresenta uma extensão espacial associada ao fluxo. A evolução do [[17 - Monotonicidade sob Torção de Cartan|funcional de entropia métrica $\mathcal{W}$]] requer a integração sobre a variedade, de forma que a impedância na fronteira do solenoide influi no gradiente do [[10 - Resolução Mecânico-Geométrica do Experimento de Stern-Gerlach|potencial quântico de Bohm]] na região externa.
    

Desse modo, o movimento do elétron é condicionado localmente por uma deformação métrica que reflete a estrutura homológica decorrente da presença do solenoide, oferecendo uma interpretação puramente geométrica para o Efeito Aharonov-Bohm.

