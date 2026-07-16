# Ponte global--local — equações do subsector exterior isotrópico

## 1. Funcional

Use a ação reduzida derivada em
`ponte_global_local_exterior_warped.md`, incluindo o multiplicador $\lambda_N$
da normalização:

$$
I_+
=\int ds\,N\mathscr V
\left[
\tau\mathcal K_+
+u-4-\lambda_N
\right],
$$

com

$$
\mathscr V=e^{4x+3y-u}.
$$

Separe

$$
\mathcal K_+
=\mathcal K_2+4e^{-y}\dot y+4e^{-2y},
$$

onde

$$
\begin{aligned}
\mathcal K_2
=\;&8\dot x^2+4\dot y^2+24\dot x\dot y
-8\dot u\dot x-6\dot u\dot y\\
&+\dot u^2+\dot v^2.
\end{aligned}
$$

## 2. Restrição do lapse

Variando $N$ antes de escolher a parametrização, os termos lineares em
velocidade cancelam pela identidade de Euler. Resulta

$$
\boxed{
\mathcal C_N
=\tau\left(4e^{-2y}-\mathcal K_2\right)
+u-4-\lambda_N=0.
}
$$

Essa equação deve ser preservada durante toda a integração.

## 3. Momentos canônicos

Na gauge $N=1$,

$$
\boxed{
p_x
=\tau\mathscr V
\left(16\dot x+24\dot y-8\dot u\right),
}
$$

$$
\boxed{
p_y
=\tau\mathscr V
\left(24\dot x+8\dot y-6\dot u+4e^{-y}\right),
}
$$

$$
\boxed{
p_u
=\tau\mathscr V
\left(-8\dot x-6\dot y+2\dot u\right),
}
$$

$$
\boxed{
p_v=2\tau\mathscr V\dot v.
}
$$

## 4. Inversão exata

Defina

$$
r_x=\frac{p_x}{\tau\mathscr V},
$$

$$
r_y=\frac{p_y}{\tau\mathscr V}-4e^{-y},
$$

$$
r_u=\frac{p_u}{\tau\mathscr V}.
$$

A matriz cinética possui determinante $320$ e é invertível. As velocidades
são

$$
\boxed{
\dot x=-\frac1{16}r_x-\frac14r_u,
}
$$

$$
\boxed{
\dot y=-\frac1{10}r_y-\frac3{10}r_u,
}
$$

$$
\boxed{
\dot u=-\frac14r_x-\frac3{10}r_y-\frac75r_u,
}
$$

$$
\boxed{
\dot v=\frac{p_v}{2\tau\mathscr V}.
}
$$

## 5. Equações dos momentos

Defina

$$
F=\tau\mathcal K_++u-4-\lambda_N.
$$

As equações de Euler--Lagrange assumem a forma canônica

$$
\boxed{
\dot p_x=4\mathscr V F,
}
$$

$$
\boxed{
\dot p_y
=\mathscr V
\left[
3F+\tau\left(-4e^{-y}\dot y-8e^{-2y}\right)
\right],
}
$$

$$
\boxed{
\dot p_u=\mathscr V(1-F),
}
$$

$$
\boxed{
\dot p_v=0.
}
$$

A última igualdade é a conservação exata do fluxo de fase.

## 6. Normalização

Introduza uma variável acumulada

$$
\dot Z=\mathscr V,
$$

com

$$
Z(s_+)-Z(s_-)=Z_{\rm cos},
$$

onde o prefator de volume de $T^4\times S^3$ e a medida de $\gamma$ devem ser
restaurados na definição física de $Z_{\rm cos}$.

## 7. Dados de fronteira

O exterior é um problema de duas interfaces, não um problema regular num
único polo. Em $s=s_-$ e $s=s_+$ devem valer:

$$
p_A^++p_A^-=0,
$$

para cada traço físico $A$, com cargas relativas opostas e fluxo total nulo.
Além disso,

$$
\mathcal C_L=0,
\qquad
\mathcal C_R=0,
\qquad
\mathcal C_E=0.
$$

## 8. Estrutura do solver

O vetor de estado exterior é

$$
Y=(x,y,u,v,p_x,p_y,p_u,p_v,Z).
$$

Os parâmetros de tiro são os traços numa interface, os multiplicadores e os
dados conjugados não fixados. O resíduo contém:

1. colagem dos quatro momentos nas duas interfaces;
2. restrição do lapse;
3. normalização;
4. três vínculos cosmológicos;
5. neutralidade global.

## 9. Observação sobre a forma cinética

A matriz cinética de $(x,y,u)$ é invertível, mas indefinida. Isso não é, por
si só, uma instabilidade física: uma direção é longitudinal ao lapse e outras
podem pertencer ao setor conforme/vinculado. A estabilidade deve ser testada
somente depois de aplicar $P^{\rm phys}$ à Hessiana da solução.

## 10. Status e limite de validade

$$
\boxed{
\text{equações isotrópicas de primeira ordem e restrição do lapse derivadas.}
}
$$

O teste numérico valida esse subsector, mas ele não deve ser colado diretamente
ao DtN interno de quatro traços. A colagem completa exige os dois raios de
Berger e é formulada em `ponte_global_local_exterior_berger.md`.
