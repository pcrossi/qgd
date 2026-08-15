---
title: "Output — multispecies sweep without pole"
---

# Output — multispecies sweep without pole

## Formula

$$
\\Pi_{\\rm EM}(\\infty)=\\frac{\\alpha_0}{3\\pi}
\\sum_fN_c^{(f)}Q_f^2
E_1\\left(\\frac{m_f^2}{\\Lambda_{\\rm EM}^2}\\right).
$$

The formal boundary is $\\Pi_{\\rm EM}(\\infty)=1$.

| scenario | species | $\\sum N_cQ^2$ | $\\log_{10}(\\Lambda_{\\rm crit}/m_e)$ | $\\Pi$ at root |
|:---|---:|---:|---:|---:|
| geometric leptons | `3` | `3.000000` | `118.064508933` | `1.000000000000` |
| charged fermions — benchmark | `9` | `9.000000` | `39.022131976` | `1.000000000000` |

| scenario | $\\Pi(\\Lambda_{\\rm crit}/10)$ | $\\Pi(10\\Lambda_{\\rm crit})$ | monotonic |
|:---|---:|---:|:---:|
| geometric leptons | `0.983177696` | `1.016822304` | `True` |
| charged fermions — benchmark | `0.949533088` | `1.050466912` | `True` |

## Spectrum: geometric leptons

| species | $m_f/m_e$ | $Q_f$ | $N_c$ | weight | provenance |
|:---|---:|---:|---:|---:|:---|
| e | `1` | `-1` | `1` | `1` | metrological unit |
| mu | `206.767399` | `-1` | `1` | `1` | geometric spectral ratio |
| tau | `3477.13178` | `-1` | `1` | `1` | geometric spectral ratio |

## Spectrum: charged fermions — benchmark

| species | $m_f/m_e$ | $Q_f$ | $N_c$ | weight | provenance |
|:---|---:|---:|---:|---:|:---|
| e | `1` | `-1` | `1` | `1` | external reference |
| mu | `206.768297` | `-1` | `1` | `1` | external reference |
| tau | `3477.22855` | `-1` | `1` | `1` | external reference |
| u | `4.2270144` | `0.666667` | `3` | `1.33333` | scheme-dependent quark mass |
| d | `9.138962` | `-0.333333` | `3` | `0.333333` | scheme-dependent quark mass |
| s | `181.996458` | `-0.333333` | `3` | `0.333333` | scheme-dependent quark mass |
| c | `2485.32798` | `0.666667` | `3` | `1.33333` | scheme-dependent quark mass |
| b | `8180.05532` | `-0.333333` | `3` | `0.333333` | scheme-dependent quark mass |
| t | `338082.885` | `0.666667` | `3` | `1.33333` | scheme-dependent quark mass |

## Classification

Consistency test. The extremely high root is a consequence of the
effective extrapolation and should not be read as a predicted physical scale.
