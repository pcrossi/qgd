# Output — reduced detector response by Schur

Classification: effective reduction/apparatus.

## Impedance matrix

$$
\text{R}_{\rm app}
=
\begin{pmatrix}
1.876086956522 & 0.132608695652 \\
0.132608695652 & 1.446530100334
\end{pmatrix}.
$$

## Verifications

| test | value |
|---|---:|
| minimum eigenvalue of R_app | 1.408890543061 |
| maximum eigenvalue of R_app | 1.913726513796 |
| Gamma_det | 1.528699832776 |
| C_det = exp(-Gamma_det) | 0.216817382993 |

Interpretation: the positive detector response reduces the coherence by
$\mathcal C_{\rm det}=e^{-\Gamma_{\rm det}}$. The numbers are from a toy model.
