---
title: "Equivalência operacional GDQ-Yang-Mills"
---

# Equivalência operacional GDQ--Yang--Mills

A equivalência relevante não é uma identificação entre todos os campos brutos.
A GDQ possui graus geométricos adicionais. A equivalência setorial é entre
classes topológicas, álgebras reduzidas de observáveis e funções de resposta.

## 1. Mapa topológico

Seja:

$$
\Theta:
\mathfrak T_{\rm GDQ}
\longrightarrow
\mathfrak T_{\rm YM}
$$

o mapa entre classes topológicas do setor tubular GDQ e classes de laços/fontes
do setor efetivo. Ele preserva composição, orientação e carga:

$$
\Theta([C_1\circ C_2])
=
\Theta([C_1])\circ\Theta([C_2]),
$$

$$
Q_T(C)
=
Q_{\rm YM}(\Theta C).
$$

## 2. Álgebra de observáveis

Nos geradores de holonomia:

$$
\mathfrak H_\Theta(U_C^{\rm YM})
:=
U_{\Theta^{-1}C}^{\rm GDQ}.
$$

Nos observáveis de resposta:

$$
\mathfrak H_\Theta[F(P_\mu^{\rm YM})]
:=
F(P_\mu^{\rm GDQ,red}),
$$

com:

$$
P_\mu=-\Delta+\mu^2,
\qquad
\mu>0.
$$

No setor confinante, a função de transferência estática é:

$$
F_\mu(k^2)
=
-\frac{8\pi\sigma}{(k^2+\mu^2)^2}.
$$

Sua transformada estática, com subtração da constante, dá:

$$
V_\mu(r)
=
\sigma\frac{1-e^{-\mu r}}{\mu}.
$$

Logo:

$$
\lim_{\mu\to0^+}V_\mu(r)
=
\sigma r.
$$

## 3. Lema 1 — boa definição

Se $C\sim C'$ no quociente de gauge/topologia, então
$\Theta^{-1}[C]=\Theta^{-1}[C']$. Os transportes correspondentes diferem por
conjugação:

$$
U_{\Theta^{-1}C'}
=
g^{-1}U_{\Theta^{-1}C}g.
$$

Para laços fechados:

$$
{\rm tr}(g^{-1}Ug)={\rm tr}(U).
$$

Assim $\mathfrak H_\Theta$ é bem definido nos observáveis gauge-invariantes.

## 4. Lema 2 — preservação das relações

Como $\Theta$ preserva composição e orientação:

$$
\mathfrak H_\Theta(U_{C_1\circ C_2})
=
\mathfrak H_\Theta(U_{C_1})
\mathfrak H_\Theta(U_{C_2}),
$$

$$
\mathfrak H_\Theta(U_C^*)
=
\mathfrak H_\Theta(U_C)^*,
\qquad
\mathfrak H_\Theta(1)=1.
$$

Como $P_\mu$ é positivo e auto-adjunto:

$$
(FG)(P_\mu)=F(P_\mu)G(P_\mu),
\qquad
\overline F(P_\mu)=F(P_\mu)^*.
$$

Portanto o mapa se estende a um $*$-homomorfismo.

## 5. Lema 3 — isomorfismo setorial e estado

Se $\Theta$ é bijetivo no setor físico reduzido, define-se a inversa:

$$
\mathfrak K_\Theta(U_D^{\rm GDQ})
:=
U_{\Theta D}^{\rm YM}.
$$

Então:

$$
\mathfrak K_\Theta\circ\mathfrak H_\Theta
=
{\rm id},
\qquad
\mathfrak H_\Theta\circ\mathfrak K_\Theta
=
{\rm id}.
$$

Defina:

$$
\widetilde\omega_{\rm YM}(O)
:=
\omega_{\rm GDQ}(\mathfrak H_\Theta O).
$$

Se o estado GDQ na thimble física é positivo e normalizado, então:

$$
\widetilde\omega_{\rm YM}(O^*O)\ge0,
\qquad
\widetilde\omega_{\rm YM}(1)=1.
$$

Sob unicidade do vácuo axiomático no setor efetivo:

$$
\omega_{\rm GDQ}\circ\mathfrak H_\Theta
=
\omega_{\rm YM}.
$$

## 6. Teorema setorial

No setor tubular físico reduzido, sob bijetividade de $\Theta$, positividade da
thimble GDQ e unicidade do estado efetivo, temos:

$$
\boxed{
\mathfrak A_{\rm YM}^{\rm red}
\simeq
\mathfrak A_{\rm GDQ}^{\rm red}.
}
$$

Consequentemente:

$$
\langle O_1\cdots O_n\rangle_{\rm YM}
=
\left\langle
\mathfrak H_\Theta(O_1)\cdots
\mathfrak H_\Theta(O_n)
\right\rangle_{\rm GDQ}.
$$

Esse é o sentido preciso em que Yang--Mills clássico é recuperado pela GDQ no
setor de cor. Não é troca da ação oficial por uma ação de Yang--Mills.

