---
title: "Hessiana, projetores e resposta de interface"
---

# Hessiana, projetores e resposta de interface

## 1. Enunciado

Esta nota registra a construção que deve ser usada sempre que o capítulo falar
de aparelho real. O efeito ideal de holonomia é topológico. A correção de
aparelho real é variacional.

A cadeia correta na GDQ é:

$$
J_{\rm app}^{\rm clássico}
\to
\Phi_\ast
\to
K_{\rm GDQ}
\to
P_{\rm phys}^{\dagger}K_{\rm GDQ}P_{\rm phys}
\to
\mathsf R_{\rm app}
\to
\text{observável}.
$$

Aqui $\Phi=(g,J,H,f)$ denota os campos geométricos relevantes: métrica
Hermitiana, estrutura complexa, torção de Bismut e potencial/dilatão complexo.

## 2. Background com fonte clássica

O aparelho entra como dado clássico de contorno ou fonte externa. Para o
solenoide, essa fonte representa a corrente macroscópica, material, blindagem e
geometria do tubo.

Não se altera a ação oficial. Resolve-se a condição estacionária com fonte:

$$
\left.
\frac{\delta}{\delta\Phi}
\left(
\mathcal S_{\rm GDQ}
+
\mathcal S_{\rm app}
\right)
\right|_{\Phi_\ast}
=
0.
$$

A fonte $\mathcal S_{\rm app}$ não é novo termo fundamental. Ela especifica o
aparelho que define o experimento, como uma condição de contorno física.

## 3. Hessiana oficial

No background $\Phi_\ast$, a Hessiana é:

$$
K_{\rm GDQ}
=
\left.
\frac{\delta^2\mathcal S_{\rm GDQ}}
{\delta\Phi\,\delta\Phi}
\right|_{\Phi_\ast}.
$$

Em coordenadas locais, uma flutuação é escrita:

$$
\delta\Phi
=
(\delta g,\delta J,\delta H,\delta f).
$$

A segunda variação tem a forma:

$$
\delta^2\mathcal S_{\rm GDQ}
=
\langle
\delta\Phi,
K_{\rm GDQ}\delta\Phi
\rangle.
$$

O produto interno contém a medida ponderada da GDQ:

$$
d\mu_\ast
=
\mathcal U_\ast\sqrt{\det g_\ast}\,d^{2n}z\,\frac{d\tau}{\tau}.
$$

## 4. Remoção dos modos não físicos

Nem toda flutuação de $\Phi$ é física. Existem direções que representam
mudança de carta, calibre, reparametrização ou violação dos vínculos de carga e
fluxo.

Definimos o subespaço físico por:

$$
\mathcal V_{\rm phys}
=
\ker C_Q
\cap
\ker C_F
\cap
\mathcal G^\perp.
$$

Aqui $C_Q$ é o vínculo de carga, $C_F$ é o vínculo de fluxo e $\mathcal G$ é o
subespaço tangente às órbitas de calibre.

O projetor ortogonal ponderado é:

$$
P_{\rm phys}:
\mathcal V
\to
\mathcal V_{\rm phys}.
$$

A Hessiana física é:

$$
K_{\rm phys}
=
P_{\rm phys}^{\dagger}
K_{\rm GDQ}
P_{\rm phys}.
$$

Essa é a quantidade que pode ser diagonalizada ou reduzida à fronteira.

## 5. Separação fronteira-interior

Dividimos as flutuações físicas em variáveis de fronteira $Y$ e variáveis
internas $I$:

$$
\delta\Phi_{\rm phys}
=
(\delta\Phi_Y,\delta\Phi_I).
$$

Então:

$$
K_{\rm phys}
=
\begin{pmatrix}
K_{YY} & K_{YI}\\
K_{IY} & K_{II}
\end{pmatrix}.
$$

Para uma perturbação imposta na fronteira pelo aparelho, o interior relaxa pela
equação linear:

$$
K_{II}\delta\Phi_I
=
-
K_{IY}\delta\Phi_Y.
$$

Quando $K_{II}$ tem gap positivo no setor físico, a solução é:

$$
\delta\Phi_I
=
-
K_{II}^{-1}K_{IY}\delta\Phi_Y.
$$

Substituindo na forma quadrática, obtemos:

$$
\mathsf R_{\rm app}
=
K_{YY}
-
K_{YI}K_{II}^{-1}K_{IY}.
$$

Essa é a matriz DtN/Schur: ela transforma deformação de fronteira em resposta
normal efetiva.

## 6. Aplicação ao Aharonov--Bohm real

No AB ideal:

$$
A_{\rm eff}
=
A_{\rm harm}.
$$

No solenoide real:

$$
A_{\rm eff}
=
A_{\rm harm}
+
\delta A_{\rm surf}.
$$

A correção $\delta A_{\rm surf}$ é determinada por $\mathsf R_{\rm sol}$ e
pela fonte clássica do aparelho. A fase é:

$$
\Delta\varphi
=
\frac{q}{\hbar c}
\oint_\gamma A_{\rm eff}.
$$

Logo:

$$
\Delta\varphi
=
\frac{q\Phi}{\hbar c}
+
\frac{q}{\hbar c}
\oint_\gamma\delta A_{\rm surf}.
$$

O primeiro termo é topológico. O segundo termo é metrológico.

## 7. Condição de fechamento forte

Para uma previsão metrológica de um solenoide concreto, ainda é necessário
fornecer:

1. geometria do aparelho;
2. corrente macroscópica;
3. material e blindagem;
4. domínio e fronteira;
5. background $\Phi_\ast$;
6. projetor $P_{\rm phys}$;
7. espectro de $K_{II}$;
8. cálculo de $\mathsf R_{\rm sol}$;
9. integral de $\delta A_{\rm surf}$ no caminho experimental.

Sem esses dados, o capítulo fecha o efeito ideal e a forma da correção, mas não
um aparelho real específico.
