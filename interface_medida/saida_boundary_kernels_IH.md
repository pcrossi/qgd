# Saída — kernels de bordo e volume para \(I_H\)

## Objetivo

Comparar, no operador axial reduzido da Q42, a resposta de circulação localizada
no bordo com respostas magnéticas volumétricas. O teste usa
\(\lambda_TA_D=1\) apenas como convenção diagnóstica; não o deriva.

## Operador e observáveis

\[
K_Hu=-\frac1w(wu')'+2u,
\qquad w=e^{-x^2/4}.
\]

Uma fonte unitária é aplicada fracamente no bordo \(x=0\). Calculam-se

\[
C_{\rm resp}=u(0),
\qquad
Z_H=\frac{\int w(x)i_H(x)u(x)\,dx}{u(0)}.
\]

Foram usados um kernel uniforme normalizado e um kernel localizado de largura
\(0.4\), também normalizado.

## Limites numéricos

Na malha \(N=6400\):

| Robin | \(C_{\rm resp}\) | \(Z_{\rm uniforme}\) | \(Z_{\rm local}\) | \(E_{\min}\) |
|---:|---:|---:|---:|---:|
| 0 | 0.75225248 | 0.37500015 | 0.70197714 | 0.6646705 |
| 1 | 0.42930599 | 0.37500015 | 0.70197714 | 1.1646705 |
| 5 | 0.15799433 | 0.37500015 | 0.70197714 | 3.1646705 |

Entre \(N=3200\) e \(N=6400\), as variações máximas foram

\[
|\Delta C_{\rm resp}|<8.9\times10^{-7},\quad
|\Delta Z_{\rm uniforme}|<4.4\times10^{-7},\quad
|\Delta Z_{\rm local}|<1.2\times10^{-6}.
\]

Os resíduos lineares ficaram abaixo de \(1.8\times10^{-12}\).

## Interpretação

Robin controla a suscetibilidade de bordo: aumentar o coeficiente reduz
\(u(0)\) e eleva o custo energético. Porém, não altera o perfil normalizado
nem \(Z_H\) neste modelo linear. Em contraste, trocar o kernel magnético muda
\(Z_H\) de aproximadamente \(0.375\) para \(0.702\).

Se a circulação topológica for \(C_{1/2}=1/2\), então

\[
I_H=\frac12Z_H.
\]

Esses dois kernels diagnósticos dariam, respectivamente,

\[
I_H\simeq0.187500,
\qquad
I_H\simeq0.350989.
\]

Portanto, \(I_H=1/2\) não decorre apenas da circulação. Ele requer \(Z_H=1\),
isto é, uma identidade de localização/transgressão entre o traço topológico e
o acoplamento volumétrico.

## Status científico

O cálculo numérico está convergido como diagnóstico do operador reduzido. A
previsão física continua condicionada à derivação, pela ação oficial, de:

1. soldagem fase--torção \(\lambda_T\);
2. normalização geométrica \(A_D\);
3. kernel magnético físico \(w_H\ell_B\);
4. identidade de localização, caso a teoria imponha \(Z_H=1\).

Script reprodutível: `interface_medida/test_boundary_kernels_IH.py`.
