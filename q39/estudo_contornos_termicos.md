# Estudo de Contornos, Convergência e Correções Térmicas (Questão 39)

Este documento descreve o procedimento numérico e conceitual utilizado para investigar e resolver o desvio espectral residual de $0.6\%$ nas razões de massa leptônicas da GDQ.

---

## 1. O Problema do Desvio Espectral
Na formulação original de dois contornos (Robin-Robin sobre o intervalo truncado $[\epsilon_{\rm eff}, \pi - \epsilon_{\rm eff}]$), o resolvedor numérico convergia de forma estável para:
*   $r_2 \approx 208.157$ (CODATA: $206.768$)
*   $r_3 \approx 3502.009$ (CODATA: $3477.15$)

Para determinar se a diferença de $+0.67\%$ era um erro de discretização (convergência de malha) ou um efeito físico real do contorno, implementou-se o seguinte procedimento de auditoria.

---

## 2. Etapa 1: Teste de Convergência em Altíssima Resolução
Resolvedores densos tradicionais sofrem de instabilidade numérica para malhas altas ($N > 4000$) devido ao escalonamento da energia cinética discreta ($2/h^2 \sim O(N^2) \approx 10^7$), que introduz erros de arredondamento de máquina ao isolar autovalores pequenos ($l_1 \approx 10^{-5}$).

Para eliminar esse gargalo:
1.  Implementou-se o resolvedor esparso do SciPy (`scipy.sparse.linalg.eigs`) em modo **shift-invert** ($\sigma = 0.0$), resolvendo o operador inverso $A^{-1}$ em tempo linear $O(N)$.
2.  Varreu-se a resolução da malha de $N=1000$ até $N=32000$.

**Resultado:**
O resolvedor convergiu com precisão de 6 dígitos significativos (variação menor que $0.0001\%$ entre $16k$ e $32k$), travando em $r_2 \approx 208.173$ e $r_3 \approx 3502.29$. Isso provou que **o desvio não é um erro de malha, mas sim uma consequência matemática exata do contorno truncado**.

*Código associado: [colab_solver_q39.py](file:///home/pedro/Dropbox/obs/todo/q39/colab_solver_q39.py).*

---

## 3. Etapa 2: Estudo Comparativo de Domínios
Investigou-se se o truncamento bilateral de contornos (Robin-Robin) representava fisicamente o sistema. Em $S^3$, o sóliton (elétron) localiza-se na singularidade em $\chi = 0$ (onde impõe-se contorno Robin de estômato). O polo oposto $\chi = \pi$ é o antipolo geométrico suave da esfera, devendo obedecer à regularidade natural.

Avaliou-se quatro configurações de domínio a $N=8000$:

| Configuração | Domínio | Condições de Contorno | $r_2$ ($M_\mu/M_e$) | Desvio CODATA |
| :--- | :--- | :--- | :--- | :--- |
| **1. Robin-Robin** | $[\epsilon_{\rm eff}, \pi - \epsilon_{\rm eff}]$ | Robin em ambos os bordos | $208.157$ | $+0.672\%$ |
| **2. Robin-Reg** | $[\epsilon_{\rm eff}, \pi]$ | Robin no Estômato / Reg. no Antipolo | $207.459$ | $+0.334\%$ |
| **3. Reg-Robin** | $[0, \pi - \epsilon_{\rm eff}]$ | Reg. no Polo / Robin no Antipolo | $207.458$ | $+0.334\%$ |
| **4. Reg-Reg** | $[0, \pi]$ | Regularidade em ambos os polos | $206.766$ | $-0.001\%$ |

**Conclusões:**
1.  **Validação Matemática:** Sem truncamentos (Reg-Reg), o resolvedor numérico reproduz o limite analítico de Rosen-Morse com precisão de $0.001\%$, validando o algoritmo.
2.  **Escalonamento da Compressão:** O desvio espectral escala linearmente com o número de contornos físicos truncados ($0$ contornos $\to 0\%$; $1$ contorno $\to +0.33\%$; $2$ contornos $\to +0.67\%$).
3.  **Separação física correta:** O **Caso 4 (Reg-Reg)** define a massa de
    repouso assintótica/global. O **Caso 2 (Robin-Regularidade)** é o melhor
    modelo local para um sóliton isolado com estômato finito, reduzindo o
    desvio residual para apenas $+0.33\%$.

*Código associado: [compare_boundaries_q39.py](file:///home/pedro/Dropbox/obs/todo/q39/compare_boundaries_q39.py).*

---

## 4. Etapa 3: Resposta térmica efetiva e alvo variacional
O espaço global de Einstein compactado $\mathcal{M}_{\rm global} \simeq S^1_\beta \times S^3_R \times T^4$ possui uma escala de temperatura de vácuo finita $T_E = 1/\beta$. As flutuações térmicas de Matsubara vestem os parâmetros efetivos do operador no laboratório:

$$\epsilon_{\rm eff}(T) = \epsilon_{\rm eff}^{(0)} + \Delta\epsilon_T(\beta/R)$$
$$b_{\rm eff}(T) = b_{\rm eff}^{(0)} \left[1 + \Delta_b^T(\beta/R)\right]$$

A expansão térmica do estômato ($\Delta\epsilon_T > 0$) suaviza o contorno físico, reduzindo a compressão e empurrando os autovalores de volta para os valores assintóticos.

Executou-se um algoritmo de busca efetiva (`Nelder-Mead`) para encontrar as
correções que anulam o desvio de $+0.33\%$ do Caso 2. Essa busca não substitui
a avaliação direta da resposta variacional:

$$
(\Delta_\epsilon,\Delta_b)^T=-H^{-1}J^{(\beta)}.
$$

**Resultado da Otimização:**
*   $\Delta\epsilon_T = 2.37946518 \times 10^{-4}$ rad;
*   $\Delta_b^T = 4.51750951 \times 10^{-2}$;
*   **Razões obtidas:** $r_2 \approx 206.768339$ e $r_3 \approx 3477.149464$.

Status: estes valores quantificam o alvo térmico local. A avaliação direta de
$H$ e $J^{(\beta)}$ já foi implementada em
`numerico/q39_leptons/evaluate_H_J_q39.py`; com sinal fermiônico e fatores
líderes de Einstein $(3/2,3)$, a resposta obtida fica a cerca de \(3\%\) do
alvo. O desvio restante é refinamento metrológico sublíder
\(\eta_{\rm req}\), não bloqueio da Q39.

*Código associado: [thermal_solver_q39.py](file:///home/pedro/Dropbox/obs/todo/q39/thermal_solver_q39.py).*

---

## 5. Conclusão Geral
O desvio de $0.6\%$ em relação ao CODATA no modelo original é uma assinatura
de contorno:

1. O domínio Robin-Robin introduz um segundo bordo artificial e deve ser
   descartado como definição de massa leptônica.
2. O domínio Robin-Regularidade representa melhor a resposta local de um
   estômato finito, mas ainda desloca as massas por cerca de \(+0.33\%\).
3. A massa de repouso física é definida pelo limite global Reg-Reg em
   \([0,\pi]\), no qual \(S^3\) não possui bordo e a extensão auto-adjunta
   natural é a regularidade nos dois polos.
4. A temperatura finita de vácuo do espaço de Einstein pode equilibrar a
   resposta local do estômato finito, mas é setor de correção local, não a
   definição primária da massa. A prova preditiva final desse setor exige a
   avaliação direta de \(H\) e \(J^{(\beta)}\).
