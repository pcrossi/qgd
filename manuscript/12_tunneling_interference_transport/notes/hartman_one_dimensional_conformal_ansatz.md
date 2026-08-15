---
title: "Hartman as a conditional reduced theorem"
---

# Hartman as a conditional reduced theorem

## Statement

In the reduced one-dimensional evanescent sector:

$$
\Omega_L=[0,L],
\qquad
V_0>E,
$$

the stationary mode is:

$$
\psi(x)=\psi_0e^{-\kappa x},
\qquad
\kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar}.
$$

Therefore:

$$
\rho(x)=\rho_0e^{-2\kappa x}.
$$

In GDQ, this density is the Madelung reduction of the geometric field:

$$
\rho=e^{-(f+\bar f)/2}.
$$

What we want to prove is not superluminal propagation. The correct statement is:

1. the peak/group time can saturate with the width of the barrier;
2. this saturation is not front velocity;
3. the reduced GDQ provides a causal interpretation via saturated proper length;
4. the relation $g_{xx}\propto\rho$ is conditional on the evanescent sector, not a universal metric identity.

## Reduction hypotheses

The reduction uses:

1. stationary barrier;
2. evanescent mode;
3. real propagating current suppressed in the interior;
4. transverse modes frozen;
5. interface normalized at $x=0$;
6. longitudinal gauge of measurement;
7. minimization of the geometric energy of the channel.

Under these hypotheses, the admissible longitudinal solution is:

$$
g_{xx}(x)=g_0\frac{\rho(x)}{\rho_0},
$$

hence:

$$
g_{xx}(x)=g_0e^{-2\kappa x}.
$$

Classification:

$$
\boxed{
g_{xx}\propto\rho
\text{ is a conditional reduced solution, not a new axiom.}
}
$$

## Proper distance

The proper distance is:

$$
D_{\rm proper}(L)
=
\int_0^L\sqrt{g_{xx}(x)}\,dx.
$$

Since:

$$
\sqrt{g_{xx}(x)}
=
\sqrt{g_0}e^{-\kappa x},
$$

we have:

$$
D_{\rm proper}(L)
=
\frac{\sqrt{g_0}}{\kappa}
\left(1-e^{-\kappa L}\right).
$$

In the opaque limit:

$$
\lim_{L\to\infty}D_{\rm proper}(L)
=
\frac{\sqrt{g_0}}{\kappa}.
$$

This is the Hartman geometric saturation.

## Effective proper time

$$
\tau_{\rm GDQ}(L)
=
\int_0^L\frac{ds}{v_{\rm prop}(x)}.
$$

If, in the stationary regime, $v_{\rm prop}=v_0\le c$:

$$
\tau_{\rm GDQ}(L)
=
\frac{\sqrt{g_0}}{v_0\kappa}
\left(1-e^{-\kappa L}\right).
$$

Therefore:

$$
\lim_{L\to\infty}\tau_{\rm GDQ}(L)
=
\frac{\sqrt{g_0}}{v_0\kappa}.
$$

The saturated time is peak/group time or the channel's effective proper time. It is not front time.

## Comparison time with literature

The Hartman literature frequently uses phase time or the Wigner--Smith time:

$$
\tau_W(E)
=
\hbar
\frac{\partial}{\partial E}
\arg T(E).
$$

This time must be distinguished from the front time and the GDQ proper time.

## Packet deformation

For an incident packet:

$$
\Psi_{\rm in}(x,t)
=
\int A(E)e^{i(kx-\omega t)}\,dE,
$$

the transmitted packet is:

$$
\Psi_T(x,t)
=
\int T(E)A(E)e^{i(kx-\omega t)}\,dE.
$$

The group time approximation is legitimate when $A(E)$ is narrow and $T(E)$ is regular in the band. In opaque barriers, $T(E)$ filters the spectrum and can reshape the peak. A reshaped peak is not a superluminal signal.

## Causal front

The apparent coordinate velocity:

$$
v_{\rm coord}(L)=\frac{L}{\tau_{\rm GDQ}(L)}
$$

can grow as $L$ grows because $\tau_{\rm GDQ}$ saturates. But this ratio is not local velocity.

The local physical velocity is:

$$
v_{\rm prop}=\frac{ds}{dt}\le c,
$$

and the causal front obeys:

$$
v_{\rm front}\le c.
$$

Thus:

$$
\boxed{
\text{Hartman in GDQ is saturated proper length, not superluminal propagation.}
}
$$

## Scope and metrological pending issues

To compare with a specific experiment, it is necessary to declare:

1. exact shape of the barrier;
2. spectral band of the pulse;
3. operational definition of time;
4. detector;
5. front criterion;
6. material boundary.

These data belong to the experiment. They are not new axioms of GDQ.
