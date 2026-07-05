# Capítulo 19 - O Efeito Zeeman e Acoplamento de Torção

Na mecânica quântica convencional, o Efeito Zeeman (desdobramento dos níveis de energia de um sistema atômico sob a ação de um campo magnético externo) é introduzido de forma operacional e fenomenológica. Insere-se um termo de acoplamento magnético $- \boldsymbol{\mu} \cdot \mathbf{B}$ no Hamiltoniano de Schrödinger ou Dirac, recorrendo-se ao fator giromagnético $g$ e ao magneton de Bohr $\mu_B$ como parâmetros empíricos ou derivados de correções perturbativas da Eletrodinâmica Quântica (QED).

No formalismo da GDQ, o Efeito Zeeman emerge diretamente de primeiros princípios geométricos e topológicos. Ele é a manifestação física de uma **ressonância topológica** entre a vorticidade intrínseca do [[2 - A Geometrização da Matéria|solíton eletrônico]] (codificada pelo seu [[9 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|tensor de torção de Cartan]] próprio) e a curvatura simplética do vácuo induzida pelo campo magnético externo sobre a variedade complexa de Kähler.

Abaixo, desenvolvemos a dedução detalhada, passo a passo, livre de simplificações heurísticas, estendendo a análise ao acoplamento elétrico (Efeito Stark).

---

## 19.1 A Natureza Geométrica do Efeito Zeeman e o Acoplamento de Chern

No formalismo da GDQ, o Efeito Zeeman corresponde à **quebra da degenerescência de energia de um solíton eletrônico** através da interação direta entre seu **Tensor de Torção intrínseco ($T_{\text{elétron}}$)** e a **Conexão de Torção do vácuo ($T_{\text{ext}}$)** gerada pelo campo magnético externo ($\mathbf{B}$).

Quando um elétron ([[8 - Singularidade do Buraco Negro|solíton de Ricci]] com vorticidade $B_{ij}$) é imerso em um campo magnético, o acoplamento atua deformando e **torcendo a métrica local**. A conexão de Chern local $\theta_\alpha = -\frac{i}{\hbar} \partial_\alpha K$ (onde $K$ é o potencial de Kähler, associado à [[29 -  A constante de estrutura fina|métrica de Kähler]] local) sofre um deslocamento de calibre covariante na presença do potencial vetor eletromagnético $A_\mu$:
$$\tilde{\theta}_\alpha = \theta_\alpha - \frac{ie}{\hbar c} A_\alpha = -\frac{i}{\hbar} \left( \partial_\alpha K + \frac{e}{c} A_\alpha \right)$$
$$\tilde{\theta}_{\bar{\beta}} = \theta_{\bar{\beta}} - \frac{ie}{\hbar c} A_{\bar{\beta}} = \frac{i}{\hbar} \left( \bar{\partial}_{\bar{\beta}} K - \frac{e}{c} A_{\bar{\beta}} \right)$$

A curvatura simplética da variedade (a 2-forma de Kähler modificada $\tilde{\omega}$) é a derivada exterior da conexão acoplada:
$$\tilde{R}_{\alpha\bar{\beta}} = \bar{\partial}_{\bar{\beta}} \tilde{\theta}_\alpha = -\frac{i}{\hbar} \left( \frac{\partial^2 K}{\partial z^\alpha \partial \bar{z}^\beta} + \frac{e}{c} \left( \partial_\alpha A_{\bar{\beta}} - \bar{\partial}_{\bar{\beta}} A_\alpha \right) \right)$$

Identificando a métrica nativa de Kähler $g_{\alpha\bar{\beta}} = \partial_\alpha \bar{\partial}_{\bar{\beta}} K$ e a 2-forma de intensidade de campo de Maxwell $F_{\alpha\bar{\beta}} = \partial_\alpha A_{\bar{\beta}} - \bar{\partial}_{\bar{\beta}} A_\alpha$, obtemos:
$$\tilde{R}_{\alpha\bar{\beta}} = -\frac{i}{\hbar} \left( g_{\alpha\bar{\beta}} + \frac{e}{c} F_{\alpha\bar{\beta}} \right) \implies i\hbar \tilde{R}_{\alpha\bar{\beta}} = g_{\alpha\bar{\beta}} + \frac{e}{c} F_{\alpha\bar{\beta}}$$

