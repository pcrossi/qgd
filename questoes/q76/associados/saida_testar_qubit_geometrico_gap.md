# Saída — Q76 teste reduzido de qubit geométrico

Classificação: teste de consistência matemática / mock reduzido.

Este script verifica somente a álgebra de estabilidade por gap:

$$
K_{\rm phys}
\to
P_Q
\to
\Delta_{\rm gap}
\to
\|\delta P_Q\|.
$$

Ele não deriva a Hessiana de um hardware real.

## Background reduzido

- autovalores iniciais: `[0.0, 0.03, 1.0, 1.35, 1.8, 2.4]`
- gap lógico--complemento: `0.970000000000`

## Perturbações locais

| caso | ||dK||/gap | ||dK|| | gap novo | ||dP|| | cota 2||dK||/gap | autovalores baixos |
|---|---:|---:|---:|---:|---:|---|
| local_subcritico_10pct | 0.100 | 0.097000 | 1.057329 | 0.061093 | 0.200000 | `-0.003103, 0.000000, 1.057329, 1.421429` |
| local_subcritico_40pct | 0.400 | 0.388000 | 1.255328 | 0.189667 | 0.800000 | `-0.139188, 0.000000, 1.255328, 1.646481` |
| local_limiar_50pct | 0.500 | 0.485000 | 1.326358 | 0.219020 | 1.000000 | `-0.192415, 0.000000, 1.326358, 1.724333` |
| mix_subcritico_40pct | 0.400 | 0.388000 | 1.163428 | 0.331007 | 0.800000 | `-0.106103, -0.027325, 1.136103, 1.377325` |
| mix_supercritico_80pct | 0.800 | 0.776000 | 1.533665 | 0.484769 | 1.600000 | `-0.400096, -0.103569, 1.430096, 1.453569` |
| mix_supercritico_120pct | 1.200 | 1.164000 | 1.782525 | 0.554700 | 2.400000 | `-0.746000, -0.216263, 1.566263, 1.776000` |

## Interpretação

Para perturbações abaixo de metade do gap, o cluster permanece isolado e
a variação do subespaço lógico fica controlada. Perturbações acima desse
limiar não significam erro automático, mas deixam de estar cobertas pelo
critério simples usado na Q76.

$$
\boxed{
\text{proteção GDQ = gap Hessiano + contorno + topologia, não erro zero.}
}
$$
