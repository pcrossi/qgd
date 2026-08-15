---
title: "Output — symbolic derivation of rho Lambda"
---

# Output — symbolic derivation of rho Lambda

Classification: symbolic/dimensional verification of the reduced structural formula.

## 1. Algebraic chain

$$
V_p=\frac{4\pi}{3}r_p^3
$$

$$
\rho_{\rm UV}^{p}=\frac{M_pc^2}{V_p}
$$

The asymptotic weight of the neck is:

$$
f(r)\sim\ln\left(\frac{r}{r_p}\right),\qquad e^{-f}=\frac{r_p}{r}
$$

Hence the preserved dilution scale is:

$$
\rho_{\rm diluted}\propto\frac{r_p}{R_H}
$$

The antisymmetric count in eight dimensions is:

$$
N_{\rm Cartan}=\dim\Lambda^2(\mathbb R^8)=\binom82=28
$$

Therefore:

$$
\rho_\Lambda^{\rm GDQ}=\alpha^2N_{\rm Cartan}\rho_{\rm UV}^{p}\frac{r_p}{R_H}\frac{1}{c^2}
$$

## 2. Explicit cancellation of $c^2$

Substituting $\rho_{\rm UV}^{p}$:

$$
\rho_\Lambda^{\rm GDQ}=\alpha^2N_{\rm Cartan}\frac{M_pc^2}{(4\pi/3)r_p^3}\frac{r_p}{R_H}\frac{1}{c^2}
$$

Therefore:

$$
\rho_\Lambda^{\rm GDQ}=\alpha^2N_{\rm Cartan}\frac{M_p}{(4\pi/3)r_p^3}\frac{r_p}{R_H}
$$

## 3. Dimensional verification

| Quantity | Dimension |
|---|---:|
| $M_p$ | `kg` |
| $c^2$ | `m^2 s^-2` |
| $M_pc^2$ | `kg m^2 s^-2` |
| $V_p$ | `m^3` |
| $\rho_{\rm UV}^p$ | `kg m^-1 s^-2` |
| $r_p/R_H$, $\alpha^2$, $N_{\rm Cartan}$ | `1` |
| $\rho_\Lambda^{\rm GDQ}$ before dividing by $c^2$ | `kg m^-1 s^-2` |
| $\rho_\Lambda^{\rm GDQ}$ final | `kg m^-3` |

## 4. Status

The symbolic derivation confirms the algebraic structure, the count of 28, and the final dimension of kg/m^3. The metrological evaluation depends on $R_H=c/H_0$ as a cosmological boundary.
