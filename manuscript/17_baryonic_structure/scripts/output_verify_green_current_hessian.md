# Output — Green's current of the Hessian

## Operator tested

```text
L y = - U^{-1} d_x(U A d_x y) + V y
U = exp(-x**2)
A = x**2/5 + 1
V = x/7 + 2
```

## Test functions

```text
phi = x**2/3 + sin(x)
psi = x/5 + cos(2*x)
```

## Identity

```text
d_x j(phi, psi) - U(psi L phi - phi L psi) =
0
```

Result: `residual == 0` is `True`.

Conclusion: Green's bilinear current is conserved for modes in the kernel of the physical operator.
