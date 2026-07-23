# Sobreposição do campo clássico com o triplet de Hopf e derivação de \(g_X\)

## 1. Objetivo

Este documento calcula a forma geral da projeção

\[
j_i
=\langle\Sigma_i^+,J_{\rm app}\rangle
\]

e separa:

1. o momento magnético geométrico do objeto;
2. o campo estático que seleciona o eixo de medição;
3. a variação do campo que acopla o objeto ao ponteiro;
4. as correções de tamanho finito do estômato.

O resultado líder é:

\[
\boxed{
S_{\rm int}^{\rm red}
=\int dt\,
\mu_{\rm GDQ}
\boldsymbol n(P)\cdot
\boldsymbol B_{\rm eff}(X).
}
\]

Expandindo \(\boldsymbol B_{\rm eff}\) no ponteiro, obtém-se \(g_X\) sem
inseri-lo como parâmetro fundamental.

---

## 2. Dois espaços vetoriais tridimensionais

O campo magnético clássico pertence ao espaço de vetores axiais da folha
física:

\[
\boldsymbol B\in V_{\rm ax}^{\rm phys}\simeq\mathbb R^3.
\]

O triplet auto-dual pertence ao espaço interno:

\[
\mathcal H_+^2(T^4)
=\operatorname{span}\{\Sigma_1^+,\Sigma_2^+,\Sigma_3^+\}
\simeq\mathbb R^3.
\]

Para acoplá-los, é necessário um mapa de soldagem

\[
\mathscr S_B:
V_{\rm ax}^{\rm phys}
\longrightarrow
\mathcal H_+^2(T^4).
\]

Esse mapa não deve ser confundido com uma identificação arbitrária de
coordenadas.

---

## 3. Unicidade equivarante do levantamento

O subgrupo diagonal de rotações físicas e internas atua como \(SU(2)\) nos
dois espaços. Exige-se equivariância:

\[
\mathscr S_B(R\boldsymbol B)
=R\,\mathscr S_B(\boldsymbol B).
\]

Como ambos os espaços carregam a representação real irredutível de dimensão
3, o lema de Schur implica que todo mapa linear equivarante é proporcional à
identidade entre as representações:

