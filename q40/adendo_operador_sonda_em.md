# Q40 — Adendo: operador de sonda eletromagnética/magnética

## 1. Problema

A solução variacional do perfil torsional \(H_n(\chi)\) fechou os vínculos de
baixa energia do fator de forma elétrico do nêutron:

\[
G_E^n(0)=0,
\qquad
-6\left.\frac{dG_E^n}{dq^2}\right|_0
=
-0.117721790046\,{\rm fm}^2.
\]

Porém a comparação com Galster mostra que a curva líder ainda está distante na
região intermediária. Mesmo com o filtro de superfície:

\[
F_\Sigma(q)=\left(1+\frac{q^2}{\Lambda_\Sigma^2}\right)^{-2},
\qquad
\Lambda_\Sigma=\frac{\sqrt{12}}{r_p},
\]

o RMS relativo permanece em aproximadamente \(33\%\) para
\(q\le4\,{\rm fm}^{-1}\). Isso é grande demais para declarar o espalhamento
elástico completo como resolvido.

Portanto, o problema correto não é adicionar outro fator fenomenológico. O
problema correto é derivar o operador de resposta da sonda a partir da Hessiana
da ação GDQ em torno do nêutron.

---

## 2. Princípio variacional da resposta

Considere o sóliton do nêutron:

\[
\mathfrak G_n
=
\{g_n,f_n,\rho_n,S_n,T_n,A_n,\ldots\}.
\]

Acoplamos uma sonda eletromagnética externa \(a_\mu\) ao setor de contorno:

\[
\mathcal S_{\rm probe}
=
\mathcal S_{\rm GDQ}[\mathfrak G_n]
+
\int_{\partial\mathcal M_n}
a_\mu J^\mu_{\rm em}
\sqrt{h}\,d^3x.
\]

A resposta linear é:

\[
\delta\Phi_i
=
\int
\mathcal R_{ij}(x,y)
J_j(y)\,dy,
\]

onde:

\[
\Phi_i
=
(\rho_E,\rho_M,T_\Sigma,\omega_\Sigma,\ldots).
\]

A matriz inversa de resposta é a Hessiana:

\[
\boxed{
\mathcal R^{-1}_{ij}
=
\left.
\frac{\delta^2\mathcal S_{\rm GDQ}}
{\delta\Phi_i\,\delta\Phi_j}
\right|_{\mathfrak G_n}.
}
\]

No setor eletromagnético mínimo:

\[
\begin{pmatrix}
\delta\rho_E\\
\delta\rho_M\\
\delta T_\Sigma
\end{pmatrix}
=
\begin{pmatrix}
R_{EE} & R_{EM} & R_{ET}\\
R_{ME} & R_{MM} & R_{MT}\\
R_{TE} & R_{TM} & R_{TT}
\end{pmatrix}
\begin{pmatrix}
J_E\\
J_M\\
J_T
\end{pmatrix}.
\]

O fator de forma elétrico medido não é a transformada nua de \(H_n\), mas a
projeção da resposta:

\[
\boxed{
G_E^{n,\rm phys}(q^2)
=
\Pi_E(q)\,
\mathcal R(q)\,
J_{\rm em}(q).
}
\]

---

## 3. Redução radial de superfície

Na camada local:

\[
\xi=r-r_p=C_rR_B(\chi-\epsilon_{\rm eff}),
\]

o perfil líder é:

\[
H_n(\xi,\tau_n)
=
|\mu_n|
\left[
K_{\tau_n}(\xi,\xi_+)-K_{\tau_n}(\xi,\xi_-)
\right].
\]

A sonda de superfície deve agir sobre esse perfil como operador radial:

\[
\mathcal D_\Sigma
=
1
-\ell_\Sigma^2\partial_\xi^2
+\ell_\Sigma^4\partial_\xi^4
+\mathcal C_{EMT},
\]

onde \(\mathcal C_{EMT}\) contém os acoplamentos cruzados elétrico-magnético-
torsionais. Em espaço de momento:

\[
\mathcal D_\Sigma(q)
=
1+\ell_\Sigma^2q^2+\ell_\Sigma^4q^4+\mathcal C_{EMT}(q).
\]

O filtro usado anteriormente corresponde apenas ao caso escalar mínimo:

\[
\mathcal C_{EMT}=0,
\qquad
\ell_\Sigma^2=\frac{r_p^2}{12},
\]

o que dá:

\[
F_\Sigma(q)
=
\mathcal D_\Sigma(q)^{-1}
\simeq
\left(1+\frac{q^2}{\Lambda_\Sigma^2}\right)^{-2},
\qquad
\Lambda_\Sigma=\frac{\sqrt{12}}{r_p}.
\]

Esse filtro é útil como teste de direção, mas não pode substituir a Hessiana
completa.

---

## 4. Condições que o operador completo deve satisfazer

O operador físico de sonda deve obedecer:

### 4.1 Carga nula

\[
G_E^{n,\rm phys}(0)=0.
\]

Isso exige:

\[
\Pi_E(0)\mathcal R(0)J_{\rm em}(0)=0,
\]

