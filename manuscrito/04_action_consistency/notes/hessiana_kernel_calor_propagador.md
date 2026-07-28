---
title: "Hessiana, kernel de calor e propagador modificado"
---

# Hessiana, kernel de calor e propagador modificado

Esta nota registra a dedução técnica do fator gaussiano que aparece em
propagadores efetivos da GDQ. O ponto central é separar três objetos:

1. a Hessiana da ação oficial;
2. o gerador normalizado do semigrupo de calor;
3. o propagador espectral efetivo.

## 1. Segunda variação da ação oficial

Seja:

$$
\Phi_\ast
=
(g_\ast,f_\ast,\bar f_\ast)
$$

um background admissível, isto é, uma configuração que satisfaz as equações de
bulk, os vínculos e os contornos do problema. Para uma perturbação física
$\eta$:

$$
\Phi
=
\Phi_\ast+\varepsilon\eta.
$$

Como $\Phi_\ast$ é estacionário:

$$
\delta\mathcal S_{\rm GDQ}[\Phi_\ast;\eta]=0.
$$

A ordem quadrática é:

$$
\mathcal S_{\rm GDQ}^{(2)}
=
\frac12
\langle
\eta,
\mathcal O_{\rm Hess}^{(2)}
\eta
\rangle_{\mathcal U_\ast}.
$$

Aqui $\mathcal O_{\rm Hess}^{(2)}$ é a Hessiana bruta. Ela ainda inclui
fatores de escala provenientes da ação, inclusive o fator de fluxo $\tau$.

## 2. O gerador correto do calor

A ação oficial contém o bloco:

$$
\tau
\left(
\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f
\right).
$$

Por isso, no setor quadrático de segunda ordem, a Hessiana aparece na forma:

$$
\mathcal O_{\rm Hess}^{(2)}
=
\tau L_{\rm GDQ}^{(2)}.
$$

O operador que gera o semigrupo de calor não é
$\mathcal O_{\rm Hess}^{(2)}$ novamente multiplicado por $\tau$. O gerador
normalizado é:

$$
L_{\rm GDQ}^{(2)}
:=
\tau^{-1}
\mathcal O_{\rm Hess}^{(2)}.
$$

Logo o kernel de calor efetivo é:

$$
K_\tau
=
e^{-\tau L_{\rm GDQ}^{(2)}}.
$$

Esse ponto evita o erro dimensional:

$$
e^{-\tau(\tau L)}
=
e^{-\tau^2L},
$$

que produziria amortecimento de ordem errada no momento.

## 3. Limite plano

No limite plano euclidiano, para um modo escalar reduzido:

$$
L_{\rm GDQ}^{(2)}
\to
p_E^2+m^2.
$$

Então:

$$
e^{-\tau L_{\rm GDQ}^{(2)}}
\to
e^{-\tau(p_E^2+m^2)}.
$$

Se a massa for mantida no denominador do propagador e o amortecimento for
associado ao setor cinético:

$$
G_\tau(p_E)
=
\frac{e^{-\tau p_E^2}}{p_E^2+m^2}.
$$

Com:

$$
\widehat\Lambda_\tau
=
\tau^{-1/2},
$$

obtém-se:

$$
G_\tau(p_E)
=
\frac{e^{-p_E^2/\widehat\Lambda_\tau^2}}{p_E^2+m^2}.
$$

Assim, o gaussiano não é inserido à mão. Ele é o limite plano do semigrupo de
calor da Hessiana normalizada.

## 4. Polos e fantasmas

Suponha uma decomposição espectral:

$$
L_{\rm GDQ}^{(2)}\psi_n
=
\lambda_n\psi_n.
$$

No setor invertível:

$$
G_\tau\psi_n
=
\frac{e^{-\tau\lambda_n}}{\lambda_n}
\psi_n.
$$

Como:

$$
e^{-z}\ne0
$$

para todo $z$ finito, o numerador inteiro não cria zeros nem polos adicionais.
Os polos são aqueles do inverso:

