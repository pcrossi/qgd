# Apêndice 6: Geometrização do Espalhamento de Klein-Nishina

Neste apêndice, detalhamos o formalismo matemático e as equações diferenciais para a dedução da **Seção de Choque de Klein-Nishina** a partir dos primeiros princípios da [[02 - A Geometrização da Matéria|Geometrodinâmica Quântica (GDQ)]], no âmbito da teoria Kähler-Perelman-Sudarshan-Cartan (GDQ).

Diferentemente do tratamento perturbativo convencional da Eletrodinâmica Quântica (QED) baseado em diagramas de Feynman, o espalhamento relativístico no formalismo da [[02 - A Geometrização da Matéria|GDQ]] é modelado a partir da colisão entre uma perturbação da métrica de calibre e um [[17 - Monotonicidade sob Torção de Cartan|sóliton de Ricci encolhedor]] (*shrinking Ricci soliton*, o [[26 - Próton - O Solíton de Ricci Composto|elétron]]) imersos no superfluido do [[12 -  O Tempo de Tunelamento Quântico (Efeito Hartman)|vácuo]].

---

## Ap.6.1 Perturbação da Métrica de Kähler e a EDP Linearizada

O [[26 - Próton - O Solíton de Ricci Composto|elétron]] estacionário em repouso é descrito pelo [[12 -  O Tempo de Tunelamento Quântico (Efeito Hartman)|potencial de Kähler]] $K(z, \bar{z})$ e pelo campo dilatônico de Perelman $f_0$. A [[12 -  O Tempo de Tunelamento Quântico (Efeito Hartman)|métrica de Kähler]] de fundo é $g_{\mu\bar{\nu}}^{(0)} = \partial_\mu \partial_{\bar{\nu}} K$. O fóton incidente e o fóton espalhado são tratados como perturbações dinâmicas de alta frequência na métrica de Kähler:

$$g_{\mu\bar{\nu}}(x, \tau) = g_{\mu\bar{\nu}}^{(0)} + \delta g_{\mu\bar{\nu}}(x, \tau)$$

A perturbação $\delta g_{\mu\bar{\nu}}$ acopla-se à conexão Hermitiana e propaga-se como uma oscilação na curvatura de calibre, parametrizada pelos vetores de polarização transversais (direções de deformação elástica) $\epsilon_\mu$ e $\epsilon'_\mu$:

$$\delta g_{\mu\bar{\nu}} \propto \epsilon_{\mu} \bar{\epsilon}'_{\nu} e^{i k \cdot x} + \text{c.c.}$$

A evolução sob o [[17 - Monotonicidade sob Torção de Cartan|Fluxo de Ricci-Perelman]] modificado para a perturbação do campo dilatônico $\delta f(x)$ sob a presença do campo de [[09 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo|torção antissimétrica de Cartan]]-Perelman ($H_{\mu\alpha\beta}$) obedece à equação diferencial parcial linearizada não-homogênea:

$$\left( \square_{K} + 2\nabla^{(0)} f_0 \cdot \nabla \right) \delta f(x) = \mathcal{J}_{\text{GDQ}}(x)$$

onde $\square_{K} = g^{(0)\mu\bar{\nu}}\partial_\mu \partial_{\bar{\nu}}$ é o Laplaciano de Kähler e a fonte tensorial $\mathcal{J}_{\text{GDQ}}$ surge do acoplamento não-linear entre a torção intrínseca do [[26 - Próton - O Solíton de Ricci Composto|solíton]] e a curvatura de calibre das ondas perturbadoras.

---

## Ap.6.2 Resolução pelo Propagador de Sudarshan e Cinemática Compton

Para integrar a variação do campo dilatônico $\delta f(x)$ sob a EDP perturbada, introduzimos a Função de Green do operador de Kähler regularizada pelas condições de contorno simétricas do propagador retrocausal de Sudarshan:

$$\mathbf{G}_{\text{Sudarshan}}(x, x') = \frac{1}{2} \left[ \mathbf{G}_{\text{retardada}}(x, x') + \mathbf{G}_{\text{avançada}}(x, x') \right]$$

A solução formal convolutiva é dada por:

$$\delta f(x) = \int_{\mathcal{M}} \mathbf{G}_{\text{Sudarshan}}(x, x') \mathcal{J}_{\text{GDQ}}(x') \sqrt{g^{(0)}} \, d^4x'$$

No espaço de momentos, o operador diferencial projeta dois canais geométricos de escoamento (canais $s$ e $u$) provenientes do contorno de Sudarshan:

$$\delta f(k, k') \propto \left[ \frac{\mathbf{A}}{2(p \cdot k)} - \frac{\mathbf{B}}{2(p \cdot k')} \right]$$

