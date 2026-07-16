# Ponte global--local — DtN exterior e neutralidade global

## 1. Domínio exterior

Considere

$$
M_\varepsilon
=T^4\times S^1_{L_\varepsilon}\times S^3_{R_\varepsilon}
$$

e retire vizinhanças tubulares dos defeitos:

$$
M_{+,\varepsilon}
=M_\varepsilon\setminus
\bigcup_{i=0}^{m}\mathcal N_i.
$$

Cada componente de bordo é

$$
Y_i=\partial\mathcal N_i\simeq S^3.
$$

$Y_0$ é o estômato observado localmente. As demais componentes representam
canais compensadores ou outros defeitos físicos do mesmo setor global.

## 2. Lei global de conservação

No exterior strong-KT,

$$
dH=0.
$$

Pelo teorema de Stokes,

$$
0=\int_{M_{+,\varepsilon}}dH
=\sum_{i=0}^{m}\int_{Y_i}\iota_i^*H,
$$

com as orientações induzidas. Para a carga relativa,

$$
q_i
=\frac1{2\pi}\int_{Y_i}(H-H_{\rm bg}),
$$

segue, quando $H_{\rm bg}$ é uma referência global fechada,

$$
\boxed{
\sum_{i=0}^{m}q_i=0.
}
$$

Essa identidade é a versão torsional da remoção do modo zero na equação de
Green de um espaço compacto. Ela decorre de conservação, não de uma escolha
fenomenológica.

Consequentemente, um único estômato com $q_0\neq0$ não possui exterior
strong-KT compacto com apenas uma componente de bordo. São possíveis:

1. outra componente com carga compensadora;
2. um conjunto de componentes cuja soma seja $-q_0$;
3. uma transgressão global explicitamente derivada, caso $dH$ deixe de ser
   zero num conjunto singular.

Neste documento adota-se a primeira rota, que não altera a ação.

## 3. Ação exterior on shell

Para dados de Dirichlet

$$
\mathbf X_Y=(X_{Y_0},X_{Y_1},\ldots,X_{Y_m}),
$$

resolva a ação oficial no exterior, com:

$$
\sum_iq_i=0,
$$

$$
\int_{M_\varepsilon}\mathcal U,dV=1,
$$

e cargas globais de energia, momento e momento angular fixadas. A solução é

$$
X_+[\mathbf X_Y;\mathbf q,\mathbf j].
$$

A ação exterior on shell define

$$
S_+^{\rm os}(\mathbf X_Y).
$$

Seu gradiente é o DtN não linear matricial:

$$
\boxed{
\mathcal N_{+,i}
=\frac{\delta S_+^{\rm os}}{\delta X_{Y_i}}.
}
$$

## 4. Hessiana e DtN matricial

Linearizando no background exterior,

$$
\boldsymbol\Lambda_+
=D^2S_+^{\rm os}
=
\begin{pmatrix}
\Lambda_{00}&\Lambda_{0c}\\
\Lambda_{c0}&\Lambda_{cc}
\end{pmatrix},
$$

onde o índice $c$ reúne todos os canais compensadores. A simetria da segunda
variação fornece

$$
\Lambda_{c0}=\Lambda_{0c}^\dagger.
$$

Os modos de simetria e o modo constante da medida devem ser projetados antes
da inversão de $\Lambda_{cc}$.

## 5. Eliminação dos canais globais

Se os canais compensadores não são observados localmente, eles respondem
estacionariamente:

$$
\Lambda_{c0}\eta_0
+\Lambda_{cc}\eta_c=0.
$$

No espaço físico,

$$
\eta_c
=-\Lambda_{cc}^{+}\Lambda_{c0}\eta_0,
$$

onde a pseudoinversa remove apenas os zeros exatos de Noether. Substituindo
na ação quadrática, o DtN exterior efetivo visto por $Y_0$ é

