# Q29 — Background não linear com fluxo topológico no estômato

## 1. Problema resolvido

O background warped--dilatônico da ação oficial foi resolvido novamente,
substituindo a condição natural

$$
F'(\epsilon)=0
$$

pela condição de fluxo do operador radial principal

$$
\frac{e^{-F(\epsilon)}\sin^2\epsilon}{R^2}
F'(\epsilon)
=-k.
$$

Foram mantidas a regularidade no antipolo, a normalização da medida e as
equações não lineares acopladas para $A$ e $F$. A solução foi construída por
continuação a partir de $k=0$.

## 2. Unidade normalizada de winding

Para

$$
k=1,
$$

o solver convergiu com resíduo máximo

$$
1{,}87\times10^{-5}
$$

e confirmou o fluxo imposto com precisão numérica. A norma interna do modo de
Hopf mudou de

$$
\langle\Phi_Q\rangle_{k=0}
=41{,}5682188582
$$

para

$$
\langle\Phi_Q\rangle_{k=1}
=41{,}3050378.
$$

Portanto,

$$
\boxed{
\frac{K_Q(k=1)}{K_Q(0)}
=0{,}993668694.
}
$$

O dressing não linear de uma unidade normalizada é

$$
\frac{\Delta K_Q}{K_Q}
=-0{,}6331306\%.
$$

## 3. Por que a resposta não é $41\%$

A susceptibilidade relativa $0{,}411889$ havia sido calculada mantendo o warp
$A$ fixo e usando apenas a parte principal da Hessiana dilatônica. No sistema
oficial completo, $F$ e $A$ respondem simultaneamente. A retroação métrica
cancela a maior parte da resposta dilatônica isolada.

Assim, o resultado antigo continua correto como susceptibilidade parcial,
mas não é a derivada on-shell da rigidez física.

## 4. Teste da normalização $2\pi$

Também foi testada, sem calibração experimental, a identificação direta

$$
\int H_B=2\pi k
$$

com o fluxo radial numérico. A continuação perde a solução regular entre

$$
k\simeq0{,}98
\quad\text{e}\quad
k\simeq1{,}18,
$$

com crescimento brusco do resíduo e da malha adaptativa. Portanto, não é
lícito inserir $2\pi$ diretamente na condição radial usada pelo solver.

O inteiro topológico e o fluxo canonicamente normalizado da equação radial
não são automaticamente o mesmo número. Falta derivar o fator de conversão
pela redução da $3$-forma de Bismut sobre o elo $S^3$:

$$
k
=
\frac1{\mathcal N_B}
\int_{S^3}H_B,
\qquad
J_F
=
\frac{1}{\mathcal N_B}
\frac{\delta S_\partial}{\delta F}.
$$

## 5. Comparação com o dressing eletromagnético pendente

O fator condicional anteriormente necessário era

$$
\frac{K_{\rm EM}^{\rm eff}}{K_0}
=0{,}966590303.
$$

A unidade radial testada fornece

$$
0{,}993668694,
$$

e portanto não reproduz aquele fator. Não se deve escolher um valor contínuo
de $k$ para forçar a concordância, pois isso destruiria a quantização que
motivou a rota.

## 6. Auditoria posterior da interpretação

A convenção de Bismut já usada na Q29 fixa

$$
\mathcal N_B=2\pi.
$$

Entretanto, a variação da ação mostra que o winding torsional não induz
diretamente a condição escalar $pF'=-k$. Como a ação contém $-|B|^2/12$, a
fonte correta é distribuída e quadrática:

$$
J_f^{(B)}
=
\frac{\tau}{12}
\left(|B|^2-\langle|B|^2\rangle\right).
$$

Assim, este solver permanece um teste útil de carga escalar de bordo, mas não
deve ser identificado com o winding de Bismut sem um termo de salto adicional.
Ver `q29/normalizacao_bismut_e_fonte_dilatonica.md`.

## 7. Veredito

O cálculo fecha três questões:

1. existe um background GDQ não linear regular com fluxo radial unitário;
2. sua norma de Hopf é calculável e recebe dressing finito;
3. a retroação acoplada é essencial e invalida o uso metrológico da
   susceptibilidade dilatônica isolada.

Mas ele não fecha $\alpha$. O único elo restante dessa rota é derivar
$\mathcal N_B$ e o termo de salto radial diretamente da normalização da torção
de Bismut e do funcional de contorno oficial. Sem essa derivação, nem $k=1$
nem $2\pi k$ podem ser identificados por inspeção com o fluxo escalar do
dilatão.

O cálculo reproduzível está em
`q29/solve_background_fluxo_topologico_q29.py`.
