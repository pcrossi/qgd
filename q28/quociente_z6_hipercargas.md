# Q28 — Quociente $\mathbb Z_6$ e derivação diofantina das hipercargas

## 1. Normalização inteira

Defina

$$
y=6Y.
$$

O grupo global candidato é

$$
G
=
\frac{SU(3)\times SU(2)\times U(1)_y}{\mathbb Z_6}.
$$

Escolha como gerador do subgrupo identificado

$$
z_6
=
\left(
e^{2\pi i/3}I_3,
-I_2,
e^{i\pi/3}
\right).
$$

Se $t\in\{0,1,-1\}$ é a trialidade de cor e $p\in\{0,1\}$ é a paridade de
isospin, a representação desce ao quociente se

$$
\boxed{
2t+3p+y\equiv0\pmod6.
}
$$

## 2. Congruências dos cinco multipletos

Para os espaços internos já estruturados, obtemos:

$$
q\equiv1\pmod6
$$

para $(3,2)$;

$$
u\equiv d\equiv2\pmod6
$$

para $(\bar3,1)$;

$$
\ell\equiv3\pmod6
$$

para $(1,2)$; e

$$
e\equiv0\pmod6
$$

para $(1,1)$.

O quociente sozinho fixa apenas classes módulo seis. Em particular, ele não
distingue $2$ de $-4$.

## 3. Equações de anomalia

Para uma geração de campos de Weyl esquerdos, imponha:

$$
2q+u+d=0
$$

de $[SU(3)]^2U(1)$,

$$
3q+\ell=0
$$

de $[SU(2)]^2U(1)$,

$$
6q+3u+3d+2\ell+e=0
$$

da anomalia gravitacional, e

$$
6q^3+3u^3+3d^3+2\ell^3+e^3=0
$$

da anomalia cúbica.

Das três primeiras equações:

$$
\ell=-3q,
$$

$$
u+d=-2q,
$$

$$
e=6q.
$$

Substituindo na equação cúbica:

$$
ud=-8q^2.
$$

Assim, $u$ e $d$ são raízes de

$$
x^2+2qx-8q^2=0,
$$

logo

$$
\{u,d\}=\{2q,-4q\}.
$$

## 4. Solução primitiva

A condição de representação primitiva escolhe

$$
\gcd(|q|,|u|,|d|,|\ell|,|e|)=1.
$$

Com $q\equiv1\pmod6$, a orientação mínima é

$$
q=1.
$$

Portanto,

$$
\boxed{
(q,u,d,\ell,e)
=
(1,-4,2,-3,6)
}
$$

até a troca $u\leftrightarrow d$ e conjugação simultânea da orientação.

Dividindo por seis:

$$
\boxed{
Y_Q=\frac16,
\quad
Y_{u^c}=-\frac23,
\quad
Y_{d^c}=\frac13,
\quad
Y_L=-\frac12,
\quad
Y_{e^c}=1.
}
$$

## 5. Significado lógico

As hipercargas não foram inseridas individualmente. Elas resultam da
combinação:

$$
\boxed{
\text{representações }(3,2),(\bar3,1),(1,2),(1,1)
+\mathbb Z_6
+\text{anomalias}
+\text{primitividade}.
}
$$

O cálculo ainda pressupõe que a geometria já selecionou exatamente esses
cinco tipos de representação. Ele deriva seus pesos abelianos, não a lista de
representações a partir do vazio.

## 6. Status

$$
\boxed{
\text{quociente global e hipercargas fechados como problema diofantino
condicional às representações internas.}
}
$$