consistente com a lei de resíduo:

\[
Q_n=\frac{1}{2\pi i}\oint_{\Gamma_n}\frac{\phi'}{\phi}dz=0.
\]

### 4.2 Inclinação preservada

A inclinação já derivada não deve ser destruída:

\[
-6\left.\frac{dG_E^{n,\rm phys}}{dq^2}\right|_0
=
-0.117721790046\,{\rm fm}^2
\]

salvo correções sublíderes explicitamente calculadas.

### 4.3 Amortecimento intermediário

A curva nua tem excesso de força na região \(q\simeq2\text{--}4\,{\rm fm}^{-1}\).
O operador completo deve amortecer essa região sem alterar carga e raio.

### 4.4 Assintótica

Para grande transferência:

\[
G_E(q^2)\sim(q^2)^{-2}.
\]

Isso sugere que a parte dominante do operador de superfície deve ser do tipo
bi-Helmholtz ou quarto-ordem efetivo:

\[
\mathcal D_\Sigma(q)\sim q^4.
\]

---

## 5. Interpretação física

A curva nua de \(H_n\) é uma densidade de carga torsional interna. O espalhamento
mede outra coisa: a resposta da superfície bariônica à sonda eletromagnética.
Essa resposta mistura:

1. densidade elétrica;
2. densidade magnética;
3. torção de Bismut/Cartan;
4. modos de superfície;
5. geometria de contorno.

Portanto, não é contraditório que \(H_n\) acerte o raio e ainda falhe na curva
intermediária. O raio é um momento de baixa energia. A curva completa depende
da propagação da perturbação pela casca.

---

## 6. Programa numérico mínimo

O próximo solver deve:

1. construir a malha local \(\xi\);
2. montar o vetor base:

   \[
   \Phi=(\rho_E,\rho_M,T_\Sigma);
   \]

3. montar a Hessiana reduzida:

   \[
   H_\Sigma=
   \begin{pmatrix}
   H_{EE} & H_{EM} & H_{ET}\\
   H_{ME} & H_{MM} & H_{MT}\\
   H_{TE} & H_{TM} & H_{TT}
   \end{pmatrix};
   \]

4. resolver:

   \[
   H_\Sigma\delta\Phi=J_{\rm em};
   \]

5. projetar:

   \[
   G_E^{n,\rm phys}(q^2)
   =
   \int
   \delta\rho_E(\xi)\,
   j_0(q(r_p+\xi))d\xi;
   \]

6. verificar:

   \[
   G_E^{n,\rm phys}(0)=0,
   \qquad
   -6G_E'(0)=-0.117721790046\,{\rm fm}^2;
   \]

7. comparar com Galster/dados.

---

## 7. Status

\[
\boxed{
\text{\(H_n\) fecha baixa energia; espalhamento completo exige Hessiana de sonda.}
}
\]

Neste estágio, antes da impedância coletiva, a Questão 40 não deveria afirmar
que \(G_E^n(q^2)\) completo estava resolvido. O correto naquele ponto era:

\[
\boxed{
G_E^n(0)\ \text{e}\ \langle r_n^2\rangle
\ \text{resolvidos; curva fenomenológica completa em andamento.}
}
\]

---

## 8. Primeira avaliação numérica da Hessiana EMT mínima

Foi criado o solver:

```text
numerico/q40_barions/solve_probe_response_q40.py
```

Ele implementa a Hessiana reduzida:

\[
H_\Sigma(q)
=
\begin{pmatrix}
D_E & C_{EM} & C_{ET}\\
C_{EM} & D_M & C_{MT}\\
C_{ET} & C_{MT} & D_T
\end{pmatrix},
\qquad
\Phi=(\rho_E,\rho_M,T_\Sigma).
\]

As escalas usadas foram:

\[
\Lambda_E=4.120110733\,{\rm fm}^{-1},
\qquad
\Lambda_M=4.978460168\,{\rm fm}^{-1},
\qquad
\Lambda_T=54.645815297\,{\rm fm}^{-1}.
\]

Os acoplamentos cruzados foram tomados no nível mínimo torsional:

\[
C_{ij}\propto \alpha_{\rm tor}^{(2)}q^2,
\]

de modo que desapareçam no limite sem torção e preservem os vínculos de baixa
energia.

O resultado confirma:

\[
G_E^{n,\rm EMT}(0)
=
-2.121783651554\times10^{-16},
\]

\[
\langle r_n^2\rangle_{\rm EMT}
=
-0.117721790045\,{\rm fm}^2,
\]

com diferença de apenas:

\[
\Delta\langle r_n^2\rangle
=
4.42\times10^{-13}\,{\rm fm}^2
\]

em relação à curva variacional.

Porém a comparação com Galster mostra:

\[
{\rm RMS}_{q\le2\,{\rm fm}^{-1}}
:
12.680\%\to12.679\%,
\]

\[
{\rm RMS}_{q\le4\,{\rm fm}^{-1}}
:
33.009\%\to33.006\%.
\]

Ou seja, a Hessiana EMT mínima quase não altera o filtro escalar. A razão é
matemática: os termos cruzados escolhidos são de ordem
\(\alpha_{\rm tor}^{(2)}q^2\), portanto entram no complemento de Schur
quadraticamente:

\[
\Delta D_E
\sim
-v^TB^{-1}v
\sim
-\mathcal O\!\left((\alpha_{\rm tor}^{(2)})^2q^4\right).
\]

Como:

\[
(\alpha_{\rm tor}^{(2)})^2\simeq1.895\times10^{-3},
\]

a correção é naturalmente perturbativa demais para resolver a discrepância de
forma intermediária.

### Conclusão operacional

A primeira Hessiana EMT mínima é consistente, mas insuficiente. Ela mostra que
o termo faltante não é uma mistura fraca \(E\)-\(M\)-\(T\) proporcional apenas a
\(\alpha_{\rm tor}\). O termo que deve ser derivado da ação GDQ completa é uma
impedância de superfície de ordem geométrica:

\[
\mathcal I_\Sigma(q)
=
\left.
\frac{\delta^2\mathcal S_{\rm GDQ}^{\partial}}
{\delta a_{\rm em}(q)\,\delta a_{\rm em}(-q)}
\right|_{\mathfrak G_n},
\]

incluindo a resposta coletiva da casca, não apenas a mistura perturbativa entre
densidade elétrica, densidade magnética e torção local.

O próximo refinamento deve substituir:

\[
D_E=(1+q^2/\Lambda_E^2)^2
\]

por:

\[
D_E^{\rm full}(q)
=
(1+q^2/\Lambda_E^2)^2
+
\mathcal I_\Sigma(q),
\]

com \(\mathcal I_\Sigma(0)=0\) e
\(\mathcal I_\Sigma'(0)=0\), para preservar carga e raio.

---

## 9. Diagnóstico da impedância requerida

Foi criado o script:

```text
numerico/q40_barions/diagnose_surface_impedance_q40.py
```

Ele não introduz uma nova teoria nem ajusta a GDQ. Ele pergunta qual impedância
escalar efetiva seria necessária para mapear a curva variacional GDQ na
referência Galster:

\[
D_{\rm req}(q)
=
\frac{G_E^{n,\rm var}(q^2)}
{G_E^{n,\rm Galster}(q^2)}.
\]

Subtraindo o operador bi-Helmholtz mínimo:

\[
D_\Sigma(q)
=
\left(1+\frac{q^2}{\Lambda_E^2}\right)^2,
\]

define-se:

\[
\mathcal I_\Sigma^{\rm req}(q)
=
D_{\rm req}(q)-D_\Sigma(q).
\]

A impedância foi aproximada em uma base que começa em \(q^4\), preservando
carga e raio:

\[
\mathcal I_\Sigma(q)
=
a\frac{x^2}{1+x}
+b\frac{x^2}{(1+x)^2}
+c\frac{x^3}{(1+x)^2},
\qquad
x=\frac{q^2}{\Lambda_E^2}.
\]

O diagnóstico no intervalo \(0.25\le q\le4\,{\rm fm}^{-1}\) fornece:

\[
a=-2.931258267,
\qquad
b=-1.799500597,
\qquad
c=-1.131757669.
\]

Com essa forma, o RMS relativo cai:

\[
12.680\%\to5.491\%
\qquad
(0.25\le q\le2.0\,{\rm fm}^{-1}),
\]

\[
33.010\%\to4.178\%
\qquad
(0.25\le q\le4.0\,{\rm fm}^{-1}).
\]

### Leitura física

A impedância requerida:

1. começa em \(q^4\), portanto não altera carga nem raio;
2. tem magnitude de ordem geométrica, não de ordem
   \((\alpha_{\rm tor}^{(2)})^2\);
3. tem sinal efetivo negativo no intervalo analisado, indicando amolecimento
   coletivo da casca, não simples blindagem perturbativa;
4. explica por que a Hessiana EMT mínima foi insuficiente.

Portanto, a pendência precisa ser formulada como derivação variacional de uma
impedância coletiva de superfície:

\[
\mathcal I_\Sigma(q)
=
\left.
\frac{\delta^2\mathcal S_{\rm GDQ}^{\partial,\rm col}}
{\delta a_{\rm em}(q)\delta a_{\rm em}(-q)}
\right|_{\mathfrak G_n},
\]

onde \(\mathcal S_{\rm GDQ}^{\partial,\rm col}\) é o setor coletivo da borda,
incluindo deformação da casca, magnetização e torção não local.

Essa derivação foi desenvolvida explicitamente em:

```text
q40/adendo_impedancia_variacional.md
```

O resultado é:

\[
\mathcal I_\Sigma(q)
=
-
J_\Sigma^\dagger(q)K_\Sigma^{-1}(q)J_\Sigma(q),
\]

isto é, a impedância coletiva é o complemento de Schur dos modos relaxáveis de
superfície. Assim, o sinal negativo e o início em \(q^4\) deixam de ser
postulados e passam a ser consequências variacionais.
