# Q30 — Prova do contorno causal pela thimble única

## 1. Setor físico

Fixe uma classe topológica torsional $Q_T$ e o domínio físico

$$
\mathfrak C_{Q_T}^{\rm phys}
=\{(g,f,\bar f):S=0,\ Q_T\text{ fixo},\ \int e^{-u}dV=1\}
/\text{simetrias}.
$$

O contorno causal intrínseco da variedade é

$$
\gamma\subset\mathbb C_{z_\tau},
\qquad
z_\tau=\tau+i\nu_0t,
$$

com involução causal

$$
\iota:z_\tau\mapsto\bar z_\tau,
\qquad
(g,f,\bar f)\mapsto(g,\bar f,f).
$$

Seu levantamento ao espaço de configurações é o ciclo
$\mathcal C_\gamma$ de campos compatíveis com essa involução.

## 2. Corte espectral

Seja $P_N$ a projeção sobre os primeiros $N$ modos físicos da Hessiana e

$$
S_N:=S_{\rm GDQ}\big|_{P_N\mathfrak C_{Q_T}^{\rm phys}}.
$$

Os resultados anteriores da Q30 fornecem, no setor adotado:

$$
\boxed{
\operatorname{Hess}\operatorname{Re}S_N
\ge m^2 I,
\qquad m^2>0,
}
$$

com a mesma cota após remover os modos de simetria. A coercividade significa

$$
\operatorname{Re}S_N(\Phi)
\ge
\operatorname{Re}S_N(q_N)
+\frac{m^2}{2}\|\Phi-q_N\|^2.
$$

## 3. Unicidade da sela

No componente físico geodesicamente convexo determinado pela classe $Q_T$,
a desigualdade anterior implica:

1. existência de mínimo $q_N$;
2. unicidade de $q_N$;
3. ausência de outros pontos críticos;
4. crescimento de $\operatorname{Re}S_N$ em todas as extremidades.

Logo,

$$
\boxed{
\operatorname{Crit}(S_N)\cap\mathfrak C_{Q_T}^{\rm phys}
=\{q_N\}.
}
$$

## 4. Fluxo de Picard--Lefschetz

Considere

$$
\frac{d\Phi^A}{ds}
=-G^{A\bar B}
\overline{\frac{\partial S_N}{\partial\Phi^B}}.
$$

Então

$$
\frac{d}{ds}\operatorname{Re}S_N
=-|\partial S_N\|_G^2\le0,
$$

$$
\frac{d}{ds}\operatorname{Im}S_N=0.
$$

A variedade estável de $q_N$ é a thimble $\mathcal J_N$; a instável é
$\mathcal K_N$. Como a ação é própria e há apenas uma sela, todo fluxo no
componente físico termina em $q_N$ numa direção e em
$\operatorname{Re}S_N\to+\infty$ na outra.

## 5. Número de interseção

A involução causal deixa $q_N$ fixo e troca as duas metades avançada e
retardada de $\mathcal C_\gamma$. A orientação física de $\gamma$ determina
um único cruzamento transversal com a thimble ascendente:

$$
\boxed{
n_N
=\langle\mathcal C_\gamma,\mathcal K_N\rangle
=+1.
}
$$

Não existem outras thimbles no componente. Pela decomposição de
Picard--Lefschetz,

$$
\boxed{
[\mathcal C_\gamma]=[\mathcal J_N]
}
$$

na homologia relativa

$$
H_N
\left(
\mathfrak C_{Q_T,N}^{\rm phys},
\{\operatorname{Re}S_N\to+\infty\}
\right).
$$

## 6. Ausência de Stokes

Um salto de Stokes exige duas selas distintas $q_i,q_j$ com

$$
\operatorname{Im}S_N(q_i)=\operatorname{Im}S_N(q_j).
$$

Como existe apenas $q_N$ no componente físico,

$$
\boxed{
\text{não há par de selas e, portanto, não há parede de Stokes interna.}
}
$$

Selas de outra carga torsional pertencem a componentes topológicos distintos
e não entram na mesma decomposição sem uma cirurgia que altere $Q_T$.

## 7. Positividade

Na thimble,

$$
\operatorname{Im}S_N=\operatorname{Im}S_N(q_N)
$$

é constante. Retirando essa fase global, a medida é

$$
d\mu_{N,\rm phys}
=e^{-\operatorname{Re}S_N/\hbar}
|J_N|d^Nx,
$$

com orientação escolhida pelo cruzamento $n_N=+1$. Assim,

$$
\boxed{d\mu_{N,\rm phys}\ge0.}
$$

## 8. Limite $N\to\infty$

O setor gaussiano já possui convergência em norma de traço para

$$
C_\tau=e^{-\tau L}L^{-1},
\qquad \tau>0.
$$

Com a cota coerciva uniforme, as medidas são apertadas e os funcionais
cilíndricos convergem. A unicidade impede redistribuição entre thimbles no
limite. Portanto,

$$
\boxed{
[\mathcal C_\gamma]=[\mathcal J_*],
\qquad
d\mu_{\rm phys}\ge0,
\qquad
\text{sem Stokes no setor }Q_T.
}
$$

## 9. Teorema

> **Teorema do contorno causal GDQ.** No componente físico de carga torsional
> fixa, suponha a coercividade uniforme da ação após $S=0$ e remoção das
> simetrias. Então o levantamento do contorno causal intrínseco é homólogo à
> única thimble tubular, possui número de interseção $+1$, define estado
> positivo após remoção da fase constante e não sofre saltos de Stokes
> internos.

## 10. Hipóteses efetivamente usadas

1. $S=0$ define o domínio físico;
2. $Q_T$ é conservada e separa componentes;
3. o componente reduzido é geodesicamente convexo;
4. a cota de Hessiana é uniforme em $N$;
5. a involução causal orienta o cruzamento como $+1$;
6. o limite de medidas preserva a cota coerciva.

Os itens 3--6 são a forma matemática precisa da afirmação de que o contorno
causal pertence à variedade física e de que a coercividade setorial se mantém
globalmente. Sem eles, existência local da Hessiana não bastaria.

## 11. Classificação

- fluxo de Picard--Lefschetz: identidade exata;
- unicidade e ausência de Stokes: teorema sob coercividade global;
- número de interseção: fixado pela involução/orientação causal;
- positividade: consequência na thimble orientada;
- limite funcional: condicional à uniformidade da cota já adotada.

