# Resultado do teste do exterior Berger completo

## Classificação

$$
\boxed{
\text{teste de consistência e tolerância com dados sintéticos}
}
$$

O alvo é validar as equações, não obter o background físico.

## Resultados

| `rtol` | `atol` | passo máximo | $\max|\mathcal C_N|$ | $Z(s_+)$ |
|---:|---:|---:|---:|---:|
| $10^{-7}$ | $10^{-9}$ | $2\times10^{-3}$ | $8{,}882\times10^{-16}$ | $1{,}845871138670\times10^{-2}$ |
| $10^{-9}$ | $10^{-11}$ | $10^{-3}$ | $8{,}882\times10^{-16}$ | $1{,}845871138670\times10^{-2}$ |
| $10^{-11}$ | $10^{-13}$ | $5\times10^{-4}$ | $8{,}882\times10^{-16}$ | $1{,}845871138670\times10^{-2}$ |

## Conclusão

$$
\boxed{
\text{o sistema Berger preserva a restrição no nível de arredondamento.}
}
$$

A coincidência de $Z$ sob refinamento valida a implementação local. Os dados
iniciais não são uma solução de colagem e não devem ser usados para inferir
estabilidade ou gap.
