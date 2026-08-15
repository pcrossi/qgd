# Output — symbolic derivation of the leptonic hierarchy

Classification: symbolic derivation / direct evaluation.

## 1. Electronic sector

The electron defines the reduced scale:

$$
R_e=1.
$$

## 2. Muon ratio

Bispatial support:

$$
\nu_2=\frac23.
$$

Leading term:

$$
R_\mu^{(0)}=\frac{1}{\nu_2\alpha}=\frac{3}{2}\alpha^{-1}.
$$

Interface impedance and self-energy:

$$
\Delta_\partial=\frac65,
\qquad
\Delta_{\rm self}=2\alpha.
$$

Thus:

$$
R_\mu=
2 \alpha + \frac{6}{5} + \frac{3}{2 \alpha}.
$$

## 3. Geometric saturation of the third ratio

With $R_3=z^2$, the condition is:

$$
\frac{10 \left(2 \alpha \left(10 \alpha + 5 z^{2} + 11\right) + 15\right)}{\left(10 \sqrt{\alpha} \left(z + 1\right) + \sqrt{10} \sqrt{4 \alpha \left(5 \alpha + 3\right) + 15}\right)^{2}} = \frac{2}{3}.
$$

The equivalent polynomial numerator is:

$$
10 \left(- 4 \sqrt{10} \sqrt{\alpha} z \sqrt{20 \alpha^{2} + 12 \alpha + 15} - 4 \sqrt{10} \sqrt{\alpha} \sqrt{20 \alpha^{2} + 12 \alpha + 15} + 20 \alpha^{2} + 10 \alpha z^{2} - 40 \alpha z + 22 \alpha + 15\right)=0.
$$

The two solutions for $R_3$ are:

$$
R_{3,\pm}=
\left[
2(\sqrt{R_1}+\sqrt{R_2})
\pm
\sqrt{3R_1+12\sqrt{R_1R_2}+3R_2}
\right]^2.
$$

The direct symbolic solution of the polynomial in $z$ was used by the script; the above form is the simplified form in terms of $R_1$ and $R_2$.

## 4. Numerical evaluation

| quantity | value |
|---|---:|
| alpha^-1 | 137.035999177000 |
| R_mu | 206.768593470629 |
| R_3 light branch | 6.491919023877 |
| R_3 heavy branch | 3477.446405098382 |

## 5. Posterior comparison

| ratio | GDQ | reference | relative error |
|---|---:|---:|---:|
| M_mu/M_e | 206.768593470629 | 206.768282700000 | 1.502989842682e-06 |
| M_tau/M_e | 3477.446405098382 | 3477.150000000000 | 8.524369048845e-05 |

## Verdict

The symbolic derivation produces the muon formula and the two branches of the third ratio without using experimental masses as input. The choice of the heavy branch is a physical selection of the charged triplet; the light branch remains mathematical until it has its own Hessian.
