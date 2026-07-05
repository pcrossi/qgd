# Capítulo 8 - A Estabilização da Singularidade do Buraco Negro

Na Relatividade Geral clássica, o colapso de uma estrela de massa $M$ não possui uma força de repulsão que suporte o peso quando o combustível nuclear acaba. A gravidade puxa o raio da estrela ($r_c$) para zero ($r_c \to 0$), e a energia gravitacional vai a $-\infty$.

Demonstra-se analiticamente que, no formalismo da GDQ, o potencial quântico de Bohm induz uma barreira de pressão repulsiva divergente no limite ultravioleta.

## 8.1 Limite de Equilíbrio Gravitacional-Quântico

### 8.1.1 Energia Gravitacional Clássica

Para uma massa esférica colapsando, a energia potencial gravitacional total é:
$$U_{\text{grav}} = - \frac{G M^2}{r_c}$$

### 8.1.2 A Pressão Geométrica de Bohm (GDQ)

Na formulação da GDQ, a estrela em colapso é descrita como um [[01 - O Problema Inicial - A Divergência entre a Integral de Feynman e a de Wiener|fluido de Madelung]]. Quando o raio $r_c$ diminui, a densidade de probabilidade $\rho(r)$ aumenta, concentrando-se como uma distribuição gaussiana no centro:
$$R(r) = \sqrt{\rho} = A e^{-\frac{r^2}{2r_c^2}}$$
Vamos calcular o Potencial Quântico de Bohm ($\mathcal{V}_{\text{Bohm}} = -\frac{\hbar^2}{2m} \frac{\nabla^2 R}{R}$) para os férmions (massa $m$) que compõem o centro da estrela ($r \to 0$):
- $\nabla^2 R = R \left( \frac{r^2}{r_c^4} - \frac{3}{r_c^2} \right)$
- $\mathcal{V}_{\text{Bohm}}(r \to 0) = -\frac{\hbar^2}{2m} \left( 0 - \frac{3}{r_c^2} \right) = \mathbf{+\frac{3\hbar^2}{2m r_c^2}}$

Como a estrela possui $N = M/m$ partículas, a Energia de Repulsão Topológica total do núcleo é:
$$U_{\text{Bohm}} = N \cdot \mathcal{V}_{\text{Bohm}} = \left(\frac{M}{m}\right) \frac{3\hbar^2}{2m r_c^2} = \mathbf{\frac{3\hbar^2 M}{2m^2 r_c^2}}$$

### 8.1.3 Ponto de Equilíbrio e Raio de Colapso

A energia total do sistema durante o colapso é a soma da atração gravitacional e da repulsão quântica:
$$E_{\text{total}}(r_c) = U_{\text{grav}} + U_{\text{Bohm}} = - \frac{G M^2}{r_c} + \frac{3\hbar^2 M}{2m^2 r_c^2}$$
Para encontrar o raio em que o colapso cessa (o estado de equilíbrio do [[02 - A Geometrização da Matéria|Solíton de Ricci]]), derivamos a energia total em relação ao raio e a igualamos a zero ($\frac{\partial E}{\partial r_c} = 0$):
$$\frac{G M^2}{r_c^2} - \frac{3\hbar^2 M}{m^2 r_c^3} = 0$$
Isolando o raio de colapso $r_c$:
$$\frac{G M^2}{r_c^2} = \frac{3\hbar^2 M}{m^2 r_c^3}$$
$$r_c = \frac{3\hbar^2}{G M m^2}$$

**Resultado Matemático:** O raio de colapso $r_c$ é estritamente maior que zero. A singularidade ($r_c = 0$) é matematicamente inatingível porque a repulsão geométrica cresce com $1/r^2$, enquanto a atração gravitacional cresce com $1/r$. O colapso cessa em um raio finito, estabelecendo um núcleo fisicamente regular, denso e assintoticamente estável configurado como um [[02 - A Geometrização da Matéria|Solíton de Ricci]].

---

## 8.2 Estabilidade Astrofísica e o Limite de Degenerescência de Fermi-Bohm

Para um sistema autogravitante composto por $N$ férmions degenerados sob compressão extrema, o potencial quântico de repulsão de Bohm total deve incorporar a distribuição dos estados permitidos no espaço de fase. A integração sobre a esfera de Fermi de energia cinética para um gás de férmions sob simetria esférica de raio $r_c$ fornece a energia de pressão quântica:
$$U_{\text{Pauli-Bohm}} \approx \frac{3}{10} \frac{\hbar^2}{m} \left( \frac{9\pi}{4} \right)^{2/3} \frac{N^{5/3}}{r_c^2}$$
Ao igualarmos esta repulsão degenerada à atração gravitacional newtoniana da estrela ($U_{\text{grav}} = -\frac{3}{5}\frac{GM^2}{r_c}$), onde a massa total é aproximada pelo número de nucleons ($M = N m_n$), o raio de equilíbrio estável do solíton de Fermi-Bohm é determinado rigorosamente por:
$$r_{\text{equilíbrio}} \approx \frac{\hbar^2 (9\pi/4)^{2/3}}{G m_n^2 m} N^{-1/3} \propto M^{-1/3}$$
Esta correção reestabelece a escala de estabilidade termodinâmica clássica astrofísica ($r_c \propto M^{-1/3}$), ancorando o colapso estelar GDQ no Princípio de Exclusão de Pauli.

---

## 8.3 O Formalismo Covariante do Tensor de Energia-Momento

### 8.3.1 O Tensor de Energia-Momento de Bohm Covariante

