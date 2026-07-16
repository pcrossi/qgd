---
title: "Continuação espectral do grupo unitário ao semigrupo"
tipo: derivacao
status: teorema-sob-hipoteses
---

# Continuação espectral do grupo unitário ao semigrupo

## 1. Hipóteses

Seja $H$ auto-adjunto em um espaço de Hilbert e limitado inferiormente. Após
uma translação constante, podemos supor $H\geq0$. Pelo teorema espectral,

$$
H=\int_0^\infty\lambda\,dE_H(\lambda),
$$

onde $E_H$ é a medida espectral de projeções.

## 2. Evolução real

Para $t\in\mathbb R$,

$$
U(t)
=e^{-itH/\hbar}
=\int_0^\infty
e^{-it\lambda/\hbar}\,dE_H(\lambda).
$$

Como o integrando possui módulo um,

$$
U(t)^*U(t)=I
$$

e

$$
U(t+s)=U(t)U(s).
$$

Portanto $U(t)$ é um grupo unitário fortemente contínuo.

## 3. Continuação no semiplano inferior

Para

$$
z=t-i\tau,
\qquad
\tau>0,
$$

definimos

$$
U(z)
=\int_0^\infty
e^{-iz\lambda/\hbar}\,dE_H(\lambda).
$$

Como

$$
|e^{-iz\lambda/\hbar}|
=e^{-\tau\lambda/\hbar}\leq1,
$$

o operador é limitado e analítico no interior do semiplano. No eixo
imaginário negativo,

$$
U(-i\tau)=e^{-\tau H/\hbar}.
$$

Além disso,

$$
e^{-(\tau_1+\tau_2)H/\hbar}
=e^{-\tau_1H/\hbar}e^{-\tau_2H/\hbar},
$$

mas apenas $\tau\geq0$ é contrativo. Temos um semigrupo, não um grupo
unitário.

## 4. O que não segue automaticamente

O argumento funcional não garante sozinho:

1. uma representação por medida de Wiener;
2. positividade por reflexão;
3. continuação através de cortes ou singularidades;
4. correspondência dos domínios de contorno;
5. reconstrução causal única.

Esses itens requerem hipóteses adicionais sobre o operador, o potencial, os
campos e o domínio físico.
