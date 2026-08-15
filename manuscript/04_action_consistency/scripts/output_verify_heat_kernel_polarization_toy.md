# Output — heat-kernel polarization toy

## Classification

Heat-kernel illustration. Not a physical prediction.

## Toy integral

$$
I(\\Lambda)=\\int_0^\\Lambda\\frac{k}{k^2+m^2}e^{-\\tau k^2}\,dk.
$$

The comparison without regulator is:

$$
I_0(\\Lambda)=\\frac12\\log\\left(\\frac{\\Lambda^2+m^2}{m^2}\\right).
$$

## Parameters

- $m=1$.
- $\\tau=0.25$.

## Results

| $\\Lambda$ | regulated | unregulated |
|---:|---:|---:|
| 1 | 3.018241315482e-01 | 3.465735902799e-01 |
| 2 | 5.378949826359e-01 | 8.047189562171e-01 |
| 4 | 6.772594611599e-01 | 1.416606672028e+00 |
| 8 | 6.942738779951e-01 | 2.087474378943e+00 |
| 16 | 6.942978358482e-01 | 2.775877864404e+00 |
| 32 | 6.942978358509e-01 | 3.466205886915e+00 |

## Verdict

The regulated integral saturates numerically in the UV in this toy model.

This output does not prove universal finiteness of GDQ. It only illustrates the effect of a heat-kernel factor.
