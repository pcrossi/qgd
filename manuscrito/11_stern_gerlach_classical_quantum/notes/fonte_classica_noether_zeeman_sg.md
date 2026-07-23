---
title: "Fonte clássica e Noether--Zeeman"
---

# Fonte clássica e Noether--Zeeman

Esta nota preserva a rota correta para o acoplamento magnético em
Stern--Gerlach. O campo do aparelho é fonte clássica dada; o objeto responde
por sua corrente geométrica e por sua Hessiana física. Não se insere o operador
de Pauli como interação fundamental.

## 1. Fonte clássica do aparelho

O eletroímã é descrito no espaço físico por uma corrente clássica prescrita:

$$
j_A^\mu,
\qquad
\nabla_\mu j_A^\mu=0.
$$

Ela determina:

$$
F_A=dA_A,
\qquad
dF_A=0,
\qquad
d{*F_A}=*j_A.
$$

Na região do experimento:

$$
\mathbf B_A=\nabla\times\mathbf A_A,
\qquad
\nabla|\mathbf B_A|\ne0.
$$

A GDQ não deve prever qual corrente o experimentalista escolheu. Ela deve
prever a resposta do sóliton ao campo externo fornecido.

## 2. Corrente geométrica do objeto

O objeto possui uma corrente geométrica escrita como divergência de uma
densidade antissimétrica:

$$
j_Q^\mu
=
\nabla_\alpha\mathcal T_Q^{\alpha\mu}.
$$

A densidade $\mathcal T_Q$ é a projeção spin--torção do setor de Bismut/Cartan.
Usando o acoplamento clássico de corrente:

$$
S_{\rm int}^{(1)}
=
\frac q c
\int A_{A\mu}j_Q^\mu\,d\mu,
$$

e integrando por partes:

$$
S_{\rm int}^{(1)}
=
\frac q{2c}
\int
\mathcal T_Q^{\mu\nu}F^{\rm app}_{\mu\nu}\,d\mu
+S_{\partial}^{A\mathcal T}.
$$

O sinal global depende de orientação e convenção para $F=dA$. A estrutura
bilinear gauge-invariante não depende dessa escolha.

No bulk:

$$
S_{\rm int}[\Phi;F_A]
=
\frac q{2c}
\int_{\Omega_{\rm SG}}
\chi_{\rm SG}\,
\mathcal T^{AB}[\Phi]F^{\rm app}_{AB}\,d\mu_\Phi.
$$

Essa é uma fonte de sonda. Ela não é um termo novo da ação oficial.

## 3. Variação e operador de interface

Para uma perturbação $\delta\Phi$:

$$
\delta S_{\rm int}
=
\frac q{2c}
\int_{\Omega_{\rm SG}}\chi_{\rm SG}
\left[
\left(D_\Phi\mathcal T\cdot\delta\Phi\right)^{AB}F^{\rm app}_{AB}
+\mathcal T^{AB}F^{\rm app}_{AB}\delta\log d\mu_\Phi
\right]d\mu_\Phi.
$$

Logo, no produto interno da medida oficial:

$$
J_A
=
-\frac q{2c}
\left(D_\Phi\mathcal T\right)^*
(\chi_{\rm SG}F_A)
+J_{\rm medida}.
$$

A equação linearizada é:

$$
\mathbb H_{\rm GDQ}^{\rm phys}\delta\Phi
=
J_A.
$$

Na interface, separando DtN do objeto e Hessiana do aparelho:

$$
(\Lambda_Q+\mathsf R_A)\delta\varphi
=
\delta J_A.
$$

Robin homogênea só aparece quando a fonte já foi absorvida no background
estacionário ou quando se estudam flutuações sem nova variação externa.

## 4. Redução ao módulo de Hopf

O módulo livre do spin é:

$$
\mathcal O\simeq SU(2)/U(1)\simeq S^2\simeq\mathbb{CP}^1.
$$

No setor axial, a densidade antissimétrica é dual a um vetor:

$$
t_i(P)
=
\frac12\epsilon_{ijk}\mathcal T^{jk}(P).
$$

Isotropia e equivariância implicam:

$$
t_i(P)=t_H n_i(P).
$$

Como:

$$
\frac12\mathcal T^{ij}F^{\rm app}_{ij}
=
\mathbf t(P)\cdot\mathbf B_A,
$$

