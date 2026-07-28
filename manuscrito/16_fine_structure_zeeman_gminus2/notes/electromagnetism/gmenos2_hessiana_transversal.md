---
title: "Hessiana transversal de g-2"
---

# Hessiana transversal de $g-2$

O funcional vinculado é:

$$
\mathscr I[\Phi,\lambda;B]
=
\mathcal S_{\rm GDQ}[\Phi]
-B\,M[\Phi]
-\lambda
\left(
\mathcal C[\Phi]-C_\ell
\right).
$$

Linearizando:

$$
\mathcal C[\Phi_\ell+\eta]
=
C_\ell+\langle c_\ell,\eta\rangle+O(\eta^2),
$$

$$
M[\Phi_\ell+\eta]
=
M[\Phi_\ell]+\langle m_\ell,\eta\rangle+O(\eta^2).
$$

A Hessiana física vinculada correta é:

$$
K_{\ell,\rm phys}
=
P_{\rm phys}^\dagger
\left.
\delta^2
\left(
\mathcal S_{\rm GDQ}
-\lambda_\ell\mathcal C
\right)
\right|_{\Phi_\ell}
P_{\rm phys}.
$$

O projetor remove gauge e incompatibilidades de domínio, mas não elimina
$c_\ell$. A conservação da circulação é imposta por $\lambda$. Da equação
linear:

$$
K_{\ell,\rm phys}\eta
=
B\,m_\ell+\delta\lambda\,c_\ell
$$

e do vínculo $\langle c_\ell,\eta\rangle=0$, segue:

$$
-\frac{\partial\lambda}{\partial B}
=
\frac{
\langle c_\ell,K_{\ell,\rm phys}^{+}m_\ell\rangle
}{
\langle c_\ell,K_{\ell,\rm phys}^{+}c_\ell\rangle
}.
$$

Decompõe-se:

$$
m_\ell
=
\gamma_{0,\ell}c_\ell+m_{\perp,\ell}.
$$

Então:

$$
a_\ell
=
\frac{1}{\gamma_{0,\ell}}
\frac{
\langle c_\ell,K_{\ell,\rm phys}^{+}m_{\perp,\ell}\rangle
}{
\langle c_\ell,K_{\ell,\rm phys}^{+}c_\ell\rangle
}.
$$

Essa equação é o ponto operacional do capítulo. Ela mostra exatamente o que
falta para metrologia: calcular $H_{C,\ell}$ e $m_{\perp,\ell}$ no background
real, sem escolher coeficientes pelo alvo experimental.
