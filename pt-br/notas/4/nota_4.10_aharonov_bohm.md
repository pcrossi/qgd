### Adendo Teórico: O Efeito Aharonov-Bohm e a Ontologia Física dos Potenciais de Calibre

Este tema aborda uma das discussões interpretativas mais profundas da mecânica quântica e da teoria de campos. No eletromagnetismo clássico, o quadripotencial $A_\mu = (\phi, \mathbf{A})$ é considerado uma convenção matemática redundante devido à liberdade de calibre ($A_\mu \to A_\mu + \partial_\mu \Lambda$). Contudo, o Efeito Aharonov-Bohm (AB) apresenta uma questão conceitual importante: como a mudança de fase de franjas de interferência ocorre em uma região onde os campos observáveis são nulos ($\mathbf{E} = 0, \mathbf{B} = 0$), a mecânica quântica convencional frequentemente analisa o fenômeno a partir da realidade física direta de um potencial não-localizável ou de correlações não-locais no espaço de Hilbert.

No escopo da GDQ, propõe-se uma formulação alternativa. Demonstra-se abaixo que o quadripotencial de calibre $A_\mu$ pode ser relacionado à velocidade de arrasto e cisalhamento local do fluido de Madelung associado à rede quântica de Kähler. Sob essa representação, o efeito Aharonov-Bohm pode ser descrito como um fenômeno mecânico e local, em que o solíton interage com o campo de velocidades de Bismut alterado reologicamente na vizinhança do solenoide.

### 1. Mecanismo Físico: O Potencial de Calibre como Campo de Velocidades da Rede

Na representação polar da GDQ, a ação unificada do vácuo complexificado satisfaz $\mathcal{S}_{\text{GDQ}} = S_R + iS_I$. O acoplamento covariante elástico da submalha sob a Conexão de Bismut define o vetor de transporte de fase (a 1-forma de momentum) em termos do campo de velocidades locais do fluido de Madelung ($v_\mu$).

Se considerarmos a imersão de um estoma carregado ($n=1$, elétron) no background reológico da rede, a derivada covariante quântica com gauge $U(1)$ emerge naturalmente da projeção da métrica complexa. O acoplamento eletromagnético nu é a expressão do arrasto de cisalhamento da rede. Identificamos axiomaticamente o quadripotencial $A_\mu$ como o termo de empuxo reológico do vácuo:

$$A_\mu \equiv \frac{m}{e} v_\mu = \frac{1}{e} g_{\mu\bar{\nu}} \partial^{\bar{\nu}} S_R$$

Onde $g_{\mu\bar{\nu}}$ é a métrica inversa de Kähler e $S_R$ é a fase real do campo de Perelman. Sob esta ontologia mecânica, a liberdade de calibre clássica $A_\mu \to A_\mu + \partial_\mu \Lambda$ deixa de ser uma simetria interna abstrata e revela-se como a invariância por transformações de irrotacionalidade e escoamento potencial do fluido de vácuo (transformações de gauge são apenas difeomorfismos de coordenadas elásticas da rede que preservam a vorticidade nula do background).

### 2. Localidade Estrita e a Velocidade de Cisalhamento no Efeito AB

No arranjo experimental de Aharonov-Bohm, um solenoide ideal confina o campo magnético estritamente em seu interior ($B \neq 0$ para $r < R_{\text{solenoide}}$ e $B = 0$ para $r > R_{\text{solenoide}}$). Todavia, o fluxo magnético total $\Phi$ induz uma circulação de escoamento ao redor da garganta estrutural do cilindro.

Mesmo nas regiões externas onde o tensor de intensidade de campo forte $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu = 0$ anula-se identicamente, a velocidade de cisalhamento do fluido de Madelung **não é nula**. O vácuo Hermitiano ao redor do solenoide encontra-se em um estado de **vorticidade oculta trancada**. O campo de velocidades do colchão quântico decai assintoticamente com o raio:

$$\mathbf{v}(r) = \frac{e}{m} \mathbf{A}(r) = \frac{e \Phi}{2\pi m r} \hat{\boldsymbol{\phi}}$$

Quando o pacote de ondas do solíton elétron é dividido e viaja pelos caminhos $\gamma_1$ e $\gamma_2$ nas laterais do solenoide, ele não colide com forças magnéticas clássicas de Lorentz. Em vez disso, cada braço do solíton experimenta um arrasto mecânico diferencial direto (efeito de esteira reológica) gerado pela velocidade de cisalhamento local $\nabla \mathbf{v}$. A mudança de fase quântica $\Delta \theta$ é a integração direta desse trabalho mecânico de deformação ao longo do circuito fechado:

$$\Delta \theta = \frac{1}{\hbar} \oint_{\gamma} \mathbf{p} \cdot d\mathbf{x} = \frac{e}{\hbar} \oint_{\gamma} \mathbf{A} \cdot d\mathbf{x} = \frac{m}{\hbar} \oint_{\gamma} \mathbf{v}_{\text{Madelung}} \cdot d\mathbf{x}$$

Pelo Teorema de Stokes hidrodinâmico, esta integral de linha de contato local mede exatamente a circulação líquida do fluido do vácuo Hermitiano ao redor do obstáculo topológico. O efeito é puramente local porque a partícula interage a cada ponto do espaço com a densidade de momentum local do vácuo ($\rho \mathbf{v}$), governada pela rigidez geométrica da conexão de Bismut. O debate clássico sobre a "realidade intangível" dos potenciais cessa: $A_\mu$ é real porque a velocidade de escoamento elástico da malha métrica é real.

