import GDQ.Spaces
import GDQ.LocalMeasure
import GDQ.Constitutive
import GDQ.BohmIdentity
import GDQ.RouthMadelung
import GDQ.Fields
import GDQ.FlowKernel
import GDQ.Admissibility
import GDQ.CausalContour
import GDQ.ClockHomomorphism
import GDQ.ActionDensity
import GDQ.ActionIntegration
import GDQ.GeometricInvariants
import GDQ.CoordinateGeometry
import GDQ.EuclideanOfficialAction
import GDQ.ControlledIntegrability
import GDQ.ComplexContourAction
import GDQ.VariationalHessian
import GDQ.PhysicalProjector
import GDQ.VariationalDynamics
import GDQ.OSReconstruction
import GDQ.OSReconstructedEvolution
import GDQ.CosmologicalFamily
import GDQ.GlobalLocalTransport
import GDQ.SpectralBridge
import GDQ.GlobalLocalSixLemmas
import GDQ.C3Application
import GDQ.C3ConcreteHessian
import GDQ.GaussianOfficialReduction
import GDQ.GaussianContourReduction
import GDQ.GaussianBulkDomination
import GDQ.GaussianCausalDomination
import GDQ.GaussianAdmissibleBackground
import GDQ.GaussianOfficialIntegrability
import GDQ.ConformalBismutTorsion
import GDQ.ConformalBismutConnection
import GDQ.ConformalBismutBackground
import GDQ.ConformalBismutInvariants
import GDQ.ConformalOfficialDensity
import GDQ.ConformalTorsionSaddle
import GDQ.ConformalTorsionHessian
import GDQ.ConformalTorsionProjectedHessian
import GDQ.ConformalTorsionConstraintTangent
import GDQ.PhaseQuantization
import GDQ.PhaseReconstruction
import GDQ.BoundaryPhaseQuantization
import GDQ.PhaseFirstVariation
import GDQ.NoetherPhaseCurrent
import GDQ.NoetherIdentity
import GDQ.StokesChargeBalance
import GDQ.SpinHopfMonodromy
import GDQ.CARPauli
import GDQ.SternGerlachProjectors
import GDQ.Uncertainty
import GDQ.FiniteBorn
import GDQ.MixedBornTrace
import GDQ.MeasurementAsymptotic
import GDQ.ClassicalApparatusResponse
import GDQ.ApparatusBornReadout
import GDQ.QNDBornBasins
import GDQ.SternGerlachSequential
import GDQ.SternGerlachInterface
import GDQ.DetectorDtNSchur
import GDQ.TransportInterference
import GDQ.SpinStatisticsConditional
import GDQ.AharonovBohmHolonomy
import GDQ.SagnacHolonomy
import GDQ.HolonomyPatchingStokes
import GDQ.CechChern
import GDQ.CechCohomology
import GDQ.HyperchargeDiophantine
import GDQ.KillingPoissonLie
import GDQ.YMSectorIsomorphism
import GDQ.AreaLawConditional
import GDQ.APSHopfBismut
import GDQ.GenerationJunction
import GDQ.CPRelaxation
import GDQ.PerelmanProductReduction
import GDQ.KoideGeometry
import GDQ.LeptonicHierarchy
import GDQ.MagneticResponse
import GDQ.BaryonicReduction
import GDQ.ElectroweakStability
import GDQ.GravityCosmology
import GDQ.HydrogenSpectrum
import GDQ.SimpleApplications
import GDQ.NuclearPhenomenology
import GDQ.AstrophysicsCosmology
import GDQ.LogicalStatus
import GDQ.NumericalProtocol
import GDQ.TechnicalFAQ
import GDQ.OfficialAction

/-!
Ponto de entrada da formalização da GDQ.

O primeiro estágio fixa somente:

* a distinção de tipos entre o bulk local e o espaço cosmológico;
* suas dimensões declaradas;
* a assinatura abstrata da ação oficial;
* a ponte global--local pelos seis lemas, com hipóteses explícitas.

Nenhuma equação fenomenológica é postulada neste estágio.
-/
