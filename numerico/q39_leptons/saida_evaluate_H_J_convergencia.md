# Convergência da avaliação direta \(H/J\) — Q39

Este arquivo registra a avaliação direta de:

\[
(\Delta_\epsilon,\Delta_b)^T=-H^{-1}J^{(\beta)}
\]

com sinal fermiônico aplicado:

\[
H=-H_{\rm det\ bruto},
\]

e fonte térmica líder de Einstein:

\[
J^{(\beta)}=-\eta_{\rm lead}\odot J_{\rm red},
\qquad
\eta_{\rm lead}=(3/2,3).
\]

## 1. Execução \(N=1600\), \(N_{\rm spec}=40\)

\[
H=
\begin{pmatrix}
1.615800249578\times10^6 & -8.946131163853\times10^3\\
-8.946131163853\times10^3 & 5.164752656128\times10^1
\end{pmatrix}.
\]

\[
J_{\rm red}
=
\begin{pmatrix}
-1.336604148589\times10^1\\
6.981466168382\times10^{-2}
\end{pmatrix}.
\]

\[
J^{(\beta)}
=
\begin{pmatrix}
2.004906222884\times10^1\\
-2.094439850515\times10^{-1}
\end{pmatrix}.
\]

\[
(\Delta_\epsilon,\Delta_b)_{\rm lead}
=
(2.451805090425\times10^{-4},\ 4.652422173431\times10^{-2}).
\]

Razão contra alvo inverso:

\[
\frac{\Delta_\epsilon^{\rm lead}}{\Delta_\epsilon^{\rm alvo}}
=1.030402,
\qquad
\frac{\Delta_b^{\rm lead}}{\Delta_b^{\rm alvo}}
=1.029864.
\]

Fatores requeridos:

\[
\eta_{\rm req}
=(1.471511,\ 2.928914).
\]

## 2. Execução \(N=3200\), \(N_{\rm spec}=40\)

\[
H=
\begin{pmatrix}
1.617018622126\times10^6 & -8.942767340249\times10^3\\
-8.942767340249\times10^3 & 5.170348414651\times10^1
\end{pmatrix}.
\]

\[
J_{\rm red}
=
\begin{pmatrix}
-1.336596563913\times10^1\\
6.981405054607\times10^{-2}
\end{pmatrix}.
\]

\[
J^{(\beta)}
=
\begin{pmatrix}
2.004894845869\times10^1\\
-2.094421516382\times10^{-1}
\end{pmatrix}.
\]

\[
(\Delta_\epsilon,\Delta_b)_{\rm lead}
=
(2.302581968133\times10^{-4},\ 4.387688124645\times10^{-2}).
\]

Razão contra alvo inverso:

\[
\frac{\Delta_\epsilon^{\rm lead}}{\Delta_\epsilon^{\rm alvo}}
=0.967689,
\qquad
\frac{\Delta_b^{\rm lead}}{\Delta_b^{\rm alvo}}
=0.971263.
\]

Fatores requeridos:

\[
\eta_{\rm req}
=(1.438461,\ 2.976614).
\]

## 3. Conclusão técnica

A avaliação direta de \(H\) e \(J^{(\beta)}\) está feita.

O resultado é estável no ponto essencial:

1. \(H\) é positivo após o sinal fermiônico;
2. \(J^{(\beta)}\) tem o sinal correto após o vestimento de Einstein;
3. \(-H^{-1}J^{(\beta)}\) fornece a compensação térmica com sinal correto;
4. a aproximação líder \(\eta_{\rm lead}=(3/2,3)\) fica dentro de alguns por
   cento do alvo inverso;
5. a diferença restante é refinamento sublíder de \(\eta_{\rm req}\), não falta
   de avaliação de \(H/J\).

