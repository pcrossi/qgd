# Q29 — Limite do ramo de Berger e condição da interface

Para

$$
\mathcal W(R,q)
=\frac{2(4-q^2)}{R^2}
-\frac1{2\pi^2R^6q^2}
+3\log R+\log q,
$$

o término do ramo radial é o fold

$$
\partial_R\mathcal W=0,
\qquad
\partial_R^2\mathcal W=0.
$$

Numericamente,

$$
\boxed{
R_{\rm crit}=0{,}62000249,
\qquad
q_{\rm crit}=1{,}88879499.
}
$$

O valor diagnóstico do transporte é

$$
q_{\rm tr}=\sqrt{\frac{14}{3}}=2{,}16024690.
$$

Portanto,

$$
\boxed{q_{\rm tr}>q_{\rm crit}.}
$$

O bulk homogêneo perde seu raio estacionário antes do transporte requerido.
Se $V_\partial(R,q)$ é a energia de interface, o equilíbrio correto deve
resolver simultaneamente

$$
\partial_R(\mathcal W+V_\partial)=0,
\qquad
\partial_q(\mathcal W+V_\partial)=0,
$$

com

$$
\nabla^2_{R,q}(\mathcal W+V_\partial)>0.
$$

A quártica positiva anterior descreve o gráfico radial
$r=R(1+\varepsilon Y_{\ell=1})$ e não pode ser automaticamente reutilizada
como energia de Berger. É necessário avaliar o termo de superfície sobre

$$
h_{R,q}=R^2(\sigma_1^2+\sigma_2^2+q^2\sigma_3^2),
$$

incluindo medida, curvatura extrínseca, pullback da torção, vínculo de fluxo e
segunda variação em $(R,q)$.

O resultado é um limite claro:

$$
\boxed{
\text{a interface deve estabilizar conjuntamente raio e squashing.}
}
$$
