# Q34 — Parte de matéria de $a_6$ e obstrução do termo $F^3$

## 1. Objetivo

O coeficiente $a_6$ não abeliano contém dois invariantes gauge independentes
em espaço plano, módulo identidades de Bianchi, integrações por partes e
equações de movimento:

$$
\mathcal O_{2G}
=
\operatorname{tr}
(D_\rho F_{\mu\nu}D^\rho F^{\mu\nu}),
$$

$$
\mathcal O_{3G}
=
\operatorname{tr}
(F_\mu{}^\nu F_\nu{}^\rho F_\rho{}^\mu).
$$

Este documento separa o que pode ser obtido da polarização de dois pontos do
que exige o vértice de três pontos ou o coeficiente universal completo.

## 2. Generalização da polarização de matéria

Para um férmion Dirac na representação $R$,

$$
\operatorname{tr}_R(T^aT^b)
=
T(R)\delta^{ab}.
$$

O resultado abeliano

$$
A_1^{U(1)}
=
\frac{e^2Q^2}{60\pi^2}e^{-\tau m^2}
$$

generaliza diretamente para

$$
\boxed{
A_{1,R}^{\rm Dirac}
=
\frac{g^2T(R)}{60\pi^2}
e^{-\tau m^2}.
}
$$

Para várias espécies,

$$
\boxed{
A_{1,\rm matter}
=
\frac{g^2}{60\pi^2}
\sum_f T(R_f)e^{-\tau m_f^2}.
}
$$

Na convenção

$$
\Gamma^{(2)}
=
\frac14\int
F_{\mu\nu}
\Pi(-D^2)
F^{\mu\nu}\,dV,
$$

o coeficiente de dimensão seis é

$$
\boxed{
c_{2G}^{\rm matter}
=
\frac{g^2}{240\pi^2}
\sum_f
\frac{T(R_f)}{m_f^2}
e^{-\tau m_f^2}.
}
$$

Essa expressão é uma tradução perturbativa externa do setor de matéria.
Massas e representações devem vir do espectro efetivo da GDQ ou ser
declaradas como dados externos.

## 3. Limite de Weyl

Para um férmion de Weyl, a contribuição é metade:

$$
\boxed{
c_{2G}^{\rm Weyl}
=
\frac12c_{2G}^{\rm Dirac}.
}
$$

Isso é relevante para $SU(2)_L$, cujo espectro quiral foi organizado na Q28.

## 4. Por que $F^3$ não segue da polarização

A polarização calcula a segunda derivada da ação efetiva:

$$
\Pi_{\mu\nu}^{ab}
=
\frac{\delta^2\Gamma}
{\delta A_\mu^a\delta A_\nu^b}
\bigg|_{A=0}.
$$

O operador $\mathcal O_{3G}$ começa em terceira ordem no campo de fundo.
Portanto,

$$
\frac{\delta^2}{\delta A\,\delta A}
\int\mathcal O_{3G}
\bigg|_{A=0}=0.
$$

Logo,

$$
\boxed{
\text{o coeficiente de }F^3
\text{ não pode ser reconstruído de }\Pi_{\mu\nu}.
}
$$

Inferi-lo por comparação com $A_1$ seria matematicamente circular.

## 5. Operador necessário para completar $a_6$

O cálculo restante deve aplicar o coeficiente universal $a_6$ à combinação

$$
\frac12a_6(\Delta_1)
-a_6(\Delta_0)
-\sum_f a_6(\Delta_{1/2,f}),
$$

com

$$
(\Delta_1)_\mu{}^\nu
=
-D^2\delta_\mu{}^\nu
-2\operatorname{ad}(F_\mu{}^\nu)
+\operatorname{Ric}_\mu{}^\nu,
$$

$$
\Delta_0=-D^2.
$$

Depois, todos os termos devem ser reduzidos à mesma base
$(\mathcal O_{2G},\mathcal O_{3G})$. Em fundo Hermitiano/Bismut, aparecem
também invariantes mistos com curvatura e torção, que não podem ser descartados
antes de especificar o background.

## 6. Resultado

$$
\boxed{
\text{a parte de matéria de }\mathcal O_{2G}\text{ está calculada;}
\quad
\text{o bloco vetor--jacobiano e }\mathcal O_{3G}\text{ permanecem abertos.}
}
$$

## 7. Classificação

- $c_{2G}^{\rm matter}$: **derivação perturbativa externa a partir do loop já
  calculado**;
- aplicação ao espectro Q28: **condicional às massas e aos modos propagantes**;
- coeficiente de $F^3$: **não determinado**;
- termos mistos Bismut: **dependentes do background completo**.

## 8. Referências

1. D. V. Vassilevich, “Heat kernel expansion: user's manual”,
   *Physics Reports* **388** (2003) 279--360,
   DOI: 10.1016/j.physrep.2003.09.002,
   arXiv:hep-th/0306138. Fórmula universal de $a_6$ para operadores de tipo
   Laplace.
2. P. B. Gilkey, “The spectral geometry of a Riemannian manifold”,
   *Journal of Differential Geometry* **10** (1975) 601--618. Fonte original
   do coeficiente $a_6$ citada na revisão acima.
