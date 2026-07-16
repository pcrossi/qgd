# Q38 — Retroação de carga relativa e limite do determinante espectral

## 1. Objetivo

Este documento testa se os dados atuais da GDQ bastam para:

1. realizar geometricamente \(Q_{\rm rel}=1/2\) como conexão de Bismut;
2. calcular o determinante espectral sem usar o resíduo observado;
3. declarar a Questão 38 encerrada.

## 2. Problema inverso de Bismut

No colar local \(U\simeq B^4_+\) do estômato, o perfil autodual desejado é

\[
\mathcal A_\mu^{\rm inst}
=\frac{2\eta^a_{\mu\nu}x^\nu}{x^2+\rho_0^2}T_a.
\]

Para que ele seja uma conexão de Bismut genuína, e não uma conexão de gauge
auxiliar, devem existir simultaneamente um coframe \(e^a\), uma métrica \(g\),
uma estrutura complexa \(J\) e uma 3-forma \(H\) tais que

\[
de^a+(\mathcal A^{\rm inst})^a{}_b\wedge e^b
=\frac12H^a{}_{bc}e^b\wedge e^c,
\]

\[
\nabla^{\mathcal A^{\rm inst}}g=0,
\qquad
\nabla^{\mathcal A^{\rm inst}}J=0,
\qquad
H=d^c_J\omega_g,
\]

com

\[
(g,J,H)|_{\partial U}=(g_*,J_*,H_*)|_{\partial U}.
\]

Esse é o sistema inverso de Cartan--Bismut. O ansatz BPST resolve
\(F=*F\), mas essa única equação não implica as quatro condições acima.

## 3. Construção geométrica condicional

Uma realização local possível começa por uma calota conformemente redonda de
quatro dimensões, cuja conexão espinorial autodual representa o instantão. A
calota é cortada no equador, de modo que a densidade de Pontryagin, par sob a
reflexão normal, forneça

\[
Q_{\rm rel}=\frac12.
\]

No núcleo autodual, a fonte métrica de Yang--Mills satisfaz

\[
T_{\mu\nu}^{\rm SD}
=\operatorname{tr}\left(
F_{\mu\alpha}F_\nu{}^\alpha
-\frac14g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}
\right)=0.
\]

Portanto, a parte autodual pura não exige retroação métrica local. A
retroação aparece no colar de interpolação entre o núcleo e o background
torsional de Hopf. Escrevendo

\[
g=g_*+h,qquad f=f_0+\varphi,qquad H=H_*+D_Hh,
\]

ela deve resolver

\[
\boxed{
\mathbb L_B
\begin{pmatrix}h\\ \varphi\end{pmatrix}
=-\begin{pmatrix}E_g[\mathcal A^{\rm inst}]\\E_f[\mathcal A^{\rm inst}]
\end{pmatrix},
\qquad
(h,\varphi)|_{\partial U}=0,
}
\]

onde \(\mathbb L_B\) é a Hessiana gauge-fixada de Einstein--Bismut já
estruturada nos adendos anteriores. Formalmente,

\[
\begin{pmatrix}h\\ \varphi\end{pmatrix}
=-\mathbb L_B^{-1}
\begin{pmatrix}E_g\\E_f\end{pmatrix}
+O(E^2).
\]

Isso é uma construção variacional válida, mas ainda não é uma solução
explícita: os documentos não fornecem \(E_g,E_f\) no colar nem a inversa de
\(\mathbb L_B\) com o contorno escolhido.

## 4. Carga relativa e termo de borda

A quantidade gauge-invariante em uma variedade com bordo é a combinação

\[
Q_{\rm rel}
=\frac1{8\pi^2}\int_U\operatorname{tr}(F\wedge F)
-\frac1{8\pi^2}\int_{\partial U}
\operatorname{CS}(\mathcal A,\mathcal A_*).
\]

Com a reflexão da calota e o mesmo mapa de transição nos dois lados,

\[
\boxed{Q_{\rm rel}=\frac12.}
\]

Assim, a carga pode ser fixada topologicamente. O que permanece aberto não é
a integral de carga, mas a solução do sistema inverso de Bismut no colar.

## 5. Operador do determinante

Se a retroação estivesse conhecida, o prefator seria

\[
\mathcal P_{\rm GDQ}
=\exp\left\{-\frac12
\left[
\log\det{}'\mathbb L_{B,\rm inst}
-\log\det\mathbb L_{B,0}
\right]
+\log J_{\rm orb}\right\}.
\]

Em termos do Schur,

