# Q42 — Cálculo de \(Z_H\) e teste de localização axial

## 1. Definição intrínseca

Fixe uma pequena orientação axial \(\eta_\partial\) no estômato. O campo no
exterior deve ser a solução que minimiza a forma quadrática da Hessiana com
esse valor de bordo. A ação on-shell define o operador
Dirichlet--to--Neumann:

\[
 S_{\rm on-shell}^{(2)}
 =\frac12\langle\eta_\partial,
 \mathcal N_H\eta_\partial\rangle,
\qquad
 \mathcal N_H=-Z_{\rm bulk}\,n\cdot D\eta|_{r_c}.
\]

No setor isotrópico, \(\mathcal N_H=Z_H I_2\). Esta é a definição não
ambígua de \(Z_H\).

## 2. Aplicação ao shrinker gaussiano

No background construído, mantendo apenas o símbolo principal axial,

\[
 Q[\eta]=\frac{Z_{\rm bulk}}2
 \int_{r_c}^{\infty}w(r)|\eta'(r)|^2dr,
 \qquad
 w(r)=r^3e^{-r^2/(4\tau)}.
\]

A equação de Euler--Lagrange é

\[
 (w\eta')'=0.
\]

Uma solução de energia finita que tenda a zero no infinito exigiria

\[
 \eta(r)=C\int_r^\infty\frac{ds}{w(s)}.
\]

Mas

\[
 \int_r^\infty\frac{ds}{w(s)}
 =\int_r^\infty s^{-3}e^{s^2/(4\tau)}ds=\infty.
\]

Logo não existe minimizador localizado clássico com
\(\eta(r_c)=1\), \(\eta(\infty)=0\) para o operador sem potencial.

Mais fortemente, escolha funções teste \(\eta_R\) iguais a 1 até \(R\), que
decaem em uma camada de largura \(L\) e são zero depois de \(R+L\). Então

\[
 Q[\eta_R]
 \lesssim
 \frac{Z_{\rm bulk}}{2L^2}
 \int_R^{R+L}r^3e^{-r^2/(4\tau)}dr
 \xrightarrow{R\to\infty}0.
\]

Portanto,

\[
 \boxed{\inf Q=0},
 \qquad
 \boxed{Z_H=0}
\]

no shrinker gaussiano puro com \(V_H=0\).

## 3. Interpretação

O resultado não é uma falha numérica. A rotação axial global é um modo zero
do background isotrópico, e o peso gaussiano permite deslocar a transição
para uma região de medida exponencialmente pequena. Assim, o shrinker plano
resolve as equações estacionárias de bulk, mas não representa sozinho um
estômato que localize rigidez de spin.

Consequentemente, a antiga parametrização escalar

\[
 r_B=\mu B/Z_H^{\rm global}
\]

não pode ser usada: com \(Z_H^{\rm global}=0\), ela divide por um modo de
isometria. O teste anterior com \(\beta_B=0.05\) continua válido
somente como teste do operador Robin, não como aproximação convergente ao
background físico.

## 4. Ingrediente mínimo necessário

Para obter resposta localizada positiva, a Hessiana axial deve conter pelo menos um dos seguintes
efeitos derivados da solução do estômato:

1. potencial localizado positivo \(V_H(r)\) produzido pelos blocos
   métrico--dilatônicos acoplados;
2. conexão axial não trivial cujo termo \(|D_r\eta|^2\) não admita o modo
   global constante;
3. termo cinético de bordo induzido pela completação física do defeito;
4. segundo patch/campo geométrico necessário à classe de Hopf, ausente no
   escalar global homogêneo.

Se \(V_H\ge0\) e não identicamente nulo no suporte acoplado, o problema

\[
 -w^{-1}(w\eta')'+V_H\eta=0,
 \quad \eta(r_c)=1,
 \quad \eta(\infty)=0
\]

pode fornecer

\[
 Z_H=Z_{\rm bulk}[-n\cdot\eta'(r_c)]>0.
\]

O próximo passo não é ajustar \(Z_H\), mas derivar \(V_H\) da Hessiana
acoplada de uma solução de estômato não homogênea.
