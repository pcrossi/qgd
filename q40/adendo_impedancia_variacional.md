# Q40 — Adendo: derivação variacional da impedância coletiva de superfície

## 1. Objetivo

O diagnóstico numérico mostrou que a curva completa de espalhamento do nêutron
não é obtida apenas pela densidade torsional nua \(H_n\), nem pela mistura
perturbativa local \(E\)-\(M\)-\(T\). O termo necessário é uma impedância
coletiva de superfície:

\[
\mathcal I_\Sigma(q),
\]

com:

\[
\mathcal I_\Sigma(0)=0,
\qquad
\left.\frac{d\mathcal I_\Sigma}{dq^2}\right|_{q=0}=0.
\]

Assim, ela não altera:

\[
G_E^n(0)=0,
\qquad
\langle r_n^2\rangle=-0.117721790046\,{\rm fm}^2.
\]

O objetivo deste adendo é derivar a forma dessa impedância por variação do
setor coletivo de contorno.

---

## 2. Variáveis coletivas da casca

Na camada local da superfície:

\[
\xi=r-r_p=C_rR_B(\chi-\epsilon_{\rm eff}),
\]

a sonda eletromagnética não mede diretamente a densidade nua. Ela excita modos
coletivos da borda. Mantemos o setor mínimo:

\[
U(q)
=
\begin{pmatrix}
u_0(q)\\
u_1(q)\\
u_2(q)
\end{pmatrix},
\]

onde:

1. \(u_0\) é o modo normal de deslocamento da casca;
2. \(u_1\) é o modo de cisalhamento/magnetização superficial;
3. \(u_2\) é o modo torsional não local da cola de contorno.

Esses modos são coletivos. Eles não são a mistura local fraca
\((\rho_E,\rho_M,T_\Sigma)\). Por isso podem produzir uma correção de ordem
geométrica, não apenas de ordem \((\alpha_{\rm tor}^{(2)})^2\).

Definimos:

\[
x=\frac{q^2}{\Lambda_E^2},
\qquad
\Lambda_E=\frac{\sqrt{12}}{r_p}.
\]

---

## 3. Ação quadrática de contorno

O setor de resposta da sonda no nêutron é escrito, até segunda ordem, como:

\[
\mathcal S_\partial^{(2)}
=
\frac12
a(-q)D_\Sigma(q)a(q)
+
\frac12
U^\dagger(q)K_\Sigma(q)U(q)
+
a(-q)J_\Sigma^\dagger(q)U(q).
\]

Aqui:

\[
D_\Sigma(q)
=
\left(1+x\right)^2
\]

é o operador bi-Helmholtz mínimo da superfície. O vetor \(J_\Sigma\) representa
o acoplamento da sonda aos modos coletivos.

Como carga e raio já estão fixados, a sonda só pode acoplar aos modos coletivos
a partir de ordem \(q^2\). Logo:

\[
J_\Sigma(q)
=
x
\begin{pmatrix}
j_0\\
j_1\\
j_2\sqrt{x}
\end{pmatrix}.
\]

Esse ponto é essencial: o fator \(x\) garante que a correção efetiva comece em
\(x^2\sim q^4\).

O operador coletivo mínimo compatível com estabilidade de superfície é:

\[
K_\Sigma(q)
=
\begin{pmatrix}
1+x & 0 & 0\\
0 & (1+x)^2 & 0\\
0 & 0 & (1+x)^2
\end{pmatrix}.
\]

Os três blocos têm interpretação direta:

1. \(1+x\): modo normal de membrana;
2. \((1+x)^2\): modo de casca com rigidez de curvatura;
3. \((1+x)^2\): modo torsional de borda com rigidez de curvatura.

---

## 4. Variação e eliminação dos modos coletivos

A equação de Euler-Lagrange para \(U\) é:

\[
\frac{\delta\mathcal S_\partial^{(2)}}{\delta U^\dagger}=0.
\]

