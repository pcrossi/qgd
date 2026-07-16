# Ponte global--local da GDQ — Lema 4: localização e gap uniforme

> [!important] Atualização arquitetural
> O gap é transportado do operador físico local pelo limite apontado, sem sela
> global--local. Ver `ponte_global_local_lemas_sem_colar.md`.

## 1. Objetivo

O Lema 4 deve impedir que os modos ligados do estômato se dissolvam no
contínuo durante a descompactificação. O resultado precisa distinguir:

1. modos zero de simetria;
2. modos topológicos protegidos;
3. modos ligados positivos;
4. instabilidades negativas;
5. o espectro essencial do bulk planar.

Este documento demonstra um critério suficiente abstrato e audita sua
aplicação ao operador radial já derivado na Q29. A verificação quantitativa do
critério no background BI permanece aberta.

## 2. Operador físico reduzido

Parta da Hessiana oficial restrita ao espaço tangente dos vínculos. Remova:

1. difeomorfismos infinitesimais;
2. reparametrizações radiais;
3. modos globais de isometria;
4. variações que alteram a carga relativa fixada.

Denote o espaço físico resultante por $\mathcal H_\varepsilon^{\rm phys}$ e a
forma fechada por $q_\varepsilon^{\rm phys}$. O operador auto-adjunto
associado é $K_\varepsilon^{\rm phys}$.

No colar de cohomogeneidade um, sua forma local geral é matricial:

$$
K_\varepsilon^{\rm phys}\eta
=-W_\varepsilon^{-1}
\frac d{dr}
\left(P_\varepsilon\frac{d\eta}{dr}
+C_\varepsilon\eta\right)
+W_\varepsilon^{-1}C_\varepsilon^T\eta'
+W_\varepsilon^{-1}V_\varepsilon\eta.
$$

$W_\varepsilon$ é o peso positivo induzido por
$\mathcal U_\varepsilon dV_{g_\varepsilon}$. A condição de interface deve
anular o concomitante de Green.

## 3. Hipóteses quantitativas de localização

Além de BI, imponha as condições L4.1--L4.6.

### L4.1 — Elipticidade física uniforme

Depois dos vínculos e da projeção física, existem $p_-,p_+>0$ independentes
de $\varepsilon$ tais que

$$
p_-|\xi|^2
\leq
\langle\xi,P_\varepsilon^{\rm phys}(r)\xi\rangle
\leq p_+|\xi|^2.
$$

### L4.2 — Controle do peso

Em compactos e na região assintótica relevante,

$$
0<w_-\leq W_\varepsilon(r)\leq w_+<\infty,
$$

ou valem as desigualdades ponderadas equivalentes depois da conjugação
unitária para $L^2(dr)$.

### L4.3 — Limiar assintótico uniforme

Existe $\Sigma_*>-\infty$ tal que, fora de uma vizinhança uniforme do
estômato,

$$
q_\varepsilon^{\rm phys}[\eta]
\geq
(\Sigma_*-o_R(1))\|\eta\|^2
$$

para funções suportadas em $r>R$, uniformemente em $\varepsilon$. Pelo
critério de Persson, isso implica

$$
\inf\operatorname{spec}_{\rm ess}K_P^{\rm phys}\geq\Sigma_*.
$$

### L4.4 — Estado ligado uniforme

Existe um subespaço teste $F_{a,\varepsilon}$ de dimensão $m_a$ suportado
próximo ao estômato e um $\delta_a>0$ independente de $\varepsilon$ tal que

$$
\sup_{0\ne\eta\in F_{a,\varepsilon}}
\frac{q_\varepsilon^{\rm phys}[\eta]}{\|\eta\|^2}
\leq\Sigma_*-2\delta_a.
$$

Pelo princípio min--max, existem ao menos $m_a$ autovalores abaixo do limiar.

### L4.5 — Separação interna do cluster

Para um intervalo compacto

$$
I_a=[\lambda_a^--\delta_a/2,\lambda_a^++\delta_a/2]
\subset(-\infty,\Sigma_*-\delta_a),
$$

