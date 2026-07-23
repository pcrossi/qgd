---
title: "Checklist operacional — Capítulo 21"
---

# Checklist operacional — Capítulo 21

## 1. Enunciado

O capítulo responde:

1. como o ângulo CP forte relaxa sem postular partícula fundamental nova;
2. como a periodicidade topológica gera potencial global;
3. como a relaxação é provada por Lyapunov;
4. como comparar o resíduo CP com o limite de EDM do nêutron;
5. por que monopolo magnético pontual local não é ontologia fundamental;
6. como Hopf--Cauchy fornece meia-monodromia.

## 2. Construções preservadas

| Construção | Local | Status |
|---|---|---|
| $q_C=(8\pi^2)^{-1}{\rm Tr}(F_C\wedge F_C)$ | `21.1` | definição efetiva |
| $Q_C\in\mathbb Z$ e $\theta\sim\theta+2\pi$ | `21.1`, `21.3` | topológico |
| modo angular $\vartheta_B$ | `21.2` | estrutural |
| $V=\chi(1-\cos\theta)$ | `21.3` | potencial global periódico |
| $K_{\rm CP}^{\rm phys}=P_{\rm phys}\delta^2\mathcal S_{\rm GDQ}P_{\rm phys}$ | `21.3`, `21.9`, nota Hessiana | definição do canal físico |
| $\chi_{\rm top}^{\rm GDQ}=\langle\eta_B,K_{\rm CP}^{\rm phys}\eta_B\rangle$ | nota Hessiana | condicional ao background forte |
| fluxo $\dot\theta=-\kappa\chi\sin\theta$ | `21.4` | relaxação |
| $f_B$ como rigidez torsional | `21.5` | condicional à normalização |
| EDM residual | `21.6` | comparação conservadora |
| $\nabla\cdot(\nabla\times v)=0$ | `21.7` | identidade local |
| $\operatorname{Res}\Omega_S=1/2$ | `21.8` | meia-monodromia |

## 3. Hessiana, projetores e vínculos

A normalização metrológica do modo torsional deve vir de:

$$
K_{\rm tor}^{\rm phys}
=
P_{\rm phys}
\delta^2\mathcal S_{\rm GDQ}[\Phi_\ast]
P_{\rm phys}.
$$

O capítulo não afirma que $K_{\rm tor}^{\rm phys}$ completo já foi
diagonalizado. O valor de $f_B$ é classificado como rigidez geométrica proposta
e condicionado à extração canônica final.

## 4. Scripts incorporados

| Script | Saída | Resultado |
|---|---|---|
| `relaxacao_cp_torsional.py` | `saida_relaxacao_cp_torsional.md` | $f_B=6{,}442945228853\times10^{17}$ GeV, $m_B=8{,}837901608259\times10^{-12}$ eV |
| `periodicidade_cp_carga_inteira.py` | `saida_periodicidade_cp_carga_inteira.md` | invariância de $\exp(i\theta Q_C)$ sob $\theta\mapsto\theta+2\pi$ para $Q_C\in\mathbb Z$ |
| `hessiana_susceptibilidade_cp.py` | `saida_hessiana_susceptibilidade_cp.md` | Hessiana $+\chi$ no mínimo CP e $-\chi$ no máximo instável |
| `hopf_cauchy_residuo.py` | `saida_hopf_cauchy_residuo.md` | resíduo $1/2$, holonomia $-1$ |
| `monopolo_vorticidade.py` | `saida_monopolo_vorticidade.md` | divergência da vorticidade regular igual a zero |

Todos os scripts são autocontidos, comentados e geram Markdown.

## 5. Comparações

| Quantidade | Valor reduzido | Referência/comparação | Status |
|---|---:|---:|---|
| $f_B$ | $6{,}442945228853\times10^{17}$ GeV | escala axion-like alta | condicional |
| $m_B$ se houver polo | $8{,}837901608259\times10^{-12}$ eV | relação com $\chi_{\rm top}^{1/4}=75{,}46$ MeV | comparação |
| limite $|d_n|$ | relaxa para zero | $1{,}8\times10^{-26}\,e\,{\rm cm}$ | compatível |
| $\theta_{\rm residual}$ máximo | $4{,}736842105263\times10^{-11}$ | inferido do limite de EDM | comparação |

## 6. O que não foi guardado

Não foram incorporadas tentativas históricas que tratavam o potencial
quadrático como global, nem linguagem de áxion fundamental. O capítulo guarda
apenas a forma periódica, a relaxação por Lyapunov e a interpretação torsional.

## 7. Resultado editorial

O capítulo está fechado estruturalmente. Permanecem como refinamentos:

1. normalização canônica de $f_B$ pela Hessiana oficial;
2. susceptibilidade topológica calculada diretamente no background forte;
3. EDM residual com bordos, ruído e volume finito;
4. cosmologia quantitativa do modo torsional.
