# Q51 — Aproximação espectral inicial de \(\mathsf R_\partial^{\rm GDQ}\)

## 1. Objetivo

Depois do no-go para fórmulas escalares, testamos uma aproximação mais fiel à
GDQ: reaproveitar a base variacional de impedância coletiva da Q40.

A Q40 fornece:

$$
\mathcal I_\Sigma(x)
=
j_0^2\frac{x^2}{1+x}
+j_1^2\frac{x^2}{(1+x)^2}
+j_2^2\frac{x^3}{(1+x)^2}.
$$

com:

$$
j_0=1{,}712091781054,
\quad
j_1=1{,}341454657186,
\quad
j_2=1{,}063840998206.
$$

## 2. Variável de canal alfa

Para o canal alfa, testamos:

$$
\chi_{\rm curv}
=
\frac{\delta_{\rm touch}^2}{x_{\rm barrier}},
$$

onde:

$$
\delta_{\rm touch}
=
\frac{R_{\rm touch}-R_{\rm pai}}{R_{\rm pai}},
$$

e:

$$
x_{\rm barrier}
=
\frac{V_C(R_{\rm touch})}{Q_\alpha}-1.
$$

## 3. Escala testada

A escala geométrica reduzida testada foi:

$$
E_\partial^{\rm spec}
=
\frac4{\alpha}\mathcal I_\Sigma(\chi_{\rm curv}).
$$

Interpretação:

1. o fator \(4\) conta os quatro nucleons do cluster alfa;
2. \(1/\alpha\) representa a complacência eletrogeométrica global;
3. essa escala é hipótese reduzida, não derivação completa.

## 4. Resultado

A saída está em:

- `saida_aproximacao_espectral_Rpartial_q51.md`.

Resumo:

| Núcleo | \(E_\partial^{\rm req}\) | \(E_\partial^{\rm spec}\) |
| --- | ---: | ---: |
| U-238 | \(0{,}000000\) | \(0{,}329982\) |
| U-234 | \(0{,}425065\) | \(0{,}453031\) |
| U-232 | \(0{,}373825\) | \(0{,}592495\) |
| Th-232 | \(0{,}000000\) | \(0{,}318344\) |
| Ra-226 | \(0{,}422411\) | \(0{,}519740\) |
| Po-212 | \(1{,}557848\) | \(3{,}067555\) |

## 5. Interpretação

A aproximação acerta a ordem de grandeza em U-234 e Ra-226, mas:

1. gera energia positiva em U-238 e Th-232, onde o diagnóstico pede quase zero;
2. superestima Po-212;
3. portanto, não pode ser o fechamento final.

O que falta é o projetor físico de canal:

$$
P_\perp\Phi_{4N},
$$

que deve anular ou reduzir o overlap em canais incompatíveis e amplificar
apenas as componentes realmente alfa-preformadas.

## 6. Veredito

$$
\boxed{
\text{a impedância média está na escala correta, mas falta o projetor espectral de canal.}
}
$$

Próximo passo: construir \(P_\perp\) a partir dos números quânticos de
superfície e do espectro de camada do background nuclear.

