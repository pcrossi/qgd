# Q29 — Vínculo de Noether na Hessiana de Berger

## 1. Formulação não reduzida

Introduza a densidade torsional homogênea $T$ como variável independente. O
fluxo conservado é

$$
\Phi_N=R^3qT=\frac1\pi.
$$

O funcional com multiplicador é

$$
\mathcal L_N
=\frac{2(4-q^2)}{R^2}
+3\log R+\log q
-\frac12T^2
+\lambda_N\left(R^3qT-\frac1\pi\right).
$$

A equação de $T$ fornece

$$
T=\frac1{\pi R^3q},
$$

e recupera exatamente

$$
-\frac12T^2
=-\frac1{2\pi^2R^6q^2}.
$$

## 2. Espaço tangente físico

As variações permitidas satisfazem

$$
D\Phi_N(\delta R,\delta q,\delta T)=0,
$$

isto é,

$$
\delta T
=-\frac{3T}{R}\delta R
-\frac{T}{q}\delta q.
$$

Uma base matricial de $\ker D\Phi_N$ é

$$
P_N
=\begin{pmatrix}
1&0\\
0&1\\
-3T/R&-T/q
\end{pmatrix}.
$$

A Hessiana física é

$$
H_N^{\rm phys}
=P_N^T\nabla^2_{R,q,T}\mathcal L_NP_N.
$$

## 3. Identidade exata

O cálculo simbólico fornece

$$
\boxed{
H_N^{\rm phys}
=\nabla^2_{R,q}
\left[
\frac{2(4-q^2)}{R^2}
-\frac1{2\pi^2R^6q^2}
+3\log R+\log q
\right].
}
$$

A diferença entre as duas matrizes é identicamente zero, não apenas no ponto
estacionário.

No ramo grande,

$$
H_N^{\rm phys}
=\begin{pmatrix}
1{,}49760634&0{,}99761109\\
0{,}99761109&-2{,}00636284
\end{pmatrix},
$$

com autovalor negativo $-2{,}27048288$.

## 4. Interpretação

O vínculo de Noether não foi omitido no teste anterior: ele já estava
incorporado pela dependência $R^{-6}q^{-2}$ do fluxo fixo. Manter $T$ constante
durante o squashing violaria a conservação e poderia produzir uma rigidez
espúria.

Isso não exclui contribuições adicionais dos modos **relativos** dos três
estômatos. Porém, no modo homogêneo comum de Berger, a conservação do fluxo não
remove a instabilidade.

Esses modos foram posteriormente decompostos pelo Laplaciano de $C_3$. Eles
podem estabilizar as duas diferenças entre gargantas, mas anulam-se exatamente
no modo comum; ver `questoes/q29/associados/berger_tres_estomatos_modos_relativos.md`.

## 5. Veredito

$$
\boxed{
\text{Noether está incluído, mas não estabiliza o modo comum de Berger.}
}
$$
