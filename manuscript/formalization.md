---
title: "Structural Map of Proofs and Formalizations"
---

# Structural Map of Proofs and Formalizations

## 1. Function of this document

This file connects three different layers:

$$
\text{didactic chapter}
\longrightarrow
\text{written mathematical proof}
\longrightarrow
\text{Lean verification}.
$$

The written proof remains in the manuscript. Lean code is a complementary certification: it verifies the formalized statements but does not replace the geometric hypotheses, domains, and physical meaning explained in the text.

The canonical modules are in `formal/GDQ/`. Experimental files in question folders do not constitute a citable proof by the manuscript.

The technical module-by-module catalog, with the exact names of the theorems, is in the [Canonical index of Lean proofs](../formal/index.md).

## 2. Status legend

- **formalized:** the indicated statement compiles in the canonical package;
- **partially formalized:** only the algebraic or reduced layer has been certified;
- **written proof:** there is a mathematical proof in the manuscript, but it is not yet fully translated into Lean;
- **not started:** there is no corresponding canonical Lean module.

## 3. Map by chapter

| Chapter | Mathematical core | Written proof | Canonical Lean modules | Status |
|---|---|---|---|---|
| [[01_initial_problem/index\|01 — Initial problem]] | Feynman--Wiener divergence and Bohm identity | chapter notes | [BohmIdentity](../formal/GDQ/BohmIdentity.lean) | local differential identity formalized; path integrals contrast remains an analytical explanation |
| [[02_geometrization/index\|02 — Geometrization]] | spaces, fields, measure and constitutive relations | chapter notes | [Spaces](../formal/GDQ/Spaces.lean), [LocalMeasure](../formal/GDQ/LocalMeasure.lean), [Constitutive](../formal/GDQ/Constitutive.lean), [Fields](../formal/GDQ/Fields.lean), [FlowKernel](../formal/GDQ/FlowKernel.lean), [Admissibility](../formal/GDQ/Admissibility.lean) | formalized at the structural core |
| [[03_complex_causality/index\|03 — Complex causality]] | causal boundary and exponential clock | chapter notes | [CausalContour](../formal/GDQ/CausalContour.lean), [ClockHomomorphism](../formal/GDQ/ClockHomomorphism.lean), [ComplexContourAction](../formal/GDQ/ComplexContourAction.lean) | formalized conditionally on the boundary |
| [[04_action_consistency/index\|04 — Action and consistency]] | density, official integral, integrability and Hessian | chapter notes | [ActionDensity](../formal/GDQ/ActionDensity.lean), [ActionIntegration](../formal/GDQ/ActionIntegration.lean), [OfficialAction](../formal/GDQ/OfficialAction.lean), [EuclideanOfficialAction](../formal/GDQ/EuclideanOfficialAction.lean), [ControlledIntegrability](../formal/GDQ/ControlledIntegrability.lean), [VariationalHessian](../formal/GDQ/VariationalHessian.lean), [PhysicalProjector](../formal/GDQ/PhysicalProjector.lean), [VariationalDynamics](../formal/GDQ/VariationalDynamics.lean) | formalized in the declared domain; the variational equation is primary and Hessian/projector are derived |
| [[05_equations_conservation/index\|05 — Equations and conservation]] | first variation, current, phase charge and Routh minimum | variation and Noether notes | [BohmIdentity](../formal/GDQ/BohmIdentity.lean), [PhaseFirstVariation](../formal/GDQ/PhaseFirstVariation.lean), [NoetherPhaseCurrent](../formal/GDQ/NoetherPhaseCurrent.lean), [NoetherIdentity](../formal/GDQ/NoetherIdentity.lean), [StokesChargeBalance](../formal/GDQ/StokesChargeBalance.lean), [BoundaryPhaseQuantization](../formal/GDQ/BoundaryPhaseQuantization.lean), [RouthMadelung](../formal/GDQ/RouthMadelung.lean) | pointwise variation, off-shell identity, weak conservation, and finite kernel of Routh minimum formalized; functional limit and dissipative attraction remain conditional |
| [[06_global_local_bridge/index\|06 — Global--local bridge]] | six lemmas, spectral transport, projectors and gap $C_3$ | chapter notes | [PhysicalProjector](../formal/GDQ/PhysicalProjector.lean), [VariationalDynamics](../formal/GDQ/VariationalDynamics.lean), [CosmologicalFamily](../formal/GDQ/CosmologicalFamily.lean), [GlobalLocalTransport](../formal/GDQ/GlobalLocalTransport.lean), [SpectralBridge](../formal/GDQ/SpectralBridge.lean), [GlobalLocalSixLemmas](../formal/GDQ/GlobalLocalSixLemmas.lean), [C3Application](../formal/GDQ/C3Application.lean), [C3ConcreteHessian](../formal/GDQ/C3ConcreteHessian.lean) | the six lemmas have explicit Lean statements and canonical composition; hypotheses Mosco/Agmon/Riesz hypotheses remain conditioned on the background, as in the human proof |
| [[07_classical_limit/index\|07 — Classical limit]] | Gaussian reduction and local correspondence | chapter notes | [GaussianOfficialReduction](../formal/GDQ/GaussianOfficialReduction.lean), [GaussianContourReduction](../formal/GDQ/GaussianContourReduction.lean), [GaussianBulkDomination](../formal/GDQ/GaussianBulkDomination.lean), [GaussianCausalDomination](../formal/GDQ/GaussianCausalDomination.lean), [GaussianAdmissibleBackground](../formal/GDQ/GaussianAdmissibleBackground.lean) | formalized in the declared Gaussian background |
| [[08_hilbert_quantization_uncertainty/index\|08 — Hilbert and quantization]] | OS reconstruction, circular phase, Chern class, relative quantization and uncertainty | chapter notes | [OSReconstruction](../formal/GDQ/OSReconstruction.lean), [OSReconstructedEvolution](../formal/GDQ/OSReconstructedEvolution.lean), [PhaseQuantization](../formal/GDQ/PhaseQuantization.lean), [PhaseReconstruction](../formal/GDQ/PhaseReconstruction.lean), [BoundaryPhaseQuantization](../formal/GDQ/BoundaryPhaseQuantization.lean), [CechChern](../formal/GDQ/CechChern.lean), [CechCohomology](../formal/GDQ/CechCohomology.lean), [Uncertainty](../formal/GDQ/Uncertainty.lean) | zero quotient and completion formalized under OS pairing; positivity and generator of each background remain conditional |
| [[09_measurement_born_interface/index\|09 — Measurement and Born]] | classical--quantum interface, source, Schur, basins and readouts | chapter notes | [FiniteBorn](../formal/GDQ/FiniteBorn.lean), [MixedBornTrace](../formal/GDQ/MixedBornTrace.lean), [MeasurementAsymptotic](../formal/GDQ/MeasurementAsymptotic.lean), [ClassicalApparatusResponse](../formal/GDQ/ClassicalApparatusResponse.lean), [ApparatusBornReadout](../formal/GDQ/ApparatusBornReadout.lean), [QNDBornBasins](../formal/GDQ/QNDBornBasins.lean) | linear response, Schur, spectral Born, and finite version of Born-basins formalized in the Gaussian QND sector; continuous capture uses the analytical separation theorem |
| [[10_spin_statistics_pauli/index\|10 — Spin and statistics]] | half-monodromy, Hopf, CAR and Pauli | chapter notes | [SpinHopfMonodromy](../formal/GDQ/SpinHopfMonodromy.lean), [CARPauli](../formal/GDQ/CARPauli.lean), [SpinStatisticsConditional](../formal/GDQ/SpinStatisticsConditional.lean) | half-monodromy and CAR $\Rightarrow$ Pauli formalized; hypotheses and application of the spin--statistics bridge are typed, but the relativistic analytical theorem remains external |
| [[11_stern_gerlach_classical_quantum/index\|11 — Stern--Gerlach]] | two-channel projectors, angular weights, interface Hessian and apparatus response | chapter notes and scripts | [SternGerlachProjectors](../formal/GDQ/SternGerlachProjectors.lean), [SternGerlachSequential](../formal/GDQ/SternGerlachSequential.lean), [SternGerlachInterface](../formal/GDQ/SternGerlachInterface.lean) | projectors, weights, sequences, free boundary condition, Schur/DtN, modal response, stiffness and Noether--Zeeman formalized in the reduced sector; real magnet remains metrology |
| [[12_tunneling_interference_transport/index\|12 — Transport and interference]] | kernels, boundaries and propagation | chapter notes and scripts | [DetectorDtNSchur](../formal/GDQ/DetectorDtNSchur.lean), [TransportInterference](../formal/GDQ/TransportInterference.lean) | DtN/Schur, attenuation, Hartman saturation, double-slit identity, and independence of future data outside the causal support formalized in the reduced sector |
| [[13_holonomies_ab_sagnac/index\|13 — Holonomies]] | Aharonov--Bohm and Sagnac | chapter notes and scripts | [AharonovBohmHolonomy](../formal/GDQ/AharonovBohmHolonomy.lean), [SagnacHolonomy](../formal/GDQ/SagnacHolonomy.lean), [HolonomyPatchingStokes](../formal/GDQ/HolonomyPatchingStokes.lean) | gauge invariance, gluing by lifts, cellular Stokes, and Sagnac ideal factor formalized; smooth application to each domain and response of real apparatus remain geometric/metrological data |
| [[14_geometric_particle_taxonomy/index\|14 — Taxonomy and generations]] | three centers, hypercharges, generators and local index | chapter notes | [C3Application](../formal/GDQ/C3Application.lean), [C3ConcreteHessian](../formal/GDQ/C3ConcreteHessian.lean), [GenerationJunction](../formal/GDQ/GenerationJunction.lean), [HyperchargeDiophantine](../formal/GDQ/HyperchargeDiophantine.lean), [KillingPoissonLie](../formal/GDQ/KillingPoissonLie.lean), [APSHopfBismut](../formal/GDQ/APSHopfBismut.lean) | $C_3$ sector, selection of $N=3$ under rank two and isolation, hypercharges, local Lie representation, and APS discrete kernel formalized; global existence of potentials and spectral flow remain geometric hypotheses |
| [[15_leptonic_hierarchy_masses/index\|15 — Leptonic hierarchy]] | torsional background and spectral operator | chapter notes and scripts | [ConformalBismutTorsion](../formal/GDQ/ConformalBismutTorsion.lean), [ConformalBismutConnection](../formal/GDQ/ConformalBismutConnection.lean), [ConformalBismutBackground](../formal/GDQ/ConformalBismutBackground.lean), [ConformalTorsionSaddle](../formal/GDQ/ConformalTorsionSaddle.lean), [ConformalTorsionHessian](../formal/GDQ/ConformalTorsionHessian.lean), [ConformalTorsionProjectedHessian](../formal/GDQ/ConformalTorsionProjectedHessian.lean), [ConformalTorsionConstraintTangent](../formal/GDQ/ConformalTorsionConstraintTangent.lean), [PerelmanProductReduction](../formal/GDQ/PerelmanProductReduction.lean), [KoideGeometry](../formal/GDQ/KoideGeometry.lean), [LeptonicHierarchy](../formal/GDQ/LeptonicHierarchy.lean) | $K_{aa}$, normalized tangent, 3D/8D product reduction, saturation and algebra of the reduced hierarchy formalized; universal derivation of coefficients, dynamic selection of the tau branch, and mixed backgrounds remain conditional |
| [[16_fine_structure_zeeman_gminus2/index\|16 — Fine structure and Zeeman]] | magnetic response and probe Hessian | chapter notes and scripts | [SternGerlachInterface](../formal/GDQ/SternGerlachInterface.lean), [MagneticResponse](../formal/GDQ/MagneticResponse.lean) | $g_0=2$ under minimal map, harmonic norm, leading term, Hessian decomposition and orthogonal channel cancellation formalized; cosmological $\alpha$ and higher $g-2$ remain conditional |
| [[17_baryonic_structure/index\|17 — Baryonic structure]] | torsional constraints, masses, Schur and beta | chapter notes and scripts | [BaryonicReduction](../formal/GDQ/BaryonicReduction.lean) | algebraic identities of the reduced model formalized; selection of the 8D saddle, surface coefficients, and the $\alpha^{-11}$ law remain conditional |
| [[18_confinement_signal_problem/index\|18 — Confinement and color]] | effective connection, Wilson and benchmark | chapter notes and scripts | [YMSectorIsomorphism](../formal/GDQ/YMSectorIsomorphism.lean), [AreaLawConditional](../formal/GDQ/AreaLawConditional.lean) | abstract isomorphism of the reduced algebras and area conditional limit formalized; concrete thimble, saddle, and gap remain background hypotheses |
| [[19_electroweak_geometric_breaking/index\|19 — Electroweak breaking]] | Hessian, Schur and mode stiffness | chapter notes and scripts | [ElectroweakStability](../formal/GDQ/ElectroweakStability.lean) | cancellation at fixed volume, positive quartic, reduced minima, Schur and neutral kernel formalized; background coefficients remain calculated inputs |
| [[20_gravity_cosmology/index\|20 — Gravitation and cosmology]] | global reduction, boundary, dilution and equations of state | chapter notes and scripts | [CosmologicalFamily](../formal/GDQ/CosmologicalFamily.lean), [GravityCosmology](../formal/GDQ/GravityCosmology.lean) | Newton group, horizon, conditional saddle/gluing, 28 channels, dilution, density, $w$ and $a_0$ formalized; complete background and cosmological Hessian remain conditional |
| [[21_cp_hopf_monopoles/index\|21 — Strong CP, monopoles and Hopf]] | topological classes and relaxation | chapter notes and scripts | [CechChern](../formal/GDQ/CechChern.lean), [CechCohomology](../formal/GDQ/CechCohomology.lean), [CPRelaxation](../formal/GDQ/CPRelaxation.lean) | topology and reduced Lyapunov kernel formalized; global convergence requires invariance/compactness of the physical flow |
| [[22_hydrogen_atom/index\|22 — Hydrogen atom]] | spectrum, spin--orbit and hyperfine | chapter notes and scripts | [HydrogenSpectrum](../formal/GDQ/HydrogenSpectrum.lean) | reduced mass, spectral symmetry, Coulombian degeneracy, fine splitting, hyperfine algebra, Zemach sign and Schur formalized; functional radial analysis and higher proton blocks remain conditional |
| [[23_simple_applications/index\|23 — Simple applications]] | well, oscillator, wall, Hartman, Casimir and rotor | chapter notes and scripts | [DetectorDtNSchur](../formal/GDQ/DetectorDtNSchur.lean), [TransportInterference](../formal/GDQ/TransportInterference.lean), [SimpleApplications](../formal/GDQ/SimpleApplications.lean) | ideal correspondence, DtN/Schur, saturation, Casimir coefficients and radial elimination formalized; real materials and molecular backgrounds remain conditional |
| [[24_nuclear_phenomenology/index\|24 — Nuclear phenomenology]] | alpha, spin--torsion shells, Klein--Nishina and neutrinos | chapter notes and scripts | [NuclearPhenomenology](../formal/GDQ/NuclearPhenomenology.lean) | reduced half-life, magic numbers, Thomson limit, positivity of the candidate neutral spectrum, and oscillation bound formalized; complete 8D Hessians and vertices remain conditional |
| [[25_astrophysics_cosmology/index\|25 — Astrophysics]] | solitons with horizon, cosmology and global normalizations | chapter notes and scripts | [GravityCosmology](../formal/GDQ/GravityCosmology.lean), [AstrophysicsCosmology](../formal/GDQ/AstrophysicsCosmology.lean) | regular core, torsional rigidity, Schur, temperature, channel entropy and normalizations formalized; 8D saddle, physical Page, and unique cosmological solver remain conditional |
| [[26_logical_status/index\|26 — Logical status]] | axioms, data, theorems, reductions and dependencies | chapter body | [LogicalStatus](../formal/GDQ/LogicalStatus.lean), [GDQ entry point](../formal/GDQ.lean) | taxonomy, strong prediction chain, and controlled reduction formalized; physical proofs remain in their own modules |
| [[27_numeric_experimental_program/index\|27 — Numerical program]] | reproducibility and benchmarks | self-contained scripts and formal note | [NumericalProtocol](../formal/GDQ/NumericalProtocol.lean) | manifesto, numerical classes, blind prediction, strong comparison and error decomposition formalized; the protocol does not certify particular backgrounds |
| [[28_technical_faq/index\|28 — Technical FAQ]] | objections, domains and limits | body, notes and proof map | [TechnicalFAQ](../formal/GDQ/TechnicalFAQ.lean) | conditionals, non-factorization of state, Born versus event, sectorial Perelman and insufficiency of numerical agreement formalized |

