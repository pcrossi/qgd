---
title: Questão 26 — spin um meio
status: closed-structurally
source: questoes/q26/questao_26.md
updated: 2026-07-16
---

# Questão 26 — spin um meio

## Estado vigente

A Q26 está fechada estruturalmente.

O spin $1/2$ não é reduzido a uma circulação escalar inteira. Ele surge do
setor spinorial efetivo da GDQ: o espaço físico reconstruído deve admitir
fibrado spin e os campos fermiônicos são seções de $S\otimes E$.

## Cadeia registrada

1. A Q2 fornece o bulk local $M=\mathbb R^4\times T^4$.
2. Como $TM$ é trivial, $w_2(TM)=0$ e o bulk admite estrutura spin.
3. As estruturas spin de $T^4$ são classificadas por
   $H^1(T^4,\mathbb Z_2)\simeq(\mathbb Z_2)^4$, gerando 16 possibilidades.
4. No espaço-tempo físico efetivo $(N,h)$ exige-se $w_2(TN)=0$.
5. O fibrado principal $P_{\rm Spin}(N)\to N$ levanta o fibrado ortonormal.
6. O campo fermiônico é $\psi\in\Gamma(S\otimes E)$, com
   $S=P_{\rm Spin}\times_{\rho_D}\mathbb C^4$.
7. A álgebra de Clifford satisfaz $\{\gamma^\mu,\gamma^\nu\}=2h^{\mu\nu}$.
8. A representação relevante de $\mathrm{Spin}^+(3,1)\simeq SL(2,\mathbb C)$ é
   $(1/2,0)\oplus(0,1/2)$.
9. Sob rotação espacial, $U(2\pi)=-I$ e $U(4\pi)=I$.

## Interpretação GDQ

A torção/vorticidade de Cartan pode interpretar geometricamente o spin no
solíton. Porém o quantum $1/2$ vem da estrutura spinorial e do recobrimento
duplo $\mathrm{Spin}\to SO$, não de uma circulação escalar isolada.

## Complemento Hopf--Cauchy

A formulação por resíduos foi fechada em
`questoes/q26/associados/spin_hopf_residuo_cauchy.md`.

Em uma carta complexa transversal ao estômato:

$$
s(z)=z^{1/2}s_0(z),
\qquad
\Omega_S=d\log s
=
\frac12\frac{dz}{z}+d\log s_0.
$$

Logo:

$$
\operatorname{Res}_{z=0}\Omega_S=\frac12,
\qquad
\frac{1}{2\pi i}\oint_\gamma\Omega_S=\frac12.
$$

Na fase física:

$$
\oint_\gamma dS_R=\frac h2=\pi\hbar,
\qquad
\exp\left(
\frac{i}{\hbar}\oint_\gamma dS_R
\right)=-1.
$$

Isto reproduz $2\pi\mapsto -1$ e $4\pi\mapsto +1$ pela meia-monodromia de
Hopf/Cauchy, sem substituir a prova spinorial.

## Limitações

Permanecem posteriores:

- seleção dinâmica de uma das 16 estruturas spin;
- realização específica do setor de Dirac do elétron por um solíton;
- estabilização de todos os modos espinoriais;
- obtenção do espectro completo de partículas a partir de $\slashed D_{B,A}$.

## Ponteiros

- Resultado: `brain/conditional-results/q26-spin-half/index.md`
- Pendência: `brain/open-problems/q26-dynamic-spin-sector-selection/index.md`
