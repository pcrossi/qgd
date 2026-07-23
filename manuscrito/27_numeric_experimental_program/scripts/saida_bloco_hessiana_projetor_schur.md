# Saída — bloco Hessiana, projetor e Schur

Classificação: ferramenta metodológica / verificação algébrica.

## Matrizes usadas

Hessiana de exemplo $K$:

```text
 4.000000  0.300000  0.600000  0.100000
 0.300000  3.000000  0.200000  0.400000
 0.600000  0.200000  5.000000  0.700000
 0.100000  0.400000  0.700000  4.500000
```

Vínculo linearizado $DC$:

```text
 1.000000 -1.000000  0.500000  0.000000
```

## Verificações

| teste | valor |
|---|---:|
| idempotencia norm(P^2-P) | 0.000000000000e+00 |
| vinculo norm(DC P) | 7.850462293419e-17 |
| simetria norm(Kphys-Kphys^T) | 3.510833468577e-16 |
| menor autovalor K_eff | -2.220446049250e-16 |

## Espectro

| operador | autovalores |
|---|---|
| $K_{\rm phys}$ | `[-1.554312234e-15  3.642271729e+00  3.828581072e+00  5.451369421e+00]` |
| $K_{\rm eff}$ | `[-2.220446049e-16  3.750985499e+00]` |

## Veredito

O bloco algébrico remove o vínculo, preserva simetria da Hessiana e produz um operador efetivo de Schur não-negativo neste exemplo até erro de arredondamento. Em aplicações físicas, apenas $K$, $DC$, domínio e contornos mudam.
