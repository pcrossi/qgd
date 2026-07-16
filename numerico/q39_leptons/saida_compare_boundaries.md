# Comparação de Contornos e Domínios (Questão 39)

Este arquivo apresenta o estudo comparativo do comportamento do espectro leptônico radial sob diferentes tipos de truncamento geodésico na hiperesfera $S^3$.

## 1. Parâmetros da Simulação
* **Constante de Acoplamento ($b$):** 0.000121797869
* **Raio de Corte Efetivo ($\epsilon_{\rm eff}$):** 0.011591040463 rad
* **Tamanho da Grade ($N$):** 8000

## 2. Ficha de Definição Operacional (GDQ)
* **Domínio:** Conforme o Caso (variando nos limites $[\epsilon_{\rm eff}, \pi - \epsilon_{\rm eff}]$, $[\epsilon_{\rm eff}, \pi - \delta]$, etc.)
* **Contorno:** Condições de Robin ($c_L = -b/s, c_R = -b/s$) nos polos truncados ou Regularidade analítica nos polos completos.
* **Medida:** $d\mu = \sin^2\chi d\chi$ (Lebesgue $d\chi$ na representação regularizada).
* **Normalização:** $\int_{\text{domínio}} |\phi(\chi)|^2 d\chi = 1$.

## 3. Resultados Espectrais das Configurações de Bordo

| Configuração de Contorno                  | r2 (mu/e)  | Desvio r2 | r3 (tau/e)  | Desvio r3 |
| ----------------------------------------- | ---------- | --------- | ----------- | --------- |
| 1. Robin-Robin (Duplo Estômato)           | 208.158808 | +0.673%   | 3502.038295 | +0.716%   |
| 2. Robin-Regularidade (Estômato Único)    | 207.460940 | +0.335%   | 3489.539602 | +0.356%   |
| 3. Regularidade-Robin (Antipolo Estômato) | 207.460427 | +0.335%   | 3489.539071 | +0.356%   |
| 4. Reg-Reg (Sem Estômato / Rosen-Morse)   | 206.767399 | -0.000%   | 3477.131776 | -0.001%   |

## 4. Análise dos Resultados
1. **Caso 4 (Regularidade-Regularidade / Rosen-Morse Global):** Representa o limite assintótico analítico. Sem o truncamento de fronteira (estômato), o solver numérico converge com precisão de máquina para os autovalores de Rosen-Morse.
2. **Caso 2 e 3 (Estômato Único):** O truncamento de apenas um polo (fronteira física do estômato) reduz a simetria de $S^3$ e introduz um desvio local de $+0.33\%$. Isso reflete o fato de que a topologia real de um único bárion é descrita por um estômato ativo no polo e condições de regularidade naturais no antipolo.
3. **Caso 1 (Duplo Estômato):** O truncamento nos dois polos gera o dobro do desvio ($+0.67\%$), demonstrando que o efeito de deformação de fronteira é aditivo.
