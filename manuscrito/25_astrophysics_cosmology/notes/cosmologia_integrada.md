---
title: "Nota — Solver cosmológico integrado"
---

# Nota — Solver cosmológico integrado

Esta nota define o contrato do solver cosmológico integrado. Ela não introduz
uma nova ação e não substitui a ação oficial por Einstein--Hilbert. O objetivo
é projetar a ação oficial para um background cosmológico comum e exigir que
todos os observáveis sejam calculados com os mesmos dados.

## 1. Sela cosmológica

$$
\Phi_*^{\rm cos}
=
(g,J,H,f,\mathcal U)_{\rm cos}.
$$

A coleção de entrada é:

$$
\mathcal P_{\rm cos}
=
\left(
\Phi_*^{\rm cos},
R_H,
\eta_b,
T_0,
\mathcal P_{\rm prim},
\mathcal B_{\rm contorno}
\right).
$$

Depois de congelada, essa coleção não pode ser reajustada para explicar cada
observável separadamente.

## 2. Hessiana física comum

$$
K_{\rm cos}^{\rm phys}
=
P_{\rm cos}^{\rm phys}
\operatorname{Hess}\mathcal S_{\rm GDQ}
P_{\rm cos}^{\rm phys}.
$$

O projetor físico remove difeomorfismos puros, modos de normalização da
medida, modos de bordo que apenas redefinem o contorno e calibre interno não
observável.

As perturbações comuns satisfazem:

$$
K_{\rm cos}^{\rm phys}\delta\Phi_{\rm cos}
=
J_{\rm bar}
+
J_\gamma
+
J_\nu
+
J_H.
$$

## 3. Fundo homogêneo

O fundo vem da equação métrica ponderada:

$$
\operatorname{Eul}_g(\mathcal S_{\rm GDQ})=0
\quad
\Longrightarrow
\quad
\mathcal E_{\rm cos}[a,H,\rho_i,\Theta_H]=0.
$$

Ele define:

$$
H(z)=\frac{\dot a}{a}.
$$

E as distâncias:

$$
D_C(z)=c\int_0^z\frac{dz'}{H(z')},
$$

$$
D_L(z)=(1+z)D_C(z),
\qquad
D_A(z)=\frac{D_C(z)}{1+z}.
$$

## 4. Observáveis produzidos pelo mesmo par

O mesmo background deve alimentar:

1. expansão homogênea;
2. perturbações escalares, vetoriais e tensoriais;
3. lentes;
4. crescimento;
5. BBN;
6. CMB;
7. holonomias de Bismut.

Para BBN:

$$
T(z)=T_0(1+z),
\qquad
H(z)=H_{\rm GDQ}(z),
$$

$$
\Gamma_{ij}^{\rm GDQ}(T)
=
\Gamma_{ij}^{\rm nuc}(T)
+
\Delta\Gamma_{ij}^{\rm Bohm-Cartan}(T,\Phi_*^{\rm cos}).
$$

Para lentes:

$$
\hat\alpha
=
\int_{\gamma_{\rm luz}}
\nabla_\perp(\Phi+\Psi)
\frac{2\,dl}{c^2}.
$$

Para o setor geométrico residual:

$$
\Theta_{\mu\nu}^{(H)}
\sim
H_{\mu\alpha\beta}H_{\nu}^{\ \alpha\beta}
-
\frac12g_{\mu\nu}|H|^2.
$$

Para birrefringência:

$$
\Delta\Psi_{\rm GDQ}
=
\frac12
\int_{\gamma_{\rm CMB}}
\omega_{\rm pol}^{B}.
$$

## 5. Critério de fechamento

O critério de fechamento é não calibrar cada observável separadamente. O
background e os parâmetros de contorno devem ser congelados antes da
comparação conjunta.

O solver só é metrologicamente fechado se um único $\mathcal P_{\rm cos}$
gerar simultaneamente $H(z)$, supernovas, BAO, CMB, BBN/lítio, lentes,
crescimento e birrefringência.
