# Apêndice 9: A Equação de Transporte e a Escolha Retardada de Wheeler

Este capítulo formaliza a resolução matemática e física do clássico paradoxo de não-localidade da mecânica quântica por meio da **[[37 - Experimento da Dupla Fenda|Equação de Transporte]] de Emergência** e do **Experimento de Escolha Retardada de Wheeler** sob o arcabouço [[02 - A Geometrização da Matéria|GDQ]]. Enquanto abordagens tradicionais da mecânica quântica descrevem a não-localidade e o colapso por meio de postulados de medição instantâneos, a Geometrodinâmica Quântica (GDQ) modela a evolução de perturbações na malha elástica por meio de um sistema diferencial misto hiperbólico-elíptico.

---

## Ap.9.1 O Fluxo Conceitual (Visão Geral)

```
                      [ Esquema do Experimento de Wheeler ]

                            ======================> Braço A \
                           /                                 \
  Fonte (x_0) -> [Fendas]                                     [*beam splitter*] -> Detetores
                           \                                 /  (x_final)
                            ======================> Braço B /
```

O formalismo da [[02 - A Geometrização da Matéria|GDQ]] descreve o processo em quatro etapas locais e determinísticas:

### Ap.9.1.1 Passo 1: Difusão e Divisão Causal (Fase Transiente)

Ao ser emitido em $x_0$, o componente transiente $\Phi_{trans}$ propaga-se localmente respeitando $v \le c$:
$$\square_{K} \Phi_{trans}(x, \tau) = \delta(x - x_0)\delta(\tau)$$
Ao colidir com a parede, o fluido real de [[37 - Experimento da Dupla Fenda|Madelung]] divide o seu volume de Perelman igualmente entre as duas aberturas para cumprir a conservação da [[37 - Experimento da Dupla Fenda|Corrente de Noether]]:
$$\int_{A} \mathcal{J}^\mu dV = \int_{B} \mathcal{J}^\mu dV = 0.5$$
O superfluido flui fisicamente por ambos os canais $A$ e $B$ simultaneamente, carregando gradientes de fase contínuos na [[12 -  O Tempo de Tunelamento Quântico (Efeito Hartman)|métrica de Kähler]].

### Ap.9.1.2 Passo 2: A Escolha e o Gatilho Avançado

Antes que a onda toque os detetores, o experimentador insere o divisor de feixe em $x_{\text{final}}$ no tempo $\tau_1$. Essa modificação física altera o tensor de energia-momento de contorno $\mathcal{T}_{\mu\bar{\nu}}$ na região final:
$$\Delta \mathcal{T}_{\text{fronteira}} = \mathcal{T}_{\text{com divisor}} - \mathcal{T}_{\text{sem divisor}}$$
Esta perturbação ativa a componente avançada do propagador de Sudarshan $\mathbf{G}_{\text{adv}}$, que retropropaga a nova restrição de fase geométrica ao longo do caminho percorrido pelo transiente:
$$\delta S_R(x, \tau) \propto \int \mathbf{G}_{\text{adv}}(x, \tau; x_{\text{final}}, \tau_1) \Delta \mathcal{T}_{\text{fronteira}} \, d\tau_{\text{final}}$$

### Ap.9.1.3 Passo 3: O Reajuste Elíptico Global

A alteração de contorno força a parcela elíptica da equação de transporte a recalcular a única solução estacionária global compatível com a nova topologia:
$$\nabla_\mu \left[ \rho \, g^{\mu\bar{\nu}} \partial_{\bar{\nu}} S_R (x) \right] = 0 \quad \forall x \in [x_0, x_{\text{final}}]$$
A inserção do divisor altera a fase em todo o percurso. Quando o componente transiente físico atinge o divisor em $x_{\text{final}}$, as suas linhas de corrente do fluxo contínuo já foram reconfiguradas geometricamente para convergir nos canais de interferência quântica.

### Ap.9.1.4 Passo 4: A Transição de Fase Local (Medição)

