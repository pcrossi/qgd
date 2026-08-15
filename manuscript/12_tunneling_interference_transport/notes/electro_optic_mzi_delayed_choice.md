---
title: "EO-MZI interferometer and delayed choice"
---

# EO-MZI interferometer and delayed choice

This note records the reduced material application of delayed choice to an electro-optic Mach--Zehnder interferometer. It does not replace the official action of GDQ; it uses the chapter as a laboratory reduction:

$$
\mathcal S_{\rm GDQ}
\to
\text{reduced Madelung sector}
\to
\text{interferometer}
\to
\textsf{R}_{\rm app}(t)
\to
\Gamma_{\rm det}
\to
\mathcal C_{\rm det}.
$$

## 1. External apparatus data

For a concrete evaluation, we freeze an EO-MZI switch with:

$$
\lambda=1550\,{\rm nm},
\qquad
V_\pi=2{,}445\,{\rm V},
\qquad
\tau_{\rm sw}=18{,}1\,{\rm ps},
$$

and power crosstalk limit:

$$
{\rm XT}=-30\,{\rm dB}.
$$

These numbers are external apparatus data. They are not axioms of GDQ and do not enter the fundamental action.

The corresponding power crosstalk is:

$$
p_{\rm leak}=10^{-3}.
$$

If the leakage is of power, the residual amplitude coherence is:

$$
\mathcal C_{\rm app}
=
\sqrt{p_{\rm leak}}
=
3{,}162277660168\times10^{-2}.
$$

## 2. Temporal impedance of the apparatus

Delayed choice is modeled as temporal impedance:

$$
\textsf{R}_{\rm app}(t)
=
\textsf{R}_{\rm off}
+
s(t-t_c)
\left(
\textsf{R}_{\rm on}
-
\textsf{R}_{\rm off}
\right).
$$

We use the smooth switch:

$$
s(t-t_c)
=
\frac{1}{1+\exp[-(t-t_c)/\tau_{\rm sw}]}.
$$

In the ideal recombined state:

$$
\textsf{R}_{\rm off}=0.
$$

In the distinguishable state, the asymptotic cost is:

$$
\Gamma_{\rm on}
=
-\ln\mathcal C_{\rm app}
=
-\ln\sqrt{p_{\rm leak}}
=
3{,}453877639491.
$$

Since:

$$
\Gamma_{\rm det}
=
\frac12
\langle
\Delta\Phi_\partial,
\textsf{R}_{\rm app}\Delta\Phi_\partial
\rangle,
$$

and we adopt the reduced normalization:

$$
\|\Delta\Phi_\partial\|^2=2,
$$

it follows:

$$
\textsf{R}_{\rm on}
=
\Gamma_{\rm on}
=
3{,}453877639491.
$$

## 3. Causal kernel

The history of the apparatus is weighted by a normalized causal kernel:

$$
w(t_f,t)
=
\frac{1}{\tau_{\rm mem}}
\exp\left[
-\frac{t_f-t-t_{\rm prop}}{\tau_{\rm mem}}
\right]
\Theta(t_f-t-t_{\rm prop}).
$$

After normalization:

$$
\int w(t_f,t)\,dt=1.
$$

For the reduced test:

$$
\tau_{\rm mem}=\tau_{\rm sw}=18{,}1\,{\rm ps}.
$$

For a path of $1\,{\rm m}$ in air:

$$
t_{\rm prop}=\frac{L}{c}=3{,}33564095198\,{\rm ns}.
$$

The observed cost is:

$$
\Gamma_{\rm det}(t_f)
=
\frac12
\int
\langle
\Delta\Phi_\partial(t),
\textsf{R}_{\rm app}(t)
\Delta\Phi_\partial(t)
\rangle
w(t_f,t)\,dt.
$$

The coherence coefficient is:

$$
\mathcal C_{\rm det}(t_f)
=
e^{-\Gamma_{\rm det}(t_f)}.
$$

In the late limit:

$$
\Gamma_\infty=3{,}453877639491,
\qquad
\mathcal C_\infty
=
3{,}162277660168\times10^{-2}.
$$

Thus the residual amplitude coherence is exactly what is expected from the crosstalk of $-30\,{\rm dB}$ when this datum is used as a frozen input of the apparatus.

## 4. Reduced material Hessian

In the reduced Mach--Zehnder arm model, the lossless coupler is:

$$
C(\theta)
=
\begin{pmatrix}
\cos\theta & i\sin\theta \\
i\sin\theta & \cos\theta
\end{pmatrix}.
$$

The ideal $3\,{\rm dB}$ coupler satisfies:

$$
\theta=\frac{\pi}{4}.
$$

The propagation in the arms is:

$$
P(\phi,\eta)
=
\begin{pmatrix}
e^{i\phi/2} & 0 \\
0 & \eta e^{-i\phi/2}
\end{pmatrix},
$$

where $\eta$ measures amplitude imbalance. The total matrix is:

$$
T_{\rm MZI}
=
C(\theta_2)P(\phi,\eta)C(\theta_1).
$$

The electro-optic phase obeys:

$$
\phi(V)=\pi\frac{V}{V_\pi}.
$$

For:

$$
V=V_\pi,
\qquad
\theta_1=\theta_2=\frac{\pi}{4},
\qquad
\eta=1,
$$

the ideal result is:

$$
p_{\rm dark}^{\rm ideal}
=
3{,}749399456655\times10^{-33},
\qquad
p_{\rm bright}^{\rm ideal}=1.
$$

That is, the stationary crosstalk is zero in the ideal apparatus. Finite crosstalk belongs to material imperfections:

$$
K_{\rm app}^{\rm red}
=
K_0
+
\delta K_\phi
+
\delta K_\eta
+
\delta K_\theta
+
\delta K_{\rm loss}.
$$

The Schur complement provides:

$$
\textsf{R}_{\rm app}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

To produce $-30\,{\rm dB}$ through isolated imperfections, the reduced equivalences are:

$$
\delta\phi
=
6{,}322448399238\times10^{-2}\,{\rm rad},
$$

$$
\delta V
=
4{,}920557195241\times10^{-2}\,{\rm V},
$$

$$
\eta
=
0{,}938693139937,
$$

or:

$$
\delta\theta
=
3{,}161224199619\times10^{-2}\,{\rm rad},
$$

with power split:

$$
\sin^2\left(\frac{\pi}{4}+\delta\theta\right)
=
0{,}531591185416.
$$

## 5. Physical interpretation

The result separates three levels:

1. the official action provides the variational structure;
2. the reduced interferometer provides the domain and the apparatus impedance;
3. the finite crosstalk comes from $\delta K_{\rm app}$, i.e., material, manufacturing, losses, and concrete electro-optic response.

Therefore, delayed choice does not require physical retrocausality. It is:

$$
\boxed{
\text{temporal boundary change}
+
\text{causal transport of the response}
+
\text{final dissipative readout}
}
$$