\[
\mathbb L_{B}=K_H-JK_T^{-1}J^\dagger.
\]

A definição espectral não ambígua é

\[
\log\frac{\det{}'\mathbb L_{B,\rm inst}}
{\det\mathbb L_{B,0}}
=-\int_0^\infty\frac{dt}{t}
\left[
\operatorname{Tr}'e^{-t\mathbb L_{B,\rm inst}}
-\operatorname{Tr}e^{-t\mathbb L_{B,0}}
\right],
\]

com os mesmos contornos, subtrações locais e escala espectral.

## 6. Por que o número ainda não foi calculado

Há quatro quantidades que ainda não foram **extraídas da ação oficial**:

1. a solução \((h,\varphi)\) no colar;
2. a extensão auto-adjunta física: Robin, APS ou outra condição derivada;
3. o tratamento dos modos zero de posição, orientação e tamanho \(\rho_0\);
4. a medida do módulo \(\rho_0\), ou um mecanismo GDQ que fixe seu valor.

O quarto ponto é decisivo. O setor topológico clássico isolado não depende de
\(\rho_0\), mas a ação oficial completa contém a curvatura, a medida de
Perelman, o dilaton, a torção constitutiva e a cola. Esses termos devem levantar
ou integrar corretamente o módulo de tamanho. Portanto, \(\rho_0/R\), o
contorno e o jacobiano não são novos parâmetros: são saídas ainda não
calculadas da redução da ação oficial no setor \(Q_{\rm rel}=1/2\).

O valor

\[
\mathcal P_{\rm req}=1.00267505
\]

não pode ser usado para escolher \(\rho_0\), o contorno ou a subtração. Isso
seria exatamente o pós-ajuste que a auditoria pretende evitar.

## 7. Resultado lógico

Foi possível construir:

1. o background assintótico steady de Einstein--Bismut;
2. a classe local autodual com \(Q_{\rm rel}=1/2\);
3. a equação linear e não linear que determina a retroação;
4. a definição do determinante relativo e de seus modos zero.

Não foi possível ainda obter legitimamente um valor numérico único para o
determinante, porque a ação oficial não foi reduzida e variada explicitamente
com respeito ao módulo \(\rho_0\), aos dados de cola e aos modos coletivos.
Isso é uma pendência de cálculo, não ausência da ação fundamental. Portanto:

\[
\boxed{
\text{Q38 está fechada estruturalmente, mas não numericamente/preditivamente.}
}
\]

Uma declaração de fechamento total neste estágio seria incorreta.

## 8. Dados mínimos para o fechamento definitivo

É necessário calcular, da ação oficial e não de CODATA:

\[
\boxed{
\rho_0/R,
\qquad
Z_{\partial}^{\rm GDQ},
\qquad
J_{\rm orb}.
}
\]

Essas três quantidades devem emergir de:

\[
\frac{dS_{\rm red}^{(Q=1/2)}}{d\rho_0}=0,
\qquad
\delta S_{\rm red}^{(Q=1/2)}\big|_{\partial U}=0,
\qquad
G_{AB}^{\rm mod}
=\left\langle\frac{\partial\Phi}{\partial m^A},
\frac{\partial\Phi}{\partial m^B}\right\rangle_{\mathcal U_*},
\]

com

\[
J_{\rm orb}=\sqrt{\det G_{AB}^{\rm mod}}.
\]

A redução radial foi executada em
`q38/reducao_radial_acao_oficial_q38.md`. Ela mostra que

\[
\frac{dS_{\rm red}}{d\rho}=0
\]

identicamente: \(\rho\) é um módulo coletivo exato do setor autodual. Logo,
ele não deve ser fixado por um mínimo clássico, mas integrado com a métrica
de módulos e o determinante primado.

Com essas saídas, a retroação vira um problema elíptico fechado e o
determinante pode ser avaliado por decomposição em harmônicos de
\(S^3\times T^5\), heat kernel relativo ou método de Gel'fand--Yaglom por
ondas parciais.

## 9. Referências matemáticas usadas na auditoria

- K.-H. Lee, *Stability and moduli space of generalized Ricci solitons*,
  arXiv:2303.00149. O trabalho fornece uma segunda variação gauge-fixada do
  funcional de Einstein--Hilbert generalizado e demonstra estabilidade de
  backgrounds Bismut-flat.
- J. Streets e Y. Ustinovskiy, *Classification of generalized Kähler--Ricci
  solitons on complex surfaces*, arXiv:1907.03819. O trabalho constrói solitons
  steady compactos em superfícies de Hopf e trata sua unicidade em classes de
  simetria.
