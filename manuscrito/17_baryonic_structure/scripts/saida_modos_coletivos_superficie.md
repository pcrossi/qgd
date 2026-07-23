---
title: "Saída — modos coletivos de superfície"
---

# Saída — modos coletivos de superfície

## Complemento de Schur de superfície

$$
\mathcal I_\Sigma(q)
=
-J_\Sigma^\dagger(q)K_\Sigma^{-1}(q)J_\Sigma(q).
$$

$$
J_\Sigma(q)
=
x
\begin{pmatrix}
j_0\\
j_1\\
j_2\sqrt{x}
\end{pmatrix},
\qquad
x=\frac{q^2}{\Lambda_E^2}.
$$

- $\Lambda_E=4.120110733\,\mathrm{fm}^{-1}$;
- $j_0=1.712091781001$;
- $j_1=1.341454668572$;
- $j_2=1.063840983764$.

## Baixa energia

- $G_E^{n,\rm full}(0)=-5.055092629214e-17$;
- $\langle r_n^2\rangle_{\rm var}=-0.117721789846\,\mathrm{fm}^2$;
- $\langle r_n^2\rangle_{\rm full}=-0.117721789845\,\mathrm{fm}^2$.

## Métricas contra Galster

| curva | intervalo $q$ | RMS | RMS relativo |
|---|---:|---:|---:|
| superfície escalar | `0.25`–`2.0` | `3.320331e-03` | `12.680%` |
| superfície escalar | `0.25`–`4.0` | `1.386907e-02` | `33.010%` |
| superfície escalar | `0.50`–`4.0` | `1.435436e-02` | `33.015%` |
| modos coletivos | `0.25`–`2.0` | `1.437846e-03` | `5.491%` |
| modos coletivos | `0.25`–`4.0` | `1.755457e-03` | `4.178%` |
| modos coletivos | `0.50`–`4.0` | `1.815911e-03` | `4.177%` |

## Amostra

| $q$ fm$^{-1}$ | GDQ refinada | Galster | $\mathcal I_\Sigma$ |
|---:|---:|---:|---:|
| `0.00` | `-5.055092629e-17` | `+0.000000000e+00` | `-0.000000000e+00` |
| `0.25` | `+1.211985445e-03` | `+1.304265250e-03` | `-6.386079377e-05` |
| `0.50` | `+4.684504261e-03` | `+5.053469782e-03` | `-1.009102659e-03` |
| `1.00` | `+1.651628964e-02` | `+1.785390119e-02` | `-1.538200254e-02` |
| `2.00` | `+4.423511563e-02` | `+4.550430080e-02` | `-2.068589770e-01` |
| `3.00` | `+5.734780404e-02` | `+5.469824591e-02` | `-8.265341760e-01` |
| `4.00` | `+4.305878440e-02` | `+4.815944018e-02` | `-2.015361222e+00` |
| `6.00` | `-1.181851392e-02` | `+2.663124558e-02` | `-6.163842771e+00` |
| `8.00` | `-6.764785518e-03` | `+1.340259138e-02` | `-1.252416523e+01` |

## Veredito

Os modos coletivos preservam carga nula e inclinação de baixa energia.
A comparação com Galster é benchmark de forma: ela informa o tamanho da
resposta de sonda, mas não altera a ação oficial.
