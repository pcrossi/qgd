---
title: Q26 spin one-half as effective spinorial sector
status: closed-structurally
source: manuscrito/10_spin_statistics_pauli/notes/spin_hopf_residuo_cauchy.md; manuscrito/10_spin_statistics_pauli/notes/estrutura_spin_em_R4_T4.md
updated: 2026-07-21
---

# Q26 spin one-half as effective spinorial sector

## Enunciado

No setor físico reconstruído da GDQ, spin $1/2$ é consequência da existência de
estrutura spin, da álgebra de Clifford e da representação espinorial de
$\mathrm{Spin}^+(3,1)$.

## Resultado

Se $(N,h)$ admite $P_{\rm Spin}(N)\to N$, então

$$
\psi\in\Gamma(S\otimes E),
\qquad
S=P_{\rm Spin}(N)\times_{\rho_D}\mathbb C^4.
$$

Com

$$
\{\gamma^\mu,\gamma^\nu\}=2h^{\mu\nu},
$$

a representação de Dirac é

$$
\left(\frac12,0\right)\oplus\left(0,\frac12\right).
$$

Portanto rotações espaciais satisfazem

$$
U(2\pi)=-I,
\qquad
U(4\pi)=I.
$$

## Status lógico

Fechado estruturalmente. A GDQ fornece interpretação torsional/vorticial do
spin, mas não substitui o fibrado spin por uma circulação inteira.

## Complemento Hopf--Cauchy

A formulação por resíduos foi fechada como complemento estrutural.

Em uma carta complexa transversal ao estômato, a seção spinorial local é

$$
s(z)=z^{1/2}s_0(z),
$$

com $s_0$ holomorfa e não nula. Portanto

$$
\Omega_S=d\log s
=
\frac12\frac{dz}{z}+d\log s_0,
\qquad
\operatorname{Res}_{z=0}\Omega_S=\frac12.
$$

Pelo teorema de Cauchy,

$$
\frac{1}{2\pi i}\oint_\gamma\Omega_S=\frac12.
$$

Assim,

$$
\oint_\gamma dS_R=\frac h2=\pi\hbar,
\qquad
\exp\left(
\frac{i}{\hbar}\oint_\gamma dS_R
\right)=-1.
$$

Duas voltas retornam $+1$. Isso realiza a mesma estrutura do recobrimento
duplo $S^3\simeq SU(2)\to SO(3)$ na fibração de Hopf.

## Não confundir

- circulação ou holonomia ajudam a interpretar a fase;
- o valor $1/2$ vem da representação spinorial e é reproduzido localmente como
  resíduo Cauchy--Hopf da meia-monodromia;
- Stern--Gerlach mede a resposta do objeto spinorial a uma sonda, não cria o
  spin.

## Preservação no manuscrito

O resultado está autocontido no Capítulo 10 do manuscrito, especialmente em:

1. `manuscrito/10_spin_statistics_pauli/10.4 - Estrutura spin e recobrimento duplo.md`;
2. `manuscrito/10_spin_statistics_pauli/10.6 - Rotação de 2pi e 4pi.md`;
3. `manuscrito/10_spin_statistics_pauli/notes/spin_hopf_residuo_cauchy.md`;
4. `manuscrito/10_spin_statistics_pauli/scripts/verificar_residuo_hopf_cauchy.py`.

O script de resíduo verifica numericamente a identidade
`(2 pi i)^(-1) int (1/2) dz/z = 1/2` para vários raios, com erro de
arredondamento da ordem de `1e-16`.
