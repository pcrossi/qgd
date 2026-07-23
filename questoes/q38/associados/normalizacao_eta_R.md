# Q38 — Normalização de \(\eta_R\)

## 1. Objetivo

Este documento trata da primeira pendência técnica de Q38:

\[
\boxed{
\eta_R
\text{ deve ser fixado pela projeção da curvatura complexa sobre }R[h],
\text{ não por ajuste numérico de }G.
}
\]

Na redução gravitacional:

\[
\mathcal R[g]
\supset
\eta_R e^{-2A(y,\tau)}R[h].
\]

Portanto, \(\eta_R\) é o fator que converte a curvatura escalar usada na ação
Kähler--Ricci da GDQ na curvatura escalar real da métrica física \(h_{\mu\nu}\).

---

## 2. Decomposição da métrica

Tomamos a decomposição local:

\[
\mathcal M_{\mathbb C}
\simeq
N\times K,
\]

com coordenadas externas \(x^\mu\) e internas \(y^a\). O bloco externo é:

\[
ds^2_{\rm ext}
=
e^{2A(y,\tau)}h_{\mu\nu}(x)dx^\mu dx^\nu.
\]

Na escrita complexa, a mesma estrutura aparece no bloco Hermitiano:

\[
g_{\mu\bar\nu}^{\rm ext}
=
\kappa_H e^{2A(y,\tau)}h_{\mu\nu}(x),
\]

onde \(\kappa_H\) registra a convenção de passagem entre:

1. métrica Hermitiana \(g_{\mu\bar\nu}\);
2. métrica real \(h_{\mu\nu}\);
3. escolha de escrever \(ds^2=g_{\mu\bar\nu}dz^\mu d\bar z^\nu\) ou
   \(ds^2=2g_{\mu\bar\nu}dz^\mu d\bar z^\nu\).

Esse é exatamente o ponto onde fatores \(1\), \(2\) ou \(1/2\) podem aparecer.

---

## 3. Regra tensorial para \(\eta_R\)

Defina a curvatura escalar complexa usada na ação como:

\[
\mathcal R_{\rm GDQ}
=
g^{\mu\bar\nu}R_{\mu\bar\nu}
+\cdots.
\]

Na expansão adiabática, mantendo apenas o termo com duas derivadas externas de
\(h_{\mu\nu}\), temos:

\[
\mathcal R_{\rm GDQ}
=
\eta_R e^{-2A}R[h]
+\mathcal R_K
+\mathcal R_{\rm mix}
+\mathcal R_A.
\]

Logo:

\[
\boxed{
\eta_R
=
\left[
\frac{\partial \mathcal R_{\rm GDQ}}
{\partial (e^{-2A}R[h])}
\right]_{g_*,f_*}.
}
\]

Essa definição é independente de coordenadas. Ela depende apenas da convenção
de normalização da curvatura complexa na ação oficial.

---

## 4. Resultado sob convenções usuais

Há duas convenções comuns.

### Convenção A — scalar Kähler já normalizado como scalar real projetado

Se a ação oficial usa \(\mathcal R\) já normalizado para que a projeção real do
bloco externo seja exatamente \(R[h]\), então:

\[
\boxed{\eta_R=1.}
\]

Essa é a convenção mais limpa para a redução Einstein--Hilbert:

\[
\mathcal S_{\mathcal R}
\to
\frac{\hbar}{\Lambda_C^2}
\mathcal V_{\rm eff}^{(G)}
\int_N R[h]\sqrt{-h}\,d^4x.
\]

### Convenção B — scalar Kähler como metade do scalar real

Em muitas convenções de geometria Kähler, a contração complexa

\[
g^{i\bar j}R_{i\bar j}
\]

corresponde a metade do escalar real do espaço Riemanniano associado,
dependendo da normalização do elemento de linha. Nesse caso:

\[
\mathcal R_{\rm real}
=
2\mathcal R_{\rm Kähler},
\]

e a projeção para \(R[h]\) exige:

\[
\boxed{\eta_R=\frac12}
\]

se \(\mathcal R_{\rm GDQ}\) for a curvatura Kähler nua, ou:

\[
\boxed{\eta_R=2}
\]

se a ação tiver sido escrita com a curvatura real mas a métrica Hermitiana
tiver sido normalizada sem o fator \(2\).

Portanto, o número isolado não deve ser escolhido abstratamente; ele deve ser
lido da convenção exata da ação oficial.

---

## 5. Como fixar \(\eta_R\) sem circularidade

O procedimento correto é:

1. escolher a convenção explícita para:

   \[
   ds^2
   =
   g_{\mu\bar\nu}dz^\mu d\bar z^\nu
   \quad
   \text{ou}
   \quad
   ds^2
   =
   2g_{\mu\bar\nu}dz^\mu d\bar z^\nu;
   \]

2. inserir o bloco externo:

   \[
   g_{\mu\bar\nu}^{\rm ext}
   =
   \kappa_H e^{2A}h_{\mu\nu};
   \]

3. calcular \(R_{\mu\bar\nu}\) mantendo apenas derivadas externas de
   \(h_{\mu\nu}\);

4. contrair com \(g^{\mu\bar\nu}\);

5. comparar o termo resultante com:

   \[
   e^{-2A}R[h].
   \]

O coeficiente obtido é \(\eta_R\).

---

## 6. Decisão provisória para Q38

Até a convenção do manuscrito ser conferida linha a linha, a forma correta de
prosseguir é manter:

\[
\boxed{
\eta_R\in\{1,\tfrac12,2\}
\text{ como fator de convenção, não como parâmetro livre.}
}
\]

Mas para todos os cálculos estruturais de Q38, podemos usar a convenção
normalizada:

\[
\boxed{\eta_R=1}
\]

desde que o texto registre explicitamente:

\[
\text{“a curvatura }\mathcal R\text{ da ação está normalizada para projetar em }R[h]\text{ no setor real físico.”}
\]

Se a auditoria da ação oficial mostrar a convenção Kähler nua, então o valor
de \(\eta_R\) deve ser alterado por fator fixo de convenção, e não ajustado
para reproduzir \(G\).

---

## 7. Próximo passo

Com \(\eta_R\) tratado como fator de convenção, o próximo objeto físico real é
o warp térmico/cosmológico:

\[
e^{2A(y,\tau)}.
\]

Produto seguinte:

\[
\boxed{
\texttt{questoes/q38/associados/warp\_termico\_einstein.md}
}
\]

Esse arquivo deve derivar como a temperatura do espaço de Einstein
\(T^5\times S^3\) entra na medida:

\[
\eta_R e^{2A}\mathcal U_*\sqrt{q_*}.
\]

