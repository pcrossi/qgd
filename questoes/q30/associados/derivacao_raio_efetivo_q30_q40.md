# Q30/Q40 — derivação do raio efetivo de superfície

## Enunciado

Queremos obter o raio usado no fator de forma da Q30 sem ajustá-lo pela tensão
hadrônica.

O raio canônico já consolidado na Q40 é um raio eletromagnético de superfície,
não uma média volumétrica do bulk:

$$
r_p=C_r\epsilon_{\rm eff}R_B.
$$

## Cadeia dedutiva

Da Q39, o raio angular efetivo do estômato é:

$$
\epsilon_{\rm eff}
=\frac{5\alpha}{\pi}
-\left(
\frac49\alpha^2-\frac\pi2\alpha^3
\right).
$$

Numericamente:

$$
\epsilon_{\rm eff}
=0.011591040463.
$$

Da Q40, a projeção Hopf de superfície fornece:

$$
C_r=\frac18\left(1+\frac\alpha4\right).
$$

Numericamente:

$$
C_r=0.125228042268.
$$

A escala bariônica é:

$$
R_B=\frac32\Lambda_C.
$$

Com:

$$
\Lambda_C=386.159268\,\mathrm{fm},
$$

obtemos:

$$
R_B=579.238902000000\,\mathrm{fm}.
$$

Portanto:

$$
r_p
=C_r\epsilon_{\rm eff}R_B
=0.840778765450\,\mathrm{fm}.
$$

## Aplicação à Q30

O cap primitivo da Q30 usava:

$$
r_\perp=0.860000000000\,\mathrm{fm}.
$$

O fator de forma induzido pelo raio de superfície derivado é:

$$
F_{\rm shape}
=\left(\frac{r_\perp}{r_p}\right)^2
=1.046245090518.
$$

A tensão correspondente é:

$$
\sigma_{\rm GDQ}
=F_{\rm shape}\pi\frac{\hbar c}{r_\perp^2}
=\pi\frac{\hbar c}{r_p^2}
=0.876946044304\,\mathrm{GeV/fm}.
$$

Em unidades de $\mathrm{GeV}^2$:

$$
\sigma_{\rm GDQ}
=0.173045114896\,\mathrm{GeV}^2.
$$

E:

$$
\sqrt{\sigma_{\rm GDQ}}
=0.415986916737\,\mathrm{GeV}.
$$

Comparação posterior com
$\sigma_{\rm had}\simeq0.890000\,\mathrm{GeV/fm}$:

$$
-1.466737\%.
$$

## Auditoria do raio legado comprimido

O raio antigo:

$$
r_{\rm legacy}=0.835400000000\,\mathrm{fm}
$$

não é o raio canônico derivado pela Q40. Ele representa uma compressão de
sonda/probe registrada historicamente. Se usado, produz:

$$
F_{\rm shape,legacy}
=1.059761067152,
$$

e:

$$
\sigma_{\rm legacy}
=0.888274921594\,\mathrm{GeV/fm},
$$

com desvio:

$$
-0.193829\%.
$$

## Status

O raio derivado pela cadeia Q39/Q40 é:

$$
\boxed{
r_p=0.840778765450\,\mathrm{fm}
}
$$

Esse raio não usa a tensão hadrônica como entrada. A Q30, usando esse raio,
fica com:

$$
\boxed{
F_{\rm shape}=1.046245090518
}
$$

e:

$$
\boxed{
\sigma_{\rm GDQ}
=0.876946044304\,\mathrm{GeV/fm}.
}
$$

O fechamento com $0,8354\,\mathrm{fm}$ permanece
como cenário de compressão de sonda, não como raio canônico de superfície.
