---
title: "Medidas e integrais em espaços de caminhos"
tipo: nota
---

# Medidas e integrais em espaços de caminhos

## Ideia intuitiva

Uma integral comum soma contribuições associadas a pontos. Uma integral sobre
caminhos soma contribuições associadas a funções inteiras. Em vez de perguntar
quanto uma função vale em cada posição $x$, perguntamos quanto um funcional
$F[x]$ vale para cada trajetória possível $x(t)$.

O conjunto de todas essas trajetórias é um espaço de dimensão infinita. Por
isso, símbolos como

$$
\int F[x]\mathcal D x
$$

precisam de uma construção que explique quais caminhos são admitidos, como
eles são ponderados e em que sentido o limite existe.

## Medida positiva

Uma medida positiva atribui a cada conjunto admissível $A$ um número
$\mu(A)\geq0$. Se $\mu$ for uma medida de probabilidade,

$$
\mu(\Omega)=1,
$$

onde $\Omega$ é o espaço de todos os resultados possíveis.

A esperança de uma variável $F$ é

$$
\mathbb E[F]
=\int_{\Omega} F,d\mu.
$$

A medida de Wiener é desse tipo. Ela é construída de modo que os incrementos
do caminho browniano tenham distribuições gaussianas compatíveis em todas as
partições temporais.

## Por que a trajetória browniana não tem velocidade ordinária

Para um incremento temporal pequeno $\Delta t$, o movimento browniano possui
escala típica

$$
|\Delta x|\sim\sqrt{\Delta t}.
$$

O quociente que tentaria definir uma velocidade comporta-se como

$$
\frac{|\Delta x|}{\Delta t}
\sim\frac1{\sqrt{\Delta t}},
$$

e cresce quando $\Delta t$ tende a zero. Isso não impede a definição da
medida: mostra apenas que a notação contínua envolvendo $\dot x^2$ é uma
representação formal da construção por incrementos, não uma energia clássica
calculada caminho a caminho.

## Integral oscilatória

Na integral de Feynman, o peso é complexo:

$$
e^{iS[x]/\hbar}.
$$

Ele não define uma probabilidade positiva. O valor final depende de
cancelamentos entre fases. Uma construção possível começa por uma sequência de
integrais em tempos discretos e define o limite como integral oscilatória.
Outras construções utilizam operadores, continuação euclidiana ou métodos
espectrais.

## Aplicação no manuscrito

O problema inicial da GDQ não é demonstrar que Wiener e Feynman são a mesma
integral. É explicar como os setores difusivo e oscilatório podem pertencer a
uma dinâmica comum sem perder, respectivamente, positividade e informação de
fase.

## Erro comum

Substituir formalmente $t$ por $-i\tau$ pode transformar a aparência de uma
equação, mas não prova por si só:

- convergência da integral;
- preservação de condições de contorno;
- positividade da teoria euclidiana;
- reconstrução de uma dinâmica unitária.

Essas propriedades precisam ser verificadas no problema considerado.

[[index|← Análise e probabilidade]]

