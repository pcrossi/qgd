# Relatório: solução variacional de H_n(chi) — Q40

## 1. Equação variacional

O perfil torsional do nêutron é tratado como solução do fluxo de calor de
Perelman na camada local de superfície:

\[
H_n(\xi,\tau_n)
=
|\mu_n|
\left[
K_{\tau_n}(\xi,\xi_+)-K_{\tau_n}(\xi,\xi_-)
\right].
\]

Com:

\[
K_\tau(\xi,\xi_0)
=
\frac{1}{\sqrt{4\pi\tau}}
\exp\left[-\frac{(\xi-\xi_0)^2}{4\tau}\right].
\]

## 2. Parâmetros derivados

- \(r_p=0.840778765432\,\mathrm{fm}\);
- \(|\mu_n|=1.912810907194\);
- \(\alpha_{\rm tor}^{(2)}=0.043530269017\);
- \(\xi_+=-0.018299662921\,\mathrm{fm}\);
- \(\xi_-=+0.018299662921\,\mathrm{fm}\);
- \(\sigma_r=0.018299662921\,\mathrm{fm}\);
- \(\tau_n=1.674388315199e-04\,\mathrm{fm}^2\).

## 3. Verificações

\[
\int H_n d\xi=-2.121783651554e-16.
\]

\[
G_E^n(0)=-2.121783651554e-16.
\]

Momento direto:

\[
\langle r_n^2\rangle=-0.117721789624\,\mathrm{fm}^2.
\]

Forma analítica:

\[
-2|\mu_n|\alpha_{\rm tor}^{(2)}r_p^2
=-0.117721789624\,\mathrm{fm}^2.
\]

Inclinação:

\[
-6\left.\frac{dG_E^n}{dq^2}\right|_0
=-0.117721790046\,\mathrm{fm}^2.
\]

## 4. Amostra da curva

| q (fm^-1) | G_E^n(q^2) |
|---:|---:|
| 0.00 | -2.121783651554e-16 |
| 0.25 | +1.220849095018e-03 |
| 0.50 | +4.818773065375e-03 |
| 1.00 | +1.826547097046e-02 |
| 2.00 | +5.838761521950e-02 |
| 4.00 | +7.570254451481e-02 |
| 6.00 | -4.225228608004e-02 |
| 8.00 | -6.920687638684e-02 |

## 5. Status

O perfil \(H_n(\chi)\) foi obtido por solução variacional líder do setor de
contorno. A curva \(G_E^n(q^2)\) fica determinada sem usar o raio experimental
do nêutron como entrada.

Próxima etapa, se desejada: comparar essa curva com parametrizações
experimentais de espalhamento elástico e acrescentar correções de sonda/magnetização.
