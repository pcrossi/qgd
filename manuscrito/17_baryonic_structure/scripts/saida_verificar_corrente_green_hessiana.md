# Saída — corrente de Green da Hessiana

## Operador testado

```text
L y = - U^{-1} d_x(U A d_x y) + V y
U = exp(-x**2)
A = x**2/5 + 1
V = x/7 + 2
```

## Funções teste

```text
phi = x**2/3 + sin(x)
psi = x/5 + cos(2*x)
```

## Identidade

```text
d_x j(phi, psi) - U(psi L phi - phi L psi) =
0
```

Resultado: `residual == 0` é `True`.

Conclusão: a corrente bilinear de Green é conservada para modos no kernel do operador físico.