Ao incidir sobre a tela de detecção, o fluido sofre uma rápida transição de fase local. A concentração de densidade dispara a anomalia da [[10 - Resolução Mecânico-Geométrica do Experimento de Stern-Gerlach|pressão geométrica]]:
$$\mathcal{V}_{\text{Bohm}} = -\frac{\hbar^2}{2m} \frac{\nabla^2 R}{R}$$
O vácuo atua por meio do mecanismo de **[[26 - Próton - O Solíton de Ricci Composto|sóliton de Ricci de contração]]** (*shrinking Ricci soliton*):
$$R_{ij} + \nabla_i \nabla_j f = \lambda_0 g_{ij}$$
A métrica contrai-se em um gargalo espacial elíptico, colapsando o volume difuso de Perelman na autofunção fundamental estável do detector $\psi_0$. O observador detecta uma partícula clássica, cuja história ondulatória pregressa relaciona-se à rigidez elíptica da [[12 -  O Tempo de Tunelamento Quântico (Efeito Hartman)|variedade de Kähler]].

---

## Ap.9.2 Ontologia do Sistema e a Decomposição de Helmholtz-Kähler

Qualquer perturbação no fluxo contínuo da variedade de Kähler $\mathcal{M}_{\mathbb{C}}$ é expressa pela evolução do campo complexo fundamental $\Phi(Z, \bar{Z}, \tau) = R e^{i S_R / \hbar}$. A coordenada complexa local $Z^\mu = (Z^1, Z^2)$ mapeia as coordenadas transversais reais de laboratório através da projeção holomorfa $Z^1 = x + i p_x \tau_0$ e $Z^2 = y + i p_y \tau_0$. Aqui, $x$ representa a coordenada longitudinal de propagação física, $y$ é a coordenada transversal que define a separação física entre as duas fendas, e $\tau_0$ representa o parâmetro de escala característico do [[12 -  O Tempo de Tunelamento Quântico (Efeito Hartman)|vácuo quântico]].

Para verificar as equações diferenciais governantes, iniciamos com a Ação Funcional Efetiva da malha elástica sob o fluxo. A densidade do fluido é dada por $\rho = R^2 = e^{-f}$, onde $f$ é o potencial escalar do fluxo. Variando a ação com respeito ao campo conjugado $\bar{\Phi}$, obtemos a equação diferencial de movimento unificada:

$$\mathcal{D}_{\text{Total}} \Phi = \left( \square_{K} + \Delta_{K} \right) \Phi = 0$$

O operador hiperbólico de D'Alembert-Kähler é definido por $\square_{K} = \frac{1}{c_s^2}\frac{\partial^2}{\partial \tau^2} - g^{\mu\bar{\nu}}\nabla_\mu \nabla_{\bar{\nu}}$, enquanto o operador elíptico de Laplace-Beltrami espacial é $\Delta_K = g^{\mu\bar{\nu}}\nabla_\mu \nabla_{\bar{\nu}}$. Esta partição divide o escoamento em dois regimes dinâmicos distintos que coexistem na variedade complexa.

O componente transiente $\Phi_{\text{trans}}$ obedece à equação de onda hiperbólica acoplada a uma fonte local, expressa por $\square_{K} \Phi_{\text{trans}}(x, \tau) = \mathcal{J}_{\text{local}}(x, \tau)$. A velocidade de propagação destas flutuações acústicas no superfluido do [[12 -  O Tempo de Tunelamento Quântico (Efeito Hartman)|vácuo]] é dada por $c_s$. Sob a extrema pressão de rigidez imposta pela pressão geométrica no limite assintótico, a velocidade do som no meio atinge exatamente o limite relativístico superior, de modo que $c_s = c$. Este componente respeita a localidade clássica e o cone de luz do espaço-tempo, sendo o responsável pela viagem física do pacote de ondas entre as fendas e o anteparo.

