# Q37 — cálculo de $Z_Q^E$ a partir da ação oficial

## 1. Objetivo

Calcular o coeficiente do modo eletromagnético primitivo no background global
de Einstein sem inserir o valor experimental de $\alpha$.

O cálculo distingue:

1. o coeficiente direto produzido pela curvatura da ação oficial;
2. a correção por retroação dos demais campos, dada pelo complemento de Schur;
3. a fórmula cosmológica histórica proposta para $\alpha$.

## 2. Ansatz geométrico do modo $U(1)_Q$

Seja $K$ a parte compacta do background e $\xi_Q$ o campo de Killing da
direção elétrica primitiva. A deformação horizontal é escrita como

$$
ds_8^2
=h_{ab}(x)dx^a dx^b
+q_{mn}(y)
\left(dy^m+\xi_Q^m A_a dx^a\right)
\left(dy^n+\xi_Q^n A_b dx^b\right).
$$

Na normalização vigente da rede de cargas,

$$
\xi_Q=2\,\partial_{\theta_1}.
$$

O desenvolvimento da curvatura escalar em segunda ordem fornece

$$
\mathcal R_8
=\mathcal R_4+\mathcal R_K
-\frac14\lVert\xi_Q\rVert_q^2
F_{ab}F^{ab}
+O(A^3,\nabla q),
$$

onde $F=dA$. Essa é uma identidade da redução métrica; não foi acrescentado
um termo de Yang--Mills à ação.

## 3. Coeficiente direto da ação oficial

Na ação oficial, o termo de curvatura aparece como

$$
\frac{\hbar}{\Lambda_C^2}\,
\tau\mathcal R\,
\mathcal U\,dV_g\,\frac{d\tau}{\tau}.
$$

Depois da projeção causal normalizada

$$
\mathfrak P_\gamma[F]
=\frac{1}{2\pi i w_\gamma}
\oint_\gamma F(\tau)\frac{d\tau}{\tau},
$$

a parcela quadrática direta é

$$
\mathcal S_Q^{(2),\mathrm{dir}}
=-\frac14 Z_{Q,\mathrm{dir}}^E
\int_{N^4}F_{ab}F^{ab}\,dV_h,
$$

com

$$
\boxed{
Z_{Q,\mathrm{dir}}^E
=\frac{\hbar}{\Lambda_C^2}
\mathfrak P_\gamma\!\left[
\tau\int_K
\mathcal U_*(y,\tau)
\lVert\xi_Q\rVert_{q_*}^2
\,dV_{q_*}
\right].
}
$$

Essa é a avaliação direta de $Z_Q^E$ que segue da ação oficial antes da
eliminação das demais flutuações.

Para um ciclo homogêneo de raio $R_1$,

$$
\lVert\xi_Q\rVert_{q_*}^2=4R_1^2.
$$

Se a medida interna é normalizada em cada corte,

$$
\int_K\mathcal U_*dV_{q_*}=1,
$$

então

$$
Z_{Q,\mathrm{dir}}^E
=\frac{4\hbar R_1^2}{\Lambda_C^2}
\mathfrak P_\gamma[\tau],
$$

quando $R_1$ é constante em $K$ e em $\tau$. Em geral, deve-se manter a média
ponderada de $\lVert\xi_Q\rVert^2$ dentro da integral causal.

## 4. Complemento de Schur

Num background warped ou torsional, o modo $A$ pode acoplar-se às demais
flutuações físicas. A normalização completa é

$$
\boxed{
Z_Q^E
=Z_{Q,\mathrm{dir}}^E+\Delta Z_Q^E,
}
$$

onde

$$
\Delta Z_Q^E
=-\frac{
\left\langle
K_{\perp Q}\eta_Q(A),
K_{\perp\perp}^{-1}K_{\perp Q}\eta_Q(A)
\right\rangle
}{
\frac12\displaystyle\int_{N^4}F_A\wedge\star_hF_A
}.
$$

No background produto exatamente homogêneo, a simetria pode anular
$K_{\perp Q}$ por ortogonalidade de representações. Isso precisa ser
verificado na Hessiana; não pode ser presumido num background warped.

## 5. Relação correta com $\alpha$

Para um único gerador já canonicamente normalizado e com carga primitiva
unitária,

$$
e_E^2=(Z_Q^E)^{-1},
\qquad
\boxed{
\alpha_E=\frac{1}{4\pi\hbar c\,Z_Q^E}.
}
$$

Antes de canonizar uma mistura de geradores, a expressão correta é matricial.
Se $A^a=v^aA_Q$, $\mathbf Z$ é a matriz cinética e
$\mathbf q_{\min}$ é o vetor de cargas primitivas da matéria, então

