---
title: Q25 sign problem algorithm
status: closed-structural-reduced-benchmark
source: questoes/q25/questao_25.md
updated: 2026-07-21
---

# Q25 sign problem algorithm

GDQ has closed Q25 structurally and operationally in the reduced physical
benchmark. Stronger metrological/asymptotic extensions are future work.

Operational update: a minimal self-contained positive-domain/holonomy pipeline
was implemented and executed in `questoes/q25/associados/`, with consolidated
output in `questoes/q25/resultados/saida_q25_validacao.md`.

Validated in the reduced class:

1. positive local domain weights;
2. closed unitary and open contractive interface matrices;
3. exchange holonomy `Hol(P_ij)=-1`;
4. finite holonomy-sensitive estimator sampled with positive measure;
5. comparison against an exact finite integral;
6. autocorrelation and spectral mixing bound in a local domain chain;
7. local experimental-data schema without fabricated values.

Physical reduced-benchmark update: `q25_run_physical_benchmark.py` was
implemented and executed. It builds a 2D lattice/apparatus, positive reduced
GDQ Hessian, unitary interfaces from impedance/Cayley transform, spin/circulation
correlations, exact finite enumeration at `L=4`, and a scaling test at
`L=4,6,8`. The reduced test found positive Hessian
`lambda_min=0.18`, interface unitarity error around `2.61e-16`,
`C_s(1)_exact≈-0.1698717`, `C_s(1)_MC≈-0.16836`, and
`tau_corr ~ N^0.934` in the tested range.

Comparison update: quantitative Parsons 2016 values were locally extracted.
The reduced GDQ benchmark reproduces the sign and order of magnitude of the
cold nearest-neighbor correlator,
`C_s(1)_exp=-0.190(8)` versus `C_s(1)_GDQ_red≈-0.1698717`, i.e. `z≈2.516`.
It does not pass as a metrological description of all extracted data: the
reduced correlation length `xi≈0.918` is too long relative to the Parsons
values `0.24–0.51` sites. This points to the missing thermal/apparatus map and
full GDQ Hessian.

Thermal ensemble update: `q25_16_thermal_ensemble_map.py` was implemented.
It scans the positive reduced GDQ ensemble
`P(x; beta_eff) ∝ exp[-beta_eff E_GDQ_red(x)]` and inverts
`C_s(1)(beta_eff)` for the digitized Fig. 2D points. The digitized curve is
representable by variable `beta_eff`; a phenomenological fit gives
`beta_eff ≈ 0.291786/(kBT/t + 0.050000)`. This is an operational thermal-map
inversion, not a derivation from the full GDQ apparatus Hessian.

Reduced-Hessian invariant test: `q25_17_hessian_thermal_map_candidates.py`
tested whether scalar invariants of the reduced Hessian determine the thermal
map without fitting. They capture the decreasing trend but fail quantitatively;
the best no-target candidate `beta=m_gap/(kBT/t+m_gap)` has RMS relative error
about `0.418`. Therefore the missing object is not the ensemble itself but the
full thermal/apparatus block: causal mobility, bath admittance, thermodynamic
boundary conditions and coupling to the measured Hessian mode.

Effective apparatus block update: `q25_18_thermal_apparatus_block.py`
implements the boundary admittance map
`beta_eff(Theta)=mu_A/(Theta+Theta_A)`, with `Theta=kBT/t`. No-target
Hessian-derived candidates still fail quantitatively. If `(mu_A,Theta_A)` are
allowed as effective apparatus data, the best fit gives
`mu_A≈0.573747`, `Theta_A≈0.721528`, RMSE beta `≈0.0896`. Classification:
effective apparatus model fitted to the thermal map, not final derivation from
the official action.

Schur apparatus update: `q25_19_schur_apparatus_derivation.py` decomposes the
reduced Hessian into measured edge mode plus orthogonal apparatus/bath:
`K=[[K_H,J],[J^T,K_A]]`. It finds `K_H≈1.93`, `chi_A≈0.222954`,
`K_Schur≈1.707046`, `chi_2≈0.159323`. Best no-fit Schur candidate gives
`mu_A≈0.554522`, `Theta_A≈0.616922`, RMSE beta `≈0.1028`, close to the fitted
apparatus values `mu_A≈0.573747`, `Theta_A≈0.721528`, RMSE `≈0.0896`. This
nearly recovers the thermal admittance, but not the residual bath width.

Bath-width correction update: `q25_21_bath_width_correction.py` tests spectral
bath corrections over apparatus modes. Target residual was
`DeltaTheta_A≈0.104606`. The best reduced spectral correction gives
`DeltaTheta_A_bath≈0.074983`, hence `Theta_A≈0.691904` versus fitted
`Theta_A≈0.721528`; remaining residual is about `0.0296`. This explains most
of the residual width, but not all.

Required closure:

Remaining refinements have been moved to `ideias/possibilidades.md`:

1. additional quantitative data extraction from Cheuk, Mazurenko and Koepsell;
2. redigitize Parsons Fig. 2D with better error bars;
3. derive the final residual width `~0.0296` from causal mobility, real
   thermal weights or omitted dissipative apparatus channels;
4. full GDQ Hessian of the apparatus/background, beyond the reduced fixture;
5. larger scaling tests and polynomial variance/complexity proof.

Domain decomposition with transmission/reflection matrices is the proposed
route to make the geometric surgery idea simulable.

Manuscript preservation update: the final reduced benchmark is now
self-contained in `manuscrito/18_confinement_signal_problem/`. The relevant
files are:

1. `18.4 - Benchmark reduzido de sistemas fermionicos.md`;
2. `notes/confinement/benchmark_fisico_reduzido_sinal.md`;
3. `scripts/benchmark_fisico_reduzido_sinal.py`;
4. `scripts/saida_benchmark_fisico_reduzido_sinal.md`.

The manuscript no longer needs to reference `questoes/q25` for the preserved
chain: positive measure, fermionic holonomy, reduced Hessian, Cayley interface,
finite enumeration, Monte Carlo check, Schur thermal curve and external
comparison are included there. Historical exploratory scripts remain in
`questoes/q25`.
