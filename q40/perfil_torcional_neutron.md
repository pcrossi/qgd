# Q40 — Perfil torsional suave para \(G_E^n\)

## 1. Objetivo

O fechamento por duas cascas de \(G_E^n\) é suficiente para fixar:

\[
G_E^n(0)=0,
\qquad
\left\langle r_n^2\right\rangle
=
-2|\mu_n|\alpha_{\rm tor}^{(2)}r_p^2.
\]

Mas ele ainda é uma idealização de borda. Para obter uma curva de fator de
forma em \(q^2\) que seja mais representativa, a distribuição singular deve ser
substituída por um perfil suave de cola torsional.

---

## 2. Troca das cascas por núcleos de calor de superfície

A substituição natural na GDQ é:

\[
\delta(\chi-\chi_\pm)
\longrightarrow
K_\sigma(\xi,\xi_\pm),
\]

Como \(r_+^{(2)}<r_p<r_-^{(2)}\), a componente positiva está ligeiramente no
lado interno do estômato e a componente negativa no lado externo. Portanto, o
perfil suave não deve ser interpretado como uma densidade volumétrica do bulk
em \(\chi\in[\epsilon_{\rm eff},\pi]\). Ele é uma densidade local de camada de
superfície.

Definimos a coordenada local:

\[
\xi=r-r_p=C_rR_B(\chi-\epsilon_{\rm eff}).
\]

Então:

\[
K_\sigma(\xi,\xi_0)
=
\frac{1}{\sqrt{2\pi}\sigma_r}
\exp\left[-\frac{(\xi-\xi_0)^2}{2\sigma_r^2}\right],
\qquad
\int_{-\infty}^{+\infty}K_\sigma(\xi,\xi_0)d\xi=1.
\]

Assim, cada componente preserva carga unitária e a diferença preserva carga
total nula sem introduzir um corte artificial de domínio.

---

## 3. Escala geométrica da largura

O deslocamento relativo de cola dupla já é:

\[
\alpha_{\rm tor}^{(2)}
=
2\alpha\ln(2\pi^2).
\]

O raio do estômato é \(\epsilon_{\rm eff}\). Portanto, a largura térmico-
torsional líder é:

\[
\sigma_\chi
=
\frac12\epsilon_{\rm eff}\alpha_{\rm tor}^{(2)},
\qquad
\sigma_r
=
C_rR_B\sigma_\chi
=
\frac12r_p\alpha_{\rm tor}^{(2)}.
\]

Essa escolha é conservadora: a largura é uma fração de segunda ordem do
estômato, não um novo parâmetro livre macroscópico.

---

## 4. Densidade elétrica suave do nêutron

O fechamento estendido suave fica:

\[
\rho_E^n(\chi)
=
|\mu_n|
\left[
K_{\sigma}(\xi,\xi_+^{(2)})
-
K_{\sigma}(\xi,\xi_-^{(2)})
\right],
\]

com:

\[
\xi_+^{(2)}
=
-\frac12r_p\alpha_{\rm tor}^{(2)},
\qquad
\xi_-^{(2)}
=
\frac12r_p\alpha_{\rm tor}^{(2)}.
\]

Equivalentemente, na coordenada observável:

\[
r_\pm^{(2)}
=
r_p
\left(1\mp\frac{\alpha_{\rm tor}^{(2)}}{2}\right).
\]

A casca negativa continua mais externa:

\[
\chi_-^{(2)}>\chi_+^{(2)}.
\]

---

## 5. Fator de forma suave

O fator de forma torna-se:

\[
G_{E,\rm suave}^n(q^2)
=
|\mu_n|
\int_{-\infty}^{+\infty}
\left[
K_{\sigma}(\xi,\xi_+^{(2)})
-
K_{\sigma}(\xi,\xi_-^{(2)})
\right]
j_0(q(r_p+\xi))\,d\xi.
\]

Como os dois núcleos têm a mesma normalização:

\[
G_{E,\rm suave}^n(0)=0.
\]

Como as duas larguras são iguais, a contribuição comum de variância cancela na
diferença dos segundos momentos. Logo:

\[
\left\langle r_n^2\right\rangle_{\rm suave}
=
|\mu_n|(r_+^2-r_-^2)
=
-2|\mu_n|\alpha_{\rm tor}^{(2)}r_p^2
\]

exatamente no modelo local de superfície, pois as duas variâncias gaussianas
são iguais e se cancelam na diferença.

---

## 6. Status

Esse perfil fecha a etapa variacional líder:

1. remove a distribuição delta;
2. preserva \(G_E^n(0)=0\);
3. preserva a inclinação de baixa energia;
4. produz uma curva \(G_E^n(q^2)\) suave;
5. coincide com a solução \(H_n(\chi)\) do fluxo de calor de Perelman na camada
   local de superfície.

Portanto, a Q40 fica estruturalmente fechada para normalizações, momentos,
raios de baixa energia e forma suave líder. A etapa posterior é comparar a
curva com espalhamento elástico e incorporar correções magnéticas/de sonda.
