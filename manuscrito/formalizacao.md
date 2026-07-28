---
title: "Mapa estrutural das provas e formalizações"
---

# Mapa estrutural das provas e formalizações

## 1. Função deste documento

Este arquivo liga três camadas diferentes:

$$
\text{capítulo didático}
\longrightarrow
\text{prova matemática escrita}
\longrightarrow
\text{verificação Lean}.
$$

A prova escrita permanece no manuscrito. O código Lean é uma certificação
complementar: ele verifica os enunciados formalizados, mas não substitui as
hipóteses geométricas, os domínios e o significado físico explicados no
texto.

Os módulos canônicos estão em `formal/GDQ/`. Arquivos experimentais em
pastas de questões não constituem prova citável pelo manuscrito.

O catálogo técnico módulo por módulo, com os nomes exatos dos teoremas, está
em [Índice canônico das provas Lean](../formal/index.md).

## 2. Legenda de status

- **formalizado:** o enunciado indicado compila no pacote canônico;
- **parcialmente formalizado:** somente a camada algébrica ou reduzida foi
  certificada;
- **prova escrita:** há demonstração matemática no manuscrito, ainda sem
  tradução integral para Lean;
- **não iniciado:** não há módulo Lean canônico correspondente.

## 3. Mapa por capítulo

