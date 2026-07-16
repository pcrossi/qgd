# Q42 — Hessiana da sonda e separação Robin

## 1. Segunda variação no espaço de orientações

Escolha localmente \(\boldsymbol B=B\hat z\) e escreva o projetor como

\[
 P=\frac12(I+\boldsymbol n\cdot\boldsymbol\sigma),
 \qquad |\boldsymbol n|=1.
\]

O funcional de sonda por unidade da medida de fronteira é

\[
 V_Z(P)=-\mu B\,\boldsymbol n\cdot\hat z.
\]

Perto dos polos, use coordenadas tangentes
\(\boldsymbol\eta=(\eta_1,\eta_2)\):

\[
 \boldsymbol n_+(\eta)
 =(\eta_1,\eta_2,+\sqrt{1-|\eta|^2}),
\]

\[
 \boldsymbol n_-(\eta)
 =(\eta_1,\eta_2,-\sqrt{1-|\eta|^2}).
\]

Então

\[
 V_Z[n_+]=-mu B+\frac{\mu B}{2}|\eta|^2+O(|\eta|^4),
\]

\[
 V_Z[n_-]=+\mu B-\frac{\mu B}{2}|\eta|^2+O(|\eta|^4).
\]

Logo

\[
 \boxed{\operatorname{Hess}V_Z|_+=+\mu B\,I_2},
 \qquad
 \boxed{\operatorname{Hess}V_Z|_-=-\mu B\,I_2}.
\]

O ramo \(+\) é o mínimo Zeeman e o ramo \(-\) é um ponto estacionário
excitado. A existência de dois resultados no Stern--Gerlach não significa
que ambos sejam mínimos de um fluxo dissipativo.

## 2. Operador Robin localizado

Se a parte normal da Hessiana localizada, restrita ao traço de fronteira, é

\[
 S_{\perp}^{(2)}=
 \frac12\int_{r_c}^{\infty}w(r)
 \langle\partial_r\eta,\mathsf Z_\partial\partial_r\eta\rangle dr,
\]

e a orientação é normalizada de modo que o termo de sonda seja integrado na
mesma medida de bordo, a variação fornece

\[
 -\mathsf Z_\partial\partial_r\eta_\pm
 \pm\mu B\eta_\pm=0
 \quad (r=r_c),
\]

onde \(-\partial_r\) é a normal exterior do domínio. Assim,

\[
 \boxed{
 \mathsf R_{\rm SG}^{\pm}
 =\pm\mathsf Z_\partial^{-1}
 \operatorname{Hess}_P S_{\rm probe}|_{\pm}},
\]

e

\[
 \boxed{(-\partial_r+\mathsf R_{\rm SG}^{\pm})\eta_\pm=0.}
\]

Em uma redução escalar de um modo localizado, um autovalor de
\(\mathsf R_{\rm SG}\) pode ser chamado \(r_B\), com dimensão de comprimento
inverso. O parâmetro diagnóstico adimensional é então

\[
 \boxed{\beta_B=\sqrt\tau\,r_B}.
\]

## 3. O que é e não é determinado

A segunda variação determina exatamente o sinal e a dependência linear em
\(B\). A matriz \(\mathsf Z_\partial\) é a normalização do traço de um modo
localizado da Hessiana, e não a rigidez de uma rotação global. Esta última é

\[
 Z_{\rm bulk}^{\rm global}G^{\rm FS}_{AB}
 =\int d\mu_*\,
 \mathfrak p_{\perp}
 (T_A,\mathbb H_{\rm GDQ}T_B),
 \qquad T_A=\partial_A\Phi(P).
\]

O atlas calculado mostra
\(Z_{\rm bulk}^{\rm global}=0\), como exige a isometria. Isso não torna
\(\mathsf Z_\partial\) singular: ela pertence ao domínio dos modos físicos
localizados excitados pela sonda, depois da projeção de gauge.

Não é matematicamente legítimo definir \(\mathsf Z_\partial=I\) e chamar o resultado de
previsão física. Essa escolha pode ser usada apenas para testar o operador
em normalização canônica.

## 4. Operadores no background gaussiano

Com

\[
 w(r)=r^3e^{-r^2/(4\tau)-F_0},
\]

o setor axial canonicamente normalizado tem operador de Sturm--Liouville

\[
 \boxed{
 L_\pm\eta=-\frac1w\frac{d}{dr}
 \left(w\frac{d\eta}{dr}\right)+V_H(r)\eta,}
\]

com a condição acima e regularidade ponderada no exterior. O potencial
\(V_H\) deve vir dos blocos algébricos da Hessiana acoplada; no teste mínimo
do modo orientacional toma-se \(V_H=0\), explicitamente como diagnóstico do
símbolo principal, não como avaliação final do operador completo.
