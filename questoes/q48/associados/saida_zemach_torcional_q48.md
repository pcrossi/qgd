# Saída — Zemach torcional Q48

Classificação: avaliação direta de ansatz reduzido herdado da Q40.
O resíduo hiperfino não foi usado para escolher os parâmetros.

## Decomposição magnética usada

$$
\frac{G_M^p(q)}{\mu_p}
=
\frac{j_0(qr_p)+\kappa_p G_{\rm tor}(q)}{1+\kappa_p}.
$$

$$
\kappa_p=\frac35\ln(2\pi^2)\left(1+\frac\alpha4\right).
$$

- kappa_p = 1.792828941528952
- mu_p/mu_N GDQ = 2.792828941528952
- r_p = 0.840778765450 fm

## Resultados

| caso | R_tor (fm) | r_Z (fm) | erro quad | nu_HFS final (Hz) | erro relativo |
|---|---:|---:|---:|---:|---:|
| torção volumétrica em R=r_p | 0.840778765450 | 1.049074404252 | 8.535e-10 | 1420431634.121131 | 1.822180e-05 |
| R_tor=sqrt(5/3) r_p | 1.085440718811 | 1.120484017819 | 8.753e-10 | 1420427802.464068 | 1.552422e-05 |
| R_tor=(1+kappa)^(1/3) r_p | 1.184031291774 | 1.153424553556 | 8.749e-10 | 1420426034.959244 | 1.427986e-05 |

## Teste de duas cascas torcionais de média nula

Forma testada:

$$
\frac{G_M^p(q)}{\mu_p}
=
j_0(qr_p)+A\left[j_0(qr_-)-j_0(qr_+)\right],
\qquad
r_\pm=r_p\left(1\pm\frac\alpha2\right).
$$

A correção preserva $G_M^p(0)/\mu_p=1$.

| amplitude A | origem | r_Z (fm) | nu_HFS final (Hz) | erro relativo |
|---:|---|---:|---:|---:|
| 1.846832903074e-02 | Q40 nêutron: alpha delta_B | 1.120962813319 | 1420427776.773127 | 1.550614e-05 |
| 6.419401184476e-01 | fração anômala kappa/(1+kappa) | 1.118412631265 | 1420427913.609368 | 1.560247e-05 |
| 1.792828941529e+00 | escala anômala kappa | 1.113705159358 | 1420428166.200259 | 1.578030e-05 |
| 1.898119441401e+00 | projetor espacial 3 delta_B/4 | 1.113274490419 | 1420428189.308852 | 1.579657e-05 |

## Leitura

A inclusão da magnetização torcional volumétrica altera o Zemach, mas,
com os raios naturais herdados da Q40, não remove integralmente o erro
de $10^{-5}$. Isso mostra que a forma magnética superior relevante não
é apenas uma bola uniforme: ela precisa do perfil radial de torção
$\widehat\rho_{\rm tor}^p(\chi)$ obtido da Hessiana local.

$$
\boxed{
\text{ansatz torcional natural testado; melhora/impacto quantificado; Hessiana local ainda necessária.}
}
$$