a redução axial fornece a forma Zeeman:

$$
E_{\rm int}
=
-\boldsymbol\mu_{\rm GDQ}\cdot\mathbf B_A.
$$

As matrizes $\sigma$ e os projetores $P_{\mathbf n}^{\pm}$ aparecem apenas
depois de restringir esse módulo ao espaço spinorial efetivo. Eles não são
inseridos na ação fundamental.

## 5. Teorema de Noether--Zeeman

A ação oficial é invariante sob deslocamento constante da fase:

$$
f\mapsto f+i\varepsilon,
\qquad
\bar f\mapsto\bar f-i\varepsilon.
$$

Promovendo $\varepsilon$ localmente, obtém-se a corrente de Noether:

$$
J_{\rm N}^A
\propto
i\tau\mathcal U
\left(
g^{A\bar B}\partial_{\bar B}\bar f
-g^{B\bar A}\partial_Bf
\right),
\qquad
\nabla_AJ_{\rm N}^A=0.
$$

No defeito, sua projeção rotacional define:

$$
\boldsymbol{\mathcal C}[\Phi]
=
\int_\Sigma\boldsymbol J_{\rm N}\cdot d\boldsymbol\Sigma.
$$

O setor elementar é:

$$
\boldsymbol C
=
\pm\frac\hbar2\boldsymbol n.
$$

Imponha o vínculo de circulação por multiplicador:

$$
\mathscr I[\Phi,\boldsymbol\lambda;\boldsymbol C,\boldsymbol B]
=
\mathcal S_{\rm GDQ}[\Phi]
-\boldsymbol B\cdot\boldsymbol M[\Phi]
-\boldsymbol\lambda\cdot
\left(\boldsymbol{\mathcal C}[\Phi]-\boldsymbol C\right).
$$

Se o campo acopla à mesma corrente conservada que define a circulação:

$$
\boldsymbol M[\Phi]
=
\gamma_0\boldsymbol{\mathcal C}[\Phi]
+\boldsymbol M_\perp[\Phi].
$$

A parte protegida satisfaz:

$$
-\frac{\partial\lambda_i}{\partial B_j}
=
\gamma_0\delta_{ij}.
$$

Portanto a componente mínima tem:

$$
Z_{\rm N}=1.
$$

O momento total pode conter vestido geométrico transversal:

$$
\gamma_{\rm eff}
=
\gamma_0+\Delta\gamma_{\rm geom}.
$$

Com Hessiana vinculada $H_C$, escreva:

$$
\gamma_{\rm eff}
=
\frac{\langle c,H_C^{-1}m\rangle}
{\langle c,H_C^{-1}c\rangle},
$$

onde $c=\delta\mathcal C/\delta\Phi$ e $m=\delta M/\delta\Phi$. Separando
$m=\gamma_0c+m_\perp$:

$$
\Delta\gamma_{\rm geom}
=
\frac{\langle c,H_C^{-1}m_\perp\rangle}
{\langle c,H_C^{-1}c\rangle}.
$$

## 6. Seleção estacionária

Por isotropia, a energia reduzida em campo fraco só pode conter:

$$
E(\boldsymbol C,\boldsymbol B)
=
E_0(C^2)-\gamma_{\rm eff}\boldsymbol C\cdot\boldsymbol B+O(B^2).
$$

Com $|\boldsymbol C|$ fixo:

$$
\delta\boldsymbol C
=
\delta\boldsymbol\theta\times\boldsymbol C.
$$

Logo:

$$
\delta E
=
-\gamma_{\rm eff}\delta\boldsymbol\theta\cdot
(\boldsymbol C\times\boldsymbol B).
$$

A condição estacionária é:

$$
\boldsymbol C\times\boldsymbol B=0.
$$

Assim:

$$
\boldsymbol C_\pm
=
\pm\frac\hbar2\frac{\boldsymbol B}{|\boldsymbol B|},
$$

e:

$$
\boldsymbol F_\pm
=
\pm\gamma_{\rm eff}\frac\hbar2\nabla|\boldsymbol B|.
$$

Esse é o fechamento estrutural do canal Zeeman em Stern--Gerlach. A metrologia
do fator total exige avaliar o vestido geométrico transversal do background
real.