Sob a dinâmica do escoamento geométrico, a curvatura de Ricci da conexão de Chern $\tilde{R}_{\alpha\bar{\beta}}$ governa o fluxo de Ricci-Perelman. A presença de um campo magnético externo uniforme altera o tensor de Ricci local, injetando uma componente eletromagnética no fluxo de deformação métrica:
$$R_{\alpha\bar{\beta}} = -\partial_\alpha \partial_{\bar{\beta}} \ln \det g + \frac{e}{\hbar c} F_{\alpha\bar{\beta}}$$

Esta equação de acoplamento de Einstein-Maxwell-Kähler demonstra que o campo magnético externo deforma intrinsecamente a geometria métrica do vácuo superfluido. A energia total do sistema torna-se dependente da orientação relativa entre a torção do solíton e a torção do campo externo.

---

## 19.2 Equivalência Matemática dos Acoplamentos de 1-Forma e 2-Forma

No manuscrito, o acoplamento magnético é expresso em duas representações: o acoplamento local da 1-forma de potencial (representação hidrodinâmica de corrente) e a contração tensorial da 2-forma (representação de spin-torção). Demonstra-se a seguir a equivalência exata entre essas duas representações através de integração por partes na variedade de Kähler.

A densidade de corrente de transporte de Madelung do fluido quântico é dada por $j^\mu = \rho v^\mu$, onde $\rho$ é a [[13 - Regra de Born|densidade de Madelung]] $\rho = R_M^2$ (representando a densidade de Perelman $\rho = e^{-f}$) e $v^\mu$ é a velocidade de corrente. O acoplamento minimal na densidade de Lagrangiana clássica é:
$$\mathcal{L}_{\text{int}}^{(1)} = \frac{e}{c} A_\mu j^\mu$$

No formalismo de Cartan, o solíton eletrônico possui uma vorticidade intrínseca que atua como uma fonte localizada de spin-torção. Introduzimos o **Tensor de Spin-Torção do Solíton** $\mathcal{T}^{\alpha\mu}$ (antissimétrico de posto 2). Em termos hidrodinâmicos, a corrente eletromagnética ligada ou de condução interna do solíton é gerada pela divergência espacial dessa densidade de torção intrínseca:
$$j^\mu = \nabla_\alpha \mathcal{T}^{\alpha\mu} = \frac{1}{\sqrt{-g}} \partial_\alpha \left( \sqrt{-g} \mathcal{T}^{\alpha\mu} \right)$$

Substituindo esta identidade de fonte na ação de interação $S_{\text{int}}$:
$$S_{\text{int}} = \int_{\mathcal{M}} \mathcal{L}_{\text{int}}^{(1)} \sqrt{-g} \, d^4x = \frac{e}{c} \int_{\mathcal{M}} A_\mu \left[ \frac{1}{\sqrt{-g}} \partial_\alpha \left( \sqrt{-g} \mathcal{T}^{\alpha\mu} \right) \right] \sqrt{-g} \, d^4x$$
$$S_{\text{int}} = \frac{e}{c} \int_{\mathcal{M}} A_\mu \partial_\alpha \left( \sqrt{-g} \mathcal{T}^{\alpha\mu} \right) d^4x$$

Aplicando a integração por partes sob a condição de que o campo do solíton decai assintoticamente de forma rápida no infinito (termo de fronteira nulo):
$$S_{\text{int}} = -\frac{e}{c} \int_{\mathcal{M}} \left( \partial_\alpha A_\mu \right) \mathcal{T}^{\alpha\mu} \sqrt{-g} \, d^4x$$

Explorando a antissimetria intrínseca de $\mathcal{T}^{\alpha\mu}$ ($\mathcal{T}^{\alpha\mu} = -\mathcal{T}^{\mu\alpha}$), podemos reescrever o integrando de forma antissimetrizada:
$$\left( \partial_\alpha A_\mu \right) \mathcal{T}^{\alpha\mu} = \frac{1}{2} \left( \partial_\alpha A_\mu - \partial_\mu A_\alpha \right) \mathcal{T}^{\alpha\mu} = -\frac{1}{2} F_{\alpha\mu} \mathcal{T}^{\alpha\mu}$$

