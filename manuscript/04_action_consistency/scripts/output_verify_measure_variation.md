# Output — variation of the constitutive measure

## Classification

Symbolic test of constitutive identity. Not a physical prediction.

## Linearized identity

For fixed metric and fixed $z_\\tau$:

$$
\\frac{\\delta\\mathcal U}{\\mathcal U}
=-\\frac12\\delta(f+\\bar f).
$$

## Finite difference test

| $\\epsilon$ | exact relative variation | linear prediction | error |
|---:|---:|---:|---:|
| 1e-02 | -4.9875208073180208e-03 | -5.0000000000000001e-03 | 1.248e-05 |
| 1e-04 | -4.9998750020833842e-05 | -5.0000000000000002e-05 | 1.250e-09 |
| 1e-06 | -4.9999987500002167e-07 | -5.0000000000000001e-07 | 1.250e-13 |
| 1e-08 | -4.9999999874836437e-09 | -5.0000000000000004e-09 | 1.252e-17 |

## Verdict

The check passed in the linear limit.

This output only verifies the constitutive variation of the measure, not the equations of motion.
