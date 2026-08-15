---
title: "Upper channels of g-2"
---

# Upper channels of $g-2$

## 1. Statement

This note records what has actually been closed regarding the upper terms of $g-2$ in QGD.

The leading term is closed:

$$
a^{(1)}=\frac{\alpha}{2\pi}.
$$

The complete metrological problem is to calculate, for each lepton:

$$
a_\ell
=
\frac{1}{\gamma_{0,\ell}}
\frac{
\langle c_\ell,H_{C,\ell}^{+}m_{\perp,\ell}\rangle
}{
\langle c_\ell,H_{C,\ell}^{+}c_\ell\rangle
}.
$$

The object that replaces diagrams in QGD is, therefore:

$$
H_{C,\ell}^{+}m_{\perp,\ell}.
$$

## 2. Formal expansion of the Hessian

Write:

$$
H_C
=
H_0+\alpha H_1+\alpha^2H_2+\cdots,
$$

$$
m_\perp
=
\alpha m_1+\alpha^2m_2+\cdots.
$$

The physical pseudoinverse must be expanded on the complement of zero modes and constraints:

$$
H_C^+
=
H_0^+
-\alpha H_0^+H_1H_0^+
+O(\alpha^2).
$$

Therefore:

$$
a_\ell
=
\alpha
\frac{
\langle c,H_0^+m_1\rangle
}{
\gamma_0\langle c,H_0^+c\rangle
}
+O(\alpha^2).
$$

The leading condition of QGD is:

$$
\frac{
\langle c,H_0^+m_1\rangle
}{
\gamma_0\langle c,H_0^+c\rangle
}
=
\frac{1}{2\pi}.
$$

## 3. Computable leading block

The reduced block that performs this contraction is:

$$
H_{\rm lead}
=
\begin{pmatrix}
1 & -1\\
-1 & 2\pi/\alpha
\end{pmatrix},
\qquad
c=
\begin{pmatrix}
1\\0
\end{pmatrix},
\qquad
m_\perp=
\begin{pmatrix}
0\\1
\end{pmatrix}.
$$

It satisfies exactly:

$$
\frac{\langle c,H_{\rm lead}^{-1}m_\perp\rangle}
{\langle c,H_{\rm lead}^{-1}c\rangle}
=
\frac{\alpha}{2\pi}.
$$

With $\alpha^{-1}=137.035999177$:

$$
a^{(1)}
=
1.161409732097664\times10^{-3}.
$$

## 4. Observed metrological residuals

Comparing only after the derivation of the leading term:

| case | $a_{\rm obs}-a^{(1)}$ | aggregated coefficient in $(\alpha/\pi)^2$ |
|---|---:|---:|
| electron | $-1.7575515076\times10^{-6}$ | $-0.325744542535$ |
| muon | $4.5108579023\times10^{-6}$ | $0.836042265346$ |

These coefficients are not derived. They measure the size that the upper physical Hessian will need to produce.

## 5. Inverse diagnostic and non-uniqueness

It is possible to construct artificial blocks with an upper channel:

$$
H=
\begin{pmatrix}
1 & -1 & -J_2\\
-1 & K_1 & 0\\
-J_2 & 0 & K_2
\end{pmatrix},
\qquad
m_\perp=(0,1,\mu_2).
$$

By choosing $\mu_2$ based on the experimental target, the observed value is recovered. But this is an inverse diagnostic, not a prediction.

For the electron and muon, a particular choice yields:

| case | $\mu_2^{\rm required}$ | classification |
|---|---:|---|
| electron | $-1.5132915275\times10^{-3}$ | inverse diagnostic |
| muon | $8.0307898069\times10^{-1}$ | inverse diagnostic |

The non-uniqueness audit shows that the same observed value is reconstructed by many triples $(J_2,K_2,\mu_2)$. Therefore, $\mu_2^{\rm required}$ is not a derived observable.

## 6. Extraction of channels when the Hessian is given

Given a file or physical operator containing $H$, $c$, and $m_\perp$, the algorithm is:

1. normalize the protected axis:

$$
e_0=\frac{c}{\lVert c\rVert};
$$

2. project the complement:

$$
P_\perp=I-e_0e_0^\dagger;
$$

3. diagonalize:

$$
P_\perp HP_\perp e_i=K_i e_i;
$$

4. calculate:

$$
J_i=-\langle e_0,He_i\rangle,
\qquad
\mu_i=\langle e_i,m_\perp\rangle.
$$

If the input is an official projected Hessian, these coefficients are derived. If the input is a `required` block, they only recover the reverse engineering embedded in the block.

## 7. Reduced official Galerkin

A reduced Galerkin truncation directly inspired by the official action was tested, with:

$$
f=F+iP,
\qquad
\mathcal U=e^{-F}.
$$

The coordinates were:

| index | mode |
|---:|---|
| 0 | circulation/linear phase on the cycle |
| 1 | leading harmonic $\sin\theta$ |
| 2 | upper harmonic $\sin2\theta$ |
| 3 | density $\operatorname{Re}f\cos\theta$ |
| 4 | conformal metric $\cos\theta$ |

