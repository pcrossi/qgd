# Q34 — Coeficiente não abeliano líder pelo heat kernel

## 1. Escopo

Este cálculo estende o coeficiente local de $F^2$ ao setor não abeliano no
formalismo de campo de fundo. Ele é uma auditoria perturbativa externa da
redução GDQ; não transforma Yang--Mills, fantasmas ou BRST em ontologia.

O grupo $G$ é compacto, a conexão de fundo é $\bar A$ e a curvatura é
$\bar F$.

## 2. Operadores obrigatórios

No gauge de fundo de Feynman, o operador vetorial mínimo é

$$
(\Delta_1)_\mu{}^\nu
=
-\bar D^2\delta_\mu{}^\nu
-2\,\operatorname{ad}(\bar F_\mu{}^\nu)
+\operatorname{Ric}_\mu{}^\nu.
$$

O jacobiano de órbita é representado pelo operador escalar adjunto

$$
\Delta_0=-\bar D^2.
$$

Para férmions na representação $R$,

$$
\Delta_{1/2}
=
\slashed D^\dagger\slashed D+m^2.
$$

A combinação de um loop é

$$
\boxed{
\Gamma^{(1)}
=
\frac12\operatorname{Tr}\log\Delta_1
-\operatorname{Tr}\log\Delta_0
-\sum_f\log\det(\slashed D_{R_f}+m_f).
}
$$

O segundo termo é o jacobiano geométrico; sua escrita por fantasmas é apenas
representação computacional.

## 3. Coeficiente de Seeley--DeWitt

Para um operador de tipo Laplace

$$
\Delta=-(\nabla^2+E),
$$

o coeficiente local quadrático em curvaturas contém, em quatro dimensões,

$$
a_4(\Delta)
\supset
\frac1{(4\pi)^2}
\int
\operatorname{tr}
\left(
\frac1{12}\Omega_{\mu\nu}\Omega^{\mu\nu}
+\frac12E^2
\right)dV,
$$

além dos termos puramente gravitacionais e derivadas totais.

Aplicando essa fórmula à combinação vetorial--jacobiano--matéria, o
coeficiente universal é

$$
\boxed{
b_0
=
\frac{11}{3}C_A
-\frac{4}{3}\sum_{\rm Dirac}T(R_f)
-\frac{1}{6}\sum_{\rm escalar\ real}T(R_s).
}
$$

Para campos de Weyl, cada contribuição fermiônica vale metade da contribuição
de Dirac. Para escalares complexos, cada contribuição vale duas vezes a de um
escalar real.

As convenções de grupo são

$$
\operatorname{tr}_R(T^aT^b)=T(R)\delta^{ab},
\qquad
f^{acd}f^{bcd}=C_A\delta^{ab}.
$$

## 4. Coeficiente local finito

Introduzindo uma escala espectral infravermelha positiva $\mu_{\rm gap}$,

$$
\int_\tau^\infty\frac{ds}{s}e^{-s\mu_{\rm gap}^2}
=
E_1(\tau\mu_{\rm gap}^2).
$$

Na convenção

$$
\Gamma_{\rm loc}
\supset
\frac14
\Delta\!\left(\frac1{g^2}\right)
\int\operatorname{tr}(F_{\mu\nu}F^{\mu\nu})\,dV,
$$

temos

$$
\boxed{
\Delta\!\left(\frac1{g^2}\right)_\tau
=
\frac{b_0}{16\pi^2}
E_1(\tau\mu_{\rm gap}^2).
}
$$

Essa expressão é condicional à convenção do operador e à existência do gap.
Sem gap, a integral absoluta diverge no extremo $s\to\infty$: é uma
divergência infravermelha do setor sem massa, não uma divergência
ultravioleta.

A diferença entre duas resoluções é definida sem escolher contratermo:

$$
\boxed{
\Delta_{\tau_1\to\tau_2}
\left(\frac1{g^2}\right)
=
\frac{b_0}{16\pi^2}
\left[
E_1(\tau_2\mu_{\rm gap}^2)
-E_1(\tau_1\mu_{\rm gap}^2)
\right].
}
$$

## 5. Aplicação aos setores efetivos da Q28

### $SU(3)_C$

Para $C_A=3$, $T(\mathbf3)=1/2$ e seis sabores Dirac efetivos,

$$
\boxed{
b_0^{SU(3)}=11-\frac23\,6=7.
}
$$

Esse valor é a tradução perturbativa externa do espectro de três gerações. Ele
não substitui a prova geométrica de confinamento da Q30.

### $SU(2)_L$

Por geração existem três doublets de Weyl coloridos e um doublet leptônico.
Em três gerações há doze doublets de Weyl. Assim, sem contar o modo de ordem,

$$
b_{0,\rm ferm}^{SU(2)}
=
\frac{22}{3}
-\frac23\left(12\cdot\frac12\right)
=
\frac{10}{3}.
$$

Se o modo de ordem eletrofraco efetivo propagar no loop como um doublet
escalar complexo, sua contribuição é $1/6$, fornecendo

$$
\boxed{
b_0^{SU(2)}
=
\frac{19}{6}.
}
$$

Essa última inclusão é condicional: $\Phi_{\rm EW}$ é modo geométrico e sua
medida de flutuações deve vir da Hessiana, não ser importada como Higgs
fundamental.

## 6. O que foi fechado

1. os operadores vetorial e de jacobiano foram combinados;
2. o coeficiente universal $a_4$ de $F^2$ foi identificado;
3. os fatores de grupo de $SU(3)$ e $SU(2)$ foram avaliados;
4. a necessidade de gap ou diferença de escalas foi explicitada;
5. a interpretação de fantasmas permaneceu auxiliar.

## 7. O que ainda falta

1. calcular $a_6$, que contém a base de dimensão seis
   $\operatorname{tr}(D_\rho F_{\mu\nu})^2$ e
   $\operatorname{tr}(F_\mu{}^\nu F_\nu{}^\rho F_\rho{}^\mu)$;
2. obter $\mu_{\rm gap}$ do espectro físico de cada setor;
3. avaliar o jacobiano em fibrados topologicamente não triviais;
4. testar a dependência dos coeficientes sob kernels covariantes admissíveis.

## 8. Classificação

- fórmula de $a_4$ e $b_0$: **auditoria perturbativa externa**;
- contagem $SU(3)$: **avaliação direta do espectro efetivo da Q28**;
- contagem $SU(2)$ com modo de ordem: **condicional à propagação do modo**;
- valor absoluto de $c_F$: **condicional ao gap espectral**.

## 9. Referência

D. V. Vassilevich, “Heat kernel expansion: user's manual”,
*Physics Reports* **388** (2003) 279--360,
DOI: 10.1016/j.physrep.2003.09.002,
arXiv:hep-th/0306138. Foram usadas a fórmula universal de $a_4$ e a aplicação
ao operador vetorial e ao jacobiano de Yang--Mills em espaço plano.
