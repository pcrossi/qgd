# Q39 — Cálculo direto da Hessiana 8D no background produto

## 1. Objetivo

Este documento calcula explicitamente \(H_\perp\), \(J\), o complemento de
Schur e o índice crítico no caso produto/bloco exato:

\[
M_8=B_3\times K_5,
\qquad
g_8=g_B\oplus g_K,
\qquad
K_5=T^5.
\]

Esse é o caso em que a redução Perelman--GDQ deve ser verdadeira.

---

## 2. Hipóteses do cálculo

Assumimos:

\[
\operatorname{Ric}(g_K)=0,
\qquad
\nabla_K f_*=0,
\qquad
H_{BK}=0
\]

ou, equivalentemente, que os componentes mistos de torção foram projetados
fora do setor físico leptônico.

A medida estacionária fatoriza:

\[
\mathcal U_8\,dV_8
=
\mathcal U_B\,dV_B
\otimes
\frac{dV_K}{\operatorname{Vol}(K_5)}.
\]

As flutuações são escritas como:

\[
\delta\Phi
=
x(b)+y(b,k),
\qquad
x\in\mathcal H_B,
\qquad
y\in\mathcal H_\perp.
\]

O complemento toroidal \(\mathcal H_\perp\) é tomado ortogonal ao kernel
constante de \(T^5\), isto é, removemos:

1. translações toroidais;
2. holonomias planas;
3. moduli constantes de forma/volume que não carregam massa leptônica;
4. modos de gauge.

---

## 3. Espectro toroidal

Escolha coordenadas angulares:

\[
\theta_a\in[0,2\pi),
\qquad
a=1,\ldots,5,
\]

com métrica:

\[
ds_K^2
=
\sum_{a=1}^5 R_a^2\,d\theta_a^2.
\]

Os modos de Fourier são:

\[
e_n(\theta)
=
\exp(i n\cdot\theta),
\qquad
n\in\mathbb Z^5.
\]

O laplaciano positivo no toro satisfaz:

\[
-\Delta_K e_n
=
\lambda_K(n)e_n,
\]

com:

\[
\lambda_K(n)
=
\sum_{a=1}^5\frac{n_a^2}{R_a^2}.
\]

O modo \(n=0\) é o kernel constante. No complemento físico:

\[
n\ne0.
\]

Logo:

\[
\lambda_K(n)\ge
\min_a\frac{1}{R_a^2}
=
\frac{1}{R_{\max}^2}.
\]

Assim, o gap toroidal é:

\[
\boxed{
m_K^2
=
\frac{1}{R_{\max}^2}.
}
\]

Se todos os raios são normalizados para \(R_a=1\):

\[
\boxed{
m_K^2=1.
}
\]

---

## 4. Cálculo de \(H_\perp\)

No setor produto, os termos quadráticos da ação oficial que contêm derivadas
toroidais reduzem à forma:

\[
\mathfrak Q_\perp[y]
=
C_\gamma
\int_{B_3}
\mathcal U_B\,dV_B
\int_{K_5}
\left(
\tau |\nabla_K y|^2
+V_\perp |y|^2
\right)
\frac{dV_K}{\operatorname{Vol}(K_5)}.
\]

Aqui \(C_\gamma>0\) é o peso real do contorno causal no setor físico e
\(V_\perp\ge0\) representa os termos algébricos não negativos após projeção de
gauge/moduli.

Expandindo:

\[
y(b,\theta)
=
\sum_{n\ne0}y_n(b)e_n(\theta),
\]

obtemos:

\[
\mathfrak Q_\perp[y]
=
C_\gamma
\sum_{n\ne0}
\int_{B_3}
\mathcal U_B
\left(
\tau\lambda_K(n)+V_\perp
\right)
|y_n(b)|^2
dV_B.
\]

Portanto:

\[
H_\perp
\ge
C_\gamma\tau m_K^2 I.
\]