onde os denominadores nascem diretamente da inversão do Laplaciano complexificado sujeito às relações de dispersão estáveis do [[26 - Próton - O Solíton de Ricci Composto|solíton]] ($p^2 = m^2c^2$) e das ondas de calibre ($k^2 = k'^2 = 0$):
*   $(p+k)^2 - m^2c^2 = 2p \cdot k$
*   $(p-k')^2 - m^2c^2 = -2p \cdot k'$

Pela conservação estrita da 1-forma complexa de Kähler no contorno fechado ($\oint \omega$), os quadrivetores momento satisfazem a conservação de Noether clássica:

$$p_\mu + k_\mu = p'_\mu + k'_\mu \implies p \cdot k - p \cdot k' = k \cdot k'$$

No referencial de repouso do [[26 - Próton - O Solíton de Ricci Composto|solíton]] ($p_\mu = (mc, \mathbf{0})$), a contração geométrica deduz o desvio de frequência Compton exato:

$$\frac{E'}{E} = \frac{1}{1 + \frac{E}{mc^2}(1 - \cos\theta)}$$

---

## Ap.6.3 Jacobiano de Contração e a Resolução dos Tensores de Interação

A seção de choque diferencial $\frac{d\sigma}{d\Omega}$ é calculada hidrodinamicamente pela taxa de fluxo da [[17 - Monotonicidade sob Torção de Cartan|medida invariante de Perelman]] $d\mu = e^{-f}\sqrt{g}d^4x$ projetada na fronteira assintótica:

$$\frac{d\sigma}{d\Omega} \propto |\delta f(k, k')|^2 \cdot \mathcal{J}_{\text{Jacobiano}}$$

A integração da função delta de conservação de energia-momento com a medida volumétrica de Perelman projeta o Jacobiano de fluxo (ou amortecimento de fase cinemático):

$$\mathcal{J}_{\text{Jacobiano}} = \left( \frac{E'}{E} \right)^2$$

Os numeradores complexos dos canais de Green $\mathbf{A}$ e $\mathbf{B}$ representam o acoplamento do [[26 - Próton - O Solíton de Ricci Composto|solíton]] aos vetores de polarização $\epsilon$ e $\epsilon'$. Sob as condições de calibre transversais no referencial de repouso ($p \cdot \epsilon = 0$ e $p \cdot \epsilon' = 0$), os tensores colapsam para:

$$\mathbf{A} = (p \cdot k)(\epsilon \cdot \epsilon') = mE(\epsilon \cdot \epsilon')$$
$$\mathbf{B} = -(p \cdot k')(\epsilon \cdot \epsilon') = -mE'(\epsilon \cdot \epsilon')$$

Ao calcular o módulo quadrado $|\delta f(k, k')|^2$, a soma algébrica das frações resulta em:

$$\frac{\mathbf{A}^2}{4(p \cdot k)^2} + \frac{\mathbf{B}^2}{4(p \cdot k')^2} - \frac{2\mathbf{A}\mathbf{B}}{4(p \cdot k)(p \cdot k')}$$
$$= \frac{m^2E^2(\epsilon \cdot \epsilon')^2}{4m^2E^2} + \frac{m^2E'^2(\epsilon \cdot \epsilon')^2}{4m^2E'^2} - \frac{-2m^2EE'(\epsilon \cdot \epsilon')^2}{4m^2EE'} = 1(\epsilon \cdot \epsilon')^2$$

---

## Ap.6.4 Média Geométrica de Spin e a Fórmula de Klein-Nishina

No formalismo [[02 - A Geometrização da Matéria|GDQ]], o [[26 - Próton - O Solíton de Ricci Composto|elétron]] possui spin $1/2$ emergente da [[34 - Monopolos e a Fibração de Hopf|Fibração de Hopf]] ($S^3 \to S^2$), onde os vetores de polarização da métrica sofrem uma precessão rotacional restauradora perpendicular ao plano de espalhamento mediada pela torção antissimétrica de Cartan ($B_{\mu\nu\lambda}$).

Esta componente de torção quiral converte o produto escalar clássico das polarizações $(\epsilon \cdot \epsilon')^2 = \cos^2\theta$ na seguinte soma de harmônicos no plano complexo cotangente de Kähler:

$$(\epsilon \cdot \epsilon')^2 \longrightarrow \frac{1}{4m^2} \left[ \frac{E}{E'} + \frac{E'}{E} - \sin^2\theta \right]$$

Unificando o prefactor clássico do raio do [[26 - Próton - O Solíton de Ricci Composto|solíton]] ($r_e^2 = \frac{e^2}{4\pi\varepsilon_0 mc^2}$), o Jacobiano de contração de fluxo $\left(\frac{E'}{E}\right)^2$ e a média geométrica tensorial calculada, obtemos a fórmula final de Klein-Nishina:

$$\frac{d\sigma}{d\Omega} = \frac{1}{2} r_e^2 \left( \frac{E'}{E} \right)^2 \left[ \frac{E'}{E} + \frac{E}{E'} - \sin^2\theta \right]$$

---

## Ap.6.5 Nota de Consistência e Limites do Modelo

A obtenção da fórmula de Klein-Nishina por meio dessa abordagem geométrica sugere caminhos para descrever o espalhamento relativístico sem recorrer a operadores bosônicos discretos. De forma a estabelecer uma correspondência matemática estrita, a formulação assume que os espinores de Dirac emergem de representações de Clifford das conexões no fibrado complexo de Kähler $\mathcal{M}$. Na ausência dessa correspondência de De Rham-Kähler entre formas diferenciais e espinores, a equivalência de spin é tratada como uma dualidade assintótica.