$$
\boxed{
\Lambda_+^{\rm eff}
=\Lambda_{00}
-\Lambda_{0c}\Lambda_{cc}^{+}\Lambda_{c0}.
}
$$

Esse complemento de Schur é a retroação global sobre o estômato local. Ele
não pode ser substituído por um fator de Fano ou impedância constante antes
de calcular os blocos.

## 6. Condição final de colagem

O DtN interno vinculado foi derivado em
`ponte_global_local_dtn_interno.md`. A condição não linear é

$$
\widetilde{\mathcal N}_-
+\mathcal N_+^{\rm eff}=0.
$$

No nível linear,

$$
\boxed{
\Lambda_{\rm glue}^{\rm phys}
=P_Y^{\rm phys}
\left(widetilde\Lambda_-+\Lambda_+^{\rm eff}\right)
P_Y^{\rm phys}.
}
$$

O parâmetro de tiro $p_{a,0}$ do colo é determinado pelo zero da condição não
linear. Ele não é calibrado por massa ou acoplamento.

## 7. Gap de interface

Depois de remover os zeros exatos, defina

$$
\Delta_Y
=\inf_{0\neq\eta\in\mathcal T_Y^{\rm phys}}
\frac{
\langle\eta,
(\widetilde\Lambda_-+\Lambda_+^{\rm eff})\eta\rangle
}{\|\eta\|^2}.
$$

A colagem linearmente rígida exige

$$
\Delta_Y>0.
$$

Para a ponte global--local, deve-se mostrar a uniformidade

$$
\inf_{\varepsilon<\varepsilon_0}\Delta_{Y,\varepsilon}>0.
$$

O complemento de Schur reduz a rigidez local por uma forma positiva quando
$\Lambda_{cc}>0$. Portanto, ignorar a retroação global sempre superestima o
gap do estômato.

## 8. Limite global--local

Quando

$$
L_\varepsilon,R_\varepsilon\to\infty,
$$

os canais compensadores se afastam na geometria apontada. Há duas
possibilidades que precisam ser distinguidas:

1. $\Lambda_{0c}\to0$: a compensação permanece global, mas desacopla da
   resposta local;
2. $\Lambda_{0c}\not\to0$: persiste uma memória topológica/global no DtN
   planar.

Qual delas ocorre é uma questão espectral. Não pode ser decidida apenas pela
convergência local da métrica.

## 9. Resultado e pendência concreta

Foi derivada a forma correta do DtN exterior e demonstrada a neutralidade
global das cargas no setor strong-KT compacto. O único objeto ainda não
avaliado é a matriz

$$
\boldsymbol\Lambda_+.
$$

Para calculá-la é necessário especificar a configuração global compensadora
que já pertence ao setor físico — número de componentes, cargas e simetria —
e resolver a Hessiana oficial no exterior. Essa escolha não pode ser inferida
do estômato local isoladamente.

## 10. Configuração mínima selecionada por simetria

Sem introduzir defeitos adicionais desnecessários, a menor configuração
compatível com

$$
\sum_iq_i=0
$$

é

$$
(q_0,q_1)=(q,-q).
$$

No fator esférico global, posicione $Y_1$ no antipolo de $Y_0$. Essa escolha:

1. maximiza a distância geodésica entre os canais;
2. preserva a isotropia axial do par;
3. coincide com a compensação do modo constante do Green em $S^3$;
4. não utiliza nenhum dado experimental.

Pela simetria de troca antipodal, o DtN possui a forma

$$
\boldsymbol\Lambda_+
=\begin{pmatrix}
D&O\\
O&D
\end{pmatrix},
$$

com $D=D^\dagger$ e $O=O^\dagger$ no setor de simetria considerado.

Introduza os canais

$$
\eta_+
=\frac{\eta_0+\eta_1}{\sqrt2},
\qquad
\eta_-
=\frac{\eta_0-\eta_1}{\sqrt2}.
$$

