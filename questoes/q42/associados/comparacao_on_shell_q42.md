# Q42 — Comparação on-shell dos backgrounds estacionários

## 1. Funcional reduzido

Na fatia normal real de dimensão quatro, use

\[
 \mathcal W_4[g,F,\tau]
 =\int_M
 \left[\tau(R+|\nabla F|^2)+F-4\right]d\mu
 +2\tau\int_{\partial M}\mathcal U K,dA,
\]

com \(\int_Md\mu=1\). O segundo termo é a completação ponderada necessária
na variedade com bordo.

## 2. Exterior gaussiano variacional

Para

\[
 x=\frac{r^2}{4\tau},
 \qquad x_c=\frac32,
\]

a distribuição radial não condicionada é Gamma de forma 2. No exterior,

\[
 Q_2(x_c)=e^{-x_c}(1+x_c),
 \qquad F_0=\log Q_2(x_c).
\]

A média condicionada é

\[
 \langle x\rangle_{x\ge x_c}
 =\frac{x_c^2+2x_c+2}{x_c+1}
 =2.9.
\]

Como \(R=0\),

\[
 \mathcal W_{\rm bulk}^{\rm G}
 =2\langle x\rangle+F_0-4
 =1.8+F_0.
\]

O termo de bordo é

\[
 \mathcal W_{\partial}^{\rm G}
 =-\frac{3x_c}{1+x_c}=-1.8.
\]

Logo

\[
 \boxed{\mathcal W_{\rm G}=F_0
 =\log\!\left(\frac52e^{-3/2}\right)}
 =-0.5837092681\ldots
\]

## 3. Shrinker cilíndrico de Hopf

No cilindro \(\mathbb R_+\times S^3_{2\sqrt\tau}\),

\[
 \tau R=\frac32,
 \qquad
 \langle\tau|\nabla F|^2\rangle=\frac12,
 \qquad
 \langle F\rangle=\frac12+\frac12\log\pi.
\]

Como \(K=0\) no bordo,

\[
 \boxed{
 \mathcal W_{\rm cyl}
 =\frac12\log\pi-\frac32}
 =-0.9276350571\ldots
\]

e

\[
 \boxed{\mathcal W_{\rm cyl}-\mathcal W_{\rm G}
 =-0.3439257890\ldots<0.}
\]

Assim, dentro desta redução normalizada, o ramo cilíndrico possui menor valor
on-shell que o exterior gaussiano livre.

## 4. O que a comparação prova

A desigualdade mostra preferência variacional entre esses dois candidatos
na fatia normal e na convenção de bordo adotada. Ela não prova estabilidade
completa do cilindro: shrinkers cilíndricos podem possuir modos de neckpinch
fora do setor axial. É necessário calcular a Hessiana em todos os blocos
métrico--dilatônicos, remover gauge e contar seus modos negativos.

No setor axial de Hopf, entretanto, o potencial \(V_H=2/\tau\) e o
coeficiente \(z_H=3\sqrt\pi/4\) já provam positividade da resposta radial.

## 5. Auditoria de \(Z_{\rm bulk}\)

O prefator da ação oficial determina a norma de qualquer deformação
\(T_A=\partial_A(g,f,\bar f)\) **depois** que esse mapa é conhecido. Porém, a
ação atual não fornece uma fórmula global

\[
 P\longmapsto(g(P),f(P),\bar f(P)).
\]

Identificar diretamente as três componentes de Hopf \(n_i\) com o único
escalar complexo global \(f\) é impossível globalmente e contradiz a análise
de Chern já registrada na Q42. Portanto, o número universal \(z_H\) foi
derivado, mas \(Z_{\rm bulk}\) não pode ser reduzido somente ao prefator
\(\hbar\tau/\Lambda_C^2\) sem especificar o pullback axial.

O fechamento mínimo é construir \(T_A\) como deformação métrica/conexão em
dois patches do fibrado de Hopf e então avaliar

\[
 Z_{\rm bulk}G^{\rm FS}_{AB}
 =\int_{S^3}d\mu_*
 \,\mathfrak p_2(T_A,\mathbb H_{\rm GDQ}T_B).
\]

