---
title: "Saída — perfil torsional do nêutron"
---

# Saída — perfil torsional do nêutron

## Perfil variacional

$$
H_n(\xi,\tau_n)
=
|\mu_n|
\left[K_{\tau_n}(\xi,\xi_+)-K_{\tau_n}(\xi,\xi_-)\right].
$$

| quantidade | valor |
|---|---:|
| $r_p$ | `0.840778765431` fm |
| $\mu_n$ | `-1.912810907182` $\mu_N$ |
| $\alpha_{\rm tor}^{(2)}$ | `0.043530268983` |
| $\xi_+$ | `-0.018299662907` fm |
| $\xi_-$ | `+0.018299662907` fm |
| $\sigma_r$ | `0.018299662907` fm |
| $\tau_n$ | `1.674388312580e-04` fm$^2$ |

## Verificações

- $\int H_n d\xi = -9.535541374287e-18$;
- $G_E^n(0) = -9.535541374287e-18$;
- $\langle r_n^2\rangle$ por momento = `-0.117721789532` fm$^2$;
- expressão analítica = `-0.117721789532` fm$^2$;
- inclinação $-6dG_E^n/dq^2|_0$ = `-0.117721789530` fm$^2$.

## Amostra da curva líder

| $q$ fm$^{-1}$ | $G_E^n(q^2)$ |
|---:|---:|
| `0.00` | `-9.535541374287e-18` |
| `0.25` | `+1.220849094054e-03` |
| `0.50` | `+4.818773061570e-03` |
| `1.00` | `+1.826547095605e-02` |
| `2.00` | `+5.838761517349e-02` |
| `4.00` | `+7.570254445558e-02` |
| `6.00` | `-4.225228604709e-02` |
| `8.00` | `-6.920687633393e-02` |

## Veredito

O perfil suave preserva carga total nula, fixa a inclinação de baixa
energia e fornece uma curva líder de superfície. A forma completa em
$q$ intermediário exige a impedância coletiva da sonda.
