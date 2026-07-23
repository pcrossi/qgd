# Q29 — Teste do modo conformal na ação oficial

## 1. Hipótese do manuscrito

O manuscrito original identifica o modo de Higgs com uma respiração conformal
homogênea da métrica. Testamos essa hipótese sem introduzir um potencial de
Landau.

Considere, em dimensão real $d$,

$$
g(\sigma)=e^{2\sigma}g_0.
$$

Para preservar a medida normalizada,

$$
\mathcal U\,dV_g=e^{-f}dV_g,
$$

é necessário deslocar

$$
f(\sigma)=f_0+d\sigma
$$

no modo homogêneo.

## 2. Redução da ação

Para $\sigma$ constante,

$$
R[g(\sigma)]=e^{-2\sigma}R_0
$$

e o termo de gradiente de $f$ não muda. A parte dependente de $\sigma$ da ação
oficial é, salvo o prefator positivo comum $C$,

$$
\boxed{
V_{\rm conf}(\sigma)
=C\left[
\tau R_0e^{-2\sigma}+d\sigma
\right].
}
$$

## 3. Ponto estacionário

A equação variacional é

$$
V_{\rm conf}'
=C\left[-2\tau R_0e^{-2\sigma}+d\right]=0.
$$

Logo,

$$
e^{-2\sigma_*}=\frac{d}{2\tau R_0}.
$$

No ponto estacionário,

$$
\boxed{
V_{\rm conf}''(\sigma_*)=2Cd>0,
}
$$

$$
V_{\rm conf}'''(\sigma_*)=-4Cd,
$$

$$
\boxed{
V_{\rm conf}^{(4)}(\sigma_*)=8Cd>0.
}
$$

## 4. Consequência

O modo de respiração possui mínimo estável e quarta variação positiva, mas não
possui termo quadrático negativo no ponto estacionário:

$$
a_2=2Cd>0.
$$

Além disso, uma rescalagem conformal homogênea é singlete sob as isometrias
internas. Ela transforma como

$$
(1,1)_0,
$$

e não como

$$
(1,2)_{1/2}.
$$

Portanto,

$$
\boxed{
\text{o modo conformal homogêneo não pode ser o modo eletrofraco da Q29.}
}
$$

## 5. O modo que deve ser procurado

O candidato legítimo precisa ser uma flutuação não homogênea e carregada do
bloco Hermitiano/torsional,

$$
\Phi_{\rm EW}
=\Pi_{(1,2)_{1/2}}
(h_{\mu\bar\nu},\varphi,\bar\varphi,B),
$$

com dependência nas coordenadas internas. Sua existência exige um background
que realize explicitamente $E_W\otimes L_Y^{1/2}$ e permita calcular o
projetor $\Pi_{(1,2)_{1/2}}$.

## 6. Veredito

A ideia geral de transição geométrica permanece possível, mas a identificação
específica “Higgs = respiração conformal homogênea” é rejeitada pela variação
da ação oficial. A Q29 só pode prosseguir pelo modo misto não homogêneo.
