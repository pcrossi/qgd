---
title: "Detector ôhmico, filtragem causal e captura Born"
---

# Detector ôhmico, filtragem causal e captura Born

Esta nota preserva a parte positiva da teoria de interface: um aparelho aberto
gera dissipação e informação por seu próprio canal macroscópico. A construção
é efetiva e condicional a uma redução quadrática da Hessiana física; ela não
altera a ação oficial da GDQ.

## 1. Canal aberto do aparelho

Considere uma coordenada de saída $x\ge0$ no aparelho e um modo físico
normalizado $y(x,t)T_y$ obtido por projeção modal da Hessiana física do
background macroscópico. A forma quadrática reduzida é:

$$
S_{\rm canal}^{(2)}
=
\frac{\zeta_A}{2}
\int dt\int_0^\infty dx
\left[
\frac1{c_A^2}(\partial_ty)^2
-(\partial_xy)^2
\right].
$$

Os coeficientes vêm de produtos internos da Hessiana projetada:

$$
\frac{\zeta_A}{c_A^2}
=
\langle T_y,K_tT_y\rangle_{\mathcal U_*},
\qquad
\zeta_A
=
\langle T_y,K_xT_y\rangle_{\mathcal U_*}.
$$

Portanto $\zeta_A$ e $c_A$ são dados do aparelho concreto. Eles não são
constantes fundamentais.

## 2. DtN retardado

A equação do canal é:

$$
\frac1{c_A^2}\partial_t^2y-\partial_x^2y=0.
$$

Com $y(0,t)=X(t)$ e condição de radiação de saída no infinito, escreva:

$$
y(x,t)
=
\int\frac{d\omega}{2\pi}
e^{-i\omega t}y_\omega(x).
$$

A solução causal de saída é:

$$
y_\omega(x)=X_\omega e^{i\omega x/c_A}.
$$

Logo:

$$
\partial_xy_\omega(0)
=
\frac{i\omega}{c_A}X_\omega.
$$

O momento normal do canal é:

$$
\Pi_A(\omega)
=
-\zeta_A\partial_xy_\omega(0).
$$

Assim, o operador Dirichlet-to-Neumann retardado é:

$$
\Lambda_A^{\rm ret}(\omega)
=
-i\omega\frac{\zeta_A}{c_A}.
$$

Definindo:

$$
\gamma_A=\frac{\zeta_A}{c_A}>0,
$$

temos:

$$
\Lambda_A^{\rm ret}(\omega)
=
-i\gamma_A\omega.
$$

Essa é a origem geométrica do atrito ôhmico. Ele não foi inserido manualmente;
ele é a resposta de um domínio aberto com condição causal de radiação.

## 3. Energia e mobilidade causal

A energia do canal é:

$$
E_A
=
\frac{\zeta_A}{2}
\int_0^\infty dx
\left[
\frac1{c_A^2}(\partial_ty)^2
+(\partial_xy)^2
\right].
$$

Para ondas de saída, a potência média irradiada pela interface é:

$$
\mathcal P_{\rm out}
=
\gamma_A\dot X^2\ge0.
$$

No limite superamortecido, a mobilidade do ponteiro é:

$$
\mathcal M_X=\gamma_A^{-1}.
$$

## 4. Ponteiro condicionado

Para dois canais $\kappa=\pm1$, use o potencial reduzido:

$$
U_\kappa(X)
=
-\frac A2X^2+\frac B4X^4-g_X\kappa X.
$$

Perto de um registro estável $X_\kappa^*$:

$$
U_\kappa'(X_\kappa^*)=0,
\qquad
k_\kappa=U_\kappa''(X_\kappa^*)>0.
$$

A equação linearizada do ponteiro é:

$$
M_X\ddot x+\gamma_A\dot x+k_\kappa x=\xi_A(t).
$$

Em temperatura $T_A$, a relação de flutuação--dissipação clássica é:

$$
\langle\xi_A(t)\xi_A(t')\rangle
=
2\gamma_Ak_BT_A\,\delta(t-t').
$$

## 5. Registro normalizado e taxa informacional

Depois de branquear o ruído do aparelho, o registro satisfaz:

$$
dY_t
=
2\sqrt{\Gamma(t)}\,\kappa\,dt+dW_t.
$$

Aqui $\Gamma(t)$ é a taxa informacional física extraída do kernel espectral do
aparelho. Para o detector ôhmico superamortecido simples:

$$
\Gamma
=
\frac{g_X^2}{8\gamma_Ak_BT_A}.
$$

Essa fórmula mostra o papel físico dos parâmetros: maior acoplamento aumenta
a informação; maior atrito ou temperatura reduzem a taxa de discriminação.

## 6. Filtragem e martingal

Defina:

$$
p_t
=
\Pr(\kappa=+1\mid\mathcal F_t^Y),
$$

onde $\mathcal F_t^Y$ é a filtração gerada pelo registro até $t$. A inovação é:

$$
d\widetilde W_t
=
dY_t
-2\sqrt{\Gamma(t)}(2p_t-1)dt.
$$

A equação de filtragem para dois sinais é:

$$
dp_t
=
4\sqrt{\Gamma(t)}\,p_t(1-p_t)d\widetilde W_t.
$$

Como não há termo de drift:

$$
\mathbb E[p_t]=p_0.
$$

Logo $p_t$ é martingal limitado. Se a informação acumulada:

$$
\mathcal I(t)=\int_0^t\Gamma(s)ds
$$

diverge, a razão de verossimilhança separa os dois canais e:

$$
p_\infty\in\{0,1\}
\quad\text{quase certamente}.
$$

Como $\mathbb E[p_\infty]=p_0$, obtemos:

$$
\Pr(p_\infty=1)=p_0.
$$

Portanto, a dinâmica do aparelho converte o peso inicial de Born em frequência
de registros sem postular colapso.

## 7. Status

O resultado é um teorema efetivo condicional:

$$
\boxed{
\text{canal QND}
+\Gamma(t)\ge0
+\mathcal I(\infty)=\infty
+\text{registros estáveis}
\Longrightarrow
\text{captura assintótica com frequência }p_0.
}
$$

O cálculo de $\zeta_A$, $c_A$, $g_X$ e $T_A$ para um aparelho real pertence à
metrologia do aparelho. Esses dados entram como background, material e
contorno; não são alterações da ação oficial.
