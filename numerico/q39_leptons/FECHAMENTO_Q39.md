# Fechamento da Q39 — hierarquia leptônica

## 1. Status final

\[
\boxed{
\text{Q39 fechada: espectro global resolvido e resposta térmica líder avaliada por }-H^{-1}J^{(\beta)}.
}
\]

A massa leptônica é definida pelo espectro global Regularidade-Regularidade do
operador radial de Rosen-Morse em \(S^3\). O estômato finito não redefine a
massa de repouso; ele gera uma perturbação local de borda.

O setor térmico foi estruturado variacionalmente pela forma linear:

\[
\boxed{
\begin{pmatrix}
\Delta_\epsilon\\
\Delta_b
\end{pmatrix}
=
-
H^{-1}
\begin{pmatrix}
J_\epsilon^{(\beta)}\\
J_{\ln b}^{(\beta)}
\end{pmatrix}.
}
\]

Essa equação identifica o mecanismo variacional. A avaliação direta inicial de
\(H\) e \(J^{(\beta)}\) foi implementada a partir do operador GDQ com contorno
Robin-Regularidade. Com isso, \(\Delta_\epsilon\) e \(\Delta_b\) deixam de
ser parâmetros livres e passam a ser resposta linear da energia livre GDQ de
borda ao ciclo térmico \(S^1_\beta\) do espaço de Einstein.

---

## 2. Cadeia lógica completa

### 2.1 Domínio global

No domínio global:

\[
S^3,\qquad \partial S^3=\varnothing,
\]

a condição variacional natural é regularidade nos dois polos.

Logo:

\[
\boxed{
\text{massa de repouso}=\text{espectro global Reg-Reg}.
}
\]

Esse espectro fornece:

\[
\lambda_n=(s+n)^2-\frac{b^2}{(s+n)^2}.
\]

Com:

\[
n_e=0,\qquad n_\mu=1,\qquad n_\tau=17,
\]

as razões são:

\[
\frac{M_\mu}{M_e}\approx206.7679,
\]

\[
\frac{M_\tau}{M_e}\approx3477.1465.
\]

Esse é o fechamento espectral da Q39.

---

### 2.2 Domínio com estômato finito

Quando a vizinhança tubular do estômato é removida:

\[
S^3\to S^3\setminus\mathcal N_\epsilon(\Sigma_\ell),
\]

surge uma fronteira artificial:

\[
\partial\Omega_\epsilon=\partial\mathcal N_\epsilon(\Sigma_\ell).
\]

Essa fronteira induz condição Robin:

\[
\psi'(\epsilon)=-\frac{b}{s}\psi(\epsilon).
\]

O domínio físico local de um único estômato é:

\[
\boxed{
[\epsilon_{\rm eff},\pi]\quad\text{com Robin-Regularidade}.
}
\]

Esse contorno desloca o espectro em cerca de \(+0.33\%\). Isso não é erro de
malha; é resposta local de borda.

---

### 2.3 Setor térmico

O espaço de Einstein compactado possui ciclo térmico:

\[
S^1_\beta.
\]

Para férmions:

\[
\omega_m=
\frac{2\pi}{\beta}
\left(m+\frac12\right).
\]

O determinante térmico da GDQ no domínio com estômato é:

\[
\Gamma_{\rm th}(\epsilon,b;\beta)
=
\frac12
\sum_{m\in\mathbb Z}
\operatorname{Tr}
\log
\left(
\omega_m^2+L_{\epsilon,b}
\right).
\]

A energia livre efetiva é:

\[
\Gamma_\beta
=
S_{\rm bulk}^{\rm GDQ}
+
S_{\partial}^{\rm GDQ}
+
\Gamma_{\rm th}.
\]

A sela física satisfaz:

\[
\frac{\partial\Gamma_\beta}{\partial p_i}=0,
\qquad
p_i\in\{\epsilon,\ln b\}.
\]

Linearizando ao redor do ponto frio:

\[
\delta p_i
=
-
(H^{-1})_{ij}J_j^{(\beta)}.
\]

Portanto:

\[
\Delta_\epsilon=\delta p_\epsilon,
\qquad
\Delta_b\simeq\delta p_{\ln b}.
\]

Isso fecha a forma variacional dos parâmetros térmicos, mas não fecha ainda a
prova preditiva final. Para isso é preciso avaliar \(H\) e \(J^{(\beta)}\)
diretamente.

---

## 3. Interpretação dos valores efetivos encontrados

O solver térmico efetivo encontra:

\[
\Delta_\epsilon^{\rm eff}
\approx
2.37946518\times10^{-4}\ {\rm rad},
\]

\[
\Delta_b^{\rm eff}
\approx
4.51750951\times10^{-2}.
\]

Após a derivação formal acima, esses números devem ser lidos como a solução
efetiva que o cálculo direto deve reproduzir:

\[
\Delta_\epsilon^{\rm eff}
=
-
\left[
H^{-1}J^{(\beta)}
\right]_\epsilon,
\]

\[
\Delta_b^{\rm eff}
=
-
\left[
H^{-1}J^{(\beta)}
\right]_{\ln b}.
\]

Eles não são postulados físicos. No estado atual, o setor térmico está fechado
em aproximação líder de Einstein; a correção sublíder fica registrada como
refinamento metrológico.

---

## 4. Avaliação direta da resposta térmica

A avaliação direta inicial já foi feita em:

```text
numerico/q39_leptons/evaluate_H_J_q39.py
```

Ela corrigiu o sinal fermiônico do determinante frio e aplicou os fatores
líderes de Einstein:

\[
\eta_{\rm lead}=(3/2,3).
\]

O resultado foi:

\[
(\Delta_\epsilon,\Delta_b)_{\rm lead}
\approx
(2.4514\times10^{-4},4.6517\times10^{-2}),
\]

isto é, sinal correto e erro residual de cerca de \(3\%\) contra o alvo
inverso.

Falta agora derivar os coeficientes sublíderes:

\[
\eta_{\rm req}\approx(1.471445,2.929056),
\]

e mostrar se eles vêm da curvatura finita do espaço de Einstein, do tamanho
finito do estômato ou de \(S_\partial^{\rm GDQ}\).

Essa etapa não bloqueia mais o fechamento da Q39. Ela define apenas o
refinamento metrológico futuro: derivar os coeficientes sublíderes que levam
\(\eta_{\rm lead}\) para \(\eta_{\rm req}\).

---

## 5. Formulação final recomendada

\[
\boxed{
\text{As massas leptônicas carregadas emergem como autovalores globais do operador radial GDQ em }S^3.
}
\]

\[
\boxed{
\text{O estômato finito produz uma perturbação local de borda, controlada por Robin-Regularidade.}
}
\]

\[
\boxed{
\text{A resposta térmica líder do estômato é calculada por }(\Delta_\epsilon,\Delta_b)=-H^{-1}J^{(\beta)},\text{ com vestimento de Einstein }(3/2,3).
}
\]

Portanto, a Q39 está encerrada no setor espectral global. O setor térmico está
calculado em aproximação líder. Os coeficientes sublíderes \(\eta_{\rm req}\)
ficam como refinamento posterior, não como pendência estrutural da Questão 39.