a estimativa min--max no complemento de $F_{a,\varepsilon}$ satisfaz

$$
q_\varepsilon^{\rm phys}[\eta]
\geq(\lambda_a^++\delta_a)\|\eta\|^2,
\qquad
\eta\perp F_{a,\varepsilon},
$$

no setor de simetria considerado. Essa condição exclui autovalores adicionais
que colidam com o cluster.

### L4.6 — Interface uniformemente semilimitada

A forma de interface $b_\varepsilon$ é real, simétrica e relativamente
limitada com constante menor que um:

$$
|b_\varepsilon[\eta]|
\leq a,q_{\varepsilon,0}[\eta]+C\|\eta\|^2,
\qquad 0\leq a<1,
$$

uniformemente. Perturbações de aparelho não fazem parte desta condição de
background; quando incluídas, sua norma de forma deve ser comparada com o
gap obtido.

## 4. Teorema condicional de gap

Sob BI e L4.1--L4.6, existe $\Delta_a>0$, independente de
$\varepsilon$, tal que

$$
\operatorname{dist}
\left(
\operatorname{spec}K_\varepsilon^{\rm phys}\cap I_a,
\operatorname{spec}K_\varepsilon^{\rm phys}\setminus I_a
\right)
\geq\Delta_a.
$$

A dimensão do subespaço espectral associado a $I_a$ é $m_a$.

### Demonstração

L4.3 separa $I_a$ do espectro essencial por pelo menos $\delta_a$. L4.4 e o
princípio min--max produzem $m_a$ autovalores abaixo do limiar. L4.5 fornece a
cota inferior no complemento e impede autovalores adicionais no intervalo.
L4.6 preserva semilimitação e autoadjunticidade pelo teorema de perturbação de
formas. Tomando a menor das separações obtidas,

$$
\Delta_a
=\min\left\{
\delta_a/2,
\operatorname{dist}(I_a,\Sigma_*)
\right\}>0.
$$

Isso demonstra o gap do cluster. A prova não determina que L4.1--L4.6 sejam
verdadeiras para a GDQ; essa verificação depende do background.

## 5. Localização de Agmon

Se $\lambda_{a,\varepsilon}\leq\Sigma_*-\delta_a$ e os coeficientes
satisfazem L4.1--L4.3, escolha

$$
0<\mu<\sqrt{\frac{\delta_a}{p_+}}.
$$

Aplicando a identidade de Agmon a
$e^{\mu d(r,\mathcal N_\varepsilon)}\Phi_{a,\varepsilon}$, com cortes suaves,
obtém-se

$$
\int
e^{2\mu d(x,\mathcal N_\varepsilon)}
|\Phi_{a,\varepsilon}|^2d\mu_\varepsilon
\leq C,
$$

onde $C$ é independente de $\varepsilon$. Consequentemente,

$$
\boxed{
\int_{d(x,\mathcal N_\varepsilon)>R}
|\Phi_{a,\varepsilon}|^2d\mu_\varepsilon
\leq Ce^{-2\mu R}.
}
$$

Para operadores matriciais, os termos de primeira ordem são absorvidos pelas
cotas de forma de L4.6 e pelas estimativas uniformes dos coeficientes.

## 6. Modos zero e estabilidade

Um modo zero não é automaticamente uma partícula ligada estável.

### Zero de simetria

Se $\Phi=\mathcal L_X\mathfrak B$ ou corresponde a uma isometria global, ele
deve ser quocientado ou fixado antes do espectro físico.

### Zero topológico

Um modo associado ao índice pode persistir enquanto a classe e o operador
Fredholm forem preservados. Isso fixa uma diferença de dimensões de kernels,
mas não fornece sozinho localização exponencial nem separação do contínuo.

### Estabilidade física

Depois da remoção dos zeros de simetria, estabilidade linear exige

$$
q_\varepsilon^{\rm phys}[\eta]\geq0.
$$

Um autovalor negativo indica instabilidade do background; não deve ser
reinterpretado como massa física positiva.

## 7. Auditoria do operador radial disponível

