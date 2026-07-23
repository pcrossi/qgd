# Saída — verificação da dimensão do kernel

## Classificação

Teste simbólico/ilustração dimensional. Não é previsão física.

## Entrada estrutural

- Dimensão real do bulk local: `8`.
- Dimensão complexa correspondente: `4`.

## Fórmula verificada

Para um kernel plano em dimensão real $d$:

$$
K_d(z_\tau)=(4\pi z_\tau)^{-d/2}.
$$

Logo, para $d=8$:

$$
K_8(z_\tau)=(4\pi z_\tau)^{-4}.
$$

## Resultado

| Quantidade | Valor |
|---|---:|
| $d$ | 8 |
| $d/2$ | 4 |
| $n$ | 4 |
| Potência esperada | 4 |

## Veredito

A checagem passou.

Esta saída confirma apenas a conta dimensional do kernel. Ela não seleciona dinamicamente o bulk local.
