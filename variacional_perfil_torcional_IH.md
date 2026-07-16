# Problema variacional do perfil torsional e determinação de \(I_H\)

## 1. Objetivo

O momento magnético estrutural foi reduzido a

\[
\mu_{\rm GDQ}
=\frac{q\ell_B}{c}I_H,
\qquad
I_H=\int W_H(r)dV_\perp.
\]

Este documento determina a forma variacional correta para obter o perfil
torsional \(t_H(r)\) e \(I_H\), sem identificar indevidamente:

- a fase \(\Theta(r)\);
- a constante de primeira integral \(J_\Theta\);
- a 3-forma de Bismut \(H\);
- a circulação física do momento;
- o número de Chern de Hopf.

Esses objetos podem estar relacionados, mas o mapa deve ser derivado.

---

## 2. Diagnóstico do background Q42

O ansatz radial da Q42 contém

\[
f_*=F(r)+i\Theta(r)
\]

e a primeira integral

\[
e^{-F}\frac{bc^2}{a}\Theta'=J_\Theta.
\]

Esse resultado controla a corrente da fase imaginária do campo \(f\).

O background cilíndrico posteriormente resolvido possui:

\[
a_{S^3}=2\sqrt\tau,
\qquad
F=\frac{r^2}{4\tau}+\frac12\log\pi,
\]

mas não fornece uma solução não nula de \(H\) ou um potencial de 2-forma
\(\mathcal A\) cuja derivada seja a torção.

Portanto:

\[
\boxed{
J_\Theta\text{ não pode ser usado como amplitude de }H
\text{ sem uma equação constitutiva adicional derivada.}
}

---

## 3. Espaço funcional torsional

Considere o setor axial já selecionado:

\[
\mathcal T_Q(r,P)
=t(r)n^i(P)\Sigma_i^+.
\]

Depois das integrações angulares e internas, a segunda variação torsional
define um produto positivo no setor físico:

\[
\boxed{
\langle t_1,t_2\rangle_K
=\int_{r_c}^{\infty}
t_1(r)\,[K_Ht_2](r)\,w_H(r)dr.
}

Aqui:

- \(K_H\) é o bloco físico da Hessiana torsional;
- \(w_H\) contém a medida oficial e os fatores métricos;
- condições Robin são impostas em \(r_c\);
- regularidade/decadência é imposta no exterior;
- modos de gauge são removidos.

Exige-se:

\[
\boxed{K_H>0}
\]

no complemento dos modos zero.

---

## 4. Funcional de circulação

A quantização topológica deve ser representada por um funcional linear
específico:

\[
\boxed{
\mathcal C_H[t]
=\int_{r_c}^{\infty}c_H(r)t(r)dr
=C_{1/2}.
}

O kernel \(c_H(r)\) depende do mapa entre a torção e a holonomia/circulação
física.

O valor esperado do setor elementar é simbolicamente

\[
C_{1/2}\sim\pi\hbar
\]

na convenção do Capítulo 11, mas a igualdade dimensional exata só pode ser
usada depois que \(c_H\), \(q\) e as unidades de \(t\) forem fixados.

O número de Chern \(c_1=\pm1\) classifica o fibrado de Hopf, mas não substitui
automaticamente \(\mathcal C_H[t]\).

---

## 5. Minimização com vínculo

Considere a energia quadrática

\[
\mathcal E_H[t]
=\frac12\langle t,t\rangle_K.
\]

Minimize-a sob

\[
\mathcal C_H[t]=C_{1/2}.
\]

O funcional aumentado é

\[
\mathcal L[t,\lambda]
=\frac12\langle t,t\rangle_K
-\lambda(\mathcal C_H[t]-C_{1/2}).
\]

A variação fornece

\[
\boxed{K_Ht=\lambda c_H^\sharp,}
\]

onde \(c_H^\sharp\) é o representante do funcional de circulação no produto
de referência.

Assim:

\[
t=\lambda K_H^{-1}c_H^\sharp.
\]

Impondo o vínculo:

\[
\lambda
=\frac{C_{1/2}}
{\mathcal C_H[K_H^{-1}c_H^\sharp]}.
\]

Portanto, o perfil de norma mínima é

\[
\boxed{
t_*(r)
=C_{1/2}
\frac{[K_H^{-1}c_H^\sharp](r)}
{\mathcal C_H[K_H^{-1}c_H^\sharp]}.
}

Esse resultado é exato para a Hessiana quadrática e mostra que a circulação
fixa a amplitude somente depois de conhecidos \(K_H\) e \(c_H\).

---

## 6. Energia mínima do setor

Substituindo \(t_*\):

\[
\boxed{
\mathcal E_H^{\rm min}
=\frac{C_{1/2}^2}
{2\mathcal C_H[K_H^{-1}c_H^\sharp]}.
}

O denominador é a susceptibilidade torsional estática do setor de circulação.

Ele desempenha o mesmo papel de uma capacitância ou indutância geométrica:
quanto maior a susceptibilidade, menor o custo para sustentar a circulação
quantizada.

---

## 7. Avaliação formal de \(I_H\)

Defina o funcional que entra no momento magnético:

\[
\mathcal I_H[t]
=\int i_H(r)t(r)dr,
\]

onde \(i_H(r)\) contém \(\chi_{\rm SG}\mathcal U_*\), a medida transversal e a
projeção usada no acoplamento ao campo.

Então:

\[
I_H=\mathcal I_H[t_*].
\]

Logo:

\[
\boxed{
I_H
=C_{1/2}
\frac{
\mathcal I_H[K_H^{-1}c_H^\sharp]
}
{
\mathcal C_H[K_H^{-1}c_H^\sharp]
}.
}

Essa é a fórmula geral que faltava. Ela separa:

1. quantum topológico \(C_{1/2}\);
2. resposta radial \(K_H^{-1}\);
3. mapa de circulação \(c_H\);
4. mapa de acoplamento magnético \(i_H\).

---

## 8. Quando \(I_H=C_{1/2}\)?

Somente se os dois funcionais forem o mesmo:

\[
\mathcal I_H=\mathcal C_H.
\]

Nesse caso:

\[
I_H=C_{1/2}.
\]

Essa igualdade não é automática. Ela exige que o campo magnético acople
exatamente à mesma combinação de torção que define a circulação quantizada.

Se os kernels forem diferentes, a razão espectral acima produz um fator de
forma geométrico.

---

## 9. Redução de Sturm--Liouville

Num ansatz radial simples, escreva

\[
\boxed{
K_H
=-\frac1{w_H}
\frac d{dr}
\left(p_H\frac d{dr}\right)
+V_H(r).
}

As condições são:

\[
(\partial_r+R_H)t|_{r_c}=0,
\]

\[
t(r)\to0
\quad\text{ou é quadrado-integrável quando }r\to\infty.
\]

A função de Green \(G_H(r,r')\) satisfaz

\[
K_HG_H(r,r')
=\frac{\delta(r-r')}{w_H(r)}.
\]

Então:

\[
[K_H^{-1}c_H^\sharp](r)
=\int G_H(r,r')c_H(r')w_H(r')dr'.
\]

Isso transforma o cálculo de \(I_H\) num problema numérico bem definido.

---

## 10. Relação com o operador axial da Q42

A Q42 calculou para a textura de Hopf no cilindro:

\[
L_H
=-\frac1{e^{-x^2/4}}
\frac d{dx}
\left(e^{-x^2/4}\frac d{dx}\right)
+2,
\]

com

\[
z_H=\frac{3\sqrt\pi}{4}.
\]

Esse operador pode servir como primeiro \(K_H\) diagnóstico se for demonstrado
que a textura axial calculada coincide com a perturbação torsional que entra em
\(\mathcal C_H\) e \(\mathcal I_H\).

Atualmente essa identificação não está provada. O operador da Q42 atua sobre o
perfil axial \(\eta\), enquanto \(t_H\) foi introduzido como projeção da
3-forma de torção.

Portanto:

\[
\boxed{
K_H=L_H\text{ é um primeiro modelo testável, não uma identidade já fechada.}
}

---

## 11. Determinação da escala de soldagem \(\ell_B\)

O mapa equivarante é

\[
\mathscr S_B(\boldsymbol B)
=\ell_BB^i\Sigma_i^+.
\]

Sua escala deve ser fixada comparando a norma geométrica do modo interno com a
normalização cinética do campo eletromagnético efetivo.

Se a redução do setor \(U(1)\) fornece

\[
S_{U(1)}
=-\frac1{4g_{\rm EM}^2}
\int F_{\mu\nu}F^{\mu\nu}d^4x,
\]

enquanto a projeção GDQ fornece

\[
S_{\rm lift}
=-\frac{\mathcal N_A\ell_B^2}{4}
\int F_{\mu\nu}F^{\mu\nu}d^4x,
\]

então:

\[
\boxed{
\ell_B
=\frac1{g_{\rm EM}\sqrt{\mathcal N_A}}.
}

Os fatores exatos dependem da convenção de carga e da definição de
\(\Sigma_i^+\), mas a dependência estrutural é fixa.

Assim, \(\ell_B\) depende do mesmo problema de normalização interna tratado na
Q37 para a constante de estrutura fina. Não pode ser obtido apenas pela
simetria de Hopf.

---

## 12. Fórmula consolidada para o momento

Combinando os resultados:

\[
\mu_{\rm GDQ}
=\frac q c\ell_BI_H,
\]

\[
I_H
=C_{1/2}
\frac{
\mathcal I_H[K_H^{-1}c_H^\sharp]
}
{
\mathcal C_H[K_H^{-1}c_H^\sharp]
},
\]

\[
\ell_B
=\frac1{g_{\rm EM}\sqrt{\mathcal N_A}},
\]

obtemos

\[
\boxed{
\mu_{\rm GDQ}
=\frac{qC_{1/2}}
{c\,g_{\rm EM}\sqrt{\mathcal N_A}}
\frac{
\mathcal I_H[K_H^{-1}c_H^\sharp]
}
{
\mathcal C_H[K_H^{-1}c_H^\sharp]
}.
}

Essa é uma fórmula dedutiva, mas ainda condicional aos operadores e
normalizações indicados.

---

## 13. Dependências identificadas

O cálculo completo de \(\mu_{\rm GDQ}\) depende de:

1. Q23/Q42: quantum de circulação e setor de Hopf;
2. Q42: Hessiana axial/torsional do estômato;
3. Q37: normalização cinética do \(U(1)\) e \(g_{\rm EM}\);
4. teoria de interface: mapa de acoplamento \(\mathcal I_H\);
5. background oficial: \(\mathcal N_A\) e condições de contorno.

Isso explica por que o momento magnético não pode ser derivado isoladamente
somente no capítulo de Stern--Gerlach.

---

## 14. O que foi fechado

1. formulação variacional do perfil torsional;
2. solução de norma mínima em termos de \(K_H^{-1}\);
3. energia mínima do setor quantizado;
4. fórmula espectral de \(I_H\);
5. condição necessária para \(I_H=C_{1/2}\);
6. redução a problema de Green/Sturm--Liouville;
7. relação de \(\ell_B\) com a normalização eletromagnética;
8. fórmula consolidada de \(\mu_{\rm GDQ}\).

---

## 15. O que permanece

1. derivar \(c_H(r)\) da holonomia da conexão;
2. derivar \(i_H(r)\) do acoplamento torsão--curvatura completo;
3. identificar ou calcular \(K_H\) torsional;
4. avaliar a função de Green;
5. obter \(g_{\rm EM}\) da Q37;
6. verificar dimensões após a projeção causal;
7. comparar o momento previsto sem calibrá-lo por \(\mu_B\).

## 16. Próximo passo

O próximo passo local é construir um teste diagnóstico tomando
\(K_H=L_H\) da Q42 e escolhendo kernels explícitos \(c_H,i_H\), para estudar a
sensibilidade de \(I_H\). Esse teste não fechará o momento físico, mas mostrará
quais dados de colagem dominam a resposta e impedirá escolhas arbitrárias de
perfil.

O teste foi implementado em `interface_medida/test_variacional_IH.py`, com
saída em `interface_medida/saida_variacional_IH.md`. O caso
\(\mathcal I_H=\mathcal C_H\) retorna exatamente
\(I_H=C_{1/2}\); kernels distintos produzem fatores de forma dependentes da
condição Robin.

A natureza geométrica dos kernels foi analisada em
`derivacao_kernels_cH_iH.md`: circulação é naturalmente um funcional de
traço/fluxo, enquanto o acoplamento magnético é volumétrico. A igualdade exige
uma identidade de localização on-shell.

## 17. Status

\[
\boxed{
\text{problema de }I_H\text{ reduzido a uma razão de respostas espectrais;}
\quad
\ell_B\text{ identificado como dependência da normalização }U(1).
}
\]