$$
\boxed{
\alpha_E
=\frac{(\mathbf q_{\min}^{T}v)^2}
{4\pi\hbar c\,v^T\mathbf Z v}.
}
$$

Essa razão é invariante sob a reescala de $v$. Escolhendo
$\mathbf q_{\min}^{T}v=1$, tem-se $Z_Q=v^T\mathbf Z v$. Reescalar apenas o
gerador, apenas a carga ou apenas a norma produz um fator espúrio.

Em unidades $\hbar=c=1$, a fórmula cosmológica histórica

$$
\alpha_{\rm cos}
=\frac{9}{8\pi^4}
\left(\frac{\pi^5}{1920}\right)^{1/4}
$$

corresponde à exigência

$$
\boxed{
Z_{Q,\rm cos}^E
=\frac{1}{4\pi\alpha_{\rm cos}}
=10{,}904984951787\ldots
}
$$

A coincidência procurada é, portanto, a identidade concreta

$$
\boxed{
\frac{\hbar}{\Lambda_C^2}
\mathfrak P_\gamma\!\left[
\tau\int_K\mathcal U_*
\lVert\xi_Q\rVert^2dV_{q_*}
\right]
+\Delta Z_Q^E
=10{,}904984951787\ldots
}
$$

em unidades naturais.

## 6. Auditoria do fator de volume

Se $\mathcal U_*$ está normalizada, um volume compacto bruto é absorvido pela
constante de normalização da medida. Assim, $6\pi^5$ não pode ser extraído uma
segunda vez apenas por ser chamado de volume global. Ele só pode reaparecer se
for resultado da média ponderada

$$
\int_K\mathcal U_*\lVert\xi_Q\rVert^2dV_{q_*},
$$

da integral causal ou do complemento de Schur.

Além disso, para métricas produto de raios unitários na convenção usual,

$$
\operatorname{Vol}(T^5\times S^3)
=(2\pi)^5(2\pi^2)=64\pi^7,
$$

e não $6\pi^5$. Portanto qualquer ocorrência de $6\pi^5$ exige métricas,
raios e normalização próprios explicitamente declarados; não é o volume
canônico do produto unitário.

## 7. Resultado

O item 1 foi reduzido a uma expressão direta da ação oficial:

$$
Z_Q^E
=\frac{\hbar}{\Lambda_C^2}
\mathfrak P_\gamma\!\left[
\tau\int_K\mathcal U_*
\lVert\xi_Q\rVert^2dV_{q_*}
\right]
+\Delta Z_Q^E.
$$

Essa fórmula mostra exatamente como provar a coincidência com a expressão
cosmológica. Os documentos atuais ainda não fornecem $q_*(y,\tau)$,
$f_*(y,\tau)$, o pullback explícito de $\gamma$ e o bloco
$K_{\perp Q}$ necessários para avaliar seu lado esquerdo. Logo, a igualdade
numérica não foi demonstrada: o número do lado direito é o valor requerido
pela fórmula candidata, não uma avaliação independente da Hessiana.

O próximo cálculo não é escolher outro fator. É inserir o background global
estacionário real nessa integral e calcular $\Delta Z_Q^E$.

## 8. Avaliação dos backgrounds atualmente disponíveis

Foram executados, sem alteração de parâmetros:

1. `questoes/q29/associados/solve_background_bismut_l1_q29.py`;
2. `questoes/q29/associados/warp_oficial_t5_s3.py`;
3. `questoes/q29/associados/test_modulos_t5_acao_oficial.py`.

O primeiro fornece a norma radial antes da matriz de Gram dos geradores:

$$
\mathcal K_Q=41{,}594825709\ldots,
$$

enquanto a fórmula cosmológica requer

$$
Z_{Q,\rm cos}^E=10{,}904984951787\ldots.
$$

Portanto, a comparação direta entre $\mathcal K_Q$ e $Z_Q^E$ não é legítima.
Para $T_3=\sigma_3/2$ e $Y=I/2$, o background redondo fornece

$$
\mathbf Z_{\rm red}
=\frac{\mathcal K_Q}{4}
\begin{pmatrix}1&0\\0&1\end{pmatrix}.
$$

Cada canal isolado possui

$$
Z_3=Z_Y=\frac{\mathcal K_Q}{4}
=10{,}3987064273\ldots.
$$

Se um deles fosse sozinho o gerador elétrico de carga mínima unitária,
resultaria

$$
\alpha^{-1}=4\pi\frac{\mathcal K_Q}{4}
=130{,}6739989\ldots,
$$

e não $137{,}036082\ldots$. O fator $1/4$ era, portanto, uma normalização
genuinamente ausente na comparação anterior.

Contudo, o fóton físico é o kernel da Hessiana neutra. No background warped
radial já implementado,