Onde $F_{\alpha\mu} = \partial_\alpha A_\mu - \partial_\mu A_\alpha$ é o tensor de Maxwell. Substituindo na ação:
$$S_{\text{int}} = \frac{e}{2c} \int_{\mathcal{M}} \mathcal{T}^{\alpha\mu} F_{\alpha\mu} \sqrt{-g} \, d^4x$$

Definindo o tensor de curvatura do campo externo na escala do solíton como $\mathcal{F}_{\alpha\mu} = \frac{e}{c} F_{\alpha\mu}$, a densidade de Lagrangiana de interação tensorial de posto 2 é exata:
$$\mathcal{L}_{\text{int}}^{(2)} = \frac{1}{2} \mathcal{T}^{\alpha\mu} \mathcal{F}_{\alpha\mu}$$

Este desenvolvimento unifica a dinâmica de correntes locais de Madelung com a descrição do acoplamento macroscópico de spin-torção.

---

## 19.3 Análise Dimensional do Tensor de Cartan-Bismut e Projeção Espacial

Para evitar imprecisões no manuscrito, é necessário clarificar o rank do tensor de torção física. Na geometria diferencial de Cartan, o tensor de torção possui rank 3, definido localmente por:
$$T^\lambda_{\mu\nu} = \Gamma^\lambda_{\mu\nu} - \Gamma^\lambda_{\nu\mu}$$

Na presença de conexões com torção totalmente antissimétrica (como a conexão de Bismut, adotada no acoplamento de Kähler com fase física), abaixamos o índice superior com a métrica para obter o tensor totalmente antissimétrico de rank 3:
$$T_{\mu\nu\lambda} = g_{\lambda\sigma} T^\sigma_{\mu\nu}$$
Onde $T_{\mu\nu\lambda} = T_{[\mu\nu\lambda]}$. Em 4 dimensões (espaço-tempo $\mathcal{M}$), uma 3-forma totalmente antissimétrica é dual de Hodge a uma 1-forma (um vetor ou axial-vetor de densidade de spin $S^\mu$):
$$S^\mu = \frac{1}{3!} \epsilon^{\mu\nu\lambda\sigma} T_{\nu\lambda\sigma}$$

Em 3 dimensões espaciais (variedade espacial $\Sigma$), contudo, a contração da 3-forma com a velocidade de escoamento quadridimensional do solíton projeta a torção espacial sobre um tensor antissimétrico de rank 2, a **vorticidade espacial de Cartan** $\mathcal{T}^{\mu\nu}$:
$$\mathcal{T}^{\mu\nu} = u_\lambda T^{\mu\nu\lambda} \implies \mathcal{T}^{ij} = \epsilon^{ijk} S_k$$
Onde $S_k$ é a componente de rotação do spin físico tridimensional.

Assim, a contração $\mathcal{T}^{\mu\nu}\mathcal{F}_{\mu\nu}$ no Hamiltoniano espacial de Zeeman corresponde à representação tridimensional da contração quadridimensional invariante $T^{\mu\nu\lambda} u_\lambda F_{\mu\nu}$.

---

## 19.4 A Emergência Topológica de $g=2$ e o Fator Geométrico de Schwinger

A razão giromagnética clássica para uma distribuição homogênea de carga e massa é $g=1$. A emergência do fator $g=2$ para o elétron sem recorrer à equação de Dirac é uma consequência direta da topologia e da quantização geométrica da GDQ.

O elétron é modelado como um solíton de spin-1/2 cujas órbitas de escoamento interno de corrente estão travadas sobre a topologia de uma **fibração de Hopf** (toro de gênero 1, $T^2$). 
1. **Fator Base ($g=2$):** Devido à quantização de fluxo de Kähler sobre a estrutura espinorial de duplo recobrimento, o fluido de carga elétrica realiza duas rotações completas ao longo do ciclo simplético toroidal para cada rotação completa do momento de massa hidrodinâmico ao longo da geodésica Riemanniana:
   $$\frac{\text{Período de Massa}}{\text{Período de Carga}} = 2 \implies g_{\text{base}} = 2$$
