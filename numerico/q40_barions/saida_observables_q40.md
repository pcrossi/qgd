# Relatório estrutural/diagnóstico: Observáveis Bariônicos (Q40)

Este relatório apresenta a avaliação estrutural dos observáveis fundamentais do
próton e do nêutron derivados a partir do sóliton de Ricci-Bismut trimodal na
GDQ. Ele **não deve ser lido como validação numérica completa** dos fatores de
forma ou do espalhamento bariônico.

## 1. Ficha de Definição Operacional (GDQ)
* **Domínio:** $\chi \in [\epsilon_B, \pi]$ rad
* **Contorno:** Condição de Robin no estômato ($c_L = -b/s$) e regularidade natural no antipolo.
* **Medida:** $d\mu = \sin^2\chi d\chi$ (representação regularizada via densidade efetiva $w(\chi)$).
* **Normalização:** $\int_{\epsilon_B}^{\pi} w(\chi) d\chi = 1$.

## 2. Parâmetros Físicos e Geométricos
* **Constante de Estrutura Fina ($\alpha$):** 0.00729735
* **Raio do Estômato Efetivo ($\epsilon_{\rm eff}$):** 1.15910405e-02 rad
* **Escala Compton do Elétron ($\Lambda_C$):** 386.159268 fm
* **Raio Cosmológico Bariônico ($R_B$):** 579.238902 fm

## 3. Momentos Magnéticos Anômalos (Fase Efetiva de Transgressão)
O acoplamento com a transgressão de Nieh-Yan de fronteira e a projeção volumétrica de magnetização torsional $\frac{3}{5}$ e $\frac{3}{4}$ fornecem:

| Observável | Calculado (GDQ) | Referência CODATA | Desvio |
| ---------- | --------------- | ----------------- | ------ |
| $\mu_p$ (Próton) | 2.792829 $\mu_N$ | 2.792847 $\mu_N$ | -0.00066% |
| $\mu_n$ (Nêutron) | -1.912811 $\mu_N$ | -1.913043 $\mu_N$ | -0.01212% |

## 4. Avaliação discreta da fórmula estrutural do raio

A tabela abaixo avalia a fórmula estrutural do raio em malhas discretas. Como a
expressão usada é analítica/projetada, a estabilidade da tabela não substitui a
validação numérica do operador bariônico completo:

| N | rp (fm) | Erro rp | rp_num (fm) | <rn^2>_target | <rn^2>_num |
| --- | --- | --- | --- | --- | --- |
| 800 | 0.840779 | -0.0109% | 0.840779 | -0.1161 | -0.116100 |
| 1600 | 0.840779 | -0.0109% | 0.840779 | -0.1161 | -0.116100 |
| 3200 | 0.840779 | -0.0109% | 0.840779 | -0.1161 | -0.116100 |
| 6400 | 0.840779 | -0.0109% | 0.840779 | -0.1161 | -0.116100 |


*Nota:* O raio analítico do próton obtido por projeção de octante de Hopf e vestimento geométrico de borda é $r_p = C_r \epsilon_B R_B \approx 0.84078$ fm (desvio de apenas -0.0109% frente ao CODATA).

## 5. Excitações Radiais e Massa da Ressonância $\Delta(1232)$
A quantização por coordenadas coletivas e o momento de inércia do sóliton composto $I_{\rm rot} = \frac{3}{10} M_p r_p^2$ preveem o primeiro estado excitado de spin-isospin $J=3/2$:

* **Momento de Inércia do Sóliton ($I_{\rm rot}$):** 198.981875 MeV fm$^2$
* **Diferença de Energia ($E_{\Delta} - M_p$):** 293.53 MeV
* **Massa Prevista para o $\Delta(1232)$:** 1231.80 MeV
* **Massa de Referência (PDG):** 1232.00 MeV
* **Desvio Absoluto:** -0.20 MeV

## 6. Fatores de Forma de Sachs $G_E(Q^2)$ e $G_M(Q^2)$
Os fatores de forma são normalizados estruturalmente para obedecer aos limites
estáticos:
* $G_E^p(0) = 1.0$, $G_E^n(0) = 0.0$
* $G_M^p(0) = \mu_p \approx 2.7928$, $G_M^n(0) = \mu_n \approx -1.9128$

O decaimento a altos momentos esperado é a lei de potência de contagem
dimensional do sóliton:

\[
G_E(Q^2)\sim (Q^2)^{-2}.
\]

Essa lei ainda deve ser demonstrada por análise assintótica da transformada de
borda e validada numericamente com o operador bariônico completo. O gráfico em
`numerico/figs/baryonic_form_factors.png` deve ser tratado como ilustração
diagnóstica, não como benchmark final.
