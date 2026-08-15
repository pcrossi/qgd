---
title: "Output — neutron torsional profile"
---

# Output — neutron torsional profile

## Variational profile

$$
H_n(\xi,\tau_n)
=
|\mu_n|
\left[K_{\tau_n}(\xi,\xi_+)-K_{\tau_n}(\xi,\xi_-)\right].
$$

| quantity | value |
|---|---:|
| $r_p$ | `0.840778765431` fm |
| $\mu_n$ | `-1.912810907182` $\mu_N$ |
| $\alpha_{\rm tor}^{(2)}$ | `0.043530268983` |
| $\xi_+$ | `-0.018299662907` fm |
| $\xi_-$ | `+0.018299662907` fm |
| $\sigma_r$ | `0.018299662907` fm |
| $\tau_n$ | `1.674388312580e-04` fm$^2$ |

## Verifications

- $\int H_n d\xi = -9.535541374287e-18$;
- $G_E^n(0) = -9.535541374287e-18$;
- $\langle r_n^2\rangle$ by moment = `-0.117721789532` fm$^2$;
- analytical expression = `-0.117721789532` fm$^2$;
- slope $-6dG_E^n/dq^2|_0$ = `-0.117721789530` fm$^2$.

## Sample of the leading curve

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

## Verdict

The smooth profile preserves zero total charge, fixes the low-energy slope, and provides a leading surface curve. The complete shape at intermediate $q$ requires the collective impedance of the probe.
