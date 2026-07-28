import Mathlib

namespace GDQ

/-!
# Born--bacias no setor QND gaussiano

Este módulo formaliza o núcleo finito exato da demonstração escrita no
Capítulo 9:

1. a condição QND é preservada pelo complemento de Schur;
2. históricos gaussianos normalizados definem uma mistura física;
3. os pesos condicionados permanecem normalizados;
4. a esperança de cada peso condicionado é o peso inicial;
5. se o histórico terminal é absorvido em um único canal, a medida da bacia
   desse canal coincide com o peso inicial.

A discretização finita dos históricos evita introduzir uma teoria informal
de integração estocástica. A passagem ao processo contínuo requer o teorema
analítico de convergência/martingal e a hipótese física de separação
assintótica declarados no manuscrito.
-/

open scoped BigOperators

section QNDAlgebra

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/--
Se o bloco do sistema e a correção produzida pela eliminação do aparelho
comutam com um projetor de canal, o complemento de Schur também comuta.
-/
theorem qnd_schur_commutes
    (systemBlock apparatusCorrection channel : E →ₗ[ℝ] E)
    (hSystem :
      systemBlock.comp channel = channel.comp systemBlock)
    (hApparatus :
      apparatusCorrection.comp channel =
        channel.comp apparatusCorrection) :
    (systemBlock - apparatusCorrection).comp channel =
      channel.comp (systemBlock - apparatusCorrection) := by
  ext x
  have hSystemAt := LinearMap.congr_fun hSystem x
  have hApparatusAt := LinearMap.congr_fun hApparatus x
  change
    systemBlock (channel x) = channel (systemBlock x)
    at hSystemAt
  change
    apparatusCorrection (channel x) =
      channel (apparatusCorrection x)
    at hApparatusAt
  change
    systemBlock (channel x) - apparatusCorrection (channel x) =
      channel (systemBlock x - apparatusCorrection x)
  rw [map_sub, hSystemAt, hApparatusAt]

/--
Comutação com os projetores e ortogonalidade entre canais anulam o bloco
fora da diagonal.
-/
theorem qnd_offDiagonal_eq_zero
    (effective channelI channelJ : E →ₗ[ℝ] E)
    (hComm : effective.comp channelJ = channelJ.comp effective)
    (hOrthogonal :
      channelI.comp channelJ = 0) :
    channelI.comp (effective.comp channelJ) = 0 := by
  ext x
  have hCommAt := LinearMap.congr_fun hComm x
  change
    effective (channelJ x) = channelJ (effective x)
    at hCommAt
  have hOrthogonalAt := LinearMap.congr_fun hOrthogonal (effective x)
  change channelI (channelJ (effective x)) = 0 at hOrthogonalAt
  change channelI (effective (channelJ x)) = 0
  rw [hCommAt]
  exact hOrthogonalAt

end QNDAlgebra

section FiniteHistories

variable
  {ι Ω : Type*}
  [Fintype ι] [DecidableEq ι]
  [Fintype Ω]

/--
Modelo finito dos históricos de saída de um aparelho QND gaussiano.

`prior i` é o peso espectral inicial do canal `i`.
`likelihood i ω` é a densidade normalizada do histórico `ω` condicionada ao
canal `i`. A positividade estrita da mistura exclui históricos de
probabilidade física nula do denominador bayesiano.
-/
structure FiniteQNDGaussianHistories (ι Ω : Type*)
    [Fintype ι] [Fintype Ω] where
  prior : ι → ℝ
  likelihood : ι → Ω → ℝ
  prior_nonneg : ∀ i, 0 ≤ prior i
  prior_sum_one : ∑ i, prior i = 1
  likelihood_nonneg : ∀ i ω, 0 ≤ likelihood i ω
  likelihood_sum_one : ∀ i, ∑ ω, likelihood i ω = 1
  mixture_pos :
    ∀ ω, 0 < ∑ i, prior i * likelihood i ω

namespace FiniteQNDGaussianHistories

/-- Densidade física da mistura de históricos. -/
noncomputable def mixture
    (M : FiniteQNDGaussianHistories ι Ω) (ω : Ω) : ℝ :=
  ∑ i, M.prior i * M.likelihood i ω

/-- Peso condicionado do canal `i` depois de observar o histórico `ω`. -/
noncomputable def posterior
    (M : FiniteQNDGaussianHistories ι Ω) (i : ι) (ω : Ω) : ℝ :=
  M.prior i * M.likelihood i ω / M.mixture ω

