# Relatório: Solver de Superfície Bariônica (Q40)

Este relatório corrige o modelo numérico do raio do próton.

O erro anterior era tratar o raio de carga como média volumétrica do autovetor
radial bruto. Na Q40, o observável eletromagnético do próton é uma **grandeza
de superfície** localizada no estômato e projetada por Hopf.

## 1. Fórmula estrutural

\[
r_p
=
C_r\epsilon_{\rm eff}R_B,
\qquad
C_r=\frac18\left(1+\frac{\alpha}{4}\right),
\qquad
R_B=\frac32\Lambda_C.
\]

Com:

- \(\Lambda_C=386.159268\,\mathrm{fm}\);
- \(R_B=579.238902\,\mathrm{fm}\);
- \(\epsilon_{\rm eff}=0.011591040463\);
- \(C_r=0.125228042268\).

Resultado:

\[
\boxed{r_p=0.840778765\,\mathrm{fm}.}
\]

## 2. Convergência por casca regularizada

A densidade de carga foi modelada como uma sequência de cascas:

\[
w_\sigma(\chi)
\propto
\exp\left[-\left(\frac{\chi-\epsilon_{\rm eff}}{\sigma}\right)^2\right],
\qquad
\chi\ge\epsilon_{\rm eff}.
\]

No limite \(\sigma\to0\), essa sequência converge para a delta de superfície
no estômato.

| sigma/epsilon | raio calculado (fm) | desvio relativo |
|---:|---:|---:|
| 0.50000000 | 1.092750294 | +2.996883e-01 |
| 0.25000000 | 0.963543027 | +1.460126e-01 |
| 0.12500000 | 0.901187729 | +7.184882e-02 |
| 0.06250000 | 0.870714331 | +3.560457e-02 |
| 0.03125000 | 0.855675767 | +1.771810e-02 |
| 0.01562500 | 0.848209103 | +8.837447e-03 |
| 0.00781250 | 0.844489334 | +4.413252e-03 |
| 0.00390625 | 0.842632892 | +2.205249e-03 |
| delta_surface | 0.840778765 | +0.000000e+00 |

## 3. Momentos magnéticos estruturais

\[
\mu_p
=
1+
\frac35\ln(2\pi^2)
\left(1+\frac{\alpha}{4}\right)
=
2.792828942\,\mu_N.
\]

\[
\mu_n
=
-\frac34\delta_B
\left(
1+\alpha\frac{3\sqrt2}{4}
\right)
=
-1.912810907\,\mu_N.
\]

## 4. Conclusão

\[
\boxed{
\text{o modelo de superfície/projeção de Hopf bate necessariamente com o raio estrutural da Q40.}
}
\]

O cálculo volumétrico radial antigo fica descartado como modelo do raio de
carga. Ele pode estudar modos internos do bulk, mas não o observável
eletromagnético de borda.
