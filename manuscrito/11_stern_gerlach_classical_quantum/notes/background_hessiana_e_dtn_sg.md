---
title: "Background, Hessiana e DtN no Stern-Gerlach"
---

# Background, Hessiana e DtN no Stern--Gerlach

## 1. O que esta nota prova

Esta nota completa a cadeia de Stern--Gerlach no nível da GDQ, separando três
camadas:

1. o background estacionário de bulk;
2. o domínio variacional no estômato;
3. a resposta de interface medida pelo aparelho.

A ação oficial não é modificada. O aparelho entra como fonte externa clássica
e como dado de contorno físico.

## 2. Background normal em $\mathbb C^2$

Na fatia normal ao estômato, usamos a métrica radial:

$$
ds_\perp^2=dr^2+a(r)^2d\Omega_3^2,
$$

com dilatão real:

$$
f=F(r).
$$

A equação estacionária métrico--dilatônica do setor de Perelman ponderado
assume a forma:

$$
\operatorname{Ric}+\nabla^2F=\frac{1}{2\tau}g.
$$

Para a métrica acima, os dois blocos independentes são:

$$
-3\frac{a''}{a}+F''=\frac{1}{2\tau},
$$

$$
\frac{2(1-a'^2)-aa''}{a^2}
+\frac{F'a'}{a}
=\frac{1}{2\tau}.
$$

A solução exata de bulk é:

$$
a_\ast(r)=r,
\qquad
F_\ast(r)=\frac{r^2}{4\tau}+F_0.
$$

Para um exterior excisado $r\ge r_c$, a normalização da medida determina:

$$
x_c=\frac{r_c^2}{4\tau},
$$

$$
F_0=\log\left(e^{-x_c}(1+x_c)\right).
$$

O script `construir_background_estacionario_sg.py` verifica numericamente que
o resíduo máximo dessas duas equações é zero, dentro da precisão de máquina,
no domínio truncado usado no teste.

## 3. Obstrução de bordo e condição variacional livre

No bordo interior do exterior excisado, a normal aponta para dentro do buraco:

$$
n=-\partial_r.
$$

Logo:

$$
n(F_\ast)=-\frac{r_c}{2\tau}.
$$

O bulk isolado não fixa sozinho a matriz Robin do estômato. Para um estômato
livre, a completação de bordo ponderada impõe a curvatura média ponderada:

$$
K-n(F)=0.
$$

Como, na hiperesfera de raio $r_c$,

$$
K=-\frac{3}{r_c},
$$

a condição livre fornece:

$$
-\frac{3}{r_c}
-\left(-\frac{r_c}{2\tau}\right)
=0.
$$

Portanto:

$$
r_c^2=6\tau,
\qquad
r_c=\sqrt{6\tau}.
$$

O verificador `verificar_contorno_variacional_sg.py` confirma, para
$\tau=1$:

$$
K-n(F)=-2.22\times10^{-16}.
$$

Essa condição define o domínio geométrico comum da Hessiana. Ela ainda não é
a resposta axial específica do aparelho.

## 4. Fonte clássica de Stern--Gerlach

O aparelho fornece um campo externo $\mathbf B(x,t)$. A direção local é:

$$
\mathbf n(x,t)=\frac{\mathbf B(x,t)}{|\mathbf B(x,t)|}.
$$

O acoplamento reduzido de sonda é:

$$
S_{\rm probe}[\Phi;\mathbf B]
=
-\mu
\int_{\Sigma_{\rm SG}}
d\mu_\Sigma(\Phi)
\operatorname{Tr}
\left(P(\Phi)\,\boldsymbol\sigma\cdot\mathbf B\right).
$$

Aqui $\Phi=(g,f,\bar f)$ e $P(\Phi)$ é o projetor axial reconstruído da
geometria. A fonte linear que entra na Hessiana é:

$$
J_{\rm SG}
=
-\left.
\frac{\delta S_{\rm probe}}{\delta\Phi}
\right|_{\Phi_\ast}.
$$

Separando a variação do projetor da variação de volume:

$$
J_{\rm SG}
=
\mu(\mathcal D_\Phi P)^*
\left(\boldsymbol\sigma\cdot\mathbf B\right)
+J_{\rm vol}.
$$

Para flutuações puramente orientacionais que preservam o volume em primeira
ordem, $J_{\rm vol}=0$.

## 5. Hessiana física e resposta linear

Se $K_{\rm GDQ}[\Phi_\ast]$ é a segunda variação da ação oficial no background
com domínio de bordo fixado, removemos difeomorfismos, fase global e isometrias
pela projeção física:

$$
K_{\rm phys}
=
P_{\rm phys}^\dagger
K_{\rm GDQ}[\Phi_\ast]
P_{\rm phys}.
$$

A resposta linear ao aparelho é:

$$
K_{\rm phys}\,\delta\Phi_{\rm SG}
=
J_{\rm SG}.
$$

No complemento dos modos zero, se o gap é positivo, a solução é:

$$
\delta\Phi_{\rm SG}
=
K_{\rm phys}^{-1}J_{\rm SG}.
$$

Decomposta em autofunções:

$$
K_{\rm phys}\Psi_\nu=\lambda_\nu\Psi_\nu,
\qquad
\lambda_\nu>0,
$$

temos:

$$
\delta\Phi_{\rm SG}
=
\sum_\nu
\frac{\langle\Psi_\nu,J_{\rm SG}\rangle}{\lambda_\nu}
\Psi_\nu.
$$

Esta é a forma correta de obter a deformação do estômato pelo aparelho. Não
há operador quântico externo inserido como ontologia nova.

## 6. Impedância de interface por Schur/DtN

Divida os graus de liberdade em interface $Y$ e interior $I$:

$$
\delta\Phi=(\delta\Phi_Y,\delta\Phi_I).
$$

A Hessiana em blocos é:

$$
K=
\begin{pmatrix}
K_{YY} & K_{YI}\\
K_{IY} & K_{II}
\end{pmatrix}.
$$

Eliminando os graus internos estacionários:

$$
\delta\Phi_I=-K_{II}^{-1}K_{IY}\delta\Phi_Y.
$$

A rigidez vista pelo aparelho é o complemento de Schur:

$$
\mathsf R_{\rm SG}
=
K_{YY}
-K_{YI}K_{II}^{-1}K_{IY}.
$$

Essa é também a interpretação DtN: o aparelho impõe dado de fronteira e a
geometria devolve a derivada normal efetiva.

## 7. Rigidez textural induzida

Projetando a fonte em modos físicos:

$$
j_{\nu A}=\langle\Psi_\nu,J_A\rangle,
$$

e escrevendo o símbolo tangencial como:

$$
\lambda_\nu+Z_\nu k^2+O(k^4),
$$

a ação induzida é:

$$
S_{\rm ind}^{(2)}
=
-\frac12
\langle J_{\rm SG},K_{\rm phys}^{-1}J_{\rm SG}\rangle.
$$

Expandindo em $k$:

$$
\frac{1}{\lambda_\nu+Z_\nu k^2}
=
\frac{1}{\lambda_\nu}
-\frac{Z_\nu}{\lambda_\nu^2}k^2
+O(k^4).
$$

Comparando com a energia de textura em $\mathbb{CP}^1$:

$$
S_{\rm eff}^{(2)}
\supset
\frac12
\int
\kappa_{AB}^{\rm SG}
\partial_aq^A\partial^aq^B\,dV,
$$

obtemos:

$$
\kappa_{AB}^{\rm SG}
=
\sum_\nu
\frac{Z_\nu}{\lambda_\nu^2}
j_{\nu A}^\ast j_{\nu B}.
$$

No background isotrópico:

$$
\kappa_H^{\rm SG}
=
\frac12
(G_{\rm FS})^{AB}
\sum_\nu
\frac{Z_\nu}{\lambda_\nu^2}
j_{\nu A}^\ast j_{\nu B}.
$$

Assim:

$$
\lambda_\nu>0,
\quad
Z_\nu>0,
\quad
j_{\nu A}\ne0
\quad
\Longrightarrow
\quad
\kappa_H^{\rm SG}>0.
$$

## 8. Resultado negativo do gaussiano e ramo cilíndrico de Hopf

O shrinker gaussiano exterior é solução exata de bulk, mas o teste DtN axial
mostra:

$$
Z_H^{\rm gaussiano}=0.
$$

Fisicamente, isso significa que a orientação global escapa para o exterior
sem custo textural. Portanto o gaussiano puro não é o estômato físico completo
para Stern--Gerlach.

O ramo cilíndrico de Hopf:

$$
\mathbb R_+\times S^3_{2\sqrt\tau}
$$

tem harmônico axial $l=2$ e potencial:

$$
V_H=\frac{2}{\tau}.
$$

O problema DtN reduzido é:

$$
-\eta''+\frac{x}{2}\eta'+2\eta=0,
\qquad
\eta(0)=1,
\qquad
\eta(\infty)=0.
$$

Para obter o DtN analiticamente, introduza:

$$
t=\frac{x^2}{4},
\qquad
\eta(x)=y(t).
$$

Então:

$$
\eta'
=
\frac{x}{2}y_t,
\qquad
\eta''
=
\frac12y_t+ty_{tt},
$$

e a equação radial torna-se:

$$
ty_{tt}
+
\left(
\frac12-t
\right)y_t
-2y
=0.
$$

Essa é a equação de Kummer com parâmetros $a=2$ e $b=1/2$. A solução que
decai no infinito é a função de Tricomi:

$$
y(t)
=
C\,U\left(2,\frac12,t\right).
$$

No bordo:

$$
U\left(2,\frac12,0\right)
=
\frac{\Gamma(1/2)}{\Gamma(5/2)}
=
\frac43.
$$

Além disso, a expansão para $t\to0^+$ contém:

$$
U\left(2,\frac12,t\right)
=
\frac43
-2\sqrt\pi\,t^{1/2}
+O(t).
$$

Como $t^{1/2}=x/2$ para $x\geq0$:

$$
U\left(2,\frac12,\frac{x^2}{4}\right)
=
\frac43
-\sqrt\pi\,x
+O(x^2).
$$

A normalização $\eta(0)=1$ fixa $C=3/4$. Portanto:

$$
z_H=-\eta'(0)
=
\frac{3\sqrt\pi}{4}
=
1.329340388179\ldots.
$$

O solver de problema de bordo fornece
$1.329340388179\ldots$ e funciona como verificação numérica independente
dessa derivação, não como fundamento da igualdade fechada.

Além disso, na família cilíndrica normalizada:

$$
\mathcal W''(2\sqrt\tau)
=
\frac{3}{2\tau}>0.
$$

Portanto o modo homogêneo de raio do cilindro de Hopf é estável no setor
reduzido. A estabilidade tensorial/radial completa de uma geometria real de
aparelho pertence ao fechamento metrológico, não ao fechamento conceitual dos
dois canais.

## 9. Coeficientes dimensionais de passagem não adiabática

No setor reduzido de dois níveis:

$$
H_2
=
\frac{\hbar}{2}
\left(\omega_\parallel\sigma_z+\omega_\perp\sigma_x\right),
$$

com:

$$
H_Z
=
-\frac{g_{\rm geom}\mu_B}{2}
\boldsymbol\sigma\cdot\mathbf B.
$$

Os parâmetros de Landau--Zener são:

$$
\Delta
=
\frac{|g_{\rm geom}|\mu_B}{\hbar}
|B_\perp|,
$$

$$
v
=
\frac{|g_{\rm geom}|\mu_B}{\hbar}
\left|
\partial_tB_\parallel
+\mathbf u\cdot\nabla B_\parallel
\right|.
$$

A probabilidade assintótica de transição é:

$$
P_{\rm LZ}
=
\exp\left(
-\frac{\pi\Delta^2}{2v}
\right).
$$

Essas quantidades são calculáveis quando o perfil do aparelho é fornecido. O
campo é dado experimental de contorno; não é parâmetro interno da ação.

## 10. Contrato para uma previsão metrológica completa

Para calcular $\kappa_H^{\rm SG}$ e $\Gamma_{\rm SG}$ de um aparelho real sem
pós-ajuste, o background numérico deve fornecer:

$$
\{\lambda_\nu,\ Z_\nu,\ j_{\nu1},\ j_{\nu2},\ \gamma_\nu,\ C_\nu\}.
$$

Então:

$$
\Gamma_{\rm SG}
=
\frac{\mu^2}{\hbar^2}
\sum_\nu
\frac{C_\nu}{\gamma_\nu}.
$$

Aqui $\gamma_\nu$ é taxa causal de relaxação, não autovalor estático. A ponte
entre ambos exige a mobilidade causal do aparelho.

## 11. Estatuto

O Stern--Gerlach está fechado como reconstrução geométrica-operacional:

- o objeto carrega spin/circulação antes do aparelho;
- o aparelho seleciona o eixo;
- Hopf fornece dois projetores;
- Born operacional fornece os pesos;
- a força clássica separa os centros de massa;
- o setor não adiabático tem critério explícito;
- a resposta de interface é Schur/DtN da Hessiana oficial.

O que permanece como metrologia aplicada é o cálculo de um detector real
específico, com material, perdas, temperatura, mobilidade e perfil
$\mathbf B(x,t)$.

## 12. Certificação Lean

O módulo canônico
[SternGerlachInterface.lean](../../../formal/GDQ/SternGerlachInterface.lean)
certifica:

1. que $r_c^2=6\tau$ anula a condição livre ponderada de bordo;
2. que a eliminação do interior produz exatamente a impedância Schur/DtN;
3. que cada resposta modal satisfaz $\lambda_\nu\delta\Phi_\nu=j_\nu$;
4. que autovalores e pesos de gradiente positivos produzem
   $\kappa_H^{\rm SG}\geq0$, estritamente positivo quando algum modo acopla;
5. a separação exata entre a componente Noether--Zeeman protegida e o vestido
   transversal;
6. a fórmula clássica de deflexão e a oposição entre os dois canais.

O módulo também certifica a positividade da forma fechada
$3\sqrt\pi/4$. A derivação da forma fechada a partir da EDO permanece na
prova analítica acima; não foi reduzida a uma definição numérica.