Como \(C_\gamma>0\), \(\tau>0\) e \(m_K^2>0\), segue:

\[
\boxed{
H_\perp\ge m_\perp^2 I,
\qquad
m_\perp^2=C_\gamma\tau R_{\max}^{-2}>0.
}
\]

No sistema normalizado \(C_\gamma=\tau=R_{\max}=1\):

\[
\boxed{
m_\perp^2=1.
}
\]

---

## 5. Cálculo do bloco misto \(J\)

O bloco misto é:

\[
J(x,y)
=
\delta_x\delta_y\mathcal S_{\rm GDQ}\big|_{\Phi_*}.
\]

No background produto:

1. \(x=x(b)\) não depende de \(\theta\);
2. \(y\) está no complemento toroidal, logo:

\[
\int_{K_5}y\,dV_K=0;
\]

3. a medida fatoriza;
4. não há índices mistos ativos \(BK\);
5. \(\nabla_K f_*=0\).

Todo termo misto contém uma integral toroidal de um modo não constante contra
um modo constante:

\[
\int_{K_5} e_n(\theta)\,dV_K=0
\qquad
(n\ne0).
\]

Logo:

\[
\boxed{
J=0.
}
\]

Esse é o ponto decisivo: no background produto exato, não há acoplamento linear
entre o setor 3D de massa e o complemento toroidal físico.

---

## 6. Complemento de Schur

Como:

\[
J=0,
\]

o complemento de Schur é:

\[
H_B^{\rm eff}
=
H_B-JH_\perp^{-1}J^\dagger
=
H_B.
\]

Portanto:

\[
\boxed{
H_B^{\rm eff}=H_B.
}
\]

Não há deslocamento do índice crítico.

---

## 7. Índice crítico

Como a Hessiana 8D é soma direta:

\[
H_8=H_B\oplus H_\perp,
\]

com:

\[
H_\perp>0
\]

no complemento físico, temos:

\[
\operatorname{ind}^{-}(H_8)
=
\operatorname{ind}^{-}(H_B)
+\operatorname{ind}^{-}(H_\perp)
=
\operatorname{ind}^{-}(H_B).
\]

Logo:

\[
\boxed{
\operatorname{Spec}_{\rm crit}(H_8)
=
\operatorname{Spec}_{\rm crit}(H_B).
}
\]

---

## 8. Conclusão para Perelman

No background produto exato:

\[
\boxed{
\text{a Hessiana 8D não cria instabilidades toroidais nem mistas.}
}
\]

Como o setor crítico 8D coincide exatamente com o setor \(B_3\), a censura
tridimensional de Perelman pode ser usada na GDQ sem afirmar uma geometrização
8D.

Em forma curta:

\[
\boxed{
\text{Perelman regula o setor crítico 3D porque o complemento 5D é positivo.}
}
\]

---

## 9. Consequência para Q39

A exclusão da quarta geração fica fortalecida:

1. o setor \(B_3\) só admite três direções primitivas de tensão;
2. o setor \(K_5\) tem gap no complemento físico;
3. o bloco misto é nulo;
4. o índice crítico 8D é o índice crítico 3D.

Portanto:

\[
\boxed{
\text{não há quarta geração leptônica primitiva no background produto GDQ.}
}
\]

---

## 10. Limitação restante

Este cálculo é completo para o background produto/bloco exato.

Ele deve ser refeito se algum dos seguintes itens for necessário:

1. warp factor não separável;
2. \(\nabla_K f_*\ne0\);
3. torção mista física \(H_{BK}\ne0\);
4. métrica toroidal com curvatura Ricci não nula;
5. modos constantes toroidais reinterpretados como graus dinâmicos de massa.

Nesses casos, \(J\) pode deixar de ser zero e o Schur deixa de ser trivial.

---

## 11. Status

\[
\boxed{
\text{cálculo 8D completo no background produto; caso warped/misto permanece condicional.}
}
\]
