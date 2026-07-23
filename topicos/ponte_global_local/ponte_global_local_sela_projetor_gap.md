# Ponte global--local — construção intrínseca da sela, do projetor físico e do gap

> [!warning] Escopo histórico
> A sela que colava o background cosmológico ao planar deixou de ser
> necessária após a prova por limite apontado em
> `topicos/ponte_global_local/ponte_global_local_lemas_sem_colar.md`. O projetor e o critério espectral
> deste documento continuam úteis como construção local. Sua avaliação física
> foi realizada para a classe gaussiana $C_3$ em
> `topicos/ponte_global_local/ponte_global_local_fechamento_c3.md`, onde $\Delta_0=1/2$. Não usar este
> arquivo para reabrir a Hipótese BI.

## 1. Enunciado

Pretende-se construir, sem importar backgrounds de outras questões:

1. uma sela bulk--interface da ação oficial da GDQ;
2. o espaço tangente físico determinado pelas conservações;
3. o projetor físico $P^{\rm phys}$;
4. a Hessiana física e o critério de gap.

O domínio global é

$$
M_\varepsilon
=T^4\times S^1_{L_\varepsilon}\times S^3_{R_\varepsilon},
$$

com interface interna $Y_\varepsilon\simeq S^3$. O limite local apontado é

$$
M_P=\mathbb R^4\times T^4.
$$

Os campos independentes são agrupados em

$$
X=(g,J,f),
$$

com

$$
J^2=-1,
\qquad g(J\cdot,J\cdot)=g,
\qquad H(X)=d_J^c\omega_g.
$$

Assim, $H$ não é variado como campo independente.

## 2. Ação e classe admissível

Usa-se somente a ação oficial

$$
\mathcal S_{\rm GDQ}[X]
=\int_\gamma\!\left[
\int_{M_\varepsilon}
\frac{\hbar}{\Lambda_C^2}
\left\{
\tau\left(\mathcal R[g,J]
+g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f\right)
+\frac{f+\bar f}{2}-n
\right\}
\mathcal U_f\,dV_g
\right]\frac{d\tau}{\tau},
$$

onde

$$
\mathcal U_f
=\frac{e^{-\operatorname{Re}f}}{(4\pi z_\tau)^4}.
$$

A classe admissível $\mathscr A_{q}$ é o conjunto de configurações que
satisfazem simultaneamente:

$$
\int_{M_\varepsilon}\mathcal U_f,dV_g=1,
$$

$$
Q[X]
=\frac1{2\pi}\int_{Y_\varepsilon}
\bigl(H(X)-H_{\rm ref}\bigr)=q\in\mathbb Z,
$$

continuidade do fluxo normal na interface,

$$
\bigl[\iota_\nu j_f\bigr]_{Y_\varepsilon}=0,
$$

e igualdade das cargas de Noether dos dois lados da colagem. Essas últimas
incluem energia, momento, momento angular e corrente de fase quando as
simetrias correspondentes são preservadas.

As condições de interface não são escolhidas depois do espectro. Elas surgem
do concomitante de Green da primeira variação:

$$
\delta\mathcal S_{\rm GDQ}
=\langle E(X),\delta X\rangle_{M_\varepsilon}
+\langle\Pi_+(X)-\Pi_-(X),\delta X\rangle_{Y_\varepsilon}.
$$

Logo, para interface livre,

$$
\Pi_+(X)=\Pi_-(X).
$$

Para carga fixada, aparece o multiplicador químico/topológico correspondente.

## 3. Papel exato de Noether

As simetrias fornecem identidades de conservação on shell:

$$
\nabla_A T^{AB}=0,
\qquad
\nabla_A j^A_f=0,
\qquad
\nabla_A J^{A}{}_{CD}=0.
$$

Integradas numa região bulk--interface, elas dão balanços de fluxo:

$$
\frac{d}{d\tau}\mathcal Q_\Omega
=-\int_{\partial\Omega}\iota_\nu\mathcal J.
$$

Portanto, Noether:

1. seleciona a folha de nível física;
2. determina quais fluxos devem ser contínuos na interface;
3. identifica os modos zero de simetria;
4. impede que a carga desapareça durante o limite global--local.

Noether não implica, sozinho, que exista um ponto crítico nessa folha nem que
esse ponto seja estável. Essas propriedades pertencem à primeira e à segunda
variações da ação.

## 4. Problema variacional com vínculos

Reúnam-se os vínculos em

$$
\mathcal C(X)
=\bigl(N(X)-1,Q(X)-q,\mathcal F(X),\mathcal N(X)\bigr)=0,
$$

onde $\mathcal F$ contém os balanços de interface e $\mathcal N$ as cargas de
Noether fixadas. O funcional aumentado é

$$
\mathscr L(X,\lambda)
=\mathcal S_{\rm GDQ}(X)
-\langle\lambda,\mathcal C(X)\rangle.
$$

A sela procurada deve resolver

$$
D_X\mathscr L(X_*,\lambda_*)=0,
\qquad
\mathcal C(X_*)=0.
$$

Essa é a formulação intrínseca correta do problema bulk--interface. Os
multiplicadores não são novos acoplamentos fundamentais: impõem dados
conservados.

## 5. Teorema de existência que de fato pode ser demonstrado

Considere uma classe gauge-fixada $\mathscr A_q^{k,\alpha}$ na qual:

