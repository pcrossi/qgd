# Q42 — Shrinker cilíndrico e potencial axial de Hopf

## 1. Segundo background estacionário exato

Considere

\[
 M_\perp=\mathbb R_+\times S^3_a,
 \qquad
 ds_\perp^2=dr^2+a^2d\Omega_3^2,
 \qquad
 F(r)=\frac{r^2}{4\tau}+F_0.
\]

Na direção radial,

\[
 \operatorname{Ric}_{rr}=0,
 \qquad F''=\frac1{2\tau}.
\]

Na esfera tridimensional,

\[
 \operatorname{Ric}_{S^3}=\frac2{a^2}g_{S^3},
 \qquad \nabla^2F|_{S^3}=0.
\]

Logo

\[
 \operatorname{Ric}+\nabla^2F=\frac1{2\tau}g
\]

seleciona

\[
 \boxed{a^2=4\tau},
 \qquad
 \boxed{a=2\sqrt\tau}.
\]

Este é o shrinker cilíndrico de Perelman. Diferentemente do ramo gaussiano
plano, ele contém uma garganta \(S^3\) de raio não nulo.

## 2. Contorno variacional

No bordo \(r=0\), a normal exterior é \(n=-\partial_r\). Como a seção
\(S^3\) tem raio constante,

\[
 K=0.
\]

Além disso,

\[
 nF|_{r=0}=0.
\]

Portanto,

\[
 \boxed{K-nF=0}
\]

sem ajuste. O bordo é uma garganta ponderadamente mínima.

Com a convenção normal de kernel em quatro dimensões,

\[
 (4\pi\tau)^{-2}
 \int_0^\infty dr\int_{S^3_a}dA,e^{-F}=1,
\]

e \(a=2\sqrt\tau\), obtém-se

\[
 \boxed{F_0=\frac12\log\pi}.
\]

## 3. Potencial axial derivado da geometria de Hopf

As três componentes do mapa de Hopf

\[
 n:S^3\longrightarrow S^2
\]

são polinômios harmônicos homogêneos de grau \(l=2\) nas coordenadas de
\(S^3\). Para uma esfera de raio \(a\),

\[
 -\Delta_{S^3_a}n_i
 =\frac{l(l+2)}{a^2}n_i
 =\frac8{a^2}n_i.
\]

Como \(a^2=4\tau\), o bloco angular da Hessiana produz

\[
 \boxed{V_H=\frac2\tau}.
\]

Esse potencial não foi escolhido para localizar o modo: ele é o autovalor
do harmônico de Hopf no background estacionário.

## 4. Problema Dirichlet--to--Neumann

Em \(x=r/\sqrt\tau\), o perfil radial axial satisfaz

\[
 \boxed{-\eta''+\frac{x}{2}\eta'+2\eta=0},
 \qquad
 \eta(0)=1,
 \qquad
 \eta(\infty)=0.
\]

Equivalentemente,

\[
 -\frac1{e^{-x^2/4}}
 \frac d{dx}\left(e^{-x^2/4}\eta'\right)+2\eta=0.
\]

O coeficiente adimensional de Dirichlet--to--Neumann é

\[
 \boxed{z_H=-\eta'(0)>0}.
\]

A solução decrescente é, após normalização em \(x=0\),

\[
 \eta(x)=
 \frac{U\!\left(2,\frac12,\frac{x^2}{4}\right)}
 {U\!\left(2,\frac12,0\right)},
\]

onde \(U\) é a função de Tricomi. Usando

\[
 U\!\left(2,\frac12,0\right)=\frac43
\]

e a expansão lateral em \(x=0\), obtém-se

\[
 \boxed{z_H=\frac{3\sqrt\pi}{4}
 =1.329340388179\ldots}.
\]

Restaurando a coordenada física, o resultado para uma textura localizada é

\[
 \boxed{\mathcal N_H
 =\frac{\mathsf Z_\partial}{\sqrt\tau}\,z_H},
\]

na convenção em que a medida comum de bordo foi removida da definição. Assim,

\[
 \boxed{
 \mathsf R_{\rm SG}^{\pm}
 =\pm\mathcal N_H^{-1}
 \operatorname{Hess}_P S_{\rm probe}|_\pm}.
\]

O número \(z_H\) é universal neste ramo. A matriz dimensional
\(\mathsf Z_\partial\) pertence ao traço dos modos localizados. Ela não deve
ser identificada com \(Z_{\rm bulk}^{\rm global}=0\).

## 5. Alcance

O ramo cilíndrico resolve três problemas do ramo plano:

1. possui garganta \(S^3\) real;
2. satisfaz automaticamente a condição de bordo ponderada;
3. fornece \(V_H=2/\tau>0\), removendo o modo axial zero.

Ele não prova, sozinho, que este é o estômato físico selecionado globalmente
entre todos os pontos críticos da ação. Essa seleção requer comparar os
valores on-shell e a estabilidade dos ramos admissíveis.
