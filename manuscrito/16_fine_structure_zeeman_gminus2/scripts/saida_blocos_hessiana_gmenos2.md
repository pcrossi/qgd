# Capítulo 16 — saída do construtor de blocos de Hessiana

## Classificação

- Blocos líderes: avaliação direta da quantidade já derivada.
- Blocos `required`: diagnóstico inverso do canal superior faltante.

## Parâmetros

- `alpha_inv = 137.035999177000`
- `alpha = 7.297352564331424e-03`
- `K1 = 2*pi/alpha = 8.610225765836003e+02`
- `a_leader = alpha/(2*pi) = 1.161409732097664e-03`

## Bloco líder universal

- arquivo: `hessiana_lider_gmenos2.npz`
- `a_geom = 1.161409732097665e-03`
- `g_total = 2.002322819464196e+00`
- `eig_min = 9.988372413989819e-01`

## Hierarquia Q39 usada para rigidez diagnóstica

| caso | papel Q39 | M_l/M_e | K2 usado |
|---|---|---:|---:|
| elétron | torção primária | 1.000000000000000e+00 | 8.610225765836003e+02 |
| múon | torção transversal/biespacial | 2.067685934706287e+02 | 1.780324271066477e+05 |
| tau | saturação tridimensional | 3.477446405098381e+03 | 2.994159863649186e+06 |

## Blocos superiores required

Nestes blocos a amplitude `mu2_required` é escolhida para atingir `a_obs`. Portanto, são engenharia inversa diagnóstica.

| caso | a_obs | residuo a_obs-a_leader | mu2_required | a_reconstruido | arquivo |
|---|---:|---:|---:|---:|---|
| elétron | 1.159652180590109e-03 | -1.757551507554920e-06 | -1.513291527513514e-03 | 1.159652180590110e-03 | `hessiana_required_e_gmenos2.npz` |
| múon | 1.165920590000000e-03 | 4.510857902335647e-06 | 8.030789806924942e-01 | 1.165920590000000e-03 | `hessiana_required_mu_gmenos2.npz` |
| tau | — | — | — | — | — |

## Veredito

O bloco líder constrói $H_C,c,m_\perp$ sem alvo experimental e reproduz exatamente $\alpha/(2\pi)$.

Os blocos `required` mostram numericamente o tamanho da resposta transversal superior que falta derivar. Eles não fecham metrologicamente $g-2$, mas transformam a pendência em uma quantidade precisa: derivar da ação oficial o canal que substituirá `mu2_required`.
