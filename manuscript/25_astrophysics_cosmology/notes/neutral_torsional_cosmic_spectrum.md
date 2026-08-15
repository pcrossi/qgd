---
title: "Note — Cosmic Spectrum of Neutral Torsional Modes"
---

# Note — Cosmic Spectrum of Neutral Torsional Modes

## 1. Physical Hypothesis Examined

Consider two conjugate orientations of the neutral sector:

$$
\nu_i^{(+)}$$ and $$\nu_j^{(-)}.
$$

The sign designates torsional orientation, not electric charge. The channel:

$$
\nu_i^{(+)}+\nu_j^{(-)}
\longrightarrow
\gamma+\gamma
$$

is permitted only when:

1. the total torsional circulation can cancel;
2. the overlap between the modes is not forbidden;
3. energy, momentum, and angular momentum are conserved;
4. the radiative jet of the action in the cosmological background does not vanish.

The calculation in this note determines spectral positions. It does not assume that all encounters annihilate, nor that the photonic channel has unitary branching.

## 2. Energy per Photon

In the center of mass:

$$
P^\mu
=
p_i^\mu+p_j^\mu
=
(\sqrt{s_{ij}},\mathbf{0}).
$$

A single photon cannot carry $P^2=s_{ij}>0$. For two photons:

$$
P^\mu
=
k_1^\mu+k_2^\mu,
\qquad
k_1^2=k_2^2=0,
$$

and:

$$
E_{\gamma,*}^{(ij)}
=
\frac{\sqrt{s_{ij}}}{2}.
$$

In the cold limit:

$$
\boxed{
E_{\gamma,*}^{(ij)}
\simeq
\frac{m_i+m_j}{2}c^2.
}
$$

Thus:

$$
\boxed{
\lambda_{ij,*}
=
\frac{2hc}{(m_i+m_j)c^2}.
}
$$

## 3. Variational Coupling

The physical coefficient must come from the cosmological neutral background:

$$
\Phi_\nu^{\rm cos}
=
(g,J,H,f,\mathcal U)_nu.
$$

After projecting constraints and eliminating internal modes:

$$
C_{ij\gamma\gamma}^{\rm GDQ}
=
D^4\mathcal S_{\rm red}[\Phi_\nu^{\rm cos}]
[\eta_i^+,\eta_j^-,\psi_\gamma,\psi_\gamma]
-
D^3\mathcal S_{\rm red}
G_{\rm int}
D^3\mathcal S_{\rm red}.
$$

The cross section is:

$$
\langle\sigma v\rangle_{ij}
\propto
\int d\Pi_{\gamma\gamma}
\left|
C_{ij\gamma\gamma}^{\rm GDQ}
\right|^2.
$$

Since this jet has not yet been evaluated in the 8D background, absolute and relative intensities remain open.

## 4. Spectral Comb

The candidate inertial scales of the neutral sector are:

$$
m_1=0,
\qquad
m_2=8.798417219655\times10^{-3}\ {\rm eV},
\qquad
m_3=5.042386973059\times10^{-2}\ {\rm eV}.
$$

With the mean relic momentum included, one obtains:

| Channel | $E_{\gamma,*}$ | $\lambda_*$ |
|---|---:|---:|
| $\nu_1\bar\nu_1$ | $0.528$ meV | $2346.9\,\mu{\rm m}$ |
| $\nu_1\bar\nu_2$ | $4.671$ meV | $265.4\,\mu{\rm m}$ |
| $\nu_1\bar\nu_3$ | $25.477$ meV | $48.7\,\mu{\rm m}$ |
| $\nu_2\bar\nu_2$ | $8.814$ meV | $140.7\,\mu{\rm m}$ |
| $\nu_2\bar\nu_3$ | $29.620$ meV | $41.9\,\mu{\rm m}$ |
| $\nu_3\bar\nu_3$ | $50.427$ meV | $24.6\,\mu{\rm m}$ |

Crossed channels are conditional on off-diagonal overlaps. The first channel is thermal and broad because $m_1=0$ in the reduced minimum branch.

## 5. Temperature and Width

The cosmological reference condition is:

$$
T_{\nu,0}
=
\left(
\frac{4}{11}
\right)^{1/3}
T_{\gamma,0}.
$$

For:

$$
T_{\gamma,0}
=
2.72548\ {\rm K},
$$

it yields:

$$
T_{\nu,0}
=
1.9453546\ {\rm K}.
$$

The decoupled distribution has:

