# Q29 — Hessiana de Berger e transporte diferencial

## 1. Correção do teste homogêneo

O funcional já usado é

$$
\mathcal W(R,q)
=\tau\left[
\frac{2(4-q^2)}{R^2}
-\frac{n_B^2}{2\pi^2R^6q^2}
\right]
+3\log R+\log q.
$$

O teste anterior mostrou corretamente que os pontos estacionários possuem
$q=1$, mas não calculou sua estabilidade anisotrópica.

No ramo físico

$$
(R,q)=(1{,}998411184770,1),
$$

a Hessiana é

$$
H_{Rq}
=\begin{pmatrix}
1{,}49760634&0{,}99761109\\
0{,}99761109&-2{,}00636284
\end{pmatrix}.
$$

Seu espectro é

$$
\operatorname{spec}H
=\{-2{,}27048288,1{,}76172639\}.
$$

Depois de integrar a resposta radial por complemento de Schur,

$$
\boxed{
H_q^{\rm eff}
=H_{qq}-H_{qR}H_{RR}^{-1}H_{Rq}
=-2{,}67090856<0.
}
$$

Portanto, a esfera redonda não é um mínimo no setor de Berger: existe uma
instabilidade real de squashing. O funcional homogêneo isolado é runaway e
precisa da rigidez positiva de interface ou de gradientes normais para formar
um mínimo finito.

## 2. Normas corretas dos geradores

Para

$$
ds^2=R^2(\sigma_1^2+\sigma_2^2+q^2\sigma_3^2),
$$

o gerador $U(1)_Y$ alinhado com a fibra de Hopf possui norma proporcional a

$$
N_Y\propto q^2.
$$

Cada gerador espacial de $SU(2)_L$, ao ser expresso no referencial do corpo e
integrado pela medida de Haar, amostra igualmente as três direções. Portanto,

$$
N_W\propto\frac{2+q^2}{3}.
$$

Assim,

$$
\boxed{
\frac{Z_W}{Z_Y}
=\frac{2+q^2}{3q^2}.
}
$$

A fórmula $(1+q^2)/(2q^2)$ de `ideias/zz.md` não corresponde à média dos três eixos
de $SU(2)$ e, além disso, nunca alcançaria $10/21$, pois seu limite inferior
seria $1/2$.

## 3. Valor geométrico necessário

Impondo apenas como diagnóstico a condição já isolada

$$
\frac{Z_W}{Z_Y}=\frac{10}{21},
$$

obtemos

$$
21(2+q^2)=30q^2,
$$

logo

$$
\boxed{
q_*^2=\frac{14}{3},
\qquad
q_*=2{,}16024689947.
}
$$

Esse cálculo mostra que Berger possui capacidade geométrica suficiente para o
transporte. Ainda não demonstra que a ação seleciona esse valor: usá-lo no
solver antes de construir o mínimo seria engenharia inversa.

## 4. Próxima derivação

É necessário calcular a energia positiva da interface sob squashing. Escreva

$$
q=1+s
$$

e expanda a ação completa:

$$
V_{\rm eff}(s)
=\frac12H_q^{\rm eff}s^2
+\frac13c_3s^3
+\frac14c_4s^4+\cdots.
$$

O bulk fornece $H_q^{\rm eff}<0$. A interface deve fornecer $c_4>0$ e,
possivelmente, termos ímpares porque a fibra e a base não são equivalentes.
Somente a minimização dessa expressão, sem usar $10/21$ como entrada, decide
se $q_*$ coincide com $\sqrt{14/3}$.

## 5. Veredito

Berger passou no primeiro teste necessário:

$$
\boxed{
q=1\text{ é instável e }q\ne1\text{ altera diferencialmente }W/Y.
}
$$

O ponto ainda aberto é a estabilização variacional do valor de $q$.

Uma análise posterior encontrou um fold radial em
$q_{\rm crit}=1{,}88879499$, abaixo de $\sqrt{14/3}$. Logo, a interface deve
estabilizar conjuntamente $R$ e $q$; ver
`questoes/q29/associados/berger_limite_e_condicao_interface.md`.
