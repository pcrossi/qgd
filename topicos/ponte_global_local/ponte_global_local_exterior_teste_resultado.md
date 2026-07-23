# Resultado do teste do sistema exterior warped

## Classificação

$$
\boxed{
\text{teste de consistência e de tolerância em background sintético}
}
$$

Não é uma solução cosmológica física e não usa alvos experimentais.

## Sistema testado

Foi integrado o sistema canônico de
`topicos/ponte_global_local/ponte_global_local_exterior_equacoes.md` no intervalo

$$
0\leq s\leq0{,}02,
$$

com $\lambda_N$ escolhido apenas para satisfazer a restrição inicial

$$
\mathcal C_N(0)=0.
$$

## Refinamento

| `rtol` | `atol` | passo máximo | $\max|\mathcal C_N|$ | $Z(s_+)$ |
|---:|---:|---:|---:|---:|
| $10^{-7}$ | $10^{-9}$ | $2\times10^{-3}$ | $8{,}882\times10^{-16}$ | $1{,}721058703783\times10^{-2}$ |
| $10^{-9}$ | $10^{-11}$ | $10^{-3}$ | $8{,}882\times10^{-16}$ | $1{,}721058703783\times10^{-2}$ |
| $10^{-11}$ | $10^{-13}$ | $5\times10^{-4}$ | $8{,}882\times10^{-16}$ | $1{,}721058703783\times10^{-2}$ |

## Conclusão

O resíduo está no nível de arredondamento e a normalização acumulada é
invariante sob o refinamento empregado. Portanto:

$$
\boxed{
\text{a inversão dos momentos e as equações canônicas preservam a restrição.}
}
$$

Esse resultado valida a implementação local do exterior. O próximo teste deve
substituir os dados sintéticos pelos traços fornecidos pelo DtN interno e
resolver simultaneamente as duas interfaces e os vínculos cosmológicos.
