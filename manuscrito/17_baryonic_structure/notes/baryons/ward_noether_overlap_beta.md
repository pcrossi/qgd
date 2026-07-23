---
title: "Ward--Noether, modos de saída e overlap beta"
---

# Ward--Noether, modos de saída e overlap beta

## 1. Enunciado

Esta nota preserva a construção correta do setor beta: as conservações
determinam seleção, cinemática e base angular do decaimento beta, mas não
determinam sozinhas a magnitude dos coeficientes reduzidos.

O processo é

$$
n\to p+e^-+\bar\nu_e.
$$

A ação oficial não recebe um vértice fundamental novo. O vértice efetivo é a
quarta variação projetada da ação GDQ no background de cirurgia:

$$
\mathcal V_{\rm eff}^{(4)}
=
\mathcal S_{\rm GDQ}^{(4)}
-
\mathcal S_{\rm GDQ}^{(3)}
K_\perp^{-1}
\mathcal S_{\rm GDQ}^{(3)}
+
\text{permutações}.
$$

## 2. Modos de saída Dirac--Bismut

Na borda $S^3_r$, o operador tangencial reduzido usado no setor de saída é

$$
D_{m,-3/2}^{(j)}
=
\frac1r
\left(
2\boldsymbol\sigma\cdot\mathbf L
-
m\sigma_3
\right).
$$

Para o canal eletrônico, $m=-1$ e $j=1/2$. O espectro em unidades $r^{-1}$ é

$$
\{-1-\sqrt5,\ 0,\ \sqrt5-1,\ 2\}.
$$

O kernel do bloco é unidimensional; com a multiplicidade espectadora de
Peter--Weyl, o setor físico antes da projeção APS tem dimensão $2$.

Para o modo neutro torsional, $m=0$ e $j=0$:

$$
D_{0,-3/2}^{(0)}=0_{2\times2}.
$$

Logo o kernel neutro tem dimensão $2$. Esse é o setor reduzido do
antineutrino torsional. A orientação APS e a corrente de saída selecionam o
subespaço físico propagante; a equação tangencial isolada não escolhe uma
base única.

## 3. O zero parcial não anula o decaimento

O overlap entre apenas o modo eletrônico e o modo neutro com operador orbital
escalar pode ser zero. Isso não implica que o processo completo tenha
amplitude nula, porque o vértice físico contém também as pernas bariônicas
$n$ e $p$.

A amplitude não polarizada completa é reduzida por isotropia a dois
invariantes:

$$
\mathcal M_0=C_SS+C_TT.
$$

Uma base conveniente é

$$
S=(p^\dagger n)(e^\dagger\nu),
$$

$$
T=\sum_i(p^\dagger\sigma_i n)(e^\dagger\sigma_i\nu).
$$

A álgebra de Pauli fornece a identidade de Fierz:

$$
\sum_i
(\sigma_i)_{ab}
(\sigma_i)_{cd}
=
2\delta_{ad}\delta_{cb}
-
\delta_{ab}\delta_{cd}.
$$

Com soma nos spins finais e média no spin inicial do nêutron:

$$
\frac12\langle S,S\rangle=2,
\qquad
\frac12\langle T,T\rangle=6,
\qquad
\frac12\langle S,T\rangle=0.
$$

Assim,

$$
\frac12\sum_{\rm spins}|\mathcal M_0|^2
=
2|C_S|^2+6|C_T|^2.
$$

## 4. O que Ward--Noether fixa

Homogeneidade temporal e espacial fornecem o delta de conservação:

$$
\mathcal M_{fi}
=
(2\pi)^4
\delta^{(4)}(P_f-P_i)
\widehat{\mathcal M}_{fi}.
$$

As cargas de Noether impõem

$$
\sum_r\epsilon_r Q_{{\rm EM},r}=0,
\qquad
\sum_r\epsilon_r Q_{T,r}=0.
$$

Em termos do vértice amputado, a identidade de Ward tem a forma esquemática

