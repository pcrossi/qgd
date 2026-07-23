# Q34 — Coeficientes locais $U(1)$ do heat kernel

## 1. Objeto e convenção

A polarização escalar já derivada é

$$
\Pi_\eta(r)
=
\frac{2\alpha_0}{\pi}
\int_0^1dx\,u
\left[
E_1(\eta)-E_1\!\left(\eta(1+ur)\right)
\right],
$$

onde

$$
u=x(1-x),
\qquad
r=\frac{q_E^2}{m^2},
\qquad
\eta=\tau m^2.
$$

A expressão é subtraída no infravermelho:

$$
\Pi_\eta(0)=0.
$$

Portanto, o coeficiente local de $F_{\mu\nu}F^{\mu\nu}$ nessa convenção é
fixado pela carga medida e não deve ser contado novamente como uma previsão:

$$
\boxed{c_F^{\rm IR}=0.}
$$

Isso não significa ausência do termo de Maxwell. Significa que sua
normalização está na definição operacional de $\alpha_0$.

## 2. Expansão local

Defina

$$
g_\eta(y)
=
E_1(\eta)-E_1(\eta(1+y)).
$$

Sua derivada exata é

$$
g_\eta'(y)
=
\frac{e^{-\eta(1+y)}}{1+y}.
$$

Logo,

$$
g_\eta(y)
=
e^{-\eta}
\left[
y-\frac{1+\eta}{2}y^2
+\frac{2+2\eta+\eta^2}{6}y^3
+O(y^4)
\right].
$$

Usando

$$
\int_0^1[x(1-x)]^pdx
=
\frac{(p!)^2}{(2p+1)!},
$$

obtemos

$$
\boxed{
\Pi_\eta(r)
=
A_1r+A_2r^2+A_3r^3+O(r^4)
}
$$

com

$$
\boxed{
A_1
=
\frac{\alpha_0e^{-\eta}}{15\pi},
}
$$

$$
\boxed{
A_2
=
-\frac{\alpha_0e^{-\eta}(1+\eta)}{140\pi},
}
$$

$$
\boxed{
A_3
=
\frac{\alpha_0e^{-\eta}(2+2\eta+\eta^2)}{1890\pi}.
}
$$

Os coeficientes são finitos para todo $\eta>0$.

## 3. Ação local

Na convenção quadrática

$$
\Gamma_\eta^{(2)}
=
\frac14
\int
F_{\mu\nu}
\Pi_\eta\!\left(\frac{-\Delta}{m^2}\right)
F^{\mu\nu}\,d^4x,
$$

a primeira correção local é

$$
\Gamma_{\eta,{\rm loc}}^{(2)}
\supset
c_{DF}(\eta)
\int
\partial_\rho F_{\mu\nu}
\partial^\rho F^{\mu\nu}\,d^4x,
$$

onde

$$
\boxed{
c_{DF}(\eta)
=
\frac{A_1}{4m^2}
=
\frac{\alpha_0e^{-\eta}}{60\pi m^2}.
}
$$

O próximo coeficiente, na base
$F(-\Delta)^2F$, é

$$
\boxed{
c_{D^2F}(\eta)
=
\frac{A_2}{4m^4}
=
-\frac{\alpha_0e^{-\eta}(1+\eta)}
{560\pi m^4}.
}
$$

Integrações por partes ou mudanças de base de operadores podem alterar a
aparência dos sinais. Os coeficientes invariantes desta auditoria são os
$A_n$ da polarização escalar euclidiana.

## 4. Ward e ausência de massa

Todos os termos aparecem dentro de

$$
F_{\mu\nu}\,\mathcal F(-\Delta)\,F^{\mu\nu}.
$$

Assim, a expansão não produz

$$
m_\gamma^2A_\mu A^\mu.
$$

A transversalidade permanece exata ordem a ordem:

$$
q^\mu\Pi_{\mu\nu}=0.
$$

## 5. Avaliação na ponte torsão--Reynolds

Com

$$
\alpha_0=\frac1{137},
\qquad
\eta=\tau_{\rm EM}^{\rm dimless}=0{,}2749005225,
$$

os coeficientes adimensionais da série podem ser avaliados diretamente. Essa
substituição testa a ponte constitutiva; não fixa a unidade $m$ nem transforma
os coeficientes dimensionais em previsão absoluta.

## 6. Status

No setor $U(1)$:

1. $c_F^{\rm IR}$ foi fixado pela condição de subtração;
2. $c_{DF}$ e os dois coeficientes seguintes foram calculados;
3. a ausência de massa fotônica e Ward permanecem manifestas;
4. a série foi verificada numericamente em
   numerico/q34_q35_u1/verificar_coeficientes_locais_u1.py.

Permanecem para a Q34:

1. coeficientes do operador não abeliano completo;
2. jacobiano em fundos topológicos;
3. comparação entre classes admissíveis de kernel.

## 7. Referência

D. V. Vassilevich, “Heat kernel expansion: user's manual”,
*Physics Reports* **388** (2003) 279--360,
DOI: 10.1016/j.physrep.2003.09.002,
arXiv:hep-th/0306138. A referência sustenta a expansão por coeficientes locais
de operadores de tipo Laplace; os coeficientes $U(1)$ deste documento foram
extraídos diretamente da polarização já derivada na GDQ.
