# Equilíbrio Térmico Efetivo do Estômato (Questão 39)

Este arquivo documenta a busca efetiva por parâmetros térmicos de Matsubara no estômato finito da GDQ. O objetivo é quantificar quais deslocamentos de borda e acoplamento seriam necessários para cancelar o desvio local observado no domínio de estômato único.

Estes parâmetros são a especificação numérica efetiva da resposta térmica. A derivação variacional GDQ formal identifica essa resposta como $-H^{-1}J^{(\beta)}$. Falta avaliar diretamente a Hessiana $H$ e as fontes térmicas $J^{(\beta)}$ a partir do operador GDQ com contorno Robin-Regularidade.

## 1. Estado de Referência a $T=0$ (Estômato Único)
* **$r_2$ (Múon/Elétron):** 207.460940 (Desvio: +0.335%)
* **$r_3$ (Tau/Elétron):** 3489.539599 (Desvio: +0.356%)

## 2. Ficha de Definição Operacional (GDQ)
* **Domínio:** $[\epsilon_{\rm eff} + \Delta_\epsilon, \pi - \delta]$ rad
* **Contorno:** Condição de Robin no estômato ($c_L = -b_T/s_T$) e regularidade no antipolo.
* **Medida:** $d\mu = \sin^2\chi d\chi$ (Lebesgue $d\chi$ na representação regularizada).
* **Normalização:** $\int_{\text{domínio}} |\phi(\chi)|^2 d\chi = 1$.

## 3. Parâmetros efetivos obtidos por Nelder-Mead
A otimização convergiu com sucesso em 4.23 segundos.

* **$\Delta_\epsilon$ (Expansão Térmica do Estômato):** 2.37946518e-04 rad
* **$\Delta_b$ (Vestimento Térmico do Acoplamento):** 4.51750951e-02 (+4.51751%)

## 4. Espectro Equilibrado Final vs CODATA

| Razão de Massa | Calculado (Otimizado) | CODATA Referência | Erro Absoluto |
| -------------- | --------------------- | ----------------- | ------------- |
| $M_\mu / M_e$ | 206.768339 | 206.768282 | 0.00005663 |
| $M_\tau / M_e$| 3477.149464 | 3477.150000 | -0.000536 |

## 5. Análise e status físico
1. **$\Delta_\epsilon > 0$:** A correção térmica expande o estômato efetivo. Isso suaviza a barreira e neutraliza a compressão geométrica induzida pela borda de Robin.
2. **Escala Física:** A variação necessária é pequena em escala angular absoluta ($\Delta_\epsilon \approx 2.38 \times 10^-4$ rad), mas não desprezível em relação ao estômato ($\approx 2\%$). O vestimento efetivo do acoplamento também é significativo ($\Delta_b \approx 4.5\%$).
3. **Pendência:** a derivação variacional formal identifica $\Delta_\epsilon$ e $\Delta_b$ como $-H^{-1}J^{(\beta)}$. Falta avaliar diretamente a Hessiana $H$ e as fontes térmicas $J^{(\beta)}$ a partir do operador GDQ com contorno Robin-Regularidade. Até lá, este script fecha a engenharia inversa numérica do alvo, não a prova preditiva final.
