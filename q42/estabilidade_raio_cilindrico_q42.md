# Q42 — Estabilidade homogênea do raio cilíndrico na ação GDQ

## 1. Restrição homogênea da própria ação

Considere a família, ainda dentro da ação oficial,

\[
 ds^2=dr^2+a^2d\Omega_3^2,
 \qquad
 F=\frac{r^2}{4\tau}+F_0(a),
 \qquad r\ge0.
\]

A normalização da medida determina

\[
 1=(4\pi\tau)^{-2}
 e^{-F_0}\operatorname{Vol}(S^3_a)
 \int_0^\infty e^{-r^2/(4\tau)}dr,
\]

portanto

\[
 \boxed{
 F_0(a)=3\log\!\left(\frac{a}{2\sqrt\tau}\right)
 +\frac12\log\pi .}
\]

Como

\[
 R=\frac6{a^2},
 \quad
 \left\langle\tau|\nabla F|^2\right\rangle=\frac12,
 \quad
 \langle F\rangle=F_0+\frac12,
\]

o funcional on-shell restrito é

\[
 \boxed{
 \mathcal W_{\rm hom}(a)
 =\frac{6\tau}{a^2}
 +3\log\!\left(\frac{a}{2\sqrt\tau}\right)
 +\frac12\log\pi-3 .}
\]

## 2. Ponto crítico e Hessiana

Sua primeira derivada é

\[
 \mathcal W_{\rm hom}'(a)
 =-\frac{12\tau}{a^3}+\frac3a.
\]

Logo

\[
 \mathcal W_{\rm hom}'(a)=0
 \quad\Longleftrightarrow\quad
 \boxed{a=2\sqrt\tau}.
\]

A segunda derivada é

\[
 \mathcal W_{\rm hom}''(a)
 =\frac{36\tau}{a^4}-\frac3{a^2},
\]

e no ponto estacionário

\[
 \boxed{
 \mathcal W_{\rm hom}''(2\sqrt\tau)
 =\frac{3}{2\tau}>0.}
\]

Portanto, o modo homogêneo que expande ou contrai o raio de toda a garganta
é estável dentro da ação GDQ normalizada.

## 3. Alcance da prova

Este cálculo usa somente curvatura, dilaton e medida da GDQ. Ele não usa
Yang--Mills, campo de Higgs ou ação de Dirac.

A positividade acima exclui o modo homogêneo de colapso radial. Ela não
exclui perturbações dependentes de \(r\), nem modos tensoriais não isotrópicos
em \(S^3\). A prova completa requer a Hessiana acoplada de
\(u(r)=\delta a(r)\) e \(\varphi(r)=\delta F(r)\), sob a restrição

\[
 \int d\mu_*\left(3\frac{u}{a}-\varphi\right)=0,
\]

seguida da remoção do modo de difeomorfismo radial.

