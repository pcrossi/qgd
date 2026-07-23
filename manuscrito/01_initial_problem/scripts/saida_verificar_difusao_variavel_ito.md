# Saída — difusão variável de Nelson--Itô

## Classificação

Teste simbólico-numérico de identidade diferencial em domínio periódico. Não é previsão física.

## Identidades testadas

$$
D=\nu_0\Omega^{-1}.
$$

$$
\partial_x^2(D\rho)
=D\rho''+2D'\rho'+\rho D''.
$$

$$
u=D\partial_x\ln\rho+\partial_xD
=D(\partial_x\ln\rho-\partial_x\ln\Omega).
$$

## Parâmetros numéricos

- Domínio periódico: $[0,2\pi)$
- Malha: $N=2048$
- $\nu_0=0.5$ em unidades reduzidas

## Erros máximos

| teste | erro máximo |
|---|---:|
| expansão de Itô | 1.691021e-10 |
| Fokker--Planck conservativa vs expandida | 1.691021e-10 |
| velocidade osmótica variável | 9.168838e-14 |

## Tamanho dos termos omitidos se $\Omega$ for tratado como constante

| quantidade | valor |
|---|---:|
| $\lVert\partial_x^2(D\rho)-D\rho''\rVert_\infty$ | 3.171848e-01 |
| fração relativa ao termo completo | 1.111239e+00 |

## Veredito

As identidades passaram. Os termos com gradientes de $\Omega$ são necessários quando $\Omega$ varia.

Nenhum alvo experimental foi usado.
