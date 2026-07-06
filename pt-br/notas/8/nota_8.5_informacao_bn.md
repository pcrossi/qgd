### Adendo Teórico: 15. O Paradoxo da Perda de Informação em Buracos Negros

O paradoxo da perda de informação só existe na Relatividade Geral clássica e na Teoria Quântica de Campos convencional porque ambas aceitam a premissa de um colapso gravitacional que culmina em uma singularidade real ($r=0$), rasgando o espaço-tempo e amputando as linhas de universo do operador de evolução temporal. Uma vez que a GDQ elimina a singularidade central através do acoplamento harmônico da pressão geométrica $T_{\mu\nu}^{(\text{Bohm})}$, o horizonte de eventos deixa de ser um sumidouro entrópico absoluto e passa a atuar como uma barreira de potencial elástico transiente.

Como o colapso é interrompido no limite ultravioleta de Cartan, o escoamento geométrico do fluxo de Ricci não atinge um ponto de parada singular; em vez disso, ele experimenta uma reversão dinâmica (um efeito de ricochete geométrico ou _bounce_). Como todo o processo é governado por equações diferenciais parciais estritamente elípticas/parabólicas acopladas sobre uma malha compacta, a evolução do sistema preserva o difeomorfismo global e a ciclicidade complexa. A informação nunca é destruída ou termalizada de forma caótica: ela é geometricamente codificada nas deformações de torção e restituída integralmente de forma assintoticamente reversível durante a fase de relaxação do solíton.

### Formalismo Matemático e Teorema de Restituição da Informação

Seja a evolução da métrica do buraco negro regularizado governada pelo sistema de Einstein-Bohm-Perelman. A ausência de uma singularidade em $r=0$ implica que o volume de Perelman $\mathcal{V}_P = \int e^{-f} dV_g$ é conservado de forma global.

1. **A Preservação da Medida Coerente:** O funcional de entropia geométrica de Perelman $\mathcal{W}(g, f, \tau)$ age como uma função de Lyapunov para o sistema. Para qualquer estado de informação quântica mapeado na forma de uma perturbação métrica/torsional $\delta g_{ij}(0)$ na fronteira assintótica, a evolução temporal complexa sob o parâmetro de escala $\tau$ obedece ao teorema de Liouville geométrico. Como o determinante da métrica modificada pelo a pressão geométrica permanece estritamente positivo em toda a extensão do bulk, $\det(g_{ij}) > 0$, o operador de evolução de curto alcance $\mathcal{U}(\tau)$ é um homeomorfismo estrito.
    
2. **O Mecanismo de Ricochete Geométrico (_Bounce_):** No núcleo do solíton ($r \to \delta_{\text{Cartan}}$), a pressão geométrica $P_Q$ diverge positivamente, superando o colapso gravitacional clássico. O tensor de Ricci local $R_{ij}$ inverte seu sinal geométrico devido à contra-pressão da rede elástica de Kähler:
    
    $$\frac{\partial g_{ij}}{\partial \tau} = -2(R_{ij} + \nabla_i \nabla_j f) > 0 \quad \text{para } r \le \delta_{\text{Cartan}}$$
    
    Este esticamento métrico força as geodésicas de calibre que transportam as frentes de onda de fase do fluido de Madelung a sofrerem reflexão total interna. O pescoço geométrico atua como um espelho de holonomia perfeita.
    
3. **Inversão Temporal e Unitaridade Estrita:** Como o propagador simétrico de Sudarshan opera no plano complexo do tempo, as fases avançadas e retardadas mantêm um trancamento síncrono. A matriz de espalhamento global $\mathcal{S}$, que conecta o estado assintótico de entrada ($I_{\text{in}}$) ao estado de evaporação/restituição de saída ($I_{\text{out}}$), é dada pelo mapeamento fechado das classes de cohomologia ao redor da garganta elástica:
    
    $$\mathcal{S}^\dagger \mathcal{S} = \exp\left( \oint_{\partial \mathcal{M}} \omega_{\text{Bismut}} \right) = \mathbf{1}$$
    
    Isso demonstra que a assinatura geométrica fina de cada partícula que entrou no horizonte modificado altera localmente a holonomia da barreira, modulando de volta a emissão do vácuo. O fluxo de saída carrega a matriz de correlação exata do estado inicial, resultando em um ganho líquido de informação perfeitamente unitário ($\Delta S_{\text{vácuo}} \equiv 0$).
