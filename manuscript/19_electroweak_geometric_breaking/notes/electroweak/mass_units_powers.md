---
title: "Powers, units, and quadratic masses"
---

# Powers, units, and quadratic masses

This note establishes an editorial-dimensional rule used in the electroweak sector. It does not alter the official action nor does it change any physical result. Its function is to prevent a common ambiguity when a mass scale is squared.

## 1. The rule

If $M$ is a mass or rest energy expressed in GeV, then the corresponding quadratic quantity is:

$$
M^2
=
\left(M\,{\rm GeV}\right)^2.
$$

For example, if the physical scale is $125\,{\rm GeV}$, then:

$$
M_H^2
\simeq
\left(125\,{\rm GeV}\right)^2.
$$

The numerical value of this quantity is:

$$
\left(125\,{\rm GeV}\right)^2
=
15625\,{\rm GeV}^2.
$$

Writing just:

$$
125\,{\rm GeV}^2
$$

means something else: the number $125$ multiplied by the quadratic unit. The numerical value becomes $125\,{\rm GeV}^2$, not $15625\,{\rm GeV}^2$.

Therefore:

$$
125\,{\rm GeV}^2
\ne
\left(125\,{\rm GeV}\right)^2.
$$

## 2. When $X\,{\rm GeV}^2$ is correct

There are also cases where the notation $X\,{\rm GeV}^2$ is correct. This occurs when $X$ is already the numerical value of a quadratic quantity.

For example, if a calculation directly yields:

$$
\Delta M_H^2
\simeq
0{,}68\,{\rm MeV}^2,
$$

then the calculated quantity is already a mass squared. Writing:

$$
\left(0{,}68\,{\rm MeV}\right)^2
$$

would change the physical value, because it would produce:

$$
0{,}4624\,{\rm MeV}^2.
$$

## 3. Safe writing format

We will use the following convention in the manuscript:

| Situation | Correct writing | Meaning |
|---|---|---|
| linear scale squared | $\left(125\,{\rm GeV}\right)^2$ | square of a $125\,{\rm GeV}$ mass |
| already calculated quadratic value | $0{,}68\,{\rm MeV}^2$ | the number $0{,}68$ is already the value of $\Delta M^2$ |
| small quadratic mass correction | $\mathcal O(10^{-6}\,{\rm GeV}^2)$ | order of magnitude in quadratic units |

Thus, an expression like:

$$
M_{H,\rm phys}^2
\simeq
\left(125\,{\rm GeV}\right)^2
+
\mathcal O(10^{-6}\,{\rm GeV}^2)
$$

is dimensionally clear: the first term is the square of the linear mass scale; the second is already a correction expressed in units of mass squared.

## 4. Status

This is an editorial-dimensional correction. It preserves:

1. the official GDQ action;
2. the reduced electroweak potential;
3. the interpretation of the Hopf mode;
4. the numerical comparisons of $W$, $Z$, and the electroweak scale;
5. any calculation in which the number is already the value of a quadratic quantity.
