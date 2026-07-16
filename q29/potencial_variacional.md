# Q29 — Bloco 2 — Potencial eletrofraco como expansão variacional

## 1. Objetivo

Derivar a forma efetiva:

\[
V_{\rm eff}(\Phi)
=
-\mu_{\rm EW}^2\Phi^\dagger\Phi
+
\lambda_{\rm EW}(\Phi^\dagger\Phi)^2
+\cdots
\]

como expansão da ação GDQ no modo \(\Phi_{\rm EW}\).

---

## 2. Expansão da ação

Considere uma deformação ao longo do modo eletrofraco:

\[
\mathfrak G(\varphi)
=
\mathfrak G_0+\varphi\,\Phi_{\rm EW}.
\]

A ação efetiva reduzida é:

\[
S_{\rm eff}(\varphi)
=
S_{\rm GDQ}[\mathfrak G(\varphi)].
\]

Expandindo:

\[
S_{\rm eff}(\varphi)
=
S_0
+
\frac12a_2|\varphi|^2
+
\frac14a_4|\varphi|^4
+O(|\varphi|^6).
\]

Para quebra eletrofraca:

\[
\boxed{
a_2<0,
\qquad
a_4>0.
}
\]

Identificamos:

\[
\boxed{
\mu_{\rm EW}^2=-a_2/2,
\qquad
\lambda_{\rm EW}=a_4/4.
}
\]

---

## 3. Origem geométrica de \(a_2\)

O coeficiente quadrático é o autovalor da Hessiana:

\[
\boxed{
a_2
=
\langle
\Phi_{\rm EW},
\mathcal O_{\rm GDQ}^{(2)}
\Phi_{\rm EW}
\rangle.
}
\]

Assim:

\[
a_2<0
\]

significa que o ponto simétrico possui direção instável no fluxo geométrico.

---

## 4. Origem geométrica de \(a_4\)

O coeficiente quartico vem da quarta variação:

\[
\boxed{
a_4
=
\delta^4S_{\rm GDQ}[\Phi_{\rm EW},\Phi_{\rm EW},
\bar\Phi_{\rm EW},\bar\Phi_{\rm EW}].
}
\]

A estabilidade exige:

\[
a_4>0.
\]

Essa positividade é a condição de bacia estável de Perelman para o modo
eletrofraco.

---

## 5. Valor esperado

O mínimo satisfaz:

\[
\frac{dV}{d|\Phi|}=0.
\]

Logo:

\[
\boxed{
v^2
=
\frac{\mu_{\rm EW}^2}{\lambda_{\rm EW}}
=
\frac{-2a_2}{a_4}
}
\]

na normalização:

\[
\langle\Phi\rangle
=
\frac1{\sqrt2}
\begin{pmatrix}0\\v\end{pmatrix}.
\]

---

## 6. Correção obrigatória

A fórmula antiga:

\[
v_K
=
\frac{M_e}{\alpha}
\left(
1-\frac{3}{4\pi^2}
\right)^{-1/2}
\]

não é a escala eletrofraca. Ela dá:

\[
v_K\simeq72{,}85\,{\rm MeV}.
\]

Portanto:

\[
\boxed{
v\neq v_K.
}
\]

Na Q29, \(v\) deve vir de:

\[
\boxed{
v^2=-2a_2/a_4.
}
\]

---

## 7. Status

\[
\boxed{
\text{potencial eletrofraco estruturado como expansão variacional da GDQ.}
}
\]

Falta calcular \(a_2\) e \(a_4\) no background estacionário oficial.