2. **Correção Anômala Conforme ($\alpha_{\text{GDQ}}$):** Sob o fluxo de Ricci-Perelman, a métrica não permanece rígida; a anomalia conforme do [[12 -  O Tempo de Tunelamento Quântico (Efeito Hartman)|vácuo de Kähler]] superfluido introduz flutuações de 1 loop no fator de escala conformal Weyl da métrica. A contração do tensor de curvatura de Chern sob essas flutuações conformes gera a correção de Schwinger de primeiros princípios:
   $$g_{\text{geom}} = 2(1 + \alpha_{\text{GDQ}})$$
   Onde $\alpha_{\text{GDQ}} = \frac{\alpha}{2\pi} \approx 0,0011614$ é dita pela constante de estrutura fina do vácuo de Kähler, $\alpha = \frac{e^2}{\hbar c}$.

O tensor de spin-torção final $\mathcal{T}^{\mu\nu}$ relaciona-se diretamente com o tensor de momento angular intrínseco $S^{\mu\nu}$ via:
$$\mathcal{T}^{\mu\nu} = g_{\text{geom}} \left( \frac{e}{2m} \right) S^{\mu\nu}$$

Onde o **Magneton de Bohr** surge como o quantum elementar de fluxo simplético de fase:
$$\mu_B = \frac{e\hbar}{2m}$$

---

## 19.5 A Dedução da Energia de Acoplamento e Hamiltoniano de Zeeman

O Hamiltoniano de interação $H_{\text{int}}$ é a integral de densidade da Lagrangiana de interação sobre o volume do solíton ($V_s$):
$$H_{\text{int}} = -\int_{V_s} \mathcal{L}_{\text{int}}^{(2)} \sqrt{-g} \, d^3x = -\frac{1}{2} \int_{V_s} \mathcal{T}^{\alpha\beta} \mathcal{F}_{\alpha\beta} \, d^3x$$

Como o campo magnético externo $\mathbf{B}$ é uniforme na escala do elétron, tratamos $\mathcal{F}_{\alpha\beta}$ como constante. O termo $\int_{V_s} \mathcal{T}^{\alpha\beta} d^3x$ é, por definição, o **Momento Magnético Geométrico** do solíton, que chamamos de $\mathbf{M}^{\alpha\beta}$:
$$\mathbf{M}^{\alpha\beta} = \int_{V_s} \mathcal{T}^{\alpha\beta} \sqrt{-g} \, d^3x$$

Portanto, o Hamiltoniano de interação reduz-se a:
$$H_{\text{Zeeman}} = -\frac{1}{2} \mathbf{M}^{\alpha\beta} \mathcal{F}_{\alpha\beta}$$

Substituindo a definição topológica de $\mathcal{T}^{\mu\nu}$:
$$H_{\text{Zeeman}} = - \frac{1}{2} \left[ g_{\text{geom}} \left( \frac{e}{2m} \right) S^{\alpha\beta} \right] \mathcal{F}_{\alpha\beta}$$

---

## 19.6 Contração Tensorial Espacial e Autovalores (Resolução Explícita)

Definido o tensor de campo magnético uniforme $\mathbf{B} = (0, 0, B_z)$ ao longo do eixo $z$, a curvatura simplética externa $\mathcal{F}_{\mu\nu}$ espacial possui as seguintes componentes espaciais não nulas na base $(1,2,3)$:
$$\mathcal{F}_{ij} = \begin{pmatrix} 0 & B_z & 0 \\ -B_z & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

Resolvemos a contração explicitamente sobre os índices espaciais $i, j \in \{1, 2, 3\}$. Como $\mathcal{F}_{ij}$ só tem componentes não nulas em $\mathcal{F}_{12}$ e $\mathcal{F}_{21}$:
$$S^{\alpha\beta} \mathcal{F}_{\alpha\beta} = S^{12}\mathcal{F}_{12} + S^{21}\mathcal{F}_{21}$$

Sabendo que as matrizes são antissimétricas ($S^{21} = -S^{12}$ e $\mathcal{F}_{21} = -\mathcal{F}_{12}$):
$$S^{\alpha\beta} \mathcal{F}_{\alpha\beta} = S^{12}(B_z) + (-S^{12})(-B_z) = 2 S^{12} B_z$$

Por definição da dualidade de Hodge em 3D, a componente $S^{12}$ do tensor de momento angular é exatamente a componente $z$ do vetor de spin: $S^{12} \equiv S_z$.

