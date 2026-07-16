# Q42 — Completação variacional do estômato

## 1. Por que um termo de contorno é obrigatório

O termo de curvatura da ação oficial contém, a \(\tau\) fixo,

\[
 I_R=C_\tau\int_{M_*}e^{-F}R\,dV_g,
 \qquad
 C_\tau=\frac{\hbar\tau}{\Lambda_C^2}
 \times\text{(normalização positiva)}.
\]

Em uma variedade excisada, a variação de \(R\) contém derivadas normais de
\(\delta g\). O problema de Dirichlet para a métrica induzida torna-se bem
posto adicionando a completação de Gibbons--Hawking ponderada

\[
 \boxed{
 I_{\partial}=2C_\tau
 \int_{\partial M_*}e^{-F}K\,dA_h .}
\]

Este termo não altera a ação oficial no interior: ele cancela somente as
derivadas normais indesejadas da variação métrica no bordo.

## 2. Condição de forma do estômato

Considere uma deformação normal da hipersuperfície,
\(X\mapsto X+\xi n\). A variação da área ponderada obedece, na convenção
\(K=\nabla_an^a\),

\[
 \delta_\xi\int_{\partial M_*}e^{-F}dA
 =\int_{\partial M_*}e^{-F}
 (K-nF)\,\xi\,dA.
\]

Logo a condição estacionária livre, sem tensão superficial adicional, é

\[
 \boxed{K_F:=K-nF=0.}
\]

Esta é uma condição geométrica, independente de coordenadas. Se o estômato
for mantido fixo externamente, \(\xi=0\), ela não é exigida; nesse caso o raio
é dado de contorno. Aqui escolhemos testar o caso dinamicamente livre.

## 3. Seleção do raio no shrinker gaussiano

No domínio exterior \(r\ge r_c\), a normal exterior no bordo interno é
\(n=-\partial_r\). Para

\[
 ds^2=dr^2+r^2d\Omega_3^2,
 \qquad F=\frac{r^2}{4\tau}+F_0,
\]

temos

\[
 K=-\frac3{r_c},
 \qquad
 nF=-\frac{r_c}{2\tau}.
\]

Portanto,

\[
 K_F=-\frac3{r_c}+\frac{r_c}{2\tau},
\]

e a condição variacional seleciona

\[
 \boxed{r_c^2=6\tau},
 \qquad
 \boxed{r_c=\sqrt{6\tau}}.
\]

Assim, o raio deixa de ser um parâmetro independente nesse ramo mínimo.

## 4. Condição linearizada para a Hessiana

Escreva uma perturbação normal da métrica como

\[
 ds^2=(1+2A)dr^2+r^2(1+2C)d\Omega_3^2,
 \qquad F=F_*+\varphi.
\]

A condição física no bordo é a linearização covariante

\[
 \boxed{\delta(K-nF)=0.}
\]

Ela acopla \(A,C,\varphi\) e constitui uma condição Robin matricial para a
Hessiana métrico--dilatônica. Em forma invariante, para variação métrica
\(h_{ab}=\delta g_{ab}\),

\[
 \delta K
 =\frac12\left[
 n(\operatorname{tr}_{\partial}h)
 -2\nabla^i h_{in}
 +\nabla_n h_{nn}
 \right]
 +\text{termos algébricos em }K_{ij}h^{ij},
\]

e

\[
 \delta(nF)=n\varphi+\delta n(F_*).
\]

Portanto, o operador de bordo completo é

\[
 \boxed{
 \mathcal B_F(h,\varphi)
 :=\delta K[h]-n\varphi-\delta n[h](F_*)=0.}
\]

Para uma flutuação puramente dilatônica com métrica de bordo congelada,
reduz-se a \(n\varphi=0\), isto é, Neumann. Uma Robin escalar não nula só
surge depois de eliminar os componentes métricos acoplados ou acrescentar a
resposta física do aparelho.

## 5. Perturbação pelo aparelho

O funcional de sonda já definido na Q42 altera a condição linearizada:

\[
 \mathcal B_F\delta\Phi
 +\mathsf R_{\rm SG}(\boldsymbol B)\delta\Phi=0.
\]

No setor axial, a simetria permite

\[
 \mathsf R_{\rm SG}
 =r_B(\boldsymbol x)\,
 \boldsymbol n_B\cdot\boldsymbol\sigma,
\]

produzindo os dois domínios

\[
 \mathcal B_F\delta\Phi_\pm\pm r_B\delta\Phi_\pm=0.
\]

O coeficiente \(r_B\) deve ser obtido da segunda variação do funcional de
sonda e do mapa \(\mathcal D_\Phi P\). Ele não é determinado pela completação
Gibbons--Hawking, que fixa apenas a parte geométrica comum.

## 6. Alcance e limitação

A condição \(K_F=0\) fecha variacionalmente o raio e fornece o domínio comum
da Hessiana. Ela não produz sozinha:

- o mapa axial \(\mathcal D_\Phi P\);
- a intensidade de resposta \(r_B\);
- a mobilidade causal e os pesos térmicos.

Logo este passo constrói \(r_c(\tau)\) e a condição Robin **matricial
geométrica**, mas a separação magnética e \(\Gamma_{\rm SG}\) ainda requerem
a resposta linear do aparelho.

