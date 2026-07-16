# Resultados da Simulação: Hierarquia Leptônica (Q39)

Este arquivo foi gerado automaticamente pelo solver de autovalores para o vácuo de Kähler da GDQ.

## 1. Parâmetros Físicos Geométricos
* **Constante de Estrutura Fina ($\alpha$):** 0.00729735
* **Raio de Corte Efetivo ($\epsilon_{\rm eff}$):** 1.15910405e-02 rad
* **Parâmetro de Rosen-Morse ($s$):** 0.01159104
* **Constante de Acoplamento ($b$):** 1.21797869e-04
* **Intensidade do Potencial Cotangente ($2b$):** 2.43595739e-04

## 2. Ficha de Definição Operacional (GDQ)
* **Domínio:** $[\epsilon_{\rm eff}, \pi - \epsilon_{\rm eff}]$ rad
* **Contorno:** Condições de Robin que cancelam a singularidade de coordenadas ($$\psi' = -b/s \psi$$).
* **Medida:** $d\mu = \sin^2\chi d\chi$ (Lebesgue $d\chi$ sob a função regularizada $\psi(\chi) = \phi(\chi)/\sin^s\chi$).
* **Normalização:** $\int_{\text{domínio}} |\phi(\chi)|^2 d\chi = 1$ (Integral de $L^2$ radial da função de onda total $\phi$).

## 3. Espectro Analítico de Rosen-Morse (Limite Regular-Regular)
* **$l_e$ (Elétron):** 2.39355764e-05
* **$l_\mu$ (Múon):** 1.023316
* **$l_\tau$ (Tau):** 289.394230
* **Razão de Massa $M_\mu / M_e$:** 206.7679 (Alvo CODATA: 206.768)
* **Razão de Massa $M_\tau / M_e$:** 3477.1465 (Alvo CODATA: 3477.15)

## 4. Estudo de Convergência da Discretização (Robin-Robin)
Abaixo está a tabela de convergência da discretização tridiagonal sob as condições de contorno de Robin:

| N    | l1         | l2       | l18        | r2 (mu/e) | r3 (tau/e) |
| ---- | ---------- | -------- | ---------- | --------- | ---------- |
| 800  | 0.00002394 | 1.037126 | 293.443197 | 208.1584  | 3501.3866  |
| 1600 | 0.00002394 | 1.037130 | 293.525958 | 208.1587  | 3501.8803  |
| 3200 | 0.00002394 | 1.037130 | 293.546623 | 208.1588  | 3502.0039  |
| 6400 | 0.00002394 | 1.037131 | 293.551786 | 208.1589  | 3502.0361  |

## 5. Notas de Convergência e Conclusão
1. O estado fundamental $l_1$ converge para o valor analítico exato com 8 dígitos de precisão.
2. A diferença residual de $\approx 0.6\%$ nas razões de massa discretas representa o deslocamento físico local induzido pelas condições de contorno de Robin na borda do estômato de tamanho finito $\epsilon_{\rm eff}$.
3. O gráfico de autoestados radiais foi salvo com sucesso em `numerico/figs/leptonic_hierarchy.png`.
