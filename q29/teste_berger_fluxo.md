# Q29 — Teste do squashing homogêneo de Berger

## 1. Ansatz

Considere

$$
ds^2
=R^2(\sigma_1^2+\sigma_2^2+q^2\sigma_3^2),
$$

onde $q=1$ é a esfera redonda. Na convenção em que
$R[S^3_{q=1}]=6/R^2$, o escalar de Berger é

$$
R_B(R,q)=\frac{2(4-q^2)}{R^2}.
$$

O volume é proporcional a $R^3q$. Com fluxo inteiro fixo, a densidade
torsional escala como $R^{-6}q^{-2}$. O funcional normalizado é

$$
\mathcal W(R,q)
=\tau\left[
\frac{2(4-q^2)}{R^2}
-\frac{n_B^2}{2\pi^2R^6q^2}
\right]
+3\log R+\log q.
$$

## 2. Resultado estacionário

Para $n_B=1$ e $\tau=1$, a solução numérica conjunta encontra os dois ramos
radiais já conhecidos, mas em ambos

$$
\boxed{q_*=1.}
$$

Os valores são

$$
(R_-,q_-)=(0{,}403099881,1),
$$

$$
(R_+,q_+)=(1{,}998411185,1).
$$

## 2.1 Correção posterior de estabilidade

O fato de $q=1$ ser estacionário não significa que seja estável. A Hessiana
completa foi posteriormente calculada e possui um autovalor negativo. Após o
complemento de Schur radial,

$$
H_q^{\rm eff}=-2{,}67090856<0.
$$

Logo, a solução redonda é um saddle com instabilidade de squashing; o
funcional homogêneo não seleciona sozinho um valor anisotrópico finito. Ver
`q29/berger_hessiana_e_transporte.md`.

## 3. Conclusão

O fluxo torsional homogêneo não seleciona um squashing **estável e finito**:

$$
\boxed{
\text{o extremo homogêneo permanece isotrópico.}
}
$$

Portanto, a quebra eletrofraca não pode ser atribuída apenas ao raio nem ao
parâmetro homogêneo de Berger. Ela exige o harmônico carregado não homogêneo
$\ell=1$ construído em `q29/modo_hopf_carregado.md` e sua retroação completa.