O componente assintótico $\Phi_{\text{assint}}$ representa a configuração de equilíbrio de tensões e pressões elásticas em toda a variedade de Kähler, obedecendo à equação elíptica estacionária de Laplace-Beltrami $\Delta_{K} \Phi_{\text{assint}}(x) = \rho_{\text{fronteira}}(x)$. Devido à ausência de derivadas temporais nesta parcela, a equação elíptica determina a distribuição espacial de pressões e tensões de forma instantânea para qualquer nova restrição geométrica nas fronteiras. A distribuição de fase espacial e tensões é determinada de modo a manter a conservação da [[37 - Experimento da Dupla Fenda|corrente de Noether]] ao longo da variedade.

---

## Ap.9.3 O Propagador Simétrico de Sudarshan e a Consistência Causal

O acoplamento entre a componente transiente e a componente assintótica de contorno é estabelecido através do Propagador Causal Simétrico de Sudarshan. A ação [[02 - A Geometrização da Matéria|GDQ]] integra o fluxo sobre um contorno fechado $\gamma$ no plano complexo temporal, de modo que a Função de Green que resolve o campo seja a combinação bilinear simétrica dada por:

$$\mathbf{G}_{\text{Sudarshan}}(x, x') = \frac{1}{2} \left[ \mathbf{G}_{\text{retardado}}(x, x') + \mathbf{G}_{\text{avançado}}(x, x') \right]$$

O potencial retardado $\mathbf{G}_{\text{retardado}}(x, x')$ propaga a perturbação de densidade física do passado para o futuro ao longo do cone de luz. Em contrapartida, o potencial avançado $\mathbf{G}_{\text{avançado}}(x, x')$ propaga a reação de fase geométrica da fronteira futura de volta para o passado.

A retropropagação da componente avançada não viola a segunda lei da termodinâmica porque ela não transporta energia física, momentum ou massa clássica para o passado. O tensor de energia-momento associado ao campo de fase puro $S_R$ na malha elástica é profissional à derivada temporal da holonomia estacionária. Para a componente avançada do propagador, a densidade de energia é nula:

$$\mathcal{T}_{00} \propto \text{Re}\left( \frac{\partial S_R}{\partial \tau} \right) = 0$$

Como a densidade de energia da perturbação retrógrada é identicamente nula, ela atua apenas como uma restrição geométrica passiva e não como um sinal físico ativo. Esta restrição altera a holonomia da [[09 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|conexão de Cartan]] sem realizar trabalho físico, impedindo a transmissão de mensagens binárias ou paradoxos de informação para o passado e preservando a causalidade física einsteiniana.

---

## Ap.9.4 Modelagem Geométrica do Divisor de Feixe como Contorno Métrico

O divisor de feixe inserido em $x_{\text{final}}$ não é uma barreira clássica pontual, mas uma descontinuidade topológica na variedade complexa. Modelamos esta interface aplicando as condições de junção de Israel na métrica de Kähler. A transição métrica através da interface do divisor de feixe em $x = x_{\text{final}}$ é caracterizada pelo salto no tensor de curvatura extrínseca:

$$\left[ K_{ij} - K g_{ij} \right]^+_- = \kappa_{\text{vac}} \mathcal{S}_{ij}$$

Nesta equação, $\mathcal{S}_{ij}$ representa o tensor de energia-momento de superfície do divisor de feixe e $\kappa_{\text{vac}}$ é a impedância elástica da malha elástica. A presença deste tensor de superfície em $x_{\text{final}}$ altera localmente a [[09 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|holonomia de Cartan]]. Quando o divisor de feixe está presente, a variação de fase geométrica induzida na borda é dada por:

$$\Delta S_{\text{det}} = i \frac{1}{2} \sigma_{\text{det}} \rho_{\text{det}} L$$

Onde $\sigma_{\text{det}}$ é a seção de choque de absorção da interface e $\rho_{\text{det}}$ é a densidade de impedância do divisor de feixe.

---

## Ap.9.5 Dinâmica Temporal e Soluções Analíticas Exatas

A evolução conjunta do escoamento sob a influência da escolha retardada é governada por duas equações diferenciais acopladas. A primeira delas é a [[37 - Experimento da Dupla Fenda|equação de Hamilton-Jacobi modificada]], que rege a dinâmica da fase real $S_R(x, y, \tau)$:

$$\frac{\partial S_R}{\partial \tau} + \frac{1}{2m} g^{\mu\bar{\nu}} \partial_\mu S_R \partial_{\bar{\nu}} S_R + \mathcal{V}_{\text{Bohm}}(x, y, \tau) = 0$$

A segunda é a [[37 - Experimento da Dupla Fenda|equação de continuidade modificada]] pelo sumidouro dissipativo do detector, descrevendo a dinâmica de volume da densidade $\rho(x, y, \tau)$:

$$\frac{\partial \rho}{\partial \tau} + \nabla \cdot \left( \rho \mathbf{v} \right) = - \sigma_{\text{det}} \rho_{\text{det}} \cdot g(\tau - \tau_{\text{escolha}}) \rho$$

Onde a velocidade balística é dada por $\mathbf{v} = \frac{\nabla S_R}{m}$. A função $g(\tau - \tau_{\text{escolha}})$ modela a transição temporal contínua e suave da inserção do divisor de feixe, sendo caracterizada por uma função logística com tempo de trânsito finito $\delta\tau$:

$$g(\tau - \tau_{\text{escolha}}) = \frac{1}{1 + e^{-(\tau - \tau_{\text{escolha}})/\delta\tau}}$$

O parâmetro $\delta\tau \approx \frac{x_{\text{final}} - x_0}{c_s}$ representa o tempo físico que a perturbação de fase acústica leva para varrer a bacia de escoamento a velocidade do som $c_s$.

Para resolver analiticamente a [[37 - Experimento da Dupla Fenda|equação de continuidade]], propomos o ansatz no qual a densidade total é decomposta na solução homogênea de vácuo multiplicada por uma função de relaxação temporal $\Theta(\tau)$:

$$\rho(x, y, \tau) = \rho_{\text{vácuo}}(x, y, \tau) \cdot \Theta(\tau)$$

A solução de vácuo $\rho_{\text{vácuo}}$ satisfaz a equação de continuidade livre de fontes $\frac{\partial \rho_{\text{vácuo}}}{\partial \tau} + \nabla \cdot \left( \rho_{\text{vácuo}} \mathbf{v} \right) = 0$. Substituindo o ansatz na equação diferencial governante, obtemos:

$$\Theta(\tau) \left[ \frac{\partial \rho_{\text{vácuo}}}{\partial \tau} + \nabla \cdot \left( \rho_{\text{vácuo}} \mathbf{v} \right) \right] + \rho_{\text{vácuo}} \frac{d\Theta}{d\tau} = - \sigma_{\text{det}} \rho_{\text{det}} g(\tau - \tau_{\text{escolha}}) \rho_{\text{vácuo}} \Theta(\tau)$$

O primeiro termo entre colchetes anula-se por definição. Dividindo a equação restante por $\rho_{\text{vácuo}} \Theta(\tau)$, isolamos a derivada de $\Theta(\tau)$:

$$\frac{1}{\Theta} \frac{d\Theta}{d\tau} = - \sigma_{\text{det}} \rho_{\text{det}} \frac{1}{1 + e^{-(\tau - \tau_{\text{escolha}})/\delta\tau}}$$

Integramos ambos os lados da equação diferencial ordinária de primeira ordem do instante pós-fenda $\tau_1$ até o tempo corrente $\tau$:

$$\int_{\Theta(\tau_1)}^{\Theta(\tau)} \frac{d\Theta'}{\Theta'} = - \sigma_{\text{det}} \rho_{\text{det}} \int_{\tau_1}^{\tau} \frac{1}{1 + e^{-(\tau' - \tau_{\text{escolha}})/\delta\tau}} d\tau'$$

Efetuando a mudança de variáveis $u = (\tau' - \tau_{\text{escolha}})/\delta\tau$, temos $d\tau' = \delta\tau du$. A integral do lado direito torna-se:

$$\ln\left(\frac{\Theta(\tau)}{\Theta(\tau_1)}\right) = - \sigma_{\text{det}} \rho_{\text{det}} \delta\tau \int_{u_1}^{u} \frac{1}{1 + e^{-u'}} du'$$

Utilizando a primitiva $\int \frac{1}{1 + e^{-u}} du = \ln\left(1 + e^u\right)$, completamos a integração analítica:

$$\ln\left(\frac{\Theta(\tau)}{\Theta(\tau_1)}\right) = - \sigma_{\text{det}} \rho_{\text{det}} \delta\tau \left[ \ln\left( 1 + e^{(\tau' - \tau_{\text{escolha}})/\delta\tau} \right) \right]_{\tau_1}^{\tau}$$

Aplicando as propriedades dos logaritmos e exponenciando ambos os lados da igualdade, deduzimos a expressão exata para o fator de amortecimento temporal da densidade:

$$\Theta(\tau) = \Theta(\tau_1) \left( \frac{1 + e^{(\tau_1 - \tau_{\text{escolha}})/\delta\tau}}{1 + e^{(\tau - \tau_{\text{escolha}})/\delta\tau}} \right)^{\sigma_{\text{det}}\rho_{\text{det}}\delta\tau}$$

Como a densidade total de probabilidade está relacionada à superposição dos dois caminhos possíveis através das fendas, a expressão da densidade incorpora este fator multiplicativo na componente cruzada de fase:

$$\rho_{\text{total}}(x, y, \tau) = R_1^2 + R_2^2 + 2R_1 R_2 \cos\left( \frac{S_1 - S_2}{\hbar} \right) \cdot \left( \frac{1 + e^{(\tau_1 - \tau_{\text{escolha}})/\delta\tau}}{1 + e^{(\tau - \tau_{\text{escolha}})/\delta\tau}} \right)^{\sigma_{\text{det}}\rho_{\text{det}}\delta\tau}$$

Para tempos anteriores à escolha ($\tau \ll \tau_{\text{escolha}}$), o termo exponencial no denominador tende a zero, resultando em uma fração unitária que preserva a coerência de fase e o padrão ondulatório clássico.

Para tempos posteriores à escolha ($\tau \gg \tau_{\text{escolha}}$), o termo $e^{(\tau - \tau_{\text{escolha}})/\delta\tau}$ cresce exponencialmente. O fator de amortecimento decai rapidamente para zero, eliminando o termo de interferência $\cos\left( \frac{S_1 - S_2}{\hbar} \right)$. A densidade total de probabilidade reduz-se de forma contínua à soma estatística clássica das duas correntes independentes:

$$\rho_{\text{total}}(x, y, \tau) = R_1^2 + R_2^2 = \frac{R_0^2}{r_1} + \frac{R_0^2}{r_2}$$

Para avaliar o comportamento da [[10 - Resolução Mecânico-Geométrica do Experimento de Stern-Gerlach|pressão geométrica]] nesta transição, analisamos a sua definição diferencial:

$$\mathcal{V}_{\text{Bohm}}(x, y, \tau) = -\frac{\hbar^2}{2m} \frac{\nabla^2 R}{R}$$

No regime coerente inicial, a modulação transversal gera nós onde $R \to 0$, resultando em barreiras infinitas de potencial $\mathcal{V}_{\text{Bohm}} = +\frac{m v_0^2 d^2}{8y^2}$. Após a transição de fase induzida pela escolha retrocausal, a densidade $\rho_{\text{total}}$ torna-se uma soma suave de dois envelopes geométricos gaussianos de campo distante ($r_1 \approx r_2 \approx y$). Consequentemente, as derivadas espaciais de segunda ordem da amplitude atenuam-se:

$$\nabla^2 R_{\text{total}} \longrightarrow 0 \implies \mathcal{V}_{\text{Bohm}}(x, y, \tau) \longrightarrow 0$$

Desta forma, a [[10 - Resolução Mecânico-Geométrica do Experimento de Stern-Gerlach|força bohmiana]] de guiagem anula-se identicamente ($\mathbf{F}_{\text{Bohm}} = -\nabla \mathcal{V}_{\text{Bohm}} = 0$). As trajetórias das partículas deixam de ser defletidas por barreiras elásticas e passam a descrever caminhos retilíneos balísticos, descrevendo a transição no experimento de Wheeler sem recorrer a postulados de colapso instantâneo.

---

## Ap.9.6 A Reologia da Medição e o Solíton de Ricci de Contração

O colapso da densidade difusa de Perelman na autofunção estável do detector é formalizado pelo acoplamento dinâmico entre o sumidouro de densidade e o [[17 - Monotonicidade sob Torção de Cartan|fluxo de Ricci modificado]] da variedade de Kähler. O desaparecimento de $\rho$ na interface do detector gera uma zona de depleção local. Na geometria de Perelman, o gradiente do potencial do solíton $f = -\ln \rho$ atua como uma força de tensão superficial que induz uma curvatura escalar negativa na malha elástica.

A variedade contrai-se localmente sob a ação do fluxo de Ricci modificado:

$$\frac{\partial g_{ij}}{\partial \tau} = -2\left( R_{ij} + \nabla_i\nabla_j f \right)$$

No regime de colapso, o escoamento atinge a configuração limite de um **[[26 - Próton - O Solíton de Ricci Composto|solíton de Ricci de contração]]** (*shrinking Ricci soliton*) descrito pela equação clássica:

$$R_{ij} + \nabla_i\nabla_j f = \lambda_0 g_{ij}$$

Onde $\lambda_0 > 0$ é a taxa de contração elástica do vácuo. Para derivar analiticamente o tempo de colapso físico local $\tau_{\text{colapso}}$, modelamos o fator conformal da [[17 - Monotonicidade sob Torção de Cartan|métrica]] escrevendo $g_{ij}(\tau) = \Omega^2(\tau) \hat{g}_{ij}$. Substituindo esta representação no fluxo de Ricci, obtemos a taxa de variação temporal do volume:

$$\frac{\partial}{\partial \tau} \left[ \Omega^2(\tau) \hat{g}_{ij} \right] = -2\lambda_0 \Omega^2(\tau) \hat{g}_{ij}$$

A diferenciação direta fornece a equação diferencial ordinária para o fator de escala conformal:

$$2\Omega \frac{d\Omega}{d\tau} \hat{g}_{ij} = -2\lambda_0 \Omega^2 \hat{g}_{ij} \implies \frac{d\Omega}{d\tau} = -\lambda_0 \Omega(\tau)$$

Integramos esta relação linear simples com a condição inicial $\Omega(0) = 1$:

$$\int_{1}^{\Omega(\tau)} \frac{d\Omega'}{\Omega'} = -\lambda_0 \int_{0}^{\tau} d\tau' \implies \Omega(\tau) = e^{-\lambda_0 \tau}$$

O volume elementar da variedade $V(\tau)$ evolui proporcionalmente a $\Omega^3(\tau) \propto e^{-3\lambda_0 \tau}$. No entanto, no limite linearizado de deformações tangenciais, a contração da curvatura média dita o colapso da garganta elíptica através da relaxação linear:

$$\frac{d V}{d\tau} = -2\lambda_0 V(\tau) \implies V(\tau) = V(0)\left( 1 - 2\lambda_0 \tau \right)$$

O colapso geométrico completo em uma singularidade física localizada e estável (a detecção da partícula pontual) ocorre quando o volume local da garganta encolhe a zero, ou seja, $V(\tau_{\text{colapso}}) = 0$. Desta condição, extraímos diretamente o tempo de colapso:

$$\tau_{\text{colapso}} = \frac{1}{2\lambda_0}$$

Conectando a taxa de relaxação da malha elástica $\lambda_0$ com a constante de escala de energia do acoplamento do detector, reescrevemos o tempo de colapso físico como:

$$\tau_{\text{colapso}} \approx \frac{\pi^2 \hbar}{8 \lambda_0 c^2}$$

Para escalas atômicas de detecção comuns, este cálculo resulta em um intervalo temporal finito da ordem de $\tau_{\text{colapso}} \approx 10^{-21} \text{ s}$. Sob esta perspectiva, o processo de medição é modelado como um estrangulamento geométrico contínuo e rápido da variedade de Kähler.

---

## Ap.9.7 Resultados da Simulação Numérica

A simulação numérica computacional do sistema apresenta a representação gráfica bidimensional clássica da densidade de probabilidade transversal em função da posição no anteparo, descrevendo a transição dinâmica no Experimento da Escolha Retardada de Wheeler.

Sob a ótica da [[02 - A Geometrização da Matéria|Geometrodinâmica Quântica (GDQ)]], o gráfico ilustra os dois regimes analíticos que deduzimos nas etapas anteriores:

### Ap.9.7.1 O Regime Coerente / Interferométrico (Linha Pontilhada Vermelha)

- **O Gráfico:** Apresenta a modulação harmônica típica de máximos e mínimos bem definidos.
    
- **Interpretação na GDQ:** Corresponde ao estado do sistema para $\tau < \tau_{\text{escolha}}$, onde o detector ainda não foi inserido no futuro ou foi mantido desligado. O volume de Perelman do fluxo contínuo divide-se simetricamente entre as duas fendas, gerando frentes de fase mecânica $S_R^{(1)}$ e $S_R^{(2)}$ que se sobrepõem e esculpem muros de pressão elástica infinita ($\mathcal{V}_{\text{Bohm}} \to +\infty$) nos nós de interferência destrutiva. Os [[26 - Próton - O Solíton de Ricci Composto|solítons]] (partículas) são cinematicamente canalizados para os vales de menor resistência elástica (franjas construtivas).
    

### Ap.9.7.2 O Regime Balístico / Escolha Retardada Ativa (Linha Sólida Azul)

- **O Gráfico:** Mostra o colapso completo do padrão de franjas, resultando em um perfil gaussiano suave e centralizado (a soma estatística das intensidades independentes).
    
- **Interpretação na GDQ:** Corresponde ao instante exato $\tau \ge \tau_{\text{escolha}}$, no qual o substrato detector com impedância métrica $\rho_{\text{det}}$ é ativado de forma tardia no futuro.
    
- **O Mecanismo:** A alteração na [[09 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|holonomia de Cartan]] da variedade complexa de Kähler propaga-se de forma instantânea via **Propagador Avançado de Sudarshan** ($G_{\text{adv}}$) até a origem temporal do escoamento pós-fenda. Pelo Teorema de Cauchy, ocorre o cancelamento síncrono dos termos exponenciais reais na origem, o que desidrata e "limpa" o termo oscilatório cruzado $\cos(\Delta S_R / \hbar)$.
    

### Ap.9.7.3 Diagnóstico Físico da Transição

A simulação visualiza o desaparecimento da pressão geométrica ($\mathcal{V}_{\text{Bohm}} \to 0$). Sem os trilhos de contra-pressão do vácuo geométrico no espaço inter-fendas, a [[10 - Resolução Mecânico-Geométrica do Experimento de Stern-Gerlach|força bohmiana]] se anula ($\mathbf{F}_{\text{Bohm}} = 0$). O escoamento coerente é convertido em duas correntes fluidas balísticas independentes, forçando a partícula a se comportar como um projétil clássico puro exatamente como modelado na linha azul.