Substituindo este resultado de volta na equação do Hamiltoniano:
$$H_{\text{Zeeman}} = - \frac{1}{2} \left[ g_{\text{geom}} \left( \frac{e}{2m} \right) \right] (2 S_z B_z) = - g_{\text{geom}} \left( \frac{e}{2m} \right) S_z B_z$$

Na [[3 - Causalidade Complexa e o Fim do Paradoxo de Wick|métrica de Kähler-Sudarshan]], a circulação do fluido quântico no interior do solíton é quantizada para manter a estabilidade do fluxo de Perelman. O momento angular não pode dissipar-se continuamente; ele obedece à quantização da ação de contorno fechado:
$$S_z = \pm \frac{\hbar}{2}$$

Substituindo os autovalores de quantização, obtemos as energias exatas dos níveis perturbados:

Para o estado de torção alinhada ($+$):
$$\Delta E_+ = - g_{\text{geom}} \left( \frac{e\hbar}{4m} \right) B_z = - \frac{1}{2} g_{\text{geom}} \mu_B B_z$$

Para o estado de torção anti-alinhada ($-$):
$$\Delta E_- = + g_{\text{geom}} \left( \frac{e\hbar}{4m} \right) B_z = + \frac{1}{2} g_{\text{geom}} \mu_B B_z$$

### A Matriz de Perturbação Espinorial e Cálculo de Autovalores

Se representarmos o estado interno do solíton numa base de espinores bidimensionais, a matriz Hamiltoniana completa $\mathcal{H}$ do sistema imerso no campo magnético será escrita de forma explícita e rigorosa como:
$$\mathcal{H} = E_0 \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - \frac{1}{2} g_{\text{geom}} \mu_B B_z \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

Para determinar os níveis de energia do sistema, resolvemos a equação característica $\det(\mathcal{H} - E \mathbb{I}) = 0$:
$$\det \begin{pmatrix} E_0 - \frac{1}{2}g_{\text{geom}}\mu_B B_z - E & 0 \\ 0 & E_0 + \frac{1}{2}g_{\text{geom}}\mu_B B_z - E \end{pmatrix} = 0$$
$$\left( E_0 - \frac{1}{2}g_{\text{geom}}\mu_B B_z - E \right) \left( E_0 + \frac{1}{2}g_{\text{geom}}\mu_B B_z - E \right) = 0$$

Cujas raízes fornecem os autovalores exatos de energia do solíton:
$$E_1 = E_0 - \frac{1}{2} g_{\text{geom}} \mu_B B_z$$
$$E_2 = E_0 + \frac{1}{2} g_{\text{geom}} \mu_B B_z$$

O efeito Zeeman normal (ou anômalo, dependendo do multiplicador de acoplamento do sistema isolado) está agora derivado, passo a passo algébrico, provando que a quebra da degenerescência é uma ramificação exata da contração entre o tensor da vorticidade local ($\mathcal{T}$) e o tensor da curvatura imposta ($\mathcal{F}$).

O efeito Zeeman ocorre porque a variedade de Kähler "ajusta" a geometria interna do solíton para minimizar a entropia de Perelman $\mathcal{W}$ sob a influência da torção externa. O shift de energia é a **diferença de energia elástica geométrica** necessária para que o solíton gire sua torção interna para alinhar-se com a torção externa imposta pelo campo.

### O Mecanismo Físico de Estabilização

| **Passo** | **Descrição Física no GDQ** |
|---|---|
| **Campo Externo** | Imposição de uma torção global na variedade de Kähler. |
| **Solíton** | O elétron mantém sua integridade através de sua própria torção de Cartan. |
| **Interação** | Tensão de cisalhamento entre a torção interna e externa. |
| **Zeeman** | Diferença de energia de "alinhamento" (torque geométrico) entre o estoma (elétron) e o fluxo do vácuo. |

Dessa forma, o efeito Zeeman indica que o momento magnético pode ser interpretado como o **momento angular da torção geométrica do vácuo** acoplado à topologia do elétron. O elétron, como um "estoma" no tecido espacial, altera sua energia interna para acomodar o fluxo magnético externo sem colapsar a estrutura da variedade.

---

## 19.7 Dinâmica de Precessão de Larmor via Fluxo de Kähler

