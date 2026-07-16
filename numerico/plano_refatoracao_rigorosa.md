# Plano de Implementação Numérica — Ontologia GDQ (Nível 2)

## 1. O Abismo entre MQ e GDQ
A maior armadilha numérica foi a "regressão fenomenológica": tentar resolver problemas da Geometrodinâmica usando ferramentas da Mecânica Quântica convencional (como a equação de Schrödinger com massas reduzidas arbitrárias) ou EDOs clássicas newtonianas. 

Na GDQ:
- **Não há "partículas pontuais" em potenciais:** As entidades são estômatos (furos/defeitos topológicos) ou monopolos/sólitons na geometria do *bulk* ($S^3 \times T^4$).
- **Não há "espaço plano + tempo":** O tempo não é absoluto. O fluxo principal que relaxa estados é o parâmetro geométrico $\tau$ do **Fluxo de Ricci-Bismut**.
- **Não há Equação de Schrödinger:** Os estados estacionários são ditados pela **Equação de Dirac-Kähler** acoplada à torção e ao Laplaciano de Hodge ($\Delta_A$) nas variedades curvas.

---

## 2. Refatoração Estrutural por Bloco (Matemática Pura)

### Bloco Q30: Confinamento (Mass Gap Yang-Mills)
* **Ontologia Errada (Anterior):** Equação de Schrödinger 1D $H = p^2/2\mu + V(r)$ para um méson.
* **Ontologia GDQ Correta:** O Mass Gap e o Confinamento surgem da geometria do fibrado de gauge $SU(3)$ na variedade compacta.
* **Implementação Numérica:**
  1. Montar a matriz do **Laplaciano de Hodge** discreto ($\Delta_A = d d^* + d^* d$) para 1-formas de conexão na métrica do setor interno.
  2. Construir o Hessiano de Perelman confinante: $\mathcal{H}_{\text{conf}} = -\Delta_A + V_{\text{Ricci}}$, onde o potencial provém da curvatura local.
  3. Calcular o espectro de autovalores desta matriz puramente geométrica. O *Mass Gap* é estritamente o primeiro autovalor $\lambda_1 > 0$, garantido pela compacidade topológica da câmara bariônica $S^3$, provando a ausência de modos contínuos assintóticos (ausência de fótons de cor livres).

### Bloco Q31: CP Forte (Relaxamento Axial)
* **Ontologia Errada (Anterior):** Pêndulo clássico amortecido no tempo newtoniano ($\ddot{\theta} + \gamma \dot{\theta} + \omega^2\sin\theta = 0$).
* **Ontologia GDQ Correta:** O ângulo $\theta$ de violação CP é um invariante topológico no setor torcional do fibrado. Ele é relaxado pelo **Fluxo de Ricci-Bismut** governado pelo Funcional de Perelman-Bismut $\mathcal{W}_B$.
* **Implementação Numérica:**
  1. Integrar a Equação de Evolução do Fluxo: $\frac{\partial \theta}{\partial \tau} = - \frac{\delta \mathcal{W}_B}{\delta \theta}$.
  2. O atrito não é uma constante genérica $\gamma$, mas o gradiente do campo do diláton (expansão do volume métrico) $\frac{\partial f}{\partial \tau}$. 
  3. A simulação exibirá como o fluxo geométrico empurra naturalmente a torção assintótica para o vácuo conservador de CP ($\theta \to 0$) em $\tau \to \infty$.

### Bloco Q40: Observáveis Bariônicos (Próton/Nêutron)
* **Ontologia Errada (Anterior):** Espalhamento de onda plana de dipolo.
* **Ontologia GDQ Correta:** O Bárion é um sóliton trimodal de Ricci-Bismut. Os observáveis são integrais da métrica sobre o domínio esférico com fronteiras de Robin (estômatos).
* **Implementação Numérica:**
  1. Solucionar a Equação de Dirac-Kähler radial na métrica esférica $S^3$ para achar a base spinorial (função de onda orgânica $\Phi_0(\chi)$).
  2. **Raio de Carga:** Integrar numericamente a distância geodésica ao quadrado $d_g^2(\chi)$ sob a medida de Perelman $e^{-f}|\Phi_0|^2 \sqrt{\det g_{S^3}}$.
  3. **Momentos Magnéticos:** Integrar no volume as densidades de **Torção de Bismut** paralela (próton) e antiparalela (nêutron) provenientes das formas de Transgressão de Nieh-Yan (termos quirais).

### Bloco Q37 e Q38: Estrutura Fina e Gravidade
* **Ontologia Errada (Anterior):** Uso de ansatz trigonométrico genérico (Q38) ou raios simétricos forçados (Q37).
* **Ontologia GDQ Correta:** Integração estrita dos tensores geométricos no setor de vácuo.
* **Implementação Numérica:**
  1. **Gravidade:** Integrar o volume de Perelman $\mathcal{V}_{\text{eff}}^{(G)}$ da métrica de background (extraindo os perfis analíticos $A, U_*, q_*$ diretamente da métrica induzida pela teoria), deduzindo a supressão natural ou reportando a discrepância com o Instantão.
  2. **Alfa:** Calcular a matriz densidade $G_*^{ab}$ do fibrado de gauge abeliano sobre $T^4$, impondo as torções internas de fronteira para quebrar a simetria de holonomia trivial e induzir a métrica exata, projetando no espinor de carga elementar $v=(2,0,0,0)$.

### Bloco Q28 / Q29: Setor Eletrofraco
* **Ontologia Errada (Anterior):** Equação fenomenológica do potencial de Higgs com $a_2, a_4$ arbitrários.
* **Ontologia GDQ Correta:** Massas são autovalores topológicos; a quebra de simetria é uma transição de sela do volume geométrico.
* **Implementação Numérica:**
  1. Calcular as constantes de gauge $1/g^2$ como normas de intersecção topológicas reais $\int ||\xi||^2 d\mu_g$ dos fibrados na variedade base.
  2. Avaliar o ponto de sela do Funcional de Volume para extrair a VEV orgânica localmente.

---

## 3. Ordem de Refatoração Crítica
Começaremos a codificação matemática purificada pelos elementos que testam diretamente a robustez dos operadores diferenciais em variedades curvas:
1. **Solver do Laplaciano de Hodge e Confinamento (Q30)**: Matriz diferencial orgânica.
2. **Fluxo de Ricci-Bismut (Q31)**: EDO de relaxamento paramétrico $\tau$.
3. **Métrica Esférica do Sóliton (Q40)**: Distâncias geodésicas baseadas em Dirac-Kähler.
4. **Volumes de Métrica (Q37 e Q38)**.
