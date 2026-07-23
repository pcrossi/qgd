---
title: "Equilíbrio torsional próton--nêutron"
---

# Equilíbrio torsional próton--nêutron

No próton:

$$
(\mathcal T_1,\mathcal T_2,\mathcal T_3)
=
(\tau,\tau,\tau).
$$

No nêutron:

$$
(\mathcal T_1,\mathcal T_2,\mathcal T_3)
=
(\tau,\tau,-2\tau).
$$

Essa segunda configuração satisfaz:

$$
\sum_a\mathcal T_a=0.
$$

A condição vem da variação de fase/torção:

$$
\delta_\vartheta\mathcal S_{\rm GDQ}=0
\quad\Longrightarrow\quad
dJ_{\rm tor}=0.
$$

O excesso de massa do nêutron é:

$$
\delta_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
$$

Ele representa cisalhamento torsional antiparalelo, não energia fixa do
antineutrino.

## 1. De onde vem o fator $\ln(2\pi^2)$

O estômato bariônico possui fronteira topológica homeomorfa a $S^3$. Na
normalização reduzida usada neste capítulo, a contribuição entrópica de
superfície é o logaritmo do volume unitário dessa fronteira:

$$
\operatorname{Vol}(S^3)
=
2\pi^2.
$$

Logo, a escala adimensional de superfície é:

$$
E_{\partial}^{(0)}
=
\ln\operatorname{Vol}(S^3)
=
\ln(2\pi^2).
$$

Esse termo não é uma massa absoluta. Ele é uma energia reduzida de superfície
medida na escala eletrônica usada pelas razões $M_B/M_e$.

## 2. De onde vem o fator $3\sqrt2/5$

O próton tem três tensões alinhadas:

$$
\mathbf t_p
=
(1,1,1).
$$

O nêutron estacionário tem um estômato invertido com o dobro da torção
oposta:

$$
\mathbf t_n
=
(1,1,-2).
$$

A condição de equilíbrio local de corrente torsional é:

$$
\sum_{a=1}^{3}(\mathbf t_n)_a
=
1+1-2
=
0.
$$

Como a orientação comum não mede cisalhamento relativo, o invariante físico
de superfície deve depender das diferenças par-a-par:

$$
I_{\rm sh}^2(\mathbf t)
=
\sum_{a<b}(t_a-t_b)^2.
$$

Para o próton:

$$
I_{\rm sh}^2(\mathbf t_p)
=
0.
$$

Para o nêutron:

$$
I_{\rm sh}^2(\mathbf t_n)
=
(1-1)^2+(1+2)^2+(1+2)^2
=
18.
$$

Assim:

$$
I_{\rm sh}(\mathbf t_n)
=
3\sqrt2.
$$

Esse fator ainda precisa ser projetado no acoplamento entre o setor
tridimensional do estômato e o contínuo local quadridimensional. A projeção
reduzida é expressa pelo triângulo pitagórico $3$-$4$-$5$.

Se $n=3$ é o número de canais torsionais do estômato e $D=4$ é a dimensão
real do contínuo local que recebe a projeção física, então o ângulo de
deflexão de fase $\theta_c$ satisfaz:

$$
\tan\theta_c
=
\frac{D}{n}
=
\frac43.
$$

Logo, a componente transmitida no setor do estômato é:

$$
\cos\theta_c
=
\frac{n}{\sqrt{n^2+D^2}}
=
\frac{3}{\sqrt{3^2+4^2}}
=
\frac35.
$$

Como a variável fundamental é complexa, $f=u+iv$, a superposição coerente
real--imaginária introduz a norma elementar:

$$
\|1+i\|
=
\sqrt2.
$$

Portanto, a admitância reduzida de Fredholm--Fano do setor bariônico é:

$$
\chi_B
=
\sqrt2\cos\theta_c
=
\frac{3\sqrt2}{5}.
$$

O triângulo $3$-$4$-$5$ não é uma numerologia separada do vínculo torsional.
Ele registra a compatibilidade entre três canais internos de estômato e a
projeção física quadridimensional do laboratório. A hipotenusa $5$ aparece
como norma euclidiana da composição $3\oplus4$.

## 3. Resultado reduzido

Multiplicando a escala entrópica de superfície pelo invariante reduzido de
cisalhamento:

$$
\delta_B
=
E_{\partial}^{(0)}\chi_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
$$

Numericamente:

$$
\delta_B
\simeq
2.530825921868.
$$

Status: derivação reduzida condicional. Ela depende da validade da redução
Fredholm--Fano que projeta os três canais torsionais do estômato no contínuo
local quadridimensional. A avaliação numérica correspondente está em
[[../../scripts/saida_derivar_delta_barioes|Saída — derivação reduzida de delta_B]].
