---
title: "Formalização Lean da fenomenologia nuclear reduzida"
---

# Formalização Lean da fenomenologia nuclear reduzida

Esta nota registra a fronteira exata entre demonstração formal, redução
efetiva e comparação numérica no Capítulo 24. O código canônico é
[NuclearPhenomenology.lean](../../../formal/GDQ/NuclearPhenomenology.lean).

## 1. O que foi formalizado

### 1.1 Canal alfa

Definida a forma reduzida

$$
T_{1/2}(\nu,W)
=
\frac{\ln 2}{\nu}e^W,
$$

o Lean prova que $T_{1/2}>0$ para $\nu>0$ e que a meia-vida cresce
monotonicamente com o expoente $W$. São consequências exatas da forma
reduzida. O código não afirma que a frequência $\nu$ ou o expoente $W$ já
tenham sido calculados pela Hessiana nuclear completa.

### 1.2 Camadas spin--torção

Para cada subnível com $j_2=2j$, a capacidade é

$$
d(j_2)=j_2+1=2j+1.
$$

O Lean verifica as somas cumulativas na ordem espectral reduzida:

$$
2,\ 8,\ 20,\ 28,\ 50,\ 82,\ 126.
$$

A prova é aritmética e exata depois de declarada a ordem dos subníveis. A
seleção dessa ordem pela Hessiana angular de Bismut continua sendo uma
derivação reduzida escrita no capítulo, e não uma diagonalização nuclear 8D
internalizada pelo assistente.

### 1.3 Klein--Nishina e Thomson

A razão cinemática

$$
r(x,\theta)
=
\frac{1}{1+x(1-\cos\theta)}
$$

é estritamente positiva e satisfaz $r\leq1$ para $x\geq0$. A distribuição
normalizada

$$
\mathcal K(x,\theta)
=
\frac12r^2
\left(
r+\frac1r-\sin^2\theta
\right)
$$

obedece exatamente

$$
\mathcal K(0,\theta)
=
\frac12(1+\cos^2\theta).
$$

O último passo usa apenas
$\sin^2\theta+\cos^2\theta=1$. Portanto, o limite Thomson não é uma
coincidência numérica. A origem 8D do vértice e do prefator $r_e^2$ permanece
condicionada à avaliação do projetor fotônico e das variações superiores da
ação oficial.

### 1.4 Setor neutro

Para o candidato reduzido

$$
\chi_\nu
=
\frac{12}{25}e^{-\alpha/4},
\qquad
\lambda_2=\frac{\chi_\nu^2}{2},
\qquad
\lambda_3=\frac{6\pi}{5},
$$

o Lean prova

$$
\chi_\nu>0,
\qquad
\lambda_2>0,
\qquad
\lambda_3>0.
$$

Consequentemente, para uma escala $S_\nu>0$, as diferenças candidatas
$S_\nu\lambda_2$ e $S_\nu\lambda_3$ são positivas. Isso certifica a
consistência algébrica do candidato; não deriva os coeficientes
$12/25$, $1/2$ ou $6\pi/5$ da Hessiana neutra.

No modelo de dois canais, o fator operacional

$$
\mathcal P(\vartheta,\phi)
=
\sin^2(2\vartheta)\sin^2\phi
$$

satisfaz formalmente

$$
0\leq\mathcal P\leq1.
$$

### 1.5 Produção e aniquilação de pares

Para energias de repouso positivas $E_e=m_ec^2$ e $E_N=M_Nc^2$, foi
formalizado o limiar nuclear:

$$
E_{\gamma,\mathrm{th}}^{(N)}
=
2E_e
\left(
1+\frac{E_e}{E_N}
\right).
$$

O Lean prova exatamente:

$$
E_{\gamma,\mathrm{th}}^{(N)}
>
2E_e
$$

e:

$$
E_{\gamma,\mathrm{th}}^{(N)}
-2E_e
=
\frac{2E_e^2}{E_N}.
$$

Também foram formalizadas as duas taxas líderes:

$$
\Gamma_{2\gamma}^{(0)}
=
\frac12\alpha^5\omega_e,
$$

$$
\Gamma_{3\gamma}^{(0)}
=
\frac{2(\pi^2-9)}{9\pi}
\alpha^6\omega_e,
$$

com prova de positividade para $\alpha>0$ e $\omega_e>0$. Por fim, o
parâmetro magnético reduzido:

$$
\chi_\gamma
=
\frac{E_\gamma}{2E_e}
\frac{B_\perp}{B_Q}
$$

é formalmente não negativo para entradas físicas não negativas.

Essas provas certificam cinemática e sinais. Elas não calculam os jatos
$D^3\mathcal S_{\rm GDQ}$ e $D^4\mathcal S_{\rm GDQ}$ no background 8D, nem
promovem as comparações de positrônio e produção nuclear a teoremas da ação.

## 2. O que não foi promovido a teorema

Não foram transformados em axiomas Lean:

1. os blocos reduzidos usados no benchmark alfa;
2. o erro RMS de $0.067894$ décadas;
3. a origem espectral completa da ordem dos níveis nucleares;
4. o projetor fotônico, o vértice Compton 8D e o prefator $r_e^2$;
5. os coeficientes do candidato neutro;
6. a concordância de $\Delta m^2$ com os valores de referência;
7. a fase $\delta_{\rm CP}$ histórica;
8. as vidas experimentais de positrônio e as seções nucleares;
9. o coeficiente assintótico da opacidade magnética;
10. o valor dos jatos de produção e aniquilação no background 8D.

Esses itens continuam classificados no corpo do capítulo como prova de
conceito, redução assintótica, candidato reduzido ou trabalho metrológico
futuro.

## 3. Relação com a ação oficial

O módulo não define uma nova ação nuclear. A cadeia física permanece:

$$
\mathcal S_{\rm GDQ}
\longrightarrow
\Phi_*
\longrightarrow
K^{\rm phys}
\longrightarrow
\text{projetores e operadores de contorno}
\longrightarrow
\text{observável}.
$$

O Lean certifica consequências exatas depois que o operador reduzido foi
obtido. A existência do background e a avaliação funcional dos blocos da
Hessiana pertencem à prova analítica e numérica do domínio físico.

Os módulos `GDQ.NuclearPhenomenology` e `GDQ.AstrophysicsCosmology` foram
compilados conjuntamente; o ponto de entrada canônico completo passou em
$8747$ tarefas. A auditoria `#print axioms` dos cinco teoremas novos deste
capítulo retornou somente `propext`,
`Classical.choice` e `Quot.sound`, sem `axiom`, `sorry` ou `admit` físico.
