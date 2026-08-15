---
title: "Numeric audit of Stern-Gerlach"
---

# Numeric audit of Stern--Gerlach

This note records the final scripts preserved in the manuscript. They are self-contained and do not depend on files external to the chapter.

## 1. Conditioned capture and Born

The script `simulate_sg_capture.py` integrates:

$$
dp_t=4\sqrt{\Gamma}\,p_t(1-p_t)\,dW_t.
$$

With thresholds $\varepsilon$ and $1-\varepsilon$, the analytical probability of first reaching the upper threshold is:

$$
P_\varepsilon(+)
=
\frac{p_0-\varepsilon}{1-2\varepsilon}.
$$

The script `validate_sg_born_threshold.py` verifies that:

$$
\lim_{\varepsilon\to0}P_\varepsilon(+)=p_0.
$$

In the preserved tests, the largest Monte Carlo deviation in the threshold study was $2.518\sigma$, compatible with statistical fluctuation. The column $|P_\varepsilon-p_0|$ decays linearly with $\varepsilon$.

## 2. Complete beam

The script `simulate_complete_sg_beam.py` combines:

1. conditioned capture of channels;
2. opposing center-of-mass force;
3. free drift to the screen.

For $\theta=60^\circ$:

- Born target: $p_+=0.75$;
- simulated frequency: $p_+=0.75184$;
- analytical separation: $0.7000000$;
- numerical separation: $0.6996684$;
- relative separation error: $4.737\times10^{-4}$.

## 3. Sequential measurements

The script `simulate_sg_sequences.py` verifies:

- sequence $z\to z$: fidelity $1$;
- sequence $z\to x$: $P(x+)=0.503325$;
- sequence $z\to x\to z$: $P(z+)=0.499975$;
- correlation between intermediate $x$ and final $z$: $0.000600$.

This reproduces the operational incompatibility of axes without interpreting $\kappa$ as a pre-existing table for all apparatuses.

## 4. Non-adiabatic regime

The script `simulate_nonadiabatic_sg.py` integrates:

$$
H(t)
=
\frac12
\left(vt\,\sigma_z+\Delta\sigma_x\right),
$$

with $\Delta=1$ and $\hbar=1$, and compares with:

$$
P_{\rm LZ}
=
\exp\left(-\frac{\pi\Delta^2}{2v}\right).
$$

In the range $v\in\{0.2,0.4,0.8,1.6,3.2\}$, the largest absolute error against Landau--Zener was:

$$
2.920\times10^{-4}.
$$

The same script calculates:

$$
\|[H,P_z^+]\|=0.707106781,
\qquad
\frac{dp_z}{dt}=0.5
$$

in a test state. Therefore, when the apparatus is not QND/adiabatic, $p_z$ ceases to be a martingale.

## 5. Reduced Robin spectrum

The script `solve_sg_robin_channels.py` solves the test operator:

$$
H_\pm
=
-\frac{d^2}{dr^2}+V(r),
\qquad
R_\pm=R_0\pm r_B.
$$

On the mesh $N=1600$:

$$
\lambda_1^+=1.030703215,
\qquad
\lambda_1^-=1.025837708,
$$

$$
\lambda_1^+-\lambda_1^-
=
4.865507054\times10^{-3}.
$$

The reduced sums are:

$$
\Gamma_{\rm red}^+=0.2426699727,
\qquad
\Gamma_{\rm red}^-=0.2949562551,
$$

$$
\kappa_{\rm red}^+=0.1000246896,
\qquad
\kappa_{\rm red}^-=0.1416924219.
$$

These numbers are a method convergence test, not a universal physical prediction.

## 6. Background, boundary, and cylindrical Hopf

`construct_sg_stationary_background.py` verifies the Gaussian bulk background with zero residue. `verify_sg_variational_boundary.py` confirms:

$$
r_c=\sqrt{6\tau},
\qquad
K-n(F)=0.
$$

`test_sg_gaussian_zh.py` shows that the pure Gaussian does not localize the axial mode:

$$
Z_H^{\rm Gaussian}=0.
$$

`solve_sg_cylindrical_hopf_dtn.py` calculates:

$$
z_H=\frac{3\sqrt\pi}{4}
=1.329340388179\ldots
$$

`compare_sg_stationary_actions.py` finds:

$$
\mathcal W_{\rm cyl}-\mathcal W_{\rm G}
=
-0.3439257889495.
$$

`verify_sg_cylindrical_radius_stability.py` confirms:

$$
\mathcal W''(2\sqrt\tau)=\frac{3}{2\tau}>0.
$$

## 7. Hopf Atlas

The script `verify_sg_hopf_atlas.py` confirms:

- maximum error of the projectors: $2.889\times10^{-16}$;
- maximum error of the transition: $1.279\times10^{-16}$;
- relative error of the Fubini--Study metric less than $8.0\times10^{-7}$.

## 8. Physical evaluator and contract

`evaluate_gdq_sg_background.py` does not contain phenomenological defaults. It requires a file with:

$$
\{\lambda_\nu,\ Z_\nu,\ j_{\nu1},\ j_{\nu2},\ \gamma_\nu,\ C_\nu\}.
$$

The fixture `test_sg_background_pipeline.py` validates only the algebra:

$$
\kappa_{\rm fixture}=1.09375,
\qquad
\Gamma_{\rm fixture}=0.9.
$$

It is explicitly non-physical.

## 9. Zeeman dimensional test

`test_sg_physical_zeeman.py` converts external apparatus data into:

$$
\Delta
=
\frac{|g_{\rm geom}|\mu_B}{\hbar}|B_\perp|,
$$

$$
v
=
\frac{|g_{\rm geom}|\mu_B}{\hbar}
|\partial_tB_\parallel+\mathbf u\cdot\nabla B_\parallel|.
$$

For the preserved test:

$$
\Delta=1.760859628909\times10^9\,{\rm s}^{-1},
$$

$$
v=8.804298144544\times10^{14}\,{\rm s}^{-2},
$$

$$
P_{\rm LZ}=0.
$$

This result means that, for these apparatus data, the passage is extremely adiabatic in the reduced model.
