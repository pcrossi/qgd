# Q29 — Normalização de Bismut e fonte dilatônica correta

## 1. Normalização já fixada pela GDQ

As convenções usadas anteriormente na Q29 são

$$
\frac1{2\pi}\int_{S^3}B=n_B\in\mathbb Z.
$$

Logo, para a $3$-forma empregada pelo manuscrito,

$$
\boxed{\mathcal N_B=2\pi.}
$$

Para o fluxo homogêneo

$$
B=b\,\operatorname{vol}_{S^3(R)},
$$

segue

$$
b=\frac{n_B}{\pi R^3},
\qquad
|B|^2=6b^2
=\frac{6n_B^2}{\pi^2R^6}.
$$

Esse resultado já havia produzido o ramo radial estável
$R=1{,}998411184\ldots$; portanto não há liberdade para escolher outra
normalização apenas para ajustar o acoplamento eletromagnético.

## 2. Como $B$ aparece na ação oficial estendida

O setor Perelman--Bismut é

$$
\mathcal S_B
=
-\frac{\tau}{12}
\int |B|^2d\mu_f,
$$

com medida normalizada

$$
d\mu_f
=
\frac{e^{-f}dV}{\int e^{-f}dV}.
$$

Sob


$$
f\longmapsto f+t\varphi,
$$

temos

$$
\delta d\mu_f
=
-(\varphi-\langle\varphi\rangle_f)d\mu_f.
$$

Assim,

$$
\delta_f\mathcal S_B[\varphi]
=
\frac{\tau}{12}
\int
\left(
|B|^2-\langle|B|^2\rangle_f
\right)
\varphi\,d\mu_f.
$$

A fonte dilatônica correta é, portanto,

$$
\boxed{
J_f^{(B)}
=
\frac{\tau}{12}
\left(
|B|^2-\langle|B|^2\rangle_f
\right).
}
$$

Ela possui média zero automaticamente, como exige a normalização.

## 3. Consequência para o fluxo homogêneo

Se

$$
B=b\,\operatorname{vol}_{S^3}
$$

e o raio é homogêneo, então $|B|^2$ é constante. Logo,

$$
J_f^{(B)}=0.
$$

O fluxo primitivo homogêneo estabiliza o raio, mas não cria um perfil
dilatônico localizado nem veste a norma eletromagnética pela covariância
radial.

Esse resultado explica por que não é lícito identificar

$$
\int_{S^3}B=2\pi
$$

com uma condição linear

$$
pF'(\epsilon)=-2\pi.
$$

São objetos variacionais diferentes: o primeiro fixa uma classe de
cohomologia de grau três; o segundo seria uma carga escalar de bordo.

## 4. Fonte localizada de estômato

Uma fonte dilatônica não homogênea surge somente se a densidade torsional
$|B|^2$ for não homogênea. Escreva

$$
B
=
\frac{2\pi n_B}{\int_{S^3}h\,dV}
h(y)\,\operatorname{vol}_{S^3},
$$

onde $h$ é o perfil torsional determinado pela cola e

$$
\int_{S^3}B=2\pi n_B.
$$

Então

$$
|B|^2
=
6
\left(
\frac{2\pi n_B}{\int h\,dV}
\right)^2h^2(y),
$$

e

$$
J_f^{(B)}(y)
=
\frac{\tau}{2}
\left(
\frac{2\pi n_B}{\int h\,dV}
\right)^2
\left(
h^2(y)-\langle h^2\rangle_f
\right).
$$

Portanto, a classe topológica fixa a integral de $B$, mas a amplitude da
fonte escalar depende também do perfil físico $h$. Isso não é uma nova
constante livre: $h$ deve ser a solução do operador torsional da cola, com as
condições Robin/regularidade já formuladas na Q40.

## 5. Correção da tentativa de fluxo escalar

O cálculo em `solve_background_fluxo_topologico_q29.py` é matematicamente
válido como família de backgrounds com carga escalar de bordo. Contudo, ele
não representa ainda a redução da torção de Bismut, porque impôs diretamente
$pF'=-k$.

Seus resultados não devem ser usados para prever $\alpha$ até que essa carga
escalar seja demonstrada por um termo de contorno explícito. Em particular,
o valor

$$
K_Q(1)/K_Q(0)=0{,}993668694
$$

é um diagnóstico do modelo de fonte escalar, não a consequência do winding
torsional $n_B=1$.

## 6. Próximo cálculo fechado

O próximo problema não contém uma normalização desconhecida. Deve-se:

1. tomar o perfil torsional variacional $h$ da cola;
2. normalizá-lo por $\int B=2\pi$;
3. construir $J_f^{(B)}$ pela fórmula quadrática acima;
4. resolver o sistema acoplado warped--dilatônico com essa fonte distribuída;
5. avaliar $K_Q$ no novo background.

Essa é a primeira rota em que topologia, ação oficial e dressing
eletromagnético aparecem na mesma cadeia variacional sem identificação
constitutiva adicional.
