# Q40 — Diagnóstico da impedância coletiva requerida

## 1. Definição

Este relatório calcula a impedância escalar efetiva que seria necessária para
levar a curva variacional GDQ até uma referência Galster:

\[
D_{\rm req}(q)=\frac{G_E^{n,\rm var}(q^2)}{G_E^{n,\rm Galster}(q^2)}.
\]

Subtraindo o operador bi-Helmholtz mínimo:

\[
D_\Sigma(q)=\left(1+\frac{q^2}{\Lambda_E^2}\right)^2,
\]

obtemos:

\[
\mathcal I_\Sigma^{\rm req}(q)=D_{\rm req}(q)-D_\Sigma(q).
\]

Isso não é adotado como teoria. É um diagnóstico da forma e da escala que a
Hessiana coletiva de superfície precisa produzir.

## 2. Base diagnóstica

Foi usada uma base que começa em \(q^4\), preservando carga e inclinação:

\[
\mathcal I_\Sigma(q)
=
a\frac{x^2}{1+x}
+b\frac{x^2}{(1+x)^2}
+c\frac{x^3}{(1+x)^2},
\qquad
x=\frac{q^2}{\Lambda_E^2}.
\]

Coeficientes no intervalo \(0.25\le q\le4\,\mathrm{fm}^{-1}\):

\[
a=-2.931258267,
\qquad
b=-1.799500597,
\qquad
c=-1.131757669.
\]

## 3. Métricas

| Intervalo | Superfície escalar | Impedância diagnóstica |
|---|---:|---:|
| \(0.25\le q\le2.0\) | 12.680% | 5.491% |
| \(0.25\le q\le4.0\) | 33.010% | 4.178% |

## 4. Amostra

| q (fm^-1) | GDQ + impedância diagnóstica | Galster | \(\mathcal I_\Sigma\) |
|---:|---:|---:|---:|
| 0.25 | +1.211985446e-03 | +1.304265250e-03 | -6.386079337e-05 |
| 0.50 | +4.684504265e-03 | +5.053469782e-03 | -1.009102653e-03 |
| 1.00 | +1.651628966e-02 | +1.785390119e-02 | -1.538200245e-02 |
| 2.00 | +4.423511564e-02 | +4.550430080e-02 | -2.068589761e-01 |
| 3.00 | +5.734780402e-02 | +5.469824591e-02 | -8.265341744e-01 |
| 4.00 | +4.305878443e-02 | +4.815944018e-02 | -2.015361222e+00 |
| 6.00 | -1.181851398e-02 | +2.663124558e-02 | -6.163842787e+00 |

## 5. Leitura

A impedância requerida começa em \(q^4\), portanto pode preservar carga e raio.
Sua magnitude é de ordem geométrica, não de ordem
\((\alpha_{\rm tor}^{(2)})^2\). Isso explica por que a Hessiana EMT mínima
foi insuficiente: a correção necessária é coletiva da superfície, não apenas
mistura perturbativa local entre \(E\), \(M\) e torção.

Figuras:

- `/home/pedro/Dropbox/obs/todo/numerico/figs/neutron_required_impedance_q40.png`;
- `/home/pedro/Dropbox/obs/todo/numerico/figs/neutron_impedance_diagnostic_curve_q40.png`.
