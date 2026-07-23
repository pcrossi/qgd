# Q43 — Referências experimentais externas para \(g-2\)

Estas referências são comparação experimental/metrológica externa. Elas não
substituem a derivação GDQ pela Hessiana oficial.

## 1. Medição moderna do momento magnético do elétron

Referência:

- X. Fan, T. G. Myers, B. A. D. Sukra, G. Gabrielse,
  *Measurement of the Electron Magnetic Moment*,
  arXiv:2209.13084.

Link:

- <https://arxiv.org/abs/2209.13084>

Valor relevante reportado:

\[
-\frac{\mu}{\mu_B}
=
\frac{g}{2}
=
1.00115965218059(13).
\]

Portanto, em módulo:

\[
g_e
\simeq
2.00231930436118.
\]

Esse valor é compatível, na precisão usada localmente, com o valor de
referência empregado no script da Q43:

\[
g_e\simeq2.00231930436092.
\]

## 2. CODATA 2022

Referência:

- P. J. Mohr, D. B. Newell, B. N. Taylor, E. Tiesinga,
  *CODATA Recommended Values of the Fundamental Physical Constants: 2022*,
  arXiv:2409.03787.

Link:

- <https://arxiv.org/abs/2409.03787>

Uso na Q43:

- referência externa para constantes fundamentais;
- comparação metrológica;
- auditoria futura dos valores de \(\alpha\), \(g_e\), \(g_\mu\) e constantes
  associadas.

## 3. Múon \(g-2\)

Referência primária usada para diagnóstico local:

- D. P. Aguillard et al.,
  *Measurement of the Positive Muon Anomalous Magnetic Moment to 0.20 ppm*,
  arXiv:2308.06230.

Link:

- <https://arxiv.org/abs/2308.06230>

Valor relevante reportado:

\[
a_\mu({\rm Exp})
=
116\,592\,059(22)\times10^{-11}.
\]

Isto equivale a:

\[
a_\mu({\rm Exp})
=0.00116592059(22).
\]

Uso na Q43:

- comparação metrológica externa;
- diagnóstico do tamanho que a resposta \(H_{C,\mu}^{-1}m_{\perp,\mu}\) deve
  produzir;
- não usar como ajuste de coeficientes.

Observação: resultados finais posteriores do Fermilab devem ser auditados em
fonte primária antes de substituir este valor no arquivo canônico.

## 4. Status na GDQ

O valor líder calculado na Q43 é:

\[
g_{\rm GDQ}^{(1)}
=
2\left(1+\frac{\alpha}{2\pi}\right).
\]

Para \(\alpha^{-1}=137.035999177\):

\[
g_{\rm GDQ}^{(1)}
=
2.002322819464196.
\]

O resíduo em relação ao elétron é:

\[
\Delta g
=
g_e-g_{\rm GDQ}^{(1)}
\simeq
-3.5\times10^{-6}.
\]

Esse resíduo deve ser explicado pelas ordens superiores da resposta GDQ:

\[
H_C^{-1}m_\perp.
\]

Não deve ser usado para ajustar coeficientes.
