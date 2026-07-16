# Q40 — Hessiana reduzida da sonda eletromagnética/magnética

## 1. Objetivo

Este relatório implementa o primeiro solver da resposta linear:

\[
H_\Sigma(q)\delta\Phi(q)=J_{\rm em}(q),
\qquad
\Phi=(\rho_E,\rho_M,T_\Sigma).
\]

A curva física é:

\[
G_E^{n,\rm phys}(q^2)
=
F_{\rm EMT}(q)G_E^{n,\rm var}(q^2),
\]

onde \(F_{\rm EMT}\) é obtido pelo complemento de Schur da Hessiana reduzida.
Galster é usado apenas como benchmark externo de forma.

## 2. Hessiana mínima

\[
H_\Sigma=
\begin{pmatrix}
D_E & C_{EM} & C_{ET}\\
C_{EM} & D_M & C_{MT}\\
C_{ET} & C_{MT} & D_T
\end{pmatrix}.
\]

Com:

\[
D_E=(1+q^2/\Lambda_E^2)^2,
\qquad
D_M=1+q^2/\Lambda_M^2,
\qquad
D_T=1+q^2/\Lambda_T^2.
\]

Os acoplamentos cruzados são proporcionais a \(q^2\), de modo que a carga e a
inclinação no zero sejam preservadas:

\[
C_{ij}\propto q^2.
\]

Escalas usadas:

- \(\Lambda_E=4.120110733\,\mathrm{fm}^{-1}\);
- \(\Lambda_M=4.978460168\,\mathrm{fm}^{-1}\);
- \(\Lambda_T=54.645815297\,\mathrm{fm}^{-1}\).

## 3. Baixa energia

\[
G_E^{n,\rm var}(0)=-2.121783651554e-16,
\qquad
G_E^{n,\rm EMT}(0)=-2.121783651554e-16.
\]

\[
\langle r_n^2\rangle_{\rm var}
=-0.117721790046\,\mathrm{fm}^2,
\qquad
\langle r_n^2\rangle_{\rm EMT}
=-0.117721790045\,\mathrm{fm}^2.
\]

Diferença:

\[
\Delta\langle r_n^2\rangle=+4.420e-13\,\mathrm{fm}^2.
\]

## 4. Comparação fenomenológica

### GDQ nua

| Intervalo | RMS | RMS relativo |
|---|---:|---:|
| 0.0 <= q <= 2.0 fm^-1 | 4.554086e-03 | 18.586% |
| 0.0 <= q <= 4.0 fm^-1 | 2.060912e-02 | 50.656% |
| 0.5 <= q <= 4.0 fm^-1 | 2.202811e-02 | 50.665% |

### GDQ + superfície escalar

| Intervalo | RMS | RMS relativo |
|---|---:|---:|
| 0.0 <= q <= 2.0 fm^-1 | 3.107019e-03 | 12.680% |
| 0.0 <= q <= 4.0 fm^-1 | 1.342979e-02 | 33.009% |
| 0.5 <= q <= 4.0 fm^-1 | 1.435436e-02 | 33.015% |

### GDQ + Hessiana EMT

| Intervalo | RMS | RMS relativo |
|---|---:|---:|
| 0.0 <= q <= 2.0 fm^-1 | 3.106778e-03 | 12.679% |
| 0.0 <= q <= 4.0 fm^-1 | 1.342853e-02 | 33.006% |
| 0.5 <= q <= 4.0 fm^-1 | 1.435301e-02 | 33.012% |


## 5. Amostra

| q (fm^-1) | GDQ nua | GDQ + Hessiana EMT | Galster | Diferença EMT |
|---:|---:|---:|---:|---:|
| 0.00 | -2.121783652e-16 | -2.121783652e-16 | +0.000000000e+00 | -2.121783652e-16 |
| 0.25 | +1.220849095e-03 | +1.211908624e-03 | +1.304265250e-03 | -9.235662555e-05 |
| 0.50 | +4.818773065e-03 | +4.679913943e-03 | +5.053469782e-03 | -3.735558390e-04 |
| 1.00 | +1.826547097e-02 | +1.628974677e-02 | +1.785390119e-02 | -1.564154419e-03 |
| 2.00 | +5.838761522e-02 | +3.824263961e-02 | +4.550430080e-02 | -7.261661188e-03 |
| 3.00 | +8.687744185e-02 | +3.710606112e-02 | +5.469824591e-02 | -1.759218478e-02 |
| 4.00 | +7.570254451e-02 | +2.006351843e-02 | +4.815944018e-02 | -2.809592176e-02 |
| 6.00 | -4.225228608e-02 | -4.339009214e-03 | +2.663124558e-02 | -3.097025480e-02 |
| 8.00 | -6.920687639e-02 | -3.041784238e-03 | +1.340259138e-02 | -1.644437561e-02 |

## 6. Leitura

A Hessiana EMT mínima preserva os vínculos de baixa energia, mas seus
acoplamentos torsionais geométricos são pequenos. Portanto, ela não substitui
sozinha o operador completo de sonda. O resultado separa claramente:

1. vínculos estruturais já fechados: carga e raio;
2. resposta escalar de superfície: melhora parcial;
3. mistura EMT mínima: correção perturbativa pequena;
4. pendência real: calcular os coeficientes de \(H_\Sigma\) diretamente da
   Hessiana completa da ação GDQ no setor de contorno.

Figuras:

- `/home/pedro/Dropbox/obs/todo/numerico/figs/neutron_ge_probe_response_q40.png`;
- `/home/pedro/Dropbox/obs/todo/numerico/figs/neutron_probe_filters_q40.png`.