\[
\boxed{
\mathscr S_B(\boldsymbol B)
=\ell_B B^i\Sigma_i^+.
}

O eixo é, portanto, determinado unicamente. Resta apenas a escala de soldagem
\(\ell_B\), que depende das unidades, da projeção da folha física e da
normalização do campo na ação.

Não existe, na ordem linear e num background isotrópico, outra matriz de
mistura independente.

---

## 4. Perfil torsional do objeto

No setor axial de Hopf, escreva a 2-forma espacial projetada da torção como

\[
\boxed{
\mathcal T_Q(r,P)
=t_H(r)n^i(P)\Sigma_i^+.
}

Aqui:

- \(t_H(r)\) é o perfil radial normalizado pela circulação e pela medida;
- \(n^i(P)\) são as coordenadas do mapa de Hopf;
- \(r\) representa as coordenadas normais ao centro do estômato.

Como a base é ortonormal:

\[
\langle\mathcal T_Q,
\mathscr S_B(\boldsymbol B)\rangle
=\ell_Bt_H(r)n^iB_i.
\]

Logo a dependência angular é obrigatoriamente

\[
\boldsymbol n(P)\cdot\boldsymbol B.
\]

---

## 5. Redução do acoplamento torsão--curvatura

O acoplamento já derivado é

\[
S_{\rm int}
=\frac q{2c}
\int
\mathcal T_Q^{AB}F^{\rm app}_{AB}\,d\mu.
\]

Em norma de 2-formas:

\[
\frac12\mathcal T^{AB}F_{AB}
=\langle\mathcal T,F\rangle.
\]

Portanto:

\[
S_{\rm int}^{\rm red}
=\frac{q\ell_B}{c}
\int dt\,dV_\perp
\chi_{\rm SG}\mathcal U_*
t_H(r)
n^i(P)B_i(X+r).
\]

Defina o peso torsional normal:

\[
\boxed{
W_H(r)
=\chi_{\rm SG}(r)\mathcal U_*(r)t_H(r).
}

Então:

\[
\boxed{
S_{\rm int}^{\rm red}
=\int dt\,
n^i(P)\,\mathcal B_i(X),
}

com

\[
\boxed{
\mathcal B_i(X)
=\frac{q\ell_B}{c}
\int W_H(r)B_i(X+r)dV_\perp.
}

\(\mathcal B_i\) possui dimensão de energia na convenção física final.

---

## 6. Limite de campo lentamente variável

Se o campo varia numa escala \(L_B\) muito maior que o raio do estômato
\(r_c\):

\[
\varepsilon_B=\frac{r_c}{L_B}\ll1,
\]

expanda:

\[
B_i(X+r)
=B_i(X)
+r^a\partial_aB_i(X)
+\frac12r^ar^b
\partial_a\partial_bB_i(X)
+\cdots.
\]

Defina os momentos do perfil:

\[
I_H=\int W_H(r)dV_\perp,
\]

\[
d_H^a=\int r^aW_H(r)dV_\perp,
\]

\[
Q_H^{ab}=\int r^ar^bW_H(r)dV_\perp.
\]

Então:

\[
\boxed{
\mathcal B_i(X)
=\frac{q\ell_B}{c}
\left[
I_HB_i
+d_H^a\partial_aB_i
+\frac12Q_H^{ab}
\partial_a\partial_bB_i
+\cdots
\right].
}

Para perfil centrado e isotrópico:

\[
d_H^a=0,
\qquad
Q_H^{ab}=\frac{I_H\langle r^2\rangle_H}{d_\perp}
\delta^{ab}.
\]

Logo:

\[
\boxed{
\mathcal B_i(X)
=\mu_{\rm GDQ}
\left[
B_i(X)
+\frac{\langle r^2\rangle_H}{2d_\perp}
\Delta B_i(X)
+O(\varepsilon_B^4)
\right],
}

onde

\[
\boxed{
\mu_{\rm GDQ}
=\frac{q\ell_B}{c}I_H.
}

O gradiente linear não corrige o momento interno de um perfil centrado, mas
produz a força sobre a coordenada coletiva do centro.

---

## 7. Campo estático e seleção da base

No ponto central \(X_0\), defina

\[
\boldsymbol B_0
=\boldsymbol B_{\rm eff}(X_0).
\]

O termo independente do ponteiro é

\[
\boxed{
V_0(P)
=-\mu_{\rm GDQ}
\boldsymbol n(P)\cdot\boldsymbol B_0.
}

Assim:

\[
\boxed{
\boldsymbol n_A
=\frac{\boldsymbol B_0}{|\boldsymbol B_0|}.
}

O campo estático escolhe a base de medida, mas não é ainda o acoplamento ao
registro macroscópico.

---

## 8. Acoplamento ao ponteiro

Se o modo coletivo \(X\) modifica o campo percebido pelo objeto:

\[
\boldsymbol B_{\rm eff}(X)
=\boldsymbol B_0
+X\boldsymbol b_X
+O(X^2),
\]

onde

\[
\boldsymbol b_X
=\left.
\frac{\partial\boldsymbol B_{\rm eff}}
{\partial X}
\right|_{X=0},
\]

então:

\[
V_{\rm int}(P,X)
=-\mu_{\rm GDQ}
X\boldsymbol n(P)\cdot\boldsymbol b_X.
\]

Se o aparelho é construído para medir ao longo do mesmo eixo:

\[
\boldsymbol b_X
=|\boldsymbol b_X|\boldsymbol n_A,
\]

obtemos

\[
\boxed{
V_{\rm int}(P,X)
=-g_XXs_{\boldsymbol n}(P),
}

com

\[
\boxed{
g_X
=\mu_{\rm GDQ}|\boldsymbol b_X|.
}

Portanto, \(g_X\) é o produto de:

1. momento magnético geométrico do objeto;
2. ganho/transdução de campo por unidade do ponteiro.

---

## 9. Caso em que o ponteiro é a posição do centro

Se \(X=z\) é a posição do centro do sóliton ao longo do gradiente:

\[
\boldsymbol b_z
=\partial_z\boldsymbol B.
\]

Então:

\[
\boxed{
g_z
=\mu_{\rm GDQ}
|\partial_z\boldsymbol B|.
}

O acoplamento possui dimensão de força e a equação mecânica é

\[
m\ddot z
=\kappa g_z.
\]

Esse é o estágio de separação do feixe. O ponteiro final da tela pode ser uma
segunda variável \(X_D\), acoplada à posição de impacto. Não se deve confundir
automaticamente \(z\) com o registro metastável do detector.

---

## 10. Caso em que o ponteiro é magnetização

Se \(X=M\) é um modo coletivo de magnetização do aparelho:

\[
\boldsymbol b_M
=\frac{\partial\boldsymbol B_{\rm local}}
{\partial M}.
\]

Logo:

\[
\boxed{
g_M
=\mu_{\rm GDQ}
\left|
\frac{\partial\boldsymbol B_{\rm local}}
{\partial M}
\right|.
}

Nesse caso, \(g_M\) depende da geometria do circuito magnético e da
susceptibilidade do material. Esses são dados legítimos do aparelho, enquanto
\(\mu_{\rm GDQ}\) pertence ao objeto.

---

## 11. Taxa informacional em termos do campo

Para o detector ôhmico clássico:

\[
\Gamma_A
=\frac{g_X^2}{8\gamma_Ak_BT_A}.
\]

Substituindo a sobreposição:

\[
\boxed{
\Gamma_A
=\frac{mu_{\rm GDQ}^2
|\boldsymbol b_X|^2}
{8\gamma_Ak_BT_A}.
}

E, usando a norma torsional do canal:

\[
\boxed{
\Gamma_A
=\frac{
\left(\frac{q\ell_B}{c}I_H\right)^2
|\boldsymbol b_X|^2}
{8k_BT_A
\sqrt{Z_t^{(\rm SG)}Z_x^{(\rm SG)}}}.
}

Agora a taxa está separada em:

- dados do objeto: \(q,I_H\);
- soldagem geométrica: \(\ell_B\);
- dados do aparelho: \(\boldsymbol b_X,T_A\);
- impedância do canal: \(Z_t,Z_x\).

---

## 12. Correções de tamanho finito

A primeira correção para perfil isotrópico é

\[
\delta B_i
=\frac{\langle r^2\rangle_H}{2d_\perp}
\Delta B_i.
\]

Ela modifica tanto a base quanto a intensidade:

\[
\boldsymbol B_{\rm eff}
=\boldsymbol B
+\delta\boldsymbol B.
\]

A mudança angular é a componente transversal:

\[
\delta\boldsymbol n_A
=\frac1{|\boldsymbol B|}
\left(I-\boldsymbol n_A\boldsymbol n_A^T\right)
\delta\boldsymbol B.
\]

Essa é uma possível correção específica da GDQ para campos que variam na
escala do estômato. Em Stern--Gerlach macroscópico ordinário, espera-se que
seja extremamente pequena.

---

## 13. Projeção na base integral de \(T^4\)

Na base canônica auto-dual:

\[
\omega_{\rm Hopf}
=n^i\Sigma_i^+.
\]

Para converter à base de fluxos integrais:

\[
\Sigma_i^+
=C_i^{ab}(R)\omega_{ab},
\]

onde os coeficientes \(C_i^{ab}\) contêm
\(1/\sqrt{G_{ab,ab}^{\rm top}}\).

Assim, a integralidade topológica restringe as amplitudes permitidas de
\(t_H\), enquanto a base canônica garante que a contração angular continue
sendo \(\boldsymbol n\cdot\boldsymbol B\).

Essa distinção impede que fatores dos raios sejam contados duas vezes.

---

## 14. O que foi derivado

1. levantamento equivarante único do campo clássico;
2. forma angular \(\boldsymbol n\cdot\boldsymbol B\);
3. momento magnético

   \[
   \mu_{\rm GDQ}=(q\ell_B/c)I_H;
   \]

4. eixo selecionado por \(\boldsymbol B_0\);
5. acoplamento ao ponteiro

   \[
   g_X=\mu_{\rm GDQ}|\boldsymbol b_X|;
   \]

6. caso de posição e força de Stern--Gerlach;
7. caso de magnetização;
8. taxa informacional em termos de objeto e aparelho;
9. primeira correção de tamanho finito.

---

## 15. O que permanece

1. calcular \(I_H\) do perfil torsional estacionário;
2. determinar \(\ell_B\) pelo mapa de soldagem folha--bulk;
3. fixar \(q\) na normalização física da ação;
4. calcular \(\boldsymbol b_X\) para um aparelho real;
5. avaliar as correções multipolares do estômato;
6. incluir mistura com modos métricos e dilatônicos;
7. comparar \(\mu_{\rm GDQ}\) com o momento observado sem usá-lo como entrada.

## 16. Próximo passo

O gargalo foi reduzido a duas quantidades intrínsecas:

\[
\boxed{I_H\quad\text{e}\quad\ell_B.}
\]

O próximo cálculo deve procurar no background cilíndrico de Hopf da Q42 um
perfil torsional normalizável \(t_H(r)\), usar a circulação quantizada para
fixar sua amplitude e avaliar \(I_H\). Em paralelo, deve-se formular o mapa de
soldagem entre a 2-forma física magnética e o triplet interno para fixar
\(\ell_B\) dimensionalmente.

A auditoria e a formulação variacional foram realizadas em
`topicos/neutron_decaimento/variacional_perfil_torcional_IH.md`. A Q42 não fornece ainda um perfil de
3-forma, e \(J_\Theta\) não pode ser identificado silenciosamente com \(H\).
O perfil de norma mínima foi reduzido a \(K_H^{-1}c_H\), e \(\ell_B\) foi
relacionado à normalização cinética do setor \(U(1)\) da Q37.

## 17. Status

\[
\boxed{
\text{sobreposição angular e }g_X\text{ derivados estruturalmente;}
\quad
I_H\text{ e }\ell_B\text{ permanecem por avaliar.}
}
\]
