# Q29 — Quártica positiva da interface do estômato

## 1. Deformação da borda

Represente a interface por um gráfico radial sobre $S^3$:

$$
r(Y)=R(1+\varepsilon Y),
$$

onde $Y=Y_{\ell=1}$ e

$$
\langle Y^2\rangle=\frac14,
\qquad
\langle Y^4\rangle=\frac18.
$$

O elemento de área relativo é

$$
\frac{dA_\varepsilon}{dA_0}
=(1+\varepsilon Y)^3
\sqrt{
1+\frac{\varepsilon^2(1-Y^2)}{(1+\varepsilon Y)^2}
}.
$$

Sua média fornece

$$
\frac{A_\varepsilon}{A_0}
=1+\frac98\varepsilon^2-\frac5{64}\varepsilon^4+O(\varepsilon^6).
$$

## 2. Vínculo de volume

O volume relativo é

$$
\frac{V_\varepsilon}{V_0}
=1+\frac32\varepsilon^2+\frac18\varepsilon^4+O(\varepsilon^6).
$$

Impondo volume conservado por um multiplicador, a escala comum é corrigida por
$V_\varepsilon^{-1/4}$. Como a área escala com a terceira potência,

$$
\left.
\frac{A_\varepsilon}{A_0}
\right|_{V=V_0}
=\frac{A_\varepsilon}{A_0}
\left(\frac{V_\varepsilon}{V_0}\right)^{-3/4}.
$$

Expandindo,

$$
\boxed{
\left.
\frac{A_\varepsilon}{A_0}
\right|_{V=V_0}
=1+\frac5{128}\varepsilon^4+O(\varepsilon^6).
}
$$

O termo quadrático cancela e a primeira penalidade física é quartica e
positiva.

## 3. Rigidez superficial já derivada

A Q40 fornece o termo torsional de superfície dos três estômatos:

$$
\mathcal S_\partial
=\alpha\left(
\frac{3\pi}{2}+\frac{3}{4\pi^3}
\right).
$$

Defina

$$
S_\partial
=\alpha\left(
\frac{3\pi}{2}+\frac{3}{4\pi^3}
\right)
=0{,}03456447695.
$$

A amplitude geométrica relativa é

$$
\varepsilon=\frac\beta{b_0},
\qquad
b_0=\frac1{\pi R^3}.
$$

Logo,

$$
V_\partial(\beta)
=S_\partial\frac5{128}
\left(\frac\beta{b_0}\right)^4.
$$

Na convenção $V\supset a_4\beta^4/4$,

$$
\boxed{
a_4^{\partial}
=\frac{5S_\partial}{32b_0^4}.
}
$$

## 4. Avaliação

Para

$$
R=1{,}998411184770,
\qquad
b_0=0{,}03988371206,
$$

obtemos

$$
\boxed{
a_4^{\partial}=2134{,}360262.
}
$$

Somando a retroação de bulk,

$$
a_4^{\rm bulk}=-0{,}805755288,
$$

segue

$$
\boxed{
a_4^{\rm total}=2133{,}554507>0.
}
$$

Portanto, a interface estabiliza amplamente o modo eletrofraco.

## 5. Mínimo

Com

$$
a_2=-0{,}253196676,
$$

o mínimo quartico ocorre em

$$
\boxed{
\beta_*=\sqrt{-\frac{a_2}{a_4^{\rm total}}}
=0{,}0108937431.
}
$$

A deformação relativa é

$$
\boxed{
\varepsilon_*=\frac{\beta_*}{b_0}
=0{,}273137642.
}
$$

## 6. Escala física

Usando a calibração dimensional bariônica e o volume de Kähler já derivados,

$$
v
=m_p\frac{6\pi^5}{7}
=246{,}111196\,\mathrm{GeV}.
$$

Isso fixa a normalização cinética do modo por

$$
\sqrt{Z_\beta}
=\frac{v}{\beta_*}
=22591{,}98\,\mathrm{GeV}.
$$

O valor de $v$ continua sendo uma calibração geométrica pela escala bariônica;
a igualdade dessa normalização com o coeficiente cinético obtido diretamente
da redução 8D ainda deve ser verificada. A estabilização e o valor adimensional
$\beta_*$, porém, não usam $v$ como alvo.

## 7. Resultado

A combinação correta é

$$
\boxed{
\text{torção de bulk: }a_2<0,
\qquad
\text{interface a volume fixo: }a_4>0.
}
$$

Assim, a GDQ produz o potencial de quebra estabilizado sem inserir uma
quártica de Higgs independente.
