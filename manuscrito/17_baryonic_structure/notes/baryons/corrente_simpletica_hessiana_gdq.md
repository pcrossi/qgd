---
title: "Corrente simplética da Hessiana oficial"
---

# Corrente simplética da Hessiana oficial

## 1. Enunciado

Esta nota preserva a construção correta usada para normalizar modos de
cirurgia, decaimento e canais bariônicos.

A corrente de continuidade de Noether e a corrente simplética da Hessiana são
relacionadas, mas não são a mesma coisa:

$$
\nabla_A J_\theta^A=0
$$

é a conservação da fase global, enquanto

$$
\nabla_A\omega^A(\delta_1\Phi,\delta_2\Phi)=0
$$

é a conservação bilinear da Hessiana linearizada.

## 2. Variáveis reais

Escreva

$$
f=\sigma+i\theta,
\qquad
\sigma=-\log\rho,
\qquad
\theta=\frac{S_R}{\hbar}.
$$

Em um corte causal fixo, a densidade local da ação oficial tem a forma

$$
\mathcal L_z
=
\frac{\hbar}{\Lambda_C^2}
\sqrt g\,\mathcal U
\left[
\tau
\left(
\mathcal R
+
|\nabla\sigma|^2
+
|\nabla\theta|^2
\right)
+
\sigma
-
4
\right],
$$

onde $4$ é $n=\dim_{\mathbb C}M$ no bulk local oficial.

## 3. Potencial pré-simplético

Para uma variação geral,

$$
\delta\mathcal L_z
=
\sqrt g
\left[
\mathcal E_I\delta\Phi^I
+
\nabla_A\Theta_z^A(\Phi;\delta\Phi)
\right].
$$

Se $h^{AB}=\delta g^{AB}$ e $h=g_{AB}h^{AB}$, a parte de curvatura ponderada
contribui com

$$
\begin{aligned}
\Theta_{g,z}^A
=
\frac{\hbar\tau}{\Lambda_C^2}
\big[
&\mathcal U(\nabla_Bh^{AB}-\nabla^Ah)\\
&-(\nabla_B\mathcal U)h^{AB}
+(\nabla^A\mathcal U)h
\big].
\end{aligned}
$$

A parte densidade--fase contribui com

$$
\Theta_{f,z}^A
=
\frac{2\hbar\tau}{\Lambda_C^2}
\mathcal U
\left(
\nabla^A\sigma\,\delta\sigma
+
\nabla^A\theta\,\delta\theta
\right).
$$

Assim,

$$
\Theta_z^A=\Theta_{g,z}^A+\Theta_{f,z}^A.
$$

## 4. Corrente simplética

Para duas perturbações,

$$
\omega_z^A(\Phi;\delta_1\Phi,\delta_2\Phi)
=
\delta_1\Theta_z^A(\Phi;\delta_2\Phi)
-
\delta_2\Theta_z^A(\Phi;\delta_1\Phi).
$$

Antissimetrizando a segunda variação da ação,

$$
\nabla_A\omega_z^A
=
\delta_1\mathcal E_I\,\delta_2\Phi^I
-
\delta_2\mathcal E_I\,\delta_1\Phi^I.
$$

Logo, em um background que satisfaz as equações oficiais, e para
perturbações que satisfazem a Hessiana linearizada,

$$
\nabla_A\omega_z^A=0.
$$

Antes de usar essa corrente como produto interno físico, devem ser removidas
as direções de gauge/difeomorfismo e impostos os vínculos de fluxo, carga e
orientação APS.

## 5. Setor de fase e continuidade

A simetria global

$$
\theta\mapsto\theta+\alpha
$$

fornece a corrente de Noether

$$
J_\theta^A
=
\frac{2\hbar\tau}{\Lambda_C^2}
\mathcal U\nabla^A\theta
=
\frac{2\tau}{\Lambda_C^2}
\mathcal U\nabla^A S_R.
$$

A equação da fase dá

$$
\nabla_AJ_\theta^A=0.
$$

Depois da reconstrução do tempo físico, essa conservação assume a forma local
de continuidade no laboratório:

$$
\partial_t\mathcal U+\nabla_i(\mathcal U v^i)=0.
$$

## 6. Forma de Green da Hessiana

Para um bloco físico escrito como

$$
L\psi
=
-\mathcal U^{-1}
\nabla_A
\left(
\mathcal U A^{AB}\nabla_B\psi
\right)
+
V\psi,
$$

a identidade de Green é

$$
\nabla_A j^A(\psi_1,\psi_2)
=
\mathcal U
\left(
\psi_2 L\psi_1-\psi_1L\psi_2
\right),
$$

com

$$
j^A(\psi_1,\psi_2)
=
\mathcal U A^{AB}
\left(
\psi_1\nabla_B\psi_2
-
\psi_2\nabla_B\psi_1
\right).
$$

Para dois modos do kernel, $L\psi_1=L\psi_2=0$, temos

$$
\nabla_Aj^A=0.
$$

Essa é a forma prática usada para normalizar modos de saída, pois o fluxo
independe da hipersuperfície de corte.

## 7. Pullback causal

A corrente física de contorno é obtida por

$$
\omega_\gamma^A
=
\oint_\gamma
\omega_z^A
\frac{d\tau}{\tau}.
$$

Na representação de Laurent, a orientação positiva do contorno seleciona o
coeficiente adequado da expansão causal:

$$
\omega_\gamma^A
=
\frac{2\pi i}{(4\pi)^4}
[z^3]\widehat\omega^A(z),
$$

onde $\widehat\omega^A$ inclui os pesos de pullback não exibidos.

## 8. Normalização dos modos

Após reconstruir a seção física, define-se

$$
(\Psi_a,\Psi_b)_\Sigma
=
i
\int_\Sigma
n_A
\omega_\gamma^A(\overline{\Psi_a},\Psi_b)
d\Sigma.
$$

A orientação APS seleciona o sinal de fluxo dos modos de saída. No setor
físico,

$$
(\Psi_a,\Psi_b)_\Sigma=\delta_{ab}.
$$

Isso remove a liberdade de reescalar separadamente as pernas do processo, mas
não substitui o cálculo do vértice físico nem do Green transversal.

## 9. Status

- potencial pré-simplético: derivado da ação oficial;
- corrente simplética: derivada por antissimetrização da segunda variação;
- corrente de Noether: derivada no setor de fase;
- forma de Green: derivada para bloco físico da Hessiana;
- normalização APS: definida no setor reconstruído;
- avaliação completa em modos bariônicos: depende dos modos físicos da
  Hessiana de superfície.

## 10. Verificação simbólica

O script `scripts/verificar_corrente_green_hessiana.py` verifica a identidade
de Green para um operador de Sturm--Liouville ponderado representativo do
bloco físico da Hessiana.