1. $g$ possui elipticidade uniforme;
2. $g,J,f$ têm cotas uniformes em $C^{k,\alpha}$;
3. a medida é tight;
4. o conjunto de vínculos é fechado;
5. a ação é coerciva e semicontínua inferiormente nas direções físicas;
6. a condição de interface é complementar elíptica.

Então uma sequência minimizante possui subsequência convergente. O limite
$X_*$ pertence à mesma folha de vínculos e minimiza a ação nela. Se
$D\mathcal C(X_*)$ é sobrejetivo, o teorema dos multiplicadores fornece
$\lambda_*$ e

$$
D_X\mathscr L(X_*,\lambda_*)=0.
$$

Isso prova existência dentro dessa classe.

O ponto ainda não demonstrado pela mera lista de conservações é a hipótese 5:
a coercividade da ação oficial após a remoção das direções de simetria e do
modo conforme. Portanto, a existência integral da sela não pode ser declarada
antes dessa desigualdade ser derivada para a GDQ.

## 6. Cálculo de $P^{\rm phys}$

Seja $\mathbb G_*$ a métrica positiva escolhida no espaço de perturbações
gauge-fixadas e defina

$$
C_*=D\mathcal C(X_*).
$$

Supondo que

$$
C_*\mathbb G_*^{-1}C_*^\dagger
$$

seja inversível no complemento das redundâncias entre vínculos, o projetor
ortogonal sobre o espaço tangente à folha conservada é

$$
P_C
=I-\mathbb G_*^{-1}C_*^\dagger
\left(C_*\mathbb G_*^{-1}C_*^\dagger\right)^{-1}C_*.
$$

Se $R_*$ é o operador infinitesimal das simetrias de gauge/difeomorfismo, o
projetor que remove suas órbitas é

$$
P_R
=I-R_*
\left(R_*^\dagger\mathbb G_*R_*\right)^{-1}
R_*^\dagger\mathbb G_*.
$$

Quando os dois projetores não comutam, a projeção física não é simplesmente
$P_CP_R$. Ela é a projeção ortogonal sobre

$$
\mathcal H_*^{\rm phys}
=\ker C_*\cap\left(\operatorname{Ran}R_*\right)^{\perp_{\mathbb G_*}},
$$

obtida pelo projetor conjunto

$$
\boxed{
P^{\rm phys}
=I-\mathbb G_*^{-1}A_*^\dagger
\left(A_*\mathbb G_*^{-1}A_*^\dagger\right)^{+}A_*,
}
$$

com

$$
A_*
=\begin{pmatrix}
C_*\\
R_*^\dagger\mathbb G_*
\end{pmatrix},
$$

e $(\cdot)^+$ a pseudoinversa de Moore--Penrose. Essa fórmula inclui, de uma
só vez, conservação de probabilidade, carga, fluxo, energia--momento, momento
angular, interface e remoção das direções de simetria.

## 7. Hessiana física

A Hessiana relevante não é somente $D^2\mathcal S$. Em presença de vínculos,
é a Hessiana do funcional aumentado:

$$
\mathbb H_*
=D_X^2\mathscr L(X_*,\lambda_*)
=D^2\mathcal S_{\rm GDQ}(X_*)
-\sum_a\lambda_*^aD^2\mathcal C_a(X_*).
$$

O operador físico é

$$
\boxed{
K_*^{\rm phys}
=P^{\rm phys\dagger}\mathbb H_*P^{\rm phys}
\big|_{\mathcal H_*^{\rm phys}}.
}
$$

Essa expressão mostra por que os multiplicadores de conservação afetam o
espectro sem modificar a ação fundamental.

## 8. Verificação do gap

No domínio global compacto, uma realização elíptica auto-adjunta de
$K_*^{\rm phys}$ possui espectro discreto. Depois de retirar os zeros exatos
de Noether, defina

$$
\Delta_\varepsilon
=\inf\left{
\frac{\langle\eta,K_{*,\varepsilon}^{\rm phys}\eta\rangle}
{\|\eta\|^2}:\;
0\neq\eta\in\mathcal H_{*,\varepsilon}^{\rm phys}
\right}.
$$

Há estabilidade linear se

$$
\Delta_\varepsilon>0.
$$

A ponte global--local requer a afirmação mais forte

$$
\inf_{0<\varepsilon<\varepsilon_0}\Delta_\varepsilon>0.
$$

Conservação de carga e de fluxo impede a mistura com setores de carga
distinta, mas não fornece o sinal desse quociente de Rayleigh. O valor do gap
só pode ser calculado depois de obter $X_*$ e $\lambda_*$ e substituir seus
coeficientes em $K_*^{\rm phys}$.

## 9. Resultado da reconstrução

Foi construído diretamente a partir da ação e das conservações:

1. o problema variacional bulk--interface;
2. a folha física de vínculos;
3. a condição natural de colagem;
4. o projetor físico completo;
5. a Hessiana correta com multiplicadores;
6. o teste exato de estabilidade e de gap uniforme.

O que ainda não foi matematicamente produzido é:

$$
\boxed{
\text{uma estimativa coerciva da ação oficial e a solução }(X_*,\lambda_*)
\text{ do sistema não linear.}
}
$$

Sem esses dois dados, atribuir um número a $\Delta_\varepsilon$ reutilizaria
um background não demonstrado. Assim, esta etapa fecha a construção formal,
mas não a existência nem o gap físico da sela GDQ.
