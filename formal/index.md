---
title: "Índice canônico das provas Lean"
---

# Índice canônico das provas Lean

## 1. Como usar este índice

Este documento cataloga apenas módulos pertencentes à biblioteca canônica
`formal/GDQ/` e importados, direta ou indiretamente, pelo ponto de entrada
[GDQ.lean](GDQ.lean).

Para cada módulo, o índice informa:

1. o resultado formalizado;
2. as declarações Lean principais;
3. o capítulo do manuscrito que interpreta o resultado;
4. o limite lógico da certificação.

O código verifica a dedução dentro das hipóteses tipadas. Ele não substitui a
prova humana, a escolha do domínio físico nem a demonstração de que um
background concreto satisfaz as hipóteses.

## 2. Espaços, campos e relações constitutivas

| Módulo | Declarações principais | Resultado | Manuscrito |
|---|---|---|---|
| [Spaces.lean](GDQ/Spaces.lean) | `GeometrySector`, `LocalBulk`, `CosmologicalSpace`, `local_sector_ne_cosmological` | distingue tipadamente o bulk local do espaço cosmológico e certifica suas dimensões | [Cap. 2](../manuscrito/02_geometrization/index.md) |
| [LocalMeasure.lean](GDQ/LocalMeasure.lean) | `torusHaarMeasure`, `localBulkReferenceMeasure` | constrói a medida produto local com Haar no toro | [Cap. 2](../manuscrito/02_geometrization/index.md) |
| [Constitutive.lean](GDQ/Constitutive.lean) | `densityFromPotential`, `densityFromPotential_pos`, `phaseFromPotential` | formaliza $\rho=e^{-\operatorname{Re}f}$, sua positividade e a fase constitutiva | [Cap. 2](../manuscrito/02_geometrization/index.md) |
| [BohmIdentity.lean](GDQ/BohmIdentity.lean) | `densityAmplitude_hasDerivAt`, `densityAmplitude_firstDerivative_hasDerivAt`, `densityAmplitude_second_ratio`, `fisherVariation_eq_bohmExpression` | prova no setor regular unidimensional que $R=e^{q/2}$ satisfaz $R''/R=q''/2+(q')^2/4$ e identifica a forma de Fisher--Bohm | [Caps. 1 e 5](../manuscrito/05_equations_conservation/index.md) |
| [Fields.lean](GDQ/Fields.lean) | `HermitianMetricData`, `ComplexStructureData`, `TorsionData`, `GDQFieldConfiguration` | tipa os campos fundamentais e o locus regular | [Cap. 2](../manuscrito/02_geometrization/index.md) |
| [FlowKernel.lean](GDQ/FlowKernel.lean) | `officialFlowKernel`, `euclideanFlowKernel`, `euclideanFlowKernel_pos` | constrói o kernel oficial e prova positividade na seção euclidiana | [Caps. 2 e 4](../manuscrito/04_action_consistency/index.md) |
| [Admissibility.lean](GDQ/Admissibility.lean) | `BismutWitness`, `AdmissibleConfiguration`, `MaterialAdmissibleConfiguration` | separa configuração bruta, admissível e material com torção não nula | [Caps. 2 e 4](../manuscrito/04_action_consistency/index.md) |

## 3. Ação oficial, geometria e integrabilidade

| Módulo | Declarações principais | Resultado | Manuscrito |
|---|---|---|---|
| [ActionDensity.lean](GDQ/ActionDensity.lean) | `officialBracket`, `officialPointDensity`, `officialPointDensity_unfold` | registra literalmente a densidade pontual da ação oficial | [Cap. 4](../manuscrito/04_action_consistency/index.md) |
| [ActionIntegration.lean](GDQ/ActionIntegration.lean) | `PulledBackActionCandidate`, `PulledBackActionCandidate.value` | define a integral iterada depois do pullback | [Cap. 4](../manuscrito/04_action_consistency/index.md) |
| [OfficialAction.lean](GDQ/OfficialAction.lean) | `OfficialActionData`, `IsStationary`, `stationary_implies_zero_variation` | tipa a ação oficial e a estacionariedade | [Cap. 4](../manuscrito/04_action_consistency/index.md) |
| [GeometricInvariants.lean](GDQ/GeometricInvariants.lean) | `EuclideanGeometricInvariants`, `euclideanOfficialDensity` | agrupa os invariantes que entram na densidade oficial | [Cap. 4](../manuscrito/04_action_consistency/index.md) |
| [CoordinateGeometry.lean](GDQ/CoordinateGeometry.lean) | `CoordinateBismutBackground.riemann`, `.ricci`, `.scalarCurvature`, `.gradientNormSq` | constrói curvaturas e invariantes a partir dos dados coordenados | [Cap. 4](../manuscrito/04_action_consistency/index.md) |
| [ControlledIntegrability.lean](GDQ/ControlledIntegrability.lean) | `IntegrableDomination`, `ControlledEuclideanOfficialActionData` | transforma majorantes integráveis em certificados da ação | [Cap. 4](../manuscrito/04_action_consistency/index.md) |
| [EuclideanOfficialAction.lean](GDQ/EuclideanOfficialAction.lean) | `PositiveRealSection`, `EuclideanOfficialActionData` | constrói a ação na seção real positiva sob integrabilidade | [Cap. 4](../manuscrito/04_action_consistency/index.md) |

## 4. Contorno causal e relógio

| Módulo | Declarações principais | Resultado | Manuscrito |
|---|---|---|---|
| [CausalContour.lean](GDQ/CausalContour.lean) | `CausalContour`, `CausalContour.dlog`, `CausalContour.dlog_ne_zero` | tipa o contorno causal e seu pullback logarítmico regular | [Cap. 3](../manuscrito/03_complex_causality/index.md) |
| [ClockHomomorphism.lean](GDQ/ClockHomomorphism.lean) | `PositiveClockHomomorphism`, `PositiveClockHomomorphism.eq_exp`, `exponentialFlowScale_add` | prova que um relógio positivo, contínuo e homogêneo é exponencial | [Caps. 3 e 6](../manuscrito/03_complex_causality/index.md) |
| [ComplexContourAction.lean](GDQ/ComplexContourAction.lean) | `complexContourOfficialDensity`, `ControlledComplexContourActionData` | transporta a densidade oficial para o contorno complexo com controle de integrabilidade | [Caps. 3 e 4](../manuscrito/03_complex_causality/index.md) |

## 5. Variação, Hessiana física e ponte espectral

| Módulo | Declarações principais | Resultado | Manuscrito |
|---|---|---|---|
| [VariationalHessian.lean](GDQ/VariationalHessian.lean) | `OfficialActionVariationFamily`, `PhysicalHessianData`, `PhysicalHessianData.HasPhysicalGap` | define variação, Hessiana comprimida, projetor físico e gap | [Caps. 4 e 5](../manuscrito/05_equations_conservation/index.md) |
| [PhysicalProjector.lean](GDQ/PhysicalProjector.lean) | `finiteDimensionalConstrainedPhysicalSector`, `OrthogonalPhysicalSector.projector_kills_gauge`, `PhysicalHessianData.physicalHessian_selfAdjoint`, `.hasPhysicalGap_of_rawCoercive` | constrói $V_{\rm phys}=\ker D\mathcal C\cap\mathcal G^\perp$, obtém seu projetor ortogonal, comprime a Hessiana e transfere coercividade para gap | [Caps. 4 e 6](../manuscrito/06_global_local_bridge/06.4%20-%20Hessiana,%20v%C3%ADnculos%20e%20projetor%20f%C3%ADsico.md) |
| [VariationalDynamics.lean](GDQ/VariationalDynamics.lean) | `unconstrainedStationary_iff_eulerLagrange_zero`, `physicallyStationary_iff_projectedGradient_zero`, `eulerLagrange_linearizes_to_hessian`, `restrictedLinearization_eq_physicalHessian`, `physicalHessian_eq_raw_of_invariant` | prova que a equação variacional é primária, a Hessiana é sua derivada na sela e o projetor apenas restringe a dinâmica linear ao setor físico | [Nota dos Caps. 4 e 6](../manuscrito/notes/action/Dinamica%20variacional,%20linearizacao%20e%20operadores%20derivados.md) |
| [PhaseFirstVariation.lean](GDQ/PhaseFirstVariation.lean) | `officialPointDensity_phase_split`, `officialPhaseSectorDensity_perturbation_exact`, `officialPhaseFirstVariation_eq_twice` | separa literalmente a parcela de fase da densidade oficial, expande-a sob $S_R\mapsto S_R+\varepsilon\eta$ e obtém sua primeira variação sem resto assintótico | [Cap. 5](../manuscrito/05_equations_conservation/index.md) |
| [NoetherPhaseCurrent.lean](GDQ/NoetherPhaseCurrent.lean) | `officialPhaseCurrent_eq_normalized`, `officialPhaseFirstVariation_eq_currentPairing`, `phaseWeakStationary_iff_currentWeaklyConserved` | extrai da variação a corrente oficial, prova a invariância por translação constante e identifica estacionariedade fraca com conservação fraca | [Cap. 5](../manuscrito/05_equations_conservation/index.md) |
| [NoetherIdentity.lean](GDQ/NoetherIdentity.lean) | `noether_off_shell_identity`, `noether_on_shell_conservation`, `noether_charge_constant` | certifica a identidade algébrica off-shell, sua redução conservativa on-shell e o balanço integrado sob contorno sem fluxo | [Cap. 5](../manuscrito/05_equations_conservation/index.md) |
| [StokesChargeBalance.lean](GDQ/StokesChargeBalance.lean) | `PhaseStokesData.oriented_charge_balance`, `.charge_conserved_of_zero_lateral_flux`, `relative_phase_quantized_from_stokes` | torna explícita a instanciação geométrica de Stokes e fecha a cadeia entre conservação, carga de bordo e quantização relativa | [Caps. 5 e 8](../manuscrito/05_equations_conservation/index.md) |
| [RouthMadelung.lean](GDQ/RouthMadelung.lean) | `routhExcess_nonneg`, `weightedPhaseEnergy_decomposition`, `normalizedPhaseEnergy_eq_one_add_excess`, `polarized_of_routhExcess_eq_zero` | certifica em discretização finita positiva a completação do quadrado de Routh e que excesso nulo normalizado equivale a $\Pi_{S_R}=\rho$ | [Caps. 5 e 6](../manuscrito/05_equations_conservation/index.md) |
| [CosmologicalFamily.lean](GDQ/CosmologicalFamily.lean) | `cosmologicalEquivSplit`, `ScaledCosmologicalGeometry`, `epsilonCosmologicalGeometry` | constrói a família cosmológica apontada e sua fatoração | [Caps. 6 e 20](../manuscrito/06_global_local_bridge/index.md) |
| [GlobalLocalTransport.lean](GDQ/GlobalLocalTransport.lean) | `PointedFieldTransport.rho_tendsto`, `.kernel_tendsto`, `WeightedMeasureTransport.distance_preserving` | transporta campos, densidade, kernel e norma entre os espaços | [Cap. 6](../manuscrito/06_global_local_bridge/index.md) |
| [SpectralBridge.lean](GDQ/SpectralBridge.lean) | `MoscoConvergenceData`, `UniformLocalizationGap`, `StrongResolventConvergence`, `RieszProjectorConvergence` | tipa os seis lemas espectrais da ponte | [Cap. 6](../manuscrito/06_global_local_bridge/index.md) |
| [GlobalLocalSixLemmas.lean](GDQ/GlobalLocalSixLemmas.lean) | `lemma1_pointed_limit`, `lemma2_fields_and_measure_transport`, `lemma3_physical_hessian_mosco`, `lemma4_uniform_gap_and_localization`, `lemma5_resolvents_and_riesz`, `lemma6_topology_vs_continuous_normalization`, `six_global_local_lemmas_explicit` | enuncia e compõe separadamente os seis lemas, preservando as hipóteses analíticas de cada background | [Cap. 6](../manuscrito/06_global_local_bridge/index.md) |
| [C3Application.lean](GDQ/C3Application.lean) | `relativeThreeCenterProjector_idempotent`, `c3PhysicalGap_pos`, `c3PhysicalGap_primitive` | constrói o projetor relativo e prova positividade do gap $C_3$ | [Caps. 6 e 14](../manuscrito/14_geometric_particle_taxonomy/index.md) |
| [C3ConcreteHessian.lean](GDQ/C3ConcreteHessian.lean) | `c3ClosureJacobian_gram_identity`, `c3ClosureJacobian_kills_common`, `c3AngularEnergy_on_relative` | liga o vínculo de três centros à Hessiana concreta | [Caps. 6 e 14](../manuscrito/14_geometric_particle_taxonomy/index.md) |
| [GenerationJunction.lean](GDQ/GenerationJunction.lean) | `isolated_horizontal_junction_has_three_centers`, `horizontal_junction_internal_zero_modes`, `c3EquilibriumTension_sum_zero`, `totalLocalAPSIndex_primitive`, `isolated_primitive_junction_generation_count` | aplica posto--nulidade ao vínculo horizontal, seleciona três centros sob isolamento e compõe índice local e multiplicidade quiral | [Cap. 14](../manuscrito/14_geometric_particle_taxonomy/index.md) |

## 6. Background gaussiano e redução clássica

| Módulo | Declarações principais | Resultado | Manuscrito |
|---|---|---|---|
| [GaussianOfficialReduction.lean](GDQ/GaussianOfficialReduction.lean) | `gaussianDensity_pos`, `gaussianGradientNormSq_eq`, `gaussianOfficialBracket` | avalia exatamente a densidade e o colchete no background gaussiano | [Cap. 7](../manuscrito/07_classical_limit/index.md) |
| [GaussianContourReduction.lean](GDQ/GaussianContourReduction.lean) | `iteratedOfficialPhaseVariation_eq_quadratic`, `realIteratedOfficialPhaseVariation_second` | prova a estrutura quadrática da variação de fase após as integrais | [Cap. 7](../manuscrito/07_classical_limit/index.md) |
| [GaussianBulkDomination.lean](GDQ/GaussianBulkDomination.lean) | `euclidean4GaussianEnvelope_integrable`, `localBulkGaussianEnvelope_integrable` | certifica a integrabilidade espacial por majorante gaussiana | [Caps. 4 e 7](../manuscrito/07_classical_limit/index.md) |
| [GaussianCausalDomination.lean](GDQ/GaussianCausalDomination.lean) | `causalGaussianEnvelope_integrable`, `constant_nonzero_not_integrable_on_real`, `finiteCausalWindow_integrable` | distingue decaimento causal, divergência constante e janela finita | [Caps. 3, 4 e 7](../manuscrito/07_classical_limit/index.md) |
| [GaussianOfficialIntegrability.lean](GDQ/GaussianOfficialIntegrability.lean) | `complexContourPointDensity_gaussian_integrable`, `gaussianOfficialBulkControl` | fecha o certificado de integrabilidade da densidade oficial gaussiana | [Caps. 4 e 7](../manuscrito/07_classical_limit/index.md) |
| [GaussianAdmissibleBackground.lean](GDQ/GaussianAdmissibleBackground.lean) | `gaussianFlatAdmissible`, `gaussianFlatAdmissible_not_material` | constrói o controle plano e prova que torção nula não representa matéria | [Caps. 7 e 15](../manuscrito/07_classical_limit/index.md) |

## 7. Background material de Bismut e sela torsional

| Módulo | Declarações principais | Resultado | Manuscrito |
|---|---|---|---|
| [ConformalBismutTorsion.lean](GDQ/ConformalBismutTorsion.lean) | `standardFundamentalForm_skew`, `conformalPotential`, `conformalScale` | constrói a forma Hermitiana conformal e sua torção | [Caps. 2 e 15](../manuscrito/15_leptonic_hierarchy_masses/index.md) |
| [ConformalBismutConnection.lean](GDQ/ConformalBismutConnection.lean) | `conformalRealMetric`, `conformalRealInverseMetric`, `conformalPhiGradient` | constrói a métrica e a conexão de Bismut coordenada | [Caps. 4 e 15](../manuscrito/15_leptonic_hierarchy_masses/index.md) |
| [ConformalBismutBackground.lean](GDQ/ConformalBismutBackground.lean) | `conformalCoordinateBismutBackground`, `conformalCoordinate_volumeDensity` | reúne o background material coordenado | [Cap. 15](../manuscrito/15_leptonic_hierarchy_masses/index.md) |
| [ConformalBismutInvariants.lean](GDQ/ConformalBismutInvariants.lean) | `conformalCoordinate_scalarCurvature`, `conformalCoordinate_gradientNormSq`, `conformalBismutInvariants` | calcula curvatura, gradiente e invariantes do background | [Cap. 15](../manuscrito/15_leptonic_hierarchy_masses/index.md) |
| [ConformalOfficialDensity.lean](GDQ/ConformalOfficialDensity.lean) | `conformalMaterialOfficialDensity_eq`, `conformalMaterial_geometricBracket_factor` | insere os invariantes na densidade literal da ação | [Caps. 4 e 15](../manuscrito/15_leptonic_hierarchy_masses/index.md) |
| [ConformalTorsionSaddle.lean](GDQ/ConformalTorsionSaddle.lean) | `exists_normalized_nonzero_torsion_root`, `normalizedTorsionSlope_strictMonoOn` | prova existência e unicidade da raiz torsional reduzida | [Cap. 15](../manuscrito/15_leptonic_hierarchy_masses/index.md) |
| [ConformalTorsionHessian.lean](GDQ/ConformalTorsionHessian.lean) | `normalizedTorsionHessianU_pos`, `coupledHessianQuadratic_schur`, `torsionCoupledMode_stable_of_schur` | prova estabilidade reduzida e enuncia o critério de Schur acoplado | [Caps. 15 e 19](../manuscrito/19_electroweak_geometric_breaking/index.md) |
| [ConformalTorsionProjectedHessian.lean](GDQ/ConformalTorsionProjectedHessian.lean) | `normalizedTorsionFirstVariationInA_hasDerivAt`, `normalizedTorsionHessianA_pos_at_saddle`, `torsionTwoModePhysicalProjector_eq_self`, `torsionReducedProjectedGap` | deriva $K_{aa}$ na amplitude geométrica, constrói o projetor do setor reduzido e prova uma cota explícita de gap sob dominância diagonal | [Cap. 15, §15.8](../manuscrito/15_leptonic_hierarchy_masses/15.8%20-%20Hessiana%208D%20e%20heran%C3%A7a%20por%20Schur.md) |
| [ConformalTorsionConstraintTangent.lean](GDQ/ConformalTorsionConstraintTangent.lean) | `normalizedTorsionReducedAction_not_stationary_in_fBase`, `normalizedTorsionReducedAction_fBase_secondDerivative_zero`, `normalizedTorsionReducedAction_mixed_fBase_u_zero`, `torsionNormalizedF0_hasDerivAt`, `existsUnique_normalizedTorsionTangent_f0` | prova que $f_{\rm base}$ não é modo físico livre e que o vínculo fixa univocamente $\delta f_0=128\tau a\,\delta a$ | [Cap. 15, §15.8](../manuscrito/15_leptonic_hierarchy_masses/15.8%20-%20Hessiana%208D%20e%20heran%C3%A7a%20por%20Schur.md) |
| [PerelmanProductReduction.lean](GDQ/PerelmanProductReduction.lean) | `factorized_fiber_flow_zero`, `factorized_totalScalar_eq_base`, `factorized_scalar_unbounded_iff_base`, `perelman_reduction_factorized` | prova o congelamento do fator Ricci-plano e a redução escalar ao fator curvo no bulk produto sem mistura | [Cap. 15](../manuscrito/15_leptonic_hierarchy_masses/index.md) |
| [KoideGeometry.lean](GDQ/KoideGeometry.lean) | `koide_saturation_iff_polynomial`, `koide_ratio_eq_two_thirds`, `koide_heavy_branch_satisfies` | prova a equivalência entre saturação geométrica e $Q=2/3$, além do ramo pesado explícito | [Cap. 15](../manuscrito/15_leptonic_hierarchy_masses/index.md) |
| [LeptonicHierarchy.lean](GDQ/LeptonicHierarchy.lean) | `reducedMuonRatio_decomposition`, `koideHeavyAmplitude_satisfies`, `no_four_independent_directions_in_three_space`, `schurCorrectedRatio_eq_reduced_of_product`, `scalarSchurEigenvalue_pos_of_subcritical` | certifica a composição reduzida do múon, os ramos de saturação, o limite dimensional e a herança/estabilidade escalar por Schur; os coeficientes reduzidos continuam hipóteses geométricas do setor declarado | [Cap. 15](../manuscrito/15_leptonic_hierarchy_masses/index.md) |
| [MagneticResponse.lean](GDQ/MagneticResponse.lean) | `magneticGFactor_minimal_eq_two`, `unitHarmonicCircleNormSq_eq`, `leadingMagneticAnomaly_eq`, `effectiveMagneticRatio_eq_minimal_plus_anomaly`, `leadingBlockResponse_eq`, `directOrthogonalChannel_vanishes` | certifica $g_0=2$ sob o mapa mínimo, a norma $1/(2\pi)$, o termo líder, a decomposição protegida/transversal e o bloco Hessiano reduzido; não calcula os canais superiores metrológicos | [Cap. 16](../manuscrito/16_fine_structure_zeeman_gminus2/index.md) |
| [BaryonicReduction.lean](GDQ/BaryonicReduction.lean) | `three_chambers_volume`, `neutron_torsional_balance`, `neutron_pairwise_shear_sq`, `reduced_neutron_minus_proton`, `quarticSchurElimination`, `reducedLifetime_inverse` | certifica a álgebra do modelo bariônico reduzido e explicita que a lei de vida média é apenas uma identidade depois de assumida | [Cap. 17](../manuscrito/17_baryonic_structure/index.md) |
| [ElectroweakStability.lean](GDQ/ElectroweakStability.lean) | `fixedVolumeAreaQuadraticCoeff_eq_zero`, `fixedVolumeAreaQuarticCoeff_eq`, `exists_positive_electroweakAmplitude`, `brokenMinimum_below_symmetricPoint`, `electromagneticInterfaceSchur_pos`, `neutralMassBlock_photonKernel`, `neutralMassBlock_massiveMode` | certifica o cancelamento quadrático e a quártica positiva da interface, os mínimos globais sob $a_2<0<a_4$, o Schur positivo e os modos neutros; não atribui os coeficientes do background | [Cap. 19](../manuscrito/19_electroweak_geometric_breaking/index.md) |
| [GravityCosmology.lean](GDQ/GravityCosmology.lean) | `newton_group_reconstruction`, `horizon_response_recovers_newton`, `axial_cost_eq_inverse_two_alpha_of_gluing`, `cartanChannelCount_eq`, `exact_linear_dilution_ratio`, `reducedCosmologicalMassDensity_cancel_c`, `vacuum_equationOfState_eq_minus_one`, `stiff_pressure_of_sixth_power_dilution`, `critical_acceleration_eq_cH_over_two_pi` | certifica a camada algébrica gravitacional e cosmológica, mantendo colagem, background global e Hessiana como hipóteses externas explícitas | [Cap. 20](../manuscrito/20_gravity_cosmology/index.md) |
| [HydrogenSpectrum.lean](GDQ/HydrogenSpectrum.lean) | `reducedMass_pos`, `sommerfeldDiracEnergy_negKappa`, `sommerfeld_two_channels_degenerate`, `fineStructure_n2_spinOrbitSplitting`, `hydrogenHyperfine_angularSplitting`, `zemachRelativeCorrection_neg`, `protonSurfaceSchur_pos` | certifica as consequências algébricas do operador atômico efetivo: massa reduzida, degenerescência, splitting fino, canais hiperfinos, Zemach e Schur; não deriva em Lean o espectro radial a partir da EDO nem os blocos metrológicos protônicos | [Cap. 22](../manuscrito/22_hydrogen_atom/index.md) |
| [SimpleApplications.lean](GDQ/SimpleApplications.lean) | `closed_circulation_recovers_infiniteWellEnergy`, `oscillator_gaussian_ground_energy`, `oscillatorLadder_spacing`, `casimirSpectralCoefficient_eq`, `casimirPressure_eq_three_energy_over_separation`, `casimirPressure_neg`, `rotor_energy_at_radial_minimum`, `centrifugalDistortion_eq_four_B_cubed` | certifica poço/circulação, oscilador, coeficientes de Casimir e eliminação radial do rotor; paredes e Hartman reutilizam os módulos de interface e transporte | [Cap. 23](../manuscrito/23_simple_applications/index.md) |
| [NuclearPhenomenology.lean](GDQ/NuclearPhenomenology.lean) | `alphaHalfLife_pos`, `alphaHalfLife_monotone_in_exponent`, `reduced_magic_number_126`, `comptonEnergyRatio_pos`, `kleinNishina_at_zero_eq_thomson`, `nuclearPairThreshold_gt_free`, `nuclearPairThreshold_recoil`, `paraPositroniumRate_pos`, `orthoPositroniumRate_pos`, `magneticPairParameter_nonneg`, `neutral_candidate_mass_splittings_pos`, `twoChannelOscillationFactor_bounds` | certifica o núcleo algébrico das reduções alfa, camadas, Compton, pares e neutrinos sem promover benchmarks, jatos 8D ou coeficientes candidatos a axiomas | [Cap. 24](../manuscrito/24_nuclear_phenomenology/index.md) |
| [AstrophysicsCosmology.lean](GDQ/AstrophysicsCosmology.lean) | `regularCoreLapse_eq_deSitter`, `isotropicThreeChannelRigidity`, `reducedSchurGap_pos`, `reducedHorizonTemperature_pos`, `shannonChannel_nonneg`, `electroweakReducedAmplitude_sq`, `protonSurfaceRadius_pos`, `contactProbeResponseRatio_lt_one`, `conjugateNeutralPhotonEnergy_symm`, `conjugateNeutralPhotonEnergy_pos`, `conjugateNeutralWavelength_pos`, `redshiftedWavelength_pos`, `emittedWavelength_le_redshifted` | certifica regularidade líder, rigidez, Schur, temperatura/entropia, normalizações globais e cinemática do pente neutro sem promover a sela 8D, o acoplamento radiativo, Page toy ou benchmarks a teoremas | [Cap. 25](../manuscrito/25_astrophysics_cosmology/index.md) |
| [LogicalStatus.lean](GDQ/LogicalStatus.lean) | `StrongPredictionReady`, `not_strongPredictionReady_of_missing_background`, `not_strongPredictionReady_of_postfit`, `ControlledReduction`, `not_controlledReduction_of_changed_action`, `attachProblemData_core` | tipa a taxonomia científica, separa axiomas de dados externos e certifica a cadeia mínima de fechamento | [Cap. 26](../manuscrito/26_logical_status/index.md) |
| [NumericalProtocol.lean](GDQ/NumericalProtocol.lean) | `ReproducibleManifest`, `BlindPredictionEligible`, `StrongComparisonEligible`, `not_blindPredictionEligible_of_target_used`, `numerical_physical_error_decomposition` | tipa classes numéricas e papéis dos dados, impede pós-ajuste de ser chamado de previsão cega e separa erro de discretização de discrepância física | [Cap. 27](../manuscrito/27_numeric_experimental_program/index.md) |
| [TechnicalFAQ.lean](GDQ/TechnicalFAQ.lean) | `ConditionalResult`, `numericalAgreement_does_not_close_missing_background`, `EntangledState`, `not_fullMeasurementDynamics_of_missing_event_dynamics`, `ProductSectorReductionAdmissible`, `not_productSectorReduction_of_mixed_torsion` | certifica as distinções lógicas da FAQ sem duplicar ou promover hipóteses físicas | [Cap. 28](../manuscrito/28_technical_faq/index.md) |

## 8. Fase, quantização e topologia

| Módulo | Declarações principais | Resultado | Manuscrito |
|---|---|---|---|
| [OSReconstruction.lean](GDQ/OSReconstruction.lean) | `ReflectionPositiveSector`, `reflectionPositive`, `nullSpace_sup_gauge`, `inner_physicalState`, `physicalState_eq_zero_of_gauge`, `physicalState_denseRange` | formaliza o núcleo OS: positividade declarada pelo pareamento refletido, quociente nulo, gauge nulo, imagem densa e completamento complexo | [Cap. 8](../manuscrito/08_hilbert_quantization_uncertainty/index.md) |
| [OSReconstructedEvolution.lean](GDQ/OSReconstructedEvolution.lean) | `PositiveEuclideanSemigroup`, `ReconstructedUnitaryGroup`, `euclideanSpectralWeight_le_one`, `lorentzianSpectralWeight_norm` | separa semigrupo euclidiano contrativo de grupo unitário e certifica os pesos espectrais modo a modo | [Nota do Cap. 8](../manuscrito/08_hilbert_quantization_uncertainty/notes/reconstrucao_os_quociente_hilbert.md) |
| [PhaseQuantization.lean](GDQ/PhaseQuantization.lean) | `closed_lift_increment_is_integer`, `liftedPhaseCirculation_quantized`, `circleLoop_has_quantized_lift` | prova a quantização de circulação de laços fechados em $U(1)$ | [Cap. 8](../manuscrito/08_hilbert_quantization_uncertainty/index.md) |
| [PhaseReconstruction.lean](GDQ/PhaseReconstruction.lean) | `norm_sq_reconstructedStateFromPotential`, `officialBracket_imaginaryShift`, `PotentialPhaseLoop.phaseIncrement_quantized` | reconstrói fase e estado de $f$ e quantiza laços admissíveis do potencial | [Cap. 8](../manuscrito/08_hilbert_quantization_uncertainty/index.md) |
| [BoundaryPhaseQuantization.lean](GDQ/BoundaryPhaseQuantization.lean) | `constantLift_has_zero_boundaryShift`, `boundaryCharge_conserved_of_zero_lateral_flux`, `BoundaryPhaseQuantizationData.product_quantized`, `.primitive_increment_quantized` | prova o no-go local e a quantização relativa $Q_S\Delta S_R\in h\mathbb Z$ | [Nota do Cap. 8](../manuscrito/08_hilbert_quantization_uncertainty/notes/quantizacao_relativa_acao_exponenciada.md) |
| [Uncertainty.lean](GDQ/Uncertainty.lean) | `cauchy_uncertainty`, `robertson_schrodinger_core`, `uncertainty_from_variance_vectors` | prova Cauchy para vetores de flutuação e sua decomposição real/imaginária de Robertson--Schrödinger no Hilbert reconstruído | [Cap. 8](../manuscrito/08_hilbert_quantization_uncertainty/index.md) |
| [FiniteBorn.lean](GDQ/FiniteBorn.lean) | `pureBornWeight_nonneg`, `pureBornWeight_le_one`, `pureBornWeights_sum_norm`, `pureBornWeights_sum_one` | prova positividade, limite unitário e normalização de Born para estados puros em base ortonormal finita | [Cap. 9](../manuscrito/09_measurement_born_interface/index.md) |
| [MixedBornTrace.lean](GDQ/MixedBornTrace.lean) | `mixedBornTraceWeight_nonneg`, `mixedBornTraceWeights_sum_one`, `mixedBornTraceWeight_le_one` | prova positividade e normalização da regra por traço para matriz densidade finita e resolução projetiva da identidade | [Cap. 9](../manuscrito/09_measurement_born_interface/index.md) |
| [MeasurementAsymptotic.lean](GDQ/MeasurementAsymptotic.lean) | `coherenceEnvelope_tendsto_zero`, `coherence_tendsto_zero_of_bound`, `ideal_record_repeatability` | prova supressão exponencial sob gap positivo e o núcleo algébrico da repetibilidade ideal | [Cap. 9](../manuscrito/09_measurement_born_interface/index.md) |
| [ClassicalApparatusResponse.lean](GDQ/ClassicalApparatusResponse.lean) | `LinearApparatusProblem.perturbation_solves`, `InterfaceBlockProblem.interior_stationary`, `.boundaryResidual_eq_schur`, `ReducedBoundaryResponse.boundaryField_solves` | formaliza a resposta à fonte clássica e prova que a eliminação do interior produz exatamente Schur/DtN | [Nota do Cap. 9](../manuscrito/09_measurement_born_interface/notes/fonte_hessiana_schur_readout_formal.md) |
| [ApparatusBornReadout.lean](GDQ/ApparatusBornReadout.lean) | `responseState_solves`, `recordWeight_nonneg`, `recordWeights_sum_one`, `recordWeight_le_one`, `BasinRealization.basinWeights_sum_one` | liga uma base espectral derivada da Hessiana à regra de Born finita, mantendo a realização dinâmica por bacias como hipótese explícita | [Nota do Cap. 9](../manuscrito/09_measurement_born_interface/notes/fonte_hessiana_schur_readout_formal.md) |
| [QNDBornBasins.lean](GDQ/QNDBornBasins.lean) | `qnd_schur_commutes`, `qnd_offDiagonal_eq_zero`, `posterior_sum_one`, `expected_posterior_eq_prior`, `AbsorbingReadout.basinWeight_eq_prior`, `qndCovarianceQuadratic_nonneg` | prova a cadeia finita QND gaussiana da Hessiana/Schur até a igualdade entre medida da bacia absorvente e peso inicial | [Nota do Cap. 9](../manuscrito/09_measurement_born_interface/notes/teorema_born_bacias_qnd_gaussiano.md) |
| [CechChern.lean](GDQ/CechChern.lean) | `U1TripleLift.exists_cechInteger`, `U1TripleLift.cechInteger_shift`, `two_pi_int_multiple_injective` | constrói o inteiro de Čech e sua transformação por cobordo | [Caps. 8 e 21](../manuscrito/08_hilbert_quantization_uncertainty/index.md) |
| [CechCohomology.lean](GDQ/CechCohomology.lean) | `cechD2_cechD1_zero`, `cechH2Class`, `U1CechLiftData.firstChernClass` | constrói cociclos, cobordos, $H^2$ e a primeira classe de Chern | [Caps. 8 e 21](../manuscrito/21_cp_hopf_monopoles/index.md) |
| [SpinHopfMonodromy.lean](GDQ/SpinHopfMonodromy.lean) | `normalizedHalfResidue_eq_half`, `halfSpinCirculation_eq_pi_hbar`, `phaseHolonomy_halfSpinCirculation`, `phaseHolonomy_double_halfSpinCirculation` | prova resíduo $1/2$, circulação $h/2$ e fechamento spinorial em duas voltas | [Cap. 10](../manuscrito/10_spin_statistics_pauli/index.md) |
| [CARPauli.lean](GDQ/CARPauli.lean) | `square_zero_of_self_anticomm`, `CreationCAR.pauli`, `antisymmetric_wavefunction_vanishes_on_diagonal` | prova que CAR implica $(a_i^\dagger)^2=0$ e que antissimetria implica anulação na diagonal | [Cap. 10](../manuscrito/10_spin_statistics_pauli/index.md) |
| [SpinStatisticsConditional.lean](GDQ/SpinStatisticsConditional.lean) | `SpinStatisticsConditions.Holds`, `SpinStatisticsBridge`, `spinStatisticsCAR`, `spin_statistics_conditional_pauli` | torna explícitas as oito hipóteses relativísticas, aplica a ponte spin--estatística e deriva Pauli; a ponte analítica completa permanece hipótese externa | [Cap. 10](../manuscrito/10_spin_statistics_pauli/index.md) |
| [SternGerlachProjectors.lean](GDQ/SternGerlachProjectors.lean) | `cliffordProjectorPlus_idempotent`, `cliffordProjectors_orthogonal`, `cliffordProjectors_complete`, `sternGerlachPlusWeight_eq_cos_sq_half`, `sternGerlachWeights_sum_one` | certifica o cálculo espectral dos dois canais e os pesos de meia-ângulo | [Cap. 11](../manuscrito/11_stern_gerlach_classical_quantum/index.md) |
| [SternGerlachSequential.lean](GDQ/SternGerlachSequential.lean) | `sternGerlach_orthogonal_plus`, `sternGerlach_orthogonal_minus`, `sternGerlach_z_x_z_return`, `sternGerlach_z_x_z_complement` | certifica que a sequência ortogonal $z\to x\to z$ produz pesos finais $1/2,1/2$ | [Cap. 11](../manuscrito/11_stern_gerlach_classical_quantum/index.md) |
| [SternGerlachInterface.lean](GDQ/SternGerlachInterface.lean) | `sternGerlach_freeBoundary_of_radius_constraint`, `sternGerlach_boundaryResidual_eq_schurDtN`, `responseCoefficient_solves`, `sternGerlachTextureRigidity_pos`, `noetherZeemanEffectiveRatio_decomposition`, `sternGerlachChannelDeflection_eq` | certifica a condição livre, a especialização Schur/DtN, a resposta modal, a rigidez axial positiva, a decomposição Noether--Zeeman e a deflexão clássica | [Nota do Cap. 11](../manuscrito/11_stern_gerlach_classical_quantum/notes/background_hessiana_e_dtn_sg.md) |
| [DetectorDtNSchur.lean](GDQ/DetectorDtNSchur.lean) | `detectorProfile_outwardDerivative_at_zero`, `detectorDtN_pos`, `detectorDecoherence_nonneg`, `detectorVisibility_mem` | deriva $\lambda\coth(\lambda L)$ do perfil hiperbólico e prova positividade da impedância, do expoente de Schur e o intervalo da visibilidade | [Cap. 12](../manuscrito/12_tunneling_interference_transport/index.md) |
| [TransportInterference.lean](GDQ/TransportInterference.lean) | `evanescentDensityRatio_mem`, `reducedHartmanDistance_tendsto`, `coherentTwoPathDensity`, `twoPathIntensity_lower_bound`, `twoPathIntensity_upper_bound`, `FiniteCausalReadoutKernel.record_eq_of_past_eq` | prova atenuação evanescente, saturação geométrica de Hartman, identidade e limites da interferência e independência causal de mudanças futuras | [Cap. 12](../manuscrito/12_tunneling_interference_transport/index.md) |
| [AharonovBohmHolonomy.lean](GDQ/AharonovBohmHolonomy.lean) | `gaugeShiftedCirculation_closed`, `aharonovBohmHolonomy_gauge_invariant`, `aharonovBohm_circulation_eq_flux` | prova invariância de calibre da holonomia em laço fechado e a equivalência circulação--fluxo sob a hipótese geométrica de Stokes | [Cap. 13](../manuscrito/13_holonomies_ab_sagnac/index.md) |
| [SagnacHolonomy.lean](GDQ/SagnacHolonomy.lean) | `sagnac_phase_difference`, `sagnac_common_phase_cancels`, `sagnac_rotation_reversal` | prova duplicação do termo ímpar, cancelamento da fase comum e reversão de sinal na holonomia de Sagnac | [Cap. 13](../manuscrito/13_holonomies_ab_sagnac/index.md) |
| [HolonomyPatchingStokes.lean](GDQ/HolonomyPatchingStokes.lean) | `discrete_stokes`, `harmonicRepresentative_circulation`, `u1Holonomy_add_integer_period`, `TwoPatchU1Gluing.holonomy_shift`, `sagnacTimeDelay_of_rotationCirculation` | prova Stokes celular finito, circulação do representante harmônico, invariância da colagem por enrolamentos inteiros e o fator $4\Omega\cdot A/c^2$ sob a circulação cinemática declarada | [Cap. 13](../manuscrito/13_holonomies_ab_sagnac/index.md) |
| [HyperchargeDiophantine.lean](GDQ/HyperchargeDiophantine.lean) | `standardHypercharges_anomaly`, `standardHypercharges_z6`, `hypercharge_unique_oriented_minimal`, `standardHypercharges_physical` | verifica anomalias e congruências e prova a unicidade orientada mínima $(1,-4,2,-3,6)$, fixada a troca dos singletos | [Cap. 14](../manuscrito/14_geometric_particle_taxonomy/index.md) |
| [KillingPoissonLie.lean](GDQ/KillingPoissonLie.lean) | `killingPotential_preserves_bracket`, `killingPotential_reflects_bracket` | formaliza os potenciais locais como homomorfismo de Lie e reflete relações quando o mapa é injetivo | [Cap. 14](../manuscrito/14_geometric_particle_taxonomy/index.md) |
| [APSHopfBismut.lean](GDQ/APSHopfBismut.lean) | `primitive_hopf_chern`, `primitive_torsional_kernel_dim`, `aps_index_invariant_of_no_crossing`, `primitive_bismut_aps_index_one` | certifica os invariantes discretos primitivos e a passagem $\Delta\mathrm{ind}=-\mathrm{SF}$ sob dados APS explícitos | [Cap. 14](../manuscrito/14_geometric_particle_taxonomy/index.md) |
| [YMSectorIsomorphism.lean](GDQ/YMSectorIsomorphism.lean) | `sectorStarIsomorphism_bijective`, `transportedYMState_normalized`, `transportedYMState_positive`, `sectorStarIsomorphism_map_three` | prova bijetividade e transporte de produto, involução, normalização e positividade entre álgebras reduzidas | [Cap. 18](../manuscrito/18_confinement_signal_problem/index.md) |
| [AreaLawConditional.lean](GDQ/AreaLawConditional.lean) | `tubular_free_energy_exact`, `tubular_free_energy_per_area`, `tubular_area_law_limit` | prova a lei de área quando perímetro e resto são subextensivos na thimble tubular admitida | [Cap. 18](../manuscrito/18_confinement_signal_problem/index.md) |
| [CPRelaxation.lean](GDQ/CPRelaxation.lean) | `cpPotential_hasDerivAt`, `cp_lyapunov_identity`, `cp_lyapunov_nonpos`, `cp_zero_critical_minimum`, `cp_pi_critical_unstable` | prova o núcleo de Lyapunov, o mínimo em $\theta=0$ e a instabilidade em $\theta=\pi$ no modo reduzido | [Cap. 21](../manuscrito/21_cp_hopf_monopoles/index.md) |

## 9. Resultados cuja prova Lean ainda não é integral

Os seguintes blocos possuem prova escrita, cálculo simbólico ou validação
numérica no manuscrito, mas ainda não uma tradução Lean completa:

1. verificação OS em backgrounds funcionais concretos e construção do
   gerador autoadjunto; o quociente nulo, o completamento e os pesos
   espectrais já estão formalizados;
2. limite estocástico contínuo e aparelhos fora da classe QND gaussiana; a
   cadeia finita de históricos, conservação da esperança e absorção já
   possuem certificação;
3. Hessianas físicas completas de Stern--Gerlach e sondas; no background
   torsional conformal, apenas $K_{aa}$ e o teorema condicional de gap
   reduzido estão formalizados, não os blocos 8D mistos;
4. operadores espectrais metrológicos das massas;
5. Yang--Mills efetivo, confinamento e Wilson em domínio concreto; o
   isomorfismo abstrato de álgebras reduzidas e o limite condicional de área
   já estão formalizados;
6. avaliação covariante completa dos coeficientes eletrofracos em backgrounds
   gerais; a estabilidade algébrica reduzida, o Schur e o kernel neutro já
   estão formalizados;
7. derivação funcional integral do espectro radial e avaliação dos blocos
   protônicos superiores; as consequências algébricas do espectro, da
   estrutura fina e da hiperfina já estão formalizadas;
8. Hessiana cosmológica completa e fenomenologia CMB/BAO/SNe; as identidades
   reduzidas de horizonte, colagem condicional, diluição, equações de estado e
   aceleração crítica já estão formalizadas;
9. Hessianas nucleares completas, vértice Compton 8D, espectro neutro
   metrológico, sela astrofísica 8D e Page curve física; nos Capítulos 24 e
   25, as identidades algébricas reduzidas, regularidade líder, Schur,
   temperatura, entropia de canais e normalizações já estão formalizados.

Esses itens não devem ser descritos como teoremas Lean apenas porque suas
camadas algébricas compartilham estruturas já formalizadas.

## 10. Auditoria da biblioteca

O pacote canônico é construído por:

```bash
lake build GDQ
```

O módulo mais recente foi validado juntamente com o pacote:

```text
lake build GDQ
Build completed successfully (8748 jobs nesta validação).
```

A consulta `#print axioms` aos teoremas centrais, incluindo a separação
oficial do setor de fase, a corrente, a forma fraca, Stokes e a quantização
relativa, retornou somente:

```text
propext
Classical.choice
Quot.sound
```

Esses são princípios fundacionais da Mathlib, não axiomas físicos adicionais.
O mesmo resultado foi obtido para a segunda derivada torsional, o projetor
reduzido, a cota de gap por dominância diagonal e o tangente do vínculo de
normalização.

## 11. Navegação

- [README técnico](README.md)
- [Ponto de entrada Lean](GDQ.lean)
- [Mapa por capítulos do manuscrito](../manuscrito/formalizacao.md)
- [Capítulo 26 — estado lógico](../manuscrito/26_logical_status/index.md)
