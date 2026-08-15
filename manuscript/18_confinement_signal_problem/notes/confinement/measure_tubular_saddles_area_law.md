---
title: "Measure of tubular saddles and area law"
---

# Measure of tubular saddles and area law

This note formalizes the transition between the GDQ tubular saddle and the area law.

## 1. Functional Sectors

For a closed contour $C$, consider:

1. $\mathfrak C_0$: vacuum sector;
2. $\mathfrak C_C$: sector with holonomy required by $C$;
3. $q_C^\ast$: Ricci--Bohm tubular saddle of least real part of the action in $\mathfrak C_C$.

The classical difference has an extensive form:

$$
{\rm Re}\,\mathcal S[q_C^\ast]
-
{\rm Re}\,\mathcal S[q_0]
=
\sigma_{\rm cl}A_{\min}(C)
+\mu_{\rm cl}P(C)
+O(1).
$$

Here $\sigma_{\rm cl}>0$ is the cost per area of the tube worldsheet.

## 2. Physical Thimble

The causal contour of GDQ is complex. Therefore, the global positive measure is not presumed. In the semiclassically stable regime, we use the steep descent thimble $\mathcal J_C$ that passes through $q_C^\ast$.

On this thimble:

1. ${\rm Im}\,\mathcal S$ is constant;
2. ${\rm Re}\,\mathcal S$ grows away from the saddle;
3. the physical Hessian has no negative directions after removing collective modes.

With spectral cutoff $N$:

$$
Z_C^{(N)}
=
\int_{\mathcal J_C^{(N)}}
d\mu_N(q)
\exp
\left[
-\frac{{\rm Re}\,\mathcal S_N[q]}{\hbar}
\right].
$$

## 3. Holonomy Response

The normalized response is:

$$
\langle\mathcal H(C)\rangle_N
=
e^{i\Theta_C}
\frac{Z_C^{(N)}}{Z_0^{(N)}}.
$$

In the Laplace limit:

$$
-\hbar\log
\left|
\langle\mathcal H(C)\rangle_N
\right|
=
\Delta S_{\rm cl}(C)
+\frac\hbar2
\log
\frac{\det{}'\mathcal H_C^{(N)}}
{\det{}'\mathcal H_0^{(N)}}
+O(\hbar^2).
$$

## 4. Effective Tension

By locality along the tube and transverse gap:

$$
\frac\hbar2
\log
\frac{\det{}'\mathcal H_C}
{\det{}'\mathcal H_0}
=
\delta\sigma\,A_{\min}(C)
+\delta\mu\,P(C)
+o(A).
$$

Define:

$$
\sigma_{\rm eff}
=
\sigma_{\rm cl}
+\delta\sigma
+O(\hbar^2).
$$

## 5. Existence of the Area Limit

If two large surfaces are glued along a boundary of length $L_\partial$, locality gives:

$$
F(A_1+A_2)
\le
F(A_1)+F(A_2)+cL_\partial,
$$

where:

$$
F(A)
:=
-\hbar\log|Z_C/Z_0|.
$$

For rectangles with bounded aspect ratio, the boundary term divided by the area tends to zero. The subadditive argument guarantees:

$$
\sigma_{\rm eff}
=
\lim_{A\to\infty}
\frac{F(A)}{A}.
$$

If $\sigma_{\rm eff}>0$, then:

$$
\left|
\langle\mathcal H(C)\rangle
\right|
=
\exp
\left[
-\frac{\sigma_{\rm eff}}{\hbar}A_{\min}(C)
-\frac{\mu_{\rm eff}}{\hbar}P(C)
+o(A)
\right].
$$

For rectangular $C_{R,T}$:

$$
V(R)
=
-\lim_{T\to\infty}
\frac\hbar T
\log
\left|
\langle\mathcal H(C_{R,T})\rangle
\right|
=
\sigma_{\rm eff}R+O(1).
$$

## 6. Status

The area law is a conditional theorem of GDQ under:

1. existence of the tubular thimble;
2. isolated saddle with $\sigma_{\rm cl}>0$;
3. physical Hessian with transverse gap;
4. spectral limit preserving locality and subadditivity.

This is sufficient for the structural closedness of this sector. It is not a complete mathematical construction of the Clay problem of pure Yang--Mills.
