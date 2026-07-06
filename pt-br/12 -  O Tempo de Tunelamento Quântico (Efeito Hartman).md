# Capítulo 12 - O Tempo de Tunelamento Quântico (Efeito Hartman)

Na física tradicional, quando uma partícula atravessa uma barreira de potencial muito larga ($L$), a mecânica quântica convencional prevê que o tempo de travessia torna-se independente de $L$. Este fenômeno, conhecido como **Efeito Hartman**, gera um aparente paradoxo causal: se a largura da parede dobra, a partícula leva o mesmo tempo para atravessar, sugerindo uma velocidade de coordenada macroscópica superluminar ($v \to \infty$).

Sob o formalismo da GDQ, a causalidade local é preservada por meio de uma contração métrica dinâmica da variedade de Kähler, a qual emerge naturalmente a partir do decaimento da densidade do fluido.

---

## 12.1 A Densidade do Fluido dentro da Barreira

Ao incidir sobre uma barreira de potencial constante $V_0 > E$, a função de onda decai exponencialmente (regime evanescente):
$$\psi(x) = \psi_0 e^{-\kappa x}$$
onde $\kappa = \sqrt{2m(V_0 - E)}/\hbar$ é a constante de atenuação. A densidade de probabilidade física do fluido correspondente é:
$$\rho(x) = \rho_0 e^{-2\kappa x}$$

---

## 12.2 O Acoplamento Métrico de Kähler-Perelman

Em conformidade com a [[02 - A Geometrização da Matéria|geometrização da matéria]] no formalismo GDQ, a métrica do espaço-tempo não é um plano de Minkowski rígido. Na ausência de correntes clássicas estacionárias (onde a fase $S_R$ é suprimida na transição evanescente), a componente métrica longitudinal $g_{xx}$ acopla-se diretamente à densidade do fluido de forma a manter a invariância da medida de volume:
$$g_{xx}(x) = g_0 \frac{\rho(x)}{\rho_0} = g_0 e^{-2\kappa x}$$
onde $g_0$ é o tensor métrico imperturbado do vácuo assintótico (adimensional, normalizado como $g_0 = 1$), e $\rho_0 \equiv \rho(0)$ define a densidade de probabilidade hidrodinâmica imediatamente na interface de incidência da barreira ($x=0$).

---

## 12.3 O Cálculo da Distância Própria e a Contração Espacial

O paradoxo do Efeito Hartman emerge porque o observador macroscópico assume um espaço euclidiano rígido de comprimento $L$. Contudo, a coordenada $x$ é uma coordenada de mapa. A distância física real ($D_{\text{própria}}$) percorrida pelo solíton dentro da barreira é encolhida pela deformação métrica:
$$D_{\text{própria}} = \int_{0}^{L} \sqrt{g_{xx}(x)} \, dx = \int_{0}^{L} \sqrt{g_0} e^{-\kappa x} \, dx$$

Resolvendo a integral analiticamente:
$$D_{\text{própria}} = \frac{\sqrt{g_0}}{\kappa} (1 - e^{-\kappa L})$$

No limite assintótico de uma barreira infinitamente espessa ($L \to \infty$), a distância própria converge para uma cota superior estrita:
$$\lim_{L \to \infty} D_{\text{própria}} = \frac{\sqrt{g_0}}{\kappa}$$

---

## 12.4 O Tempo de Trânsito e a Preservação da Causalidade Local

Pela [[28 - O Dilema da Retrocausalidade e a Segunda Lei|causalidade local de Weyl-Cartan]], o escoamento quântico atravessa a malha deformada mantendo a velocidade física local [[03 - Causalidade Complexa e o Fim do Paradoxo de Wick|invariante e limitada]] ao teto relativista, tal que $v_{\text{própria}} = \sqrt{g_{xx}} \frac{dx}{dt} = v_0 \le c$. Consequentemente, a velocidade de coordenada decai como $\frac{dx}{dt} = v_0 (g_{xx})^{-1/2}$, refletindo o arrasto inercial do vácuo.

