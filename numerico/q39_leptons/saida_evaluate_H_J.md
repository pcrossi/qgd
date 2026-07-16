# Avaliação direta operacional de H e J_beta — Q39

Este arquivo foi gerado por `evaluate_H_J_q39.py`.

## 1. Configuração

| Item | Valor |
| --- | ---: |
| `epsilon_eff` | `1.159104046325e-02` |
| `b_eff` | `1.217978692677e-04` |
| `p0 = (epsilon, ln b)` | `(1.159104046325e-02, -9.013147696539e+00)` |
| `n_grid` | `3200` |
| `n_spec` | `40` |
| `beta` | `6.283185307180e+00` |
| `h_epsilon` | `1.159104046325e-05` |
| `h_ln_b` | `1.000000000000e-03` |
| `eta_lider` | `(1.500000000000e+00, 3.000000000000e+00)` |

## 2. Funcionais no ponto frio

\[
\Gamma_0=1.014984187726e+02
\]

\[
\Gamma_{\rm th}^{\rm red}=6.795967293869e-01
\]

## 3. Hessiana fria

A Hessiana abaixo já inclui o sinal fermiônico:

\[
H=-H_{\rm det\ bruto}.
\]

\[
H=
\begin{pmatrix}
1.617018622126e+06 & -8.942767340249e+03 \\
-8.942767340249e+03 & 5.170348414651e+01
\end{pmatrix}.
\]

Autovalores de \(H\):

\[
\lambda(H)=(1.617068079317e+06, 2.246293176100e+00).
\]

Condicionamento:

\[
\kappa(H)=7.198829148935e+05.
\]

## 4. Fonte térmica

A fonte reduzida radial foi:

\[
J_{\rm red}=
\begin{pmatrix}
-1.336596563913e+01 \\
6.981405054607e-02
\end{pmatrix}.
\]

Aplicando o sinal fermiônico térmico e os fatores líderes de Einstein:

\[
\eta_{\rm lead}=
\begin{pmatrix}
3/2\\
3
\end{pmatrix},
\qquad
J^{(\beta)}=-\eta_{\rm lead}\odot J_{\rm red}.
\]

\[
J^{(\beta)}=
\begin{pmatrix}
2.004894845869e+01 \\
-2.094421516382e-01
\end{pmatrix}.
\]

## 5. Resposta variacional

Status da solução linear: `ok`.

\[
\delta p=-H^{-1}J^{(\beta)}=
\begin{pmatrix}
2.302581968133e-04 \\
4.387688124645e-02
\end{pmatrix}.
\]

Assim:

\[
\Delta_\epsilon^{\rm pred}=2.302581968133e-04,
\]

\[
\Delta_b^{\rm pred}\simeq\Delta_{\ln b}^{\rm pred}=4.387688124645e-02.
\]

## 6. Comparação com o alvo térmico inverso

| Quantidade | Predito por `-H^-1 J` | Alvo inverso | Razão predito/alvo |
| --- | ---: | ---: | ---: |
| \(\Delta_\epsilon\) | `2.302581968133e-04` | `2.379465180000e-04` | `9.676888686947e-01` |
| \(\Delta_b\) | `4.387688124645e-02` | `4.517509510000e-02` | `9.712626204622e-01` |

Razões de massa obtidas ao aplicar `delta_pred`:

\[
r_2=2.078952576940e+02,
\qquad
r_3=3.496089989354e+03.
\]

## 7. Diagnóstico da correção

Resultado cru anterior:

\[
\delta p_{\rm cru}
=
(-1.837243040667e-05, -1.827465239827e-03).
\]

Resultado com apenas o sinal frio fermiônico:

\[
\delta p_{\rm frio}
=
(1.837243040667e-05, 1.827465239827e-03).
\]

Fonte requerida para reproduzir exatamente o alvo inverso:

\[
J_{\rm req}
=
(1.922641437700e+01, -2.078094634237e-01).
\]

Fatores térmicos efetivos requeridos:

\[
\eta_{\rm req}
=
(1.438460556918e+00, 2.976613758954e+00).
\]

Comparação:

\[
\eta_{\rm lead}=(1.5,3.0),
\qquad
\eta_{\rm req}\approx(1.438461,2.976614).
\]

Portanto, os fatores líderes de heat-kernel do espaço de Einstein acertam a
ordem e o sinal, ficando a poucos por cento do alvo. O fechamento exato depende
dos coeficientes sublíderes de curvatura/borda.

## 8. Status

Esta avaliação corrige o erro de sinal da versão espectral pura e inclui o
vestimento térmico líder do espaço de Einstein:

\[
(\Delta_\epsilon,\Delta_b)^T=-H^{-1}J^{(\beta)}.
\]

O problema deixou de ser uma inconsistência de sinal. A pendência restante é
avaliar os coeficientes sublíderes de heat-kernel/curvatura do ciclo de
Einstein ou o termo explícito de borda \(S_\partial^{\rm GDQ}\). Esses
coeficientes devem deslocar \(\eta=(1.5,3.0)\) para \(\eta_{\rm req}\).