Então

$$
\boldsymbol\Lambda_+
\simeq
\begin{pmatrix}
D+O&0\\
0&D-O
\end{pmatrix}.
$$

O canal $+$ contém o modo global comum e deve ser combinado com a
normalização da medida. O canal $-$ transporta a carga orientada
estômato--antipolo.

Eliminando o traço antipodal, obtém-se

$$
\boxed{
\Lambda_+^{\rm eff}
=D-OD^+O.
}
$$

Quando $D$ e $O$ comutam no harmônico analisado,

$$
\Lambda_+^{\rm eff}
=\frac{(D-O)(D+O)}{D}
$$

no complemento do kernel. Assim, o gap efetivo pode fechar somente se um dos
canais par ou ímpar fechar, ou se $D$ adquirir um zero não removido.

## 11. Relação com o potencial cotangente

Para o setor escalar radial no $S^3_R$, a solução exterior de carga
antipodal tem perfil proporcional a

$$
G_R(\chi)
\propto\frac1R\cot\chi,
$$

entendido com a compensação global e os polos nas duas extremidades. No
limite apontado $r=R\chi$,

$$
\frac1R\cot\frac rR
\longrightarrow\frac1r.
$$

Portanto, a configuração antipodal não é apenas conveniente: ela realiza a
passagem entre o potencial cosmológico cotangente e o potencial local
newtoniano sem violar a conservação global.

### Pendência reduzida

Depois dessa seleção, não é mais necessário determinar uma configuração
compensadora arbitrária. Basta calcular, harmônico a harmônico, os dois
operadores

$$
D_\ell,
\qquad
O_\ell,
$$

da Hessiana oficial no background antipodal.

## 12. Cálculo de referência por canal espectral

Depois de diagonalizar a Hessiana física num canal harmônico, o operador
principal transportado ao longo da geodésica antipodal tem a forma

$$
K_\ell^{(0)}
=-\frac{d^2}{ds^2}+\kappa_\ell^2,
\qquad 0\leq s\leq L.
$$

Esse é o operador de referência de coeficientes congelados, não ainda a
Hessiana completa. Sua solução exata fornece o DtN

$$
\begin{pmatrix}
\pi_0\\
\pi_1
\end{pmatrix}
=
\begin{pmatrix}
D_\ell^{(0)}&O_\ell^{(0)}\\
O_\ell^{(0)}&D_\ell^{(0)}
\end{pmatrix}
\begin{pmatrix}
\eta_0\\
\eta_1
\end{pmatrix},
$$

onde

$$
D_\ell^{(0)}
=\kappa_\ell\coth(\kappa_\ell L),
$$

$$
O_\ell^{(0)}
=-\kappa_\ell\operatorname{csch}(\kappa_\ell L).
$$

O complemento de Schur é

$$
\boxed{
\Lambda_{+,\ell}^{\rm eff,(0)}
=\kappa_\ell\tanh(\kappa_\ell L).
}
$$

Para $\kappa_\ell>0$, ele é estritamente positivo. Para o modo zero,

$$
D_0^{(0)}=\frac1L,
\qquad
O_0^{(0)}=-\frac1L,
$$

e o complemento efetivo tende a zero. Esse é precisamente o modo global que
deve ser removido pela normalização/Noether.

No limite de separação grande,

$$
\Lambda_{+,\ell}^{\rm eff,(0)}
\longrightarrow\kappa_\ell,
$$

enquanto

$$
O_\ell^{(0)}=O(e^{-\kappa_\ell L}).
$$

Logo, no modelo principal, os canais massivos desacoplam
exponencialmente do antipolo e preservam gap; somente o modo zero conserva
memória global de longo alcance.

Para promover esse cálculo a resultado da GDQ, deve-se substituir
$\kappa_\ell^2$ pelo potencial matricial da Hessiana oficial e controlar a
diferença por estimativas de forma/resolvente.
