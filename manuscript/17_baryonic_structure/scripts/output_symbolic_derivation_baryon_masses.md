# Output — symbolic derivation of baryon masses

Classification: symbolic derivation / direct evaluation.

## 1. Reduced Unit

The reduced metrological unit is:

$$
E_0=M_e c^2,
\qquad
M_B/M_e=\mathcal I_B.
$$

## 2. Bulk of Three Stomata

Each chamber contributes:

$$
\operatorname{Vol}(\mathcal F_a)=2\pi^5.
$$

For three stomata:

$$
\mathcal I_B^{\rm bulk}=3(2\pi^5)=6 \pi^{5}.
$$

## 3. Torsional Surface of the Proton

The reduced surface transgression is:

$$
\mathcal I_p^\partial=
\frac{3 \alpha \left(1 + 2 \pi^{4}\right)}{4 \pi^{3}}.
$$

Logo:

$$
\frac{M_p}{M_e}=
\frac{3 \left(\alpha \left(1 + 2 \pi^{4}\right) + 8 \pi^{8}\right)}{4 \pi^{3}}.
$$

## 4. Torsional Excess of the Neutron

Torsional configurations:

$$
\mathbf t_p=(1,1,1),
\qquad
\mathbf t_n=(1,1,-2).
$$

Pairwise shear invariant:

$$
I_{\rm sh}^2(\mathbf t)=\sum_{a<b}(t_a-t_b)^2.
$$

For proton and neutron:

$$
I_{\rm sh}^2(\mathbf t_p)=0,
\qquad
I_{\rm sh}^2(\mathbf t_n)=18.
$$

The Fredholm–Fano projection uses:

$$
\cos\theta_c=\frac{3}{\sqrt{3^2+4^2}}=\frac{3}{5},
\qquad
\|1+i\|=\sqrt2.
$$

Thus:

$$
\chi_B=\sqrt2\cos\theta_c=\frac{3 \sqrt{2}}{5}.
$$

Since $\operatorname{Vol}(S^3)=2\pi^2$:

$$
\delta_B=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
$$

The equivalent symbolic form evaluated by the code is:

$$
\log{\left(\left(2 \pi^{2}\right)^{\frac{3 \sqrt{2}}{5}} \right)}.
$$

Therefore:

$$
\frac{M_n}{M_e}=\frac{M_p}{M_e}+\delta_B.
$$

## 5. Numerical Evaluation

| quantity | value |
|---|---:|
| alpha^-1 | 137.035999177000 |
| bulk 6*pi^5 | 1836.118108711689 |
| torsional surface | 0.034564476923 |
| delta_B | 2.530825921868 |
| Mp/Me | 1836.152673188612 |
| Mn/Me | 1838.683499110479 |

## 6. Subsequent Comparison

| ratio | GDQ | reference | relative error |
|---|---:|---:|---:|
| Mp/Me | 1836.152673188612 | 1836.152673430000 | -1.314640567725e-10 |
| Mn/Me | 1838.683499110479 | 1838.683661730000 | -8.844344676383e-08 |

## Verdict

The formulas for proton and neutron are obtained via reduced volume, surface torsional transgression, and antiparallel shear. The accepted values enter only afterward, as a comparison.