O tempo de trânsito de coordenada ($T$) medido pelo relógio do laboratório é calculado integrando a taxa de avanço temporal ao longo do canal contraído:
$$T = \int_{0}^{L} \frac{dt}{dx} dx = \int_{0}^{L} \frac{\sqrt{g_{xx}(x)}}{v_0} \, dx = \frac{\sqrt{g_0}}{v_0 \kappa} (1 - e^{-\kappa L})$$

No regime assintótico ($L \to \infty$), o tempo de trânsito satura de forma idêntica à distância própria:
$$\lim_{L \to \infty} T = \frac{\sqrt{g_0}}{v_0 \kappa} = \text{constante}$$

---

## 12.5 Conclusão

O tempo de tunelamento torna-se independente de $L$ não porque a partícula viaje infinitamente rápido, mas porque a **distância física real que a partícula atravessa dentro da barreira possui uma cota máxima $\frac{\sqrt{g_0}}{\kappa}$**. O espaço contrai-se transitoriamente sob a ausência de densidade, de modo que barreiras geometricamente gigantescas no laboratório são topologicamente minúsculas para o solíton GDQ, preservando a causalidade local ($v_{\text{própria}} \le c$).

---

## 12.6 Fundamentação a partir do Potencial e da Ação de Kähler

Em uma variedade de Kähler unidimensional complexa, a métrica $g_{z\bar{z}}$ é expressa localmente através da segunda derivada de um [[29 -  A constante de estrutura fina|potencial escalar de Kähler]] $K(z, \bar{z})$:
$$g_{z\bar{z}} = \frac{\partial^2 K}{\partial z \partial \bar{z}}$$

Separando em coordenadas reais ($z = x + iy$), a componente puramente espacial reduz-se a $g_{xx} = \partial_x^2 K$. No formalismo da Geometrodinâmica Quântica (GDQ), a densidade de probabilidade do conjunto bohmiano $\rho(x)$ está intrinsecamente ligada à densidade de volume local do espaço-tempo. A ação variacional do sistema geométrico é governada pelo funcional de volume de Kähler sujeito à conservação local da densidade de probabilidade.

Formulamos o princípio variacional definindo uma ação funcional $S[K]$ com um multiplicador de Lagrange $\Lambda(x)$ que impõe a restrição de fluxo incompressível na forma de volume ($\det(g) = \text{constante}$ no espaço de fase):
$$S[K] = \int \mathcal{L} \, d^4x = \int \left[ R(g) - \Lambda(x) \left( \det(g_{\mu\nu}) - \rho(x)\sqrt{-g_0} \right) \right] d^4x$$

Onde $\rho(x)$ atua como a fonte de densidade invariante e $g_0$ é a métrica assintótica Euclidiana/Minkowskiana fora da barreira de potencial.

### 12.6.1 Minimização Variacional e Emergência da Relação

Ao realizarmos a variação da ação em relação ao potencial de Kähler $K$ no subespaço espacial coordenado $x$, a restrição de volume força o determinante da subvariedade acopla-se diretamente à distribuição de densidade da função de onda tunelante. Para o caso unidimensional do Efeito Hartman, o determinante da métrica espacial reduz-se diretamente à componente $g_{xx}$:
$$\frac{\delta S}{\delta K} = 0 \implies \frac{\partial}{\partial x^2} \left( \frac{\partial \mathcal{L}}{\partial g_{xx}} \right) = 0$$

Como a forma de volume total $\omega \wedge \omega = \det(g_{z\bar{z}})\,dx \wedge dy$ deve satisfazer localmente a equação do tipo Monge-Ampère complexa sob o perfil de matéria:
$$g_{z\bar{z}} = \frac{\partial^2 K}{\partial z \partial \bar{z}} = \rho(z, \bar{z})$$

Projetando sobre a direção real $x$ do tunelamento unidimensional, onde a fase quântica e as componentes transversais estão em regime estacionário, a variação resulta diretamente na equação de campo:
$$g_{xx} = g_0 \frac{\rho(x)}{\rho_0}$$

Essa equivalência prova que a contração espacial da métrica dentro da barreira de potencial não é um postulado arbitrário: **ela é a solução exata da equação de Monge-Ampère para o potencial de Kähler $K$ quando a densidade do fluido quântico atua como a fonte do volume geométrico.**
