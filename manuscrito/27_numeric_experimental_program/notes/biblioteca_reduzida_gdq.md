---
title: "Nota — Biblioteca reduzida GDQ"
---

# Nota — Biblioteca reduzida GDQ

Esta nota documenta os blocos reduzidos reutilizáveis usados nos scripts do
programa numérico. Eles são ferramentas de verificação e prototipagem. Não são
nova ação física e não substituem a Hessiana completa da GDQ.

## 1. DtN em intervalo massivo

Considere o operador reduzido:

$$
K_{\rm red}
=
-\frac{d^2}{ds^2}
+\lambda_{\rm eff}^2
$$

em $s\in[0,L]$, com:

$$
\varphi(0)=\varphi_0,
\qquad
\varphi(L)=0.
$$

A solução estacionária é:

$$
\varphi(s)
=
\varphi_0
\frac{\sinh(\lambda_{\rm eff}(L-s))}
{\sinh(\lambda_{\rm eff}L)}.
$$

O momento normal no bordo $s=0$ é:

$$
-\varphi'(0)
=
\lambda_{\rm eff}\coth(\lambda_{\rm eff}L)\,\varphi_0.
$$

Logo, o operador DtN reduzido é:

$$
\mathsf R_{\rm DtN}
=
\lambda_{\rm eff}\coth(\lambda_{\rm eff}L).
$$

Esse bloco aparece quando um detector, parede ou canal material é aproximado
por um modo linear com comprimento efetivo $L$ e rigidez $\lambda_{\rm eff}$.

## 2. Complemento de Schur

Para uma Hessiana finita separada em bordo $\partial$ e interior $I$:

$$
K
=
\begin{pmatrix}
K_{\partial\partial} & K_{\partial I}\\
K_{I\partial} & K_{II}
\end{pmatrix},
$$

a eliminação variacional do interior dá:

$$
K_{\rm eff}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

Essa fórmula é a versão discreta do cálculo DtN acima. O sinal negativo é
importante: graus internos relaxáveis reduzem a rigidez aparente do bordo.

## 3. Resposta quadrática

Se uma fonte clássica impõe uma diferença de contorno $\Delta_\partial$ e a
impedância efetiva é $\mathsf R$, o custo quadrático é:

$$
E_{\rm resp}
=
\frac12
\langle \Delta_\partial,\mathsf R\Delta_\partial\rangle.
$$

Em problemas de detector, esse custo define o expoente de perda de coerência:

$$
\Gamma_{\rm det}
=
\frac12
\langle \Delta_\partial,\mathsf R_{\rm det}\Delta_\partial\rangle.
$$

Então a interferência reduzida recebe:

$$
V_{\rm out}
=
V_{\rm in}e^{-\Gamma_{\rm det}}.
$$

## 4. Densidade de duas alternativas

Para duas intensidades reduzidas $I_1$ e $I_2$, fase relativa $\varphi$ e
amortecimento $\Gamma$, a densidade observada é:

$$
\rho
=
I_1+I_2
+2e^{-\Gamma}\sqrt{I_1I_2}\cos\varphi.
$$

Esse bloco não postula colapso. Ele representa a resposta efetiva do detector
depois de eliminar seus graus internos.

## 5. Uso correto

Esses blocos podem ser usados quando:

- o background já foi fixado ou reduzido;
- a fonte clássica do aparelho foi declarada;
- a Hessiana completa foi aproximada por um canal linear controlado;
- a comparação é classificada como estrutural, fenomenológica ou metrológica,
  conforme o caso.

Eles não devem ser usados para declarar uma previsão cega se
$\lambda_{\rm eff}$, $L$ ou a fonte foram escolhidos depois de olhar o alvo.