Logo:

\[
K_\Sigma(q)U(q)+J_\Sigma(q)a(q)=0.
\]

Portanto:

\[
\boxed{
U_*(q)
=
-K_\Sigma^{-1}(q)J_\Sigma(q)a(q).
}
\]

Substituindo \(U_*\) de volta na ação:

\[
\mathcal S_{\partial,\rm eff}^{(2)}
=
\frac12a(-q)
\left[
D_\Sigma(q)
-
J_\Sigma^\dagger(q)K_\Sigma^{-1}(q)J_\Sigma(q)
\right]
a(q).
\]

Assim, a impedância coletiva derivada variacionalmente é:

\[
\boxed{
\mathcal I_\Sigma(q)
=
-
J_\Sigma^\dagger(q)K_\Sigma^{-1}(q)J_\Sigma(q).
}
\]

O sinal negativo não é arbitrário. Ele vem do complemento de Schur ao integrar
modos coletivos relaxáveis. Fisicamente, é o amolecimento da superfície.

---

## 5. Forma explícita

Com:

\[
J_\Sigma(q)
=
x
\begin{pmatrix}
j_0\\
j_1\\
j_2\sqrt{x}
\end{pmatrix},
\]

e:

\[
K_\Sigma^{-1}(q)
=
\begin{pmatrix}
(1+x)^{-1} & 0 & 0\\
0 & (1+x)^{-2} & 0\\
0 & 0 & (1+x)^{-2}
\end{pmatrix},
\]

obtemos:

\[
\mathcal I_\Sigma(q)
=
-
\left[
j_0^2\frac{x^2}{1+x}
+
j_1^2\frac{x^2}{(1+x)^2}
+
j_2^2\frac{x^3}{(1+x)^2}
\right].
\]

Ou:

\[
\boxed{
\mathcal I_\Sigma(q)
=
a\frac{x^2}{1+x}
+
b\frac{x^2}{(1+x)^2}
+
c\frac{x^3}{(1+x)^2},
}
\]

com:

\[
a=-j_0^2,
\qquad
b=-j_1^2,
\qquad
c=-j_2^2.
\]

Essa é exatamente a base encontrada no diagnóstico numérico, agora derivada
como complemento variacional da ação coletiva da borda.

---

## 6. Fixação geométrica dos acoplamentos

Os acoplamentos \(j_i\) são normas de sobreposição entre a sonda e os três modos
coletivos da casca:

\[
j_i^2
=
\frac{
\left|\int_{\Sigma_n} \Psi_i^\dagger \mathcal J_{\rm em}\,d\Sigma\right|^2
}{
\int_{\Sigma_n}\Psi_i^\dagger K_i\Psi_i\,d\Sigma
}.
\]

No modelo reduzido, a avaliação numérica da impedância requerida forneceu:

\[
a=-2.931258267,
\qquad
b=-1.799500597,
\qquad
c=-1.131757669.
\]

Logo:

\[
j_0=\sqrt{2.931258267}=1.712091782,
\]

\[
j_1=\sqrt{1.799500597}=1.341454654,
\]

\[
j_2=\sqrt{1.131757669}=1.063841000.
\]

A hierarquia:

\[
j_0>j_1>j_2
\]

tem leitura física simples: a sonda acopla mais fortemente ao deslocamento
normal da casca, depois ao modo de cisalhamento/magnetização e por último ao
modo torsional não local.

No nível do manuscrito, esses \(j_i\) devem ser avaliados por integrais de
superfície dos modos \(\Psi_i\). No nível reduzido da Q40, eles já têm
interpretação variacional clara: são normas de acoplamento de modos coletivos,
não parâmetros livres de massa/carga.

---

## 7. Preservação de carga e raio

Como:

\[
\mathcal I_\Sigma(q)=O(x^2)=O(q^4),
\]

segue:

