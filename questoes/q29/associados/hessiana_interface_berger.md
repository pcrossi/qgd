# Q29 — Hessiana de interface no modo Berger

## 1. Termo de bordo disponível

A completação variacional já usada nas Q29/Q42 é

$$
\mathcal S_{\partial}^{\rm GDQ}
=
2\tau
\int_{\partial M}
\mathcal U K,dA,
$$

onde $K$ é a curvatura média da interface no bulk.

Na garganta cilíndrica de Hopf adotada na Q42, existe um colar com métrica

$$
ds^2
=
dr^2+g_q,
$$

e

$$
g_q
=
R^2
\left(
\sigma_1^2+\sigma_2^2+q^2\sigma_3^2
\right),
$$

independente de $r$ no background estacionário.

## 2. Segunda forma fundamental

Para uma folheação $r=\text{constante}$,

$$
K_{ij}
=
\frac12\partial_rg_{ij}.
$$

Como $\partial_rg_q=0$ no colar produto,

$$
K_{ij}=0,
\qquad
K=0
$$

para todo $q$. Consequentemente,

$$
\mathcal S_\partial^{\rm GDQ}(q)=0
$$

e

$$
\boxed{
H_q^\partial
=
\frac{d^2\mathcal S_\partial^{\rm GDQ}}{dq^2}
=0.
}
$$

Esse resultado coincide com a avaliação on-shell anterior do cilindro de
Hopf, que encontrou $K=0$.

## 3. Vínculo de volume

O volume de Berger é

$$
V(R,q)=2\pi^2R^3q
$$

na convenção usada. Sob volume fixo,

$$
R(q)=R_0q^{-1/3}.
$$

Impor esse vínculo elimina a variação volumétrica, mas não gera energia:

$$
V(R(q),q)=2\pi^2R_0^3.
$$

Logo, uma tensão de superfície proporcional apenas a $V(S^3_q)$ também possui
Hessiana nula ao longo da direção vinculada.

## 4. Fluxo torsional

Para

$$
\int_{S^3}B=2\pi n_B
$$

e

$$
B=b(q)\operatorname{vol}_{g_q},
$$

temos

$$
b(q)=\frac{2\pi n_B}{V(R,q)}.
$$

No vínculo de volume, $b(q)$ e $|B|^2=6b^2$ são constantes. Portanto, o termo

$$
-\frac\tau{12}\int|B|^2d\mu
$$

também não acrescenta Hessiana de squashing nessa direção.

## 5. Resultado total disponível

O bulk fornece

$$
H_q^{\rm bulk,eff}
=-2{,}67090856,
$$

enquanto o termo oficial de bordo no colar produto fornece

$$
H_q^\partial=0.
$$

Assim,

$$
\boxed{
H_q^{\rm total}
=-2{,}67090856<0.
}
$$

## 6. O que seria necessário para obter rigidez positiva

Uma contribuição não nula exigiria ao menos uma destas estruturas:

1. colar não produto, com $\partial_rg_q\ne0$;
2. energia de cisalhamento extrínseca, por exemplo $K_{ij}^{\rm TF}K^{ij}_{\rm TF}$;
3. termo de contorno torsional dependente da métrica, além da transgressão
   topológica constante;
4. solução global que determine o embedding da interface e, portanto,
   $K_{ij}(q)$.

Nenhuma dessas dependências está especificada na ação de contorno atualmente
utilizada. Escolher uma função $K(q)$ para superar $2{,}67090856$ seria uma
adição constitutiva e não uma derivação.

## 7. Veredito

$$
\boxed{
\text{na geometria oficial de colar cilíndrico, }H_q^\partial=0.
}
$$

Portanto, a tentativa de estabilizar Berger pela interface existente falha de
forma definida. A rota anisotrópica para corrigir $\alpha$ não pode prosseguir
sem primeiro derivar um colar não produto da solução global da GDQ ou ampliar
explicitamente o funcional de bordo.
