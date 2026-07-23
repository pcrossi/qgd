---
title: Q24 measurement model
status: conditionally-closed-asymptotic-record-and-basin-theorem
source: manuscrito/09_measurement_born_interface/notes/teorema_assintotico_registros_gdq.md
updated: 2026-07-21
---

# Q24 measurement model

Measurement is modeled as $S+A+E$ interaction, pointer-basis selection by the
apparatus/environment coupling, decoherence of off-diagonal terms and Born
probabilities from Q22. Unique outcome requires the additional GDQ hypothesis
that real microgeometry selects one basin of attraction.

Update 2026-07-16: Q24 is conditionally closed as an asymptotic record theorem.
The measurement operator is
$\mathcal H_{\rm meas}=P^{phys} Hess_{\Phi_*} S_{\rm GDQ}^{S+A+E}P^{phys}$.
Records are sectors/basins $R_i\leftrightarrow\Omega_i\leftrightarrow\Pi_i$.
If the apparatus sectors are self-adjoint and gapped with
$\Delta_{\rm meas}>0$, then off-diagonal coherences satisfy
$|\Gamma_{ij}(\tau)|\le C_{ij}e^{-\Delta_{ij}\tau}$ and the reduced state
converges to the Born-weighted diagonal mixture. Born weights come from Q22,
not from inserting them into a partition function. Unique ontological outcome
is now formulated as a conditional real-basin theorem: if the apparatus and
environment microgeometry admits a Morse/Lyapunov basin decomposition with
stable hyperbolic records and measure-zero basin boundaries, then almost every
real event converges to one record \(R_i\), with probability
\(\mu_{\rm init}(\mathcal B_i)=\operatorname{Tr}(\rho_SP_i)\).

Manuscript status: self-contained in Chapter 9. The technical note
`manuscrito/09_measurement_born_interface/notes/teorema_assintotico_registros_gdq.md`
defines the measurement operator as the projected official GDQ Hessian with
apparatus source/boundary data, establishes the Robin/DtN domain, gives the
boundary argument for self-adjointness, defines record sectors by Riesz
projectors, assumes a measurement gap, derives exponential suppression of
off-diagonal coherences, proves ideal repeatability, and states the conditional
Morse-basin theorem for unique outcomes. The script `simular_decoerencia_sae.py`
checks decoherence, exponential gap suppression and repeatability in a reduced
finite-dimensional model.
