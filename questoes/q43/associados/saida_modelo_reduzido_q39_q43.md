# Saída — Modelo reduzido Q39→Q43

## Classificação

Teste de consistência e diagnóstico inverso. Este cálculo não é predição cega de \(g-2\).

## Parâmetros usados

- `alpha_inv = 137.035999177000`
- `alpha = 7.297352564331424e-03`
- `a1 = alpha/(2*pi) = 1.161409732097664e-03`
- `R_mu_Q39 = 2.067685934706287e+02`
- `R_tau_Q39 = 3.477446405098381e+03`

## Hierarquia Q39 usada como background reduzido

| lépton | papel Q39 | R_l=M_l/M_e | chi_rel=1/R_l |
|---|---|---:|---:|
| elétron | torção primária | 1.000000000000000e+00 | 1.000000000000000e+00 |
| múon | torção transversal/biespacial | 2.067685934706287e+02 | 4.836324430199547e-03 |
| tau | saturação tridimensional | 3.477446405098381e+03 | 2.875673363459670e-04 |

## Resíduos superiores observados

O resíduo é \(a_{\rm obs}-\alpha/(2\pi)\). O coeficiente agregado é apenas diagnóstico:

| lépton | a_obs | resíduo | C2_agregado = residuo/(alpha/pi)^2 | fonte |
|---|---:|---:|---:|---|
| elétron | 1.159652180590109e-03 | -1.757551507554920e-06 | -0.325744542535 | Fan et al. 2022/2023, g/2 |
| múon | 1.165920590000000e-03 | 4.510857902335647e-06 | 0.836042265346 | Muon g-2 world average 2023 |
| tau | — | — | — | sem uso metrológico neste teste |

## Teste: a hierarquia sozinha explica o resíduo?

Hipótese testada: o resíduo superior escala apenas com a susceptibilidade escalar diagonal \(\chi_\ell\propto1/R_\ell\), normalizada no elétron.

| lépton | resíduo previsto por chi_rel | resíduo observado | veredito |
|---|---:|---:|---|
| elétron | -1.757551507554920e-06 | -1.757551507554920e-06 | calibração de referência |
| múon | -8.500089293321902e-09 | 4.510857902335647e-06 | falha por fator -1.884e-03 |
| tau | -5.054144055184069e-10 | — | sem comparação metrológica |

## Diagnóstico inverso mínimo

Se se escreve \(a_\ell-a_1=\mathcal R_\ell\), então o operador transversal físico deve produzir exatamente \(\mathcal R_\ell\):

$$
\mathcal R_\ell=\frac{1}{\gamma_{0,\ell}}\frac{\langle c_\ell,H_{C,\ell}^{+}m_{\perp,\ell}\rangle}{\langle c_\ell,H_{C,\ell}^{+}c_\ell\rangle}-\frac{\alpha}{2\pi}.
$$

No modelo diagonal reduzido, a massa/hierarquia não determina essa contração. A informação faltante é \(m_{\perp,\ell}\) e o bloco transversal físico de \(H_{C,\ell}\).

## Conclusão

A hierarquia Q39 é necessária como background leptônico, mas é insuficiente para fechar \(g-2\). A hierarquia de massas não pode ser usada como substituto do cálculo Zeeman/anomalia. O próximo elo físico é construir \(H_{C,\ell}\), \(c_\ell\) e \(m_{\perp,\ell}\) diretamente da Hessiana oficial em cada background leptônico.