| Capítulo | Núcleo matemático | Prova escrita | Módulos Lean canônicos | Status |
|---|---|---|---|---|
| [[01_initial_problem/index\|01 — Problema inicial]] | divergência Feynman--Wiener e identidade de Bohm | notas do capítulo | [BohmIdentity](../formal/GDQ/BohmIdentity.lean) | identidade diferencial local formalizada; contraste de integrais permanece explicação analítica |
| [[02_geometrization/index\|02 — Geometrização]] | espaços, campos, medida e relações constitutivas | notas do capítulo | [Spaces](../formal/GDQ/Spaces.lean), [LocalMeasure](../formal/GDQ/LocalMeasure.lean), [Constitutive](../formal/GDQ/Constitutive.lean), [Fields](../formal/GDQ/Fields.lean), [FlowKernel](../formal/GDQ/FlowKernel.lean), [Admissibility](../formal/GDQ/Admissibility.lean) | formalizado no núcleo estrutural |
| [[03_complex_causality/index\|03 — Causalidade complexa]] | contorno causal e relógio exponencial | notas do capítulo | [CausalContour](../formal/GDQ/CausalContour.lean), [ClockHomomorphism](../formal/GDQ/ClockHomomorphism.lean), [ComplexContourAction](../formal/GDQ/ComplexContourAction.lean) | formalizado condicionalmente ao contorno |
| [[04_action_consistency/index\|04 — Ação e consistência]] | densidade, integral oficial, integrabilidade e Hessiana | notas do capítulo | [ActionDensity](../formal/GDQ/ActionDensity.lean), [ActionIntegration](../formal/GDQ/ActionIntegration.lean), [OfficialAction](../formal/GDQ/OfficialAction.lean), [EuclideanOfficialAction](../formal/GDQ/EuclideanOfficialAction.lean), [ControlledIntegrability](../formal/GDQ/ControlledIntegrability.lean), [VariationalHessian](../formal/GDQ/VariationalHessian.lean), [PhysicalProjector](../formal/GDQ/PhysicalProjector.lean), [VariationalDynamics](../formal/GDQ/VariationalDynamics.lean) | formalizado no domínio declarado; a equação variacional é primária e Hessiana/projetor são derivados |
| [[05_equations_conservation/index\|05 — Equações e conservação]] | primeira variação, corrente, carga de fase e mínimo de Routh | notas de variação e Noether | [BohmIdentity](../formal/GDQ/BohmIdentity.lean), [PhaseFirstVariation](../formal/GDQ/PhaseFirstVariation.lean), [NoetherPhaseCurrent](../formal/GDQ/NoetherPhaseCurrent.lean), [NoetherIdentity](../formal/GDQ/NoetherIdentity.lean), [StokesChargeBalance](../formal/GDQ/StokesChargeBalance.lean), [BoundaryPhaseQuantization](../formal/GDQ/BoundaryPhaseQuantization.lean), [RouthMadelung](../formal/GDQ/RouthMadelung.lean) | variação pontual, identidade off-shell, conservação fraca e núcleo finito do mínimo de Routh formalizados; limite funcional e atração dissipativa permanecem condicionais |
| [[06_global_local_bridge/index\|06 — Ponte global--local]] | seis lemas, transporte espectral, projetores e gap $C_3$ | notas do capítulo | [PhysicalProjector](../formal/GDQ/PhysicalProjector.lean), [VariationalDynamics](../formal/GDQ/VariationalDynamics.lean), [CosmologicalFamily](../formal/GDQ/CosmologicalFamily.lean), [GlobalLocalTransport](../formal/GDQ/GlobalLocalTransport.lean), [SpectralBridge](../formal/GDQ/SpectralBridge.lean), [GlobalLocalSixLemmas](../formal/GDQ/GlobalLocalSixLemmas.lean), [C3Application](../formal/GDQ/C3Application.lean), [C3ConcreteHessian](../formal/GDQ/C3ConcreteHessian.lean) | os seis lemas possuem enunciados Lean explícitos e composição canônica; hipóteses Mosco/Agmon/Riesz continuam condicionadas ao background, como na prova humana |
| [[07_classical_limit/index\|07 — Limite clássico]] | redução gaussiana e correspondência local | notas do capítulo | [GaussianOfficialReduction](../formal/GDQ/GaussianOfficialReduction.lean), [GaussianContourReduction](../formal/GDQ/GaussianContourReduction.lean), [GaussianBulkDomination](../formal/GDQ/GaussianBulkDomination.lean), [GaussianCausalDomination](../formal/GDQ/GaussianCausalDomination.lean), [GaussianAdmissibleBackground](../formal/GDQ/GaussianAdmissibleBackground.lean) | formalizado no background gaussiano declarado |
| [[08_hilbert_quantization_uncertainty/index\|08 — Hilbert e quantização]] | reconstrução OS, fase circular, classe de Chern, quantização relativa e incerteza | notas do capítulo | [OSReconstruction](../formal/GDQ/OSReconstruction.lean), [OSReconstructedEvolution](../formal/GDQ/OSReconstructedEvolution.lean), [PhaseQuantization](../formal/GDQ/PhaseQuantization.lean), [PhaseReconstruction](../formal/GDQ/PhaseReconstruction.lean), [BoundaryPhaseQuantization](../formal/GDQ/BoundaryPhaseQuantization.lean), [CechChern](../formal/GDQ/CechChern.lean), [CechCohomology](../formal/GDQ/CechCohomology.lean), [Uncertainty](../formal/GDQ/Uncertainty.lean) | quociente nulo e completamento formalizados sob pareamento OS; positividade e gerador de cada background permanecem condicionais |
| [[09_measurement_born_interface/index\|09 — Medida e Born]] | interface clássico--quântica, fonte, Schur, bacias e registros | notas do capítulo | [FiniteBorn](../formal/GDQ/FiniteBorn.lean), [MixedBornTrace](../formal/GDQ/MixedBornTrace.lean), [MeasurementAsymptotic](../formal/GDQ/MeasurementAsymptotic.lean), [ClassicalApparatusResponse](../formal/GDQ/ClassicalApparatusResponse.lean), [ApparatusBornReadout](../formal/GDQ/ApparatusBornReadout.lean), [QNDBornBasins](../formal/GDQ/QNDBornBasins.lean) | resposta linear, Schur, Born espectral e versão finita Born--bacias formalizados no setor QND gaussiano; captura contínua usa o teorema analítico de separação |
| [[10_spin_statistics_pauli/index\|10 — Spin e estatística]] | meia-monodromia, Hopf, CAR e Pauli | notas do capítulo | [SpinHopfMonodromy](../formal/GDQ/SpinHopfMonodromy.lean), [CARPauli](../formal/GDQ/CARPauli.lean), [SpinStatisticsConditional](../formal/GDQ/SpinStatisticsConditional.lean) | meia-monodromia e CAR $\Rightarrow$ Pauli formalizadas; hipóteses e aplicação da ponte spin--estatística estão tipadas, mas o teorema analítico relativístico permanece externo |
| [[11_stern_gerlach_classical_quantum/index\|11 — Stern--Gerlach]] | projetores de dois canais, pesos angulares, Hessiana de interface e resposta do aparelho | notas e scripts do capítulo | [SternGerlachProjectors](../formal/GDQ/SternGerlachProjectors.lean), [SternGerlachSequential](../formal/GDQ/SternGerlachSequential.lean), [SternGerlachInterface](../formal/GDQ/SternGerlachInterface.lean) | projetores, pesos, sequências, condição livre do bordo, Schur/DtN, resposta modal, rigidez e Noether--Zeeman formalizados no setor reduzido; magneto real permanece metrologia |
| [[12_tunneling_interference_transport/index\|12 — Transporte e interferência]] | kernels, contornos e propagação | notas e scripts do capítulo | [DetectorDtNSchur](../formal/GDQ/DetectorDtNSchur.lean), [TransportInterference](../formal/GDQ/TransportInterference.lean) | DtN/Schur, atenuação, saturação de Hartman, identidade da dupla fenda e independência de dados futuros fora do suporte causal formalizados no setor reduzido |
| [[13_holonomies_ab_sagnac/index\|13 — Holonomias]] | Aharonov--Bohm e Sagnac | notas e scripts do capítulo | [AharonovBohmHolonomy](../formal/GDQ/AharonovBohmHolonomy.lean), [SagnacHolonomy](../formal/GDQ/SagnacHolonomy.lean), [HolonomyPatchingStokes](../formal/GDQ/HolonomyPatchingStokes.lean) | invariância de calibre, colagem por levantamentos, Stokes celular e fator ideal de Sagnac formalizados; a aplicação suave a cada domínio e a resposta de aparelhos reais permanecem dados geométricos/metrológicos |
| [[14_geometric_particle_taxonomy/index\|14 — Taxonomia e gerações]] | três centros, hipercargas, geradores e índice local | notas do capítulo | [C3Application](../formal/GDQ/C3Application.lean), [C3ConcreteHessian](../formal/GDQ/C3ConcreteHessian.lean), [GenerationJunction](../formal/GDQ/GenerationJunction.lean), [HyperchargeDiophantine](../formal/GDQ/HyperchargeDiophantine.lean), [KillingPoissonLie](../formal/GDQ/KillingPoissonLie.lean), [APSHopfBismut](../formal/GDQ/APSHopfBismut.lean) | setor $C_3$, seleção $N=3$ sob posto dois e isolamento, hipercargas, representação local de Lie e núcleo discreto APS formalizados; existência global dos potenciais e caminho espectral continuam hipóteses geométricas |
| [[15_leptonic_hierarchy_masses/index\|15 — Hierarquia leptônica]] | background torsional e operador espectral | notas e scripts do capítulo | [ConformalBismutTorsion](../formal/GDQ/ConformalBismutTorsion.lean), [ConformalBismutConnection](../formal/GDQ/ConformalBismutConnection.lean), [ConformalBismutBackground](../formal/GDQ/ConformalBismutBackground.lean), [ConformalTorsionSaddle](../formal/GDQ/ConformalTorsionSaddle.lean), [ConformalTorsionHessian](../formal/GDQ/ConformalTorsionHessian.lean), [ConformalTorsionProjectedHessian](../formal/GDQ/ConformalTorsionProjectedHessian.lean), [ConformalTorsionConstraintTangent](../formal/GDQ/ConformalTorsionConstraintTangent.lean), [PerelmanProductReduction](../formal/GDQ/PerelmanProductReduction.lean), [KoideGeometry](../formal/GDQ/KoideGeometry.lean), [LeptonicHierarchy](../formal/GDQ/LeptonicHierarchy.lean) | $K_{aa}$, tangente normalizado, redução produto 3D/8D, saturação e álgebra da hierarquia reduzida formalizados; a derivação universal dos coeficientes, a seleção dinâmica do ramo do tau e backgrounds mistos permanecem condicionais |
| [[16_fine_structure_zeeman_gminus2/index\|16 — Estrutura fina e Zeeman]] | resposta magnética e Hessiana de sonda | notas e scripts do capítulo | [SternGerlachInterface](../formal/GDQ/SternGerlachInterface.lean), [MagneticResponse](../formal/GDQ/MagneticResponse.lean) | $g_0=2$ sob o mapa mínimo, norma harmônica, termo líder, decomposição Hessiana e anulação de canal ortogonal formalizados; $\alpha$ cosmológica e $g-2$ superior permanecem condicionais |
| [[17_baryonic_structure/index\|17 — Estrutura bariônica]] | vínculos torsionais, massas, Schur e beta | notas e scripts do capítulo | [BaryonicReduction](../formal/GDQ/BaryonicReduction.lean) | identidades algébricas do modelo reduzido formalizadas; seleção da sela 8D, coeficientes de superfície e lei $\alpha^{-11}$ permanecem condicionais |
| [[18_confinement_signal_problem/index\|18 — Confinamento e sinal]] | conexão efetiva, Wilson e benchmark | notas e scripts do capítulo | [YMSectorIsomorphism](../formal/GDQ/YMSectorIsomorphism.lean), [AreaLawConditional](../formal/GDQ/AreaLawConditional.lean) | isomorfismo abstrato das álgebras reduzidas e limite condicional de área formalizados; thimble, sela e gap concretos permanecem hipóteses do background |
| [[19_electroweak_geometric_breaking/index\|19 — Quebra eletrofraca]] | Hessiana, Schur e rigidez do modo | notas e scripts do capítulo | [ElectroweakStability](../formal/GDQ/ElectroweakStability.lean) | cancelamento a volume fixo, quártica positiva, mínimos reduzidos, Schur e kernel neutro formalizados; os coeficientes do background permanecem entradas calculadas |
| [[20_gravity_cosmology/index\|20 — Gravitação e cosmologia]] | redução global, contorno, diluição e equações de estado | notas e scripts do capítulo | [CosmologicalFamily](../formal/GDQ/CosmologicalFamily.lean), [GravityCosmology](../formal/GDQ/GravityCosmology.lean) | grupo de Newton, horizonte, saddle/colagem condicional, 28 canais, diluição, densidade, $w$ e $a_0$ formalizados; background e Hessiana cosmológica completos permanecem condicionais |
| [[21_cp_hopf_monopoles/index\|21 — CP, monopolos e Hopf]] | classes topológicas e relaxação | notas e scripts do capítulo | [CechChern](../formal/GDQ/CechChern.lean), [CechCohomology](../formal/GDQ/CechCohomology.lean), [CPRelaxation](../formal/GDQ/CPRelaxation.lean) | topologia e núcleo de Lyapunov reduzido formalizados; convergência global exige invariância/compacidade do fluxo físico |
| [[22_hydrogen_atom/index\|22 — Hidrogênio]] | espectro, spin--órbita e hiperfina | notas e scripts do capítulo | [HydrogenSpectrum](../formal/GDQ/HydrogenSpectrum.lean) | massa reduzida, simetria espectral, degenerescência Coulombiana, splitting fino, álgebra hiperfina, sinal de Zemach e Schur formalizados; análise radial funcional e blocos protônicos superiores permanecem condicionais |
| [[23_simple_applications/index\|23 — Aplicações simples]] | poço, oscilador, parede, Hartman, Casimir e rotor | notas e scripts do capítulo | [DetectorDtNSchur](../formal/GDQ/DetectorDtNSchur.lean), [TransportInterference](../formal/GDQ/TransportInterference.lean), [SimpleApplications](../formal/GDQ/SimpleApplications.lean) | correspondência ideal, DtN/Schur, saturação, coeficientes de Casimir e eliminação radial formalizados; materiais e backgrounds moleculares reais permanecem condicionais |
| [[24_nuclear_phenomenology/index\|24 — Fenomenologia nuclear]] | alfa, camadas spin--torção, Klein--Nishina e neutrinos | notas e scripts do capítulo | [NuclearPhenomenology](../formal/GDQ/NuclearPhenomenology.lean) | meia-vida reduzida, números mágicos, limite Thomson, positividade do espectro neutro candidato e cota de oscilação formalizados; Hessianas e vértices 8D completos permanecem condicionais |
| [[25_astrophysics_cosmology/index\|25 — Astrofísica]] | sólitons com horizonte, cosmologia e normalizações globais | notas e scripts do capítulo | [GravityCosmology](../formal/GDQ/GravityCosmology.lean), [AstrophysicsCosmology](../formal/GDQ/AstrophysicsCosmology.lean) | core regular, rigidez torsional, Schur, temperatura, entropia de canais e normalizações formalizados; sela 8D, Page física e solver cosmológico único permanecem condicionais |
| [[26_logical_status/index\|26 — Estado lógico]] | axiomas, dados, teoremas, reduções e dependências | corpo do capítulo | [LogicalStatus](../formal/GDQ/LogicalStatus.lean), [ponto de entrada GDQ](../formal/GDQ.lean) | taxonomia, cadeia de previsão forte e redução controlada formalizadas; provas físicas permanecem nos módulos próprios |
| [[27_numeric_experimental_program/index\|27 — Programa numérico]] | reprodutibilidade e benchmarks | scripts autocontidos e nota formal | [NumericalProtocol](../formal/GDQ/NumericalProtocol.lean) | manifesto, classes numéricas, previsão cega, comparação forte e decomposição de erro formalizados; o protocolo não certifica backgrounds particulares |
| [[28_technical_faq/index\|28 — FAQ técnica]] | objeções, domínios e limites | corpo, notas e mapa de provas | [TechnicalFAQ](../formal/GDQ/TechnicalFAQ.lean) | condicionais, não fatoração do estado, Born versus evento, Perelman setorial e insuficiência de concordância numérica formalizados |

