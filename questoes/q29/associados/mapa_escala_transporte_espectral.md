# Q29 — Mapa dimensional do transporte espectral

## 1. Convenção da Q32

A Q32 estabeleceu

$$
e^{-\tau L_{\rm GDQ}^{(2)}}
\longrightarrow e^{-\tau p_E^2},
\qquad
\Lambda(\tau)=\tau^{-1/2}.
$$

Assim, o parâmetro de calor físico tem dimensão de comprimento ao quadrado ou
energia inversa ao quadrado.

## 2. Adimensionalização do solver

O operador radial da Q29 foi resolvido em coordenadas internas adimensionais.
Se

$$
\ell_0=\Lambda_0^{-1}
$$

é o comprimento usado para adimensionalizar a métrica, então

$$
\lambda_n^{\rm físico}
=\Lambda_0^2\lambda_n^{\rm dimless}.
$$

A igualdade dos expoentes exige

$$
\tau_{\rm físico}\lambda_n^{\rm físico}
=s\lambda_n^{\rm dimless},
$$

logo

$$
s=\tau_{\rm físico}\Lambda_0^2.
$$

Portanto,

$$
\boxed{
Q(s)=\frac1{\sqrt{\tau_{\rm físico}}}
=\frac{\Lambda_0}{\sqrt s}.
}
$$

Use-se $s$ para o parâmetro adimensional do semigrupo, evitando confundi-lo
com o parâmetro de fluxo que também determina o background.

## 3. Escala do cruzamento

Para

$$
s_*=5{,}9090386\times10^6,
$$

obtemos

$$
\sqrt{s_*}=2430{,}8514146
$$

e

$$
\boxed{
\frac{Q_*}{\Lambda_0}
=4{,}113784964\times10^{-4}.
}
$$

Se a normalização interna for a escala de Cartan,

$$
\Lambda_0=\Lambda_C,
$$

então

$$
\boxed{Q_*=4{,}113784964\times10^{-4}\Lambda_C.}
$$

Essa é uma previsão de razão adimensional. A Q36 registra que o valor absoluto
universal de $\Lambda_C$ ainda não foi derivado; portanto, a energia em GeV não
pode ser anunciada sem uma calibração adicional.

## 4. Teste de consistência de escala

Se, apenas como teste, fosse usada a escala $v=246{,}111196$ GeV como
$\Lambda_0$, resultaria

$$
Q_*=0{,}101245\ {\rm GeV},
$$

que não é uma escala eletrofraca. Isso mostra que $v$ não pode ser identificado
automaticamente com a escala do operador interno. A escala espectral $\Lambda_0$
deve ser derivada da normalização da Hessiana, não escolhida pelo resultado.

## 5. Background fixo versus fluxo completo

O cálculo realizado usa

$$
e^{-sL_*}
$$

com $L_*$ avaliado no background estacionário obtido para o parâmetro interno
normalizado. No fluxo completo, o operador pode depender da resolução:

$$
L=L(s).
$$

Então o propagador correto é ordenado:

$$
\mathcal K(s)
=\mathcal P
\exp\left[-\int_0^sL(u)du\right].
$$

Portanto, o cruzamento calculado é exato para o semigrupo do background fixo.
Para tratá-lo como evolução física completa da GDQ, ainda é preciso verificar
adiabaticidade,

$$
\frac{\|\partial_sL\|}{\operatorname{gap}(L)^2}\ll1,
$$

ou recomputar a família de backgrounds.

## 6. Status

$$
\boxed{
\frac{Q_*}{\Lambda_0}=4{,}113784964\times10^{-4}
}
$$

está derivado no modelo espectral fixo. Permanecem:

1. determinar $\Lambda_0$ pela normalização da Hessiana/Q36;
2. provar que $\Lambda_0=\Lambda_C$ ou obter a relação correta;
3. verificar o transporte com background dependente da escala.

Uma calibração interna posterior, usando separadamente as identidades
$m_W^2=\Lambda_0^2\lambda_W$ e $m_Z^2=\Lambda_0^2\lambda_Z$ no ponto de
correspondência, forneceu $\Lambda_0\simeq126{,}354$ TeV com desacordo relativo
$6{,}44\times10^{-6}$. Ver `questoes/q29/associados/calibracao_interna_escala_espectral.md`.
