---
title: "Alpha como média de Einstein"
---

# Alpha como média de Einstein

Esta nota registra a dedução autocontida da normalização geométrica de
$\alpha$ usada no Capítulo 16. Ela substitui a necessidade de consultar
arquivos históricos externos ao manuscrito.

## 1. Enunciado

A constante de estrutura fina deve ser obtida como normalização efetiva do
canal eletromagnético primitivo, não como valor experimental inserido.

No espaço cosmológico de Einstein:

$$
K_E=T^5\times S^3,
$$

o canal elétrico é representado por um gerador primitivo $U(1)_Q$. O bulk
local oficial continua sendo:

$$
M=\mathbb R^4\times T^4.
$$

O espaço de Einstein fornece a normalização global; a ponte global--local
transporta essa normalização para a carta laboratorial sob as hipóteses já
declaradas de compatibilidade de fluxo, corrente simplética e ausência de fuga
do canal fotônico.

## 2. Hessiana efetiva do canal elétrico

A segunda variação da ação oficial restrita ao modo horizontal $U(1)_Q$ gera
um coeficiente direto:

$$
Z_{Q,\rm dir}^E
=
\frac{\hbar}{\Lambda_C^2}
\mathfrak P_\gamma
\left[
\tau
\int_{K_E}
\mathcal U_*
\lVert\xi_Q\rVert_{q_*}^2
dV_{q_*}
\right].
$$

Aqui $\xi_Q$ é o campo interno primitivo da carga e $\mathfrak P_\gamma$ indica
o pullback causal ao contorno $\gamma$.

Como os modos ortogonais respondem linearmente à fonte elétrica, a rigidez
observada não é apenas $Z_{Q,\rm dir}^E$. Ela é o complemento de Schur da
Hessiana física:

$$
Z_Q^E
=
v^T
\left(
Z_{QQ}
-
Z_{Q\perp}Z_{\perp\perp}^{-1}Z_{\perp Q}
\right)
v.
$$

Em unidades naturais:

$$
\alpha_E
=
\frac{1}{4\pi Z_Q^E}.
$$

Esse é o ponto em que a GDQ substitui a linguagem de acoplamento livre por
uma impedância geométrica calculável.

## 3. Ensemble de câmaras e origem de $1920$

Seja $W(D_5)$ o grupo de Weyl:

$$
W(D_5)\simeq(\mathbb Z_2)^4\rtimes S_5,
\qquad
|W(D_5)|=2^4 5!=1920.
$$

O número $1920$ não é holonomia local nem ajuste. Ele entra como cardinalidade
da órbita cosmológica completa quando o background inteiro é transportado por
pullback:

$$
\Phi_a=(g_a,J_a,H_a,f_a,\mathcal U_a,Q_a),
\qquad
\Phi_{\gamma a}=\gamma^*\Phi_a.
$$

Como a ação oficial é covariante por pullback,

$$
\mathcal S_{\rm GDQ}[\Phi_{\gamma a}]
=
\mathcal S_{\rm GDQ}[\Phi_a].
$$

No ensemble isotrópico, todas as câmaras da órbita têm o mesmo peso:

$$
w_a=\frac1{|W(D_5)|}.
$$

Logo o peso angular de uma câmara fundamental nos cinco ângulos é:

$$
\mathcal V_{\rm chamber}
=
\frac{\pi^5}{1920}.
$$

A restrição é importante: se um eixo externo for congelado antes da média, o
grupo físico se reduz ao estabilizador desse eixo e não se pode dividir por
$1920$ sem dupla contagem. A fórmula abaixo usa a órbita completa transportada.

## 4. Raiz quarta como média geométrica

A resposta física observada em quatro direções não deve ser a soma dos
autovalores nem o volume bruto. Para um tensor positivo de complacência
$\mathsf C_E$, a escala multiplicativa invariável sob mudança de base é:

$$
C_E
=
\left(
\det\mathsf C_E
\right)^{1/4}.
$$

No ensemble isotrópico, a órbita distribui o peso da câmara igualmente entre
as quatro direções físicas. A construção adota a identificação constitutiva:

$$
\det\mathsf C_E
=
\frac{\pi^5}{1920},
$$

e:

$$
C_E
=
\left(
\frac{\pi^5}{1920}
\right)^{1/4}.
$$

Assim, a raiz quarta não é artifício dimensional: ela é a média geométrica da
complacência física em quatro direções. O passo
$\det\mathsf C_E=\pi^5/1920$ é a hipótese específica da classe de ensemble;
ele não segue apenas da isotropia ou do lema de Schur.

