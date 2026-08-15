# Chapter 16 — upper residuals after the leading term

Classification: external metrological comparison and size diagnostic. It is not a derivation of the upper QGD terms.

- alpha^-1 used: `137.035999177000`
- x = alpha/pi: `2.322819464195329e-03`
- leading term: `a1 = alpha/(2*pi) = 1.161409732097664e-03`

| case | a_obs | sigma | a_obs-a1 | g_obs | g_leader | g_obs-g_leader | aggregated C2 | source |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| electron Fan 2022 | 1.159652180590109e-03 | 1.300000000000000e-13 | -1.757551507554920e-06 | 2.002319304361180 | 2.002322819464196 | -3.515103015109839e-06 | -0.325744542535 | Fan et al. arXiv:2209.13084 |
| muon world avg 2023 | 1.165920590000000e-03 | 2.200000000000000e-10 | 4.510857902335647e-06 | 2.002331841180000 | 2.002322819464196 | 9.021715804671294e-06 | 0.836042265346 | Aguillard et al. arXiv:2308.06230 |

## QGD Reading

For each lepton, the residual must be produced by:

$$
\Delta\gamma_{\rm geom}^{\rm upper}
=
\frac{\langle c,H_C^{-1}m_\perp\rangle}
{\langle c,H_C^{-1}c\rangle}
-\gamma_0\frac{\alpha}{2\pi}.
$$

The `aggregated C2` is only the effective coefficient that would appear if the entire residual were put into `(alpha/pi)^2`. It is not a derivation.

For the electron, the aggregated coefficient is of the order of negative unity, as expected for a small upper correction. For the muon, the aggregated coefficient changes significantly, showing that the heavy leptonic background cannot be replaced by the electron background.
