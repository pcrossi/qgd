---
title: "Identidade entre velocidade osmótica e potencial quântico"
tipo: derivacao
status: identidade-exata-sob-hipoteses
---

# Identidade entre velocidade osmótica e potencial quântico

## 1. Identidade diferencial

Para $\rho>0$, escreva $R=\sqrt\rho$. Como

$$
\ln R=\frac12\ln\rho,
$$

temos

$$
\frac{\Delta R}{R}
=\Delta\ln R+|\nabla\ln R|^2
=\frac12\Delta\ln\rho
+\frac14|\nabla\ln\rho|^2.
$$

Se

$$
u=\nu\nabla\ln\rho,
$$

então

$$
\nabla\cdot u=\nu\Delta\ln\rho
$$

e

$$
|u|^2=\nu^2|\nabla\ln\rho|^2.
$$

Consequentemente,

$$
m\nu\nabla\cdot u+\frac{m}{2}|u|^2
=2m\nu^2\frac{\Delta\sqrt\rho}{\sqrt\rho}.
$$

Para

$$
\nu=\frac{\hbar}{2m},
$$

segue

$$
\boxed{
m\nu\nabla\cdot u+\frac{m}{2}|u|^2
=\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
}
$$

Assim, o potencial quântico pode ser escrito como

$$
\boxed{
Q[\rho]
=-\left(
m\nu\nabla\cdot u+\frac{m}{2}|u|^2
\right).
}
$$

## 2. Sinal e interpretação

$Q$ não é universalmente positivo nem universalmente repulsivo. Seu sinal
depende da curvatura local de $\sqrt\rho$. O que é universal é sua forma
diferencial. A força associada é $-\nabla Q$ e também pode mudar de direção.

Em determinados perfis localizados ou perto de zeros da densidade, esse termo
pode atuar como barreira. Essa propriedade deve ser demonstrada para o perfil
em questão; não pode ser inferida apenas do nome “pressão quântica”.

## 3. Generalização geométrica

Numa variedade Riemanniana, substitui-se $\nabla$ pela derivada covariante e
$\Delta$ pelo laplaciano de Laplace--Beltrami. Com medida ponderada ou torção,
podem surgir termos adicionais. Portanto a identidade plana é o limite que a
redução GDQ precisa reproduzir, não a expressão completa em todo background.
