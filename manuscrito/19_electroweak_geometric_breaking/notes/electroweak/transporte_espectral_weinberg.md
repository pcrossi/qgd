---
title: "Transporte espectral do ângulo de Weinberg"
---

# Transporte espectral do ângulo de Weinberg

Esta nota separa o ponto geométrico comum do valor operacional após transporte.
Ela também registra a comparação numérica usada apenas como diagnóstico.

## 1. Ponto comum

No ponto geométrico comum herdado da taxonomia interna:

$$
I_2=2,
\qquad
I_Y=\frac{10}{3}.
$$

Assim:

$$
\frac{g'^2}{g^2}
=
\frac35,
$$

e:

$$
\sin^2\theta_W
=
\frac{g'^2}{g^2+g'^2}
=
\frac38.
$$

Esse valor é a correspondência local. Ele não deve ser forçado a ser o valor
operacional medido em outra escala.

## 2. Transporte diferencial

Se as rigidezes são transportadas por fatores $Z_W$ e $Z_Y$:

$$
\frac1{g_{\rm EW}^2}
=
Z_W\frac1{g_{\rm match}^2},
$$

$$
\frac1{g_{\rm EW}'{}^2}
=
Z_Y\frac1{g_{\rm match}'{}^2},
$$

então:

$$
\frac{g_{\rm EW}'{}^2}{g_{\rm EW}^2}
=
\frac35\frac{Z_W}{Z_Y}.
$$

O valor operacional:

$$
\sin^2\theta_W=\frac29
$$

equivale a:

$$
\frac{g'^2}{g^2}=\frac27.
$$

Logo a condição necessária e suficiente é:

$$
\boxed{
\frac{Z_W}{Z_Y}
=
\frac{10}{21}.
}
$$

Essa é uma condição de transporte. Ela não altera a ação oficial e não deve
ser imposta como alvo.

## 3. Transporte espectral reduzido

No modelo reduzido, as rigidezes são lidas como traços de calor da Hessiana:

$$
K_a(s)
=
C_{\rm GDQ}{\rm Tr}
\left(
T_a^2e^{-s\mathcal O_a}
\right).
$$

O cálculo espectral reduzido mostra a transição:

$$
\frac38
\longrightarrow
\frac29
$$

em:

$$
s_\ast=5{,}9090386\times10^6.
$$

O parâmetro $s$ é adimensional. A escala de resolução associada é:

$$
\frac{Q_\ast}{\Lambda_0}
=
\frac1{\sqrt{s_\ast}}
=
4{,}113784964\times10^{-4}.
$$

Com a calibração interna do operador:

$$
\Lambda_0=126354{,}3162\,{\rm GeV},
$$

segue:

$$
Q_\ast=51{,}97944877\,{\rm GeV}.
$$

Esse número é escala de resolução do semigrupo, não automaticamente massa de
partícula.

## 4. Comparação W/Z

Com:

$$
v=246{,}111195996\,{\rm GeV},
$$

e a identidade condicional:

$$
\alpha_{\rm EW}^{-1}=132{,}457669,
\qquad
\sin^2\theta_W=\frac29,
$$

obtém-se:

$$
m_W=80{,}403325\,{\rm GeV},
$$

$$
m_Z=91{,}168801\,{\rm GeV}.
$$

Comparando com os valores de referência usados no diagnóstico:

$$
m_W^{\rm ref}=80{,}379\,{\rm GeV},
\qquad
m_Z^{\rm ref}=91{,}1876\,{\rm GeV},
$$

os erros são aproximadamente:

$$
\delta_W=+0{,}0303\%,
\qquad
\delta_Z=-0{,}0206\%.
$$

## 5. Status

O transporte espectral é uma rota quantitativamente forte. O fechamento
metrológico final exige derivar $Z_W/Z_Y$ e $\alpha_{\rm EW}$ diretamente da
Hessiana global de contorno, sem usar $m_W$ ou $m_Z$ como alvo.

## 6. Verificação computacional

O script:

$$
{\tt scripts/transporte\_weinberg\_condicional.py}
$$

calcula a condição $Z_W/Z_Y=10/21$, a escala $Q_\ast$, os valores $W/Z$ e os
erros relativos.
