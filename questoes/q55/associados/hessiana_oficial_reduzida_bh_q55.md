# Q55 — Hessiana oficial reduzida: primeiro bloco calculável

## Classificação

Teorema operacional reduzido / cálculo de bloco físico parcial.

Este documento define o primeiro bloco da Hessiana que pode ser calculado sem
inventar nova ação: o setor radial da amplitude

$$
u(r)=\sqrt{\rho(r)}.
$$

Ele não é a Hessiana completa de buraco negro, mas é parte da cadeia:

$$
\operatorname{Hess}\mathcal S_{\rm GDQ}
\longrightarrow
K_{\rm BH}^{\rm phys}.
$$

## 1. Origem na ação oficial

Na ação GDQ, a dependência em

$$
f_R=-\ln\rho
$$

e na medida

$$
\mathcal U=\frac{\rho}{(4\pi z_\tau)^n}
$$

gera, na redução Madelung/radial, a rigidez de amplitude de Bohm. O setor
torsional de Bismut fornece uma contribuição repulsiva efetiva na densidade.
Na menor redução radial admissível, o funcional de energia é:

$$
E[u,\phi]
=
\frac12\int|\nabla u|^2dV
+
\frac{\lambda_T}{2}\int u^4dV
+
\frac12\int\phi u^2dV,
$$

com:

$$
\Delta\phi=u^2.
$$

Aqui $\lambda_T$ representa a projeção radial efetiva do bloco torsional da
Hessiana oficial. Até ser calculado diretamente do setor de Bismut completo,
ele permanece parâmetro de redução.

## 2. Equação estacionária

Com normalização fixa:

$$
\int u^2dV=N,
$$

a equação de Euler--Lagrange é:

$$
-\frac12\Delta u
+
\left(
\phi+\lambda_Tu^2
\right)u
=
\mu u.
$$

Na simetria radial:

$$
u''+\frac2r u'
=
2(\phi+\lambda_Tu^2-\mu)u.
$$

Esta é a equação resolvida em:

`solve_sela_densidade_bohm_q55.py`.

## 3. Segunda variação antes de eliminar $\phi$

Variando:

$$
u\mapsto u+\delta u,
\qquad
\phi\mapsto\phi+\delta\phi,
$$

temos:

$$
\Delta\delta\phi
=
2u\,\delta u.
$$

A equação linearizada da amplitude é:

$$
\left[
-\frac12\Delta
+
\phi-\mu
+
3\lambda_Tu^2
\right]\delta u
+
u\,\delta\phi
=
0.
$$

Eliminando $\delta\phi$ por Schur:

$$
\delta\phi
=
\Delta^{-1}(2u\,\delta u),
$$

obtemos o bloco não-local:

$$
K_{uu}^{\rm Schur}
=
-\frac12\Delta
+
\phi-\mu
+
3\lambda_Tu^2
+
u\,\Delta^{-1}(2u\,\cdot).
$$

Como $\Delta^{-1}$ com condição de Dirichlet é negativo no domínio radial, o
último termo representa a retroação atrativa gravitacional.

## 4. Projeção física

O modo de normalização deve ser removido:

$$
\delta N
=
2\int u\,\delta u\,dV
=0.
$$

No variável regular:

$$
y(r)=r\,\delta u(r),
$$

o modo removido é proporcional a:

$$
y_N(r)=r\,u(r).
$$

O bloco físico radial é:

$$
K_{uu,0}^{\rm phys}
=
P_NK_{uu}^{\rm Schur}P_N,
$$

onde:

$$
P_N
=
1
-
\frac{|y_N\rangle\langle y_N|}
{\langle y_N,y_N\rangle}.
$$

## 5. Critério

Se:

$$
\lambda_{\min}
\left(
K_{uu,0}^{\rm phys}
\right)
>0,
$$

então o background é estável no setor radial de amplitude com retroação
gravitacional não-local incluída.

Se aparecer:

$$
\lambda_{\min}<0,
$$

o core regular possui instabilidade radial física nessa redução.

## 6. Limitação

Este bloco ainda não contém:

1. flutuações métricas tensoriais completas;
2. flutuações torsionais independentes;
3. flutuações de fase/circulação;
4. modos de horizonte;
5. condições globais de Kruskal/Page curve.

Portanto ele é um bloco de \(K_{\rm BH}^{phys}\), não \(K_{\rm BH}^{phys}\)
inteiro.
