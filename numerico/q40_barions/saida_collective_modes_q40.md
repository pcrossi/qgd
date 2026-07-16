# Q40 — Refinamento dos modos coletivos de superfície

## 1. Definição

Este relatório avalia explicitamente, no modelo reduzido da Q40, os acoplamentos
dos modos coletivos da borda:

\[
\mathcal I_\Sigma(q)
=
-
J_\Sigma^\dagger(q)K_\Sigma^-1(q)J_\Sigma(q).
\]

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
\qquad
x=\frac{q^2}{\Lambda_E^2},
\qquad
\Lambda_E=4.120110733\,\mathrm{fm}^{-1}.
\]

## 2. Modos avaliados

\[
j_0=1.712091781054,
\qquad
j_1=1.341454657186,
\qquad
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

Interpretação:

1. \(j_0\): modo normal de deslocamento da casca;
2. \(j_1\): modo de cisalhamento/magnetização;
3. \(j_2\): modo torsional não local.

## 3. Baixa energia

\[
G_E^{n,\rm full}(0)=-2.121783651554e-16.
\]

\[
\langle r_n^2\rangle_{\rm var}
=-0.117721790046\,\mathrm{fm}^2,
\qquad
\langle r_n^2\rangle_{\rm full}
=-0.117721790045\,\mathrm{fm}^2.
\]

Diferença:

\[
\Delta\langle r_n^2\rangle=+8.284e-13\,\mathrm{fm}^2.
\]

## 4. Métricas contra Galster

| Curva | Intervalo \(q\) | RMS | RMS relativo |
|---|---:|---:|---:|
| Superfície escalar | 0.25–2.0 | 3.320330e-03 | 12.680% |
| Superfície escalar | 0.25–4.0 | 1.386907e-02 | 33.010% |
| Superfície escalar | 0.50–4.0 | 1.435436e-02 | 33.015% |
| Modos coletivos refinados | 0.25–2.0 | 1.437846e-03 | 5.491% |
| Modos coletivos refinados | 0.25–4.0 | 1.755457e-03 | 4.178% |
| Modos coletivos refinados | 0.50–4.0 | 1.815911e-03 | 4.177% |

## 5. Amostra

| q (fm^-1) | GDQ refinada | Galster | \(\mathcal I_\Sigma\) |
|---:|---:|---:|---:|
| 0.00 | -2.121783652e-16 | +0.000000000e+00 | -0.000000000e+00 |
| 0.25 | +1.211985446e-03 | +1.304265250e-03 | -6.386079337e-05 |
| 0.50 | +4.684504265e-03 | +5.053469782e-03 | -1.009102653e-03 |
| 1.00 | +1.651628966e-02 | +1.785390119e-02 | -1.538200245e-02 |
| 2.00 | +4.423511564e-02 | +4.550430080e-02 | -2.068589761e-01 |
| 3.00 | +5.734780402e-02 | +5.469824591e-02 | -8.265341744e-01 |
| 4.00 | +4.305878443e-02 | +4.815944018e-02 | -2.015361222e+00 |
| 6.00 | -1.181851398e-02 | +2.663124558e-02 | -6.163842787e+00 |
| 8.00 | -6.764785559e-03 | +1.340259138e-02 | -1.252416528e+01 |

## 6. Veredito

O refinamento por modos coletivos:

1. preserva \(G_E^n(0)=0\);
2. preserva \(\langle r_n^2\rangle\);
3. implementa \(\mathcal I_\Sigma=-J^\dagger K^-1J\);
4. reduz o desvio de forma para a escala de poucos por cento no intervalo
   \(0.25\le q\le4\,\mathrm{fm}^{-1}\);
5. transforma a pendência da Q40 em comparação experimental fina, não em falta
   estrutural.

Figuras:

- `/home/pedro/Dropbox/obs/todo/numerico/figs/neutron_collective_modes_curve_q40.png`;
- `/home/pedro/Dropbox/obs/todo/numerico/figs/neutron_collective_modes_impedance_q40.png`.