$$
\lambda_n=0.
$$

No limite plano:

$$
p_E^2+m^2=0.
$$

Portanto, o amortecimento gaussiano não introduz fantasmas por si só. A
ausência completa de fantasmas no setor métrico/gauge ainda exige:

1. projetor físico que remova modos de gauge;
2. domínio auto-adjunto;
3. positividade do setor físico;
4. reconstrução lorentziana causal.

## 5. Setor escalar reduzido

Para a redução:

$$
S[f]
=
\tau
\int
\left(
R_0+|\nabla f|^2
\right)
e^{-f}dV,
\qquad
f=f_0+\varphi,
$$

a expansão até segunda ordem produz:

$$
S_\varphi^{(2)}
=
\tau
\int e^{-f_0}
\left[
|\nabla\varphi|^2
-2\varphi\nabla f_0\cdot\nabla\varphi
+\frac12
\left(
R_0+|\nabla f_0|^2
\right)
\varphi^2
\right]dV.
$$

No produto interno ponderado:

$$
\langle u,v\rangle_{f_0}
=
\int uv\,e^{-f_0}dV,
$$

após integração por partes:

$$
\mathcal O_{\rm Hess,\varphi}^{(2)}
=
2\tau
\left[
-\Delta_{f_0}
+\Delta f_0
+\frac12R_0
-\frac12|\nabla f_0|^2
\right].
$$

Portanto:

$$
L_\varphi
=
2
\left[
-\Delta_{f_0}
+\Delta f_0
+\frac12R_0
-\frac12|\nabla f_0|^2
\right].
$$

Na ação oficial completa, a medida:

$$
\mathcal U
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}
$$

e o termo:

$$
\frac{f+\bar f}{2}-n
$$

adicionam potenciais e acoplamentos mistos. Portanto esta expressão é a
redução escalar local, não a Hessiana total.

## 6. Blocos físicos

Com flutuações escalares e métricas, a forma geral é:

$$
L_{\rm GDQ}^{(2)}
=
\begin{pmatrix}
L_\varphi & L_{\varphi h}\\
L_{h\varphi} & L_{h,{\rm phys}}
\end{pmatrix}.
$$

O setor físico requer:

$$
L_{h,{\rm phys}}
=
\Pi_{\rm phys}L_h\Pi_{\rm phys}.
$$

Em gauge Hermitiano--DeTurck ponderado, uma condição típica é:

$$
\mathcal F_\nu(h)
=
\nabla^\mu h_{\mu\bar\nu}
-\frac12\nabla_{\bar\nu}{\rm tr}_g h
-h_{\mu\bar\nu}\nabla^\mu f_0
=
0.
$$

O propagador completo é:

$$
G_\tau
=
e^{-\tau L_{\rm GDQ}^{(2)}}
\left(
L_{\rm GDQ}^{(2)}
\right)^{-1},
$$

no domínio físico.

## 7. Continuação lorentziana

Não se deve fazer a substituição ingênua:

$$
e^{-p_E^2/\widehat\Lambda_\tau^2}
\mapsto
e^{+p_h^2/\widehat\Lambda_\tau^2}.
$$

A rota correta é:

$$
\text{kernel euclidiano}
\to
\text{funções de Schwinger refletidamente positivas}
\to
\text{reconstrução OS/Sudarshan}
\to
G_{\rm ret}.
$$

As condições de Osterwalder--Schrader mostram por que funções euclidianas não
produzem automaticamente uma teoria lorentziana: covariância, simetria,
positividade por reflexão e propriedades de cluster fazem parte das hipóteses
de reconstrução.^[[[../../ref/Osterwalder and Schrader 1973 - Axioms for Euclidean Green Functions|Osterwalder--Schrader 1973, axiomas E0--E4]]].

O critério causal final é:

$$
\operatorname{supp}G_{\rm ret}
\subseteq
J_h^+.
$$

Esse é um critério de reconstrução física, não uma manipulação algébrica do
expoente.