$$
\langle p_\nu\rangle
\simeq
3.151374\,k_BT_{\nu,0}.
$$

This produces a small thermal width in the two massive modes and a millimeter continuum for the massless mode.

## 6. Cosmological Transport

Redshift transforms:

$$
E_0
=
\frac{E_*}{1+z},
\qquad
\lambda_0
=(1+z)\lambda_*.
$$

In the homogeneous toy model with constant cross section, density $n_\nu(z)=n_{\nu,0}(1+z)^3$, and no depletion:

$$
\frac{dI}{dz}
\propto
\frac{1+z}{H(z)}.
$$

The kernel produced by this expression serves to localize the signature and test sensitivity. It does not replace the unique cosmological solver.

## 7. Band Comparison

COBE/DIRBE measured:

$$
\nu I_\nu(140\,\mu{\rm m})
=
25\pm7\ {\rm nW\,m^{-2}\,sr^{-1}},
$$

e:

$$
\nu I_\nu(240\,\mu{\rm m})
=
14\pm3\ {\rm nW\,m^{-2}\,sr^{-1}}.
$$

The position of channel $22$ is:

$$
\lambda_{22,*}
=
140.663\,\mu{\rm m},
$$

$0.474\%$ above the $140\,\mu{\rm m}$ band. The same line emitted at:

$$
z
=
0.7062
$$

arrives today at $240\,\mu{\rm m}$. Channel $12$ lies within the FIRAS domain, and channel $33$ lies close to the Spitzer $24\,\mu{\rm m}$ band.

This coincidence demonstrates spectral compatibility, not causal origin. The cosmic infrared background already has a substantial contribution from galaxies and dust.

## 8. Inverse Intensity Scale

To show the order of magnitude, and only as reverse engineering, assign the entire FIRAS intensity of:

$$
I_{\rm FIRAS}
=
14\ {\rm nW\,m^{-2}\,sr^{-1}}
$$

to the diagonal channel $22$ between $z=0$ and $z=5$. The bolometric intensity would be:

$$
I
=
\frac{c}{4\pi}
\langle\sigma v\rangle_{22}
n_{\nu,0}^2
(2m_2c^2)
\int_0^5
\frac{1+z}{H(z)}
\,dz.
$$

Inversion yields:

$$
\langle\sigma v\rangle_{22}^{\rm inv}
=
3.09675\times10^{-29}\ {\rm m^3\,s^{-1}},
$$

with optical depth:

$$
\tau_{\rm ann}
\simeq
1.22494\times10^{-2}.
$$

These values are not derived constants. The sensitivity test varies the inverse cross section from $1.31\times10^{-28}$ for $z_{\max}=1$ to $3.10\times10^{-29}\ {\rm m^3\,s^{-1}}$ for $z_{\max}=5$.

## 9. Falsifiable Signature

The appropriate test looks for:

1. a comb in the energy ratios $(m_i+m_j)/2$;
2. width compatible with the relic temperature;
3. tail towards larger wavelengths due to redshift;
4. intensity ratios calculated by the overlaps;
5. component uncorrelated with dust;
6. neutral depletion compatible with cosmology.

The current result is:

$$
\boxed{
\text{position and normalized shape conditionally predicted;}
\quad
\text{brightness still open}.
}
$$

The script [[../scripts/neutral_torsional_cosmic_spectrum.py]] reproduces the comb, the redshift kernel, the band comparison, and the convergence tests.

## 10. Comparison References

- D. J. Fixsen, “The Temperature of the Cosmic Microwave Background,” *Astrophysical Journal* **707**, 916 (2009): <https://doi.org/10.1088/0004-637X/707/2/916>.
- M. G. Hauser et al., “The COBE Diffuse Infrared Background Experiment Search for the Cosmic Infrared Background,” *Astrophysical Journal* **508**, 25 (1998): <https://doi.org/10.1086/306379>.
- D. J. Fixsen et al., “The Spectrum of the Extragalactic Far-Infrared Background from the COBE FIRAS Observations,” *Astrophysical Journal* **508**, 123 (1998): <https://doi.org/10.1086/306383>.
- C. Papovich et al., “The 24 Micron Source Counts in Deep Spitzer Surveys,” *Astrophysical Journal Supplement Series* **154**, 70 (2004): <https://doi.org/10.1086/422880>.
- H. Dole et al., “The Cosmic Infrared Background Resolved by Spitzer,” *Astronomy & Astrophysics* **451**, 417 (2006): <https://doi.org/10.1051/0004-6361:20054446>.
