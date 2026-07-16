# Q29 — Teste do possível vínculo Kähler sobre Berger

## 1. Garganta local de Hopf

A interface é

$$
S^3\longrightarrow S^2
$$

com forma de contato $\eta$ e métrica de Berger

$$
h_q=R^2(g_H+q^2\eta^2).
$$

Mas

$$
H^2(S^3;\mathbb R)=0.
$$

Portanto, qualquer forma de grau dois fechada sobre a interface é exata. Uma
deformação de $q$ não pode ser proibida por uma classe de Kähler intrínseca de
$S^3$, pois tal classe não existe.

O preenchimento local natural é a bola $B^4\subset\mathbb C^2$, para a qual

$$
H^2(B^4;\mathbb R)=0.
$$

Assim, também não há período local de grau dois que fixe o comprimento da
fibra de Hopf.

## 2. Compatibilidade Kähler local não fixa $q$

Num preenchimento cohomogeneidade um, escreva

$$
g_4
=dr^2+a(r)^2g_H+c(r)^2\eta^2.
$$

A condição Kähler relaciona $c(r)$ a $a'(r)$, conforme a normalização das
formas invariantes. No bordo,

$$
q=\frac{c(r_c)}{a(r_c)}
$$

é então um dado da derivada normal do preenchimento, não uma classe
cohomológica. Diferentes condições de contorno podem produzir diferentes
$q$ sem alterar qualquer classe em $H^2(B^4)$.

## 3. Espaço cosmológico

Pela fórmula de Künneth,

$$
H^2(T^5\times S^3)
\simeq H^2(T^5)
\simeq\mathbb R^{10}.
$$

Todas essas classes vêm dos ciclos toroidais. O fator $S^3$ não fornece um
ciclo de grau dois independente cuja área possa congelar o squashing de Hopf.

Além disso,

$$
b_1(T^5\times S^3)=5.
$$

Toda variedade compacta Kähler possui primeiro número de Betti par. Logo,

$$
\boxed{T^5\times S^3\text{ não admite estrutura Kähler compacta.}}
$$

Ela pode admitir uma estrutura Hermitiana não Kähler, como exige a conexão de
Bismut, mas então a forma fundamental satisfaz em geral

$$
d\omega\ne0,
$$

e $[\omega]$ não define uma classe de Kähler conservada.

## 4. Consequência

O vínculo proposto

$$
\delta_q[\omega]=0
$$

não remove o modo comum de Berger:

1. localmente, $H^2(S^3)=H^2(B^4)=0$;
2. globalmente, as classes de grau dois pertencem ao toro;
3. o background cosmológico é Hermitiano--Bismut, não Kähler estrito.

Uma restrição ainda poderia vir de uma **classe Hermitiana diferente**, como
fluxo quantizado de torção em $H^3$, holonomia ou condição de contorno causal.
Mas o fluxo de $H^3(S^3)$ já foi testado por Noether e não estabilizou o modo
comum.

## 5. Veredito

$$
\boxed{
\text{a classe de Kähler não fornece a rigidez absoluta de Berger.}
}
$$

Assim, as três propostas de `zz.md` foram testadas:

1. volume fixo: Hessiana negativa;
2. fluxo torsional/Noether: já incluído, Hessiana negativa;
3. classe de Kähler: topologicamente indisponível nesse setor.

A rota Berger, com a ação e os contornos atualmente derivados, não fecha o
transporte $3/8\to2/9$.
