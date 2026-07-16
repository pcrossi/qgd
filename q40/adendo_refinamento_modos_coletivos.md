# Q40 — Adendo: refinamento dos modos coletivos de superfície

## 1. Objetivo

Este adendo executa o refinamento que restava após a derivação variacional da
impedância coletiva:

\[
\mathcal I_\Sigma(q)
=
-
J_\Sigma^\dagger(q)K_\Sigma^{-1}(q)J_\Sigma(q).
\]

A tarefa é avaliar, no modelo reduzido da Q40, os acoplamentos dos modos
coletivos:

\[
J_\Sigma(q)
=
x
\begin{pmatrix}
j_0\\
j_1\\
j_2\sqrt{x}
\end{pmatrix},
\qquad
x=\frac{q^2}{\Lambda_E^2}.
\]

Os três modos são:

1. \(\Psi_0\): deslocamento normal da casca;
2. \(\Psi_1\): cisalhamento/magnetização superficial;
3. \(\Psi_2\): torção não local da cola de contorno.

---

## 2. Solver

O refinamento foi implementado em:

```text
numerico/q40_barions/refine_collective_modes_q40.py
```

Saída:

```text
numerico/q40_barions/saida_collective_modes_q40.md
```

Figuras:

```text
numerico/figs/neutron_collective_modes_curve_q40.png
numerico/figs/neutron_collective_modes_impedance_q40.png
```

---

## 3. Acoplamentos avaliados

A projeção dos modos coletivos fornece:

\[
j_0=1.712091781054,
\]

\[
j_1=1.341454657186,
\]

\[
j_2=1.063840998206.
\]

Equivalentemente:

\[
j_0^2=2.931258266752,
\qquad
j_1^2=1.799500597287,
\qquad
j_2^2=1.131757669465.
\]

Portanto:

\[
\mathcal I_\Sigma(q)
=
-
\left[
2.931258266752\frac{x^2}{1+x}
+
1.799500597287\frac{x^2}{(1+x)^2}
+
1.131757669465\frac{x^3}{(1+x)^2}
\right].
\]

Essa é a forma variacional refinada da impedância no modelo reduzido.

---

## 4. Verificação de baixa energia

O solver obtém:

\[
G_E^{n,\rm full}(0)
=
-2.121783651554\times10^{-16}.
\]

O raio quadrático permanece:

\[
\langle r_n^2\rangle_{\rm var}
=
-0.117721790046\,{\rm fm}^2,
\]

\[
\langle r_n^2\rangle_{\rm full}
=
-0.117721790045\,{\rm fm}^2.
\]

A diferença é:

\[
\Delta\langle r_n^2\rangle
=
8.284\times10^{-13}\,{\rm fm}^2.
\]

Logo, o refinamento não destrói carga nem raio.

---

## 5. Comparação de forma

Contra Galster como benchmark compacto:

### Superfície escalar

\[
{\rm RMS}_{0.25\le q\le2.0}=12.680\%,
\]

\[
{\rm RMS}_{0.25\le q\le4.0}=33.010\%.
\]

### Modos coletivos refinados

\[
{\rm RMS}_{0.25\le q\le2.0}=5.491\%,
\]

\[
{\rm RMS}_{0.25\le q\le4.0}=4.178\%.
\]

Assim, a curva deixa de estar grosseiramente fora e entra no regime de
comparação experimental fina.

---

## 6. Leitura física

O resultado confirma a sequência lógica:

1. \(H_n\) resolve carga e raio;
2. o filtro escalar de superfície acerta a direção, mas não a forma;
3. a Hessiana EMT local é pequena demais;
4. a impedância coletiva de superfície fornece a correção dominante;
5. a origem variacional é o complemento de Schur dos modos relaxáveis;
6. a correção começa em \(q^4\), preservando baixa energia;
7. a queda assintótica \(G_E\sim(q^2)^{-2}\) permanece.

---

## 7. Status

\[
\boxed{
\text{Q40 fechada no nível estrutural e no refinamento reduzido de superfície.}
}
\]

O que ainda pode ser feito depois é comparação experimental detalhada e
avaliação dos mesmos modos \(\Psi_i\) diretamente na ação completa do manuscrito.
Isso já é refinamento fenomenológico, não lacuna da Questão 40.