Result:

1. the bare action provides $H$ and $c$;
2. without an external magnetic source, $m_\perp^{\rm naked}=0$ and $a=0$;
3. the magnetic source must come from the physical map $M[\Phi;B]$;
4. the simple truncation possesses negative modes and is not the physical leptonic saddle.

This result is important: it prevents calling an unstable truncation a metrological prediction.

## 8. Effective leptonic background and magnetic source

The weak magnetic map is:

$$
M[\Phi;B]
=
B\left(\gamma_0\mathcal C[\Phi]+M_\perp[\Phi]\right).
$$

The minimal part is protected:

$$
M_{\rm min}=B\gamma_0\mathcal C.
$$

The leading transverse part is the harmonic component:

$$
M_\perp^{(1)}=B A_h[\Phi],
\qquad
\langle h,h\rangle=\frac{1}{2\pi}.
$$

The minimal effective backgrounds preserve:

| lepton | $M_\ell/M_e$ | effective $K_2$ | $a$ obtained |
|---|---:|---:|---:|
| electron | $1$ | $8.6102257658\times10^2$ | $\alpha/(2\pi)$ |
| muon | $206.7685934706$ | $1.7803242711\times10^5$ | $\alpha/(2\pi)$ |
| tau | $3477.4464050984$ | $2.9941598636\times10^6$ | $\alpha/(2\pi)$ |

They show that the hierarchy provides background stiffness, but does not create by itself the upper residual.

## 9. Hodge selection rule

For a uniform magnetic field on the Noether cycle:

$$
h=\frac{d\vartheta}{2\pi}.
$$

Exact upper modes have the form:

$$
e_k\propto d\sin(k\vartheta),
\qquad
k\ge1.
$$

Since $h$ is harmonic and $e_k$ is exact:

$$
\langle h,e_k\rangle=0.
$$

Numerically, the preserved test yields:

$$
\langle h,e_1\rangle\simeq -4.36\times10^{-17},
\qquad
\langle h,e_2\rangle\simeq -2.72\times10^{-17}.
$$

Therefore:

$$
\mu_{2,\ell}^{\rm direct}=0.
$$

Consequence: the universal correction cannot be a new direct linear source in a uniform magnetic field.

## 10. Hessian mixture and density channel

The first allowed universal mechanism is a Hessian correction:

$$
H_C=H_0+\alpha H_1+\cdots.
$$

The harmonic selection yields:

$$
\cos^2\theta
=
\frac12(1+\cos2\theta).
$$

Removing the constant mode:

$$
\beta_{12}
=
\langle u_2,u_1^2-\langle u_1^2\rangle\rangle
=
\frac{1}{2\sqrt\pi}
\simeq
0.282094791773878.
$$

The reduced test with:

$$
(H_1)_{12}=(H_1)_{21}
=
\beta_{12}\sqrt{K_1K_2}
$$

is stable, but alters $a$ only in the last recorded digits:

$$
a\simeq1.1614146537\times10^{-3}.
$$

The local test of upper variations shows that the robust cubic coupling in the reduced action is not leading squared directly to the upper mode, but rather mediated by the density:

$$
T_{123}
\simeq
-6.2831748693
\simeq
-2\pi.
$$

Thus, the relevant correction has the form:

$$
\Delta H_{12}
=
\eta_\ell T_{123},
$$

where $\eta_\ell$ must be calculated from the physical leptonic saddle.

## 11. Reduced angular saddle

The normalized reduced angular saddle varies:

$$
y=(a_1,a_2,\eta,\sigma),
$$

with fixed circulation:

$$
P'
=
\frac{1}{2\pi}
+a_1\cos\theta
+2a_2\cos2\theta.
$$

The measure constraint is:

$$
\frac{1}{2\pi}
\int_0^{2\pi}\rho\sqrt g\,d\theta
=1.
$$

The only normalized stationary root found in the reduced model is:

$$
a_1=a_2=\eta_\ell=\sigma=0.
$$

The final numerical value was:

$$
\eta_\ell\simeq -1.34\times10^{-9},
$$

with negative eigenvalue of the Hessian:

$$
\lambda_{\min}\simeq -6.247\times10^{-2}.
$$

Therefore, the reduced homogeneous angular saddle is not the physical 8D leptonic saddle and cannot produce the metrological correction.

## 12. Status

Structurally closed:

- Zeeman by Noether and isotropy;
- $g_0=2$;
- $a^{(1)}=\alpha/(2\pi)$;
- the Hessian operator that defines the anomaly;
- the non-uniqueness of the inverse upper channels;
- the selection rule $\mu_2^{\rm direct}=0$ for uniform field;
- the density-mediated route for upper corrections.

Remains metrological/future:

- solve the stable 8D leptonic saddle $\Phi_\ell$;
- calculate $H_{C,\ell}$, $T_{ijk}$, $Q_{ijkl}$ and $M[\Phi;B]$ on this saddle;
- obtain $\eta_\ell$ or the complete non-homogeneous density profile;
- re-run the same extractor without using experimental $g-2$ as target.
