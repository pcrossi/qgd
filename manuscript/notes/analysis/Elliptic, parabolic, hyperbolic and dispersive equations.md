---
title: "Elliptic, parabolic, hyperbolic and dispersive equations"
type: note
---

# Elliptic, parabolic, hyperbolic and dispersive equations

## Why classify equations

The local classification of a differential equation is determined by the principal part of the operator. However, the differential expression alone does not define the entire physical problem. It is also necessary to specify the domain, initial data, and boundary or radiation conditions.

This distinction, central in the treatments of Sommerfeld and Morse–Feshbach, separates two questions:

1. what is the local type of the differential expression?
2. what physical and spectral problem has been defined for this expression?

We will use **equation type** for classification by the principal symbol and **boundary value problem** for the complete physical realization.

## Elliptic equations

The elementary example is the Laplace equation:

$$
\Delta u=0.
$$

It describes equilibrium configurations. In general, elliptic problems are formulated with boundary data and do not define causal temporal propagation.

The Helmholtz equation provides an important example. The spatial operator is elliptic, but, in an exterior domain, we still need to choose the asymptotic behavior. The Sommerfeld radiation condition selects outgoing or incoming waves. It does not change the elliptic type of the differential expression; it changes the admissible physical solution and the corresponding Green's function.

## Parabolic equations

The basic example is the heat equation:

$$
\frac{\partial u}{\partial\tau}
=\kappa\Delta u.
$$

It describes diffusion and smoothing. Initial data determine an evolution in which small-scale irregularities are dampened.

The Ricci flow has a parabolic character after correcting the degeneracy produced by diffeomorphism invariance.

## Hyperbolic equations

The basic example is the wave equation:

$$
\frac{\partial^2u}{\partial t^2}
-c^2\Delta u=0.
$$

Perturbations propagate with a finite causal domain. Lorentzian operators, such as the Klein–Gordon operator, belong to this class under usual conditions.

The hyperbolic symbol alone also does not choose between advanced and retarded propagators. This choice depends on the data and the causal prescription imposed on the problem.

## Dispersive equations

The Schrödinger equation is

$$
i\hbar\frac{\partial\psi}{\partial t}
=H\psi.
$$

It is of first order in time and is not hyperbolic in the same sense as the wave equation. It is classified as dispersive: different spectral components accumulate different phases, producing propagation and interference without the characteristic damping of heat.

## Relationship with Euclidean continuation

A continuation between Lorentzian time and Euclidean time can relate hyperbolic operators to elliptic operators, and unitary evolution to diffusive semigroups. This relationship depends on the operator, the spectrum, the domain, and the boundary conditions; it is not an automatic consequence of replacing one letter with another.

## The equation and the boundary value problem

In the language of mathematical physics, the same differential expression can generate distinct operators when it receives different domains or boundary conditions. Schematically:

$$
\boxed{
\text{physical operator}
=\text{differential expression}
+\text{domain}
+\text{boundary conditions}.
}
$$

The boundary conditions can determine:

- existence and uniqueness;
- self-adjointness;
- discrete or continuous spectrum;
- edge modes and resonances;
- stability;
- incoming or outgoing solutions;
- advanced, retarded, or Euclidean Green's function.

It is in this sense that they participate in the physical classification of the problem. They do not alter, in general, the local discriminant of the equation, but they determine which realization of the operator represents the observed system.

This is the care found in *Partial Differential Equations in Physics*, by Arnold Sommerfeld, and in *Methods of Theoretical Physics*, by Philip M. Morse and Herman Feshbach: equation, domain, boundary, Green's function, and spectrum must be treated as parts of the same mathematical problem.

## Application in GDQ

In the manuscript, we will use:

- **elliptic** for spatial operators and stationary problems;
- **parabolic** for the flow and diffusion sector;
- **hyperbolic** for relativistic Lorentzian propagation;
- **dispersive or unitary** for the Schrödinger evolution.

This convention avoids calling all quantum dynamics hyperbolic and makes the proposed bridge between the different sectors more precise. For each GDQ operator, we will record separately:

1. principal symbol;
2. domain;
3. initial and boundary conditions;
4. causal prescription;
5. spectral realization.

[[index|← Analysis and Probability]]