O documento `q29/fase1_colar_dinamico_reducao_radial.md` já derivou

$$
\mathcal J\eta
=-\frac d{dr}(P\eta'+C\eta)+C^T\eta'+V\eta
$$

e o concomitante de Green correto. Entretanto, para
$X=(a,c,f)$, sua matriz principal é

$$
P
=\frac{\tau e^{-f}}N
\begin{pmatrix}
4c&4a&-4ac\\
4a&0&-2a^2\\
-4ac&-2a^2&2a^2c
\end{pmatrix},
$$

com

$$
\det P
=16\frac{\tau^3e^{-3f}}{N^3}a^4c>0,
$$

mas assinatura indefinida. Portanto, essa matriz antes dos vínculos não
satisfaz L4.1.

O passo físico obrigatório é:

1. linearizar a restrição do lapse $\delta E_N=0$;
2. eliminar a direção de reparametrização radial;
3. construir a matriz reduzida $P^{\rm phys}$ pelo pullback ao subespaço de
   vínculos, ou pelo complemento de Schur quando o bloco eliminado for
   invertível;
4. calcular os menores autovalores de $P^{\rm phys}(r)$ ao longo da solução
   BI;
5. somente então testar L4.1.

Sem essa redução, um solver pode diagonalizar modos não físicos e produzir um
falso gap.

## 8. Quantidades que precisam ser extraídas do background BI

Para fechar a aplicação do lema, devem ser calculadas sem dados
fenomenológicos:

$$
p_-
=\inf_{\varepsilon,r}
\lambda_{\min}(P_\varepsilon^{\rm phys}(r)),
$$

$$
\Sigma_*
=\liminf_{R\to\infty}
\inf_{\varepsilon}
\inf_{\operatorname{supp}\eta\subset\{r>R\}}
\frac{q_\varepsilon^{\rm phys}[\eta]}{\|\eta\|^2},
$$

$$
\lambda_{a,\varepsilon}
=\inf_{\eta\in\mathcal S_a}
\frac{q_\varepsilon^{\rm phys}[\eta]}{\|\eta\|^2},
$$

e

$$
\delta_a
=\inf_\varepsilon
(\Sigma_*-\lambda_{a,\varepsilon}).
$$

$\mathcal S_a$ é o setor fixado por carga, índice e simetria, não um conjunto
escolhido pela massa experimental.

## 9. Teste numérico legítimo

Depois de congelar um background BI, uma sequência de domínios
$[r_c,R_j]$, $R_j\to\infty$, deve registrar:

1. espectro antes e depois da projeção dos vínculos;
2. assinatura de $P^{\rm phys}$ em cada ponto da malha;
3. autovalores ligados e aproximação do contínuo;
4. massa do modo fora de uma vizinhança fixa;
5. sensibilidade às condições externas;
6. refinamento simultâneo de malha e domínio.

Esse cálculo será teste de consistência e convergência, não prova da
existência do background.

## 10. Relação com o Lema 3

As estimativas de Agmon fornecem ausência de fuga de massa para os modos no
cluster. A elipticidade e a semilimitação uniformes fornecem compacidade local.
Juntas, elas estabelecem a condição liminf de Mosco no setor ligado.
Consequentemente, sob L4.1--L4.6, o Lema 3B fica concluído para esse setor.

## 11. Status

### Demonstrado

1. critério suficiente de gap uniforme;
2. estimativa exponencial uniforme de Agmon;
3. tratamento separado dos modos zero;
4. identificação da redução física necessária no operador radial existente;
5. fechamento do Lema 3B condicionado a L4.1--L4.6.

### Ainda não demonstrado para a GDQ

1. positividade uniforme de $P^{\rm phys}$;
2. valor do limiar $\Sigma_*$;
3. existência de um estado teste abaixo do limiar;
4. separação interna do cluster;
5. gap numérico ou analítico do background físico.

$$
\boxed{
\text{Lema 4 como teorema analítico: demonstrado condicionalmente;}
\qquad
\text{verificação no background GDQ: aberta e dependente de BI.}
}
$$
