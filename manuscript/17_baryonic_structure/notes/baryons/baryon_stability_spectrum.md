---
title: "Leading spectrum and baryonic stability"
---

# Leading spectrum and baryonic stability

## 1. Baryonic Hessian

The stability of a baryon is evaluated by the physical Hessian:

$$
K_B^{\rm phys}
=
P_{\rm phys}^\dagger
\left.
\delta^2\mathcal S_{\rm GDQ}
\right|_{\Phi_B}
P_{\rm phys;.
$$

The projector $P_{\rm phys}$ removes:

1. redundant diffeomorphisms;
2. variations that violate the normalization of $\mathcal U$;
3. variations that change the charge/residue;
4. variations that change the topological class of the baryon;
5. modes incompatible with the boundary of the stoma.

In the preserved sector, the proton has no continuous path to the vacuum without violating the Cauchy charge, the Noether flux, or the trimodal class.

## 2. Moment of Inertia

For the reduced surface shell:

$$
\langle r^2\rangle_{\rm surf}
=
\frac35r_p^2.
$$

The leading moment of inertia is:

$$
I_{\rm rot}
=
\frac12M_p\langle r^2\rangle_{\rm surf}
=
\frac{3}{10}M_pr_p^2.
$$

## 3. Rotational Scale

The leading rotational energy is:

$$
E_{\rm rot}
=
\frac{5(\hbar c)^2}{M_pr_p^2}.
$$

This scale provides the first test against the $\Delta(1232)$ channel:

$$
M_\Delta^{\rm lead}
=
M_p+E_{\rm rot}.
$$

It must be read as a leading approximation, since it does not yet diagonalize the radial, torsional, and throat modes of the complete Hessian.

## 4. Free Neutron

The neutron preserves baryon number, but the antiparallel torsional orientation opens a neutral shear channel. This makes the free neutron dynamically unstable without making the proton unstable.

The essential point is:

$$
B_{\rm top}=1
$$

for proton and neutron, but:

$$
Q_p=1,
\qquad
Q_n=0.
$$

The beta decay of the neutron is then a dynamic surgery in a neutral sector, not a continuous loss of the baryonic class.

Script:

[[../../scripts/baryon_stability_spectrum|baryon_stability_spectrum.py]]

Output:

[[../../scripts/output_baryon_stability_spectrum|Output — baryon stability and spectrum]].