$$
\mathbf Z
=\frac{\mathcal K_Q}{4}
\begin{pmatrix}
1&\delta_B\\
\delta_B&1
\end{pmatrix},
\qquad
\delta_B=-0{,}2709378871,
$$

e $v_\gamma=(1,1)$. Na convenção de carga primitiva unitária,

$$
Z_\gamma=v_\gamma^T\mathbf Z v_\gamma
=15{,}1626057595\ldots,
$$

o que dá

$$
\alpha^{-1}=190{,}5389235\ldots.
$$

O quociente entre o valor cosmológico requerido e a norma de um canal
isolado seria

$$
\frac{Z_{Q,\rm cos}^E}{\mathcal K_Q/4}
=1{,}0486866831\ldots,
$$

mas escolher esse número como prefator seria calibração posterior. Além disso,
essa não é a comparação física final enquanto a matriz neutra completa não
estiver correta.

O teste dos módulos de $T^5$ também confirma que, no background steady com
medida normalizada, os módulos toroidais constantes possuem gradiente e
Hessiana nulos. Finalmente, para uma inserção suave constante em $\tau$,

$$
\mathfrak P_\gamma[\tau C]=0.
$$

Logo o background atualmente disponível não calcula o $Z_Q^E$ requerido. Uma
contribuição não nula deve vir de dependência meromorfa/monodromia física do
background causal ou de um bloco não nulo do complemento de Schur, ambos
derivados da ação. Alternativamente, a matriz deve ser recalculada no
background Hermitiano anisotrópico completo, porque a média radial não retém
todas as componentes horizontais. Essa é uma conclusão numérica negativa
útil: a fórmula cosmológica e a norma canônica da Hessiana ainda não coincidem
nos backgrounds já implementados.

## 9. Auditoria dimensional corrigida

Com


$$
X^\mu=\ell_C\widehat X^\mu,
\qquad
F_{\mu\nu}^{\rm phys}=\ell_C^{-2}\widehat F_{\mu\nu},
$$

tem-se

$$
d^4X\,F_{\rm phys}^2
=d^4\widehat X\,\widehat F^2.
$$

Logo a redução Maxwell em quatro dimensões é conforme e não deixa uma potência
residual de $\ell_C$. Na convenção dimensional corrigida,

$$
\mathcal S_{\rm GDQ}=\hbar\widehat{\mathcal I}_{\rm GDQ},
$$

e $\mathbf Z$ é adimensional. Não se pode introduzir posteriormente um fator
$Z_C$ dimensional para corrigir o número. O que faltava na comparação era:

1. a matriz de Gram dos geradores;
2. a diagonalização canônica do setor neutro;
3. a carga mínima expressa na mesma base;
4. possivelmente as componentes horizontais ausentes na truncagem radial.

A análise dimensional remove a antiga ambiguidade de $\Lambda_C$, mas não
transforma $41{,}5948$ diretamente em $10{,}90498$.

## 10. Setores que não podem ser identificados antes da colagem global

Há uma segunda fonte de erro conceitual. A direção elétrica primitiva da Q37
foi inicialmente descrita no setor toroidal $U(1)^4$, enquanto
$\mathcal K_Q=41{,}594825709\ldots$ foi calculado para a fibra de Hopf do
setor neutro eletrofraco em $S^3$. São blocos diferentes antes da identificação
global do gerador físico.

O gerador que deve entrar na fórmula de $\alpha$ é o vetor global

$$
v_Q
\in
\operatorname{Lie}(U(1)^4_{T^4})
\oplus
\operatorname{span}\{T_3,Y\}_{S^3},
$$

selecionado simultaneamente pela carga primitiva, pela Hessiana de massa e
pelas condições de Noether. Sua norma é

$$
Z_Q^E=v_Q^T\mathbf Z_Ev_Q,
$$

onde $\mathbf Z_E$ é a matriz cinética **global**, incluindo blocos toroidais,
de Hopf e cruzados. O solver radial de $S^3$ calcula somente um subbloco dessa
matriz. Portanto a diferença restante não deve ser interpretada como um fator
escalar ausente; ela é, antes de tudo, um bloco matricial ainda não calculado.

O cálculo final deve montar

$$
\mathbf Z_E
=
\begin{pmatrix}
\mathbf Z_{TT}&\mathbf Z_{TH}\\
\mathbf Z_{HT}&\mathbf Z_{HH}
\end{pmatrix}
$$

diretamente da Hessiana oficial em $T^5\times S^3$, determinar $v_Q$ sem usar
$\alpha$ e só então avaliar

$$
\alpha_E
=\frac{(\mathbf q_{\min}^Tv_Q)^2}
{4\pi\hbar c\,v_Q^T\mathbf Z_Ev_Q}.
$$
