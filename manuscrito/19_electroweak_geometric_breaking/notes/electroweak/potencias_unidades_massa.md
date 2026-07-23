---
title: "Potências, unidades e massas quadráticas"
---

# Potências, unidades e massas quadráticas

Esta nota fixa uma regra editorial-dimensional usada no setor eletrofraco.
Ela não altera a ação oficial nem muda nenhum resultado físico. A função dela
é impedir uma ambiguidade comum quando uma escala de massa é elevada ao
quadrado.

## 1. A regra

Se $M$ é uma massa ou energia de repouso expressa em GeV, então a grandeza
quadrática correspondente é:

$$
M^2
=
\left(M\,{\rm GeV}\right)^2.
$$

Por exemplo, se a escala física é $125\,{\rm GeV}$, então:

$$
M_H^2
\simeq
\left(125\,{\rm GeV}\right)^2.
$$

O valor numérico dessa quantidade é:

$$
\left(125\,{\rm GeV}\right)^2
=
15625\,{\rm GeV}^2.
$$

Escrever apenas:

$$
125\,{\rm GeV}^2
$$

significa outra coisa: o número $125$ multiplicado pela unidade quadrática. O
valor numérico fica $125\,{\rm GeV}^2$, não $15625\,{\rm GeV}^2$.

Portanto:

$$
125\,{\rm GeV}^2
\ne
\left(125\,{\rm GeV}\right)^2.
$$

## 2. Quando $X\,{\rm GeV}^2$ é correto

Também há casos em que a notação $X\,{\rm GeV}^2$ é correta. Isso ocorre
quando $X$ já é o valor numérico de uma grandeza quadrática.

Por exemplo, se um cálculo fornece diretamente:

$$
\Delta M_H^2
\simeq
0{,}68\,{\rm MeV}^2,
$$

então a grandeza calculada já é uma massa ao quadrado. Escrever:

$$
\left(0{,}68\,{\rm MeV}\right)^2
$$

mudaria o valor físico, pois produziria:

$$
0{,}4624\,{\rm MeV}^2.
$$

## 3. Forma segura de escrita

Usaremos a seguinte convenção no manuscrito:

| Situação | Escrita correta | Significado |
|---|---|---|
| escala linear ao quadrado | $\left(125\,{\rm GeV}\right)^2$ | quadrado de uma massa de $125\,{\rm GeV}$ |
| valor quadrático já calculado | $0{,}68\,{\rm MeV}^2$ | o número $0{,}68$ já é o valor de $\Delta M^2$ |
| correção pequena de massa quadrática | $\mathcal O(10^{-6}\,{\rm GeV}^2)$ | ordem de grandeza em unidade quadrática |

Assim, uma expressão como:

$$
M_{H,\rm phys}^2
\simeq
\left(125\,{\rm GeV}\right)^2
+
\mathcal O(10^{-6}\,{\rm GeV}^2)
$$

é dimensionalmente clara: o primeiro termo é o quadrado da escala linear de
massa; o segundo já é uma correção expressa em unidade de massa ao quadrado.

## 4. Status

Esta é uma correção editorial-dimensional. Ela preserva:

1. a ação oficial da GDQ;
2. o potencial eletrofraco reduzido;
3. a interpretação do modo de Hopf;
4. as comparações numéricas de $W$, $Z$ e da escala eletrofraca;
5. qualquer cálculo em que o número já seja valor de uma grandeza quadrática.

