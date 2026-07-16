---
title: Boundary conditions from variation
status: active
concepts:
  - boundary
  - interface
  - Robin
  - DtN
---

# Boundary conditions from variation

## Definition

Boundary/interface conditions in GDQ arise from the first variation:

$$
\delta\mathcal S\big|_{\partial M}
=\int_{\partial M}\Pi_A\,\delta\Phi^A.
$$

To make the problem well-posed one must specify how this term vanishes or is
balanced.

## Legitimate closures

1. Dirichlet: fix the field trace.
2. Neumann: fix or vanish the normal momentum.
3. Robin/interface: relate field trace and normal momentum through a derived
   interface response.
4. Apparatus/source: balance object flux with declared external source.

## Caution

Dirichlet-to-Neumann and Robin coefficients must come from the solved internal
domain, an interface action or declared apparatus data. They cannot be chosen
after the spectrum is known and then called derived.

## Sources

- `manuscrito/05_equations_conservation/05.3 - Variação da fase e conservação do fluxo.md`
- `manuscrito/05_equations_conservation/05.4 - Variação da densidade e equilíbrio dinâmico.md`
- `manuscrito/05_equations_conservation/05.6 - Noether, vínculos e condições de bordo.md`
