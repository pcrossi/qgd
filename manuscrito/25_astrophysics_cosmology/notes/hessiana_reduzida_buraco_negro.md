---
title: "Nota — Hessiana reduzida do buraco negro regular"
---

# Nota — Hessiana reduzida do buraco negro regular

Esta nota registra os blocos espectrais reduzidos usados para testar a
estabilidade do buraco negro GDQ como sóliton com horizonte. O operador
covariante final é:

$$
K_{\rm BH}^{\rm phys}
=
P_{\rm BH}^{\rm phys}
\operatorname{Hess}_{\Phi_{\rm BH,*}}\mathcal S_{\rm GDQ}
P_{\rm BH}^{\rm phys}.
$$

A redução abaixo não é a matriz 8D completa; ela é a avaliação dos blocos que
podem ser computados a partir da sela radial e do exterior estático.

## 1. Origem torsional de $\lambda_T$

Na conexão de Bismut:

$$
\mathcal R^B
=
\mathcal R^{LC}
-
\frac1{12}|H|^2.
$$

No core isotrópico:

$$
H_{abc}
=
q_T\rho\,\varepsilon_{abc}.
$$

Então:

$$
|H|^2
=
6q_T^2\rho^2.
$$

O termo torsional reduzido é:

$$
E_H
=
\frac1{12}\int |H|^2\,dV
=
\frac{q_T^2}{2}\int\rho^2\,dV
=
\frac{q_T^2}{2}\int u^4\,dV.
$$

Comparando com:

$$
U_T
=
\frac{\lambda_T}{2}\int u^4\,dV,
$$

segue:

$$
\lambda_T=q_T^2.
$$

Na normalização isotrópica mínima dos três canais ortogonais de circulação
Cartan--Bismut:

$$
q_T^2=1+1+1=3.
$$

Portanto:

$$
\lambda_T=3.
$$

## 2. Virial

Para:

$$
E[u]=K+U_T+W,
$$

com:

$$
K=\frac12\int|\nabla u|^2\,dV,
\qquad
U_T=\frac{\lambda_T}{2}\int u^4\,dV,
\qquad
W=\frac12\int\phi u^2\,dV,
$$

a reescala preservando massa:

$$
u_a(r)=a^{3/2}u(ar)
$$

implica, sem bordo:

$$
2K+3U_T+W=0.
$$

Para $\lambda_T=3$, a avaliação reduziu a:

$$
K=3.1675522712965487\times10^{-1},
$$

$$
U_T=9.808336775055311\times10^{-2},
$$

$$
W=-9.274781821673822\times10^{-1},
$$

com:

$$
2K+3U_T+W
=
2.8237534358688254\times10^{-4}.
$$

O resíduo relativo foi:

$$
1.5220431610642136\times10^{-4}.
$$

Na direção coletiva:

$$
\frac{d^2E}{da^2}\bigg|_{a=1}
=
1.193971365853>0.
$$

## 3. Bloco radial de amplitude com Schur

A segunda variação antes de eliminar $\phi$ é:

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

A perturbação do potencial satisfaz:

$$
\Delta\delta\phi
=
2u\,\delta u.
$$

Eliminando $\delta\phi$ por complemento de Schur:

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

O modo de normalização:

$$
y_N(r)=ru(r)
$$

é removido por:

$$
P_N
=
1
-
\frac{|y_N\rangle\langle y_N|}
{\langle y_N,y_N\rangle}.
$$

O bloco físico radial é:

$$
K_{uu,0}^{\rm phys}
=
P_NK_{uu}^{\rm Schur}P_N.
$$

Antes da projeção:

$$
\lambda_{\rm raw,1}
=
-1.927437459951\times10^{-1}.
$$

Depois da projeção:

$$
\lambda_{\rm phys,1}
=
-5.982003087324\times10^{-13}
\simeq0,
$$

e:

$$
\lambda_{\rm phys,2}
=
3.651456961676\times10^{-2}>0.
$$

A convergência de malha foi:

| $N$ | $\lambda_{\rm phys,2}$ |
|---:|---:|
| $300$ | $3.650859450588\times10^{-2}$ |
| $450$ | $3.651280931120\times10^{-2}$ |
| $650$ | $3.651456961676\times10^{-2}$ |
| $850$ | $3.651524343579\times10^{-2}$ |