## 4. Núcleo formal da quantização

A cadeia formal vigente é:

$$
f
\longrightarrow
\rho(f),\,e^{i\operatorname{Im}f}
\longrightarrow
\text{fase circular}
\longrightarrow
\Delta S_R\in h\mathbb Z.
$$

Para problemas relativos de bordo:

$$
\widehat J_S
\longrightarrow
Q_S
\longrightarrow
\Delta I_{\rm red}=Q_S\Delta S_R
\longrightarrow
Q_S\Delta S_R\in h\mathbb Z.
$$

As provas humanas estão em:

- [[08_hilbert_quantization_uncertainty/notes/wallstrom_fibrado_linha_u1|Fibrado $U(1)$ e Wallstrom]];
- [[08_hilbert_quantization_uncertainty/notes/quantizacao_relativa_acao_exponenciada|Quantização relativa e ação exponenciada]];
- [[10_spin_statistics_pauli/notes/provas_lemas_definicoes|Spin, Hopf e meia-monodromia]].

## 5. Regra para novas migrações

Uma prova experimental só será promovida quando:

1. o enunciado coincidir com o estado vigente do manuscrito;
2. todas as hipóteses estiverem tipadas ou declaradas;
3. não houver `sorry`, `admit` ou axioma físico oculto;
4. o módulo compilar no pacote canônico;
5. a prova escrita permanecer autocontida;
6. o capítulo apontar para a nota humana e para o código canônico;
7. `memory.md` registrar o status e os limites.

[[index|← Sumário do manuscrito]]
