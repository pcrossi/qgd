# Output — linear physical projector

## Classification

Linear illustration of physical quotient. Not a physical prediction.

## Construction

Given the removed directions gathered in $A$, we use:

$$
P=I-A(A^TA)^{-1}A^T
$$

after orthonormalization of the columns.

## Result

- Total dimension: `5`.
- Projected physical dimension: `2`.
- Error $P^2-P$: `0.000e+00`.
- Error $P^T-P$: `0.000e+00`.
- Direction removal error: `0.000e+00`.
- Eigenvalues of $P$: `[0.0, 0.0, 0.0, 1.0, 1.0]`.

## Verdict

The check passed.

This output illustrates the algebra of the projector. In the real GDQ problem, $P_{\\rm phys}$ depends on the domain, constraints, and boundary.