## 4. Harmônicos escalares de amplitude

Para:

$$
\delta u(r,\Omega)
=
\frac{y_\ell(r)}{r}Y_{\ell m}(\Omega),
$$

o operador local recebe:

$$
\frac{\ell(\ell+1)}{2r^2}.
$$

O Green de Schur radial usa:

$$
\left(
\frac{d^2}{dr^2}
-
\frac{\ell(\ell+1)}{r^2}
\right)
\delta\psi_\ell
=
2uy_\ell.
$$

Para $0\le\ell\le8$, não houve autovalor físico negativo. O menor modo foi:

$$
\lambda_{\ell=1}
=
1.909625790263\times10^{-3}>0.
$$

## 5. Setor de fase/circulação

A forma quadrática é:

$$
Q_\theta[\delta\theta]
=
\frac12\int\rho|\nabla\delta\theta|^2\,dV.
$$

Logo:

$$
K_\theta
=
-\nabla\cdot(\rho\nabla).
$$

O zero em $\ell=0$ é:

$$
8.536256780627\times10^{-13}
\simeq0,
$$

e representa a fase global protegida por Noether. O menor modo físico
não-zero foi:

$$
\lambda_{\ell=1}
=
6.572554660398\times10^{-2}>0.
$$

## 6. Setor torsional e métrico axial

Sem piso infravermelho artificial, o bloco torsional reduzido é:

$$
K_{HH,\ell}^{red}
=
-\frac{d^2}{dr^2}
+
\frac{\ell(\ell+1)}{r^2}
+
2\lambda_T\rho(r).
$$

O menor gap encontrado foi:

$$
\lambda_{\min}(K_{HH}^{red})
=
1.475541776890\times10^{-1}>0.
$$

No patch exterior estático, o setor métrico axial reduzido é:

$$
K_{gg,\ell}^{red}
=
-\frac{d^2}{dr^2}
+
V_{gg,\ell}(r),
$$

com:

$$
V_{gg,\ell}
=
A
\left[
\frac{\ell(\ell+1)}{r^2}
-
\frac{6m(r)}{r^3}
+
4\pi(\epsilon-p_r)
\right].
$$

O menor gap encontrado foi:

$$
\lambda_{\min}(K_{gg}^{red})
=
1.493545907614\times10^{-1}>0.
$$

## 7. Acoplamentos cruzados por Schur

O acoplamento métrico--dilatônico vem da variação da medida ponderada:

$$
\mathcal U=e^{-f_R}(4\pi z_\tau)^{-n}.
$$

No patch exterior reduzido:

$$
J_{gf}^{red}
\sim
\sqrt A\,|\partial_r f_R|\sqrt\rho.
$$

O acoplamento métrico--torsional vem da variação de:

$$
\sqrt g\,|H|^2.
$$

No setor reduzido:

$$
J_{gH}^{red}
\sim
\sqrt{\lambda_T}\rho.
$$

As normas foram:

$$
\|K_{gf}^{red}\|
=
6.166879064740\times10^{-4},
$$

$$
\|K_{gH}^{red}\|
=
8.076881453156\times10^{-6}.
$$

As razões de Schur foram:

$$
\chi_{gf}
=
1.333410946325\times10^{-3},
$$

$$
\chi_{gH}
=
2.960174621482\times10^{-9}.
$$

Como ambas são muito menores que $1$, os acoplamentos cruzados reduzidos não
fecham o gap dos blocos diagonais testados.

## 8. Horizonte e Page toy

A gravidade de superfície reduzida é:

$$
\kappa_H
=
\frac12e^{\Phi(r_H)}|A'(r_H)|.
$$

A temperatura é:

$$
T_H
=
\frac{\kappa_H}{2\pi}.
$$

Para os dois horizontes:

$$
T_1=2.332099662324\times10^{-2},
\qquad
T_2=4.844788989724\times10^{-3}.
$$

A curva de Page preservada nesta camada é apenas toy unitária:

$$
S_{\rm toy}(0)=0,
\qquad
\max S_{\rm toy}=2.696953704284\times10^{-5},
\qquad
S_{\rm toy}(1)=0.
$$

A Page curve física exige canais espectrais reais de
$K_{\rm BH}^{\rm phys}$ em coordenadas regulares atravessando horizontes.

