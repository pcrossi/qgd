# Output — reduced alpha decay

Classification: reduced GDQ proof of concept.

## Comparison in log10(T_1/2)

| Channel | log10(T_ref) | log10(T_GDQ_red) | residue |
|---|---:|---:|---:|
| U-238 | 17.149217 | 17.224558 | +0.075341 |
| U-234 | 12.889155 | 12.792212 | -0.096943 |
| U-232 | 9.337323 | 9.298479 | -0.038844 |
| Th-232 | 17.646780 | 17.708693 | +0.061913 |
| Ra-226 | 10.703224 | 10.624607 | -0.078617 |
| Po-212 | -6.524329 | -6.556893 | -0.032564 |

## Metrics

- Reduced GDQ RMS: `0.067894` decades
- Gamow RMS with reduced internal frequency: `0.303358` decades
- Relative improvement: `77.619%`

## Interpretation

The result preserves the final reduced chain: Schur complement, Riesz projector of the alpha channel, shell rigidity via spin--torsion, and determinant mobility for the doubly magic daughter nucleus. The status is not a final metrological prediction because the actual blocks of the complete nuclear Hessian must still replace the reduced blocks.
