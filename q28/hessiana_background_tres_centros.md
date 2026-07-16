# Q28 — Hessiana do background GDQ de três centros

## 1. Objetivo

Considere o domínio com três núcleos excisados

$$
\Omega_3
=\mathcal M_{\mathbb C}\setminus
\bigcup_{a=1}^{3}\mathcal N_a,
\qquad
\partial\mathcal N_a\simeq S^3.
$$

O background procurado é

$$
\Phi_*^{(3)}
=(g_*^{(3)},f_*^{(3)},\bar f_*^{(3)}),
$$

solução estacionária da ação oficial no bulk e das condições variacionais nas
três componentes de bordo.

Depois da fixação Hermitiano--DeTurck e da restrição da normalização de
$\mathcal U$, a Hessiana oficial tem a forma

$$
\mathbb H_*^{(3)}
=\frac{\hbar}{\Lambda_C^2}
\begin{pmatrix}
L_{ff}&L_{fg}\\
L_{gf}&L_{gg}^{\rm HD}
\end{pmatrix}_{\Phi_*^{(3)}}.
$$

O símbolo principal de $L_{ff}$ é o Laplaciano com drift e o de
$L_{gg}^{\rm HD}$ é o operador de Lichnerowicz com drift. Isso determina a
expressão diferencial no interior de $\Omega_3$, mas não determina sozinho o
domínio do operador.

## 2. Definições físicas dos três blocos

### 2.1 Vínculo de conservação no problema variacional

A conservação não pode ser aplicada somente depois de resolver o background.
O vínculo vetorial de tensão é

$$
\mathcal C(\Phi)=\sum_{a=1}^{3}\mathbf T_a[\Phi].
$$

Separadamente, a circulação orientada obedece ao vínculo escalar

$$
\mathcal C_q(\Phi)
=\sum_{a=1}^{3}q_a[\Phi]+Q_{\rm bulk}[\Phi]-Q_{\rm tot}=0.
$$

No nêutron, a solução inteira mínima pode ser $(1,1,-2)$ e
$Q_{\rm tot}=0$. No próton, os três fluxos locais podem ser coorientados; sua
soma não deve ser artificialmente anulada, pois é compensada pelo termo do
sóliton global e fornece $Q_{\rm tot}\ne0$. Portanto, fechamento mecânico e
conservação de carga são vínculos distintos.

O background físico é um extremo do funcional aumentado

$$
\boxed{
\widetilde{\mathcal S}[\Phi,\boldsymbol\lambda]
=\mathcal S_{\rm GDQ}[\Phi]
+\boldsymbol\lambda\cdot\mathcal C(\Phi)
+\lambda_q\mathcal C_q(\Phi),
}
$$

onde as duas componentes de $\boldsymbol\lambda\in\mathcal H^*$ são
determinadas simultaneamente por

$$
\frac{\delta\mathcal S_{\rm GDQ}}{\delta\Phi}
+D\mathcal C(\Phi)^\dagger\boldsymbol\lambda
+D\mathcal C_q(\Phi)^\dagger\lambda_q=0,
\qquad
\boxed{\mathcal C(\Phi)=0,\quad\mathcal C_q(\Phi)=0.}
$$

As flutuações físicas pertencem a $\ker D\mathbf C_*$ e a Hessiana correta é

$$
\boxed{
\mathbb H_{\rm cons}
=\left.
\left(
\mathbb H_{\rm GDQ}
+\sum_{I=1}^{2}\lambda_I D^2\mathcal C_I
+\lambda_qD^2\mathcal C_q
\right)
\right|_{\ker D\mathbf C_*}.
}
$$

Antes de eliminar o multiplicador, o sistema linearizado possui a forma KKT

$$
\boxed{
\mathbb K_{\rm KKT}
=\begin{pmatrix}
\mathbb H_{\rm GDQ}+\lambda_ID^2\mathcal C_I+\lambda_qD^2\mathcal C_q
&D\mathbf C_*^\dagger\\
D\mathbf C_*&0
\end{pmatrix}.
}
$$

Aqui $\mathbf C=(\mathcal C_1,\mathcal C_2,\mathcal C_q)$ reúne os três
vínculos reais.

Se $e_i=\partial_{\vartheta_i}\Phi_*^{(3)}$, com $i=1,2$, são os dois modos
relativos do triângulo de estômatos, então

$$
(H_{\rm rel})_{ij}
=\left\langle e_i,\mathbb H_{\rm cons}e_j\right\rangle_{\mathcal U_*}.
$$

Pela simetria $C_3$ do background equilátero,

$$
H_{\rm rel}
=\frac32\kappa_{\rm rel}T^2I_2,
$$

de modo que

$$
\boxed{
\kappa_{\rm rel}
=\frac1{3T^2}\operatorname{tr}H_{\rm rel}.
}
$$

Se $\Pi_\perp$ projeta sobre as flutuações radiais, dilatônicas e tensoriais
ortogonais aos modos relativos e aos modos de gauge,

$$
\boxed{
K_\perp
=\Pi_\perp\mathbb H_{\rm cons}\Pi_\perp,
}
$$

e

$$
\boxed{
J
=\Pi_{\rm rel}\mathbb H_{\rm cons}\Pi_\perp.
}
$$

Essas fórmulas não são parâmetros fenomenológicos: são exatamente os
pullbacks físicos da segunda variação oficial.

## 3. Termo de bordo da segunda variação

Como $\Omega_3$ possui bordo, a integração por partes produz

$$
\delta^2\mathcal S_{\rm GDQ}
=\langle\delta\Phi,\mathbb H_{\rm bulk}\delta\Phi\rangle_{\Omega_3}
+\sum_{a=1}^{3}
\int_{\partial\mathcal N_a}
\mathfrak b_a
(\delta\Phi,\nabla_n\delta\Phi).
$$

