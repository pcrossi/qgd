# Q39 — saída do cálculo da Hessiana 8D produto

## Entrada normalizada

- raios de `T^5`: `[1.0, 1.0, 1.0, 1.0, 1.0]`
- `tau = 1.0`
- `C_gamma = 1.0`

## Resultado analítico avaliado

- `m_perp^2 = C_gamma * tau / R_max^2 = 1.000000000000`
- `||J|| = 0.000000000000`
- `||J H_perp^-1 J^dagger|| = 0.000000000000`

## Índice crítico

| `ind(H_B)` | `ind(H_perp)` | `ind(H_8)` |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 2 | 0 | 2 |
| 3 | 0 | 3 |

## Veredito

No background produto normalizado, o complemento toroidal é coercivo,
o bloco misto é nulo e o índice crítico 8D coincide com o índice do
setor 3D curvo.

$$
\operatorname{ind}^{-}(H_8)
=
\operatorname{ind}^{-}(H_B).
$$
