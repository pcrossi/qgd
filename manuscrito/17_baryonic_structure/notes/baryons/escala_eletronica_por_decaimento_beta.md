---
title: "Escala eletrônica por decaimento beta"
---

# Escala eletrônica por decaimento beta

Esta nota registra uma consequência metrológica importante da construção
bariônica reduzida.

No setor bariônico, as massas são obtidas em unidades eletrônicas:

$$
\frac{M_p}{M_e},
\qquad
\frac{M_n}{M_e}.
$$

A diferença nêutron--próton é:

$$
\frac{M_n-M_p}{M_e}
=
\delta_B.
$$

Como o decaimento beta livre possui endpoint:

$$
Q_\beta
=
M_n-M_p-M_e,
$$

segue:

$$
Q_\beta
=
(\delta_B-1)M_ec^2.
$$

Logo:

$$
M_ec^2
=
\frac{Q_\beta}{\delta_B-1}.
$$

Com:

$$
\delta_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5}
\simeq
2.530825921868,
$$

e usando o endpoint experimental do beta livre como dado de contorno
metrológico:

$$
Q_\beta
\simeq
0.78233356\,{\rm MeV},
$$

obtemos:

$$
M_ec^2
\simeq
0.51105325\,{\rm MeV}.
$$

Comparado ao valor de referência:

$$
M_ec^2_{\rm ref}
=
0.51099895\,{\rm MeV},
$$

o erro relativo é:

$$
\frac{0.51105325-0.51099895}{0.51099895}
\simeq
1.06\times10^{-4}.
$$

## Leitura física

Essa não é uma previsão absoluta de unidade a partir do nada. O endpoint
$Q_\beta$ é um dado físico de contorno/metrologia. O que a GDQ fornece é a
ponte geométrica:

$$
\delta_B-1,
$$

que converte o endpoint beta em escala eletrônica.

Portanto, o status correto é:

$$
\boxed{
\text{determinação metrológica da escala eletrônica por endpoint beta.}
}
$$

Ela é mais forte que simplesmente escolher $M_e$ como unidade, mas permanece
dependente do dado experimental $Q_\beta$.

Verificação autocontida:
[[../../scripts/saida_escala_eletronica_beta|Saída — escala eletrônica por beta]].