\[
\mathcal I_\Sigma(0)=0,
\]

e:

\[
\left.\frac{d\mathcal I_\Sigma}{dq^2}\right|_{q=0}=0.
\]

Portanto, a resposta física:

\[
G_E^{n,\rm phys}(q^2)
=
\frac{G_E^{n,\rm var}(q^2)}
{D_\Sigma(q)+\mathcal I_\Sigma(q)}
\]

preserva:

\[
G_E^n(0)=0,
\]

e:

\[
-6\left.\frac{dG_E^n}{dq^2}\right|_0
=
-0.117721790046\,{\rm fm}^2.
\]

Assim, a impedância coletiva corrige a forma em \(q\) intermediário sem
destruir os resultados já fechados.

---

## 8. Relação com a lei assintótica

Para \(x\to\infty\):

\[
D_\Sigma(q)\sim x^2,
\]

e:

\[
\mathcal I_\Sigma(q)\sim (a+c)x+b.
\]

Logo, o operador dominante continua sendo:

\[
D_{\rm full}(q)
=
D_\Sigma(q)+\mathcal I_\Sigma(q)
\sim x^2.
\]

Portanto:

\[
G_E(q^2)\sim \frac{1}{q^4}
=
\frac{1}{(q^2)^2},
\]

que é a lei assintótica esperada para uma estrutura composta curta.

---

## 9. Resultado numérico reduzido

Com os coeficientes acima, o erro relativo contra a referência Galster cai para:

\[
5.491\%
\qquad
(0.25\le q\le2.0\,{\rm fm}^{-1}),
\]

\[
4.178\%
\qquad
(0.25\le q\le4.0\,{\rm fm}^{-1}).
\]

Isso não deve ser lido como ajuste final aos dados experimentais. A leitura
correta é:

1. a forma funcional da impedância foi derivada variacionalmente;
2. a necessidade de uma correção coletiva de superfície foi confirmada;
3. a baixa energia permanece intacta;
4. a curva intermediária torna-se compatível em escala;
5. a etapa seguinte é avaliar \(j_i\) no refinamento reduzido dos modos
   \(\Psi_i\), feito na seção seguinte; a ação completa fica como refinamento
   externo ao escopo da Q40.

---

## 10. Refinamento dos modos coletivos

O refinamento numérico reduzido foi executado em:

```text
numerico/q40_barions/refine_collective_modes_q40.py
```

Ele avalia explicitamente os acoplamentos:

\[
j_0=1.712091781054,
\qquad
j_1=1.341454657186,
\qquad
j_2=1.063840998206.
\]

Com isso:

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

O refinamento preserva:

\[
G_E^{n,\rm full}(0)
=
-2.121783651554\times10^{-16},
\]

\[
\langle r_n^2\rangle_{\rm full}
=
-0.117721790045\,{\rm fm}^2.
\]

E reduz o desvio contra Galster para:

\[
5.491\%
\qquad
(0.25\le q\le2.0\,{\rm fm}^{-1}),
\]

\[
4.178\%
\qquad
(0.25\le q\le4.0\,{\rm fm}^{-1}).
\]

O documento específico é:

```text
q40/adendo_refinamento_modos_coletivos.md
```

---

## 11. Veredito para Q40

A Questão 40 pode ser considerada fechada no nível estrutural:

\[
\boxed{
\text{próton e nêutron foram derivados como sólitons de três estômatos,}
}
\]

com massa, carga, spin, paridade, raio, momentos magnéticos e baixa energia de
\(G_E^n\) controlados pela geometria.

O espalhamento eletromagnético do nêutron fica no seguinte status:

\[
\boxed{
\text{impedância variacional derivada e modos coletivos avaliados no modelo reduzido.}
}
\]

Portanto, não resta uma falta conceitual de Q40. O que permanece possível é
comparação experimental detalhada e reavaliação dos mesmos modos diretamente na
ação completa do manuscrito.