## 5. Projetor isotrópico como contração da Hessiana

A covariância por pullback implica:

$$
[K_{\rm phys},\gamma]=0,
\qquad
\gamma\in W(D_5).
$$

Depois da média sobre a órbita completa, o subespaço físico de quatro direções
é isotrópico. Pelo lema de Schur:

$$
K_{\rm phys}\big|_{\mathscr H_{\rm phys}^{(4)}}
=
\lambda_E\mathbf 1_4,
\qquad
\lambda_E>0.
$$

Logo:

$$
K_{\rm phys}^{-1}\big|_{\mathscr H_{\rm phys}^{(4)}}
=
\lambda_E^{-1}\mathbf 1_4.
$$

Na razão projetiva que define o canal elétrico, $\lambda_E^{-1}$ cancela. O
restante é uma contração angular/torsional:

$$
\mathcal P_{\rm iso}
=
\frac1{\pi^4}
\left\langle
\Pi_{\rm circ}^2
\right\rangle_{\rm Hopf}.
$$

No eixo Hopf unitário $u\in S^3$, o momento de Haar usado é:

$$
\left\langle
(n\cdot u)^4
\right\rangle_{S^3}
=
\frac18.
$$

A contração coerente das três direções Cartan--Schouten preservadas pela
torção paralelizante entra como $3^2$. Portanto:

$$
\mathcal P_{\rm iso}
=
\frac1{\pi^4}
\frac18
3^2
=
\frac9{8\pi^4}.
$$

## 6. Resultado

A expressão resultante é:

$$
\alpha_E^{\rm mean}
=
\frac{9}{8\pi^4}
\left(
\frac{\pi^5}{1920}
\right)^{1/4}.
$$

Ela combina dois fatores:

1. a média geométrica dos quatro autovalores físicos da complacência global;
2. o projetor isotrópico do canal elétrico.

A câmara fundamental do toro cosmológico tem peso:

$$
\mathcal V_{\rm chamber}
=
\frac{\pi^5}{1920}.
$$

A média geométrica nas quatro direções observáveis é:

$$
C_E
=
\left(
\mathcal V_{\rm chamber}
\right)^{1/4}.
$$

O projetor isotrópico é:

$$
\mathcal P_{\rm iso}
=
\frac{9}{8\pi^4}.
$$

Portanto:

$$
\alpha_E^{\rm mean}
=
\mathcal P_{\rm iso}C_E.
$$

Numericamente:

$$
\left(
\alpha_E^{\rm mean}
\right)^{-1}
=
137.036082448164\ldots.
$$

E a impedância equivalente é:

$$
Z_Q^E
=
\frac1{4\pi\alpha_E^{\rm mean}}
=
10.904984951787\ldots.
$$

Comparação metrológica, sem usar o valor aceito na construção:

$$
\alpha_{\rm ref}^{-1}\simeq137.035999,
\qquad
\frac{
137.036082448164-137.035999
}{
137.035999
}
\simeq
6.1\times10^{-7}.
$$

## 7. Diagnóstico DtN/Schur redondo

Uma aproximação redonda local usa um kernel fotônico radial $K_0$ acoplado a
uma impedância de Dirichlet--to--Neumann do primeiro harmônico em uma 4-bola:

$$
K_\partial^{\rm DtN}
=
\pi^2R^2.
$$

O complemento de Schur reduzido é:

$$
Z_{Q,\rm red}^E
=
\frac{
K_0K_\partial^{\rm DtN}
}{
K_0+K_\partial^{\rm DtN}
}.
$$

Com os valores preservados do teste redondo:

$$
K_0=15.162605758555,
\qquad
K_\partial^{\rm DtN}=39.415718607388,
$$

obtém-se:

$$
\left(
\alpha_{\rm DtN}^{\rm red}
\right)^{-1}
=
137.604601778653.
$$

Esse resultado é diagnóstico, não fechamento final: ele mostra a escala
correta da impedância de contorno, mas ainda pertence à classe redonda local,
não à média cosmológica isotrópica.

## 8. Status

Classificação: teorema condicional. O número de $\alpha$ está derivado dentro
da classe de ensemble isotrópico de Einstein, com transporte global--local do
canal fotônico. A condição remanescente é verificar se o background global
real pertence a essa classe ou se requer uma média menos simétrica.