## 4. Formal core of quantization

The active formal chain is:

$$
f
\longrightarrow
\rho(f),\,e^{i\operatorname{Im}f}
\longrightarrow
\text{circular phase}
\longrightarrow
\Delta S_R\in h\mathbb Z.
$$

For relative boundary problems:

$$
\widehat J_S
\longrightarrow
Q_S
\longrightarrow
\Delta I_{\rm red}=Q_S\Delta S_R
\longrightarrow
Q_S\Delta S_R\in h\mathbb Z.
$$

The human proofs are in:

- [[08_hilbert_quantization_uncertainty/notes/wallstrom_fibrado_linha_u1|U(1) line bundle and Wallstrom]];
- [[08_hilbert_quantization_uncertainty/notes/quantizacao_relativa_acao_exponenciada|Relative quantization and exponentiated action]];
- [[10_spin_statistics_pauli/notes/provas_lemas_definicoes|Spin, Hopf, and half-monodromy]].

## 5. Rule for new migrations

An experimental proof will only be promoted when:

1. the statement coincides with the current state of the manuscript;
2. all hypotheses are typed or declared;
3. there is no `sorry`, `admit` or hidden physical axiom;
4. the module compiles in the canonical package;
5. the written proof remains self-contained;
6. the chapter points to the human note and the canonical code;
7. `memory.md` records the status and boundaries.

[[index|← Manuscript Summary]]
