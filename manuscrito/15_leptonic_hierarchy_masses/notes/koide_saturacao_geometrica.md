---
title: "Koide como saturação geométrica"
---

# Koide como saturação geométrica

Defina:

$$
A_i=\sqrt{R_i}.
$$

A condição GDQ é:

$$
\|A_\perp\|^2=\|A_\parallel\|^2.
$$

Ela equivale a:

$$
Q
=
\frac{R_1+R_2+R_3}
{(\sqrt{R_1}+\sqrt{R_2}+\sqrt{R_3})^2}
=
\frac23.
$$

Dados $R_1$ e $R_2$, a terceira razão é:

$$
R_{3,\pm}
=
\left[
2(\sqrt{R_1}+\sqrt{R_2})
\pm
\sqrt{
3R_1+12\sqrt{R_1R_2}+3R_2
}
\right]^2.
$$

A equação de saturação não escolhe o ramo físico. O ramo pesado é o candidato
para o tau carregado no tripleto observado, mas sua seleção dinâmica depende
da Hessiana física do background leptônico. O ramo leve também exige domínio,
contorno e Hessiana próprios antes de qualquer interpretação física.

A equivalência algébrica, a solução pesada e a ordenação dos dois ramos são
certificadas em
[KoideGeometry.lean](../../../formal/GDQ/KoideGeometry.lean) e
[LeptonicHierarchy.lean](../../../formal/GDQ/LeptonicHierarchy.lean).