Introduzimos a contribuição quântica no espaço-tempo por meio de um fluido ideal quântico efetivo derivado da formulação de Hamilton-Jacobi-Bohm covariante. O tensor de energia-momento associado ao potencial quântico $Q$, denotado por $T_{\mu\nu}^{(\text{Bohm})}$, é definido como:
$$T_{\mu\nu}^{(\text{Bohm})} = (\rho_{\text{Bohm}} + P_Q) u_\mu u_\nu + P_Q g_{\mu\nu}$$
Onde:
- $u_\mu$ é a quadrivelocidade do fluido quântico (normalizada tal que $u_\mu u^\mu = -1$).
- $\rho_{\text{Bohm}}$ é a densidade de energia induzida pelo campo quântico.
- $P_Q$ é a **pressão quântica repulsiva**, explicitamente dada em função do potencial quântico de Bohm $Q$:
$$P_Q = - \rho_0 Q = \rho_0 \left( \frac{\hbar^2}{2m} \frac{\Box \sqrt{\rho_0}}{\sqrt{\rho_0}} \right)$$
onde $\rho_0$ é a densidade de probabilidade invariante do ensemble e $\Box \equiv g^{\alpha\beta}\nabla_\alpha\nabla_\beta$ é o operador de d'Alembertian covariante na métrica de fundo $g_{\mu\nu}$.

### 8.3.2 Acoplamento nas Equações de Einstein e a Transição de Regime

As equações de campo modificadas assumem a forma:
$$G_{\mu\nu} \equiv R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} = \kappa \left( T_{\mu\nu}^{(\text{Clássico})} + T_{\mu\nu}^{(\text{Bohm})} \right)$$

No regime assintótico externo ($r \gg \ell_{\text{Planck}}$ ou $r > r_s$), a densidade de probabilidade $\rho_0$ tende a uma distribuição espacialmente homogênea ou evanescente na escala quântica, fazendo com que los gradientes de $\sqrt{\rho_0}$ colapsem: $\nabla_\alpha \sqrt{\rho_0} \to 0 \implies Q \to 0$ e $P_Q \to 0$. Assim, $T_{\mu\nu}^{(\text{Bohm})} \to 0$, recuperando identicamente o tensor de energia-momento do vácuo clássico ($T_{\mu\nu}^{(\text{Clássico})} = 0$) e, por consequência, a [[28 - O Limite Clássico e o Princípio da Correspondência|métrica pura de Schwarzschild]] externa.

No regime interno ($r \to 0$), o adensamento da função de onda do colapso gera um gradiente extremo em $\rho_0$. O potencial quântico $Q$ diverge positivamente com sinal invertido, disparando uma **pressão quântica negativa/repulsiva isotrópica** ($P_Q \ll 0$) que atua como uma constante cosmológica local dinâmica, violando a Condição de Energia Forte (SEC) de Hawking-Penrose. É essa violação geométrica estrita que impede a formação da singularidade pontual, substituindo-a por um cerne ("core") regular estável de raio mínimo $r_{\text{min}} \sim \ell_{\text{Planck}}$ (onde $\ell_{\text{Planck}}$ é a [[04 - A Ação Funcional e Consistência Quântica (Loops)|escala de Planck]]).

### 8.3.3 Prova de Conservação do Tensor de Energia-Momento ($\nabla^\mu T_{\mu\nu} = 0$)

Para garantir a consistência física, a identidade de Bianchi ($\nabla^\mu G_{\mu\nu} = 0$) exige que $\nabla^\mu (T_{\mu\nu}^{(\text{Clássico})} + T_{\mu\nu}^{(\text{Bohm})}) = 0$. No interior do horizonte, onde o termo clássico é desprezível face à magnitude quântica, a divergência de $T_{\mu\nu}^{(\text{Bohm})}$ expande-se como:
$$\nabla^\mu T_{\mu\nu}^{(\text{Bohm})} = \nabla^\mu \left[ (\rho_{\text{Bohm}} + P_Q) u_\mu u_\nu \right] + \nabla_\nu P_Q = 0$$

Projetando esta equação na direção paralela e perpendicular à quadrivelocidade $u_\mu$:

1. **Projeção Longitudinal ($u^\nu \nabla^\mu T_{\mu\nu} = 0$):** Resulta na equação de continuidade para o fluido bohmiano, mostrando que o fluxo de energia quântica é perfeitamente conservado ao longo das geodésicas do fluido:
    $$u^\mu \nabla_\mu \rho_{\text{Bohm}} + (\rho_{\text{Bohm}} + P_Q) \nabla^\mu u_\mu = 0$$

2. **Projeção Transversal (Equação de Euler Modificada):**
    $$(\rho_{\text{Bohm}} + P_Q) u^\mu \nabla^\mu u_\nu = - \left( g_{\nu\mu} + u_\nu u_\mu \right) \nabla^\mu P_Q$$

Esta última relação prova que a aceleração das geodésicas do fluido ($u^\mu \nabla^\mu u_\nu$) é balanceada exatamente pelo gradiente da pressão quântica $\nabla^\mu P_Q$. À medida que o colapso avança, o gradiente de pressão quântica cresce na direção oposta à atração gravitacional clássica, zerando a aceleração líquida exatamente em $r = r_{\text{min}}$.

Como a transição entre as componentes do tensor é mediada analiticamente pela variação suave e contínua da função de onda $\psi = \sqrt{\rho_0}e^{iS/\hbar}$ sob a ação do operador $\Box$, a transição de regimes é perfeitamente suave ($C^\infty$), eliminando qualquer "gap" ou descontinuidade física na estrutura métrica do espaço-tempo.

> [!note]- Adendo: Unitaridade e Resolução do Paradoxo da Perda de Informação via Fluxo de Ricochete
> 
> ![[notas/8/nota_8.5_informacao_bn.md]]
