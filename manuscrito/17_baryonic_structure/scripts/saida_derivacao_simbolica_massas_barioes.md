# Saída — derivação simbólica das massas bariônicas

Classificação: derivação simbólica das consequências do modelo reduzido condicional / avaliação direta.

## 1. Unidade reduzida

A unidade metrológica reduzida é:

$$
E_0=M_e c^2,
\qquad
M_B/M_e=\mathcal I_B.
$$

## 2. Bulk de três estômatos

Cada câmara contribui:

$$
\operatorname{Vol}(\mathcal F_a)=2\pi^5.
$$

Para três estômatos:

$$
\mathcal I_B^{\rm bulk}=3(2\pi^5)=6 \pi^{5}.
$$

## 3. Superfície torsional do próton

A transgressão de superfície reduzida é:

$$
\mathcal I_p^\partial=
\frac{3 \alpha \left(1 + 2 \pi^{4}\right)}{4 \pi^{3}}.
$$

Logo:

$$
\frac{M_p}{M_e}=
\frac{3 \left(\alpha \left(1 + 2 \pi^{4}\right) + 8 \pi^{8}\right)}{4 \pi^{3}}.
$$

## 4. Excesso torsional do nêutron

Configurações torsionais:

$$
\mathbf t_p=(1,1,1),
\qquad
\mathbf t_n=(1,1,-2).
$$

Invariante par-a-par:

$$
I_{\rm sh}^2(\mathbf t)=\sum_{a<b}(t_a-t_b)^2.
$$

Para o próton e o nêutron:

$$
I_{\rm sh}^2(\mathbf t_p)=0,
\qquad
I_{\rm sh}^2(\mathbf t_n)=18.
$$

A projeção Fredholm--Fano usa:

$$
\cos\theta_c=\frac{3}{\sqrt{3^2+4^2}}=\frac{3}{5},
\qquad
\|1+i\|=\sqrt2.
$$

Assim:

$$
\chi_B=\sqrt2\cos\theta_c=\frac{3 \sqrt{2}}{5}.
$$

Como $\operatorname{Vol}(S^3)=2\pi^2$:

$$
\delta_B=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
$$

A forma simbólica equivalente avaliada pelo código é:

$$
\log{\left(\left(2 \pi^{2}\right)^{\frac{3 \sqrt{2}}{5}} \right)}.
$$

Portanto:

$$
\frac{M_n}{M_e}=\frac{M_p}{M_e}+\delta_B.
$$

## 5. Avaliação numérica

| quantidade | valor |
|---|---:|
| alpha^-1 | 137.035999177000 |
| bulk 6*pi^5 | 1836.118108711689 |
| superfície torsional | 0.034564476923 |
| delta_B | 2.530825921868 |
| Mp/Me | 1836.152673188612 |
| Mn/Me | 1838.683499110479 |

## 6. Comparação posterior

| razão | GDQ | referência | erro relativo |
|---|---:|---:|---:|
| Mp/Me | 1836.152673188612 | 1836.152673426000 | -1.292856117250e-10 |
| Mn/Me | 1838.683499110479 | 1838.683662000000 | -8.859029086476e-08 |

## Veredito

As fórmulas seguem das hipóteses do modelo reduzido: volume de três câmaras, coeficientes de transgressão e projeção 3--4--5. O script não demonstra que a sela 8D seleciona esses coeficientes. Os valores aceitos entram somente depois, como comparação.
