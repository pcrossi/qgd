---
title: "Primeira variação da ação GDQ: estrutura completa"
---

# Primeira variação da ação GDQ: estrutura completa

Esta nota reúne a álgebra universal usada nos Capítulos 4 e 5. Ela não
substitui as derivações pedagógicas do texto principal.

Defina

$$
C=\frac{\hbar}{\Lambda_C^2},
\qquad
\mathcal L_0
=\tau\left(
\mathcal R+g^{\mu\bar\nu}
\partial_\mu f\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}-n.
$$

Então

$$
S=\operatorname{Re}
\int_\gamma\int_M
C\mathcal U\mathcal L_0\,dV_g\frac{d\tau}{\tau}.
$$

## Regra do produto

$$
\delta S
=\operatorname{Re}\int_\gamma\int_M
C\mathcal U
\left[
\delta\mathcal L_0
+\mathcal L_0\frac{\delta\mathcal U}{\mathcal U}
+\mathcal L_0\frac{\delta dV_g}{dV_g}
\right]
dV_g\frac{d\tau}{\tau}.
$$

Para variações de $f$ e $\bar f$ com $z_\tau$ fixo,

$$
\frac{\delta\mathcal U}{\mathcal U}
=-\frac12(\delta f+\delta\bar f).
$$

Se $g^{AB}$ é a variável métrica,

$$
\frac{\delta dV_g}{dV_g}
=-\frac12g_{AB}\delta g^{AB}.
$$

Se, em vez disso, usamos $g_{AB}$, o sinal é positivo:

$$
\frac{\delta dV_g}{dV_g}
=\frac12g^{AB}\delta g_{AB}.
$$

As duas convenções não devem ser misturadas.

## Gradiente complexo

$$
\begin{aligned}
\delta\left(
g^{\mu\bar\nu}\partial_\mu f
\partial_{\bar\nu}\bar f
\right)
={}&\delta g^{\mu\bar\nu}
\partial_\mu f\partial_{\bar\nu}\bar f
\\
&+g^{\mu\bar\nu}
\partial_\mu\delta f\partial_{\bar\nu}\bar f
\\
&+g^{\mu\bar\nu}
\partial_\mu f\partial_{\bar\nu}\delta\bar f.
\end{aligned}
$$

As duas últimas parcelas são integradas por partes com o peso $\mathcal U$.
Elas produzem os operadores de Euler--Lagrange e o concomitante de bordo.

## Curvatura ponderada

Na convenção $\delta g^{AB}$,

$$
\begin{aligned}
\delta\int_M\mathcal U\mathcal R\,dV_g
={}&\int_M
\left[
\mathcal U\left(
\mathcal R_{AB}-\frac12\mathcal Rg_{AB}
\right)
\\
&+g_{AB}\Delta_g\mathcal U
-\nabla_A\nabla_B\mathcal U
\right]
\delta g^{AB}\,dV_g
+B_{\mathcal R}.
\end{aligned}
$$

## Normalização

O vínculo é

$$
N[\mathcal U,g]
=\int_M\mathcal U\,dV_g=1.
$$

Variamos

$$
S_{\rm restrita}
=S-C\int_\gamma\lambda(\tau)(N-1)\frac{d\tau}{\tau}.
$$

Para $q=\ln\rho$,

$$
\delta_qN
=\int_M\mathcal U\,\delta q\,dV_g.
$$

Para a métrica inversa,

$$
\delta_gN
=-\frac12\int_M
\mathcal U g_{AB}\delta g^{AB}\,dV_g.
$$

Assim, o mesmo $\lambda(\tau)$ aparece nas equações normalizadas de densidade
e métrica.

## Estrutura final

Depois das integrações por partes,

$$
\delta S_{\rm restrita}
=\int_\gamma\int_M
\left(
\mathcal E_g^{AB}\delta g_{AB}
+\mathcal E_f\delta f
+\mathcal E_{\bar f}\delta\bar f
\right)
+\int_\gamma\int_{\partial M}\Theta.
$$

Os coeficientes de bulk fornecem as equações. $\Theta$ fornece os momentos de
interface. As fórmulas explícitas em $(\rho,S_R)$ estão em
[[../../05_equations_conservation/index|Capítulo 5]].