A dinâmica temporal da torção $\mathcal{T}^{\mu\nu}$ no plano complexificado é governada pelo colchete de Poisson de Kähler. Para qualquer observável sobre a variedade de Kähler, a evolução segue o campo vetorial hamiltoniano $X_H$:
$$\frac{d\mathcal{T}^{\mu\nu}}{d\tau} = \{\mathcal{T}^{\mu\nu}, H_{\text{Zeeman}}\}$$

Onde o colchete simplético de Kähler entre as componentes do spin é dado por $\{S_i, S_j\} = \epsilon_{ijk} S_k$. Expandindo a equação de movimento para a component vetorial do spin:
$$\frac{d S_i}{d\tau} = \{S_i, - \boldsymbol{\mu} \cdot \mathbf{B}\} = -g_{\text{geom}} \left( \frac{e}{2m} \right) \{S_i, S_j B_j\} = -g_{\text{geom}} \left( \frac{e}{2m} \right) \epsilon_{ijk} S_k B_j$$

Reorganizando os índices sob a forma vetorial clássica, recuperamos a **Equação de Precessão de Larmor** tridimensional:
$$\frac{d\mathbf{S}}{dt} = \boldsymbol{\mu} \times \mathbf{B}$$

A precessão é o resultado direto do escoamento helicoidal do fluido de Kähler quando a torção própria do solíton é submetida ao torque restaurador gerado pela curvatura eletromagnética externa.

---

## 19.8 O Efeito Stark como Polarização Conforme da Métrica

Diferente do campo magnético, um campo elétrico externo uniforme $\mathbf{E} = (0, 0, E_z)$ introduz um potencial eletrostático escalar $\Phi(z) = -E_z z$ (ou $A_0 = -E_z z$).

No formalismo da GDQ, o acoplamento de uma carga elétrica de teste com um potencial externo ocorre de forma direta ao fator conformal $\phi(x)$ da métrica física local $g_{\mu\nu} = e^{2\phi} \bar{g}_{\mu\nu}$. O potencial atua modificando a densidade dilatônica de Perelman $\rho = e^{-f}$, redefinindo o potencial quântico de Bohm:
$$f \to f + \frac{e}{\hbar c} \Phi$$

O Hamiltoniano perturbativo é:
$$H_{\text{Stark}} = -e \mathbf{E} \cdot \mathbf{r}$$

### O Efeito Stark Linear

Para o estado fundamental do solíton eletrônico isolado, a paridade espacial da densidade $\rho_0(r) = e^{-f_0(r)}$ é estritamente simétrica (função par). A integral do momento de dipolo elétrico linear sobre a variedade simétrica é nula:
$$\langle d \rangle = \int_{\mathcal{M}} e \mathbf{r} \rho_0(r) dV = 0$$

Portanto, o Efeito Stark linear é nulo para o solíton eletrônico no estado fundamental, preservando a estabilidade da simetria esférica/toroidal.

### O Efeito Stark Quadrático

Quando o campo elétrico externo $\mathbf{E}$ é aplicado, o gradiente de potencial deforma assimetricamente o fator conformal $\phi$ da métrica local. O escoamento geométrico do solíton sofre um cisalhamento elástico, deslocando a densidade do dilaton $f$ em direção oposta à força do campo. Este deslocamento polariza o solíton de Ricci.

A densidade deformada $\rho(\mathbf{E})$ é resolvida expandindo o funcional de entropia de Perelman $\mathcal{W}$ até segunda ordem na perturbação do campo:
$$\mathcal{W}(g, f, \mathbf{E}) = \mathcal{W}_0 - \frac{1}{2} \alpha_e \mathbf{E}^2$$

Onde $\alpha_e$ é a **polarizabilidade geométrica** do solíton, determinada pela rigidez elástica do escoamento de Perelman contra a deformação de Weyl. O desvio de energia de segunda ordem (Efeito Stark Quadrático) é:
$$\Delta E_{\text{Stark}} = -\frac{1}{2} \alpha_e \mathbf{E}^2$$

O Efeito Stark é, portanto, a expressão do estresse termodinâmico sofrido pela métrica de Kähler, que altera sua energia própria local para acomodar a polarização conformal imposta pela DFE (Distribuição de Força Elétrica) externa.
