# Q40 — Adendo: solução variacional de \(H_n(\chi)\)

## 1. Objetivo

O fechamento anterior de \(G_E^n\) substituiu as duas cascas de carga por uma
camada suave de superfície. Faltava justificar esse perfil a partir de uma
equação variacional, isto é, escrever \(H_n(\chi)\) como solução de um problema
de extremalização da GDQ, e não apenas como regularização conveniente.

O objetivo deste adendo é derivar:

\[
H_n(\chi)
\]

como perfil torsional estacionário da cola antiparalela do nêutron.

---

## 2. Coordenada correta da variação

O perfil do nêutron vive na camada de superfície do estômato. A coordenada
radial observável é:

\[
r=C_rR_B\chi.
\]

Escrevemos a coordenada local de superfície:

\[
\xi=r-r_p=C_rR_B(\chi-\epsilon_{\rm eff}).
\]

Essa coordenada atravessa o contorno. Portanto, ela não deve ser cortada
artificialmente em \(\xi\ge0\). A componente positiva da polarização elétrica
fica ligeiramente no lado interno do estômato, enquanto a componente negativa
fica ligeiramente no lado externo.

---

## 3. Fonte torsional estacionária

Para o nêutron, a lei de compensação torsional estacionária é:

\[
(\mathcal T_1,\mathcal T_2,\mathcal T_3)
=
(\tau,\tau,-2\tau),
\qquad
\sum_a\mathcal T_a=0.
\]

No canal elétrico neutro, isso aparece como duas interfaces de sinal oposto:

\[
\xi_+=-\frac12r_p\alpha_{\rm tor}^{(2)},
\qquad
\xi_-=\frac12r_p\alpha_{\rm tor}^{(2)},
\]

onde:

\[
\alpha_{\rm tor}^{(2)}=2\alpha\ln(2\pi^2).
\]

A fonte torsional de superfície é:

\[
J_n(\xi)
=
|\mu_n|
\left[
\delta(\xi-\xi_+)-\delta(\xi-\xi_-)
\right].
\]

Ela satisfaz:

\[
\int J_n(\xi)d\xi=0.
\]

Logo, a carga global permanece nula.

---

## 4. Funcional variacional reduzido

Na vizinhança da solução estacionária, a ação GDQ de contorno reduzida para a
cola torsional tem a forma quadrática de Hessiana:

\[
\mathcal S_H[H]
=
\frac12
\int
H(\xi)
\left(\partial_\tau-\partial_\xi^2\right)
H(\xi)
d\xi d\tau
-
\int J_n(\xi)H(\xi,0)d\xi .
\]

Essa é a forma local da equação de calor conjugada de Perelman na camada de
superfície. A variação dá:

\[
\frac{\delta\mathcal S_H}{\delta H}=0
\quad\Longrightarrow\quad
\left(\partial_\tau-\partial_\xi^2\right)H_n(\xi,\tau)=0,
\]

com condição inicial torsional:

\[
H_n(\xi,0)=J_n(\xi).
\]

Portanto:

\[
H_n(\xi,\tau)
=
e^{\tau\partial_\xi^2}J_n(\xi).
\]

---

## 5. Solução por núcleo de calor

O núcleo de calor na camada local é:

\[
K_\tau(\xi,\xi_0)
=
\frac{1}{\sqrt{4\pi\tau}}
\exp\left[-\frac{(\xi-\xi_0)^2}{4\tau}\right].
\]

Logo:

\[
\boxed{
H_n(\xi,\tau)
=
|\mu_n|
\left[
K_\tau(\xi,\xi_+)
-
K_\tau(\xi,\xi_-)
\right].
}
\]

Essa é a solução variacional procurada.

---

## 6. Fixação geométrica de \(\tau\)

A largura física do núcleo é:

\[
\sigma_r=\sqrt{2\tau}.
\]

A escala torsional líder já foi fixada pela separação de cola dupla:

\[
\sigma_r
=
\frac12r_p\alpha_{\rm tor}^{(2)}.
\]

Portanto:

\[
\boxed{
\tau_n
=
\frac{\sigma_r^2}{2}
=
\frac18r_p^2\left(\alpha_{\rm tor}^{(2)}\right)^2.
}
\]

Nenhum parâmetro fenomenológico novo foi introduzido.

---

## 7. Densidade elétrica e fator de forma

Identificamos a densidade elétrica efetiva do nêutron com o perfil torsional
projetado:

\[
\rho_E^n(\xi)=H_n(\xi,\tau_n).
\]

Então:

\[
\boxed{
G_E^n(q^2)
=
\int_{-\infty}^{+\infty}
H_n(\xi,\tau_n)
j_0(q(r_p+\xi))\,d\xi.
}
\]

Como:

\[
\int K_{\tau_n}(\xi,\xi_+)d\xi
=
\int K_{\tau_n}(\xi,\xi_-)d\xi
=1,
\]

temos:

\[
\boxed{
G_E^n(0)=0.
}
\]

Além disso, como os dois núcleos têm a mesma largura:

\[
\left\langle r_n^2\right\rangle
=
|\mu_n|
\left[
(\xi_++r_p)^2-(\xi_-+r_p)^2
\right].
\]

Logo:

\[
\boxed{
\left\langle r_n^2\right\rangle
=
-2|\mu_n|\alpha_{\rm tor}^{(2)}r_p^2.
}
\]

Ou seja, a solução variacional preserva exatamente o fechamento de baixa
energia já obtido.

---

## 8. Status

O solver `numerico/q40_barions/solve_hn_variational_q40.py` fornece:

\[
\xi_+=-0.018299662921\,{\rm fm},
\qquad
\xi_-=+0.018299662921\,{\rm fm},
\]

\[
\sigma_r=0.018299662921\,{\rm fm},
\qquad
\tau_n=1.674388315199\times10^{-4}\,{\rm fm}^2.
\]

A carga integrada é:

\[
\int H_n d\xi=-2.12\times10^{-16}.
\]

Logo:

\[
G_E^n(0)=-2.12\times10^{-16}.
\]

O momento quadrático direto é:

\[
\langle r_n^2\rangle=-0.117721789624\,{\rm fm}^2.
\]

A inclinação numérica é:

\[
-6\left.\frac{dG_E^n}{dq^2}\right|_0
=
-0.117721790046\,{\rm fm}^2.
\]

Portanto, o erro entre momento direto, fórmula analítica e inclinação é apenas
erro numérico de discretização.

---

Com este adendo:

1. \(H_n(\chi)\) foi derivado como solução variacional do setor de contorno;
2. a curva completa líder \(G_E^n(q^2)\) foi determinada por integral de Fourier
   radial;
3. \(G_E^n(0)=0\) segue automaticamente;
4. \(\langle r_n^2\rangle\) segue automaticamente;
5. nenhum dado experimental do raio elétrico do nêutron foi usado como entrada.

O que permanece posterior é comparar a curva obtida com dados de espalhamento
elástico e, se necessário, incluir correções de sonda, canais magnéticos e
modos excitados da Hessiana completa.

---

## 9. Comparação fenomenológica inicial com Galster

Foi criado o script:

```text
numerico/q40_barions/compare_ge_neutron_q40.py
```

Ele usa a curva variacional:

\[
G_E^n(q^2)
=
\int H_n(\xi,\tau_n)j_0(q(r_p+\xi))d\xi
\]

e a compara com a parametrização de Galster:

\[
G_{E,\rm Galster}^n(Q^2)
=
-\mu_n
\frac{\tau}{1+\eta\tau}
G_D(Q^2),
\qquad
\tau=\frac{Q^2}{4M_N^2},
\qquad
G_D=(1+Q^2/0.71)^{-2}.
\]

A comparação não ajusta parâmetros da GDQ. Ela é somente um teste de forma.
O resultado numérico foi:

\[
{\rm RMS}_{0\le q\le2\,{\rm fm}^{-1}}
=
4.554086\times10^{-3},
\qquad
{\rm RMS}_{\rm rel}=18.586\%.
\]

Para \(0\le q\le4\,{\rm fm}^{-1}\), o RMS relativo sobe para
\(50.656\%\). O pico da curva GDQ líder ocorre em:

\[
q_{\rm pico}^{\rm GDQ}=3.260\,{\rm fm}^{-1},
\qquad
G_E^n=0.088420819,
\]

enquanto Galster produz:

\[
q_{\rm pico}^{\rm Galster}=2.960\,{\rm fm}^{-1},
\qquad
G_E^n=0.054711709.
\]

Foi então acrescentado o operador líder de sonda/superfície:

\[
F_\Sigma(q)
=
\left(1+\frac{q^2}{\Lambda_\Sigma^2}\right)^{-2},
\qquad
\Lambda_\Sigma=\frac{\sqrt{12}}{r_p}
=4.119257854\,{\rm fm}^{-1}.
\]

A curva física líder passa a ser:

\[
G_{E,\Sigma}^n(q^2)=F_\Sigma(q)G_{E,\rm var}^n(q^2).
\]

Como \(F_\Sigma(0)=1\), o operador de sonda preserva carga nula e inclinação
no zero. A comparação melhora para:

\[
{\rm RMS}_{\rm rel}:18.586\%\to12.680\%
\qquad
(0\le q\le2\,{\rm fm}^{-1}),
\]

\[
{\rm RMS}_{\rm rel}:50.656\%\to33.009\%
\qquad
(0\le q\le4\,{\rm fm}^{-1}).
\]

Portanto, a solução variacional de \(H_n\) fecha a estrutura de baixa energia
— carga nula e raio quadrático — e o filtro de superfície derivado de \(r_p\)
aponta a deformação correta em espalhamento. A curva fenomenológica completa
ainda requer a inclusão do operador de sonda/magnetização da Hessiana
eletromagnética completa. Essa correção deve deformar a região intermediária sem
destruir os vínculos:

\[
G_E^n(0)=0,
\qquad
-6\left.\frac{dG_E^n}{dq^2}\right|_0
=
-0.117721790046\,{\rm fm}^2.
\]
