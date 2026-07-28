# Quantização da fase e pente de Dirac

## 1. Enunciado

O objetivo é separar rigorosamente duas etapas.

Primeiro, a fase física é circular:

$$
e^{iS_R/\hbar}\in U(1).
$$

Para o levantamento local linear $\chi(\theta)=\alpha\theta$, o fechamento
global em $\theta\sim\theta+2\pi$ exige:

$$
e^{i2\pi\alpha}=1.
$$

Logo:

$$
\alpha=n,
\qquad
n\in\mathbb Z,
$$

e:

$$
\oint_C dS_R
=
2\pi\hbar n
=
nh.
$$

Segundo, depois que os caracteres inteiros já foram selecionados, a análise
harmônica permite escrever formalmente:

$$
\sum_{n\in\mathbb Z}e^{in\theta}
=
2\pi\sum_{k\in\mathbb Z}\delta(\theta-2\pi k).
$$

Essa igualdade não é pontual. Ela vale como identidade de distribuições
periódicas.

## 2. O que foi provado em Lean

O módulo `GDQ/PhaseQuantization.lean` prova:

1. a fase inicial é a unidade;
2. o fechamento após uma volta é equivalente à integralidade de $\alpha$;
3. para um levantamento geral $\chi$, não necessariamente linear, a igualdade
   dos valores físicos nos extremos implica:

$$
\chi(2\pi)-\chi(0)=2\pi n;
$$

4. a circulação resultante é um múltiplo inteiro de $2\pi\hbar$;
5. para qualquer laço contínuo $\gamma:[0,1]\to U(1)$, o próprio Lean
   constrói um levantamento contínuo $\Gamma:[0,1]\to\mathbb R$ e prova:

$$
\Gamma(1)-\Gamma(0)=2\pi n;
$$

6. a condição de cociclo em uma interseção tripla produz:

$$
\lambda_{ab}+\lambda_{bc}+\lambda_{ca}=2\pi n_{abc};
$$

7. a fórmula de soma de Poisson vale rigorosamente para funções de Schwartz,
   usando o teorema correspondente da Mathlib.

Não há `axiom`, `sorry` ou `admit` no módulo.

## 3. Regularização pelo calor

Para evitar somas divergentes, introduz-se $\varepsilon>0$:

$$
D_\varepsilon(\theta)
=
\sum_{n\in\mathbb Z}
e^{-\varepsilon n^2}e^{in\theta}.
$$

Pela soma de Poisson:

$$
D_\varepsilon(\theta)
=
\sqrt{\frac{\pi}{\varepsilon}}
\sum_{k\in\mathbb Z}
\exp\left[
-\frac{(\theta-2\pi k)^2}{4\varepsilon}
\right].
$$

Ambos os lados são funções suaves para $\varepsilon>0$. No limite
$\varepsilon\downarrow0$, a família converge no sentido distribucional para:

$$
2\pi\sum_{k\in\mathbb Z}\delta(\theta-2\pi k).
$$

O script `scripts/verificar_pente_dirac_regularizado.py` compara as duas
representações com truncamentos independentes.

## 4. Status científico

- A quantização topológica da circulação está demonstrada no setor escalar
  regular para todo laço contínuo de fase global $U(1)$.
- A existência do levantamento já não é apenas hipótese: ela é construída em
  Lean pelo teorema de levantamento de caminhos da cobertura
  $\exp:\mathbb R\to U(1)$.
- A integralidade do cociclo de Čech levantado também está demonstrada.
  `GDQ.CechCohomology` constrói o complexo algébrico, prova
  $\delta_2\delta_1=0$, define $\check H^2=Z^2/B^2$, constrói
  `firstChernClass` e prova sua independência sob mudanças de levantamento.
- `GDQ.PhaseReconstruction` reconstrói a fase diretamente do potencial
  oficial `f`, prova $|\Psi(f)|^2=\rho(f)$ e obtém $\Delta S_R=nh$ para um
  laço admissível do próprio potencial.
- A soma de Poisson não é a origem da quantização; ela é sua representação
  harmônica.
- O pente de Dirac é rigoroso como distribuição ou como limite de uma família
  regularizada, não como soma pontual ordinária.
- Setores spinoriais não são consequência deste teorema escalar. A
  meia-monodromia da classe Hopf/spinorial foi formalizada separadamente em
  `GDQ.SpinHopfMonodromy`: a integral de Cauchy produz resíduo `1/2`,
  circulação `h/2` e holonomias `-1,+1`. A estatística fermiônica ainda exige
  a construção global adicional do capítulo de spin.
