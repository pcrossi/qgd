---
title: "Noether, três estômatos e Hessiana"
---

# Noether, três estômatos e Hessiana

## 1. Vínculo de Noether

Com:

$$
f=u+iv,
$$

a simetria $v\mapsto v+\varepsilon$ gera conservação de corrente. No junction:

$$
\sum_{a=1}^{N}\mathbf T_a=0.
$$

As tensões pertencem à distribuição horizontal de Hopf:

$$
\mathcal H=\ker\eta_H,
\qquad
\dim_{\mathbb R}\mathcal H=2.
$$

## 2. Seleção de $N=3$

Um junction elementar precisa ser fechado, não colinear e isolado. Em dimensão
horizontal dois:

$$
N\ge3.
$$

Para $N>3$ aparecem $N-3$ modos internos nulos. Isolamento exige:

$$
N-3=0.
$$

Logo:

$$
N=3.
$$

## 2.1 Forma precisa por posto--nulidade

Seja:

$$
D\mathcal C:
\mathbb R^N\longrightarrow\mathbb R^2
$$

a linearização do vínculo horizontal. A não colinearidade regular exige:

$$
\operatorname{rank}D\mathcal C=2.
$$

Pelo teorema de posto--nulidade:

$$
\dim\ker D\mathcal C=N-2.
$$

Uma dessas direções é a rotação simultânea de todas as tensões. Logo, depois
de removê-la, a dimensão do kernel interno é:

$$
\dim\ker_{\rm interno}D\mathcal C=N-3.
$$

O junction elementar isolado exige kernel interno nulo. Portanto:

$$
N-3=0
\quad\Longrightarrow\quad
N=3.
$$

Essa implicação foi certificada em
[GenerationJunction.lean](../../../formal/GDQ/GenerationJunction.lean).
O teorema Lean mantém posto dois e isolamento como hipóteses explícitas; ele
não as atribui silenciosamente a backgrounds warped ou mistos não
diagonalizados.

## 3. Hessiana vinculada

O vínculo é:

$$
\mathcal C
=
\sum_{a=1}^{3}\mathbf T_a.
$$

O funcional aumentado é:

$$
\widetilde{\mathcal S}
=
\mathcal S_{\rm GDQ}
+
\boldsymbol\lambda\cdot\mathcal C.
$$

A Hessiana angular é:

$$
H_\theta
=
\kappa_{\rm rel}(D\mathcal C)^\dagger D\mathcal C.
$$

No equilíbrio $C_3$:

$$
\operatorname{spec}H_\theta
=
\kappa_{\rm rel}T^2
\left\{
0,
\frac32,
\frac32
\right\}.
$$

Projetando fora a rotação global:

$$
H_{\rm rel}
=
\frac32\kappa_{\rm rel}T^2I_2.
$$

Como $J_{\theta r}=0$, o complemento de Schur mantém:

$$
H_{\rm eff}=H_{\rm rel}.
$$

Status: estabilidade coletiva fechada no modelo horizontal reduzido.
