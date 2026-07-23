# Q43 — resíduos superiores depois do termo líder

Classificação: comparação metrológica externa e diagnóstico de tamanho.
Não é derivação dos termos superiores da GDQ.

- alpha^-1 usado: `137.035999177000`
- x = alpha/pi: `2.322819464195329e-03`
- termo líder: `a1 = alpha/(2*pi) = 1.161409732097664e-03`

| caso | a_obs | sigma | a_obs-a1 | g_obs | g_lider | g_obs-g_lider | C2 agregado | fonte |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| electron Fan 2022 | 1.159652180590109e-03 | 1.300000000000000e-13 | -1.757551507554920e-06 | 2.002319304361180 | 2.002322819464196 | -3.515103015109839e-06 | -0.325744542535 | Fan et al. arXiv:2209.13084 |
| muon world avg 2023 | 1.165920590000000e-03 | 2.200000000000000e-10 | 4.510857902335647e-06 | 2.002331841180000 | 2.002322819464196 | 9.021715804671294e-06 | 0.836042265346 | Aguillard et al. arXiv:2308.06230 |

## Leitura GDQ

Para cada lépton, o resíduo deve ser produzido por:

$$
\Delta\gamma_{\rm geom}^{\rm sup}
=
\frac{\langle c,H_C^{-1}m_\perp\rangle}
{\langle c,H_C^{-1}c\rangle}
-\gamma_0\frac{\alpha}{2\pi}.
$$

O `C2 agregado` é apenas o coeficiente efetivo que apareceria se todo
o resíduo fosse colocado em `(alpha/pi)^2`. Ele não é uma derivação.

Para o elétron, o coeficiente agregado é da ordem de unidade negativa,
como esperado para uma correção superior pequena. Para o múon, o
coeficiente agregado muda de modo significativo, mostrando que o
background leptônico pesado não pode ser substituído pelo background
do elétron.
