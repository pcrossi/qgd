# Q29 — Estabilização pelo fluxo torsional quantizado em $S^3$

## 1. Vínculo topológico

Como

$$
H^3(S^3,\mathbb Z)=\mathbb Z,
$$

impomos

$$
\frac1{2\pi}\int_{S^3}B=n_B\in\mathbb Z.
$$

Para

$$
B=b\,\operatorname{vol}_{S^3(R)},
$$

e $\operatorname{Vol}(S^3(R))=2\pi^2R^3$,

$$
b=\frac{n_B}{\pi R^3}.
$$

Com a convenção $|B|^2=6b^2$,

$$
\frac1{12}|B|^2
=\frac{n_B^2}{2\pi^2R^6}.
$$

## 2. Funcional radial normalizado

Para $R[S^3]=6/R^2$ e medida uniforme normalizada, o deslocamento constante de
$f$ contribui com $\log\operatorname{Vol}\sim3\log R$. Desprezando constantes
independentes de $R$,

$$
\boxed{
\mathcal W_n(R)
=\tau\left(
\frac6{R^2}
-\frac{n_B^2}{2\pi^2R^6}
\right)
+3\log R.
}
$$

## 3. Equação estacionária

Com $x=R^2$, a condição $\mathcal W_n'(R)=0$ torna-se

$$
\boxed{
x^3-4\tau x^2+\frac{\tau n_B^2}{\pi^2}=0.
}
$$

Para $\tau=1$ e fluxo primitivo $n_B=1$, existem dois extremos positivos:

$$
R_-=0{,}403099876,
$$

$$
R_+=1{,}998411184.
$$

As segundas derivadas são

$$
\mathcal W''(R_-)=-1707{,}21<0,
$$

$$
\boxed{
\mathcal W''(R_+)=1{,}497606>0.
}
$$

Logo, o fluxo quantizado produz um ramo radial estável próximo ao raio
gaussiano $2\sqrt\tau$.

### Correção posterior do significado de estabilidade

A primeira variação satisfaz
$\delta\mathcal W_T=-\tau\langle E_T,\delta g\rangle$, enquanto o fluxo do
Capítulo 17 é $\partial_\tau g=-2E_T=(2/\tau)\operatorname{grad}\mathcal W_T$.
Ele sobe $\mathcal W_T$. Portanto, o ramo com $\mathcal W''(R_+)>0$ é mínimo
coercivo do funcional estático, mas repulsor do fluxo ascendente. A expressão
“ramo radial estável” acima vale apenas para uma dinâmica de descida da ação,
não para o fluxo entrópico documentado. Fonte:
`questoes/q30/associados/auditoria_sinal_fluxo_perelman_bismut.md`.

## 4. O que foi resolvido

O vínculo topológico fornece elasticidade finita para a magnitude torsional:

$$
\boxed{
\text{a direção radial do fluxo primitivo possui um mínimo estável.}
}
$$

Isso substitui a quártica arbitrária do script antigo por um funcional
geométrico não polinomial cuja expansão no mínimo possui coeficientes
determinados.

## 5. O que ainda não é quebra eletrofraca

O fluxo homogêneo $B\propto\operatorname{vol}_{S^3}$ é isotrópico. Ele
estabiliza o raio, mas não escolhe sozinho a direção

$$
SU(2)_L\times U(1)_Y\to U(1)_{\rm EM}.
$$

Para isso é necessário o modo não homogêneo

$$
\Xi_{\rm EW}\in E_W\otimes L_Y^{1/2}
$$

e sua retroação anisotrópica sobre a métrica de $S^3$. O cálculo radial prova
que a magnitude pode ser estabilizada; não calcula ainda o projetor carregado
nem o transporte de $g$ e $g'$.