theorem mixture_pos'
    (M : FiniteQNDGaussianHistories ι Ω) (ω : Ω) :
    0 < M.mixture ω :=
  M.mixture_pos ω

theorem mixture_ne_zero
    (M : FiniteQNDGaussianHistories ι Ω) (ω : Ω) :
    M.mixture ω ≠ 0 :=
  ne_of_gt (M.mixture_pos' ω)

/--
Multiplicar o posterior pela densidade da mistura recupera exatamente a
contribuição conjunta do canal e do histórico.
-/
theorem mixture_mul_posterior
    (M : FiniteQNDGaussianHistories ι Ω) (i : ι) (ω : Ω) :
    M.mixture ω * M.posterior i ω =
      M.prior i * M.likelihood i ω := by
  rw [posterior]
  field_simp [M.mixture_ne_zero ω]

/-- Os pesos condicionados somam um para cada histórico físico. -/
theorem posterior_sum_one
    (M : FiniteQNDGaussianHistories ι Ω) (ω : Ω) :
    ∑ i, M.posterior i ω = 1 := by
  simp_rw [posterior]
  rw [← Finset.sum_div]
  change M.mixture ω / M.mixture ω = 1
  exact div_self (M.mixture_ne_zero ω)

/-- Cada peso condicionado é não negativo. -/
theorem posterior_nonneg
    (M : FiniteQNDGaussianHistories ι Ω) (i : ι) (ω : Ω) :
    0 ≤ M.posterior i ω := by
  unfold posterior
  exact div_nonneg
    (mul_nonneg (M.prior_nonneg i) (M.likelihood_nonneg i ω))
    (le_of_lt (M.mixture_pos' ω))

/--
Versão finita exata da propriedade de martingal: a esperança física do
posterior de cada canal é o seu peso inicial.
-/
theorem expected_posterior_eq_prior
    (M : FiniteQNDGaussianHistories ι Ω) (i : ι) :
    ∑ ω, M.mixture ω * M.posterior i ω = M.prior i := by
  simp_rw [M.mixture_mul_posterior]
  rw [← Finset.mul_sum]
  rw [M.likelihood_sum_one i, mul_one]

/-- Indicador do canal terminal selecionado pelo histórico. -/
def terminalIndicator (i outcome : ι) : ℝ :=
  if outcome = i then 1 else 0

/--
Uma realização absorvente associa a cada histórico um único registro e
identifica o posterior terminal com o indicador desse registro.
-/
structure AbsorbingReadout
    (M : FiniteQNDGaussianHistories ι Ω) where
  outcome : Ω → ι
  posterior_absorbs :
    ∀ i ω, M.posterior i ω = terminalIndicator i (outcome ω)

/-- Medida física da bacia terminal do canal `i`. -/
noncomputable def AbsorbingReadout.basinWeight
    {M : FiniteQNDGaussianHistories ι Ω}
    (R : AbsorbingReadout M) (i : ι) : ℝ :=
  ∑ ω, M.mixture ω * terminalIndicator i (R.outcome ω)

/--
Teorema Born--bacias finito: normalização dos históricos, conservação da
esperança e absorção em um registro implicam que a medida da bacia é o peso
espectral inicial.
-/
theorem AbsorbingReadout.basinWeight_eq_prior
    {M : FiniteQNDGaussianHistories ι Ω}
    (R : AbsorbingReadout M) (i : ι) :
    R.basinWeight i = M.prior i := by
  rw [AbsorbingReadout.basinWeight]
  have hAbsorb :
      (∑ ω,
        M.mixture ω * terminalIndicator i (R.outcome ω)) =
      ∑ ω, M.mixture ω * M.posterior i ω := by
    apply Finset.sum_congr rfl
    intro ω _
    rw [R.posterior_absorbs i ω]
  rw [hAbsorb]
  exact M.expected_posterior_eq_prior i

/-- As medidas de todas as bacias absorventes somam um. -/
theorem AbsorbingReadout.basinWeights_sum_one
    {M : FiniteQNDGaussianHistories ι Ω}
    (R : AbsorbingReadout M) :
    ∑ i, R.basinWeight i = 1 := by
  simp_rw [R.basinWeight_eq_prior]
  exact M.prior_sum_one

end FiniteQNDGaussianHistories

end FiniteHistories

section DiffusionGeometry

variable
  {ι α : Type*}
  [Fintype ι]
  [Fintype α]

/-- Sinal médio do aparelho condicionado aos pesos correntes. -/
noncomputable def qndMeanSignal
    (p : ι → ℝ) (signal : ι → α → ℝ) (a : α) : ℝ :=
  ∑ j, p j * signal j a

/-- Coeficiente de inovação do peso do canal `i`. -/
noncomputable def qndNoiseCoefficient
    (p : ι → ℝ) (signal : ι → α → ℝ) (i : ι) (a : α) : ℝ :=
  p i * (signal i a - qndMeanSignal p signal a)

/-- Um canal ausente permanece numa face do simplex. -/
theorem qndNoiseCoefficient_eq_zero_of_weight_eq_zero
    (p : ι → ℝ) (signal : ι → α → ℝ) (i : ι)
    (hi : p i = 0) :
    ∀ a, qndNoiseCoefficient p signal i a = 0 := by
  intro a
  simp [qndNoiseCoefficient, hi]

/--
Os coeficientes de inovação são tangentes ao simplex: sua soma sobre os
canais desaparece quando os pesos somam um.
-/
theorem qndNoiseCoefficient_sum_zero
    (p : ι → ℝ) (signal : ι → α → ℝ)
    (hp : ∑ i, p i = 1) (a : α) :
    ∑ i, qndNoiseCoefficient p signal i a = 0 := by
  simp_rw [qndNoiseCoefficient, mul_sub]
  rw [Finset.sum_sub_distrib]
  change
    qndMeanSignal p signal a -
      ∑ i, p i * qndMeanSignal p signal a = 0
  rw [← Finset.sum_mul, hp, one_mul, sub_self]

/-- Entrada da matriz de covariância dos pesos condicionados. -/
noncomputable def qndCovarianceEntry
    (p : ι → ℝ) (signal : ι → α → ℝ) (i j : ι) : ℝ :=
  ∑ a,
    qndNoiseCoefficient p signal i a *
      qndNoiseCoefficient p signal j a

/-- Cada coluna da covariância soma zero: o ruído preserva o simplex. -/
theorem qndCovarianceEntry_sum_zero
    (p : ι → ℝ) (signal : ι → α → ℝ)
    (hp : ∑ i, p i = 1) (j : ι) :
    ∑ i, qndCovarianceEntry p signal i j = 0 := by
  simp_rw [qndCovarianceEntry]
  rw [Finset.sum_comm]
  apply Finset.sum_eq_zero
  intro a _
  rw [← Finset.sum_mul]
  rw [qndNoiseCoefficient_sum_zero p signal hp a, zero_mul]

/--
Forma quadrática de Gram da covariância dos pesos condicionados.
-/
noncomputable def qndCovarianceQuadratic
    (p : ι → ℝ) (signal : ι → α → ℝ) (v : ι → ℝ) : ℝ :=
  ∑ a, (∑ i, v i * qndNoiseCoefficient p signal i a) ^ 2

/-- A covariância QND é positiva semidefinida por construção de Gram. -/
theorem qndCovarianceQuadratic_nonneg
    (p : ι → ℝ) (signal : ι → α → ℝ) (v : ι → ℝ) :
    0 ≤ qndCovarianceQuadratic p signal v := by
  exact Finset.sum_nonneg fun _ _ => sq_nonneg _

/--
Informação discriminante estacionária acumulada entre dois canais.
-/
noncomputable def stationaryPairInformation
    (signal : ι → α → ℝ) (i j : ι) (t : ℝ) : ℝ :=
  (t / 2) * ∑ a, (signal i a - signal j a) ^ 2

/--
Uma separação uniforme positiva dos sinais força crescimento ao menos linear
da informação acumulada.
-/
theorem stationaryPairInformation_lower_bound
    (signal : ι → α → ℝ) (i j : ι) (t ε : ℝ)
    (ht : 0 ≤ t)
    (hsep : ε ≤ ∑ a, (signal i a - signal j a) ^ 2) :
    (t / 2) * ε ≤ stationaryPairInformation signal i j t := by
  unfold stationaryPairInformation
  exact mul_le_mul_of_nonneg_left hsep (by positivity)

end DiffusionGeometry

end GDQ
