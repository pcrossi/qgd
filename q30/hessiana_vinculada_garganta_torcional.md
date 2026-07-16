# Q30 — Hessiana vinculada da garganta com carga torsional conservada

## 1. Objetivo

Calcular a rigidez produzida ao puxar um estômato sem variar
independentemente sua carga e seu módulo de torção.

Usa-se o funcional radial homogêneo já derivado e consolidado na Q35,

$$
\mathcal W_Q(R)
=\tau\left(
\frac6{R^2}-\frac{Q_T^2}{2\pi^2R^6}
\right)+3\log R.
$$

Esse é um cálculo no setor homogêneo $S^3$ da garganta. Ele não identifica o
espaço cosmológico inteiro com o bulk local $\mathbb R^4\times T^4$; usa
apenas o ciclo de ligação tridimensional do estômato e sua carga conservada.

## 2. Equilíbrio radial

A primeira variação é

$$
\mathcal W_Q'(R)
=\frac{3}{\pi^2R^7}
\left[
Q_T^2\tau+\pi^2R^6-4\pi^2\tau R^4
\right].
$$

Logo, o raio estacionário satisfaz

$$
\boxed{
R^6-4\tau R^4+\frac{\tau Q_T^2}{\pi^2}=0.
}
$$

Essa é a mesma equação de equilíbrio usada na Q35. Aqui ela é interpretada
como o balanço entre curvatura, torção conservada e medida.

## 3. Segunda variação vinculada

Antes de impor a equação de sela,

$$
\mathcal W_Q''(R)
=-\frac{3}{\pi^2R^8}
\left[
7Q_T^2\tau+\pi^2R^6-12\pi^2\tau R^4
\right].
$$

Eliminando $Q_T$ pela equação estacionária, obtém-se a identidade

$$
\boxed{
K_R:=\left.\mathcal W_Q''(R)\right|_{\rm sela}
=\frac{6(3R^2-8\tau)}{R^4}.
}
$$

Portanto, o modo radial vinculado é estritamente estável se e somente se

$$
\boxed{R^2>\frac83\tau.}
$$

Isso é mais forte que afirmar verbalmente que a conservação gera rigidez: é
o critério exato da Hessiana no módulo homogêneo.

## 4. Avaliação da solução constitutiva vigente

Na solução condicional da Q35 com $Q_T=1$ e $\alpha=1/137$,

$$
R=1.03707435228632,
\qquad
\tau=0.274900522513626.
$$

Assim,

$$
\frac{R^2}{\tau}=3.91240875912406>\frac83
$$

e

$$
\boxed{K_R=5.32888850629080>0.}
$$

Classificação numérica: avaliação direta de uma Hessiana já derivada, mas
condicional à entrada constitutiva $\alpha=1/137$. Não é previsão cega de
$\alpha$ e não usa $1/128$.

## 5. Resposta ao puxamento

Se uma sonda clássica aplica uma força generalizada $J_R$ na garganta, a
expansão estática é

$$
\delta^2\mathcal W_J
=\frac12K_R(\delta R)^2-J_R\delta R.
$$

Logo,

$$
\boxed{
\delta R=K_R^{-1}J_R,
\qquad
K_R^{-1}=0.187656393790\ldots
}
$$

nas unidades adimensionais dessa solução. A deformação induz simultaneamente

$$
\frac{\delta |H|}{|H|}
=-3\frac{\delta R}{R}
$$

porque $V_{S^3}\propto R^3$ e $Q_T$ é conservada. Assim, resposta mecânica e
resposta torsional são o mesmo modo vinculado.

## 6. Relação com o problema causal

O cálculo prova coercividade local no modo radial homogêneo sem escolher um
jato causal. A Hessiana determina rigidez e resposta estática. Ela não
determina por si só a mobilidade causal ou o tempo de relaxação.

Para uma evolução linear, ainda é necessário derivar da dinâmica GDQ um
operador de mobilidade $\mathsf M_R$. Só então se poderia escrever, por
exemplo,

$$
\mathsf M_R\,\partial_t\delta R+K_R\delta R=J_R
$$

ou sua continuação complexa. Postular $\mathsf M_R$ seria acrescentar uma
dinâmica externa.

## 7. Resultado

$$
\boxed{
\text{a conservação torsional fecha e estabiliza o modo radial homogêneo
da garganta na solução vigente.}
}
$$

Permanecem para a coercividade total:

1. modos anisotrópicos e não homogêneos da garganta;
2. blocos de curvatura, dilatão e suas misturas;
3. mobilidade causal e thimble global.
