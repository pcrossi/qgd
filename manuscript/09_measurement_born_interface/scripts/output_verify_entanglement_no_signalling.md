# Output — reduced entanglement and no-signalling

Classification: reduced operational consistency test.

## Non-factorization

Schmidt singular values of the singlet:

| index | value |
|---:|---:|
| 0 | 0.707106781187 |
| 1 | 0.707106781187 |

Since both values are non-zero, the state does not have Schmidt rank 1 and is not
a product state. The smallest preserved singular value is:

$$
0.707106781187.
$$

## Correlation and marginals

| axis A | axis B | $a\cdot b$ | $E(a,b)$ | target $-a\cdot b$ | $P(+|a,b)$ in A | $P(+|a,b)$ in B |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 1.000000000000 | -1.000000000000 | -1.000000000000 | 0.500000000000 | 0.500000000000 |
| 0 | 1 | 0.000000000000 | 0.000000000000 | -0.000000000000 | 0.500000000000 | 0.500000000000 |
| 0 | 2 | 0.707106781187 | -0.707106781187 | -0.707106781187 | 0.500000000000 | 0.500000000000 |
| 1 | 0 | 0.000000000000 | 0.000000000000 | -0.000000000000 | 0.500000000000 | 0.500000000000 |
| 1 | 1 | 1.000000000000 | -1.000000000000 | -1.000000000000 | 0.500000000000 | 0.500000000000 |
| 1 | 2 | -0.707106781187 | 0.707106781187 | 0.707106781187 | 0.500000000000 | 0.500000000000 |
| 2 | 0 | 0.707106781187 | -0.707106781187 | -0.707106781187 | 0.500000000000 | 0.500000000000 |
| 2 | 1 | 0.707106781187 | -0.707106781187 | -0.707106781187 | 0.500000000000 | 0.500000000000 |
| 2 | 2 | 0.000000000000 | 0.000000000000 | -0.000000000000 | 0.500000000000 | 0.500000000000 |

## Errors

| test | value |
|---|---:|
| maximum error in $E(a,b)+a\cdot b$ | 0.000000000000e+00 |
| maximum variation of marginal A when changing B | 0.000000000000e+00 |
| maximum variation of marginal B when changing A | 0.000000000000e+00 |
| reduced CHSH value | -2.828427124746 |
| target $-2\sqrt 2$ | -2.828427124746 |

## Interpretation

The test shows that the joint correlation depends on both axes, but the
local marginals remain equal to $1/2$. This is operational compatibility
with no-signalling in the reduced projective sector. The complete GDQ must
still derive real apparatuses via $K_{AB}^{\rm phys}$, $\text{R}_A$ and
$\text{R}_B$.
