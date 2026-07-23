---
title: "Saída — derivação simbólica de rho Lambda"
---

# Saída — derivação simbólica de rho Lambda

Classificação: verificação simbólica/dimensional da fórmula estrutural reduzida.

## 1. Cadeia algébrica

$$
V_p=\frac{4\pi}{3}r_p^3
$$

$$
\rho_{\rm UV}^{p}=\frac{M_pc^2}{V_p}
$$

O peso assintótico do colar é:

$$
f(r)\sim\ln\left(\frac{r}{r_p}\right),\qquad e^{-f}=\frac{r_p}{r}
$$

Logo a escala de diluição preservada é:

$$
\rho_{\rm diluida}\propto\frac{r_p}{R_H}
$$

A contagem antissimétrica em oito dimensões é:

$$
N_{\rm Cartan}=\dim\Lambda^2(\mathbb R^8)=\binom82=28
$$

Portanto:

$$
\rho_\Lambda^{\rm GDQ}=\alpha^2N_{\rm Cartan}\rho_{\rm UV}^{p}\frac{r_p}{R_H}\frac1{c^2}
$$

## 2. Cancelamento explícito de $c^2$

Substituindo $\rho_{\rm UV}^{p}$:

$$
\rho_\Lambda^{\rm GDQ}=\alpha^2N_{\rm Cartan}\frac{M_pc^2}{(4\pi/3)r_p^3}\frac{r_p}{R_H}\frac1{c^2}
$$

Logo:

$$
\rho_\Lambda^{\rm GDQ}=\alpha^2N_{\rm Cartan}\frac{M_p}{(4\pi/3)r_p^3}\frac{r_p}{R_H}
$$

## 3. Verificação dimensional

| Quantidade | Dimensão |
|---|---:|
| $M_p$ | `kg` |
| $c^2$ | `m^2 s^-2` |
| $M_pc^2$ | `kg m^2 s^-2` |
| $V_p$ | `m^3` |
| $\rho_{\rm UV}^p$ | `kg m^-1 s^-2` |
| $r_p/R_H$, $\alpha^2$, $N_{\rm Cartan}$ | `1` |
| $\rho_\Lambda^{\rm GDQ}$ antes de dividir por $c^2$ | `kg m^-1 s^-2` |
| $\rho_\Lambda^{\rm GDQ}$ final | `kg m^-3` |

## 4. Status

A derivação simbólica confirma a estrutura algébrica, a contagem 28 e a dimensão final kg/m^3. A avaliação metrológica depende de $R_H=c/H_0$ como contorno cosmológico.
