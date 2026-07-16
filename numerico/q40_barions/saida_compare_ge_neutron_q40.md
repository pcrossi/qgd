# Q40 — Comparação de \(G_E^n\) variacional com Galster

Este relatório compara a curva variacional líder da GDQ para o fator de forma
elétrico do nêutron com a parametrização de Galster. Galster é usado aqui
somente como referência fenomenológica compacta; nenhum parâmetro da GDQ é
ajustado por ela.

## 1. Entrada GDQ

- \(r_p=0.840778765432\\,\\mathrm{fm}\);
- \(\mu_n=-1.912810907194\\,\\mu_N\);
- \(\alpha_{\\rm tor}^{(2)}=0.043530269017\);
- \(\tau_n=1.674388315199e-04\\,\\mathrm{fm}^2\).

## 2. Referência Galster

Foi usada a forma:

\\[
G_E^n(Q^2)
=
-\mu_n
\\frac{\\tau}{1+\\eta\\tau}
G_D(Q^2),
\\qquad
\\tau=\\frac{Q^2}{4M_N^2},
\\qquad
G_D=(1+Q^2/0.71)^{-2},
\\]

com \(\eta=5.6\), \(M_N=0.93956542052\\,\\mathrm{GeV}\) e
\(Q^2=(\\hbar c q)^2\).

## 3. Métricas de forma

Além da curva nua, foi testado o operador de sonda/superfície:

\[
F_\Sigma(q)=\left(1+\frac{q^2}{\Lambda_\Sigma^2}\right)^{-2},
\qquad
\Lambda_\Sigma=\frac{\sqrt{12}}{r_p}
=4.120110733\,\mathrm{fm}^{-1}
=0.813009010\,\mathrm{GeV}.
\]

Como \(F_\Sigma(0)=1\), esse fator não altera \(G_E^n(0)\) nem a inclinação em
\(q=0\). Ele só representa a resposta finita da superfície composta em
transferência intermediária.

| Intervalo | RMS nu | RMS rel. nu | RMS sonda | RMS rel. sonda |
|---|---:|---:|---:|---:|
| 0.0 <= q <= 2.0 fm^-1 | 4.554086e-03 | 18.586% | 3.107019e-03 | 12.680% |
| 0.0 <= q <= 4.0 fm^-1 | 2.060912e-02 | 50.656% | 1.342979e-02 | 33.009% |
| 0.5 <= q <= 4.0 fm^-1 | 2.202811e-02 | 50.665% | 1.435436e-02 | 33.015% |

## 4. Picos

- GDQ nua: \(q=3.260\\,\\mathrm{fm}^{-1}\),
  \(G_E^n=0.088420819\);
- GDQ + sonda: \(q=2.440\\,\\mathrm{fm}^{-1}\),
  \(G_E^n=0.040799346\);
- Galster: \(q=2.960\\,\\mathrm{fm}^{-1}\),
  \(G_E^n=0.054711709\).

## 5. Amostra

| q (fm^-1) | GDQ nua | GDQ + sonda | Galster | Dif. sonda |
|---:|---:|---:|---:|---:|
| 0.00 | -2.121783652e-16 | -2.121783652e-16 | +0.000000000e+00 | -2.121783652e-16 |
| 0.25 | +1.220849095e-03 | +1.211908614e-03 | +1.304265250e-03 | -9.235663563e-05 |
| 0.50 | +4.818773065e-03 | +4.679913338e-03 | +5.053469782e-03 | -3.735564438e-04 |
| 1.00 | +1.826547097e-02 | +1.628971672e-02 | +1.785390119e-02 | -1.564184463e-03 |
| 2.00 | +5.838761522e-02 | +3.824189573e-02 | +4.550430080e-02 | -7.262405067e-03 |
| 3.00 | +8.687744185e-02 | +3.710402443e-02 | +5.469824591e-02 | -1.759422148e-02 |
| 4.00 | +7.570254451e-02 | +2.006172126e-02 | +4.815944018e-02 | -2.809771892e-02 |
| 6.00 | -4.225228608e-02 | -4.338491104e-03 | +2.663124558e-02 | -3.096973669e-02 |
| 8.00 | -6.920687639e-02 | -3.041441983e-03 | +1.340259138e-02 | -1.644403336e-02 |

## 6. Leitura física

A curva GDQ nua acerta automaticamente a carga nula e o raio quadrático
negativo por construção variacional do perfil torsional. O operador
bi-Helmholtz de superfície reduz a oscilação intermediária sem tocar nos
vínculos de baixa energia. A pendência que sobra é derivar a forma completa do
operador de sonda/magnetização a partir da Hessiana eletromagnética da ação
GDQ, em vez de manter apenas seu fator líder de superfície.

Figura gerada:

`/home/pedro/Dropbox/obs/todo/numerico/figs/neutron_ge_gdq_vs_galster_q40.png`
