---
title: "Formalização Lean da astrofísica e cosmologia reduzidas"
---

# Formalização Lean da astrofísica e cosmologia reduzidas

O código canônico deste capítulo é
[AstrophysicsCosmology.lean](../../../formal/GDQ/AstrophysicsCosmology.lean).
Ele reutiliza os resultados já certificados em
[GravityCosmology.lean](../../../formal/GDQ/GravityCosmology.lean),
[ElectroweakStability.lean](../../../formal/GDQ/ElectroweakStability.lean) e
[HydrogenSpectrum.lean](../../../formal/GDQ/HydrogenSpectrum.lean).

Essa reutilização é importante: energia escura, aceleração crítica, mínimo
eletrofraco e resposta protônica não são quatro novas ações. São projeções e
reduções condicionadas da ação oficial.

## 1. Core regular

Se o perfil central de massa possui termo líder

$$
m(r)=m_3r^3+O(r^5),
$$

então o lapse possui termo líder

$$
A(r)
=
1-\frac{2Gm_3}{c^2}r^2+O(r^4).
$$

Definindo

$$
\Lambda_{\rm core}
=
\frac{6Gm_3}{c^2},
$$

o Lean prova exatamente

$$
1-\frac{2Gm_3}{c^2}r^2
=
1-\frac{\Lambda_{\rm core}}{3}r^2.
$$

Também certifica a não negatividade das expressões de curvatura do core para
$\Lambda_{\rm core}\geq0$. A existência de uma solução global com a expansão
acima continua sendo resultado da sela radial reduzida, não consequência
puramente algébrica.

## 2. Torção e estabilidade de Schur

Da contração

$$
|H|^2=6q_T^2\rho^2
$$

segue a rigidez quártica reduzida

$$
\lambda_T=q_T^2\geq0.
$$

A normalização isotrópica mínima dos três canais satisfaz formalmente

$$
1^2+1^2+1^2=3.
$$

Para um bloco eliminado com gap $\lambda_B>0$, o gap escalar de Schur é

$$
\lambda_{\rm Schur}
=
\lambda_A-\frac{J^2}{\lambda_B}.
$$

O código demonstra

$$
J^2<\lambda_A\lambda_B
\quad\Longrightarrow\quad
\lambda_{\rm Schur}>0.
$$

Essa é a condição exata usada para interpretar as pequenas razões de Schur
do cálculo reduzido. Os valores numéricos dos gaps não são axiomas Lean.

## 3. Horizonte e informação

Para gravidade superficial positiva,

$$
T_H=\frac{\kappa_H}{2\pi}>0.
$$

Para um peso de canal $0\leq w\leq1$, o Lean prova

$$
-w\ln w\geq0,
$$

e, para um canal puro,

$$
-1\ln1=0.
$$

Isso certifica a álgebra de entropia usada no toy unitário. Não constrói uma
Page curve física. Essa curva exige os projetores espectrais reais da
Hessiana covariante do background com horizonte.

## 4. Escala eletrofraca e raio de superfície

Sob $a_2<0<a_4$, a amplitude reduzida

$$
\beta_*=\sqrt{-\frac{a_2}{a_4}}
$$

satisfaz exatamente

$$
\beta_*^2=-\frac{a_2}{a_4}.
$$

A formalização também prova a positividade das normalizações

$$
v_{\rm global}
=
M_p\frac{6\pi^5}{7}
$$

para $M_p>0$, e

$$
r_p^{\rm surf}
=
\frac18
\left(1+\frac{\alpha}{4}\right)
\epsilon_{\rm eff}
\frac{3\Lambda_C}{2}
$$

para $\alpha\geq0$, $\epsilon_{\rm eff}>0$ e $\Lambda_C>0$.

Se a resposta de contato escala como $\mu^3$, massas reduzidas
$0\leq\mu_{\rm leve}<\mu_{\rm pesada}$ implicam

$$
0
\leq
\left(\frac{\mu_{\rm leve}}{\mu_{\rm pesada}}\right)^3
<1.
$$

Isso formaliza a supressão relativa da sonda eletrônica. Os valores absolutos
de $H_p^{\rm surf}$ e $J_{p,\ell}$ ainda precisam ser avaliados.

## 5. Pente radiativo neutro

Condicionado à existência do canal radiativo entre orientações neutras
conjugadas, a energia fria por fóton foi definida por:

$$
E_{\gamma,*}^{(ij)}
=
\frac{m_i+m_j}{2}c^2.
$$

O Lean prova que essa energia é simétrica sob $i\leftrightarrow j$ e
estritamente positiva quando $m_i+m_j>0$. Para $hc>0$, o comprimento de onda:

$$
\lambda_{ij,*}
=
\frac{2hc}{(m_i+m_j)c^2}
$$

é estritamente positivo. O transporte cosmológico:

$$
\lambda_0
=
(1+z)\lambda_*
$$

preserva a positividade e satisfaz $\lambda_0\geq\lambda_*$ para $z\geq0$.

Isso certifica o núcleo cinemático do pente e do redshift. Não prova que o
jato $C_{ij\gamma\gamma}^{\rm GDQ}$ seja não nulo e não determina a
intensidade espectral.

## 6. Limites preservados

O módulo não afirma:

1. existência geral de uma sela 8D com horizonte;
2. extensão geodésica global;
3. estabilidade de todos os setores polares e mistos;
4. Page curve física;
5. solução conjunta de CMB, BAO, supernovas, BBN e lentes;
6. derivação integral de $Z_\beta$;
7. metrologia absoluta do raio de cada sonda;
8. existência e valor do canal torsão--torsão--radiação;
9. brilho absoluto do pente neutro e sua separação da emissão por poeira.

Esses pontos permanecem explícitos no capítulo. As comparações numéricas
testam as reduções declaradas; não substituem os elos funcionais faltantes.

Os módulos `GDQ.NuclearPhenomenology` e `GDQ.AstrophysicsCosmology` foram
compilados conjuntamente; o ponto de entrada canônico completo passou em
$8747$ tarefas. A auditoria `#print axioms` dos cinco teoremas novos do pente
e do redshift retornou somente `propext`,
`Classical.choice` e `Quot.sound`, sem `axiom`, `sorry` ou `admit` físico.
