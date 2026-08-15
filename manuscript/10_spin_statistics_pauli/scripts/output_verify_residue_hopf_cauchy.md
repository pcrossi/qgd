# Output — verify Hopf/Cauchy residue

Classification: symbolic-numerical test of topological identity.

Integral tested:

$$
\frac{1}{2\pi i}\oint_{|z|=r} \frac12\frac{dz}{z}.
$$

| radius r | Re(integral) | Im(integral) | error to 1/2 |
|---:|---:|---:|---:|
| 0.050 | 0.500000000000 | -6.296885539364e-20 | 1.110223203196e-16 |
| 0.100 | 0.500000000000 | -6.296885539364e-20 | 1.110223203196e-16 |
| 0.300 | 0.500000000000 | -1.001775166815e-20 | 1.110223029145e-16 |
| 0.700 | 0.500000000000 | -6.944032246981e-20 | 1.110223241787e-16 |
| 1.000 | 0.500000000000 | -9.368870235938e-20 | 1.110223419932e-16 |

Interpretation: the normalized circulation is $1/2$ and is independent of the loop radius. This represents the Hopf spinor half-monodromy around the stoma.