Equivalentemente, a forma de Green do operador é

$$
\mathfrak G(\Phi_1,\Phi_2)
=\sum_{a=1}^{3}\int_{\partial\mathcal N_a}
\left(
\langle\Phi_1,Z_n\nabla_n\Phi_2\rangle
-\langle Z_n\nabla_n\Phi_1,\Phi_2\rangle
\right).
$$

Para que a Hessiana seja auto-adjunta é necessário escolher, em cada
estômato, um subespaço lagrangiano de dados de Cauchy. Em notação Robin
matricial,

$$
\left.
(Z_n\nabla_n+\mathsf R_a)\delta\Phi
\right|_{\partial\mathcal N_a}=0,
\qquad
\mathsf R_a=\mathsf R_a^\dagger.
$$

O vínculo torna as três condições coletivas. A variação de bordo assume a
forma

$$
\boxed{
Z_n\nabla_n\Phi_a
+\mathsf R_a^{(0)}\Phi_a
+D_a\mathcal C^\dagger\boldsymbol\lambda=0,
\qquad a=1,2,3.
}
$$

O mesmo multiplicador correlaciona os três estômatos e impõe a conservação do
fluxo durante a solução, não posteriormente.

## 4. Subdeterminação pela ação oficial atual

A ação oficial, complementada pelo vínculo, determina o fechamento coletivo e
o termo $D\mathcal C^\dagger\boldsymbol\lambda$. A integral de bulk ainda não
declara:

1. um funcional de bordo cuja segunda variação determine $\mathsf R_a$;
2. dados de Dirichlet para $g$ e $f$ nos estômatos;
3. uma impedância Robin externa;
4. uma lei de colagem que determine os saltos normais dos três centros.

Portanto, mesmo com o vínculo, a mesma expressão de bulk admite diferentes extensões
auto-adjuntas. Para duas escolhas admissíveis $\mathsf R$ e $\mathsf R'$, em
geral,

$$
\operatorname{spec}K_\perp(\mathsf R)
\ne
\operatorname{spec}K_\perp(\mathsf R'),
$$

$$
\kappa_{\rm rel}(\mathsf R)
\ne
\kappa_{\rm rel}(\mathsf R'),
\qquad
J(\mathsf R)\ne J(\mathsf R').
$$

Isso não é dificuldade numérica: é ausência de definição do problema de
contorno.

## 5. O que o cálculo numérico já prova

O solver horizontal avalia a restrição universal

$$
\mathcal E_{\rm close}
=\frac12\left|\sum_a\mathbf T_a\right|^2.
$$

Ele prova numericamente que o único junction fechado, não colinear e isolado
nessa restrição é $N=3$. Ele determina a matriz de Gram adimensional

$$
\frac{H_{\rm rel}}{\kappa_{\rm rel}T^2}
=\operatorname{diag}\left(\frac32,\frac32\right),
$$

mas não determina o prefator físico $\kappa_{\rm rel}T^2$, nem o operador
$K_\perp$, nem o acoplamento $J$.

## 6. Dado mínimo que fecha o cálculo

Sem modificar o bulk da ação oficial, é necessário fixar uma destas classes:

### 6.1 Contorno geométrico fixo

$$
\delta g|_{\partial\mathcal N_a}=0,
\qquad
\delta f|_{\partial\mathcal N_a}=0.
$$

### 6.2 Contorno natural derivado

Especificar o funcional de bordo GDQ cuja primeira variação anule o fluxo e
cuja segunda variação produza $\mathsf R_a$.

### 6.3 Colagem dinâmica

Especificar a solução interior de cada núcleo e exigir continuidade do campo
e do momento normal. A eliminação do interior fornece a aplicação
Dirichlet--to--Neumann

$$
\mathsf R_a
=-\operatorname{DN}_{\mathcal N_a},
$$

sem parâmetro ajustado.

A terceira rota é a mais intrínseca: a impedância nasce da própria colagem e
não precisa ser acrescentada como constante externa.

## 7. Algoritmo completo depois da colagem

Uma vez determinada $\mathsf R_a$, o cálculo é inequívoco:

1. resolver simultaneamente as equações de Euler--Lagrange, o multiplicador
   $\boldsymbol\lambda$ e $\mathcal C(\Phi)=0$ no domínio de três centros;
2. diferenciar a solução em relação aos dois módulos relativos;
3. montar a Hessiana esparsa gauge-fixada;
4. projetar modos de gauge e a rotação comum;
5. calcular $\kappa_{\rm rel}$ pela fórmula de traço;
6. montar $K_\perp$ e $J$ pelas projeções;
7. avaliar

   $$
   H_{\rm eff}
   =H_{\rm rel}-JK_\perp^{-1}J^\dagger;
   $$

8. verificar a positividade de $H_{\rm eff}$ e de $K_\perp$.

## 8. Veredito

Com a ação oficial e o vínculo, $\kappa_{\rm rel}$, $K_\perp$ e $J$ são os
blocos da Hessiana restrita $\mathbb H_{\rm cons}$. O vínculo seleciona o
fechamento coletivo e correlaciona as três bordas. Ele não fornece sozinho a
resposta normal de cada interior; essa resposta é a aplicação
Dirichlet--to--Neumann da colagem.

$$
\boxed{
\text{A pendência mínima é a aplicação Dirichlet--to--Neumann da colagem de
cada estômato.}
}
$$

Somente depois dela é matematicamente possível calcular a Hessiana completa
do background GDQ de três centros sem ajuste.
