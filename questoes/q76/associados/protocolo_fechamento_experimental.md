# Q76 — protocolo de fechamento experimental de um qubit GDQ

## 1. Objetivo

Este protocolo especifica como testar a proposta de qubit geométrico sem
misturar a GDQ com um Hamiltoniano de qubit postulado.

A cadeia exigida é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast
\to
K_{\rm phys}
\to
P_Q
\to
\Delta_{\rm gap},J
\to
\mathsf R_{\rm app}
\to
\text{taxas observáveis}.
$$

## 2. Dados de entrada permitidos

Os dados externos permitidos são dados do aparelho e do material:

1. geometria do defeito;
2. temperatura;
3. tempo de porta;
4. espectro de ruído do banho;
5. eficiência de preparação e leitura;
6. campos clássicos aplicados.

Esses dados não alteram a ação oficial. Eles definem o problema de contorno.

## 3. Quantidades que a GDQ deve produzir

Para um protótipo real, a GDQ deve calcular:

$$
\Delta_{\rm gap}
=
\lambda_2-\lambda_1,
$$

onde $\lambda_0,\lambda_1$ formam o subespaço lógico e $\lambda_2$ é o primeiro
modo externo.

Também deve calcular:

$$
J_{\rm leak}
=
\left\|
P_\perp \delta K P_Q
\right\|,
$$

e a impedância de aparelho:

$$
\mathsf R_{\rm app}
=
\Pi_{\rm app}^{\rm DtN}
+\Pi_{\rm obj}^{\rm DtN}.
$$

Fisicamente:

- $\Delta_{\rm gap}$ mede isolamento espectral;
- $J_{\rm leak}$ mede quanto uma porta ou perturbação mistura o qubit com modos
  externos;
- $\mathsf R_{\rm app}$ controla preparação, seleção de eixo e leitura.

## 4. Conversão para taxas

Uma vez obtidos $\Delta_{\rm gap}$ e $J_{\rm leak}$:

$$
\epsilon_{\rm leak}
\simeq
\left(
\frac{J_{\rm leak}}{\Delta_{\rm gap}}
\right)^2.
$$

As taxas de relaxação e descoerência devem ser calculadas por acoplamento de
contorno ao banho:

$$
\Gamma_1
\sim
\left\|
J_{\rm th}^{\rm eff}
\right\|^2
S_{\rm bath}(\omega_Q),
\qquad
T_1=\Gamma_1^{-1}.
$$

O mesmo raciocínio vale para $T_2$, incluindo ruído longitudinal de fase.

## 5. Comparação com dispositivos reais

O teste é aceito como comparação fenomenológica se:

1. os parâmetros experimentais forem congelados antes da comparação;
2. $J_{\rm leak}$ e $\Delta_{\rm gap}$ vierem do mesmo operador;
3. $T_1,T_2$ forem derivados do acoplamento de contorno ou recebidos como dado
   experimental declarado;
4. o readout for separado do erro de porta;
5. a tabela final mostrar erro total e fidelidade.

## 6. O que fecharia a Q76 de modo forte

A Q76 passaria de programa promissor para previsão forte se um protótipo real
fosse modelado com:

$$
\Phi_\ast
\text{ estacionário real},
\qquad
K_{\rm phys}
\text{ diagonalizado},
\qquad
\mathsf R_{\rm app}
\text{ calculado por contorno},
$$

e a fidelidade prevista fosse obtida sem usar a fidelidade experimental como
alvo.

Até esse ponto, os scripts da Q76 são ferramentas de requisitos e validação de
consistência, não prova definitiva de hardware.
