---
title: "Razão do múon por tensão intrínseca"
---

# Razão do múon por tensão intrínseca

Seja $V\simeq\mathbb R^3$ o suporte intrínseco e seja
$P_k:V\to V$ um projetor ortogonal de posto $k$. A fração geométrica ocupada é
o traço normalizado:

$$
\nu_k
=
\frac{\operatorname{tr}P_k}{\operatorname{tr}I_V}
=
\frac{k}{3}.
$$

Para suporte biespacial:

$$
\nu_2=\frac23.
$$

Logo:

$$
R_\mu^{(0)}
=
\frac{1}{\nu_2\alpha}
=
\frac32\alpha^{-1}.
$$

Escreva a impedância reduzida do canal de interface como:

$$
\chi_\partial=\frac{3\sqrt2}{5}.
$$

Depois da projeção normalizada do canal:

$$
\Delta_\partial
=
\sqrt2\,\chi_\partial
=
\sqrt2\frac{3\sqrt2}{5}
=
\frac65.
$$

A simetria global de fase produz uma carga conservada de Noether. No setor
reduzido, uma circulação primitiva contribui com a unidade adimensional
$\alpha$. Como o projetor biespacial contém duas direções ortogonais, a soma
das duas contribuições é:

$$
\Delta_{\rm self}
=
\alpha+\alpha
=
2\alpha.
$$

Portanto:

$$
R_\mu
=
\frac32\alpha^{-1}
+
\frac65
+
2\alpha.
$$

## O que foi provado e o que foi assumido

Uma vez dados $\nu_2$, $\chi_\partial$ e a unidade de circulação, a composição
acima é uma identidade analítica. O ponto ainda condicional é a universalidade
desses dados fora do modelo intrínseco reduzido. Em particular, um background
warped ou com blocos métricos--torsionais mistos deve recalcular a impedância
pela Hessiana física e pelo operador DtN, em vez de reutilizar
automaticamente $3\sqrt2/5$.

A parte algébrica foi formalizada sem `sorry` em
[LeptonicHierarchy.lean](../../../formal/GDQ/LeptonicHierarchy.lean).
