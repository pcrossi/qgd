---
title: "Output — powers and units"
---

# Output — powers and units

Classification: editorial symbolic/dimensional test.

## Linear mass squared

| Writing | numerical value in the quadratic unit |
|---|---:|
| $125\,{\rm GeV}^2$ | `125.000000` GeV² |
| $(125\,{\rm GeV})^2$ | `15625.000000` GeV² |

Ratio between the two readings:

$$
\frac{(125\,{\rm GeV})^2}{125\,{\rm GeV}^2}
=
125.000000.
$$

Therefore, if the physical meaning is Higgs mass squared, the safe writing is:

$$
M_H^2\simeq(125\,{\rm GeV})^2.
$$

## Already calculated quadratic value

If a calculation directly yields:

$$
\Delta M_H^2\simeq0.68\,{\rm MeV}^2,
$$

then the number `0.68` is already the value of the quadratic quantity. Writing
$(0.68\,{\rm MeV})^2$ would change the value to:

$$
0.462400\,{\rm MeV}^2.
$$

## Conclusion

- Use $(M\,{\rm GeV})^2$ when the linear number must also be squared.
- Use $X\,{\rm GeV}^2$ when $X$ is already the value of a quadratic quantity.