$$
q_\mu\Gamma_A^\mu
=
\sum_{r\in{\rm ext}}
\epsilon_r Q_{A,r}K_r.
$$

On-shell, $K_r\psi_r=0$, então

$$
q_\mu\Gamma_A^\mu=0.
$$

Isso fixa a parte longitudinal e exclui canais que violam conservação. Não
fixa a parte transversal física do vértice.

De fato, para qualquer $\lambda\in\mathbb C$,

$$
C_S\mapsto\lambda C_S,
\qquad
C_T\mapsto\lambda C_T
$$

preserva as cargas, isotropia e identidades homogêneas on-shell, mas muda a
taxa por $|\lambda|^2$:

$$
\Gamma_n\mapsto|\lambda|^2\Gamma_n.
$$

Logo,

$$
\boxed{
\text{Noether isolado não determina }C_S,C_T.
}
$$

O fechamento requer a ação projetada:

$$
C_A
=
\frac{\hbar}{\Lambda_C^2}
\frac{2\pi i}{(4\pi)^4}
[z^3]F_A,
\qquad
A\in\{S,T\}.
$$

## 5. Jatos causais e combinação contraída

Se o peso causal e o vértice possuem expansões

$$
P(z)=P_0+P_1z+\frac12P_2z^2+\frac16P_3z^3,
$$

$$
N(z)=N_0+N_1z+\frac12N_2z^2+\frac16N_3z^3,
$$

então o coeficiente cúbico do produto é

$$
[z^3](PN)
=
\frac16P_0N_3
+
\frac12P_1N_2
+
\frac12P_2N_1
+
\frac16P_3N_0.
$$

Para uma energia torsional escrita como $E_T=E_0e^{-X(z)}$, com

$$
X(z)=x_1z+\frac12x_2z^2+\frac16x_3z^3,
$$

temos

$$
E_T'''(0)
=
E_0
\left(
-x_1^3+3x_1x_2-x_3
\right).
$$

Essas identidades não atribuem valores aos jatos físicos; elas definem o que
deve ser calculado a partir do background causal.

## 6. Projetor de fluxo e Schur quártico

Se $C(v)=c\cdot v$ é um vínculo linear de fluxo, o projetor euclidiano para o
subespaço físico é

$$
P_Q
=
I
-
c^T(cc^T)^{-1}c.
$$

Ele satisfaz

$$
P_Q^2=P_Q,
\qquad
cP_Q=0.
$$

Ao eliminar um modo transversal $\xi$ de

$$
\frac12K\xi^2+\frac12G\xi q^2+\frac1{24}V_4q^4,
$$

a solução estacionária é

$$
\xi_*=-\frac{G}{2K}q^2.
$$

Substituindo de volta, a quarta variação efetiva é

$$
V_{4,\rm eff}
=
V_4-\frac{3G^2}{K}.
$$

Esse é o complemento de Schur elementar que aparece na quarta variação
projetada.

## 7. Status

Demonstrado:

1. os modos de saída reduzidos do operador declarado;
2. a existência de dois invariantes angulares $S,T$;
3. a norma não polarizada $2|C_S|^2+6|C_T|^2$;
4. que Ward--Noether não fixa a magnitude transversal;
5. as identidades simbólicas dos jatos causais;
6. o projetor de fluxo e o Schur quártico elementar.

Condicional:

1. os valores separados de $C_S$ e $C_T$;
2. correlações angulares e observáveis polarizados;
3. avaliação direta dos jatos $[z^3]F_S$ e $[z^3]F_T$ pela Hessiana completa.

Verificações autocontidas:

- `scripts/resolver_modos_dirac_bismut_beta.py`;
- `scripts/verificar_overlap_quatro_modos_beta.py`;
- `scripts/verificar_liberdade_noether_beta.py`;
- `scripts/verificar_jatos_causais_beta.py`;
- `scripts/verificar_projecao_fluxo_quartica_beta.py`.
